# 绿碳链证｜当前公开数据汇总与五维雷达视图

## 背景与基线
- 日期：2026-10-17
- Git：`bc07224463e018fff427dbf23d380476b2ffad9c`
- 分支：`feature/readme-data-report-20261017`
- 8家公开画像，3家V3.2模型，5家未准入。

## 结论与解读边界
- 当前公开数据汇总，不是正式登记报告；未生成、冻结或登记新凭证；不宣称独立核验。
- 基于Git HEAD已跟踪白名单文件在临时目录复算；未使用运行API、原机数据库、补充数据、银行记录或历史凭证账本。
- 全部8家画像；当前V3.2主线只收录3家可复算企业，另5家五维为null，不评分、不补零、不排行。3家附件观测未独立核验，5家演示值年度未确认。
- 五维图只使用main-quant V3.2的0—100参考分。画像JSON保留base100字段但不绘制；基期100是相对规模，不可与参考分混用。
- V3.2历史项目模型把一般环保费用用于投入轴、把清洁装机份额用于结构轴；不证明转型CapEx或低碳发电份额。碳合规轴不证明实际配额盈缺/履约成本。
- 源模型缺维会重新归一化；旧输入适配器存在Scope2缺值转0和total_tco2e转Scope1+Scope2=0逻辑。本次3家年度Scope1/2均非空，该补零分支未触发；本报告不自行补值。
- 历史字段不生效：原始JSON中的carbon.credit（例如大唐+16 BP）、评级、action、disclosure_status=verified均仅为历史模型元数据，不作为本报告建议、授信意见、真实定价或独立核验结论。后续核对已另行记录；本次不修改模型。参数、权重与预测力未经独立实证验证。
- carbon_compliance的正负描述可能存在矛盾：本报告只列源模型原始数值与规则，未经专业验证，不据此断言实际配额结余、缺口或收益。
- 原文件status=verified只是历史标签；来源标题、URL为索引/检索线索，未下载逐页核对PDF、组织边界、气体口径及Scope2地点法/市场法。
- 画像、演示记录、主线披露提取、附件快照同企业可有不同值；分开保留，不静默合并/覆盖。所有字段和年度均列示，真实0保留、null不补0。
- 主线evidence结构轴文字权重0.25与实际等权0.20冲突，原输出保留，以scoring_method及weights_applied为准；元数据自称8家/V3.1等可能陈旧，以实际数组及代码输出计数。
- 五维线只连相邻已知轴；不跨缺值闭合。未取得模型输入的企业显示空框而非零分。森林绿本期、哑金上期。

## 华能国际（600011）
原版演示值 · 年度未确认 / 年度：演示当前期 / V3.2：未取得可复算输入

### 原始轴值与参考分
|轴|单位|本期原始值|本期参考分|上期原始值|上期参考分|
|---|---|---|---|---|---|
| ① 存量能效 | gCO₂/kWh | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ② 边际改善 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ③ 绿色投入强度 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ④ 低碳结构 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ⑤ 碳合规与边际收益 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |

### 画像 / 全部年度 / 全源字段 / 全模型输出
```json
{
  "code": "600011",
  "name": "华能国际",
  "profile": {
    "radar": {
      "kind": "base100",
      "previous_year": null,
      "current_year": "演示当前期",
      "ticks": [
        0,
        50,
        100,
        150,
        200
      ],
      "axes": [
        {
          "key": "scope1",
          "label": "scope1",
          "index": null,
          "current_value": 310000000,
          "previous_value": null,
          "unit": "tCO2"
        },
        {
          "key": "scope2",
          "label": "scope2",
          "index": null,
          "current_value": 8000000,
          "previous_value": null,
          "unit": "tCO2"
        },
        {
          "key": "production",
          "label": "发电量",
          "index": null,
          "current_value": 447000,
          "previous_value": null,
          "unit": "GWh"
        },
        {
          "key": "intensity",
          "label": "排放强度",
          "index": null,
          "current_value": 711.4093959731543,
          "previous_value": null,
          "unit": "kgCO2/MWh"
        }
      ],
      "meaning": "基期=100的相对规模，不是绩效评分，不按面积评价好坏"
    },
    "code": "600011",
    "name": "华能国际",
    "type": "火电",
    "year": "演示当前期",
    "previous_year": null,
    "data_kind": "demo",
    "quality_label": "原版演示值 · 年度未确认",
    "comparability": "unavailable",
    "scope2_method": "unknown",
    "metrics": {
      "scope1": {
        "value": 310000000,
        "unit": "tCO2"
      },
      "scope2": {
        "value": 8000000,
        "unit": "tCO2"
      },
      "total": {
        "value": 318000000,
        "unit": "tCO2"
      },
      "production": {
        "value": 447000,
        "unit": "GWh"
      },
      "intensity": {
        "value": 711.4093959731543,
        "unit": "kgCO2/MWh"
      }
    },
    "changes": {
      "scope1": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "scope2": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "total": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "production": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "intensity": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      }
    },
    "trend": [
      {
        "year": "演示当前期",
        "scope1": 310000000,
        "scope2": 8000000,
        "total": 318000000,
        "production": 447000,
        "intensity": 711.4093959731543
      }
    ],
    "sources": [
      {
        "source_id": "600011-source-1",
        "title": "原data_store.DISCLOSURES演示数据",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E5%8D%8E%E8%83%BD%E5%9B%BD%E9%99%85%20%E5%8E%9Fdata_store.DISCLOSURES%E6%BC%94%E7%A4%BA%E6%95%B0%E6%8D%AE",
        "source_kind": "search"
      },
      {
        "source_id": "600011-public-index",
        "title": "华能国际2020年度社会责任报告",
        "metric_keys": [],
        "location": "历史报告索引，未确认对应本次年度观测",
        "status": "index_only",
        "hash_kind": "metadata_not_pdf",
        "url": "https://static.cninfo.com.cn/finalpage/2021-03-24/1209438774.PDF",
        "source_kind": "report_index"
      }
    ],
    "methods": [
      {
        "key": "scope1",
        "name": "Scope 1直接排放",
        "formula": "E₁ = Σ 活动数据 × 对应排放因子",
        "meaning": "企业控制范围内燃烧及工艺排放；本平台使用提供的披露值，不自行核算原始活动数据。",
        "basis_name": "GHG Protocol Corporate Standard（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "因子、温室气体及组织边界须核对原报告；概览不是已核验完整清单。"
      },
      {
        "key": "scope2",
        "name": "Scope 2外购能源排放",
        "formula": "E₂ = Σ 外购电／热／蒸汽／冷量 × 对应因子",
        "meaning": "区分地点法与市场法；两种方法不可相加为双份排放。",
        "basis_name": "GHG Protocol Scope 2 Guidance（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/scope-2-guidance",
        "limitation": "市场法合同工具需满足质量条件；当前附件方法未确认。"
      },
      {
        "key": "total",
        "name": "选定方法后的范围1+2汇总",
        "formula": "E = E₁ + E₂（同年度、边界及气体口径）",
        "meaning": "表示企业排放规模，不等于碳市场履约排放，也不直接惩罚大企业。",
        "basis_name": "GHG企业清单范围分列原则；合计为本项目展示",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "CO₂与CO₂e不得悄悄互换；总量不转换为信用风险分。"
      },
      {
        "key": "intensity",
        "name": "电力业务生产强度",
        "formula": "CI = E ÷ G；吨／GWh数值＝kg／MWh",
        "meaning": "区分单位产出效率与企业规模，避免只观察总量。",
        "basis_name": "TPI电力v5（已读方法摘要，部门强度思路）",
        "basis_url": "https://www.transitionpathwayinitiative.org/knowledge-hub/methodologies/electricity-utilities-methodology-v5",
        "limitation": "本项目Scope1+2分子不能冒称完全复制TPI详细方法；其他行业需另换分母。"
      },
      {
        "key": "change",
        "name": "同口径年度变化",
        "formula": "Δx = (xₜ ÷ xₜ₋₁ − 1) × 100%",
        "meaning": "并列排放、产量及强度变化，辅助解释扩产与效率；产量下降不天然更好。",
        "basis_name": "数学同比；GHG一致性与透明核算目的",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "边界重述、方法变更或前值非正时不计算；下降不证明主动转型。"
      }
    ],
    "findings": [
      {
        "title": "先核对边界和Scope2方法",
        "detail": "附件未提供完整组织边界、气体基准和地点/市场法定位；图中复算明确属于假设演示，不是确认可比。",
        "severity": "warning"
      },
      {
        "title": "无需为五维补造数据",
        "detail": "移除无可靠披露的投入/结构计分轴；保留相关原值为未核验补充信息，不计算综合评级。",
        "severity": "info"
      }
    ],
    "method_version": "scope12-transition-1.9.4",
    "limitations": [
      "不计算人为综合分或信用评级。",
      "资料属于演示/附件，原报告未独立核验；只有公式可复算。",
      "Scope1/2聚焦不是完整企业足迹或完整IFRS/GRI合规评估。",
      "银行价值是版本核验、口径解释与待核事项，而不是已证实预测信用风险。"
    ],
    "optional_observations": {
      "warning": "数据原年度标签与历史序列不一致，未拼接Scope2历史或伪造同比。"
    }
  },
  "main_quant": null,
  "radar_v32": [
    {
      "key": "intensity",
      "short": "存量能效",
      "label": "① 存量能效",
      "unit": "gCO₂/kWh",
      "desc": "度电碳排放强度，反映机组技术是否先进",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "trend",
      "short": "边际改善",
      "label": "② 边际改善",
      "unit": "%",
      "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "green_capex",
      "short": "绿色投入",
      "label": "③ 绿色投入强度",
      "unit": "%",
      "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "structure",
      "short": "低碳结构",
      "label": "④ 低碳结构",
      "unit": "%",
      "desc": "控股清洁能源装机容量占比，长期结构韧性",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "carbon_compliance",
      "short": "碳合规承压",
      "label": "⑤ 碳合规与边际收益",
      "unit": "%",
      "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    }
  ],
  "public_source_records": {
    "data/companies.json": null,
    "data/companies_multiyear.json": null,
    "data/carbon_disclosure_ledger.json": null,
    "data/esg_announcements.json": null,
    "data/raw/esg_announcements.json": {
      "name": "华能国际",
      "reports": [
        {
          "title": "华能国际2023年度社会责任报告",
          "url": "finalpage/2024-03-20/1219348218.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "华能国际2022年度社会责任报告",
          "url": "finalpage/2023-03-22/1216181432.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "华能国际2021年度社会责任报告",
          "url": "finalpage/2022-03-23/1212645184.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "华能国际2020年度社会责任报告",
          "url": "finalpage/2021-03-24/1209438774.PDF",
          "kw": "社会责任报告"
        }
      ]
    },
    "data/processed/radar_attachment_snapshot.json": null,
    "data/待填_多年度环境绩效.csv": [
      {
        "证券代码": "600011",
        "企业名称": "华能国际",
        "报告年度": "2022",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600011",
        "企业名称": "华能国际",
        "报告年度": "2023",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600011",
        "企业名称": "华能国际",
        "报告年度": "2024",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      }
    ],
    "server/data_store.py::DISCLOSURES": {
      "name": "华能国际",
      "type": "火电",
      "scope1_tco2": 310000000,
      "scope2_tco2": 8000000,
      "power_gen_gwh": 447000,
      "coal_consumed_wan_t": 9800,
      "revenue_100m": 246700,
      "scope3_disclosed": false,
      "env_penalty_count": 2,
      "disclosure_years": 4,
      "water_use_wan_t": 21000,
      "wastewater_treated_pct": 95.0,
      "solid_waste_util_pct": 92.0,
      "energy_intensity_gj_per_mwh": 9.8,
      "safe_prod_invest_pct": 1.2,
      "employee_training_h": 42,
      "board_indep_pct": 36.4,
      "esg_committee": true
    }
  }
}
```

## 国电电力（600795）
原版演示值 · 年度未确认 / 年度：演示当前期 / V3.2：未取得可复算输入

### 原始轴值与参考分
|轴|单位|本期原始值|本期参考分|上期原始值|上期参考分|
|---|---|---|---|---|---|
| ① 存量能效 | gCO₂/kWh | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ② 边际改善 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ③ 绿色投入强度 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ④ 低碳结构 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ⑤ 碳合规与边际收益 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |

### 画像 / 全部年度 / 全源字段 / 全模型输出
```json
{
  "code": "600795",
  "name": "国电电力",
  "profile": {
    "radar": {
      "kind": "base100",
      "previous_year": null,
      "current_year": "演示当前期",
      "ticks": [
        0,
        50,
        100,
        150,
        200
      ],
      "axes": [
        {
          "key": "scope1",
          "label": "scope1",
          "index": null,
          "current_value": 240000000,
          "previous_value": null,
          "unit": "tCO2"
        },
        {
          "key": "scope2",
          "label": "scope2",
          "index": null,
          "current_value": 5000000,
          "previous_value": null,
          "unit": "tCO2"
        },
        {
          "key": "production",
          "label": "发电量",
          "index": null,
          "current_value": 400000,
          "previous_value": null,
          "unit": "GWh"
        },
        {
          "key": "intensity",
          "label": "排放强度",
          "index": null,
          "current_value": 612.5,
          "previous_value": null,
          "unit": "kgCO2/MWh"
        }
      ],
      "meaning": "基期=100的相对规模，不是绩效评分，不按面积评价好坏"
    },
    "code": "600795",
    "name": "国电电力",
    "type": "火电",
    "year": "演示当前期",
    "previous_year": null,
    "data_kind": "demo",
    "quality_label": "原版演示值 · 年度未确认",
    "comparability": "unavailable",
    "scope2_method": "unknown",
    "metrics": {
      "scope1": {
        "value": 240000000,
        "unit": "tCO2"
      },
      "scope2": {
        "value": 5000000,
        "unit": "tCO2"
      },
      "total": {
        "value": 245000000,
        "unit": "tCO2"
      },
      "production": {
        "value": 400000,
        "unit": "GWh"
      },
      "intensity": {
        "value": 612.5,
        "unit": "kgCO2/MWh"
      }
    },
    "changes": {
      "scope1": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "scope2": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "total": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "production": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "intensity": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      }
    },
    "trend": [
      {
        "year": "演示当前期",
        "scope1": 240000000,
        "scope2": 5000000,
        "total": 245000000,
        "production": 400000,
        "intensity": 612.5
      }
    ],
    "sources": [
      {
        "source_id": "600795-source-1",
        "title": "原data_store.DISCLOSURES演示数据",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E5%9B%BD%E7%94%B5%E7%94%B5%E5%8A%9B%20%E5%8E%9Fdata_store.DISCLOSURES%E6%BC%94%E7%A4%BA%E6%95%B0%E6%8D%AE",
        "source_kind": "search"
      },
      {
        "source_id": "600795-public-index",
        "title": "国电电力发展股份有限公司董事会战略与ESG管理委员会实施细则",
        "metric_keys": [],
        "location": "历史报告索引，未确认对应本次年度观测",
        "status": "index_only",
        "hash_kind": "metadata_not_pdf",
        "url": "https://static.cninfo.com.cn/finalpage/2023-04-15/1216418380.PDF",
        "source_kind": "report_index"
      }
    ],
    "methods": [
      {
        "key": "scope1",
        "name": "Scope 1直接排放",
        "formula": "E₁ = Σ 活动数据 × 对应排放因子",
        "meaning": "企业控制范围内燃烧及工艺排放；本平台使用提供的披露值，不自行核算原始活动数据。",
        "basis_name": "GHG Protocol Corporate Standard（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "因子、温室气体及组织边界须核对原报告；概览不是已核验完整清单。"
      },
      {
        "key": "scope2",
        "name": "Scope 2外购能源排放",
        "formula": "E₂ = Σ 外购电／热／蒸汽／冷量 × 对应因子",
        "meaning": "区分地点法与市场法；两种方法不可相加为双份排放。",
        "basis_name": "GHG Protocol Scope 2 Guidance（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/scope-2-guidance",
        "limitation": "市场法合同工具需满足质量条件；当前附件方法未确认。"
      },
      {
        "key": "total",
        "name": "选定方法后的范围1+2汇总",
        "formula": "E = E₁ + E₂（同年度、边界及气体口径）",
        "meaning": "表示企业排放规模，不等于碳市场履约排放，也不直接惩罚大企业。",
        "basis_name": "GHG企业清单范围分列原则；合计为本项目展示",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "CO₂与CO₂e不得悄悄互换；总量不转换为信用风险分。"
      },
      {
        "key": "intensity",
        "name": "电力业务生产强度",
        "formula": "CI = E ÷ G；吨／GWh数值＝kg／MWh",
        "meaning": "区分单位产出效率与企业规模，避免只观察总量。",
        "basis_name": "TPI电力v5（已读方法摘要，部门强度思路）",
        "basis_url": "https://www.transitionpathwayinitiative.org/knowledge-hub/methodologies/electricity-utilities-methodology-v5",
        "limitation": "本项目Scope1+2分子不能冒称完全复制TPI详细方法；其他行业需另换分母。"
      },
      {
        "key": "change",
        "name": "同口径年度变化",
        "formula": "Δx = (xₜ ÷ xₜ₋₁ − 1) × 100%",
        "meaning": "并列排放、产量及强度变化，辅助解释扩产与效率；产量下降不天然更好。",
        "basis_name": "数学同比；GHG一致性与透明核算目的",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "边界重述、方法变更或前值非正时不计算；下降不证明主动转型。"
      }
    ],
    "findings": [
      {
        "title": "先核对边界和Scope2方法",
        "detail": "附件未提供完整组织边界、气体基准和地点/市场法定位；图中复算明确属于假设演示，不是确认可比。",
        "severity": "warning"
      },
      {
        "title": "无需为五维补造数据",
        "detail": "移除无可靠披露的投入/结构计分轴；保留相关原值为未核验补充信息，不计算综合评级。",
        "severity": "info"
      }
    ],
    "method_version": "scope12-transition-1.9.4",
    "limitations": [
      "不计算人为综合分或信用评级。",
      "资料属于演示/附件，原报告未独立核验；只有公式可复算。",
      "Scope1/2聚焦不是完整企业足迹或完整IFRS/GRI合规评估。",
      "银行价值是版本核验、口径解释与待核事项，而不是已证实预测信用风险。"
    ],
    "optional_observations": {
      "warning": "数据原年度标签与历史序列不一致，未拼接Scope2历史或伪造同比。"
    }
  },
  "main_quant": null,
  "radar_v32": [
    {
      "key": "intensity",
      "short": "存量能效",
      "label": "① 存量能效",
      "unit": "gCO₂/kWh",
      "desc": "度电碳排放强度，反映机组技术是否先进",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "trend",
      "short": "边际改善",
      "label": "② 边际改善",
      "unit": "%",
      "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "green_capex",
      "short": "绿色投入",
      "label": "③ 绿色投入强度",
      "unit": "%",
      "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "structure",
      "short": "低碳结构",
      "label": "④ 低碳结构",
      "unit": "%",
      "desc": "控股清洁能源装机容量占比，长期结构韧性",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "carbon_compliance",
      "short": "碳合规承压",
      "label": "⑤ 碳合规与边际收益",
      "unit": "%",
      "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    }
  ],
  "public_source_records": {
    "data/companies.json": null,
    "data/companies_multiyear.json": null,
    "data/carbon_disclosure_ledger.json": null,
    "data/esg_announcements.json": null,
    "data/raw/esg_announcements.json": {
      "name": "国电电力",
      "reports": [
        {
          "title": "国电电力2021年社会责任报告",
          "url": "finalpage/2022-04-26/1213109241.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "国电电力2020年社会责任报告",
          "url": "finalpage/2021-04-20/1209727374.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "董事会战略与ESG管理委员会实施细则（2025.12）",
          "url": "finalpage/2025-12-13/1224872058.PDF",
          "kw": "ESG"
        },
        {
          "title": "国电电力发展股份有限公司董事会战略与ESG管理委员会实施细则",
          "url": "finalpage/2023-04-15/1216418380.PDF",
          "kw": "ESG"
        }
      ]
    },
    "data/processed/radar_attachment_snapshot.json": null,
    "data/待填_多年度环境绩效.csv": [
      {
        "证券代码": "600795",
        "企业名称": "国电电力",
        "报告年度": "2022",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600795",
        "企业名称": "国电电力",
        "报告年度": "2023",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600795",
        "企业名称": "国电电力",
        "报告年度": "2024",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      }
    ],
    "server/data_store.py::DISCLOSURES": {
      "name": "国电电力",
      "type": "火电",
      "scope1_tco2": 240000000,
      "scope2_tco2": 5000000,
      "power_gen_gwh": 400000,
      "coal_consumed_wan_t": 8200,
      "revenue_100m": 192000,
      "scope3_disclosed": false,
      "env_penalty_count": 1,
      "disclosure_years": 4,
      "water_use_wan_t": 18500,
      "wastewater_treated_pct": 96.0,
      "solid_waste_util_pct": 90.0,
      "energy_intensity_gj_per_mwh": 9.6,
      "safe_prod_invest_pct": 1.4,
      "employee_training_h": 38,
      "board_indep_pct": 37.5,
      "esg_committee": true
    }
  }
}
```

## 大唐发电（601991）
附件观测 · 未独立核验 / 年度：2024 / V3.2：2024；综合参考分 43.5（非信用结论）

### 原始轴值与参考分
|轴|单位|本期原始值|本期参考分|上期原始值|上期参考分|
|---|---|---|---|---|---|
| ① 存量能效 | gCO₂/kWh | 739.69 | 26.0 | 716.58 | 28.3 |
| ② 边际改善 | % | 3.23 | 42.0 | -14.71 | 81.3 |
| ③ 绿色投入强度 | % | 2.45 | 49.1 | 1.2 | 24.0 |
| ④ 低碳结构 | % | 40.37 | 40.4 | 30.0 | 30.0 |
| ⑤ 碳合规与边际收益 | % | 9.79 | 59.8 | 12.61 | 62.6 |

### 画像 / 全部年度 / 全源字段 / 全模型输出
```json
{
  "code": "601991",
  "name": "大唐发电",
  "profile": {
    "radar": {
      "kind": "base100",
      "previous_year": 2023,
      "current_year": 2024,
      "ticks": [
        0,
        50,
        100,
        150,
        200
      ],
      "axes": [
        {
          "key": "scope1",
          "label": "scope1",
          "index": 107.09026719496089,
          "current_value": 210817900,
          "previous_value": 196860000,
          "unit": "tCO2"
        },
        {
          "key": "scope2",
          "label": "scope2",
          "index": 63.294117647058826,
          "current_value": 107600,
          "previous_value": 170000,
          "unit": "tCO2"
        },
        {
          "key": "production",
          "label": "发电量",
          "index": 103.7074618397652,
          "current_value": 285153,
          "previous_value": 274959,
          "unit": "GWh"
        },
        {
          "key": "intensity",
          "label": "排放强度",
          "index": 103.22543568106357,
          "current_value": 739.6923756720076,
          "previous_value": 716.5795627711768,
          "unit": "kgCO2/MWh"
        }
      ],
      "meaning": "基期=100的相对规模，不是绩效评分，不按面积评价好坏"
    },
    "code": "601991",
    "name": "大唐发电",
    "type": "火电",
    "year": 2024,
    "previous_year": 2023,
    "data_kind": "attachment_unverified",
    "quality_label": "附件观测 · 未独立核验",
    "comparability": "assumed_comparable_for_demo_only",
    "scope2_method": "unknown",
    "metrics": {
      "scope1": {
        "value": 210817900,
        "unit": "tCO2"
      },
      "scope2": {
        "value": 107600,
        "unit": "tCO2"
      },
      "total": {
        "value": 210925500,
        "unit": "tCO2"
      },
      "production": {
        "value": 285153,
        "unit": "GWh"
      },
      "intensity": {
        "value": 739.6923756720076,
        "unit": "kgCO2/MWh"
      }
    },
    "changes": {
      "scope1": {
        "value": 7.090267194960886,
        "reason": null
      },
      "scope2": {
        "value": -36.705882352941174,
        "reason": null
      },
      "total": {
        "value": 7.052479317870386,
        "reason": null
      },
      "production": {
        "value": 3.7074618397652026,
        "reason": null
      },
      "intensity": {
        "value": 3.225435681063571,
        "reason": null
      }
    },
    "trend": [
      {
        "year": 2022,
        "scope1": 191860000,
        "scope2": 970000,
        "total": 192830000,
        "production": 229517,
        "intensity": 840.15563117329
      },
      {
        "year": 2023,
        "scope1": 196860000,
        "scope2": 170000,
        "total": 197030000,
        "production": 274959,
        "intensity": 716.5795627711768
      },
      {
        "year": 2024,
        "scope1": 210817900,
        "scope2": 107600,
        "total": 210925500,
        "production": 285153,
        "intensity": 739.6923756720076
      }
    ],
    "sources": [
      {
        "source_id": "601991-source-1",
        "title": "2024年度可持续发展报告（环境、社会及管治报告）环境绩效表",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E5%A4%A7%E5%94%90%E5%8F%91%E7%94%B5%202024%E5%B9%B4%E5%BA%A6%E5%8F%AF%E6%8C%81%E7%BB%AD%E5%8F%91%E5%B1%95%E6%8A%A5%E5%91%8A%EF%BC%88%E7%8E%AF%E5%A2%83%E3%80%81%E7%A4%BE%E4%BC%9A%E5%8F%8A%E7%AE%A1%E6%B2%BB%E6%8A%A5%E5%91%8A%EF%BC%89%E7%8E%AF%E5%A2%83%E7%BB%A9%E6%95%88%E8%A1%A8",
        "source_kind": "search"
      },
      {
        "source_id": "601991-source-2",
        "title": "2024 年年度报告（现金流量表：资本开支）",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E5%A4%A7%E5%94%90%E5%8F%91%E7%94%B5%202024%20%E5%B9%B4%E5%B9%B4%E5%BA%A6%E6%8A%A5%E5%91%8A%EF%BC%88%E7%8E%B0%E9%87%91%E6%B5%81%E9%87%8F%E8%A1%A8%EF%BC%9A%E8%B5%84%E6%9C%AC%E5%BC%80%E6%94%AF%EF%BC%89",
        "source_kind": "search"
      },
      {
        "source_id": "601991-source-3",
        "title": "界面新闻《五大电力上市公司碳排放量发布》汇总",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E5%A4%A7%E5%94%90%E5%8F%91%E7%94%B5%20%E7%95%8C%E9%9D%A2%E6%96%B0%E9%97%BB%E3%80%8A%E4%BA%94%E5%A4%A7%E7%94%B5%E5%8A%9B%E4%B8%8A%E5%B8%82%E5%85%AC%E5%8F%B8%E7%A2%B3%E6%8E%92%E6%94%BE%E9%87%8F%E5%8F%91%E5%B8%83%E3%80%8B%E6%B1%87%E6%80%BB",
        "source_kind": "search"
      },
      {
        "source_id": "601991-public-index",
        "title": "大唐发电2024年可持续发展报告（环境、社会及管治报告）",
        "metric_keys": [],
        "location": "历史报告索引，未确认对应本次年度观测",
        "status": "index_only",
        "hash_kind": "metadata_not_pdf",
        "url": "https://static.cninfo.com.cn/finalpage/2025-03-26/1222896371.PDF",
        "source_kind": "report_index"
      }
    ],
    "methods": [
      {
        "key": "scope1",
        "name": "Scope 1直接排放",
        "formula": "E₁ = Σ 活动数据 × 对应排放因子",
        "meaning": "企业控制范围内燃烧及工艺排放；本平台使用提供的披露值，不自行核算原始活动数据。",
        "basis_name": "GHG Protocol Corporate Standard（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "因子、温室气体及组织边界须核对原报告；概览不是已核验完整清单。"
      },
      {
        "key": "scope2",
        "name": "Scope 2外购能源排放",
        "formula": "E₂ = Σ 外购电／热／蒸汽／冷量 × 对应因子",
        "meaning": "区分地点法与市场法；两种方法不可相加为双份排放。",
        "basis_name": "GHG Protocol Scope 2 Guidance（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/scope-2-guidance",
        "limitation": "市场法合同工具需满足质量条件；当前附件方法未确认。"
      },
      {
        "key": "total",
        "name": "选定方法后的范围1+2汇总",
        "formula": "E = E₁ + E₂（同年度、边界及气体口径）",
        "meaning": "表示企业排放规模，不等于碳市场履约排放，也不直接惩罚大企业。",
        "basis_name": "GHG企业清单范围分列原则；合计为本项目展示",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "CO₂与CO₂e不得悄悄互换；总量不转换为信用风险分。"
      },
      {
        "key": "intensity",
        "name": "电力业务生产强度",
        "formula": "CI = E ÷ G；吨／GWh数值＝kg／MWh",
        "meaning": "区分单位产出效率与企业规模，避免只观察总量。",
        "basis_name": "TPI电力v5（已读方法摘要，部门强度思路）",
        "basis_url": "https://www.transitionpathwayinitiative.org/knowledge-hub/methodologies/electricity-utilities-methodology-v5",
        "limitation": "本项目Scope1+2分子不能冒称完全复制TPI详细方法；其他行业需另换分母。"
      },
      {
        "key": "change",
        "name": "同口径年度变化",
        "formula": "Δx = (xₜ ÷ xₜ₋₁ − 1) × 100%",
        "meaning": "并列排放、产量及强度变化，辅助解释扩产与效率；产量下降不天然更好。",
        "basis_name": "数学同比；GHG一致性与透明核算目的",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "边界重述、方法变更或前值非正时不计算；下降不证明主动转型。"
      }
    ],
    "findings": [
      {
        "title": "先核对边界和Scope2方法",
        "detail": "附件未提供完整组织边界、气体基准和地点/市场法定位；图中复算明确属于假设演示，不是确认可比。",
        "severity": "warning"
      },
      {
        "title": "无需为五维补造数据",
        "detail": "移除无可靠披露的投入/结构计分轴；保留相关原值为未核验补充信息，不计算综合评级。",
        "severity": "info"
      }
    ],
    "method_version": "scope12-transition-1.9.4",
    "limitations": [
      "不计算人为综合分或信用评级。",
      "资料属于演示/附件，原报告未独立核验；只有公式可复算。",
      "Scope1/2聚焦不是完整企业足迹或完整IFRS/GRI合规评估。",
      "银行价值是版本核验、口径解释与待核事项，而不是已证实预测信用风险。"
    ],
    "optional_observations": {
      "clean_capacity_share_pct": 40.37,
      "environmental_spending_note": "环保节能投入 7.48 亿元 ÷ 现金流总资本开支 304.8 亿元 = 2.45%",
      "warning": "装机占比、一般环保费用仅作补充信息，不替代发电结构或低碳资本支出。"
    }
  },
  "main_quant": {
    "code": "601991",
    "name": "大唐发电",
    "type": "火电",
    "carbon": {
      "code": "601991",
      "name": "大唐发电",
      "group": "thermal",
      "year": 2024,
      "model_version": "GreenTrace-Power V3.2 (等权五维雷达)",
      "available": true,
      "ci_g_per_kwh": 739.7,
      "change_rate_pct": 3.23,
      "change_rate_basis": "同比",
      "clean_energy_share_pct": 40.37,
      "clean_energy_share_basis": "控股清洁能源装机容量占比",
      "score_intensity": 26.0,
      "score_trend": 42.0,
      "score_green_capex": 49.1,
      "score_structure": 40.4,
      "score_carbon_compliance": 59.8,
      "weights_applied": {
        "intensity": 0.2,
        "trend": 0.2,
        "green_capex": 0.2,
        "structure": 0.2,
        "carbon_compliance": 0.2
      },
      "carbon_score": 43.5,
      "rating": "B-",
      "rating_label": "碳配额承压资产",
      "benchmark_tco2_per_mwh": 0.82,
      "benchmark_label": "全国碳市场发电行业基准线",
      "deviation_vs_baseline_pct": -9.8,
      "missing": [],
      "data_coverage": 100,
      "years_used": [
        2022,
        2023,
        2024
      ],
      "group_label": "火电组",
      "disclosure_status": "verified",
      "ledger_note": "",
      "confidence_grade": "完整",
      "credit": {
        "delta_bp": 16,
        "action": "不享受降息，且上浮 16 个 BP；需开立节能改造专项监管账户"
      },
      "self_reported_intensity_g_per_kwh": 853.83,
      "self_reported_gap_pct": -13.4,
      "baseline_version": "全国碳市场发电行业基准线 2024",
      "sources": [
        "2024年度可持续发展报告（环境、社会及管治报告）环境绩效表",
        "2024 年年度报告（现金流量表：资本开支）",
        "界面新闻《五大电力上市公司碳排放量发布》汇总"
      ],
      "radar": [
        {
          "key": "intensity",
          "short": "存量能效",
          "label": "① 存量能效",
          "unit": "gCO₂/kWh",
          "desc": "度电碳排放强度，反映机组技术是否先进",
          "value": 739.69,
          "score": 26.0,
          "available": true,
          "note": ""
        },
        {
          "key": "trend",
          "short": "边际改善",
          "label": "② 边际改善",
          "unit": "%",
          "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
          "value": 3.23,
          "score": 42.0,
          "available": true,
          "note": "口径：同比"
        },
        {
          "key": "green_capex",
          "short": "绿色投入",
          "label": "③ 绿色投入强度",
          "unit": "%",
          "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
          "value": 2.45,
          "score": 49.1,
          "available": true,
          "note": "环保节能投入 7.48 亿元 ÷ 现金流总资本开支 304.8 亿元 = 2.45%"
        },
        {
          "key": "structure",
          "short": "低碳结构",
          "label": "④ 低碳结构",
          "unit": "%",
          "desc": "控股清洁能源装机容量占比，长期结构韧性",
          "value": 40.37,
          "score": 40.4,
          "available": true,
          "note": "口径：控股清洁能源装机容量占比"
        },
        {
          "key": "carbon_compliance",
          "short": "碳合规承压",
          "label": "⑤ 碳合规与边际收益",
          "unit": "%",
          "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
          "value": 9.79,
          "score": 59.8,
          "available": true,
          "note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +9.79%，配额略有结余"
        }
      ],
      "radar_prev": [
        {
          "key": "intensity",
          "short": "存量能效",
          "label": "① 存量能效",
          "unit": "gCO₂/kWh",
          "desc": "度电碳排放强度，反映机组技术是否先进",
          "value": 716.58,
          "score": 28.3,
          "available": true,
          "note": "2023 年复算值"
        },
        {
          "key": "trend",
          "short": "边际改善",
          "label": "② 边际改善",
          "unit": "%",
          "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
          "value": -14.71,
          "score": 81.3,
          "available": true,
          "note": "口径：同比"
        },
        {
          "key": "green_capex",
          "short": "绿色投入",
          "label": "③ 绿色投入强度",
          "unit": "%",
          "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
          "value": 1.2,
          "score": 24.0,
          "available": true,
          "note": "上一年度披露值"
        },
        {
          "key": "structure",
          "short": "低碳结构",
          "label": "④ 低碳结构",
          "unit": "%",
          "desc": "控股清洁能源装机容量占比，长期结构韧性",
          "value": 30.0,
          "score": 30.0,
          "available": true,
          "note": "上一年度披露值"
        },
        {
          "key": "carbon_compliance",
          "short": "碳合规承压",
          "label": "⑤ 碳合规与边际收益",
          "unit": "%",
          "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
          "value": 12.61,
          "score": 62.6,
          "available": true,
          "note": "按 2023 年基准线同口径重算"
        }
      ],
      "radar_prev_year": 2023,
      "verdict": {
        "rating": "B-",
        "label": "碳配额承压资产",
        "action": "不享受降息；建议开立节能改造专项监管账户",
        "reason": "综合分 43.5 分（等权五维平均；实际生效 5 维，权重重新归一化后为 存量能效 20%、边际改善 20%、绿色投入 20%、低碳结构 20%、碳合规承压 20%）最强轴 ⑤ 碳合规与边际收益 59.8 分；最弱轴 ① 存量能效 26.0 分。优势轴：⑤ 碳合规与边际收益 59.8。承压轴（低于 50 分）：① 存量能效 26.0、④ 低碳结构 40.4、② 边际改善 42.0、③ 绿色投入强度 49.1。评级由综合分按固定档位表判定（≥60 为 B+，≥45 为 B，≥30 为 B−），可独立复算。",
        "score": 43.5,
        "weights_applied": {
          "intensity": 0.2,
          "trend": 0.2,
          "green_capex": 0.2,
          "structure": 0.2,
          "carbon_compliance": 0.2
        },
        "computable": true
      }
    },
    "scoring_method": {
      "model_version": "GreenTrace-Power V3.2 (等权五维雷达)",
      "intensity": "I =（范围一 + 范围二）÷ 全口径发电量，单位 gCO₂/kWh",
      "trend": "τ =（I 今年 − I 去年）÷ I 去年；不足两年时用多年度等效年化变化率",
      "structure_raw": "ρ = 控股清洁能源装机容量占比（年报 / ESG 报告披露值）",
      "dims": [
        {
          "label": "① 存量能效",
          "formula": "S① =（1000 − I）÷ 10，限定 [0, 100]"
        },
        {
          "label": "② 边际改善",
          "formula": "S② = 50 + 50 × tanh(−5 × τ)"
        },
        {
          "label": "③ 绿色投入强度",
          "formula": "S③ = 100 × 环保节能投入 ÷ 现金流总资本开支 ÷ 5，上限 100"
        },
        {
          "label": "④ 低碳结构",
          "formula": "S④ = 清洁能源装机占比，直接对应百分比"
        },
        {
          "label": "⑤ 碳合规与边际收益",
          "formula": "S⑤ = 50 +（基准线 − I）÷ 基准线 × 100，限定 [0, 100]"
        }
      ],
      "composite": "综合分 S = 五维等权平均（每维 20%）：S = 0.20×(S①+S②+S③+S④+S⑤)",
      "weights_note": "等权固定权重，每维 20%，真实参与综合分计算。选择等权是因为尚无实证证据表明某一维对信用风险的预测力更强；等权是可复算、可审计的中性基准。",
      "missing_rule": "缺失维度不臆测、不计 0 分；其权重在剩余可得维度上重新归一化",
      "rating_rule": "评级由综合分查固定档位表判定，无人工干预：≥90 为 AAA，≥80 为 AA，≥70 为 A，≥60 为 B+，≥45 为 B，≥30 为 B-，≥0 为 C",
      "baseline": "全国碳市场发电行业基准线（gCO₂/kWh）：2022 年 823、2023 年 820、2024 年 820",
      "credit": "信贷联动：Δr = −(S − 60) × 1 BP（高于 60 分下浮利率）",
      "disclaimer": "评分为样本内相对比较，非绝对评级；不构成第三方鉴证意见，不构成授信结论。"
    },
    "evidence": [
      {
        "field": "scope1_tco2 / scope2_tco2",
        "source": "大唐发电 年度报告及 ESG 报告披露",
        "note": "披露值，来源已索引"
      },
      {
        "field": "power_gen_gwh",
        "source": "大唐发电 年度报告 / ESG 报告披露",
        "note": "全口径发电量，作为强度分母"
      },
      {
        "field": "intensity",
        "source": "平台复算 =（范围一 + 范围二）÷ 发电量",
        "note": "统一口径；tCO₂/GWh 数值上等于 gCO₂/kWh"
      },
      {
        "field": "clean_energy_share",
        "source": "企业 ESG 报告披露",
        "note": "口径：控股清洁能源装机容量占比，用于结构维度打分（权重 0.25）"
      },
      {
        "field": "企业自报排放强度",
        "source": "企业报告原文",
        "note": "分子为全公司排放、分母为火电发电量；与统一口径不可直接比较"
      }
    ],
    "reports_count": 5,
    "reports": [
      {
        "title": "大唐发电2023年社会责任报告（环境、社会及管治报告）",
        "url": "finalpage/2024-03-23/1219391420.PDF",
        "kw": "社会责任报告"
      },
      {
        "title": "大唐发电2022年社会责任报告（环境、社会及管治报告）",
        "url": "finalpage/2023-03-29/1216247175.PDF",
        "kw": "社会责任报告"
      },
      {
        "title": "大唐发电2021年社会责任报告（环境、社会及管治报告）",
        "url": "finalpage/2022-03-30/1212731328.PDF",
        "kw": "社会责任报告"
      },
      {
        "title": "大唐发电2020年社会责任报告",
        "url": "finalpage/2021-03-27/1209466225.PDF",
        "kw": "社会责任报告"
      },
      {
        "title": "大唐发电2024年可持续发展报告（环境、社会及管治报告）",
        "url": "finalpage/2025-03-26/1222896371.PDF",
        "kw": "可持续发展报告"
      }
    ]
  },
  "radar_v32": [
    {
      "key": "intensity",
      "short": "存量能效",
      "label": "① 存量能效",
      "unit": "gCO₂/kWh",
      "desc": "度电碳排放强度，反映机组技术是否先进",
      "value": 739.69,
      "score": 26.0,
      "available": true,
      "note": ""
    },
    {
      "key": "trend",
      "short": "边际改善",
      "label": "② 边际改善",
      "unit": "%",
      "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
      "value": 3.23,
      "score": 42.0,
      "available": true,
      "note": "口径：同比"
    },
    {
      "key": "green_capex",
      "short": "绿色投入",
      "label": "③ 绿色投入强度",
      "unit": "%",
      "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
      "value": 2.45,
      "score": 49.1,
      "available": true,
      "note": "环保节能投入 7.48 亿元 ÷ 现金流总资本开支 304.8 亿元 = 2.45%"
    },
    {
      "key": "structure",
      "short": "低碳结构",
      "label": "④ 低碳结构",
      "unit": "%",
      "desc": "控股清洁能源装机容量占比，长期结构韧性",
      "value": 40.37,
      "score": 40.4,
      "available": true,
      "note": "口径：控股清洁能源装机容量占比"
    },
    {
      "key": "carbon_compliance",
      "short": "碳合规承压",
      "label": "⑤ 碳合规与边际收益",
      "unit": "%",
      "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
      "value": 9.79,
      "score": 59.8,
      "available": true,
      "note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +9.79%，配额略有结余"
    }
  ],
  "public_source_records": {
    "data/companies.json": {
      "code": "601991",
      "name": "大唐发电",
      "type": "火电",
      "group": "thermal",
      "scope1_tco2": 210000000,
      "scope2_tco2": 4000000,
      "power_gen_gwh": 310000,
      "water_wan_ton": 15200,
      "wastewater_rate_pct": 93.0,
      "solid_waste_reuse_pct": 88.0,
      "energy_gj_per_mwh": 10.1,
      "scope3_disclosed": false,
      "env_penalties": 1,
      "safety_spend_pct": 1.1,
      "training_hours": 35,
      "esg_years": 3,
      "indep_director_pct": 33.3,
      "esg_committee": false,
      "completeness_pct": 80
    },
    "data/companies_multiyear.json": {
      "code": "601991",
      "name": "大唐发电",
      "group": "thermal",
      "assurance": false,
      "years": {
        "2022": {
          "scope1_tco2": 191860000,
          "scope2_tco2": 970000,
          "power_gen_gwh": 229517
        },
        "2023": {
          "scope1_tco2": 196860000,
          "scope2_tco2": 170000,
          "power_gen_gwh": 274959
        },
        "2024": {
          "scope1_tco2": 210817900,
          "scope2_tco2": 107600,
          "power_gen_gwh": 285153
        }
      },
      "status": "verified",
      "self_reported_intensity_g_per_kwh": 853.83,
      "clean_energy_share_pct": 40.37,
      "clean_energy_share_basis": "控股清洁能源装机容量占比",
      "green_capex_abs_yi": 7.48,
      "green_capex_total_yi": 304.8,
      "green_capex_note": "环保节能投入 7.48 亿元 ÷ 现金流总资本开支 304.8 亿元 = 2.45%",
      "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +9.79%，配额略有结余",
      "previous_year": {
        "green_capex_pct": 1.2,
        "clean_energy_pct": 30.0
      },
      "note": ""
    },
    "data/carbon_disclosure_ledger.json": {
      "code": "601991",
      "name": "大唐发电",
      "group": "thermal",
      "type": "火电",
      "years": {
        "2022": {
          "scope1_tco2": 191860000,
          "scope2_tco2": 970000,
          "power_gen_gwh": 229517
        },
        "2023": {
          "scope1_tco2": 196860000,
          "scope2_tco2": 170000,
          "power_gen_gwh": 274959
        },
        "2024": {
          "scope1_tco2": 210817900,
          "scope2_tco2": 107600,
          "power_gen_gwh": 285153
        }
      },
      "clean_energy_share_pct": 40.37,
      "clean_energy_share_basis": "控股清洁能源装机容量占比",
      "green_capex_abs_yi": 7.48,
      "green_capex_total_yi": 304.8,
      "green_capex_note": "环保节能投入 7.48 亿元 ÷ 现金流总资本开支 304.8 亿元 = 2.45%",
      "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +9.79%，配额略有结余",
      "previous_year": {
        "green_capex_pct": 1.2,
        "clean_energy_pct": 30.0
      },
      "self_reported_intensity_g_per_kwh": 853.83,
      "status": "verified",
      "sources": [
        "2024年度可持续发展报告（环境、社会及管治报告）环境绩效表",
        "2024 年年度报告（现金流量表：资本开支）",
        "界面新闻《五大电力上市公司碳排放量发布》汇总"
      ]
    },
    "data/esg_announcements.json": {
      "name": "大唐发电",
      "reports": [
        {
          "title": "大唐发电2023年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2024-03-23/1219391420.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2022年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2023-03-29/1216247175.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2021年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2022-03-30/1212731328.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2020年社会责任报告",
          "url": "finalpage/2021-03-27/1209466225.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2024年可持续发展报告（环境、社会及管治报告）",
          "url": "finalpage/2025-03-26/1222896371.PDF",
          "kw": "可持续发展报告"
        }
      ]
    },
    "data/raw/esg_announcements.json": {
      "name": "大唐发电",
      "reports": [
        {
          "title": "大唐发电2023年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2024-03-23/1219391420.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2022年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2023-03-29/1216247175.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2021年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2022-03-30/1212731328.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2020年社会责任报告",
          "url": "finalpage/2021-03-27/1209466225.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2024年可持续发展报告（环境、社会及管治报告）",
          "url": "finalpage/2025-03-26/1222896371.PDF",
          "kw": "可持续发展报告"
        }
      ]
    },
    "data/processed/radar_attachment_snapshot.json": {
      "code": "601991",
      "name": "大唐发电",
      "group": "thermal",
      "type": "火电",
      "years": {
        "2022": {
          "scope1_tco2": 191860000,
          "scope2_tco2": 970000,
          "power_gen_gwh": 229517
        },
        "2023": {
          "scope1_tco2": 196860000,
          "scope2_tco2": 170000,
          "power_gen_gwh": 274959
        },
        "2024": {
          "scope1_tco2": 210817900,
          "scope2_tco2": 107600,
          "power_gen_gwh": 285153
        }
      },
      "clean_energy_share_pct": 40.37,
      "clean_energy_share_basis": "控股清洁能源装机容量占比",
      "green_capex_abs_yi": 7.48,
      "green_capex_total_yi": 304.8,
      "green_capex_note": "环保节能投入 7.48 亿元 ÷ 现金流总资本开支 304.8 亿元 = 2.45%",
      "carbon_cost_note": "较全国基准线 750 gCO₂/kWh 偏离 +1.37%，配额基本平衡",
      "previous_year": {
        "green_capex_pct": 1.2,
        "clean_energy_pct": 30.0
      },
      "self_reported_intensity_g_per_kwh": 853.83,
      "status": "verified",
      "sources": [
        "2024年度可持续发展报告（环境、社会及管治报告）环境绩效表",
        "2024 年年度报告（现金流量表：资本开支）",
        "界面新闻《五大电力上市公司碳排放量发布》汇总"
      ]
    },
    "data/待填_多年度环境绩效.csv": [
      {
        "证券代码": "601991",
        "企业名称": "大唐发电",
        "报告年度": "2022",
        "直接排放_万吨CO2": "19186",
        "间接排放_万吨CO2": "97",
        "发电量_亿千瓦时": "2346.8",
        "排放强度_克每千瓦时": "817.8",
        "数据来源": "2022年度社会责任报告 环境绩效表"
      },
      {
        "证券代码": "601991",
        "企业名称": "大唐发电",
        "报告年度": "2023",
        "直接排放_万吨CO2": "19686",
        "间接排放_万吨CO2": "17",
        "发电量_亿千瓦时": "2300.96",
        "排放强度_克每千瓦时": "856.3",
        "数据来源": "2023年度社会责任报告 环境绩效表"
      },
      {
        "证券代码": "601991",
        "企业名称": "大唐发电",
        "报告年度": "2024",
        "直接排放_万吨CO2": "21081.79",
        "间接排放_万吨CO2": "10.76",
        "发电量_亿千瓦时": "2469.65",
        "排放强度_克每千瓦时": "853.83",
        "数据来源": "2024年度社会责任报告 环境绩效表"
      }
    ],
    "server/data_store.py::DISCLOSURES": {
      "name": "大唐发电",
      "type": "火电",
      "scope1_tco2": 210000000,
      "scope2_tco2": 4000000,
      "power_gen_gwh": 310000,
      "coal_consumed_wan_t": 7500,
      "revenue_100m": 122000,
      "scope3_disclosed": false,
      "env_penalty_count": 1,
      "disclosure_years": 3,
      "water_use_wan_t": 15200,
      "wastewater_treated_pct": 93.0,
      "solid_waste_util_pct": 88.0,
      "energy_intensity_gj_per_mwh": 10.1,
      "safe_prod_invest_pct": 1.1,
      "employee_training_h": 35,
      "board_indep_pct": 33.3,
      "esg_committee": false
    }
  }
}
```

## 华电国际（600027）
原版演示值 · 年度未确认 / 年度：演示当前期 / V3.2：未取得可复算输入

### 原始轴值与参考分
|轴|单位|本期原始值|本期参考分|上期原始值|上期参考分|
|---|---|---|---|---|---|
| ① 存量能效 | gCO₂/kWh | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ② 边际改善 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ③ 绿色投入强度 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ④ 低碳结构 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ⑤ 碳合规与边际收益 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |

### 画像 / 全部年度 / 全源字段 / 全模型输出
```json
{
  "code": "600027",
  "name": "华电国际",
  "profile": {
    "radar": {
      "kind": "base100",
      "previous_year": null,
      "current_year": "演示当前期",
      "ticks": [
        0,
        50,
        100,
        150,
        200
      ],
      "axes": [
        {
          "key": "scope1",
          "label": "scope1",
          "index": null,
          "current_value": 180000000,
          "previous_value": null,
          "unit": "tCO2"
        },
        {
          "key": "scope2",
          "label": "scope2",
          "index": null,
          "current_value": 3500000,
          "previous_value": null,
          "unit": "tCO2"
        },
        {
          "key": "production",
          "label": "发电量",
          "index": null,
          "current_value": 260000,
          "previous_value": null,
          "unit": "GWh"
        },
        {
          "key": "intensity",
          "label": "排放强度",
          "index": null,
          "current_value": 705.7692307692307,
          "previous_value": null,
          "unit": "kgCO2/MWh"
        }
      ],
      "meaning": "基期=100的相对规模，不是绩效评分，不按面积评价好坏"
    },
    "code": "600027",
    "name": "华电国际",
    "type": "火电",
    "year": "演示当前期",
    "previous_year": null,
    "data_kind": "demo",
    "quality_label": "原版演示值 · 年度未确认",
    "comparability": "unavailable",
    "scope2_method": "unknown",
    "metrics": {
      "scope1": {
        "value": 180000000,
        "unit": "tCO2"
      },
      "scope2": {
        "value": 3500000,
        "unit": "tCO2"
      },
      "total": {
        "value": 183500000,
        "unit": "tCO2"
      },
      "production": {
        "value": 260000,
        "unit": "GWh"
      },
      "intensity": {
        "value": 705.7692307692307,
        "unit": "kgCO2/MWh"
      }
    },
    "changes": {
      "scope1": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "scope2": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "total": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "production": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "intensity": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      }
    },
    "trend": [
      {
        "year": "演示当前期",
        "scope1": 180000000,
        "scope2": 3500000,
        "total": 183500000,
        "production": 260000,
        "intensity": 705.7692307692307
      }
    ],
    "sources": [
      {
        "source_id": "600027-source-1",
        "title": "原data_store.DISCLOSURES演示数据",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E5%8D%8E%E7%94%B5%E5%9B%BD%E9%99%85%20%E5%8E%9Fdata_store.DISCLOSURES%E6%BC%94%E7%A4%BA%E6%95%B0%E6%8D%AE",
        "source_kind": "search"
      },
      {
        "source_id": "600027-public-index",
        "title": "社会责任报告",
        "metric_keys": [],
        "location": "历史报告索引，未确认对应本次年度观测",
        "status": "index_only",
        "hash_kind": "metadata_not_pdf",
        "url": "https://static.cninfo.com.cn/finalpage/2021-03-31/1209485828.PDF",
        "source_kind": "report_index"
      }
    ],
    "methods": [
      {
        "key": "scope1",
        "name": "Scope 1直接排放",
        "formula": "E₁ = Σ 活动数据 × 对应排放因子",
        "meaning": "企业控制范围内燃烧及工艺排放；本平台使用提供的披露值，不自行核算原始活动数据。",
        "basis_name": "GHG Protocol Corporate Standard（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "因子、温室气体及组织边界须核对原报告；概览不是已核验完整清单。"
      },
      {
        "key": "scope2",
        "name": "Scope 2外购能源排放",
        "formula": "E₂ = Σ 外购电／热／蒸汽／冷量 × 对应因子",
        "meaning": "区分地点法与市场法；两种方法不可相加为双份排放。",
        "basis_name": "GHG Protocol Scope 2 Guidance（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/scope-2-guidance",
        "limitation": "市场法合同工具需满足质量条件；当前附件方法未确认。"
      },
      {
        "key": "total",
        "name": "选定方法后的范围1+2汇总",
        "formula": "E = E₁ + E₂（同年度、边界及气体口径）",
        "meaning": "表示企业排放规模，不等于碳市场履约排放，也不直接惩罚大企业。",
        "basis_name": "GHG企业清单范围分列原则；合计为本项目展示",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "CO₂与CO₂e不得悄悄互换；总量不转换为信用风险分。"
      },
      {
        "key": "intensity",
        "name": "电力业务生产强度",
        "formula": "CI = E ÷ G；吨／GWh数值＝kg／MWh",
        "meaning": "区分单位产出效率与企业规模，避免只观察总量。",
        "basis_name": "TPI电力v5（已读方法摘要，部门强度思路）",
        "basis_url": "https://www.transitionpathwayinitiative.org/knowledge-hub/methodologies/electricity-utilities-methodology-v5",
        "limitation": "本项目Scope1+2分子不能冒称完全复制TPI详细方法；其他行业需另换分母。"
      },
      {
        "key": "change",
        "name": "同口径年度变化",
        "formula": "Δx = (xₜ ÷ xₜ₋₁ − 1) × 100%",
        "meaning": "并列排放、产量及强度变化，辅助解释扩产与效率；产量下降不天然更好。",
        "basis_name": "数学同比；GHG一致性与透明核算目的",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "边界重述、方法变更或前值非正时不计算；下降不证明主动转型。"
      }
    ],
    "findings": [
      {
        "title": "先核对边界和Scope2方法",
        "detail": "附件未提供完整组织边界、气体基准和地点/市场法定位；图中复算明确属于假设演示，不是确认可比。",
        "severity": "warning"
      },
      {
        "title": "无需为五维补造数据",
        "detail": "移除无可靠披露的投入/结构计分轴；保留相关原值为未核验补充信息，不计算综合评级。",
        "severity": "info"
      }
    ],
    "method_version": "scope12-transition-1.9.4",
    "limitations": [
      "不计算人为综合分或信用评级。",
      "资料属于演示/附件，原报告未独立核验；只有公式可复算。",
      "Scope1/2聚焦不是完整企业足迹或完整IFRS/GRI合规评估。",
      "银行价值是版本核验、口径解释与待核事项，而不是已证实预测信用风险。"
    ],
    "optional_observations": {
      "warning": "数据原年度标签与历史序列不一致，未拼接Scope2历史或伪造同比。"
    }
  },
  "main_quant": null,
  "radar_v32": [
    {
      "key": "intensity",
      "short": "存量能效",
      "label": "① 存量能效",
      "unit": "gCO₂/kWh",
      "desc": "度电碳排放强度，反映机组技术是否先进",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "trend",
      "short": "边际改善",
      "label": "② 边际改善",
      "unit": "%",
      "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "green_capex",
      "short": "绿色投入",
      "label": "③ 绿色投入强度",
      "unit": "%",
      "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "structure",
      "short": "低碳结构",
      "label": "④ 低碳结构",
      "unit": "%",
      "desc": "控股清洁能源装机容量占比，长期结构韧性",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "carbon_compliance",
      "short": "碳合规承压",
      "label": "⑤ 碳合规与边际收益",
      "unit": "%",
      "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    }
  ],
  "public_source_records": {
    "data/companies.json": null,
    "data/companies_multiyear.json": null,
    "data/carbon_disclosure_ledger.json": null,
    "data/esg_announcements.json": null,
    "data/raw/esg_announcements.json": {
      "name": "华电国际",
      "reports": [
        {
          "title": "2024年度社会责任报告",
          "url": "finalpage/2025-03-28/1222927028.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2023年度社会责任报告",
          "url": "finalpage/2024-03-28/1219426307.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2022年度社会责任报告",
          "url": "finalpage/2023-03-30/1216257622.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2021年度社会责任报告",
          "url": "finalpage/2022-03-26/1212687595.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "社会责任报告",
          "url": "finalpage/2021-03-31/1209485828.PDF",
          "kw": "社会责任报告"
        }
      ]
    },
    "data/processed/radar_attachment_snapshot.json": null,
    "data/待填_多年度环境绩效.csv": [
      {
        "证券代码": "600027",
        "企业名称": "华电国际",
        "报告年度": "2022",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600027",
        "企业名称": "华电国际",
        "报告年度": "2023",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600027",
        "企业名称": "华电国际",
        "报告年度": "2024",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      }
    ],
    "server/data_store.py::DISCLOSURES": {
      "name": "华电国际",
      "type": "火电",
      "scope1_tco2": 180000000,
      "scope2_tco2": 3500000,
      "power_gen_gwh": 260000,
      "coal_consumed_wan_t": 6800,
      "revenue_100m": 117000,
      "scope3_disclosed": false,
      "env_penalty_count": 0,
      "disclosure_years": 5,
      "water_use_wan_t": 12800,
      "wastewater_treated_pct": 97.0,
      "solid_waste_util_pct": 93.0,
      "energy_intensity_gj_per_mwh": 9.5,
      "safe_prod_invest_pct": 1.3,
      "employee_training_h": 40,
      "board_indep_pct": 38.5,
      "esg_committee": true
    }
  }
}
```

## 上海电力（600021）
原版演示值 · 年度未确认 / 年度：演示当前期 / V3.2：未取得可复算输入

### 原始轴值与参考分
|轴|单位|本期原始值|本期参考分|上期原始值|上期参考分|
|---|---|---|---|---|---|
| ① 存量能效 | gCO₂/kWh | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ② 边际改善 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ③ 绿色投入强度 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ④ 低碳结构 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ⑤ 碳合规与边际收益 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |

### 画像 / 全部年度 / 全源字段 / 全模型输出
```json
{
  "code": "600021",
  "name": "上海电力",
  "profile": {
    "radar": {
      "kind": "base100",
      "previous_year": null,
      "current_year": "演示当前期",
      "ticks": [
        0,
        50,
        100,
        150,
        200
      ],
      "axes": [
        {
          "key": "scope1",
          "label": "scope1",
          "index": null,
          "current_value": 22000000,
          "previous_value": null,
          "unit": "tCO2"
        },
        {
          "key": "scope2",
          "label": "scope2",
          "index": null,
          "current_value": 900000,
          "previous_value": null,
          "unit": "tCO2"
        },
        {
          "key": "production",
          "label": "发电量",
          "index": null,
          "current_value": 48000,
          "previous_value": null,
          "unit": "GWh"
        },
        {
          "key": "intensity",
          "label": "排放强度",
          "index": null,
          "current_value": 477.0833333333333,
          "previous_value": null,
          "unit": "kgCO2/MWh"
        }
      ],
      "meaning": "基期=100的相对规模，不是绩效评分，不按面积评价好坏"
    },
    "code": "600021",
    "name": "上海电力",
    "type": "火电/新能源",
    "year": "演示当前期",
    "previous_year": null,
    "data_kind": "demo",
    "quality_label": "原版演示值 · 年度未确认",
    "comparability": "unavailable",
    "scope2_method": "unknown",
    "metrics": {
      "scope1": {
        "value": 22000000,
        "unit": "tCO2"
      },
      "scope2": {
        "value": 900000,
        "unit": "tCO2"
      },
      "total": {
        "value": 22900000,
        "unit": "tCO2"
      },
      "production": {
        "value": 48000,
        "unit": "GWh"
      },
      "intensity": {
        "value": 477.0833333333333,
        "unit": "kgCO2/MWh"
      }
    },
    "changes": {
      "scope1": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "scope2": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "total": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "production": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "intensity": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      }
    },
    "trend": [
      {
        "year": "演示当前期",
        "scope1": 22000000,
        "scope2": 900000,
        "total": 22900000,
        "production": 48000,
        "intensity": 477.0833333333333
      }
    ],
    "sources": [
      {
        "source_id": "600021-source-1",
        "title": "原data_store.DISCLOSURES演示数据",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E4%B8%8A%E6%B5%B7%E7%94%B5%E5%8A%9B%20%E5%8E%9Fdata_store.DISCLOSURES%E6%BC%94%E7%A4%BA%E6%95%B0%E6%8D%AE",
        "source_kind": "search"
      },
      {
        "source_id": "600021-public-index",
        "title": "上海电力股份有限公司2022年环境、社会及治理（ESG）报告",
        "metric_keys": [],
        "location": "历史报告索引，未确认对应本次年度观测",
        "status": "index_only",
        "hash_kind": "metadata_not_pdf",
        "url": "https://static.cninfo.com.cn/finalpage/2023-03-31/1216277810.PDF",
        "source_kind": "report_index"
      }
    ],
    "methods": [
      {
        "key": "scope1",
        "name": "Scope 1直接排放",
        "formula": "E₁ = Σ 活动数据 × 对应排放因子",
        "meaning": "企业控制范围内燃烧及工艺排放；本平台使用提供的披露值，不自行核算原始活动数据。",
        "basis_name": "GHG Protocol Corporate Standard（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "因子、温室气体及组织边界须核对原报告；概览不是已核验完整清单。"
      },
      {
        "key": "scope2",
        "name": "Scope 2外购能源排放",
        "formula": "E₂ = Σ 外购电／热／蒸汽／冷量 × 对应因子",
        "meaning": "区分地点法与市场法；两种方法不可相加为双份排放。",
        "basis_name": "GHG Protocol Scope 2 Guidance（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/scope-2-guidance",
        "limitation": "市场法合同工具需满足质量条件；当前附件方法未确认。"
      },
      {
        "key": "total",
        "name": "选定方法后的范围1+2汇总",
        "formula": "E = E₁ + E₂（同年度、边界及气体口径）",
        "meaning": "表示企业排放规模，不等于碳市场履约排放，也不直接惩罚大企业。",
        "basis_name": "GHG企业清单范围分列原则；合计为本项目展示",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "CO₂与CO₂e不得悄悄互换；总量不转换为信用风险分。"
      },
      {
        "key": "intensity",
        "name": "电力业务生产强度",
        "formula": "CI = E ÷ G；吨／GWh数值＝kg／MWh",
        "meaning": "区分单位产出效率与企业规模，避免只观察总量。",
        "basis_name": "TPI电力v5（已读方法摘要，部门强度思路）",
        "basis_url": "https://www.transitionpathwayinitiative.org/knowledge-hub/methodologies/electricity-utilities-methodology-v5",
        "limitation": "本项目Scope1+2分子不能冒称完全复制TPI详细方法；其他行业需另换分母。"
      },
      {
        "key": "change",
        "name": "同口径年度变化",
        "formula": "Δx = (xₜ ÷ xₜ₋₁ − 1) × 100%",
        "meaning": "并列排放、产量及强度变化，辅助解释扩产与效率；产量下降不天然更好。",
        "basis_name": "数学同比；GHG一致性与透明核算目的",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "边界重述、方法变更或前值非正时不计算；下降不证明主动转型。"
      }
    ],
    "findings": [
      {
        "title": "先核对边界和Scope2方法",
        "detail": "附件未提供完整组织边界、气体基准和地点/市场法定位；图中复算明确属于假设演示，不是确认可比。",
        "severity": "warning"
      },
      {
        "title": "无需为五维补造数据",
        "detail": "移除无可靠披露的投入/结构计分轴；保留相关原值为未核验补充信息，不计算综合评级。",
        "severity": "info"
      }
    ],
    "method_version": "scope12-transition-1.9.4",
    "limitations": [
      "不计算人为综合分或信用评级。",
      "资料属于演示/附件，原报告未独立核验；只有公式可复算。",
      "Scope1/2聚焦不是完整企业足迹或完整IFRS/GRI合规评估。",
      "银行价值是版本核验、口径解释与待核事项，而不是已证实预测信用风险。"
    ],
    "optional_observations": {
      "warning": "数据原年度标签与历史序列不一致，未拼接Scope2历史或伪造同比。"
    }
  },
  "main_quant": null,
  "radar_v32": [
    {
      "key": "intensity",
      "short": "存量能效",
      "label": "① 存量能效",
      "unit": "gCO₂/kWh",
      "desc": "度电碳排放强度，反映机组技术是否先进",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "trend",
      "short": "边际改善",
      "label": "② 边际改善",
      "unit": "%",
      "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "green_capex",
      "short": "绿色投入",
      "label": "③ 绿色投入强度",
      "unit": "%",
      "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "structure",
      "short": "低碳结构",
      "label": "④ 低碳结构",
      "unit": "%",
      "desc": "控股清洁能源装机容量占比，长期结构韧性",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "carbon_compliance",
      "short": "碳合规承压",
      "label": "⑤ 碳合规与边际收益",
      "unit": "%",
      "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    }
  ],
  "public_source_records": {
    "data/companies.json": null,
    "data/companies_multiyear.json": null,
    "data/carbon_disclosure_ledger.json": null,
    "data/esg_announcements.json": null,
    "data/raw/esg_announcements.json": {
      "name": "上海电力",
      "reports": [
        {
          "title": "上海电力2021年可持续发展报告",
          "url": "finalpage/2022-04-29/1213210445.PDF",
          "kw": "可持续发展报告"
        },
        {
          "title": "上海电力股份有限公司董事会环境社会及治理（ESG）委员会实施细则（经公司第九届董事会第五次会议审议通过）",
          "url": "finalpage/2025-09-10/1224648482.PDF",
          "kw": "ESG"
        },
        {
          "title": "上海电力股份有限公司2024年环境、社会及治理（ESG）报告",
          "url": "finalpage/2025-04-29/1223373838.PDF",
          "kw": "ESG"
        },
        {
          "title": "上海电力股份有限公司董事会环境社会及治理（ESG）委员会实施细则（经公司董事会2024年第二次临时会议审议通过）",
          "url": "finalpage/2024-04-27/1219874402.PDF",
          "kw": "ESG"
        },
        {
          "title": "上海电力股份有限公司 2023年环境、社会及治理（ESG）报告",
          "url": "finalpage/2024-04-02/1219492977.PDF",
          "kw": "ESG"
        },
        {
          "title": "上海电力股份有限公司2022年环境、社会及治理（ESG）报告",
          "url": "finalpage/2023-03-31/1216277810.PDF",
          "kw": "ESG"
        }
      ]
    },
    "data/processed/radar_attachment_snapshot.json": null,
    "data/待填_多年度环境绩效.csv": [
      {
        "证券代码": "600021",
        "企业名称": "上海电力",
        "报告年度": "2022",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600021",
        "企业名称": "上海电力",
        "报告年度": "2023",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600021",
        "企业名称": "上海电力",
        "报告年度": "2024",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      }
    ],
    "server/data_store.py::DISCLOSURES": {
      "name": "上海电力",
      "type": "火电/新能源",
      "scope1_tco2": 22000000,
      "scope2_tco2": 900000,
      "power_gen_gwh": 48000,
      "coal_consumed_wan_t": 900,
      "revenue_100m": 42000,
      "scope3_disclosed": true,
      "env_penalty_count": 0,
      "disclosure_years": 6,
      "water_use_wan_t": 2400,
      "wastewater_treated_pct": 98.0,
      "solid_waste_util_pct": 95.0,
      "energy_intensity_gj_per_mwh": 8.2,
      "safe_prod_invest_pct": 1.5,
      "employee_training_h": 48,
      "board_indep_pct": 40.0,
      "esg_committee": true
    }
  }
}
```

## 国投电力（600886）
附件观测 · 未独立核验 / 年度：2024 / V3.2：2024；综合参考分 78.1（非信用结论）

### 原始轴值与参考分
|轴|单位|本期原始值|本期参考分|上期原始值|上期参考分|
|---|---|---|---|---|---|
| ① 存量能效 | gCO₂/kWh | 287.71 | 71.2 | 314.4 | 68.6 |
| ② 边际改善 | % | -8.49 | 70.0 | 缺失（null） | 缺失（null） |
| ③ 绿色投入强度 | % | 3.95 | 79.1 | 2.0 | 40.0 |
| ④ 低碳结构 | % | 70.42 | 70.4 | 12.05 | 12.1 |
| ⑤ 碳合规与边际收益 | % | 64.91 | 100.0 | 61.66 | 100.0 |

### 画像 / 全部年度 / 全源字段 / 全模型输出
```json
{
  "code": "600886",
  "name": "国投电力",
  "profile": {
    "radar": {
      "kind": "base100",
      "previous_year": 2023,
      "current_year": 2024,
      "ticks": [
        0,
        50,
        100,
        150,
        200
      ],
      "axes": [
        {
          "key": "scope1",
          "label": "scope1",
          "index": 97.5806500949142,
          "current_value": 48808719,
          "previous_value": 50018850,
          "unit": "tCO2"
        },
        {
          "key": "scope2",
          "label": "scope2",
          "index": 77.26255876326775,
          "current_value": 698000,
          "previous_value": 903413,
          "unit": "tCO2"
        },
        {
          "key": "production",
          "label": "发电量",
          "index": 106.23958114666041,
          "current_value": 172072,
          "previous_value": 161966,
          "unit": "GWh"
        },
        {
          "key": "intensity",
          "label": "排放强度",
          "index": 91.51032537550479,
          "current_value": 287.7093251662095,
          "previous_value": 314.4009421730487,
          "unit": "kgCO2/MWh"
        }
      ],
      "meaning": "基期=100的相对规模，不是绩效评分，不按面积评价好坏"
    },
    "code": "600886",
    "name": "国投电力",
    "type": "水电为主",
    "year": 2024,
    "previous_year": 2023,
    "data_kind": "attachment_unverified",
    "quality_label": "附件观测 · 未独立核验",
    "comparability": "assumed_comparable_for_demo_only",
    "scope2_method": "unknown",
    "metrics": {
      "scope1": {
        "value": 48808719,
        "unit": "tCO2"
      },
      "scope2": {
        "value": 698000,
        "unit": "tCO2"
      },
      "total": {
        "value": 49506719,
        "unit": "tCO2"
      },
      "production": {
        "value": 172072,
        "unit": "GWh"
      },
      "intensity": {
        "value": 287.7093251662095,
        "unit": "kgCO2/MWh"
      }
    },
    "changes": {
      "scope1": {
        "value": -2.419349905085788,
        "reason": null
      },
      "scope2": {
        "value": -22.73744123673226,
        "reason": null
      },
      "total": {
        "value": -2.779813615117621,
        "reason": null
      },
      "production": {
        "value": 6.239581146660411,
        "reason": null
      },
      "intensity": {
        "value": -8.489674624495214,
        "reason": null
      }
    },
    "trend": [
      {
        "year": 2023,
        "scope1": 50018850,
        "scope2": 903413,
        "total": 50922263,
        "production": 161966,
        "intensity": 314.4009421730487
      },
      {
        "year": 2024,
        "scope1": 48808719,
        "scope2": 698000,
        "total": 49506719,
        "production": 172072,
        "intensity": 287.7093251662095
      }
    ],
    "sources": [
      {
        "source_id": "600886-source-1",
        "title": "2024年环境、社会与治理报告 关键绩效表（第一部分：环境范畴）",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E5%9B%BD%E6%8A%95%E7%94%B5%E5%8A%9B%202024%E5%B9%B4%E7%8E%AF%E5%A2%83%E3%80%81%E7%A4%BE%E4%BC%9A%E4%B8%8E%E6%B2%BB%E7%90%86%E6%8A%A5%E5%91%8A%20%E5%85%B3%E9%94%AE%E7%BB%A9%E6%95%88%E8%A1%A8%EF%BC%88%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86%EF%BC%9A%E7%8E%AF%E5%A2%83%E8%8C%83%E7%95%B4%EF%BC%89",
        "source_kind": "search"
      },
      {
        "source_id": "600886-source-2",
        "title": "2024 年年度报告（现金流量表：资本开支）",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E5%9B%BD%E6%8A%95%E7%94%B5%E5%8A%9B%202024%20%E5%B9%B4%E5%B9%B4%E5%BA%A6%E6%8A%A5%E5%91%8A%EF%BC%88%E7%8E%B0%E9%87%91%E6%B5%81%E9%87%8F%E8%A1%A8%EF%BC%9A%E8%B5%84%E6%9C%AC%E5%BC%80%E6%94%AF%EF%BC%89",
        "source_kind": "search"
      },
      {
        "source_id": "600886-source-3",
        "title": "报告正文：2024 年控股企业累计完成发电量 1720.72 亿千瓦时，同比增长 6.24%",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E5%9B%BD%E6%8A%95%E7%94%B5%E5%8A%9B%20%E6%8A%A5%E5%91%8A%E6%AD%A3%E6%96%87%EF%BC%9A2024%20%E5%B9%B4%E6%8E%A7%E8%82%A1%E4%BC%81%E4%B8%9A%E7%B4%AF%E8%AE%A1%E5%AE%8C%E6%88%90%E5%8F%91%E7%94%B5%E9%87%8F%201720.72%20%E4%BA%BF%E5%8D%83%E7%93%A6%E6%97%B6%EF%BC%8C%E5%90%8C%E6%AF%94%E5%A2%9E%E9%95%BF%206.24%25",
        "source_kind": "search"
      },
      {
        "source_id": "600886-public-index",
        "title": "国投电力控股股份有限公司2020年企业社会责任报告",
        "metric_keys": [],
        "location": "历史报告索引，未确认对应本次年度观测",
        "status": "index_only",
        "hash_kind": "metadata_not_pdf",
        "url": "https://static.cninfo.com.cn/finalpage/2021-04-29/1209858500.PDF",
        "source_kind": "report_index"
      }
    ],
    "methods": [
      {
        "key": "scope1",
        "name": "Scope 1直接排放",
        "formula": "E₁ = Σ 活动数据 × 对应排放因子",
        "meaning": "企业控制范围内燃烧及工艺排放；本平台使用提供的披露值，不自行核算原始活动数据。",
        "basis_name": "GHG Protocol Corporate Standard（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "因子、温室气体及组织边界须核对原报告；概览不是已核验完整清单。"
      },
      {
        "key": "scope2",
        "name": "Scope 2外购能源排放",
        "formula": "E₂ = Σ 外购电／热／蒸汽／冷量 × 对应因子",
        "meaning": "区分地点法与市场法；两种方法不可相加为双份排放。",
        "basis_name": "GHG Protocol Scope 2 Guidance（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/scope-2-guidance",
        "limitation": "市场法合同工具需满足质量条件；当前附件方法未确认。"
      },
      {
        "key": "total",
        "name": "选定方法后的范围1+2汇总",
        "formula": "E = E₁ + E₂（同年度、边界及气体口径）",
        "meaning": "表示企业排放规模，不等于碳市场履约排放，也不直接惩罚大企业。",
        "basis_name": "GHG企业清单范围分列原则；合计为本项目展示",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "CO₂与CO₂e不得悄悄互换；总量不转换为信用风险分。"
      },
      {
        "key": "intensity",
        "name": "电力业务生产强度",
        "formula": "CI = E ÷ G；吨／GWh数值＝kg／MWh",
        "meaning": "区分单位产出效率与企业规模，避免只观察总量。",
        "basis_name": "TPI电力v5（已读方法摘要，部门强度思路）",
        "basis_url": "https://www.transitionpathwayinitiative.org/knowledge-hub/methodologies/electricity-utilities-methodology-v5",
        "limitation": "本项目Scope1+2分子不能冒称完全复制TPI详细方法；其他行业需另换分母。"
      },
      {
        "key": "change",
        "name": "同口径年度变化",
        "formula": "Δx = (xₜ ÷ xₜ₋₁ − 1) × 100%",
        "meaning": "并列排放、产量及强度变化，辅助解释扩产与效率；产量下降不天然更好。",
        "basis_name": "数学同比；GHG一致性与透明核算目的",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "边界重述、方法变更或前值非正时不计算；下降不证明主动转型。"
      }
    ],
    "findings": [
      {
        "title": "先核对边界和Scope2方法",
        "detail": "附件未提供完整组织边界、气体基准和地点/市场法定位；图中复算明确属于假设演示，不是确认可比。",
        "severity": "warning"
      },
      {
        "title": "无需为五维补造数据",
        "detail": "移除无可靠披露的投入/结构计分轴；保留相关原值为未核验补充信息，不计算综合评级。",
        "severity": "info"
      }
    ],
    "method_version": "scope12-transition-1.9.4",
    "limitations": [
      "不计算人为综合分或信用评级。",
      "资料属于演示/附件，原报告未独立核验；只有公式可复算。",
      "Scope1/2聚焦不是完整企业足迹或完整IFRS/GRI合规评估。",
      "银行价值是版本核验、口径解释与待核事项，而不是已证实预测信用风险。"
    ],
    "optional_observations": {
      "clean_capacity_share_pct": 67.2,
      "environmental_spending_note": "环保投入 7.458 亿 + 节能投入 1.156 亿 = 8.61 亿元 ÷ 资本开支 217.7 亿元 = 3.96%",
      "warning": "装机占比、一般环保费用仅作补充信息，不替代发电结构或低碳资本支出。"
    }
  },
  "main_quant": {
    "code": "600886",
    "name": "国投电力",
    "type": "水电为主",
    "carbon": {
      "code": "600886",
      "name": "国投电力",
      "group": "clean",
      "year": 2024,
      "model_version": "GreenTrace-Power V3.2 (等权五维雷达)",
      "available": true,
      "ci_g_per_kwh": 287.7,
      "change_rate_pct": -8.49,
      "change_rate_basis": "同比",
      "clean_energy_share_pct": 70.42,
      "clean_energy_share_basis": "控股清洁能源装机容量占比（口径与大唐、浙能严格一致）",
      "score_intensity": 71.2,
      "score_trend": 70.0,
      "score_green_capex": 79.1,
      "score_structure": 70.4,
      "score_carbon_compliance": 100.0,
      "weights_applied": {
        "intensity": 0.2,
        "trend": 0.2,
        "green_capex": 0.2,
        "structure": 0.2,
        "carbon_compliance": 0.2
      },
      "carbon_score": 78.1,
      "rating": "A",
      "rating_label": "绿色资产",
      "benchmark_tco2_per_mwh": 0.82,
      "benchmark_label": "全国碳市场发电行业基准线",
      "deviation_vs_baseline_pct": -64.9,
      "missing": [],
      "data_coverage": 67,
      "years_used": [
        2023,
        2024
      ],
      "group_label": "水电/新能源组",
      "disclosure_status": "verified",
      "ledger_note": "",
      "confidence_grade": "部分",
      "credit": {
        "delta_bp": -18,
        "action": "贷款利率下浮 18 个 BP（0.18%）"
      },
      "self_reported_intensity_g_per_kwh": null,
      "baseline_version": "全国碳市场发电行业基准线 2024",
      "sources": [
        "2024年环境、社会与治理报告 关键绩效表（第一部分：环境范畴）",
        "2024 年年度报告（现金流量表：资本开支）",
        "报告正文：2024 年控股企业累计完成发电量 1720.72 亿千瓦时，同比增长 6.24%"
      ],
      "radar": [
        {
          "key": "intensity",
          "short": "存量能效",
          "label": "① 存量能效",
          "unit": "gCO₂/kWh",
          "desc": "度电碳排放强度，反映机组技术是否先进",
          "value": 287.71,
          "score": 71.2,
          "available": true,
          "note": ""
        },
        {
          "key": "trend",
          "short": "边际改善",
          "label": "② 边际改善",
          "unit": "%",
          "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
          "value": -8.49,
          "score": 70.0,
          "available": true,
          "note": "口径：同比"
        },
        {
          "key": "green_capex",
          "short": "绿色投入",
          "label": "③ 绿色投入强度",
          "unit": "%",
          "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
          "value": 3.95,
          "score": 79.1,
          "available": true,
          "note": "环保投入 7.458 亿 + 节能投入 1.156 亿 = 8.61 亿元 ÷ 资本开支 217.7 亿元 = 3.96%"
        },
        {
          "key": "structure",
          "short": "低碳结构",
          "label": "④ 低碳结构",
          "unit": "%",
          "desc": "控股清洁能源装机容量占比，长期结构韧性",
          "value": 70.42,
          "score": 70.4,
          "available": true,
          "note": "口径：控股清洁能源装机容量占比（口径与大唐、浙能严格一致）"
        },
        {
          "key": "carbon_compliance",
          "short": "碳合规承压",
          "label": "⑤ 碳合规与边际收益",
          "unit": "%",
          "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
          "value": 64.91,
          "score": 100.0,
          "available": true,
          "note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +64.91%，巨额配额结余，形成正贡献"
        }
      ],
      "radar_prev": [
        {
          "key": "intensity",
          "short": "存量能效",
          "label": "① 存量能效",
          "unit": "gCO₂/kWh",
          "desc": "度电碳排放强度，反映机组技术是否先进",
          "value": 314.4,
          "score": 68.6,
          "available": true,
          "note": "2023 年复算值"
        },
        {
          "key": "trend",
          "short": "边际改善",
          "label": "② 边际改善",
          "unit": "%",
          "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
          "value": null,
          "score": null,
          "available": false,
          "note": "口径：无历史数据"
        },
        {
          "key": "green_capex",
          "short": "绿色投入",
          "label": "③ 绿色投入强度",
          "unit": "%",
          "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
          "value": 2.0,
          "score": 40.0,
          "available": true,
          "note": "上一年度披露值"
        },
        {
          "key": "structure",
          "short": "低碳结构",
          "label": "④ 低碳结构",
          "unit": "%",
          "desc": "控股清洁能源装机容量占比，长期结构韧性",
          "value": 12.05,
          "score": 12.1,
          "available": true,
          "note": "上一年度披露值"
        },
        {
          "key": "carbon_compliance",
          "short": "碳合规承压",
          "label": "⑤ 碳合规与边际收益",
          "unit": "%",
          "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
          "value": 61.66,
          "score": 100.0,
          "available": true,
          "note": "按 2023 年基准线同口径重算"
        }
      ],
      "radar_prev_year": 2023,
      "verdict": {
        "rating": "A",
        "label": "绿色资产",
        "action": "建议利率适度下浮，按年度复核",
        "reason": "综合分 78.1 分（等权五维平均；实际生效 5 维，权重重新归一化后为 存量能效 20%、边际改善 20%、绿色投入 20%、低碳结构 20%、碳合规承压 20%）最强轴 ⑤ 碳合规与边际收益 100.0 分；最弱轴 ② 边际改善 70.0 分。优势轴：⑤ 碳合规与边际收益 100.0、③ 绿色投入强度 79.1、① 存量能效 71.2、④ 低碳结构 70.4、② 边际改善 70.0。评级由综合分按固定档位表判定（≥60 为 B+，≥45 为 B，≥30 为 B−），可独立复算。",
        "score": 78.1,
        "weights_applied": {
          "intensity": 0.2,
          "trend": 0.2,
          "green_capex": 0.2,
          "structure": 0.2,
          "carbon_compliance": 0.2
        },
        "computable": true
      }
    },
    "scoring_method": {
      "model_version": "GreenTrace-Power V3.2 (等权五维雷达)",
      "intensity": "I =（范围一 + 范围二）÷ 全口径发电量，单位 gCO₂/kWh",
      "trend": "τ =（I 今年 − I 去年）÷ I 去年；不足两年时用多年度等效年化变化率",
      "structure_raw": "ρ = 控股清洁能源装机容量占比（年报 / ESG 报告披露值）",
      "dims": [
        {
          "label": "① 存量能效",
          "formula": "S① =（1000 − I）÷ 10，限定 [0, 100]"
        },
        {
          "label": "② 边际改善",
          "formula": "S② = 50 + 50 × tanh(−5 × τ)"
        },
        {
          "label": "③ 绿色投入强度",
          "formula": "S③ = 100 × 环保节能投入 ÷ 现金流总资本开支 ÷ 5，上限 100"
        },
        {
          "label": "④ 低碳结构",
          "formula": "S④ = 清洁能源装机占比，直接对应百分比"
        },
        {
          "label": "⑤ 碳合规与边际收益",
          "formula": "S⑤ = 50 +（基准线 − I）÷ 基准线 × 100，限定 [0, 100]"
        }
      ],
      "composite": "综合分 S = 五维等权平均（每维 20%）：S = 0.20×(S①+S②+S③+S④+S⑤)",
      "weights_note": "等权固定权重，每维 20%，真实参与综合分计算。选择等权是因为尚无实证证据表明某一维对信用风险的预测力更强；等权是可复算、可审计的中性基准。",
      "missing_rule": "缺失维度不臆测、不计 0 分；其权重在剩余可得维度上重新归一化",
      "rating_rule": "评级由综合分查固定档位表判定，无人工干预：≥90 为 AAA，≥80 为 AA，≥70 为 A，≥60 为 B+，≥45 为 B，≥30 为 B-，≥0 为 C",
      "baseline": "全国碳市场发电行业基准线（gCO₂/kWh）：2022 年 823、2023 年 820、2024 年 820",
      "credit": "信贷联动：Δr = −(S − 60) × 1 BP（高于 60 分下浮利率）",
      "disclaimer": "评分为样本内相对比较，非绝对评级；不构成第三方鉴证意见，不构成授信结论。"
    },
    "evidence": [
      {
        "field": "scope1_tco2 / scope2_tco2",
        "source": "国投电力 年度报告及 ESG 报告披露",
        "note": "披露值，来源已索引"
      },
      {
        "field": "power_gen_gwh",
        "source": "国投电力 年度报告 / ESG 报告披露",
        "note": "全口径发电量，作为强度分母"
      },
      {
        "field": "intensity",
        "source": "平台复算 =（范围一 + 范围二）÷ 发电量",
        "note": "统一口径；tCO₂/GWh 数值上等于 gCO₂/kWh"
      },
      {
        "field": "clean_energy_share",
        "source": "企业 ESG 报告披露",
        "note": "口径：控股清洁能源装机容量占比（口径与大唐、浙能严格一致），用于结构维度打分（权重 0.25）"
      }
    ],
    "reports_count": 2,
    "reports": [
      {
        "title": "国投电力控股股份有限公司2021年度社会责任报告",
        "url": "finalpage/2022-04-29/1213224206.PDF",
        "kw": "社会责任报告"
      },
      {
        "title": "国投电力控股股份有限公司2020年企业社会责任报告",
        "url": "finalpage/2021-04-29/1209858500.PDF",
        "kw": "社会责任报告"
      }
    ]
  },
  "radar_v32": [
    {
      "key": "intensity",
      "short": "存量能效",
      "label": "① 存量能效",
      "unit": "gCO₂/kWh",
      "desc": "度电碳排放强度，反映机组技术是否先进",
      "value": 287.71,
      "score": 71.2,
      "available": true,
      "note": ""
    },
    {
      "key": "trend",
      "short": "边际改善",
      "label": "② 边际改善",
      "unit": "%",
      "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
      "value": -8.49,
      "score": 70.0,
      "available": true,
      "note": "口径：同比"
    },
    {
      "key": "green_capex",
      "short": "绿色投入",
      "label": "③ 绿色投入强度",
      "unit": "%",
      "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
      "value": 3.95,
      "score": 79.1,
      "available": true,
      "note": "环保投入 7.458 亿 + 节能投入 1.156 亿 = 8.61 亿元 ÷ 资本开支 217.7 亿元 = 3.96%"
    },
    {
      "key": "structure",
      "short": "低碳结构",
      "label": "④ 低碳结构",
      "unit": "%",
      "desc": "控股清洁能源装机容量占比，长期结构韧性",
      "value": 70.42,
      "score": 70.4,
      "available": true,
      "note": "口径：控股清洁能源装机容量占比（口径与大唐、浙能严格一致）"
    },
    {
      "key": "carbon_compliance",
      "short": "碳合规承压",
      "label": "⑤ 碳合规与边际收益",
      "unit": "%",
      "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
      "value": 64.91,
      "score": 100.0,
      "available": true,
      "note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +64.91%，巨额配额结余，形成正贡献"
    }
  ],
  "public_source_records": {
    "data/companies.json": {
      "code": "600886",
      "name": "国投电力",
      "type": "水电为主",
      "group": "clean",
      "scope1_tco2": 36000000,
      "scope2_tco2": 2000000,
      "power_gen_gwh": 310000,
      "water_wan_ton": 3200,
      "wastewater_rate_pct": 96.0,
      "solid_waste_reuse_pct": 89.0,
      "energy_gj_per_mwh": 3.5,
      "scope3_disclosed": false,
      "env_penalties": 0,
      "safety_spend_pct": 1.6,
      "training_hours": 44,
      "esg_years": 3,
      "indep_director_pct": 41.7,
      "esg_committee": true,
      "completeness_pct": 80
    },
    "data/companies_multiyear.json": {
      "code": "600886",
      "name": "国投电力",
      "group": "clean",
      "assurance": false,
      "years": {
        "2023": {
          "scope1_tco2": 50018850,
          "scope2_tco2": 903413,
          "power_gen_gwh": 161966
        },
        "2024": {
          "scope1_tco2": 48808719,
          "scope2_tco2": 698000,
          "power_gen_gwh": 172072
        }
      },
      "status": "verified",
      "self_reported_intensity_g_per_kwh": null,
      "clean_energy_share_pct": 70.42,
      "clean_energy_share_basis": "控股清洁能源装机容量占比（口径与大唐、浙能严格一致）",
      "green_capex_abs_yi": 8.61,
      "green_capex_total_yi": 217.7,
      "green_capex_note": "环保投入 7.458 亿 + 节能投入 1.156 亿 = 8.61 亿元 ÷ 资本开支 217.7 亿元 = 3.96%",
      "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +64.91%，巨额配额结余，形成正贡献",
      "previous_year": {
        "green_capex_pct": 2.0,
        "clean_energy_pct": 12.05
      },
      "note": ""
    },
    "data/carbon_disclosure_ledger.json": {
      "code": "600886",
      "name": "国投电力",
      "group": "clean",
      "type": "水电为主",
      "years": {
        "2023": {
          "scope1_tco2": 50018850,
          "scope2_tco2": 903413,
          "power_gen_gwh": 161966
        },
        "2024": {
          "scope1_tco2": 48808719,
          "scope2_tco2": 698000,
          "power_gen_gwh": 172072
        }
      },
      "clean_energy_share_pct": 70.42,
      "clean_energy_share_basis": "控股清洁能源装机容量占比（口径与大唐、浙能严格一致）",
      "green_capex_abs_yi": 8.61,
      "green_capex_total_yi": 217.7,
      "green_capex_note": "环保投入 7.458 亿 + 节能投入 1.156 亿 = 8.61 亿元 ÷ 资本开支 217.7 亿元 = 3.96%",
      "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +64.91%，巨额配额结余，形成正贡献",
      "previous_year": {
        "green_capex_pct": 2.0,
        "clean_energy_pct": 12.05
      },
      "status": "verified",
      "sources": [
        "2024年环境、社会与治理报告 关键绩效表（第一部分：环境范畴）",
        "2024 年年度报告（现金流量表：资本开支）",
        "报告正文：2024 年控股企业累计完成发电量 1720.72 亿千瓦时，同比增长 6.24%"
      ]
    },
    "data/esg_announcements.json": {
      "name": "国投电力",
      "reports": [
        {
          "title": "国投电力控股股份有限公司2021年度社会责任报告",
          "url": "finalpage/2022-04-29/1213224206.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "国投电力控股股份有限公司2020年企业社会责任报告",
          "url": "finalpage/2021-04-29/1209858500.PDF",
          "kw": "社会责任报告"
        }
      ]
    },
    "data/raw/esg_announcements.json": {
      "name": "国投电力",
      "reports": [
        {
          "title": "国投电力控股股份有限公司2021年度社会责任报告",
          "url": "finalpage/2022-04-29/1213224206.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "国投电力控股股份有限公司2020年企业社会责任报告",
          "url": "finalpage/2021-04-29/1209858500.PDF",
          "kw": "社会责任报告"
        }
      ]
    },
    "data/processed/radar_attachment_snapshot.json": {
      "code": "600886",
      "name": "国投电力",
      "group": "clean",
      "type": "水电为主",
      "years": {
        "2023": {
          "scope1_tco2": 50018850,
          "scope2_tco2": 903413,
          "power_gen_gwh": 161966
        },
        "2024": {
          "scope1_tco2": 48808719,
          "scope2_tco2": 698000,
          "power_gen_gwh": 172072
        }
      },
      "clean_energy_share_pct": 67.2,
      "clean_energy_share_basis": "补充观测值（ESG口径，时点与年报不同，非年报值）；2024年报原文为70.42%（截至2024年底控股清洁能源装机占比），现行台账采用70.42",
      "green_capex_abs_yi": 8.61,
      "green_capex_total_yi": 217.7,
      "green_capex_note": "环保投入 7.458 亿 + 节能投入 1.156 亿 = 8.61 亿元 ÷ 资本开支 217.7 亿元 = 3.96%",
      "carbon_cost_note": "较全国基准线 750 gCO₂/kWh 偏离 +61.64%，巨额配额结余，形成正贡献",
      "previous_year": {
        "green_capex_pct": 2.0,
        "clean_energy_pct": 12.05
      },
      "status": "verified",
      "sources": [
        "2024年环境、社会与治理报告 关键绩效表（第一部分：环境范畴）",
        "2024 年年度报告（现金流量表：资本开支）",
        "报告正文：2024 年控股企业累计完成发电量 1720.72 亿千瓦时，同比增长 6.24%"
      ]
    },
    "data/待填_多年度环境绩效.csv": [
      {
        "证券代码": "600886",
        "企业名称": "国投电力",
        "报告年度": "2022",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600886",
        "企业名称": "国投电力",
        "报告年度": "2023",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600886",
        "企业名称": "国投电力",
        "报告年度": "2024",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      }
    ],
    "server/data_store.py::DISCLOSURES": {
      "name": "国投电力",
      "type": "水电为主",
      "scope1_tco2": 18000000,
      "scope2_tco2": 400000,
      "power_gen_gwh": 155000,
      "coal_consumed_wan_t": 500,
      "revenue_100m": 58000,
      "scope3_disclosed": false,
      "env_penalty_count": 0,
      "disclosure_years": 3,
      "water_use_wan_t": 3200,
      "wastewater_treated_pct": 96.0,
      "solid_waste_util_pct": 89.0,
      "energy_intensity_gj_per_mwh": 3.5,
      "safe_prod_invest_pct": 1.6,
      "employee_training_h": 44,
      "board_indep_pct": 41.7,
      "esg_committee": true
    }
  }
}
```

## 长江电力（600900）
原版演示值 · 年度未确认 / 年度：演示当前期 / V3.2：未取得可复算输入

### 原始轴值与参考分
|轴|单位|本期原始值|本期参考分|上期原始值|上期参考分|
|---|---|---|---|---|---|
| ① 存量能效 | gCO₂/kWh | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ② 边际改善 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ③ 绿色投入强度 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ④ 低碳结构 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |
| ⑤ 碳合规与边际收益 | % | 缺失（null） | 缺失（null） | 缺失（null） | 缺失（null） |

### 画像 / 全部年度 / 全源字段 / 全模型输出
```json
{
  "code": "600900",
  "name": "长江电力",
  "profile": {
    "radar": {
      "kind": "base100",
      "previous_year": null,
      "current_year": "演示当前期",
      "ticks": [
        0,
        50,
        100,
        150,
        200
      ],
      "axes": [
        {
          "key": "scope1",
          "label": "scope1",
          "index": null,
          "current_value": 900000,
          "previous_value": null,
          "unit": "tCO2"
        },
        {
          "key": "scope2",
          "label": "scope2",
          "index": null,
          "current_value": 150000,
          "previous_value": null,
          "unit": "tCO2"
        },
        {
          "key": "production",
          "label": "发电量",
          "index": null,
          "current_value": 276000,
          "previous_value": null,
          "unit": "GWh"
        },
        {
          "key": "intensity",
          "label": "排放强度",
          "index": null,
          "current_value": 3.8043478260869565,
          "previous_value": null,
          "unit": "kgCO2/MWh"
        }
      ],
      "meaning": "基期=100的相对规模，不是绩效评分，不按面积评价好坏"
    },
    "code": "600900",
    "name": "长江电力",
    "type": "水电",
    "year": "演示当前期",
    "previous_year": null,
    "data_kind": "demo",
    "quality_label": "原版演示值 · 年度未确认",
    "comparability": "unavailable",
    "scope2_method": "unknown",
    "metrics": {
      "scope1": {
        "value": 900000,
        "unit": "tCO2"
      },
      "scope2": {
        "value": 150000,
        "unit": "tCO2"
      },
      "total": {
        "value": 1050000,
        "unit": "tCO2"
      },
      "production": {
        "value": 276000,
        "unit": "GWh"
      },
      "intensity": {
        "value": 3.8043478260869565,
        "unit": "kgCO2/MWh"
      }
    },
    "changes": {
      "scope1": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "scope2": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "total": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "production": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      },
      "intensity": {
        "value": null,
        "reason": "缺同口径上一期、前值非正或数值超限"
      }
    },
    "trend": [
      {
        "year": "演示当前期",
        "scope1": 900000,
        "scope2": 150000,
        "total": 1050000,
        "production": 276000,
        "intensity": 3.8043478260869565
      }
    ],
    "sources": [
      {
        "source_id": "600900-source-1",
        "title": "原data_store.DISCLOSURES演示数据",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E9%95%BF%E6%B1%9F%E7%94%B5%E5%8A%9B%20%E5%8E%9Fdata_store.DISCLOSURES%E6%BC%94%E7%A4%BA%E6%95%B0%E6%8D%AE",
        "source_kind": "search"
      },
      {
        "source_id": "600900-public-index",
        "title": "长江电力2023年度环境、社会和治理（ESG）报告",
        "metric_keys": [],
        "location": "历史报告索引，未确认对应本次年度观测",
        "status": "index_only",
        "hash_kind": "metadata_not_pdf",
        "url": "https://static.cninfo.com.cn/finalpage/2024-04-30/1219922583.PDF",
        "source_kind": "report_index"
      }
    ],
    "methods": [
      {
        "key": "scope1",
        "name": "Scope 1直接排放",
        "formula": "E₁ = Σ 活动数据 × 对应排放因子",
        "meaning": "企业控制范围内燃烧及工艺排放；本平台使用提供的披露值，不自行核算原始活动数据。",
        "basis_name": "GHG Protocol Corporate Standard（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "因子、温室气体及组织边界须核对原报告；概览不是已核验完整清单。"
      },
      {
        "key": "scope2",
        "name": "Scope 2外购能源排放",
        "formula": "E₂ = Σ 外购电／热／蒸汽／冷量 × 对应因子",
        "meaning": "区分地点法与市场法；两种方法不可相加为双份排放。",
        "basis_name": "GHG Protocol Scope 2 Guidance（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/scope-2-guidance",
        "limitation": "市场法合同工具需满足质量条件；当前附件方法未确认。"
      },
      {
        "key": "total",
        "name": "选定方法后的范围1+2汇总",
        "formula": "E = E₁ + E₂（同年度、边界及气体口径）",
        "meaning": "表示企业排放规模，不等于碳市场履约排放，也不直接惩罚大企业。",
        "basis_name": "GHG企业清单范围分列原则；合计为本项目展示",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "CO₂与CO₂e不得悄悄互换；总量不转换为信用风险分。"
      },
      {
        "key": "intensity",
        "name": "电力业务生产强度",
        "formula": "CI = E ÷ G；吨／GWh数值＝kg／MWh",
        "meaning": "区分单位产出效率与企业规模，避免只观察总量。",
        "basis_name": "TPI电力v5（已读方法摘要，部门强度思路）",
        "basis_url": "https://www.transitionpathwayinitiative.org/knowledge-hub/methodologies/electricity-utilities-methodology-v5",
        "limitation": "本项目Scope1+2分子不能冒称完全复制TPI详细方法；其他行业需另换分母。"
      },
      {
        "key": "change",
        "name": "同口径年度变化",
        "formula": "Δx = (xₜ ÷ xₜ₋₁ − 1) × 100%",
        "meaning": "并列排放、产量及强度变化，辅助解释扩产与效率；产量下降不天然更好。",
        "basis_name": "数学同比；GHG一致性与透明核算目的",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "边界重述、方法变更或前值非正时不计算；下降不证明主动转型。"
      }
    ],
    "findings": [
      {
        "title": "先核对边界和Scope2方法",
        "detail": "附件未提供完整组织边界、气体基准和地点/市场法定位；图中复算明确属于假设演示，不是确认可比。",
        "severity": "warning"
      },
      {
        "title": "无需为五维补造数据",
        "detail": "移除无可靠披露的投入/结构计分轴；保留相关原值为未核验补充信息，不计算综合评级。",
        "severity": "info"
      }
    ],
    "method_version": "scope12-transition-1.9.4",
    "limitations": [
      "不计算人为综合分或信用评级。",
      "资料属于演示/附件，原报告未独立核验；只有公式可复算。",
      "Scope1/2聚焦不是完整企业足迹或完整IFRS/GRI合规评估。",
      "银行价值是版本核验、口径解释与待核事项，而不是已证实预测信用风险。"
    ],
    "optional_observations": {
      "warning": "数据原年度标签与历史序列不一致，未拼接Scope2历史或伪造同比。"
    }
  },
  "main_quant": null,
  "radar_v32": [
    {
      "key": "intensity",
      "short": "存量能效",
      "label": "① 存量能效",
      "unit": "gCO₂/kWh",
      "desc": "度电碳排放强度，反映机组技术是否先进",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "trend",
      "short": "边际改善",
      "label": "② 边际改善",
      "unit": "%",
      "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "green_capex",
      "short": "绿色投入",
      "label": "③ 绿色投入强度",
      "unit": "%",
      "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "structure",
      "short": "低碳结构",
      "label": "④ 低碳结构",
      "unit": "%",
      "desc": "控股清洁能源装机容量占比，长期结构韧性",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    },
    {
      "key": "carbon_compliance",
      "short": "碳合规承压",
      "label": "⑤ 碳合规与边际收益",
      "unit": "%",
      "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
      "value": null,
      "score": null,
      "available": false,
      "note": "未取得当前V3.2可复算年度输入；不以演示值替代"
    }
  ],
  "public_source_records": {
    "data/companies.json": null,
    "data/companies_multiyear.json": null,
    "data/carbon_disclosure_ledger.json": null,
    "data/esg_announcements.json": null,
    "data/raw/esg_announcements.json": {
      "name": "长江电力",
      "reports": [
        {
          "title": "长江电力2022年度社会责任报告",
          "url": "finalpage/2023-04-28/1216664105.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "长江电力2021年度社会责任报告",
          "url": "finalpage/2022-04-30/1213270603.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "长江电力2020年度社会责任报告",
          "url": "finalpage/2021-04-30/1209875193.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "长江电力2024年度环境、社会和治理（ESG）报告",
          "url": "finalpage/2025-04-30/1223421180.PDF",
          "kw": "ESG"
        },
        {
          "title": "长江电力2023年度环境、社会和治理（ESG）报告",
          "url": "finalpage/2024-04-30/1219922583.PDF",
          "kw": "ESG"
        }
      ]
    },
    "data/processed/radar_attachment_snapshot.json": null,
    "data/待填_多年度环境绩效.csv": [
      {
        "证券代码": "600900",
        "企业名称": "长江电力",
        "报告年度": "2022",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600900",
        "企业名称": "长江电力",
        "报告年度": "2023",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600900",
        "企业名称": "长江电力",
        "报告年度": "2024",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      }
    ],
    "server/data_store.py::DISCLOSURES": {
      "name": "长江电力",
      "type": "水电",
      "scope1_tco2": 900000,
      "scope2_tco2": 150000,
      "power_gen_gwh": 276000,
      "coal_consumed_wan_t": 0,
      "revenue_100m": 78000,
      "scope3_disclosed": true,
      "env_penalty_count": 0,
      "disclosure_years": 5,
      "water_use_wan_t": 950,
      "wastewater_treated_pct": 99.0,
      "solid_waste_util_pct": 96.0,
      "energy_intensity_gj_per_mwh": 0.6,
      "safe_prod_invest_pct": 1.8,
      "employee_training_h": 52,
      "board_indep_pct": 44.4,
      "esg_committee": true
    }
  }
}
```

## 浙能电力（600023）
附件观测 · 未独立核验 / 年度：2024 / V3.2：2024；综合参考分 38.2（非信用结论）

### 原始轴值与参考分
|轴|单位|本期原始值|本期参考分|上期原始值|上期参考分|
|---|---|---|---|---|---|
| ① 存量能效 | gCO₂/kWh | 872.75 | 12.7 | 870.12 | 13.0 |
| ② 边际改善 | % | 0.3 | 49.2 | -1.49 | 53.7 |
| ③ 绿色投入强度 | % | 3.72 | 74.4 | 1.86 | 37.2 |
| ④ 低碳结构 | % | 10.87 | 10.9 | 9.0 | 9.0 |
| ⑤ 碳合规与边际收益 | % | -6.43 | 43.6 | -6.11 | 43.9 |

### 画像 / 全部年度 / 全源字段 / 全模型输出
```json
{
  "code": "600023",
  "name": "浙能电力",
  "profile": {
    "radar": {
      "kind": "base100",
      "previous_year": 2023,
      "current_year": 2024,
      "ticks": [
        0,
        50,
        100,
        150,
        200
      ],
      "axes": [
        {
          "key": "scope1",
          "label": "scope1",
          "index": 106.88368031101221,
          "current_value": 151762000,
          "previous_value": 141988000,
          "unit": "tCO2"
        },
        {
          "key": "scope2",
          "label": "scope2",
          "index": 110.20408163265304,
          "current_value": 54000,
          "previous_value": 49000,
          "unit": "tCO2"
        },
        {
          "key": "production",
          "label": "发电量",
          "index": 106.56342273245201,
          "current_value": 173952,
          "previous_value": 163238,
          "unit": "GWh"
        },
        {
          "key": "intensity",
          "label": "排放强度",
          "index": 100.30160729088597,
          "current_value": 872.7465047829286,
          "previous_value": 870.1221529300775,
          "unit": "kgCO2/MWh"
        }
      ],
      "meaning": "基期=100的相对规模，不是绩效评分，不按面积评价好坏"
    },
    "code": "600023",
    "name": "浙能电力",
    "type": "火电",
    "year": 2024,
    "previous_year": 2023,
    "data_kind": "attachment_unverified",
    "quality_label": "附件观测 · 未独立核验",
    "comparability": "assumed_comparable_for_demo_only",
    "scope2_method": "unknown",
    "metrics": {
      "scope1": {
        "value": 151762000,
        "unit": "tCO2"
      },
      "scope2": {
        "value": 54000,
        "unit": "tCO2"
      },
      "total": {
        "value": 151816000,
        "unit": "tCO2"
      },
      "production": {
        "value": 173952,
        "unit": "GWh"
      },
      "intensity": {
        "value": 872.7465047829286,
        "unit": "kgCO2/MWh"
      }
    },
    "changes": {
      "scope1": {
        "value": 6.883680311012208,
        "reason": null
      },
      "scope2": {
        "value": 10.20408163265305,
        "reason": null
      },
      "total": {
        "value": 6.884825784830717,
        "reason": null
      },
      "production": {
        "value": 6.563422732452007,
        "reason": null
      },
      "intensity": {
        "value": 0.3016072908859746,
        "reason": null
      }
    },
    "trend": [
      {
        "year": 2022,
        "scope1": 134210000,
        "scope2": 42000,
        "total": 134252000,
        "production": 151986,
        "intensity": 883.3182003605596
      },
      {
        "year": 2023,
        "scope1": 141988000,
        "scope2": 49000,
        "total": 142037000,
        "production": 163238,
        "intensity": 870.1221529300775
      },
      {
        "year": 2024,
        "scope1": 151762000,
        "scope2": 54000,
        "total": 151816000,
        "production": 173952,
        "intensity": 872.7465047829286
      }
    ],
    "sources": [
      {
        "source_id": "600023-source-1",
        "title": "2024年可持续发展暨环境、社会和治理（ESG）报告 关键绩效表",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E6%B5%99%E8%83%BD%E7%94%B5%E5%8A%9B%202024%E5%B9%B4%E5%8F%AF%E6%8C%81%E7%BB%AD%E5%8F%91%E5%B1%95%E6%9A%A8%E7%8E%AF%E5%A2%83%E3%80%81%E7%A4%BE%E4%BC%9A%E5%92%8C%E6%B2%BB%E7%90%86%EF%BC%88ESG%EF%BC%89%E6%8A%A5%E5%91%8A%20%E5%85%B3%E9%94%AE%E7%BB%A9%E6%95%88%E8%A1%A8",
        "source_kind": "search"
      },
      {
        "source_id": "600023-source-2",
        "title": "2024 年年度报告（现金流量表：资本开支、清洁能源装机）",
        "metric_keys": [
          "scope1",
          "scope2",
          "production"
        ],
        "location": "仅提供报告/来源标题，未核对页码与原文数值",
        "status": "unverified",
        "hash_kind": "metadata_not_pdf",
        "url": "https://www.cninfo.com.cn/new/fulltextSearch?keyWord=%E6%B5%99%E8%83%BD%E7%94%B5%E5%8A%9B%202024%20%E5%B9%B4%E5%B9%B4%E5%BA%A6%E6%8A%A5%E5%91%8A%EF%BC%88%E7%8E%B0%E9%87%91%E6%B5%81%E9%87%8F%E8%A1%A8%EF%BC%9A%E8%B5%84%E6%9C%AC%E5%BC%80%E6%94%AF%E3%80%81%E6%B8%85%E6%B4%81%E8%83%BD%E6%BA%90%E8%A3%85%E6%9C%BA%EF%BC%89",
        "source_kind": "search"
      },
      {
        "source_id": "600023-public-index",
        "title": "2024年可持续发展暨环境、社会和治理（ESG）报告",
        "metric_keys": [],
        "location": "历史报告索引，未确认对应本次年度观测",
        "status": "index_only",
        "hash_kind": "metadata_not_pdf",
        "url": "https://static.cninfo.com.cn/finalpage/2025-04-29/1223358270.PDF",
        "source_kind": "report_index"
      }
    ],
    "methods": [
      {
        "key": "scope1",
        "name": "Scope 1直接排放",
        "formula": "E₁ = Σ 活动数据 × 对应排放因子",
        "meaning": "企业控制范围内燃烧及工艺排放；本平台使用提供的披露值，不自行核算原始活动数据。",
        "basis_name": "GHG Protocol Corporate Standard（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "因子、温室气体及组织边界须核对原报告；概览不是已核验完整清单。"
      },
      {
        "key": "scope2",
        "name": "Scope 2外购能源排放",
        "formula": "E₂ = Σ 外购电／热／蒸汽／冷量 × 对应因子",
        "meaning": "区分地点法与市场法；两种方法不可相加为双份排放。",
        "basis_name": "GHG Protocol Scope 2 Guidance（已读官方概览）",
        "basis_url": "https://ghgprotocol.org/scope-2-guidance",
        "limitation": "市场法合同工具需满足质量条件；当前附件方法未确认。"
      },
      {
        "key": "total",
        "name": "选定方法后的范围1+2汇总",
        "formula": "E = E₁ + E₂（同年度、边界及气体口径）",
        "meaning": "表示企业排放规模，不等于碳市场履约排放，也不直接惩罚大企业。",
        "basis_name": "GHG企业清单范围分列原则；合计为本项目展示",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "CO₂与CO₂e不得悄悄互换；总量不转换为信用风险分。"
      },
      {
        "key": "intensity",
        "name": "电力业务生产强度",
        "formula": "CI = E ÷ G；吨／GWh数值＝kg／MWh",
        "meaning": "区分单位产出效率与企业规模，避免只观察总量。",
        "basis_name": "TPI电力v5（已读方法摘要，部门强度思路）",
        "basis_url": "https://www.transitionpathwayinitiative.org/knowledge-hub/methodologies/electricity-utilities-methodology-v5",
        "limitation": "本项目Scope1+2分子不能冒称完全复制TPI详细方法；其他行业需另换分母。"
      },
      {
        "key": "change",
        "name": "同口径年度变化",
        "formula": "Δx = (xₜ ÷ xₜ₋₁ − 1) × 100%",
        "meaning": "并列排放、产量及强度变化，辅助解释扩产与效率；产量下降不天然更好。",
        "basis_name": "数学同比；GHG一致性与透明核算目的",
        "basis_url": "https://ghgprotocol.org/corporate-standard",
        "limitation": "边界重述、方法变更或前值非正时不计算；下降不证明主动转型。"
      }
    ],
    "findings": [
      {
        "title": "先核对边界和Scope2方法",
        "detail": "附件未提供完整组织边界、气体基准和地点/市场法定位；图中复算明确属于假设演示，不是确认可比。",
        "severity": "warning"
      },
      {
        "title": "无需为五维补造数据",
        "detail": "移除无可靠披露的投入/结构计分轴；保留相关原值为未核验补充信息，不计算综合评级。",
        "severity": "info"
      }
    ],
    "method_version": "scope12-transition-1.9.4",
    "limitations": [
      "不计算人为综合分或信用评级。",
      "资料属于演示/附件，原报告未独立核验；只有公式可复算。",
      "Scope1/2聚焦不是完整企业足迹或完整IFRS/GRI合规评估。",
      "银行价值是版本核验、口径解释与待核事项，而不是已证实预测信用风险。"
    ],
    "optional_observations": {
      "clean_capacity_share_pct": 10.87,
      "environmental_spending_note": "环保总投入 3.60 亿元 ÷ 现金流总资本开支 96.8 亿元 = 3.72%",
      "warning": "装机占比、一般环保费用仅作补充信息，不替代发电结构或低碳资本支出。"
    }
  },
  "main_quant": {
    "code": "600023",
    "name": "浙能电力",
    "type": "火电",
    "carbon": {
      "code": "600023",
      "name": "浙能电力",
      "group": "thermal",
      "year": 2024,
      "model_version": "GreenTrace-Power V3.2 (等权五维雷达)",
      "available": true,
      "ci_g_per_kwh": 872.7,
      "change_rate_pct": 0.3,
      "change_rate_basis": "同比",
      "clean_energy_share_pct": 10.87,
      "clean_energy_share_basis": "控股清洁能源装机容量占比（年报披露值）",
      "score_intensity": 12.7,
      "score_trend": 49.2,
      "score_green_capex": 74.4,
      "score_structure": 10.9,
      "score_carbon_compliance": 43.6,
      "weights_applied": {
        "intensity": 0.2,
        "trend": 0.2,
        "green_capex": 0.2,
        "structure": 0.2,
        "carbon_compliance": 0.2
      },
      "carbon_score": 38.2,
      "rating": "B-",
      "rating_label": "碳配额承压资产",
      "benchmark_tco2_per_mwh": 0.82,
      "benchmark_label": "全国碳市场发电行业基准线",
      "deviation_vs_baseline_pct": 6.4,
      "missing": [],
      "data_coverage": 100,
      "years_used": [
        2022,
        2023,
        2024
      ],
      "group_label": "火电组",
      "disclosure_status": "verified",
      "ledger_note": "",
      "confidence_grade": "完整",
      "credit": {
        "delta_bp": 22,
        "action": "不享受降息，且上浮 22 个 BP；需开立节能改造专项监管账户"
      },
      "self_reported_intensity_g_per_kwh": null,
      "baseline_version": "全国碳市场发电行业基准线 2024",
      "sources": [
        "2024年可持续发展暨环境、社会和治理（ESG）报告 关键绩效表",
        "2024 年年度报告（现金流量表：资本开支、清洁能源装机）"
      ],
      "radar": [
        {
          "key": "intensity",
          "short": "存量能效",
          "label": "① 存量能效",
          "unit": "gCO₂/kWh",
          "desc": "度电碳排放强度，反映机组技术是否先进",
          "value": 872.75,
          "score": 12.7,
          "available": true,
          "note": ""
        },
        {
          "key": "trend",
          "short": "边际改善",
          "label": "② 边际改善",
          "unit": "%",
          "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
          "value": 0.3,
          "score": 49.2,
          "available": true,
          "note": "口径：同比"
        },
        {
          "key": "green_capex",
          "short": "绿色投入",
          "label": "③ 绿色投入强度",
          "unit": "%",
          "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
          "value": 3.72,
          "score": 74.4,
          "available": true,
          "note": "环保总投入 3.60 亿元 ÷ 现金流总资本开支 96.8 亿元 = 3.72%"
        },
        {
          "key": "structure",
          "short": "低碳结构",
          "label": "④ 低碳结构",
          "unit": "%",
          "desc": "控股清洁能源装机容量占比，长期结构韧性",
          "value": 10.87,
          "score": 10.9,
          "available": true,
          "note": "口径：控股清洁能源装机容量占比（年报披露值）"
        },
        {
          "key": "carbon_compliance",
          "short": "碳合规承压",
          "label": "⑤ 碳合规与边际收益",
          "unit": "%",
          "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
          "value": -6.43,
          "score": 43.6,
          "available": true,
          "note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 −6.43%，配额存在缺口，需外购配额"
        }
      ],
      "radar_prev": [
        {
          "key": "intensity",
          "short": "存量能效",
          "label": "① 存量能效",
          "unit": "gCO₂/kWh",
          "desc": "度电碳排放强度，反映机组技术是否先进",
          "value": 870.12,
          "score": 13.0,
          "available": true,
          "note": "2023 年复算值"
        },
        {
          "key": "trend",
          "short": "边际改善",
          "label": "② 边际改善",
          "unit": "%",
          "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
          "value": -1.49,
          "score": 53.7,
          "available": true,
          "note": "口径：同比"
        },
        {
          "key": "green_capex",
          "short": "绿色投入",
          "label": "③ 绿色投入强度",
          "unit": "%",
          "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
          "value": 1.86,
          "score": 37.2,
          "available": true,
          "note": "上一年度披露值"
        },
        {
          "key": "structure",
          "short": "低碳结构",
          "label": "④ 低碳结构",
          "unit": "%",
          "desc": "控股清洁能源装机容量占比，长期结构韧性",
          "value": 9.0,
          "score": 9.0,
          "available": true,
          "note": "上一年度披露值"
        },
        {
          "key": "carbon_compliance",
          "short": "碳合规承压",
          "label": "⑤ 碳合规与边际收益",
          "unit": "%",
          "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
          "value": -6.11,
          "score": 43.9,
          "available": true,
          "note": "按 2023 年基准线同口径重算"
        }
      ],
      "radar_prev_year": 2023,
      "verdict": {
        "rating": "B-",
        "label": "碳配额承压资产",
        "action": "不享受降息；建议开立节能改造专项监管账户",
        "reason": "综合分 38.2 分（等权五维平均；实际生效 5 维，权重重新归一化后为 存量能效 20%、边际改善 20%、绿色投入 20%、低碳结构 20%、碳合规承压 20%）最强轴 ③ 绿色投入强度 74.4 分；最弱轴 ④ 低碳结构 10.9 分。优势轴：③ 绿色投入强度 74.4。承压轴（低于 50 分）：④ 低碳结构 10.9、① 存量能效 12.7、⑤ 碳合规与边际收益 43.6、② 边际改善 49.2。评级由综合分按固定档位表判定（≥60 为 B+，≥45 为 B，≥30 为 B−），可独立复算。",
        "score": 38.2,
        "weights_applied": {
          "intensity": 0.2,
          "trend": 0.2,
          "green_capex": 0.2,
          "structure": 0.2,
          "carbon_compliance": 0.2
        },
        "computable": true
      }
    },
    "scoring_method": {
      "model_version": "GreenTrace-Power V3.2 (等权五维雷达)",
      "intensity": "I =（范围一 + 范围二）÷ 全口径发电量，单位 gCO₂/kWh",
      "trend": "τ =（I 今年 − I 去年）÷ I 去年；不足两年时用多年度等效年化变化率",
      "structure_raw": "ρ = 控股清洁能源装机容量占比（年报 / ESG 报告披露值）",
      "dims": [
        {
          "label": "① 存量能效",
          "formula": "S① =（1000 − I）÷ 10，限定 [0, 100]"
        },
        {
          "label": "② 边际改善",
          "formula": "S② = 50 + 50 × tanh(−5 × τ)"
        },
        {
          "label": "③ 绿色投入强度",
          "formula": "S③ = 100 × 环保节能投入 ÷ 现金流总资本开支 ÷ 5，上限 100"
        },
        {
          "label": "④ 低碳结构",
          "formula": "S④ = 清洁能源装机占比，直接对应百分比"
        },
        {
          "label": "⑤ 碳合规与边际收益",
          "formula": "S⑤ = 50 +（基准线 − I）÷ 基准线 × 100，限定 [0, 100]"
        }
      ],
      "composite": "综合分 S = 五维等权平均（每维 20%）：S = 0.20×(S①+S②+S③+S④+S⑤)",
      "weights_note": "等权固定权重，每维 20%，真实参与综合分计算。选择等权是因为尚无实证证据表明某一维对信用风险的预测力更强；等权是可复算、可审计的中性基准。",
      "missing_rule": "缺失维度不臆测、不计 0 分；其权重在剩余可得维度上重新归一化",
      "rating_rule": "评级由综合分查固定档位表判定，无人工干预：≥90 为 AAA，≥80 为 AA，≥70 为 A，≥60 为 B+，≥45 为 B，≥30 为 B-，≥0 为 C",
      "baseline": "全国碳市场发电行业基准线（gCO₂/kWh）：2022 年 823、2023 年 820、2024 年 820",
      "credit": "信贷联动：Δr = −(S − 60) × 1 BP（高于 60 分下浮利率）",
      "disclaimer": "评分为样本内相对比较，非绝对评级；不构成第三方鉴证意见，不构成授信结论。"
    },
    "evidence": [
      {
        "field": "scope1_tco2 / scope2_tco2",
        "source": "浙能电力 年度报告及 ESG 报告披露",
        "note": "披露值，来源已索引"
      },
      {
        "field": "power_gen_gwh",
        "source": "浙能电力 年度报告 / ESG 报告披露",
        "note": "全口径发电量，作为强度分母"
      },
      {
        "field": "intensity",
        "source": "平台复算 =（范围一 + 范围二）÷ 发电量",
        "note": "统一口径；tCO₂/GWh 数值上等于 gCO₂/kWh"
      },
      {
        "field": "clean_energy_share",
        "source": "企业 ESG 报告披露",
        "note": "口径：控股清洁能源装机容量占比（年报披露值），用于结构维度打分（权重 0.25）"
      }
    ],
    "reports_count": 4,
    "reports": [
      {
        "title": "2023年度社会责任暨环境、社会和公司治理（ESG）报告",
        "url": "finalpage/2024-04-30/1219904672.PDF",
        "kw": "社会责任报告"
      },
      {
        "title": "2022年度社会责任暨环境、社会和公司治理（ESG）报告",
        "url": "finalpage/2023-04-28/1216648702.PDF",
        "kw": "社会责任报告"
      },
      {
        "title": "2021年度社会责任暨环境、社会和公司治理（ESG）报告",
        "url": "finalpage/2022-04-29/1213204420.PDF",
        "kw": "社会责任报告"
      },
      {
        "title": "2024年可持续发展暨环境、社会和治理（ESG）报告",
        "url": "finalpage/2025-04-29/1223358270.PDF",
        "kw": "可持续发展报告"
      }
    ]
  },
  "radar_v32": [
    {
      "key": "intensity",
      "short": "存量能效",
      "label": "① 存量能效",
      "unit": "gCO₂/kWh",
      "desc": "度电碳排放强度，反映机组技术是否先进",
      "value": 872.75,
      "score": 12.7,
      "available": true,
      "note": ""
    },
    {
      "key": "trend",
      "short": "边际改善",
      "label": "② 边际改善",
      "unit": "%",
      "desc": "碳强度年度变化率，负=减排；转型金融的核心看点",
      "value": 0.3,
      "score": 49.2,
      "available": true,
      "note": "口径：同比"
    },
    {
      "key": "green_capex",
      "short": "绿色投入",
      "label": "③ 绿色投入强度",
      "unit": "%",
      "desc": "环保节能投入 ÷ 现金流总资本开支，衡量真金白银的投入",
      "value": 3.72,
      "score": 74.4,
      "available": true,
      "note": "环保总投入 3.60 亿元 ÷ 现金流总资本开支 96.8 亿元 = 3.72%"
    },
    {
      "key": "structure",
      "short": "低碳结构",
      "label": "④ 低碳结构",
      "unit": "%",
      "desc": "控股清洁能源装机容量占比，长期结构韧性",
      "value": 10.87,
      "score": 10.9,
      "available": true,
      "note": "口径：控股清洁能源装机容量占比（年报披露值）"
    },
    {
      "key": "carbon_compliance",
      "short": "碳合规承压",
      "label": "⑤ 碳合规与边际收益",
      "unit": "%",
      "desc": "实际能效较全国碳市场基准线的偏离度，负偏离=需外购配额、现金流承压",
      "value": -6.43,
      "score": 43.6,
      "available": true,
      "note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 −6.43%，配额存在缺口，需外购配额"
    }
  ],
  "public_source_records": {
    "data/companies.json": {
      "code": "600023",
      "name": "浙能电力",
      "type": "火电",
      "group": "thermal",
      "scope1_tco2": 320000000,
      "scope2_tco2": 7000000,
      "power_gen_gwh": 340000,
      "water_wan_ton": 11800,
      "wastewater_rate_pct": 94.0,
      "solid_waste_reuse_pct": 91.0,
      "energy_gj_per_mwh": 9.9,
      "scope3_disclosed": false,
      "env_penalties": 1,
      "safety_spend_pct": 1.2,
      "training_hours": 36,
      "esg_years": 4,
      "indep_director_pct": 35.0,
      "esg_committee": false,
      "completeness_pct": 80
    },
    "data/companies_multiyear.json": {
      "code": "600023",
      "name": "浙能电力",
      "group": "thermal",
      "assurance": false,
      "years": {
        "2022": {
          "scope1_tco2": 134210000,
          "scope2_tco2": 42000,
          "power_gen_gwh": 151986
        },
        "2023": {
          "scope1_tco2": 141988000,
          "scope2_tco2": 49000,
          "power_gen_gwh": 163238
        },
        "2024": {
          "scope1_tco2": 151762000,
          "scope2_tco2": 54000,
          "power_gen_gwh": 173952
        }
      },
      "status": "verified",
      "self_reported_intensity_g_per_kwh": null,
      "clean_energy_share_pct": 10.87,
      "clean_energy_share_basis": "控股清洁能源装机容量占比（年报披露值）",
      "green_capex_abs_yi": 3.6,
      "green_capex_total_yi": 96.8,
      "green_capex_note": "环保总投入 3.60 亿元 ÷ 现金流总资本开支 96.8 亿元 = 3.72%",
      "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 −6.43%，配额存在缺口，需外购配额",
      "previous_year": {
        "green_capex_pct": 1.86,
        "clean_energy_pct": 9.0
      },
      "note": ""
    },
    "data/carbon_disclosure_ledger.json": {
      "code": "600023",
      "name": "浙能电力",
      "group": "thermal",
      "type": "火电",
      "years": {
        "2022": {
          "scope1_tco2": 134210000,
          "scope2_tco2": 42000,
          "power_gen_gwh": 151986
        },
        "2023": {
          "scope1_tco2": 141988000,
          "scope2_tco2": 49000,
          "power_gen_gwh": 163238
        },
        "2024": {
          "scope1_tco2": 151762000,
          "scope2_tco2": 54000,
          "power_gen_gwh": 173952
        }
      },
      "clean_energy_share_pct": 10.87,
      "clean_energy_share_basis": "控股清洁能源装机容量占比（年报披露值）",
      "green_capex_abs_yi": 3.6,
      "green_capex_total_yi": 96.8,
      "green_capex_note": "环保总投入 3.60 亿元 ÷ 现金流总资本开支 96.8 亿元 = 3.72%",
      "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 −6.43%，配额存在缺口，需外购配额",
      "previous_year": {
        "green_capex_pct": 1.86,
        "clean_energy_pct": 9.0
      },
      "status": "verified",
      "sources": [
        "2024年可持续发展暨环境、社会和治理（ESG）报告 关键绩效表",
        "2024 年年度报告（现金流量表：资本开支、清洁能源装机）"
      ]
    },
    "data/esg_announcements.json": {
      "name": "浙能电力",
      "reports": [
        {
          "title": "2023年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2024-04-30/1219904672.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2022年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2023-04-28/1216648702.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2021年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2022-04-29/1213204420.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2024年可持续发展暨环境、社会和治理（ESG）报告",
          "url": "finalpage/2025-04-29/1223358270.PDF",
          "kw": "可持续发展报告"
        }
      ]
    },
    "data/raw/esg_announcements.json": {
      "name": "浙能电力",
      "reports": [
        {
          "title": "2023年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2024-04-30/1219904672.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2022年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2023-04-28/1216648702.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2021年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2022-04-29/1213204420.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2024年可持续发展暨环境、社会和治理（ESG）报告",
          "url": "finalpage/2025-04-29/1223358270.PDF",
          "kw": "可持续发展报告"
        }
      ]
    },
    "data/processed/radar_attachment_snapshot.json": {
      "code": "600023",
      "name": "浙能电力",
      "group": "thermal",
      "type": "火电",
      "years": {
        "2022": {
          "scope1_tco2": 134210000,
          "scope2_tco2": 42000,
          "power_gen_gwh": 151986
        },
        "2023": {
          "scope1_tco2": 141988000,
          "scope2_tco2": 49000,
          "power_gen_gwh": 163238
        },
        "2024": {
          "scope1_tco2": 151762000,
          "scope2_tco2": 54000,
          "power_gen_gwh": 173952
        }
      },
      "clean_energy_share_pct": 10.87,
      "clean_energy_share_basis": "控股清洁能源装机容量占比（年报披露值）",
      "green_capex_abs_yi": 3.6,
      "green_capex_total_yi": 96.8,
      "green_capex_note": "环保总投入 3.60 亿元 ÷ 现金流总资本开支 96.8 亿元 = 3.72%",
      "carbon_cost_note": "较全国基准线 750 gCO₂/kWh 偏离 −16.36%，配额严重超标，需外购配额",
      "previous_year": {
        "green_capex_pct": 1.86,
        "clean_energy_pct": 9.0
      },
      "status": "verified",
      "sources": [
        "2024年可持续发展暨环境、社会和治理（ESG）报告 关键绩效表",
        "2024 年年度报告（现金流量表：资本开支、清洁能源装机）"
      ]
    },
    "data/待填_多年度环境绩效.csv": [
      {
        "证券代码": "600023",
        "企业名称": "浙能电力",
        "报告年度": "2022",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600023",
        "企业名称": "浙能电力",
        "报告年度": "2023",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      },
      {
        "证券代码": "600023",
        "企业名称": "浙能电力",
        "报告年度": "2024",
        "直接排放_万吨CO2": "",
        "间接排放_万吨CO2": "",
        "发电量_亿千瓦时": "",
        "排放强度_克每千瓦时": "",
        "数据来源": "待填"
      }
    ],
    "server/data_store.py::DISCLOSURES": {
      "name": "浙能电力",
      "type": "火电",
      "scope1_tco2": 160000000,
      "scope2_tco2": 3000000,
      "power_gen_gwh": 170000,
      "coal_consumed_wan_t": 6200,
      "revenue_100m": 98000,
      "scope3_disclosed": false,
      "env_penalty_count": 1,
      "disclosure_years": 4,
      "water_use_wan_t": 11800,
      "wastewater_treated_pct": 94.0,
      "solid_waste_util_pct": 91.0,
      "energy_intensity_gj_per_mwh": 9.9,
      "safe_prod_invest_pct": 1.2,
      "employee_training_h": 36,
      "board_indep_pct": 35.0,
      "esg_committee": false
    }
  }
}
```

## 全部公开数据源（全字段与全部年份）
```json
{
  "data/companies.json": {
    "_meta": {
      "title": "绿鉴 ESG 样本数据集（8 家电力上市公司）",
      "disclaimer": "企业披露值为基于公开报告的演示数据集，不构成第三方鉴证意见，不构成授信结论。",
      "source": "企业 2020-2023 年度社会责任报告 / 可持续发展报告（巨潮资讯网）",
      "fields": {
        "scope1_tco2": "范围一直接排放，tCO₂，企业披露值",
        "scope2_tco2": "范围二外购能源间接排放，tCO₂，企业披露值",
        "power_gen_gwh": "发电量，GWh，企业披露值",
        "water_wan_ton": "水耗，万吨/年",
        "wastewater_rate_pct": "废水处理率，%",
        "solid_waste_reuse_pct": "固废综合利用率，%",
        "energy_gj_per_mwh": "供电能耗，GJ/MWh",
        "scope3_disclosed": "是否披露范围三排放",
        "env_penalties": "环境处罚记录数",
        "safety_spend_pct": "安全投入占营收，%",
        "training_hours": "人均培训，学时/年",
        "esg_years": "ESG/社会责任报告披露年限",
        "indep_director_pct": "独立董事占比，%",
        "esg_committee": "是否设立 ESG 委员会",
        "completeness_pct": "数据完整度，%（演示口径：披露字段数 / 应披露字段数）"
      },
      "note": "本样本仅保留有可复算碳数据的三家企业；被移除企业的完整数据见 _archived_companies.json"
    },
    "companies": [
      {
        "code": "601991",
        "name": "大唐发电",
        "type": "火电",
        "group": "thermal",
        "scope1_tco2": 210000000,
        "scope2_tco2": 4000000,
        "power_gen_gwh": 310000,
        "water_wan_ton": 15200,
        "wastewater_rate_pct": 93.0,
        "solid_waste_reuse_pct": 88.0,
        "energy_gj_per_mwh": 10.1,
        "scope3_disclosed": false,
        "env_penalties": 1,
        "safety_spend_pct": 1.1,
        "training_hours": 35,
        "esg_years": 3,
        "indep_director_pct": 33.3,
        "esg_committee": false,
        "completeness_pct": 80
      },
      {
        "code": "600023",
        "name": "浙能电力",
        "type": "火电",
        "group": "thermal",
        "scope1_tco2": 320000000,
        "scope2_tco2": 7000000,
        "power_gen_gwh": 340000,
        "water_wan_ton": 11800,
        "wastewater_rate_pct": 94.0,
        "solid_waste_reuse_pct": 91.0,
        "energy_gj_per_mwh": 9.9,
        "scope3_disclosed": false,
        "env_penalties": 1,
        "safety_spend_pct": 1.2,
        "training_hours": 36,
        "esg_years": 4,
        "indep_director_pct": 35.0,
        "esg_committee": false,
        "completeness_pct": 80
      },
      {
        "code": "600886",
        "name": "国投电力",
        "type": "水电为主",
        "group": "clean",
        "scope1_tco2": 36000000,
        "scope2_tco2": 2000000,
        "power_gen_gwh": 310000,
        "water_wan_ton": 3200,
        "wastewater_rate_pct": 96.0,
        "solid_waste_reuse_pct": 89.0,
        "energy_gj_per_mwh": 3.5,
        "scope3_disclosed": false,
        "env_penalties": 0,
        "safety_spend_pct": 1.6,
        "training_hours": 44,
        "esg_years": 3,
        "indep_director_pct": 41.7,
        "esg_committee": true,
        "completeness_pct": 80
      }
    ]
  },
  "data/companies_multiyear.json": {
    "companies": [
      {
        "code": "601991",
        "name": "大唐发电",
        "group": "thermal",
        "assurance": false,
        "years": {
          "2022": {
            "scope1_tco2": 191860000,
            "scope2_tco2": 970000,
            "power_gen_gwh": 229517
          },
          "2023": {
            "scope1_tco2": 196860000,
            "scope2_tco2": 170000,
            "power_gen_gwh": 274959
          },
          "2024": {
            "scope1_tco2": 210817900,
            "scope2_tco2": 107600,
            "power_gen_gwh": 285153
          }
        },
        "status": "verified",
        "self_reported_intensity_g_per_kwh": 853.83,
        "clean_energy_share_pct": 40.37,
        "clean_energy_share_basis": "控股清洁能源装机容量占比",
        "green_capex_abs_yi": 7.48,
        "green_capex_total_yi": 304.8,
        "green_capex_note": "环保节能投入 7.48 亿元 ÷ 现金流总资本开支 304.8 亿元 = 2.45%",
        "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +9.79%，配额略有结余",
        "previous_year": {
          "green_capex_pct": 1.2,
          "clean_energy_pct": 30.0
        },
        "note": ""
      },
      {
        "code": "600023",
        "name": "浙能电力",
        "group": "thermal",
        "assurance": false,
        "years": {
          "2022": {
            "scope1_tco2": 134210000,
            "scope2_tco2": 42000,
            "power_gen_gwh": 151986
          },
          "2023": {
            "scope1_tco2": 141988000,
            "scope2_tco2": 49000,
            "power_gen_gwh": 163238
          },
          "2024": {
            "scope1_tco2": 151762000,
            "scope2_tco2": 54000,
            "power_gen_gwh": 173952
          }
        },
        "status": "verified",
        "self_reported_intensity_g_per_kwh": null,
        "clean_energy_share_pct": 10.87,
        "clean_energy_share_basis": "控股清洁能源装机容量占比（年报披露值）",
        "green_capex_abs_yi": 3.6,
        "green_capex_total_yi": 96.8,
        "green_capex_note": "环保总投入 3.60 亿元 ÷ 现金流总资本开支 96.8 亿元 = 3.72%",
        "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 −6.43%，配额存在缺口，需外购配额",
        "previous_year": {
          "green_capex_pct": 1.86,
          "clean_energy_pct": 9.0
        },
        "note": ""
      },
      {
        "code": "600886",
        "name": "国投电力",
        "group": "clean",
        "assurance": false,
        "years": {
          "2023": {
            "scope1_tco2": 50018850,
            "scope2_tco2": 903413,
            "power_gen_gwh": 161966
          },
          "2024": {
            "scope1_tco2": 48808719,
            "scope2_tco2": 698000,
            "power_gen_gwh": 172072
          }
        },
        "status": "verified",
        "self_reported_intensity_g_per_kwh": null,
        "clean_energy_share_pct": 70.42,
        "clean_energy_share_basis": "控股清洁能源装机容量占比（口径与大唐、浙能严格一致）",
        "green_capex_abs_yi": 8.61,
        "green_capex_total_yi": 217.7,
        "green_capex_note": "环保投入 7.458 亿 + 节能投入 1.156 亿 = 8.61 亿元 ÷ 资本开支 217.7 亿元 = 3.96%",
        "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +64.91%，巨额配额结余，形成正贡献",
        "previous_year": {
          "green_capex_pct": 2.0,
          "clean_energy_pct": 12.05
        },
        "note": ""
      }
    ]
  },
  "data/carbon_disclosure_ledger.json": {
    "_meta": {
      "title": "绿鉴 · 电力企业碳数据采集台账（3 家样本）",
      "purpose": "记录每家企业碳相关指标的原始值与来源，作为雷达图与碳表现分的唯一输入。",
      "updated": "2026-10",
      "model": "GreenTrace-Power V3.1 (五维雷达)",
      "dimensions": {
        "D1_intensity": {
          "name": "存量能效",
          "raw": "度电碳排放强度 (gCO₂/kWh) = (范围一 + 范围二) ÷ 全口径发电量",
          "score": "逆向归一化：(1000 − 强度) ÷ 10，限定 [0,100]",
          "meaning": "反映机组技术是否先进（超超临界 vs 落后小火电）"
        },
        "D2_trend": {
          "name": "边际改善",
          "raw": "年度碳排放强度变化率 YoY Δ%",
          "score": "50 + 50 × tanh(−5 × τ)，τ 为变化率（负=减排）",
          "meaning": "转型金融的核心看点：银行支持的是『降得快』而非『天生绿』"
        },
        "D3_green_capex": {
          "name": "绿色投入强度",
          "raw": "环保节能投入 ÷ 现金流总资本开支 (CAPEX)，%",
          "score": "正向线性映射，上限 5.0% → 100 分",
          "meaning": "企业有没有真金白银投资未来，还是只在喊口号"
        },
        "D4_structure": {
          "name": "低碳结构",
          "raw": "控股清洁能源装机容量占比，%",
          "score": "正向映射：直接对应百分比得分（100% 装机 = 100 分）",
          "meaning": "抵御碳关税与煤价波动的长期结构韧性"
        },
        "D5_carbon_compliance": {
          "name": "碳合规承压与边际收益",
          "raw": "实际能效较全国碳市场发电行业基准线（2022/2023/2024 = 823/820/820 gCO₂/kWh）的偏离度：(基准线 − 强度) ÷ 基准线",
          "score": "以 50 分为配额平衡点；正偏离（结余）加分至 100，负偏离（缺口）扣分至 0",
          "meaning": "直接关联银行信用风险：配额缺口需花钱买配额，现金流承压"
        }
      },
      "baselines": {
        "intensity_scale_max": 1000,
        "intensity_scale_min": 0,
        "carbon_market_benchmark_tco2_per_mwh": {
          "2022": 0.823,
          "2023": 0.82,
          "2024": 0.82
        },
        "green_capex_full_mark_pct": 5.0
      },
      "note": "维度 5 的基准线是「全国碳市场发电行业基准线」（按年度 820–823 gCO₂/kWh），它决定配额结余还是缺口；与维度 1 的标尺上限 1000 是两套不同参数，不可混用。基准线值须与 carbon_model.py 的 BENCHMARK_TCO2_PER_MWH 保持一致。"
    },
    "companies": [
      {
        "code": "601991",
        "name": "大唐发电",
        "group": "thermal",
        "type": "火电",
        "years": {
          "2022": {
            "scope1_tco2": 191860000,
            "scope2_tco2": 970000,
            "power_gen_gwh": 229517
          },
          "2023": {
            "scope1_tco2": 196860000,
            "scope2_tco2": 170000,
            "power_gen_gwh": 274959
          },
          "2024": {
            "scope1_tco2": 210817900,
            "scope2_tco2": 107600,
            "power_gen_gwh": 285153
          }
        },
        "clean_energy_share_pct": 40.37,
        "clean_energy_share_basis": "控股清洁能源装机容量占比",
        "green_capex_abs_yi": 7.48,
        "green_capex_total_yi": 304.8,
        "green_capex_note": "环保节能投入 7.48 亿元 ÷ 现金流总资本开支 304.8 亿元 = 2.45%",
        "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +9.79%，配额略有结余",
        "previous_year": {
          "green_capex_pct": 1.2,
          "clean_energy_pct": 30.0
        },
        "self_reported_intensity_g_per_kwh": 853.83,
        "status": "verified",
        "sources": [
          "2024年度可持续发展报告（环境、社会及管治报告）环境绩效表",
          "2024 年年度报告（现金流量表：资本开支）",
          "界面新闻《五大电力上市公司碳排放量发布》汇总"
        ]
      },
      {
        "code": "600023",
        "name": "浙能电力",
        "group": "thermal",
        "type": "火电",
        "years": {
          "2022": {
            "scope1_tco2": 134210000,
            "scope2_tco2": 42000,
            "power_gen_gwh": 151986
          },
          "2023": {
            "scope1_tco2": 141988000,
            "scope2_tco2": 49000,
            "power_gen_gwh": 163238
          },
          "2024": {
            "scope1_tco2": 151762000,
            "scope2_tco2": 54000,
            "power_gen_gwh": 173952
          }
        },
        "clean_energy_share_pct": 10.87,
        "clean_energy_share_basis": "控股清洁能源装机容量占比（年报披露值）",
        "green_capex_abs_yi": 3.6,
        "green_capex_total_yi": 96.8,
        "green_capex_note": "环保总投入 3.60 亿元 ÷ 现金流总资本开支 96.8 亿元 = 3.72%",
        "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 −6.43%，配额存在缺口，需外购配额",
        "previous_year": {
          "green_capex_pct": 1.86,
          "clean_energy_pct": 9.0
        },
        "status": "verified",
        "sources": [
          "2024年可持续发展暨环境、社会和治理（ESG）报告 关键绩效表",
          "2024 年年度报告（现金流量表：资本开支、清洁能源装机）"
        ]
      },
      {
        "code": "600886",
        "name": "国投电力",
        "group": "clean",
        "type": "水电为主",
        "years": {
          "2023": {
            "scope1_tco2": 50018850,
            "scope2_tco2": 903413,
            "power_gen_gwh": 161966
          },
          "2024": {
            "scope1_tco2": 48808719,
            "scope2_tco2": 698000,
            "power_gen_gwh": 172072
          }
        },
        "clean_energy_share_pct": 70.42,
        "clean_energy_share_basis": "控股清洁能源装机容量占比（口径与大唐、浙能严格一致）",
        "green_capex_abs_yi": 8.61,
        "green_capex_total_yi": 217.7,
        "green_capex_note": "环保投入 7.458 亿 + 节能投入 1.156 亿 = 8.61 亿元 ÷ 资本开支 217.7 亿元 = 3.96%",
        "carbon_cost_note": "较全国碳市场基准线 820 gCO₂/kWh 偏离 +64.91%，巨额配额结余，形成正贡献",
        "previous_year": {
          "green_capex_pct": 2.0,
          "clean_energy_pct": 12.05
        },
        "status": "verified",
        "sources": [
          "2024年环境、社会与治理报告 关键绩效表（第一部分：环境范畴）",
          "2024 年年度报告（现金流量表：资本开支）",
          "报告正文：2024 年控股企业累计完成发电量 1720.72 亿千瓦时，同比增长 6.24%"
        ]
      }
    ]
  },
  "data/esg_announcements.json": {
    "601991": {
      "name": "大唐发电",
      "reports": [
        {
          "title": "大唐发电2023年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2024-03-23/1219391420.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2022年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2023-03-29/1216247175.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2021年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2022-03-30/1212731328.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2020年社会责任报告",
          "url": "finalpage/2021-03-27/1209466225.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2024年可持续发展报告（环境、社会及管治报告）",
          "url": "finalpage/2025-03-26/1222896371.PDF",
          "kw": "可持续发展报告"
        }
      ]
    },
    "600886": {
      "name": "国投电力",
      "reports": [
        {
          "title": "国投电力控股股份有限公司2021年度社会责任报告",
          "url": "finalpage/2022-04-29/1213224206.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "国投电力控股股份有限公司2020年企业社会责任报告",
          "url": "finalpage/2021-04-29/1209858500.PDF",
          "kw": "社会责任报告"
        }
      ]
    },
    "600023": {
      "name": "浙能电力",
      "reports": [
        {
          "title": "2023年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2024-04-30/1219904672.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2022年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2023-04-28/1216648702.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2021年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2022-04-29/1213204420.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2024年可持续发展暨环境、社会和治理（ESG）报告",
          "url": "finalpage/2025-04-29/1223358270.PDF",
          "kw": "可持续发展报告"
        }
      ]
    }
  },
  "data/raw/esg_announcements.json": {
    "600011": {
      "name": "华能国际",
      "reports": [
        {
          "title": "华能国际2023年度社会责任报告",
          "url": "finalpage/2024-03-20/1219348218.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "华能国际2022年度社会责任报告",
          "url": "finalpage/2023-03-22/1216181432.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "华能国际2021年度社会责任报告",
          "url": "finalpage/2022-03-23/1212645184.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "华能国际2020年度社会责任报告",
          "url": "finalpage/2021-03-24/1209438774.PDF",
          "kw": "社会责任报告"
        }
      ]
    },
    "600795": {
      "name": "国电电力",
      "reports": [
        {
          "title": "国电电力2021年社会责任报告",
          "url": "finalpage/2022-04-26/1213109241.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "国电电力2020年社会责任报告",
          "url": "finalpage/2021-04-20/1209727374.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "董事会战略与ESG管理委员会实施细则（2025.12）",
          "url": "finalpage/2025-12-13/1224872058.PDF",
          "kw": "ESG"
        },
        {
          "title": "国电电力发展股份有限公司董事会战略与ESG管理委员会实施细则",
          "url": "finalpage/2023-04-15/1216418380.PDF",
          "kw": "ESG"
        }
      ]
    },
    "601991": {
      "name": "大唐发电",
      "reports": [
        {
          "title": "大唐发电2023年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2024-03-23/1219391420.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2022年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2023-03-29/1216247175.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2021年社会责任报告（环境、社会及管治报告）",
          "url": "finalpage/2022-03-30/1212731328.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2020年社会责任报告",
          "url": "finalpage/2021-03-27/1209466225.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "大唐发电2024年可持续发展报告（环境、社会及管治报告）",
          "url": "finalpage/2025-03-26/1222896371.PDF",
          "kw": "可持续发展报告"
        }
      ]
    },
    "600027": {
      "name": "华电国际",
      "reports": [
        {
          "title": "2024年度社会责任报告",
          "url": "finalpage/2025-03-28/1222927028.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2023年度社会责任报告",
          "url": "finalpage/2024-03-28/1219426307.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2022年度社会责任报告",
          "url": "finalpage/2023-03-30/1216257622.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2021年度社会责任报告",
          "url": "finalpage/2022-03-26/1212687595.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "社会责任报告",
          "url": "finalpage/2021-03-31/1209485828.PDF",
          "kw": "社会责任报告"
        }
      ]
    },
    "600021": {
      "name": "上海电力",
      "reports": [
        {
          "title": "上海电力2021年可持续发展报告",
          "url": "finalpage/2022-04-29/1213210445.PDF",
          "kw": "可持续发展报告"
        },
        {
          "title": "上海电力股份有限公司董事会环境社会及治理（ESG）委员会实施细则（经公司第九届董事会第五次会议审议通过）",
          "url": "finalpage/2025-09-10/1224648482.PDF",
          "kw": "ESG"
        },
        {
          "title": "上海电力股份有限公司2024年环境、社会及治理（ESG）报告",
          "url": "finalpage/2025-04-29/1223373838.PDF",
          "kw": "ESG"
        },
        {
          "title": "上海电力股份有限公司董事会环境社会及治理（ESG）委员会实施细则（经公司董事会2024年第二次临时会议审议通过）",
          "url": "finalpage/2024-04-27/1219874402.PDF",
          "kw": "ESG"
        },
        {
          "title": "上海电力股份有限公司 2023年环境、社会及治理（ESG）报告",
          "url": "finalpage/2024-04-02/1219492977.PDF",
          "kw": "ESG"
        },
        {
          "title": "上海电力股份有限公司2022年环境、社会及治理（ESG）报告",
          "url": "finalpage/2023-03-31/1216277810.PDF",
          "kw": "ESG"
        }
      ]
    },
    "600886": {
      "name": "国投电力",
      "reports": [
        {
          "title": "国投电力控股股份有限公司2021年度社会责任报告",
          "url": "finalpage/2022-04-29/1213224206.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "国投电力控股股份有限公司2020年企业社会责任报告",
          "url": "finalpage/2021-04-29/1209858500.PDF",
          "kw": "社会责任报告"
        }
      ]
    },
    "600900": {
      "name": "长江电力",
      "reports": [
        {
          "title": "长江电力2022年度社会责任报告",
          "url": "finalpage/2023-04-28/1216664105.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "长江电力2021年度社会责任报告",
          "url": "finalpage/2022-04-30/1213270603.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "长江电力2020年度社会责任报告",
          "url": "finalpage/2021-04-30/1209875193.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "长江电力2024年度环境、社会和治理（ESG）报告",
          "url": "finalpage/2025-04-30/1223421180.PDF",
          "kw": "ESG"
        },
        {
          "title": "长江电力2023年度环境、社会和治理（ESG）报告",
          "url": "finalpage/2024-04-30/1219922583.PDF",
          "kw": "ESG"
        }
      ]
    },
    "600023": {
      "name": "浙能电力",
      "reports": [
        {
          "title": "2023年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2024-04-30/1219904672.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2022年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2023-04-28/1216648702.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2021年度社会责任暨环境、社会和公司治理（ESG）报告",
          "url": "finalpage/2022-04-29/1213204420.PDF",
          "kw": "社会责任报告"
        },
        {
          "title": "2024年可持续发展暨环境、社会和治理（ESG）报告",
          "url": "finalpage/2025-04-29/1223358270.PDF",
          "kw": "可持续发展报告"
        }
      ]
    }
  },
  "data/processed/radar_attachment_snapshot.json": {
    "_meta": {
      "title": "绿鉴 · 电力企业碳数据采集台账（3 家样本）",
      "purpose": "记录每家企业碳相关指标的原始值与来源，作为雷达图与碳表现分的唯一输入。",
      "updated": "2026-10",
      "model": "GreenTrace-Power V3.1 (五维雷达)",
      "dimensions": {
        "D1_intensity": {
          "name": "存量能效",
          "raw": "度电碳排放强度 (gCO₂/kWh) = (范围一 + 范围二) ÷ 全口径发电量",
          "score": "逆向归一化：(1000 − 强度) ÷ 10，限定 [0,100]",
          "meaning": "反映机组技术是否先进（超超临界 vs 落后小火电）"
        },
        "D2_trend": {
          "name": "边际改善",
          "raw": "年度碳排放强度变化率 YoY Δ%",
          "score": "50 + 50 × tanh(−5 × τ)，τ 为变化率（负=减排）",
          "meaning": "转型金融的核心看点：银行支持的是『降得快』而非『天生绿』"
        },
        "D3_green_capex": {
          "name": "绿色投入强度",
          "raw": "环保节能投入 ÷ 现金流总资本开支 (CAPEX)，%",
          "score": "正向线性映射，上限 5.0% → 100 分",
          "meaning": "企业有没有真金白银投资未来，还是只在喊口号"
        },
        "D4_structure": {
          "name": "低碳结构",
          "raw": "控股清洁能源装机容量占比，%",
          "score": "正向映射：直接对应百分比得分（100% 装机 = 100 分）",
          "meaning": "抵御碳关税与煤价波动的长期结构韧性"
        },
        "D5_carbon_compliance": {
          "name": "碳合规承压与边际收益",
          "raw": "实际能效较全国基准线 (750 gCO₂/kWh) 的偏离度：(750 − 强度) ÷ 750",
          "score": "以 50 分为配额平衡点；正偏离（结余）加分至 100，负偏离（缺口）扣分至 0",
          "meaning": "直接关联银行信用风险：配额缺口需花钱买配额，现金流承压"
        }
      },
      "baselines": {
        "intensity_scale_max": 1000,
        "intensity_scale_min": 0,
        "national_benchmark_g_per_kwh": 750,
        "green_capex_full_mark_pct": 5.0
      },
      "note": "维度 5 的基准线 750 gCO₂/kWh 为全国火电平均基准值，与维度 1 的标尺上限 1000 是两套不同参数，不可混用。"
    },
    "companies": [
      {
        "code": "601991",
        "name": "大唐发电",
        "group": "thermal",
        "type": "火电",
        "years": {
          "2022": {
            "scope1_tco2": 191860000,
            "scope2_tco2": 970000,
            "power_gen_gwh": 229517
          },
          "2023": {
            "scope1_tco2": 196860000,
            "scope2_tco2": 170000,
            "power_gen_gwh": 274959
          },
          "2024": {
            "scope1_tco2": 210817900,
            "scope2_tco2": 107600,
            "power_gen_gwh": 285153
          }
        },
        "clean_energy_share_pct": 40.37,
        "clean_energy_share_basis": "控股清洁能源装机容量占比",
        "green_capex_abs_yi": 7.48,
        "green_capex_total_yi": 304.8,
        "green_capex_note": "环保节能投入 7.48 亿元 ÷ 现金流总资本开支 304.8 亿元 = 2.45%",
        "carbon_cost_note": "较全国基准线 750 gCO₂/kWh 偏离 +1.37%，配额基本平衡",
        "previous_year": {
          "green_capex_pct": 1.2,
          "clean_energy_pct": 30.0
        },
        "self_reported_intensity_g_per_kwh": 853.83,
        "status": "verified",
        "sources": [
          "2024年度可持续发展报告（环境、社会及管治报告）环境绩效表",
          "2024 年年度报告（现金流量表：资本开支）",
          "界面新闻《五大电力上市公司碳排放量发布》汇总"
        ]
      },
      {
        "code": "600023",
        "name": "浙能电力",
        "group": "thermal",
        "type": "火电",
        "years": {
          "2022": {
            "scope1_tco2": 134210000,
            "scope2_tco2": 42000,
            "power_gen_gwh": 151986
          },
          "2023": {
            "scope1_tco2": 141988000,
            "scope2_tco2": 49000,
            "power_gen_gwh": 163238
          },
          "2024": {
            "scope1_tco2": 151762000,
            "scope2_tco2": 54000,
            "power_gen_gwh": 173952
          }
        },
        "clean_energy_share_pct": 10.87,
        "clean_energy_share_basis": "控股清洁能源装机容量占比（年报披露值）",
        "green_capex_abs_yi": 3.6,
        "green_capex_total_yi": 96.8,
        "green_capex_note": "环保总投入 3.60 亿元 ÷ 现金流总资本开支 96.8 亿元 = 3.72%",
        "carbon_cost_note": "较全国基准线 750 gCO₂/kWh 偏离 −16.36%，配额严重超标，需外购配额",
        "previous_year": {
          "green_capex_pct": 1.86,
          "clean_energy_pct": 9.0
        },
        "status": "verified",
        "sources": [
          "2024年可持续发展暨环境、社会和治理（ESG）报告 关键绩效表",
          "2024 年年度报告（现金流量表：资本开支、清洁能源装机）"
        ]
      },
      {
        "code": "600886",
        "name": "国投电力",
        "group": "clean",
        "type": "水电为主",
        "years": {
          "2023": {
            "scope1_tco2": 50018850,
            "scope2_tco2": 903413,
            "power_gen_gwh": 161966
          },
          "2024": {
            "scope1_tco2": 48808719,
            "scope2_tco2": 698000,
            "power_gen_gwh": 172072
          }
        },
        "clean_energy_share_pct": 67.2,
        "clean_energy_share_basis": "补充观测值（ESG口径，时点与年报不同，非年报值）；2024年报原文为70.42%（截至2024年底控股清洁能源装机占比），现行台账采用70.42",
        "green_capex_abs_yi": 8.61,
        "green_capex_total_yi": 217.7,
        "green_capex_note": "环保投入 7.458 亿 + 节能投入 1.156 亿 = 8.61 亿元 ÷ 资本开支 217.7 亿元 = 3.96%",
        "carbon_cost_note": "较全国基准线 750 gCO₂/kWh 偏离 +61.64%，巨额配额结余，形成正贡献",
        "previous_year": {
          "green_capex_pct": 2.0,
          "clean_energy_pct": 12.05
        },
        "status": "verified",
        "sources": [
          "2024年环境、社会与治理报告 关键绩效表（第一部分：环境范畴）",
          "2024 年年度报告（现金流量表：资本开支）",
          "报告正文：2024 年控股企业累计完成发电量 1720.72 亿千瓦时，同比增长 6.24%"
        ]
      }
    ]
  },
  "data/待填_多年度环境绩效.csv": [
    {
      "证券代码": "601991",
      "企业名称": "大唐发电",
      "报告年度": "2022",
      "直接排放_万吨CO2": "19186",
      "间接排放_万吨CO2": "97",
      "发电量_亿千瓦时": "2346.8",
      "排放强度_克每千瓦时": "817.8",
      "数据来源": "2022年度社会责任报告 环境绩效表"
    },
    {
      "证券代码": "601991",
      "企业名称": "大唐发电",
      "报告年度": "2023",
      "直接排放_万吨CO2": "19686",
      "间接排放_万吨CO2": "17",
      "发电量_亿千瓦时": "2300.96",
      "排放强度_克每千瓦时": "856.3",
      "数据来源": "2023年度社会责任报告 环境绩效表"
    },
    {
      "证券代码": "601991",
      "企业名称": "大唐发电",
      "报告年度": "2024",
      "直接排放_万吨CO2": "21081.79",
      "间接排放_万吨CO2": "10.76",
      "发电量_亿千瓦时": "2469.65",
      "排放强度_克每千瓦时": "853.83",
      "数据来源": "2024年度社会责任报告 环境绩效表"
    },
    {
      "证券代码": "600011",
      "企业名称": "华能国际",
      "报告年度": "2022",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600011",
      "企业名称": "华能国际",
      "报告年度": "2023",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600011",
      "企业名称": "华能国际",
      "报告年度": "2024",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600795",
      "企业名称": "国电电力",
      "报告年度": "2022",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600795",
      "企业名称": "国电电力",
      "报告年度": "2023",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600795",
      "企业名称": "国电电力",
      "报告年度": "2024",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600027",
      "企业名称": "华电国际",
      "报告年度": "2022",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600027",
      "企业名称": "华电国际",
      "报告年度": "2023",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600027",
      "企业名称": "华电国际",
      "报告年度": "2024",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600023",
      "企业名称": "浙能电力",
      "报告年度": "2022",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600023",
      "企业名称": "浙能电力",
      "报告年度": "2023",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600023",
      "企业名称": "浙能电力",
      "报告年度": "2024",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600021",
      "企业名称": "上海电力",
      "报告年度": "2022",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600021",
      "企业名称": "上海电力",
      "报告年度": "2023",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600021",
      "企业名称": "上海电力",
      "报告年度": "2024",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600886",
      "企业名称": "国投电力",
      "报告年度": "2022",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600886",
      "企业名称": "国投电力",
      "报告年度": "2023",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600886",
      "企业名称": "国投电力",
      "报告年度": "2024",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600900",
      "企业名称": "长江电力",
      "报告年度": "2022",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600900",
      "企业名称": "长江电力",
      "报告年度": "2023",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    },
    {
      "证券代码": "600900",
      "企业名称": "长江电力",
      "报告年度": "2024",
      "直接排放_万吨CO2": "",
      "间接排放_万吨CO2": "",
      "发电量_亿千瓦时": "",
      "排放强度_克每千瓦时": "",
      "数据来源": "待填"
    }
  ],
  "server/data_store.py::DISCLOSURES": {
    "600011": {
      "name": "华能国际",
      "type": "火电",
      "scope1_tco2": 310000000,
      "scope2_tco2": 8000000,
      "power_gen_gwh": 447000,
      "coal_consumed_wan_t": 9800,
      "revenue_100m": 246700,
      "scope3_disclosed": false,
      "env_penalty_count": 2,
      "disclosure_years": 4,
      "water_use_wan_t": 21000,
      "wastewater_treated_pct": 95.0,
      "solid_waste_util_pct": 92.0,
      "energy_intensity_gj_per_mwh": 9.8,
      "safe_prod_invest_pct": 1.2,
      "employee_training_h": 42,
      "board_indep_pct": 36.4,
      "esg_committee": true
    },
    "600795": {
      "name": "国电电力",
      "type": "火电",
      "scope1_tco2": 240000000,
      "scope2_tco2": 5000000,
      "power_gen_gwh": 400000,
      "coal_consumed_wan_t": 8200,
      "revenue_100m": 192000,
      "scope3_disclosed": false,
      "env_penalty_count": 1,
      "disclosure_years": 4,
      "water_use_wan_t": 18500,
      "wastewater_treated_pct": 96.0,
      "solid_waste_util_pct": 90.0,
      "energy_intensity_gj_per_mwh": 9.6,
      "safe_prod_invest_pct": 1.4,
      "employee_training_h": 38,
      "board_indep_pct": 37.5,
      "esg_committee": true
    },
    "601991": {
      "name": "大唐发电",
      "type": "火电",
      "scope1_tco2": 210000000,
      "scope2_tco2": 4000000,
      "power_gen_gwh": 310000,
      "coal_consumed_wan_t": 7500,
      "revenue_100m": 122000,
      "scope3_disclosed": false,
      "env_penalty_count": 1,
      "disclosure_years": 3,
      "water_use_wan_t": 15200,
      "wastewater_treated_pct": 93.0,
      "solid_waste_util_pct": 88.0,
      "energy_intensity_gj_per_mwh": 10.1,
      "safe_prod_invest_pct": 1.1,
      "employee_training_h": 35,
      "board_indep_pct": 33.3,
      "esg_committee": false
    },
    "600027": {
      "name": "华电国际",
      "type": "火电",
      "scope1_tco2": 180000000,
      "scope2_tco2": 3500000,
      "power_gen_gwh": 260000,
      "coal_consumed_wan_t": 6800,
      "revenue_100m": 117000,
      "scope3_disclosed": false,
      "env_penalty_count": 0,
      "disclosure_years": 5,
      "water_use_wan_t": 12800,
      "wastewater_treated_pct": 97.0,
      "solid_waste_util_pct": 93.0,
      "energy_intensity_gj_per_mwh": 9.5,
      "safe_prod_invest_pct": 1.3,
      "employee_training_h": 40,
      "board_indep_pct": 38.5,
      "esg_committee": true
    },
    "600021": {
      "name": "上海电力",
      "type": "火电/新能源",
      "scope1_tco2": 22000000,
      "scope2_tco2": 900000,
      "power_gen_gwh": 48000,
      "coal_consumed_wan_t": 900,
      "revenue_100m": 42000,
      "scope3_disclosed": true,
      "env_penalty_count": 0,
      "disclosure_years": 6,
      "water_use_wan_t": 2400,
      "wastewater_treated_pct": 98.0,
      "solid_waste_util_pct": 95.0,
      "energy_intensity_gj_per_mwh": 8.2,
      "safe_prod_invest_pct": 1.5,
      "employee_training_h": 48,
      "board_indep_pct": 40.0,
      "esg_committee": true
    },
    "600886": {
      "name": "国投电力",
      "type": "水电为主",
      "scope1_tco2": 18000000,
      "scope2_tco2": 400000,
      "power_gen_gwh": 155000,
      "coal_consumed_wan_t": 500,
      "revenue_100m": 58000,
      "scope3_disclosed": false,
      "env_penalty_count": 0,
      "disclosure_years": 3,
      "water_use_wan_t": 3200,
      "wastewater_treated_pct": 96.0,
      "solid_waste_util_pct": 89.0,
      "energy_intensity_gj_per_mwh": 3.5,
      "safe_prod_invest_pct": 1.6,
      "employee_training_h": 44,
      "board_indep_pct": 41.7,
      "esg_committee": true
    },
    "600900": {
      "name": "长江电力",
      "type": "水电",
      "scope1_tco2": 900000,
      "scope2_tco2": 150000,
      "power_gen_gwh": 276000,
      "coal_consumed_wan_t": 0,
      "revenue_100m": 78000,
      "scope3_disclosed": true,
      "env_penalty_count": 0,
      "disclosure_years": 5,
      "water_use_wan_t": 950,
      "wastewater_treated_pct": 99.0,
      "solid_waste_util_pct": 96.0,
      "energy_intensity_gj_per_mwh": 0.6,
      "safe_prod_invest_pct": 1.8,
      "employee_training_h": 52,
      "board_indep_pct": 44.4,
      "esg_committee": true
    },
    "600023": {
      "name": "浙能电力",
      "type": "火电",
      "scope1_tco2": 160000000,
      "scope2_tco2": 3000000,
      "power_gen_gwh": 170000,
      "coal_consumed_wan_t": 6200,
      "revenue_100m": 98000,
      "scope3_disclosed": false,
      "env_penalty_count": 1,
      "disclosure_years": 4,
      "water_use_wan_t": 11800,
      "wastewater_treated_pct": 94.0,
      "solid_waste_util_pct": 91.0,
      "energy_intensity_gj_per_mwh": 9.9,
      "safe_prod_invest_pct": 1.2,
      "employee_training_h": 36,
      "board_indep_pct": 35.0,
      "esg_committee": false
    }
  }
}
```

## 基线输入SHA-256
```json
{
  "carbon_model.py": "cf82f30f75aadb25402a40d0b43c869314f185d038c6729eb742b16a1c88f26f",
  "legacy_main.py": "ad1682e81207a5920d91ebc399c24054169d8449ca02ac819865b01d65ca9c43",
  "miniserver.py": "b62ea2667c7553d31fab3f7419f94aa60caae5e67d71b4e89dc0dd05898be89e",
  "server/data_store.py": "788892ebfc976623eca6f7c95390a410e192595d6d91d4e5d6b21dba51eb6e96",
  "server/carbon_profile.py": "62a50926c4a1473fb3cb02df51883bd64c014aa93d7e886148837879a51d3e7b",
  "server/profile_extensions.py": "90b4562ab07dc36af9ee772957c5a201ead4cdbe4d9a43a0758dbd06e52d996e",
  "data/companies.json": "b544db07f2b69a467a945569cdddfa7c90b70372c23be2e0781548fcc2f5b79c",
  "data/companies_multiyear.json": "9af38e5ebe5e2ff3e19ff27f1043eda40b949dee89899b6b14ff39abd06fc6db",
  "data/carbon_disclosure_ledger.json": "20d7e46937decc6489c3bbe30c89ea50a86919448ce7d7a70394a9095ea8a975",
  "data/esg_announcements.json": "1da9f3e6f9b34b252e4ca20cedbfee7f65577565f0b81d4f6c6d081d4e481ac8",
  "data/raw/esg_announcements.json": "24932c0427f17cd061fddff470a09ee86aae6f3e880088763e8691d738fd8c53",
  "data/processed/radar_attachment_snapshot.json": "da9af843d1c6a5bb3d8bb3d28e0c9a4850628f6806e625b5172dc9cec6d1c2dc",
  "data/待填_多年度环境绩效.csv": "1911ad0ea34580e280ddc17fe57d2a064e8612c647882cb5c34b0305aeac155a"
}
```

## 验证、问题优先级、执行建议与未验证事项
```json
{
  "company_count": 8,
  "main_quant_count": 3,
  "null_preserved": 178,
  "private_key_scan": "PASS",
  "original_source_hashes_unchanged": true,
  "source_scope": "Git HEAD allowlist only; no original runtime DB or historical attest ledger accessed",
  "scope2_fallback_triggered": false,
  "no_freeze_or_network_calls": true,
  "radar": "only adjacent non-null score vertices joined; all-null companies have no data lines",
  "unverified": [
    "未进行浏览器交互/打印与跨设备实际渲染测试",
    "未核验原PDF、边界、气体和Scope2方法",
    "未验证模型预测力、配额合规或真实授信适用性"
  ],
  "priority_advice": [
    "P0：正式使用前逐项对照公开披露原文与年度边界",
    "P1：区分环保费用与转型CapEx、装机与发电份额",
    "P1：旧模型零替代/证据权重文字需另行授权处理；本任务不改业务代码",
    "P2：扩大可比样本并评估权重、档位和增量预测能力"
  ]
}
```

## 验收标准
- 8家企业全部公开字段与年份、3家main-quant完整输出均列示。
- null未补0；真实0保留；缺轴不跨越闭合；0—100参考分不与基期100混用。
- HTML内联CSS/SVG/JSON，无CDN依赖；JSON支持从内嵌数据离线下载。
- 仅Git跟踪白名单，临时空扩展库；无用户补充/银行/历史凭证数据。
- 旁文件：public-data.json、validation.json、radar-{code}.svg。
