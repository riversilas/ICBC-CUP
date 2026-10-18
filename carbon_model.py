# -*- coding: utf-8 -*-
"""绿鉴 · 电力企业绿色信用模型 V3.2（等权五维雷达）

设计原则（P0 重构后）
--------------------------------------------------------------------------
1. **只有一个模型**。V3.1 之前同时存在「PCPS 三维综合分」与「五维雷达」两套
   打分口径，参数还不一致（强度标尺 900 vs 1000），导致同一家企业在 STEP1
   与 STEP2 显示两个不同评级。V3.2 删除 PCPS 三维，只保留五维雷达。

2. **评级必须可复算**。V3.1 的评级来自 `RISK_VERDICTS` 人工写死的字典，
   任何公式都复现不出来——这与平台"可复算、可溯源"的立论直接冲突。
   V3.2 的评级 = 五维等权综合分 → 查固定档位表，纯公式，无人工干预。

3. **权重必须真参与计算**。V3.1 声明了 `RADAR_WEIGHTS` 却不使用，还把
   structure / carbon_compliance 写成 0.0，与风控结论里大谈结构轴自相矛盾。
   V3.2 采用**等权固定权重（每维 20%）**——在没有先验证据说明哪一维更能
   预测信用风险时，等权是最透明的中性基准，且一句话能讲清：
   「综合分就是五个轴的平均高度」。

4. **缺失维度不臆测、不计 0**。权重在剩余可得维度上重新归一化。

--------------------------------------------------------------------------
与 V3.1 的参数差异（全部收敛为一套）
--------------------------------------------------------------------------
| 参数 | V3.1 | V3.2 |
|---|---|---|
| 强度标尺上限 | PCPS 900 / 雷达 1000 两套 | **1000**（唯一） |
| 碳合规基准线 | `NATIONAL_BENCHMARK` 750 | **全国碳市场发电行业基准线**（按年度，820–823） |
| 趋势灵敏度 k | 代码 10 / 文档 5 | **5**（采用 `算法说明` 中已论证的取值） |
| 维度权重 | 0.40/0.35/0.25/0/0 且不参与计算 | **等权 0.20 × 5，真参与计算** |
| 评级来源 | `RISK_VERDICTS` 人工字典 | **公式产生** |
| 全绿豁免 | 强度 ≤50 则强制 ≥95 分 | **已删除**（人工兜底，破坏可复算性） |
"""

from __future__ import annotations

import json
import math
from pathlib import Path

MODEL_VERSION = "GreenTrace-Power V3.2 (等权五维雷达)"

# ---------------------------------------------------------------------------
# 1. 五维定义（唯一一套模型）
# ---------------------------------------------------------------------------
RADAR_DIMS = [
    {"key": "intensity", "short": "存量能效", "label": "① 存量能效",
     "unit": "gCO₂/kWh", "desc": "度电碳排放强度，反映机组技术是否先进"},
    {"key": "trend", "short": "边际改善", "label": "② 边际改善",
     "unit": "%", "desc": "碳强度年度变化率，负=减排；转型金融的核心看点"},
    {"key": "green_capex", "short": "绿色投入", "label": "③ 绿色投入强度",
     "unit": "%", "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入"},
    {"key": "structure", "short": "低碳结构", "label": "④ 低碳结构",
     "unit": "%", "desc": "控股清洁能源装机容量占比，长期结构韧性"},
    {"key": "carbon_compliance", "short": "碳合规承压", "label": "⑤ 碳合规与边际收益",
     "unit": "%", "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压"},
]

# ---- 归一化标尺（唯一一套） ----
INTENSITY_SCALE_MAX = 1000.0     # 维度 ①：0 gCO₂/kWh 得 100 分，1000 得 0 分
GREEN_CAPEX_FULL_MARK = 5.0      # 维度 ③：绿色投入占 CAPEX 达 5.0% 得满分
TANH_K = 5.0                     # 维度 ②：趋势项灵敏度（见下方说明）

# 全国碳市场发电行业基准线（tCO₂/MWh）。维度 ⑤ 用它判定配额结余 / 缺口。
# 注：该值应按生态环境部每年公布的发电行业基准线逐年更新，此处为已核验的年度值。
BENCHMARK_TCO2_PER_MWH = {2022: 0.823, 2023: 0.820, 2024: 0.820}
BENCHMARK_LABEL = "全国碳市场发电行业基准线"
BENCHMARK_DEFAULT = 0.820

# ---- 权重：等权固定，且真参与计算 ----
# 等权理由：在缺乏「哪一维更能预测信用风险」的实证证据前，等权是最透明的
# 中性基准，且易于解释（综合分 = 五个轴的平均高度）。待 P3 做敏感性分析
# （等权 / 风险加权 / 主成分）后再决定是否调整。
RADAR_WEIGHTS = {d["key"]: 0.20 for d in RADAR_DIMS}
RADAR_WEIGHTS_NOTE = (
    "等权固定权重，每维 20%，真实参与综合分计算。"
    "选择等权是因为尚无实证证据表明某一维对信用风险的预测力更强；"
    "等权是可复算、可审计的中性基准。"
)

# 趋势项 k 的取值说明：原方案建议 k=15 太灵敏（火电企业年度强度变化普遍在
# ±3% 以内，k=15 会把正常波动放大成极端分数）。本模型取 **k=5**，使 ±5% 的
# 年度变化对应约 12 分分差，贴合电力行业实际波动幅度。k 属待校准参数，
# 应在 P3 阶段做 k=3/5/8 的敏感性测试，验证企业排序是否稳定。

# ---------------------------------------------------------------------------
# 2. 评级档位（唯一评级依据：综合分查此表，无人工干预）
# ---------------------------------------------------------------------------
RATING_BANDS = [
    (90, "AAA", "纯绿标杆资产"),
    (80, "AA", "优质绿色资产"),
    (70, "A", "绿色资产"),
    (60, "B+", "转型支持资产"),
    (45, "B", "传统火电转型期"),
    (30, "B-", "碳配额承压资产"),
    (0, "C", "高碳待整改资产"),
]

# 银行动作：按档位规则给出，不再人工逐家编写
RATING_ACTIONS = {
    "AAA": "建议执行最优档优惠利率，纳入绿色资产标杆池",
    "AA": "建议利率下浮，纳入绿色信贷优先支持名单",
    "A": "建议利率适度下浮，按年度复核",
    "B+": "可给予转型支持利率；建议挂钩下年度降碳 KPI",
    "B": "平价发放；建议建立季度碳强度跟踪",
    "B-": "不享受降息；建议开立节能改造专项监管账户",
    "C": "建议利率上浮并纳入重点管控名单",
}

CREDIT_THRESHOLD = 60.0          # Δr 的分界分
CREDIT_BP_PER_POINT = 1.0        # 每分对应 1 BP


# ---------------------------------------------------------------------------
# 3. 基础量
# ---------------------------------------------------------------------------
def intensity(company: dict, year: int) -> float:
    """度电碳排放强度 I_t =（范围一 + 范围二）÷ 全口径发电量，单位 gCO₂/kWh。

    单位换算：tCO₂/GWh 数值上恰好等于 gCO₂/kWh
    （1 t = 10⁶ g，1 GWh = 10⁶ kWh），因此直接相除即可，不要乘 1000。
    """
    row = company["years"][str(year)]
    return (row["scope1_tco2"] + row["scope2_tco2"]) / row["power_gen_gwh"]


def available_years(company: dict) -> list[int]:
    return sorted(int(y) for y in company["years"])


def change_rate(company: dict, year: int) -> tuple[float | None, str]:
    """碳强度变化率 τ（正=反弹，负=下降），返回 (变化率, 口径说明)。

    优先用同比；不足两年时退回「多年度等效年化」（对单年波动更稳健）。
    """
    years = available_years(company)
    if year - 1 in years:
        prev = intensity(company, year - 1)
        if prev > 0:
            return (intensity(company, year) - prev) / prev, "同比"
    past = [y for y in years if y < year]
    if past:
        base_year = past[0]
        span = year - base_year
        if span > 0:
            base = intensity(company, base_year)
            if base > 0:
                return (intensity(company, year) / base) ** (1.0 / span) - 1.0, \
                       f"{base_year}–{year} 年化"
    return None, "无历史数据"


def benchmark_g_per_kwh(year: int) -> float:
    """该年度的全国碳市场发电行业基准线，单位 gCO₂/kWh。"""
    return BENCHMARK_TCO2_PER_MWH.get(year, BENCHMARK_DEFAULT) * 1000.0


# ---------------------------------------------------------------------------
# 4. 五个维度的打分函数（唯一一套）
# ---------------------------------------------------------------------------
def score_dim1_intensity(ci: float) -> float:
    """维度 ① 存量能效：逆向归一化 S = (1000 − 强度) ÷ 10，限定 [0, 100]。"""
    return max(0.0, min(100.0, (INTENSITY_SCALE_MAX - ci) / 10.0))


def score_trend(tau: float) -> float:
    """维度 ② 边际改善：S = 50 + 50·tanh(−k·τ)。

    τ=0 得 50 分；减排得高分，反弹得低分。tanh 让分数自然收敛于 [0,100]：
    减排再猛也不爆表，反弹再大也不出负分，两端平滑。
    """
    return 50.0 + 50.0 * math.tanh(-TANH_K * tau)


def score_dim3_green_capex(pct: float) -> float:
    """维度 ③ 绿色投入强度：正向线性，5.0% 得满分。"""
    return max(0.0, min(100.0, 100.0 * pct / GREEN_CAPEX_FULL_MARK))


def score_dim4_structure(pct: float) -> float:
    """维度 ④ 低碳结构：清洁能源装机占比直接对应得分。"""
    return max(0.0, min(100.0, pct))


def carbon_compliance_deviation(ci: float, year: int) -> float:
    """维度 ⑤ 原始值：较全国碳市场基准线的偏离度，(基准 − 强度) ÷ 基准，%。"""
    b = benchmark_g_per_kwh(year)
    return (b - ci) / b * 100.0


def score_dim5_compliance(dev_pct: float) -> float:
    """维度 ⑤ 打分：50 分为配额平衡点。

    正偏离（强度优于基准、配额结余）从 50 加分至 100；
    负偏离（强度差于基准、配额缺口）从 50 扣分至 0。线性、正负对称。
    """
    return max(0.0, min(100.0, 50.0 + dev_pct))


# ---------------------------------------------------------------------------
# 5. 综合分与评级（纯公式）
# ---------------------------------------------------------------------------
def _renormalize(available: dict[str, float]) -> dict[str, float]:
    """缺失处理：可得维度的权重重新归一化（不臆测、不计 0 分）。"""
    total = sum(available.values())
    if total <= 0:
        return {}
    return {k: v / total for k, v in available.items()}


def composite_from_radar(radar: list[dict]) -> tuple[float | None, dict[str, float]]:
    """等权五维综合分 = 各可得维度得分的加权平均（权重重新归一化）。

    返回 (综合分, 实际生效权重)。全部维度缺失时综合分为 None。
    """
    scores = {d["key"]: d["score"] for d in radar
              if d.get("available") and d.get("score") is not None}
    if not scores:
        return None, {}
    w = _renormalize({k: RADAR_WEIGHTS[k] for k in scores})
    return sum(scores[k] * w[k] for k in w), w


def rating_of(score: float | None) -> tuple[str | None, str]:
    """综合分 → 评级档位。这是唯一的评级来源。"""
    if score is None:
        return None, "无法评级"
    for floor, name, label in RATING_BANDS:
        if score >= floor:
            return name, label
    return "C", "高碳待整改资产"


def verdict_for(radar: list[dict], score: float | None,
                weights: dict[str, float]) -> dict | None:
    """由五维雷达形态生成银行风控结论——全部字段可复算，无人工核定。

    返回 {rating, label, action, reason, score, weights_applied, computable}
    """
    if score is None:
        return None
    rating, label = rating_of(score)
    avail = [d for d in radar if d.get("available") and d.get("score") is not None]
    if not avail:
        return None

    best = max(avail, key=lambda d: d["score"])
    worst = min(avail, key=lambda d: d["score"])
    below = sorted([d for d in avail if d["score"] < 50.0], key=lambda d: d["score"])
    above = sorted([d for d in avail if d["score"] >= 50.0],
                   key=lambda d: -d["score"])
    missing = [d["label"] for d in radar if not d.get("available")]

    w_txt = "、".join(f"{d['short']} {weights[d['key']] * 100:.0f}%" for d in avail)
    parts = [
        f"综合分 {score:.1f} 分（等权五维平均；实际生效 {len(avail)} 维，"
        f"权重重新归一化后为 {w_txt}）"
    ]
    parts.append(f"最强轴 {best['label']} {best['score']:.1f} 分；"
                 f"最弱轴 {worst['label']} {worst['score']:.1f} 分。")
    if above:
        parts.append("优势轴：" + "、".join(
            f"{d['label']} {d['score']:.1f}" for d in above) + "。")
    if below:
        parts.append("承压轴（低于 50 分）：" + "、".join(
            f"{d['label']} {d['score']:.1f}" for d in below) + "。")
    if missing:
        parts.append("未取得数据的维度：" + "、".join(missing) +
                     "（不臆测、不计 0 分，权重已在剩余维度上重新归一化）。")
    parts.append(f"评级由综合分按固定档位表判定（≥{RATING_BANDS[3][0]} 为 B+，"
                 f"≥{RATING_BANDS[4][0]} 为 B，≥{RATING_BANDS[5][0]} 为 B−），可独立复算。")

    return {
        "rating": rating,
        "label": label,
        "action": RATING_ACTIONS.get(rating, "—"),
        "reason": "".join(parts),
        "score": round(score, 1),
        "weights_applied": {k: round(v, 3) for k, v in weights.items()},
        "computable": True,
    }


# ---------------------------------------------------------------------------
# 6. 单企业完整结果（供 API 与上链使用）
# ---------------------------------------------------------------------------
def carbon_score(company: dict, year: int) -> dict:
    """输出一家企业的综合分、五维子分与全部中间量，便于上链与复核。"""
    years = available_years(company)
    if not years:
        # 没有任何可复算的排放/发电量数据（例如纯水电企业只披露替代减排量）。
        # 不臆测、不填 0，如实返回不可用。
        return {
            "code": company["code"], "name": company["name"],
            "group": company["group"], "year": year,
            "model_version": MODEL_VERSION,
            "available": False,
            "ci_g_per_kwh": None, "change_rate_pct": None,
            "clean_energy_share_pct": company.get("clean_energy_share_pct"),
            "score_intensity": None, "score_trend": None,
            "score_green_capex": None, "score_structure": None,
            "score_carbon_compliance": None,
            "weights_applied": {}, "carbon_score": None,
            "rating": None, "rating_label": "无法评级",
            "missing": ["intensity", "trend"],
            "data_coverage": 0, "years_used": [],
            "note": company.get("note", ""),
        }

    ci = intensity(company, year)
    tau, tau_basis = change_rate(company, year)
    radar = radar_values(company, year)
    score, weights_used = composite_from_radar(radar)
    rating, rating_label = rating_of(score)

    by_key = {d["key"]: d.get("score") for d in radar}
    missing = [d["key"] for d in radar if not d.get("available")]
    baseline = BENCHMARK_TCO2_PER_MWH.get(year, BENCHMARK_DEFAULT)

    return {
        "code": company["code"],
        "name": company["name"],
        "group": company["group"],
        "year": year,
        "model_version": MODEL_VERSION,
        "available": True,

        # 原始量
        "ci_g_per_kwh": round(ci, 1),
        "change_rate_pct": round(tau * 100.0, 2) if tau is not None else None,
        "change_rate_basis": tau_basis,
        "clean_energy_share_pct": company.get("clean_energy_share_pct"),
        "clean_energy_share_basis": company.get("clean_energy_share_basis"),

        # 五个维度（唯一一套）
        "score_intensity": by_key.get("intensity"),
        "score_trend": by_key.get("trend"),
        "score_green_capex": by_key.get("green_capex"),
        "score_structure": by_key.get("structure"),
        "score_carbon_compliance": by_key.get("carbon_compliance"),

        # 聚合（纯公式）
        "weights_applied": {k: round(v, 3) for k, v in weights_used.items()},
        "carbon_score": round(score, 1) if score is not None else None,
        "rating": rating,
        "rating_label": rating_label,

        # 对照与元信息
        "benchmark_tco2_per_mwh": baseline,
        "benchmark_label": BENCHMARK_LABEL,
        "deviation_vs_baseline_pct": round((ci - baseline * 1000.0) /
                                           (baseline * 1000.0) * 100.0, 1),
        "missing": missing,
        "data_coverage": round(len(years) / 3.0 * 100.0),
        "years_used": years,
    }


# 数据可信度的取值：用**中文词语**而非字母。
# 原因：绿色信用评级用 AAA/AA/A/B+/B/B−/C 的字母档位，若可信度也用 A/B/C/D，
# 两者会被当成同一个指标——实测中大唐电力的「评级 B−」与「可信度 B 级」几乎
# 无法区分，国投电力更是「评级 A / 可信度 C」并排出现。改用词语后不可能误读。
CONFIDENCE_LEVELS = {
    "full":     "充分",   # 三年数据完整 + 清洁占比 + 第三方鉴证
    "complete": "完整",   # 三年数据完整 + 清洁占比
    "partial":  "部分",   # 至少两年
    "thin":     "不足",   # 仅一年或数据不足
}


def confidence_grade(company: dict) -> str:
    """数据可信度（与综合分完全分离，不参与打分）。

    返回中文词语而非字母，避免与绿色信用评级的字母档位混淆。
    """
    years = company.get("years", {})
    usable = sum(1 for r in years.values()
                 if r.get("scope1_tco2") is not None and r.get("power_gen_gwh"))
    has_structure = company.get("clean_energy_share_pct") is not None
    if usable >= 3 and has_structure and company.get("assurance"):
        return CONFIDENCE_LEVELS["full"]
    if usable >= 3 and has_structure:
        return CONFIDENCE_LEVELS["complete"]
    if usable >= 2:
        return CONFIDENCE_LEVELS["partial"]
    return CONFIDENCE_LEVELS["thin"]


# ---------------------------------------------------------------------------
# 7. 信贷定价联动
# ---------------------------------------------------------------------------
def rate_delta_bp(score: float, threshold: float = CREDIT_THRESHOLD) -> int:
    """Δr = −(S − 60) × 1.0 BP。高于 60 分下浮，低于 60 分上浮。"""
    return -int(round((score - threshold) * CREDIT_BP_PER_POINT))


def credit_pricing(score: float) -> dict:
    bp = rate_delta_bp(score)
    if bp < 0:
        action = f"贷款利率下浮 {abs(bp)} 个 BP（{abs(bp)/100:.2f}%）"
    elif bp == 0:
        action = "平价发放"
    else:
        action = (f"不享受降息，且上浮 {bp} 个 BP；"
                  f"需开立节能改造专项监管账户")
    return {"delta_bp": bp, "action": action}


CHAIN_FIELDS = [
    "code", "name", "group", "year",
    "ci_g_per_kwh", "change_rate_pct", "clean_energy_share_pct",
    "score_intensity", "score_trend", "score_green_capex",
    "score_structure", "score_carbon_compliance",
    "weights_applied", "carbon_score", "rating",
    "data_coverage", "confidence_grade",
    "model_version", "baseline_version", "timestamp",
]


# ---------------------------------------------------------------------------
# 8. 五维雷达（本年 / 上年）
# ---------------------------------------------------------------------------
def _radar_row(spec: dict, value, score, note: str) -> dict:
    return {
        "key": spec["key"], "short": spec["short"], "label": spec["label"],
        "unit": spec["unit"], "desc": spec["desc"],
        "value": round(value, 2) if isinstance(value, (int, float)) else None,
        "score": round(score, 1) if isinstance(score, (int, float)) else None,
        "available": score is not None,
        "note": note,
    }


def radar_values(company: dict, year: int) -> list[dict]:
    """本年度的五维雷达原始值与得分。全部维度来自真实披露数据。"""
    has_years = bool(company.get("years"))
    ci = intensity(company, year) if has_years else None
    tau, tau_basis = change_rate(company, year) if has_years else (None, "无数据")

    gc_pct = None
    if company.get("green_capex_abs_yi") and company.get("green_capex_total_yi"):
        gc_pct = company["green_capex_abs_yi"] / company["green_capex_total_yi"] * 100.0

    rho = company.get("clean_energy_share_pct")
    dev = carbon_compliance_deviation(ci, year) if ci is not None else None

    raw = {
        "intensity": (ci, "" if ci is not None else "未取得可复算的排放量与发电量"),
        "trend": (tau * 100.0 if tau is not None else None,
                  f"口径：{tau_basis}" if tau is not None else "缺少历史年度数据"),
        "green_capex": (gc_pct, company.get("green_capex_note", "")),
        "structure": (rho, f"口径：{company.get('clean_energy_share_basis', '未注明')}"),
        "carbon_compliance": (
            dev, company.get("carbon_cost_note", "")
            or f"较{BENCHMARK_LABEL} {benchmark_g_per_kwh(year):.0f} gCO₂/kWh 的偏离度"),
    }
    scorers = {
        "intensity": score_dim1_intensity,
        "trend": lambda v: score_trend(v / 100.0),
        "green_capex": score_dim3_green_capex,
        "structure": score_dim4_structure,
        "carbon_compliance": score_dim5_compliance,
    }

    out = []
    for spec in RADAR_DIMS:
        k = spec["key"]
        value, note = raw[k]
        score = scorers[k](value) if value is not None else None
        out.append(_radar_row(spec, value, score, note))
    return out


def radar_prev_values(company: dict, year: int) -> list[dict]:
    """上一年度雷达值，用于双层叠加时序对比。

    维度 1/2/5 来自上一年度排放序列（真实历史数据）；
    维度 3/4 没有年度序列，改从台账 `previous_year` 的披露值取。
    任何一项没有上年披露值时，该轴标为未取得，绝不复用本年数值。
    """
    years = available_years(company)
    prev_year = year - 1
    py = company.get("previous_year") or {}

    if prev_year in years:
        ci_prev = intensity(company, prev_year)
        tau_prev, basis_prev = change_rate(company, prev_year)
    else:
        ci_prev, tau_prev, basis_prev = None, None, "无上一年度排放数据"

    gc_prev = py.get("green_capex_pct")
    rho_prev = py.get("clean_energy_pct")

    raw = {
        "intensity": (ci_prev, f"{prev_year} 年复算值" if ci_prev is not None
                      else "无上一年度排放数据"),
        "trend": (tau_prev * 100.0 if tau_prev is not None else None,
                  f"口径：{basis_prev}"),
        "green_capex": (gc_prev, "上一年度披露值" if gc_prev is not None
                        else "上一年度未披露绿色投入占比"),
        "structure": (rho_prev, "上一年度披露值" if rho_prev is not None
                      else "上一年度未披露清洁能源装机占比"),
        "carbon_compliance": (
            carbon_compliance_deviation(ci_prev, prev_year) if ci_prev is not None else None,
            f"按 {prev_year} 年基准线同口径重算" if ci_prev is not None else "无上一年度数据"),
    }
    scorers = {
        "intensity": score_dim1_intensity,
        "trend": lambda v: score_trend(v / 100.0),
        "green_capex": score_dim3_green_capex,
        "structure": score_dim4_structure,
        "carbon_compliance": score_dim5_compliance,
    }

    out = []
    for spec in RADAR_DIMS:
        k = spec["key"]
        value, note = raw[k]
        score = scorers[k](value) if value is not None else None
        out.append(_radar_row(spec, value, score, note))
    return out


# ---------------------------------------------------------------------------
# 9. 自检：直接运行本文件会打印实测验算表（用于同步文档）
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    data = json.loads(
        (here / "data" / "carbon_disclosure_ledger.json").read_text(encoding="utf-8"))

    print(f"模型：{MODEL_VERSION}")
    print(f"权重：{RADAR_WEIGHTS}   趋势灵敏度 k={TANH_K}")
    print()
    hdr = (f"{'企业':<10}{'强度':>8}{'同比%':>8}{'①能效':>8}{'②趋势':>8}"
           f"{'③投入':>8}{'④结构':>8}{'⑤合规':>8}{'综合':>8}{'评级':>6}")
    print(hdr)
    print("-" * len(hdr))
    for c in data["companies"]:
        years = available_years(c)
        r = carbon_score(c, max(years))
        def f(v):
            return f"{v:.1f}" if isinstance(v, (int, float)) else "—"
        print(f"{c['name']:<10}{f(r['ci_g_per_kwh']):>8}"
              f"{f(r['change_rate_pct']):>8}{f(r['score_intensity']):>8}"
              f"{f(r['score_trend']):>8}{f(r['score_green_capex']):>8}"
              f"{f(r['score_structure']):>8}{f(r['score_carbon_compliance']):>8}"
              f"{f(r['carbon_score']):>8}{str(r['rating']):>6}")
    print()
    print("评级档位表：")
    for floor, name, label in RATING_BANDS:
        print(f"  ≥{floor:>3}  {name:<4} {label}")
