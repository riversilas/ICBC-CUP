# -*- coding: utf-8 -*-
"""从 carbon_model.py 直接生成算法说明用的 Markdown 实测验算表。

为什么需要它
--------------------------------------------------------------------------
早期版本的算法说明里的实测验算表是**手工抄**的，结果代码改了参数（如趋势
灵敏度 k 从 5 改成 10）而文档没跟着改，导致同一份项目里出现三张互相矛盾的
评级表。本脚本让文档表格**永远等于代码的实际输出**。

用法
--------------------------------------------------------------------------
    python gen_doc_table.py            # 打印到屏幕，粘贴进算法说明
    python gen_doc_table.py > 表.md    # 或重定向到文件

输出中的数值全部来自 carbon_model.py 的当前常量与公式，不含任何手工数字。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import carbon_model as CM  # noqa: E402

LEDGER = ROOT / "data" / "carbon_disclosure_ledger.json"
ledger = json.loads(LEDGER.read_text(encoding="utf-8"))

print("<!-- 本表由 gen_doc_table.py 从 carbon_model.py 自动生成，请勿手工编辑 -->")
print(f"<!-- 模型：{CM.MODEL_VERSION}　TANH_K={CM.TANH_K}　"
      f"标尺={CM.INTENSITY_SCALE_MAX:.0f}　权重=等权 {1 / len(CM.RADAR_WEIGHTS):.2f} -->")
print()
print("| 企业 | 排放强度<br>gCO₂/kWh | 同比<br>% | ① 存量<br>能效 | ② 边际<br>改善 | "
      "③ 绿色<br>投入 | ④ 低碳<br>结构 | ⑤ 碳合规<br>承压 | **综合分** | 评级 | 可信度 | Δr |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|")

for c in ledger["companies"]:
    years = CM.available_years(c)
    if not years:
        continue
    r = CM.carbon_score(c, max(years))
    grade = CM.confidence_grade(c)
    credit = CM.credit_pricing(r["carbon_score"])

    def f(v, nd=1):
        return f"{v:.{nd}f}" if isinstance(v, (int, float)) else "—"

    bp = credit["delta_bp"]
    bp_txt = f"{bp:+d} BP" if bp else "0 BP"
    print(f"| {r['name']} | {f(r['ci_g_per_kwh'])} | {f(r['change_rate_pct'], 2)} | "
          f"{f(r['score_intensity'])} | {f(r['score_trend'])} | "
          f"{f(r['score_green_capex'])} | {f(r['score_structure'])} | "
          f"{f(r['score_carbon_compliance'])} | **{f(r['carbon_score'])}** | "
          f"{r['rating']} | {grade} | {bp_txt} |")

print()
print("未取得可复算数据的样本（不评分、不臆测）：")
for c in ledger["companies"]:
    if not CM.available_years(c):
        print(f"- {c['name']}（{c['code']}）")
print("- 华能国际（600011）、国电电力（600795）、华电国际（600027）、"
      "上海电力（600021）、长江电力（600900）—— 台账 `data/待填_多年度环境绩效.csv` 中数据待补")

# ---------------------------------------------------------------------------
# 逐企业五维明细（含上一年度对比）
# README 的「雷达图怎么读」一节直接引用这段，避免再次手抄过期数字。
# ---------------------------------------------------------------------------
print()
print()
print("<!-- 以下为逐企业五维明细（本年 vs 上年），同样由 gen_doc_table.py 生成 -->")
for c in ledger["companies"]:
    years = CM.available_years(c)
    if not years:
        continue
    y = max(years)
    cur = CM.radar_values(c, y)
    prev = CM.radar_prev_values(c, y)
    pv = {d["key"]: d for d in prev}

    def g(d, k, field):
        return d[k].get(field) if k in d else None

    cur_map = {d["key"]: d for d in cur}
    print()
    print(f"**{c['name']}（{c['code']}）**　报告年度 {y}")
    print()
    print("| 维度 | 本年度得分 | 上一年度得分 | ▲▼ 分差 | 原始值 |")
    print("|---|---|---|---|---|")
    for spec in CM.RADAR_DIMS:
        k = spec["key"]
        a, b = cur_map.get(k, {}), pv.get(k, {})
        sa, sb = a.get("score"), b.get("score")
        delta = f"{sa - sb:+.1f}" if (sa is not None and sb is not None) else "—"
        raw = a.get("value")
        raw_txt = f"{raw}{spec['unit']}" if raw is not None else "—"
        print(f"| {spec['label']} | {sa if sa is not None else '—'} | "
              f"{sb if sb is not None else '—'} | {delta} | {raw_txt} |")
    credit = CM.credit_pricing(CM.carbon_score(c, y)["carbon_score"])
    print()
    print(f"综合分 **{CM.carbon_score(c, y)['carbon_score']}**，"
          f"评级 **{CM.carbon_score(c, y)['rating']}**，Δr = {credit['delta_bp']:+d} BP")
