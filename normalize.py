# -*- coding: utf-8 -*-
"""把披露台账（人工从各公司报告提取的原始值）归一化成模型输入，并打印结果。

用法：python normalize.py
输出：data/companies_multiyear.json （模型直接读取）
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8")

import carbon_model as M  # noqa: E402

LEDGER = HERE / "data" / "carbon_disclosure_ledger.json"
OUT = HERE / "data" / "companies_multiyear.json"


def to_model_inputs(ledger: dict) -> list[dict]:
    """只输出「有发电量、可直接复算强度」的年度；缺失年度不补、不猜。"""
    out = []
    for c in ledger["companies"]:
        years = {}
        for y, row in (c.get("years") or {}).items():
            gen = row.get("power_gen_gwh")
            if not gen:
                continue  # 没有发电量就算不出强度，直接跳过该年度
            s1 = row.get("scope1_tco2")
            s2 = row.get("scope2_tco2")
            if s1 is None and row.get("total_tco2e") is not None:
                # 公司只披露了总量、未拆分范围：按总量处理，范围二记 0
                s1, s2 = row["total_tco2e"], 0
            if s1 is None:
                continue
            years[y] = {
                "scope1_tco2": s1,
                "scope2_tco2": s2 or 0,
                "power_gen_gwh": gen,
            }
        # 有年度数据、或有清洁能源占比的，都保留（纯水电企业可能只有结构数据）
        if years or c.get("clean_energy_share_pct") is not None or c.get("substitute_metrics"):
            out.append({
                "code": c["code"], "name": c["name"], "group": c["group"],
                "assurance": False, "years": years,
                "status": c.get("status"),
                "self_reported_intensity_g_per_kwh": c.get("self_reported_intensity_g_per_kwh"),
                "clean_energy_share_pct": c.get("clean_energy_share_pct"),
                "clean_energy_share_basis": c.get("clean_energy_share_basis"),
                "green_capex_abs_yi": c.get("green_capex_abs_yi"),
                "green_capex_total_yi": c.get("green_capex_total_yi"),
                "green_capex_note": c.get("green_capex_note", ""),
                "carbon_cost_note": c.get("carbon_cost_note", ""),
                "previous_year": c.get("previous_year"),
                "note": c.get("note", ""),
            })
    return out


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    companies = to_model_inputs(ledger)
    OUT.write_text(json.dumps({"companies": companies}, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    print(f"可复算企业 {len(companies)} 家 -> {OUT.name}\n")

    hdr = (f"{'代码':<8}{'名称':<10}{'年度数':<7}{'CI(g/kWh)':>11}{'变化率%':>9}"
           f"{'清洁占比%':>10}{'强度':>7}{'趋势':>7}{'结构':>7}{'综合':>7}  评级")
    print(hdr)
    print("-" * len(hdr))
    for c in companies:
        r = M.carbon_score(c, 2024)
        if not r.get("available"):
            print(f"{c['code']:<8}{c['name']:<10}{len(c['years']):<7}{'数据不足，无法复算':>40}")
            continue
        f = lambda v, p=1: ('%.*f' % (p, v)) if isinstance(v, (int, float)) else '-'
        self_rep = c.get("self_reported_intensity_g_per_kwh")
        print(f"{c['code']:<8}{c['name']:<10}{len(c['years']):<7}"
              f"{f(r['ci_g_per_kwh']):>11}{f(r['change_rate_pct'], 2):>9}"
              f"{f(r['clean_energy_share_pct']):>10}"
              f"{f(r['score_intensity']):>7}{f(r['score_trend']):>7}"
              f"{f(r['score_structure']):>7}{f(r['carbon_score']):>7}  {r['rating']}")

    print("\n注：强度单位 gCO₂/kWh；强度项标尺 I_min=0、I_max=900；"
          "趋势项 = 50 + 50·tanh(−5·τ)；结构项 = 100×ρ^0.8。")


if __name__ == "__main__":
    main()
