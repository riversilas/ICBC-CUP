# -*- coding: utf-8 -*-
"""绿鉴 — 可信 ESG 数据平台（MVP）后端。

零第三方依赖：整个后端只使用 Python 标准库，拷贝到任何装了 Python 3.10+
的机器上都能直接运行，比赛现场不需要联网装包。

接口：
    GET  /                            前端页面
    GET  /static/<path>               静态资源
    GET  /api/companies               企业列表（含碳表现分，供 STEP 1 表格）
    GET  /api/company/<code>          单企业鉴证分析（STEP 2 / STEP 3 数据源）
    POST /api/attest/company/<code>   生成报告摘要并存证（STEP 3）
    GET  /api/verify/<digest>         存证查验（STEP 4）
    GET  /api/ledger                  调试：查看本地存证账本

术语边界（务必保留）：
    本系统输出的是「可验证的披露数据 + 存证状态」，不是第三方鉴证意见，
    也不是授信结论。链上记录只是防篡改存证，不等于官方认证。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import socket
import threading
import webbrowser
from datetime import datetime
from pathlib import Path

import carbon_model as CM
from miniserver import serve

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
STATIC_DIR = BASE_DIR / "static"
LEDGER_PATH = BASE_DIR / "chain_ledger.json"

DEFAULT_PORT = 8899
MODEL_VERSION = CM.MODEL_VERSION   # 单一真源：版本号只在 carbon_model.py 维护

_ledger_lock = threading.Lock()


# ==========================================================================
# 数据加载
# ==========================================================================
def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


COMPANIES = _load_json(DATA_DIR / "companies.json")["companies"]
BY_CODE = {c["code"]: c for c in COMPANIES}
ANNOUNCEMENTS = _load_json(DATA_DIR / "esg_announcements.json")

# 多年度碳数据台账（人工从各公司报告提取 + 交叉验证）
_LEDGER_FILE = DATA_DIR / "carbon_disclosure_ledger.json"
DISCLOSURE = _load_json(_LEDGER_FILE) if _LEDGER_FILE.exists() else {"companies": []}
CARBON_INPUT = {c["code"]: c for c in DISCLOSURE.get("companies", [])}

GROUPS = {
    "thermal": [c for c in COMPANIES if c["group"] == "thermal"],
    "clean": [c for c in COMPANIES if c["group"] == "clean"],
}
GROUP_LABEL = {"thermal": "火电组", "clean": "水电/新能源组"}


# ==========================================================================
# 第 1 步：碳核算（排放强度 = 范围一 + 范围二 ÷ 发电量）
# ==========================================================================
def median(values: list[float]) -> float:
    xs = sorted(values)
    n = len(xs)
    if n == 0:
        return 0.0
    mid = n // 2
    return float(xs[mid]) if n % 2 else (xs[mid - 1] + xs[mid]) / 2.0


def _carbon_inputs(code: str) -> dict | None:
    """把披露台账转成 carbon_model 需要的结构。没有年度数据的返回 None。"""
    raw = CARBON_INPUT.get(code)
    if not raw:
        return None
    years = {}
    for year, row in (raw.get("years") or {}).items():
        gen = row.get("power_gen_gwh")
        if not gen:
            continue  # 没有发电量就算不出强度，不猜
        s1, s2 = row.get("scope1_tco2"), row.get("scope2_tco2")
        if s1 is None and row.get("total_tco2e") is not None:
            s1, s2 = row["total_tco2e"], 0
        if s1 is None:
            continue
        years[year] = {"scope1_tco2": s1, "scope2_tco2": s2 or 0,
                       "power_gen_gwh": gen}
    return {
        "code": raw["code"], "name": raw["name"], "group": raw["group"],
        "assurance": raw.get("assurance", False), "years": years,
        "clean_energy_share_pct": raw.get("clean_energy_share_pct"),
        "clean_energy_share_basis": raw.get("clean_energy_share_basis"),
        # 雷达图维度：绿色投入由「绝对额 ÷ 总资本开支」现算，占比不预存，
        # 避免台账里出现与分子分母不一致的冗余数字。
        "green_capex_abs_yi": raw.get("green_capex_abs_yi"),
        "green_capex_total_yi": raw.get("green_capex_total_yi"),
        "green_capex_note": raw.get("green_capex_note", ""),
        "carbon_cost_share_pct": raw.get("carbon_cost_share_pct"),
        "carbon_cost_note": raw.get("carbon_cost_note", ""),
        "previous_year": raw.get("previous_year"),
        "note": raw.get("note", ""),
    }


def compute_metrics(code: str) -> dict:
    """演示用核算结果（单年度披露值），保持与原版字段一致。"""
    c = BY_CODE[code]
    peers = GROUPS[c["group"]]
    intensity = c["scope1_tco2"] / c["power_gen_gwh"]
    group_median = median([p["scope1_tco2"] / p["power_gen_gwh"] for p in peers])
    deviation = (intensity - group_median) / group_median * 100.0
    ordered = sorted((p["scope1_tco2"] / p["power_gen_gwh"], p["code"]) for p in peers)
    rank = [pc for _, pc in ordered].index(code) + 1
    return {
        "scope1_tco2": c["scope1_tco2"],
        "scope2_tco2": c["scope2_tco2"],
        "power_gen_gwh": c["power_gen_gwh"],
        "emission_intensity_tco2_per_gwh": round(intensity, 1),
        "group_median": round(group_median, 1),
        "deviation_pct": round(deviation, 1),
        "peer_rank": f"{rank}/{len(peers)}",
        "green_flag": intensity < group_median,
        "completeness_pct": c["completeness_pct"],
    }


# ==========================================================================
# 第 2 步：碳表现分（GreenTrace-Power V3.1）
# ==========================================================================
def carbon_payload(code: str) -> dict:
    """PCPS 碳表现分 + 全部中间量 + 数据可信度。数据不足时如实返回 available=False。"""
    c = BY_CODE[code]
    raw = CARBON_INPUT.get(code, {})
    inputs = _carbon_inputs(code)

    # 没有任何年度数据（例如纯水电企业只披露替代减排量、或企业拒披）：
    # 不臆测、不填 0，如实返回不可用，并保留已获得的清洁能源占比供展示。
    if inputs is None or not inputs["years"]:
        return {
            "available": False,
            "code": code, "name": c["name"], "group": c["group"],
            "group_label": GROUP_LABEL[c["group"]],
            "disclosure_status": raw.get("status", "pending"),
            "note": raw.get("note", ""),
            "clean_energy_share_pct": raw.get("clean_energy_share_pct"),
            "clean_energy_share_basis": raw.get("clean_energy_share_basis"),
            "missing": ["排放量或发电量未从公开报告提取到，无法复算度电碳排放强度"],
            "model_version": MODEL_VERSION,
        }

    years = sorted(int(y) for y in inputs["years"])
    year = max(years)
    r = CM.carbon_score(inputs, year)
    r["group_label"] = GROUP_LABEL[inputs["group"]]
    r["disclosure_status"] = raw.get("status", "unknown")
    r["ledger_note"] = raw.get("note", "")
    r["confidence_grade"] = CM.confidence_grade(inputs)
    r["credit"] = CM.credit_pricing(r["carbon_score"]) if r.get("carbon_score") is not None else None
    r["self_reported_intensity_g_per_kwh"] = raw.get("self_reported_intensity_g_per_kwh")
    if r["self_reported_intensity_g_per_kwh"]:
        r["self_reported_gap_pct"] = round(
            (r["ci_g_per_kwh"] / r["self_reported_intensity_g_per_kwh"] - 1) * 100, 1)
    r["baseline_version"] = f"{CM.BENCHMARK_LABEL} {year}"
    r["sources"] = raw.get("sources", [])
    # 五维雷达图：本年 vs 上一年，用于时序叠加对比
    r["radar"] = CM.radar_values(inputs, year)
    prev = CM.radar_prev_values(inputs, year)
    r["radar_prev"] = prev
    r["radar_prev_year"] = (year - 1) if prev else None
    # 银行风控结论：由五维雷达形态 + 等权综合分按固定规则生成，无人工核定，可复算
    r["verdict"] = CM.verdict_for(r["radar"], r["carbon_score"], r["weights_applied"])
    return r


def carbon_rows() -> list[dict]:
    """STEP 1 表格数据。

    列的设计原则：**企业识别 + 五维原始值**。
    STEP 2 的雷达是同一批数据折算成 0–100 分之后的形态，两者一一对应。
    数据可信度不属于五维，是"数据注记"，不在这里当指标列。
    """
    rows = []
    for c in COMPANIES:
        p = carbon_payload(c["code"])
        dim = {d["key"]: d for d in (p.get("radar") or [])}
        rows.append({
            "code": c["code"], "name": c["name"], "type": c["type"],
            "group_label": GROUP_LABEL[c["group"]],
            "available": p["available"],
            # ---- 五维原始值 ----
            "ci_g_per_kwh": p.get("ci_g_per_kwh"),                    # ① 存量能效
            "change_rate_pct": p.get("change_rate_pct"),              # ② 边际改善
            "green_capex_pct": (dim.get("green_capex") or {}).get("value"),             # ③ 绿色投入
            "clean_energy_share_pct": p.get("clean_energy_share_pct"),  # ④ 低碳结构
            "carbon_compliance_dev_pct": (dim.get("carbon_compliance") or {}).get("value"),  # ⑤ 碳合规
            # ---- 结果与注记 ----
            "carbon_score": p.get("carbon_score"),
            "rating": p.get("rating"),
            "data_coverage": p.get("data_coverage"),
            "confidence_grade": p.get("confidence_grade"),
            "disclosure_status": p.get("disclosure_status"),
        })
    rows.sort(key=lambda r: (not r["available"],
                             -(r["carbon_score"] if r["carbon_score"] is not None else -1)))
    return rows


# ==========================================================================
# 第 3 / 4 步：存证与查验
# ==========================================================================
def read_ledger() -> list[dict]:
    if not LEDGER_PATH.exists():
        return []
    try:
        data = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def write_ledger(records: list[dict]) -> None:
    LEDGER_PATH.write_text(json.dumps(records, ensure_ascii=False, indent=1),
                           encoding="utf-8")


def attest(code: str) -> dict:
    """对五维绿色信用评级结果生成 SHA256 摘要并写入本地存证账本。

    上链内容设计（对应三个不可替代作用）：
      1. `radar_coordinates` —— 五维坐标数组，**整体哈希**，防"拆东墙补西墙"的局部篡改；
      2. `rating` —— 唯一的评级依据（五维雷达核定），与前端展示严格一致；
      3. `model_version` / `baseline_version` —— 版本元数据，模型升级时生成新凭证不覆盖旧凭证。

    防跨期伪造的用法：本年度凭证一旦上链即锁定时间戳，次年计算"边际改善"
    时调链上同期坐标作基准，企业无法通过篡改历史账本伪造减排加速度。

    竞赛阶段用本地账本模拟链上存证；接入 FISCO BCOS 时只需把 write_ledger
    换成链上 SDK 调用，摘要算法与上链字段都不用改。
    """
    carbon = carbon_payload(code)
    radar = carbon.get("radar") or []
    verdict = carbon.get("verdict") or {}
    payload = {
        "company": code,
        "company_name": carbon.get("name"),
        "reporting_year": carbon.get("year"),
        "radar_coordinates": [
            {"key": d["key"], "label": d["label"], "score": d["score"]} for d in radar
        ],
        "rating": verdict.get("rating"),
        "rating_label": verdict.get("label"),
        "risk_action": verdict.get("action"),
        "weights": CM.RADAR_WEIGHTS,
        "weights_note": CM.RADAR_WEIGHTS_NOTE,
        "model_version": MODEL_VERSION,
        "baseline_version": carbon.get("baseline_version"),
        "data_coverage": carbon.get("data_coverage"),
        "confidence_grade": carbon.get("confidence_grade"),
    }
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True,
                           separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    with _ledger_lock:
        ledger = read_ledger()
        record = {
            "digest": digest,
            "type": "green_credit_rating",
            "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "tx": f"local-{len(ledger) + 1:06d}",
            "payload": payload,
        }
        ledger.append(record)
        write_ledger(ledger)
    return record


def verify(digest: str) -> dict:
    """存证查验：不只要找到记录，还要用存储的 payload 重算摘要做比对。

    V3.1 的实现只做字符串查找（digest 在不在文件里），无法发现账本自身被改：
    只要 digest 字段不动，把 payload 里的评级改成 AAA 也照样"查验通过"。
    V3.2 改为重算 SHA256 并与记录比对，并单独报告 payload 完整性。
    """
    digest = (digest or "").strip().lower()
    if not digest:
        return {"valid": False, "payload_intact": None, "recomputed_digest": None,
                "record": None, "message": "未提供存证摘要。"}
    with _ledger_lock:
        ledger = read_ledger()
    for record in ledger:
        stored = record.get("digest")
        if not stored or stored.lower() != digest:
            continue
        recomputed = hashlib.sha256(
            json.dumps(record.get("payload"), ensure_ascii=False,
                       sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        intact = (recomputed == stored)
        return {
            "valid": True,
            "payload_intact": intact,
            "recomputed_digest": recomputed,
            "record": record,
            "message": ("存证存在，用存证内容重算的摘要与链上记录一致，未被篡改。"
                        if intact else
                        "存证存在，但用存证内容重算的摘要与链上记录不一致——"
                        "账本记录本身已被修改。"),
        }
    return {"valid": False, "payload_intact": None, "recomputed_digest": None,
            "record": None,
            "message": "未找到匹配存证。若企业提交的报告被篡改过，其摘要将无法匹配链上记录。"}


def tamper_demo(digest: str) -> dict:
    """篡改试验：把已存证内容改写一位，看摘要如何变化。**不修改账本**。

    这是语义正确的演示——企业若篡改报告内容，重新计算的摘要必然对不上
    链上记录。V3.1 的演示只是把摘要字符串改一位，说明力弱得多。
    """
    digest = (digest or "").strip().lower()
    with _ledger_lock:
        ledger = read_ledger()
    hit = next((r for r in ledger if (r.get("digest") or "").lower() == digest), None)
    if hit is None:
        return {"error": "未找到该存证摘要"}

    original = hit.get("payload") or {}
    tampered = json.loads(json.dumps(original))     # 深拷贝
    changes = []
    if tampered.get("rating") not in (None, "AAA"):
        changes.append(f"评级 {tampered['rating']} → AAA")
        tampered["rating"] = "AAA"
        tampered["rating_label"] = "纯绿标杆资产"
    elif tampered.get("radar_coordinates"):
        first = tampered["radar_coordinates"][0]
        old = first.get("score")
        first["score"] = round(min(100.0, (old or 0) + 20.0), 1)
        changes.append(f"{first.get('label')} 得分 {old} → {first['score']}")

    fake_digest = hashlib.sha256(
        json.dumps(tampered, ensure_ascii=False, sort_keys=True,
                   separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return {
        "original_digest": hit.get("digest"),
        "tampered_digest": fake_digest,
        "changes": changes,
        "matches_ledger": fake_digest == hit.get("digest"),
        "note": "篡改后的内容会得到完全不同的摘要，链上记录中不存在该摘要，查验必然失败。",
    }


# ==========================================================================
# 路由（标准 WSGI application）
# ==========================================================================
def _json_response(obj, status: int = 200):
    body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
    return status, [("Content-Type", "application/json; charset=utf-8"),
                    ("Content-Length", str(len(body)))], [body]


def _file_response(path: Path, fallback_type: str = "application/octet-stream"):
    if not path.is_file():
        return _json_response({"error": "not found", "path": str(path.name)}, 404)
    body = path.read_bytes()
    ctype = mimetypes.guess_type(path.name)[0] or fallback_type
    if path.suffix == ".html":
        ctype = "text/html; charset=utf-8"
    if path.suffix == ".json":
        ctype = "application/json; charset=utf-8"
    return 200, [("Content-Type", ctype),
                 ("Content-Length", str(len(body))),
                 ("Cache-Control", "no-store")], [body]


def application(environ, start_response):
    method = environ.get("REQUEST_METHOD", "GET")
    path = environ.get("PATH_INFO", "/") or "/"
    parts = [p for p in path.split("/") if p]

    try:
        if path == "/" or path == "/index.html":
            status, headers, body = _file_response(STATIC_DIR / "index.html")

        elif path in ("/app", "/app/"):
            status, headers, body = _file_response(STATIC_DIR / "app.html")

        elif parts[:1] == ["static"]:
            rel = Path(*parts[1:])
            target = (STATIC_DIR / rel).resolve()
            if STATIC_DIR.resolve() not in target.parents:
                status, headers, body = _json_response({"error": "forbidden"}, 403)
            else:
                status, headers, body = _file_response(target)

        elif path == "/api/companies":
            status, headers, body = _json_response({
                "count": len(COMPANIES),
                "companies": [dict({"code": c["code"], "name": c["name"],
                                    "type": c["type"],
                                    "reports_count": len(ANNOUNCEMENTS.get(c["code"], {}).get("reports", []))},
                                   **compute_metrics(c["code"])) for c in COMPANIES],
            })

        elif path == "/api/carbon":
            status, headers, body = _json_response({
                "model_version": MODEL_VERSION,
                "baseline": {str(k): v for k, v in CM.BENCHMARK_TCO2_PER_MWH.items()},
                "weights": CM.RADAR_WEIGHTS,
                "count": len(COMPANIES),
                "rows": carbon_rows(),
            })

        elif len(parts) == 3 and parts[:2] == ["api", "company"]:
            code = parts[2]
            if code not in BY_CODE:
                status, headers, body = _json_response(
                    {"error": "unknown company", "code": code}, 404)
            else:
                payload = company_payload(code)
                status, headers, body = _json_response(payload)

        elif len(parts) == 4 and parts[:2] == ["api", "attest"] and parts[2] == "company":
            code = parts[3]
            if method != "POST":
                status, headers, body = _json_response({"error": "POST required"}, 405)
            elif code not in BY_CODE:
                status, headers, body = _json_response(
                    {"error": "unknown company", "code": code}, 404)
            else:
                status, headers, body = _json_response(attest(code))

        elif len(parts) == 3 and parts[:2] == ["api", "verify"]:
            status, headers, body = _json_response(verify(parts[2]))

        elif len(parts) == 4 and parts[:3] == ["api", "demo", "tamper"]:
            status, headers, body = _json_response(tamper_demo(parts[3]))

        elif path == "/api/ledger":
            records = read_ledger()
            status, headers, body = _json_response(
                {"count": len(records), "records": records})

        else:
            status, headers, body = _json_response(
                {"error": "not found", "path": path}, 404)

    except Exception as exc:  # 演示环境：任何异常都返回 JSON，避免页面白屏
        status, headers, body = _json_response(
            {"error": "internal error", "detail": repr(exc)}, 500)

    start_response(f"{status} {'OK' if status == 200 else 'Error'}",
                   [(k, v) for k, v in headers])
    return body


def company_payload(code: str) -> dict:
    """STEP 2 / STEP 3 的完整数据。

    2026-10-16 起移除前台从未消费的旧口径字段（metrics 三维演示核算、
    peers/peer_group 同强度对照），API 契约与现行 V3.2 展示保持单一口径。
    """
    c = BY_CODE[code]
    reports = ANNOUNCEMENTS.get(code, {}).get("reports", [])
    return {
        "code": c["code"], "name": c["name"], "type": c["type"],
        "carbon": carbon_payload(code),
        "scoring_method": scoring_method(),
        "evidence": build_evidence(code),
        "reports_count": len(reports),
        "reports": reports,
    }


def scoring_method() -> dict:
    """对外披露的算法口径。与 carbon_model.py 的常量同源，避免文档与代码再次分叉。"""
    bench = "、".join(f"{y} 年 {v * 1000:.0f}"
                      for y, v in sorted(CM.BENCHMARK_TCO2_PER_MWH.items()))
    return {
        "model_version": MODEL_VERSION,
        "intensity": "I =（范围一 + 范围二）÷ 全口径发电量，单位 gCO₂/kWh",
        "trend": "τ =（I 今年 − I 去年）÷ I 去年；不足两年时用多年度等效年化变化率",
        "structure_raw": "ρ = 控股清洁能源装机容量占比（年报 / ESG 报告披露值）",
        "dims": [
            {"label": "① 存量能效",
             "formula": f"S① =（{CM.INTENSITY_SCALE_MAX:.0f} − I）÷ 10，限定 [0, 100]"},
            {"label": "② 边际改善",
             "formula": f"S② = 50 + 50 × tanh(−{CM.TANH_K:g} × τ)"},
            {"label": "③ 绿色投入强度",
             "formula": f"S③ = 100 × 环保节能投入 ÷ 现金流总资本开支 ÷ "
                        f"{CM.GREEN_CAPEX_FULL_MARK:g}，上限 100"},
            {"label": "④ 低碳结构", "formula": "S④ = 清洁能源装机占比，直接对应百分比"},
            {"label": "⑤ 碳合规与边际收益",
             "formula": f"S⑤ = 50 +（基准线 − I）÷ 基准线 × 100，限定 [0, 100]"},
        ],
        "composite": "综合分 S = 五维等权平均（每维 20%）："
                     "S = 0.20×(S①+S②+S③+S④+S⑤)",
        "weights_note": CM.RADAR_WEIGHTS_NOTE,
        "missing_rule": "缺失维度不臆测、不计 0 分；其权重在剩余可得维度上重新归一化",
        "rating_rule": "评级由综合分查固定档位表判定，无人工干预："
                       + "，".join(f"≥{f} 为 {n}" for f, n, _ in CM.RATING_BANDS),
        "baseline": f"{CM.BENCHMARK_LABEL}（gCO₂/kWh）：{bench}",
        "credit": f"信贷联动：Δr = −(S − {CM.CREDIT_THRESHOLD:g}) × "
                  f"{CM.CREDIT_BP_PER_POINT:g} BP（高于 {CM.CREDIT_THRESHOLD:g} 分下浮利率）",
        "disclaimer": "评分为样本内相对比较，非绝对评级；不构成第三方鉴证意见，不构成授信结论。",
    }


def build_evidence(code: str) -> list[dict]:
    name = BY_CODE[code]["name"]
    raw = CARBON_INPUT.get(code, {})
    items = [
        {"field": "scope1_tco2 / scope2_tco2", "source": f"{name} 年度报告及 ESG 报告披露",
         "note": "披露值，来源已索引"},
        {"field": "power_gen_gwh", "source": f"{name} 年度报告 / ESG 报告披露",
         "note": "全口径发电量，作为强度分母"},
        {"field": "intensity", "source": "平台复算 =（范围一 + 范围二）÷ 发电量",
         "note": "统一口径；tCO₂/GWh 数值上等于 gCO₂/kWh"},
    ]
    if raw.get("clean_energy_share_pct") is not None:
        items.append({
            "field": "clean_energy_share",
            "source": raw.get("clean_energy_share_source", "企业 ESG 报告披露"),
            "note": f"口径：{raw.get('clean_energy_share_basis', '未注明')}，"
                    f"用于结构维度打分（权重 0.25）",
        })
    if raw.get("self_reported_intensity_g_per_kwh"):
        items.append({
            "field": "企业自报排放强度",
            "source": "企业报告原文",
            "note": "分子为全公司排放、分母为火电发电量；与统一口径不可直接比较",
        })
    return items


# ==========================================================================
# 启动
# ==========================================================================
def lan_ip() -> str:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return "127.0.0.1"


def main() -> None:
    parser = argparse.ArgumentParser(description="绿鉴 — 可信 ESG 数据平台（MVP）")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--lan", action="store_true", help="开放局域网访问（手机演示）")
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--verbose", action="store_true", help="打印访问日志")
    args = parser.parse_args()

    host = "0.0.0.0" if args.lan else "127.0.0.1"
    url = f"http://127.0.0.1:{args.port}"

    print("=" * 60)
    print("  绿鉴 — 可信 ESG 数据平台（MVP）  " + MODEL_VERSION)
    print("=" * 60)
    print(f"  本机访问 : {url}")
    if args.lan:
        print(f"  手机访问 : http://{lan_ip()}:{args.port}   （需同一 WiFi）")
    print(f"  存证账本 : {LEDGER_PATH}")
    print(f"  碳数据台账: {_LEDGER_FILE.name}"
          f"（{len(CARBON_INPUT)} 家，其中可复算 "
          f"{sum(1 for c in COMPANIES if carbon_payload(c['code'])['available'])} 家）")
    print("  停止服务 : Ctrl + C")
    print("=" * 60)

    if not args.no_browser:
        threading.Timer(1.2, lambda: webbrowser.open(url)).start()
    serve(application, host=host, port=args.port, verbose=args.verbose)


if __name__ == "__main__":
    main()
