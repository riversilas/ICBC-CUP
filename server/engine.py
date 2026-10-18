# -*- coding: utf-8 -*-
"""绿鉴(绿碳链证)MVP - 引擎层 (按 TECH_DOC §5, V1.5 采用碳模型量化准则)

V1.5 量化准则升级 — 采用《GreenTrace Carbon Model V1.0》方法论并适配电力行业:
  四变量:  CI 碳强度(度电排放) / TR 三年减排趋势 / PG 科学路径偏离 / AG 绝对排放变化
  标准化:  稳健 Z 分数(Median/MAD) → 正态CDF → 0-100
  赋权:    熵权法 + Spearman 相关性去冗余
  聚合:    加权几何平均(非完全补偿, 短板效应)
  约束:    科学路径修正 AF(γ=0.5, 待校准) → FinalScore
  独立输出: 数据可信等级 A/B/C/D(鉴证提高可信度, 不机械加碳分)

单位修正(V1.5): 排放强度统一为 kgCO₂/MWh(=原gCO₂/kWh数值), 修复此前单位标注错误。
"""
from data_store import DISCLOSURES
import math

COAL_GROUP = ["600011", "600795", "601991", "600027", "600023"]
CLEAN_GROUP = ["600021", "600886", "600900"]
GAMMA = 0.5          # 科学路径惩罚强度(待校准; 敏感性测试 0.25/0.5/0.75/1.0)
MODEL_VERSION = "Carbon-Model-V1.0-Adapted-Power"
WEIGHT_VERSION = "entropy-2026T3-8samples"

# 碳模型四变量历史数据(演示数据集, 供 TR/AG 计算; 上线前替换真实披露)
# base(2021基准) / prev(2022) / cur(2023): scope1_tco2 与 power_gen_gwh
HISTORY = {
    "600011": {"scope1": [3.35e8, 3.20e8, 3.10e8], "gen": [455000, 451000, 447000]},
    "600795": {"scope1": [2.60e8, 2.48e8, 2.40e8], "gen": [408000, 404000, 400000]},
    "601991": {"scope1": [2.35e8, 2.22e8, 2.10e8], "gen": [318000, 314000, 310000]},
    "600027": {"scope1": [1.92e8, 1.86e8, 1.80e8], "gen": [266000, 263000, 260000]},
    "600021": {"scope1": [2.60e7, 2.38e7, 2.20e7], "gen": [50500, 49200, 48000]},
    "600886": {"scope1": [2.05e7, 1.92e7, 1.80e7], "gen": [158000, 156500, 155000]},
    "600900": {"scope1": [1.02e6, 9.6e5, 9.0e5], "gen": [272000, 274000, 276000]},
    "600023": {"scope1": [1.78e8, 1.69e8, 1.60e8], "gen": [175000, 172500, 170000]},
}

# 电力行业科学减碳路径基准 kgCO₂/MWh(演示值, 参考 SBTi 电力行业 1.5°C 路径思路, 待校准)
PATHWAY_KG_PER_MWH = {"cur": 380.0, "prev": 395.0, "base": 410.0}
PATHWAY_VERSION = "SBTi-power-demo-2026"

REQUIRED_FIELDS = ["scope1_tco2", "scope2_tco2", "power_gen_gwh",
                   "revenue_100m", "scope3_disclosed"]


# ---------------- 基础指标 ----------------

def carbon_intensity_kg_mwh(d):
    """CI 当前碳强度: Scope1 tCO2 / 发电量 MWh → kgCO₂/MWh"""
    if not d.get("power_gen_gwh"):
        return None
    return d["scope1_tco2"] * 1000 / (d["power_gen_gwh"] * 1000)  # = t/GWh数值 == kg/MWh


def ci_series(code):
    """三年度碳强度序列 [base, prev, cur] kgCO₂/MWh"""
    h, cur = HISTORY[code], DISCLOSURES[code]
    c0 = h["scope1"][0] * 1000 / (h["gen"][0] * 1000)
    c1 = h["scope1"][1] * 1000 / (h["gen"][1] * 1000)
    c2 = carbon_intensity_kg_mwh(cur)
    return [c0, c1, c2]


def tr_three_year_ci_cr(code):
    """TR 三年碳强度复合下降率(越高越好)"""
    c0, _, c2 = ci_series(code)
    if c0 <= 0 or c2 <= 0:
        return None
    return 1 - (c2 / c0) ** (1 / 3)


def pg_pathway(code, year_key="cur"):
    """PG 科学路径偏离度 = (实际强度-路径)/路径 (越低越好)"""
    ci = carbon_intensity_kg_mwh(DISCLOSURES[code])
    b = PATHWAY_KG_PER_MWH[year_key]
    return (ci - b) / b


def ag_abs_change(code):
    """AG 绝对排放同比变化率 = (E_cur - E_prev)/E_prev (越低越好)"""
    h = HISTORY[code]
    e_prev, e_cur = h["scope1"][1], h["scope1"][2]
    return (e_cur - e_prev) / e_prev


# ---------------- 稳健标准化 (Median/MAD → 正态CDF → 0-100) ----------------

def _median(v):
    s = sorted(v)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def _mad(v, med):
    return _median([abs(x - med) for x in v])


def _norm_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def robust_scores(codes, extractor, positive):
    """对指标做稳健标准化返回 {code: 0-100分}
    positive=True: 收益型(越高越好); False: 成本型(越低越好)"""
    raw = {c: extractor(c) for c in codes}
    vals = [v for v in raw.values() if v is not None]
    if len(vals) < 3:
        return {c: (50 if raw[c] is not None else None) for c in codes}
    med = _median(vals)
    mad = _mad(vals, med)
    out = {}
    for c, v in raw.items():
        if v is None:
            out[c] = None
            continue
        z = (v - med) / (1.4826 * mad) if mad > 0 else 0.0
        p = _norm_cdf(z) * 100
        out[c] = round(p if positive else 100 - p)
    return out


# ---------------- 四变量计算(全样本) ----------------

def compute_variable_scores():
    codes = list(DISCLOSURES.keys())
    return {
        "CI": robust_scores(codes, lambda c: carbon_intensity_kg_mwh(DISCLOSURES[c]), positive=False),
        "TR": robust_scores(codes, tr_three_year_ci_cr, positive=True),
        "PG": robust_scores(codes, lambda c: pg_pathway(c), positive=False),
        "AG": robust_scores(codes, ag_abs_change, positive=False),
    }


# ---------------- 熵权 + Spearman 去冗余 ----------------

def entropy_weights(scores_by_var):
    """熵权法: 样本区分度越大权重越高"""
    codes = list(DISCLOSURES.keys())
    vars_ = list(scores_by_var.keys())
    eps = 1e-9
    e_map = {}
    for var in vars_:
        s = [scores_by_var[var][c] for c in codes if scores_by_var[var][c] is not None]
        n = len(s)
        if n == 0:
            e_map[var] = 1.0
            continue
        tot = sum(x + eps for x in s)
        p = [(x + eps) / tot for x in s]
        e = -sum(pi * math.log(pi) for pi in p) / math.log(n)
        e_map[var] = e
    d = {var: 1 - e_map[var] for var in vars_}
    tot_d = sum(d.values()) or 1.0
    return {var: d[var] / tot_d for var in vars_}


def _rank(v):
    """Return one-based average ranks, including ties (Spearman midranks)."""
    ordered = sorted(enumerate(v), key=lambda item: item[1])
    ranks = [0.0] * len(v)
    start = 0
    while start < len(ordered):
        end = start + 1
        while end < len(ordered) and ordered[end][1] == ordered[start][1]:
            end += 1
        average = (start + 1 + end) / 2
        for index, _ in ordered[start:end]:
            ranks[index] = average
        start = end
    return ranks


def spearman_adjust(scores_by_var, w):
    """Spearman 秩相关去冗余: 与其他指标越相关, 权重越被压低"""
    codes = list(DISCLOSURES.keys())
    vars_ = list(scores_by_var.keys())
    m = len(vars_)
    rho = {}
    for i, a in enumerate(vars_):
        for b in vars_[i + 1:]:
            va = [scores_by_var[a][c] for c in codes if scores_by_var[a][c] is not None]
            vb = [scores_by_var[b][c] for c in codes if scores_by_var[b][c] is not None]
            if len(va) == len(vb) and len(va) >= 3:
                ra, rb = _rank(va), _rank(vb)
                ma, mb = sum(ra) / len(ra), sum(rb) / len(rb)
                num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
                den = (sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb)) ** 0.5
                rho[(a, b)] = num / den if den else 0.0
    R = {}
    for a in vars_:
        rel = [abs(rho[k]) for k in rho if a in k]
        R[a] = 1 - (sum(rel) / (m - 1)) if rel else 1.0
    tw = sum(w[v] * R[v] for v in vars_) or 1.0
    return {v: w[v] * R[v] / tw for v in vars_}, R


# ---------------- 几何聚合 + 路径约束 ----------------

def geo_aggregate(sub_scores, w):
    """加权几何平均: BaseScore = 100 × Π((S+1)/101)^w"""
    prod = 1.0
    for var, s in sub_scores.items():
        if s is None:
            continue
        prod *= ((s + 1) / 101) ** w.get(var, 0)
    return round(100 * prod, 1)


def pathway_factor(code, gamma=GAMMA):
    """AF = [min(1, B/CI)]^γ — 实际强度越高于科学路径, 惩罚越重"""
    ci = carbon_intensity_kg_mwh(DISCLOSURES[code])
    b = PATHWAY_KG_PER_MWH["cur"]
    return min(1.0, b / ci) ** gamma if ci and ci > 0 else 1.0


def confidence_grade(code):
    """数据可信等级(独立于碳表现分): A/B/C/D"""
    d = DISCLOSURES[code]
    if d["env_penalty_count"] > 0:
        return "B", "存在环境处罚记录, 部分口径待复核"
    if d["scope3_disclosed"] and d["disclosure_years"] >= 5:
        return "A", "关键 Scope 数据披露完整, 历史可比"
    if d["disclosure_years"] >= 4:
        return "B", "主要数据完整, 部分口径未经独立复核"
    return "C", "披露覆盖不足或边界存在变化"


# ---------------- 汇总分析入口 ----------------

def group_median_intensity():
    vals = sorted(carbon_intensity_kg_mwh(DISCLOSURES[c]) for c in COAL_GROUP)
    n = len(vals)
    return vals[n // 2] if n % 2 else (vals[n // 2 - 1] + vals[n // 2]) / 2


def emission_intensity(d):
    """兼容旧接口, 单位 kgCO₂/MWh"""
    return round(carbon_intensity_kg_mwh(d), 1) if d.get("power_gen_gwh") else None


def esg_scores(code):
    """E/S/G 细分(百分位法保留用于 E 维度内部结构展示)"""
    d = DISCLOSURES[code]
    all_codes = list(DISCLOSURES.keys())

    def fam(field, positive=True):
        vals = [DISCLOSURES[c].get(field) for c in all_codes]
        v = d.get(field)
        if v is None:
            return None
        below = sum(1 for x in vals if x < v)
        r = below / (len(vals) - 1) * 100 if len(vals) > 1 else 50
        return round(r if positive else 100 - r)

    e_carbon = (fam("scope1_tco2", False) or 0) * 0.7 + \
               (100 if d["scope3_disclosed"] else 40) * 0.15 + \
               (fam("energy_intensity_gj_per_mwh", False) or 0) * 0.15
    e_water = (fam("water_use_wan_t", False) or 0) * 0.6 + (fam("wastewater_treated_pct") or 0) * 0.4
    e_pollution = fam("solid_waste_util_pct") or 0
    e_energy = fam("energy_intensity_gj_per_mwh", False) or 0
    e_score = round(e_carbon * 0.4 + e_water * 0.2 + e_pollution * 0.2 + e_energy * 0.2)
    s_score = round((fam("env_penalty_count", False) or 0) * 0.4 +
                    (fam("safe_prod_invest_pct") or 0) * 0.3 +
                    (fam("employee_training_h") or 0) * 0.3)
    g_score = round((fam("disclosure_years") or 0) * 0.4 +
                    (fam("board_indep_pct") or 0) * 0.3 +
                    (100 if d["esg_committee"] else 40) * 0.3)
    composite = round(e_score * 0.4 + s_score * 0.3 + g_score * 0.3)
    return {
        "E": {"carbon": round(e_carbon), "water": round(e_water),
              "pollution": round(e_pollution), "energy": round(e_energy), "score": e_score},
        "S": {"penalty": fam("env_penalty_count", False), "safety": fam("safe_prod_invest_pct"),
              "training": fam("employee_training_h"), "score": s_score},
        "G": {"disclosure": fam("disclosure_years"), "board": fam("board_indep_pct"),
              "committee": 100 if d["esg_committee"] else 40, "score": g_score},
        "composite": composite,
        "metrics_display": {
            "E": {"碳排放强度 kgCO₂/MWh": emission_intensity(d),
                  "Scope 3 披露": "已披露" if d["scope3_disclosed"] else "未披露",
                  "水耗 万吨/年": d["water_use_wan_t"],
                  "废水处理率 %": d["wastewater_treated_pct"],
                  "固废综合利用率 %": d["solid_waste_util_pct"],
                  "供电能耗 GJ/MWh": d["energy_intensity_gj_per_mwh"]},
            "S": {"环境处罚记录 数": d["env_penalty_count"],
                  "安全投入占营收 %": d["safe_prod_invest_pct"],
                  "人均培训 学时/年": d["employee_training_h"]},
            "G": {"ESG披露年限": d["disclosure_years"],
                  "独董占比 %": d["board_indep_pct"],
                  "ESG委员会": "已设立" if d["esg_committee"] else "未设立"},
        },
    }


SCORING_METHOD = {
    "method": "碳模型四变量法（稳健标准化 · 熵权 · 几何聚合 · 科学路径约束）",
    "rule": "四变量: 当前碳强度CI / 三年减排趋势TR / 科学路径偏离PG / 绝对排放变化AG。先做稳健Z分数(Median/MAD)标准化并映射0-100，熵权法赋权并用Spearman相关去冗余，加权几何平均聚合，最后乘以科学路径修正系数AF(γ=0.5, 待校准)。",
    "weights": "权重由样本熵计算(非固定40/25/35)，并随样本更新——每次计算披露权重版本。",
    "composite": "FinalScore = BaseScore × AF；数据可信等级(A/B/C/D)独立展示，不机械加进碳分。",
    "disclaimer": "评分为样本内相对比较，非绝对评级；不构成信用评价或投资建议。路径基准与γ为演示参数，正式使用前需专业校准与第三方复核。",
}


def analyze(code):
    d = DISCLOSURES.get(code)
    if not d:
        return None
    intensity = emission_intensity(d)
    median = group_median_intensity()
    group = COAL_GROUP if code in COAL_GROUP else CLEAN_GROUP

    peers = [{"code": c, "name": DISCLOSURES[c]["name"],
              "intensity": emission_intensity(DISCLOSURES[c])} for c in group]
    peers.sort(key=lambda x: x["intensity"] or 0)
    rank = [i for i, p in enumerate(peers) if p["code"] == code][0] + 1

    deviation_pct = round((intensity - median) / median * 100, 1) if intensity else None
    green_flag = intensity < median

    disclosed = sum(1 for f in REQUIRED_FIELDS if d.get(f) not in (None, 0, False))
    completeness = round(disclosed / len(REQUIRED_FIELDS) * 100)

    risks = []
    if deviation_pct and deviation_pct > 15:
        risks.append({"level": "yellow", "text": f"排放强度高于火电组中位数 {deviation_pct}%"})
    if not d["scope3_disclosed"]:
        risks.append({"level": "info", "text": "未披露 Scope 3 排放（价值链间接排放），数据完整度受限"})
    if d["env_penalty_count"] > 0:
        risks.append({"level": "yellow", "text": f"存在 {d['env_penalty_count']} 条环境处罚记录，需核对披露说明"})
    if not risks:
        risks.append({"level": "green", "text": "未发现明显异常"})

    # ---------- 碳模型四变量 ----------
    vs = compute_variable_scores()
    sub = {v: vs[v][code] for v in vs}
    w0 = entropy_weights(vs)
    w, R = spearman_adjust(vs, w0)
    base_score = geo_aggregate(sub, w)
    af = pathway_factor(code)
    final_score = round(base_score * af, 1)
    grade, grade_note = confidence_grade(code)
    ci_hist = ci_series(code)
    pg = pg_pathway(code)

    result = {
        "code": code, "name": d["name"], "type": d["type"],
        "metrics": {
            "scope1_tco2": d["scope1_tco2"], "scope2_tco2": d["scope2_tco2"],
            "power_gen_gwh": d["power_gen_gwh"],
            "emission_intensity_tco2_per_gwh": intensity,
            "group_median": round(median, 1),
            "deviation_pct": deviation_pct,
            "peer_rank": f"{rank}/{len(peers)}",
            "green_flag": green_flag,
            "completeness_pct": completeness,
        },
        "risks": risks,
        "peer_group": group,
        "peers": peers,
        "evidence": [
            {"field": "scope1_tco2", "source": f"{d['name']} ESG/社会责任报告披露",
             "note": "披露值, 来源索引已存证"},
            {"field": "power_gen_gwh", "source": f"{d['name']} 年度报告披露", "note": "披露值"},
            {"field": "emission_intensity", "source": "CI = Scope1 ÷ 发电量",
             "note": "kgCO₂/MWh 口径, 公式见 TECH_DOC §5"},
        ],
        # ---------- 碳模型输出 ----------
        "carbon_model": {
            "model_version": MODEL_VERSION,
            "weight_version": WEIGHT_VERSION,
            "pathway_version": PATHWAY_VERSION,
            "variables": {
                "CI": {"desc": "当前碳强度", "unit": "kgCO₂/MWh",
                       "value": intensity, "score": sub["CI"]},
                "TR": {"desc": "三年碳强度复合下降率",
                       "value": round(tr_three_year_ci_cr(code) * 100, 2), "score": sub["TR"]},
                "PG": {"desc": "科学路径偏离度",
                       "value": round(pg * 100, 1), "score": sub["PG"]},
                "AG": {"desc": "绝对排放同比变化",
                       "value": round(ag_abs_change(code) * 100, 2), "score": sub["AG"]},
            },
            "entropy_weights_raw": {k: round(v, 3) for k, v in w0.items()},
            "weights_final": {k: round(v, 3) for k, v in w.items()},
            "redundancy_R": {k: round(v, 3) for k, v in R.items()},
            "base_score": base_score,
            "pathway_factor": round(af, 3),
            "final_score": final_score,
            "confidence_grade": grade,
            "confidence_note": grade_note,
            "gamma": GAMMA,
            "ci_history": [round(x, 1) for x in ci_hist],
            "gamma_sensitivity": {str(g): round(geo_aggregate(sub, w) * pathway_factor(code, g), 1)
                                   for g in (0.25, 0.5, 0.75, 1.0)},
        },
        "esg": esg_scores(code),
        "scoring_method": SCORING_METHOD,
    }
    return result
