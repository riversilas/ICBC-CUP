# -*- coding: utf-8 -*-
"""绿鉴MVP - 数据层: 加载样本企业数据与报告索引
路径兼容开发与PyInstaller打包(V1.4): 资源从 _MEIPASS 读, 可写文件在 exe 目录
"""
import json, csv, os, sys, hashlib
from datetime import datetime


def _frozen():
    return getattr(sys, "frozen", False)


def PROJECT_ROOT():
    """可写根目录: 开发=项目根; 打包=exe所在目录"""
    if _frozen():
        return os.path.dirname(sys.executable)
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def RESOURCE_ROOT():
    """只读资源根: 开发=项目根; 打包=PyInstaller解包目录"""
    if _frozen():
        return sys._MEIPASS
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


RAW = os.path.join(RESOURCE_ROOT(), "data", "raw")
PROC = os.path.join(PROJECT_ROOT(), "data", "processed")
PROC_RESOURCE = os.path.join(RESOURCE_ROOT(), "data", "processed")

# ---------- 排放因子 (演示用公开值, 实际使用需按最新官方因子校准) ----------
EMISSION_FACTORS = {
    "grid_co2_kg_per_kwh": 0.5568,   # 全国电网平均排放因子(演示值)
    "raw_coal_tco2_per_t": 1.9003,   # 原煤
    "natural_gas_tco2_per_km3": 21.622,  # 天然气
}

# ---------- 结构化披露数据 (基于ESG报告披露值的样例数据集, 2022年度) ----------
# 数值来源: 各公司ESG/社会责任报告披露口径的演示数据, 用于引擎流程验证
# 上线前用真实披露值替换; 每条带source标注, 保持"来源可溯源"原则
DISCLOSURES = {
    "600011": {"name": "华能国际", "type": "火电",
               "scope1_tco2": 310000000, "scope2_tco2": 8000000,
               "power_gen_gwh": 447000, "coal_consumed_wan_t": 9800,
               "revenue_100m": 246700, "scope3_disclosed": False,
               "env_penalty_count": 2, "disclosure_years": 4,
               # E维度细分(演示数据集, 上线前替换真实披露值)
               "water_use_wan_t": 21000, "wastewater_treated_pct": 95.0,
               "solid_waste_util_pct": 92.0, "energy_intensity_gj_per_mwh": 9.8,
               # S维度
               "safe_prod_invest_pct": 1.2, "employee_training_h": 42,
               # G维度
               "board_indep_pct": 36.4, "esg_committee": True},
    "600795": {"name": "国电电力", "type": "火电",
               "scope1_tco2": 240000000, "scope2_tco2": 5000000,
               "power_gen_gwh": 400000, "coal_consumed_wan_t": 8200,
               "revenue_100m": 192000, "scope3_disclosed": False,
               "env_penalty_count": 1, "disclosure_years": 4,
               "water_use_wan_t": 18500, "wastewater_treated_pct": 96.0,
               "solid_waste_util_pct": 90.0, "energy_intensity_gj_per_mwh": 9.6,
               "safe_prod_invest_pct": 1.4, "employee_training_h": 38,
               "board_indep_pct": 37.5, "esg_committee": True},
    "601991": {"name": "大唐发电", "type": "火电",
               "scope1_tco2": 210000000, "scope2_tco2": 4000000,
               "power_gen_gwh": 310000, "coal_consumed_wan_t": 7500,
               "revenue_100m": 122000, "scope3_disclosed": False,
               "env_penalty_count": 1, "disclosure_years": 3,
               "water_use_wan_t": 15200, "wastewater_treated_pct": 93.0,
               "solid_waste_util_pct": 88.0, "energy_intensity_gj_per_mwh": 10.1,
               "safe_prod_invest_pct": 1.1, "employee_training_h": 35,
               "board_indep_pct": 33.3, "esg_committee": False},
    "600027": {"name": "华电国际", "type": "火电",
               "scope1_tco2": 180000000, "scope2_tco2": 3500000,
               "power_gen_gwh": 260000, "coal_consumed_wan_t": 6800,
               "revenue_100m": 117000, "scope3_disclosed": False,
               "env_penalty_count": 0, "disclosure_years": 5,
               "water_use_wan_t": 12800, "wastewater_treated_pct": 97.0,
               "solid_waste_util_pct": 93.0, "energy_intensity_gj_per_mwh": 9.5,
               "safe_prod_invest_pct": 1.3, "employee_training_h": 40,
               "board_indep_pct": 38.5, "esg_committee": True},
    "600021": {"name": "上海电力", "type": "火电/新能源",
               "scope1_tco2": 22000000, "scope2_tco2": 900000,
               "power_gen_gwh": 48000, "coal_consumed_wan_t": 900,
               "revenue_100m": 42000, "scope3_disclosed": True,
               "env_penalty_count": 0, "disclosure_years": 6,
               "water_use_wan_t": 2400, "wastewater_treated_pct": 98.0,
               "solid_waste_util_pct": 95.0, "energy_intensity_gj_per_mwh": 8.2,
               "safe_prod_invest_pct": 1.5, "employee_training_h": 48,
               "board_indep_pct": 40.0, "esg_committee": True},
    "600886": {"name": "国投电力", "type": "水电为主",
               "scope1_tco2": 18000000, "scope2_tco2": 400000,
               "power_gen_gwh": 155000, "coal_consumed_wan_t": 500,
               "revenue_100m": 58000, "scope3_disclosed": False,
               "env_penalty_count": 0, "disclosure_years": 3,
               "water_use_wan_t": 3200, "wastewater_treated_pct": 96.0,
               "solid_waste_util_pct": 89.0, "energy_intensity_gj_per_mwh": 3.5,
               "safe_prod_invest_pct": 1.6, "employee_training_h": 44,
               "board_indep_pct": 41.7, "esg_committee": True},
    "600900": {"name": "长江电力", "type": "水电",
               "scope1_tco2": 900000, "scope2_tco2": 150000,
               "power_gen_gwh": 276000, "coal_consumed_wan_t": 0,
               "revenue_100m": 78000, "scope3_disclosed": True,
               "env_penalty_count": 0, "disclosure_years": 5,
               "water_use_wan_t": 950, "wastewater_treated_pct": 99.0,
               "solid_waste_util_pct": 96.0, "energy_intensity_gj_per_mwh": 0.6,
               "safe_prod_invest_pct": 1.8, "employee_training_h": 52,
               "board_indep_pct": 44.4, "esg_committee": True},
    "600023": {"name": "浙能电力", "type": "火电",
               "scope1_tco2": 160000000, "scope2_tco2": 3000000,
               "power_gen_gwh": 170000, "coal_consumed_wan_t": 6200,
               "revenue_100m": 98000, "scope3_disclosed": False,
               "env_penalty_count": 1, "disclosure_years": 4,
               "water_use_wan_t": 11800, "wastewater_treated_pct": 94.0,
               "solid_waste_util_pct": 91.0, "energy_intensity_gj_per_mwh": 9.9,
               "safe_prod_invest_pct": 1.2, "employee_training_h": 36,
               "board_indep_pct": 35.0, "esg_committee": False},
}


def load_reports_index():
    with open(os.path.join(RAW, "esg_announcements.json"), encoding="utf-8") as f:
        return json.load(f)


def load_basic_info():
    p = os.path.join(PROC, "样本企业基础信息.csv")
    if not os.path.exists(p):
        p = os.path.join(PROC_RESOURCE, "样本企业基础信息.csv")  # 打包回退到内置资源
    out = {}
    if os.path.exists(p):
        with open(p, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                out[row["代码"]] = row
    return out


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def report_digest_index():
    """35份报告索引 -> 每份生成摘要存证记录(不下载PDF, 用索引元数据做存证演示)"""
    idx = load_reports_index()
    records = []
    for code, info in idx.items():
        for r in info["reports"]:
            raw = f"{code}|{r['title']}|{r['url']}"
            records.append({
                "code": code, "company": info["name"],
                "title": r["title"], "url": r["url"],
                "digest": hashlib.sha256(raw.encode()).hexdigest()[:16],
            })
    return records
