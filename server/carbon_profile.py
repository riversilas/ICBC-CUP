"""Scope1/2 inventory profile; standards inform accounting, not invented scores."""
from pathlib import Path
import json,math
import data_store as ds
import profile_extensions as ext
from urllib.parse import quote
# Method/schema identity is retained for frozen manifests, not a release number.
VERSION='scope12-transition-1.9.4'
GHG='https://ghgprotocol.org/corporate-standard'
S2='https://ghgprotocol.org/scope-2-guidance'
TPI='https://www.transitionpathwayinitiative.org/knowledge-hub/methodologies/electricity-utilities-methodology-v5'

def metric(value,unit,reason=None):
    return {'value':value,'unit':unit,**({'reason':reason} if reason else {})}
def change(x,y):
    v=(x/y-1)*100 if x is not None and y is not None and y>0 else None
    return {'value':v,'reason':None} if v is not None and math.isfinite(v) else {'value':None,'reason':'缺同口径上一期、前值非正或数值超限'}
def annual(r,y):
    a=r.get('scope1_tco2');b=r.get('scope2_tco2');g=r.get('power_gen_gwh')
    known_mismatch = r.get('scope1_gas_basis') and r.get('scope2_gas_basis') and r['scope1_gas_basis']!=r['scope2_gas_basis']
    known_mismatch = known_mismatch or (r.get('scope1_boundary') and r.get('scope2_boundary') and r['scope1_boundary']!=r['scope2_boundary'])
    total=a+b if a is not None and b is not None and not known_mismatch else None
    return {'year':y,'scope1':a,'scope2':b,'total':total,'production':g,'intensity':total/g if total is not None and g and g>0 else None}
def methods():
    return [
        {'key':'scope1','name':'Scope 1直接排放','formula':'E₁ = Σ 活动数据 × 对应排放因子','meaning':'企业控制范围内燃烧及工艺排放；本平台使用提供的披露值，不自行核算原始活动数据。','basis_name':'GHG Protocol Corporate Standard（已读官方概览）','basis_url':GHG,'limitation':'因子、温室气体及组织边界须核对原报告；概览不是已核验完整清单。'},
        {'key':'scope2','name':'Scope 2外购能源排放','formula':'E₂ = Σ 外购电／热／蒸汽／冷量 × 对应因子','meaning':'区分地点法与市场法；两种方法不可相加为双份排放。','basis_name':'GHG Protocol Scope 2 Guidance（已读官方概览）','basis_url':S2,'limitation':'市场法合同工具需满足质量条件；当前附件方法未确认。'},
        {'key':'total','name':'选定方法后的范围1+2汇总','formula':'E = E₁ + E₂（同年度、边界及气体口径）','meaning':'表示企业排放规模，不等于碳市场履约排放，也不直接惩罚大企业。','basis_name':'GHG企业清单范围分列原则；合计为本项目展示','basis_url':GHG,'limitation':'CO₂与CO₂e不得悄悄互换；总量不转换为信用风险分。'},
        {'key':'intensity','name':'电力业务生产强度','formula':'CI = E ÷ G；吨／GWh数值＝kg／MWh','meaning':'区分单位产出效率与企业规模，避免只观察总量。','basis_name':'TPI电力v5（已读方法摘要，部门强度思路）','basis_url':TPI,'limitation':'本项目Scope1+2分子不能冒称完全复制TPI详细方法；其他行业需另换分母。'},
        {'key':'change','name':'同口径年度变化','formula':'Δx = (xₜ ÷ xₜ₋₁ − 1) × 100%','meaning':'并列排放、产量及强度变化，辅助解释扩产与效率；产量下降不天然更好。','basis_name':'数学同比；GHG一致性与透明核算目的','basis_url':GHG,'limitation':'边界重述、方法变更或前值非正时不计算；下降不证明主动转型。'}]
def profile(code):
    d=ds.DISCLOSURES.get(code)
    if not d:raise KeyError(code)
    rows=json.loads((Path(ds.PROC_RESOURCE)/'radar_attachment_snapshot.json').read_text(encoding='utf-8'))['companies']
    row=next((r for r in rows if r['code']==code),None)
    if row:
        ys=sorted(int(y) for y in row['years']);trend=[annual(row['years'][str(y)],y) for y in ys];cur=trend[-1];prev=trend[-2] if len(trend)>1 else {}
        label='附件观测 · 未独立核验';kind='attachment_unverified';comparability='assumed_comparable_for_demo_only'
        titles=row.get('sources',[]);extras={'clean_capacity_share_pct':row.get('clean_energy_share_pct'),'environmental_spending_note':row.get('green_capex_note'),'warning':'装机占比、一般环保费用仅作补充信息，不替代发电结构或低碳资本支出。'}
    else:
        cur=annual(d,'演示当前期');prev={};trend=[cur];label='原版演示值 · 年度未确认';kind='demo';comparability='unavailable';titles=['原data_store.DISCLOSURES演示数据'];extras={'warning':'数据原年度标签与历史序列不一致，未拼接Scope2历史或伪造同比。'}
    units={'scope1':'tCO2','scope2':'tCO2','total':'tCO2','production':'GWh','intensity':'kgCO2/MWh'}
    metrics={k:metric(cur[k],u) for k,u in units.items()}
    changes={k:change(cur.get(k),prev.get(k)) for k in units}
    if row and prev:
        raw_cur=row['years'][str(cur['year'])];raw_prev=row['years'][str(prev['year'])]
        if any(raw_cur.get(k) and raw_prev.get(k) and raw_cur[k]!=raw_prev[k] for k in ('boundary_id','gas_basis','scope2_method')):
            changes={k:{'value':None,'reason':'已知年度边界、气体或Scope2方法变更，禁止同比'} for k in units}
    idx=ds.load_reports_index().get(code,{})
    report_links=idx.get('reports',[])
    sources=[{'source_id':f'{code}-source-{i+1}','title':t,'metric_keys':['scope1','scope2','production'],'location':'仅提供报告/来源标题，未核对页码与原文数值','status':'unverified','hash_kind':'metadata_not_pdf','url':'https://www.cninfo.com.cn/new/fulltextSearch?keyWord='+quote(d['name']+' '+t),'source_kind':'search'} for i,t in enumerate(titles)]
    if report_links:
        rr=report_links[-1];sources.append({'source_id':code+'-public-index','title':rr['title'],'metric_keys':[],'location':'历史报告索引，未确认对应本次年度观测','status':'index_only','hash_kind':'metadata_not_pdf','url':'https://static.cninfo.com.cn/'+rr['url']})
    findings=[{'title':'先核对边界和Scope2方法','detail':'附件未提供完整组织边界、气体基准和地点/市场法定位；图中复算明确属于假设演示，不是确认可比。','severity':'warning'}, {'title':'无需为五维补造数据','detail':'移除无可靠披露的投入/结构计分轴；保留相关原值为未核验补充信息，不计算综合评级。','severity':'info'}]
    if changes['total']['value'] is not None and changes['intensity']['value'] is not None and changes['total']['value']>0 and changes['intensity']['value']<0:
        findings.append({'title':'排放总量上升，单位产出强度下降','detail':'同时查看发电量变化，区分业务规模与效率；不直接认定信用风险。','severity':'warning'})
    bank_cases=[{'name':'Holcim：历史气候KPI挂钩银团授信','detail':'官方2021年公告：30亿欧元银团授信再融资，气候及安全年度目标影响贷款成本。不是当前贷款缺口，也不代表工行合作。','url':'https://www.holcim.com/media/media-releases/holcim-commits-to-40-sustainable-financing-by-2024'}, {'name':'SSAB：银行团授信与融资安排','detail':'官网债务融资说明确认银行融资和已承诺后备授信；不将未用额度冒称提款或资金短缺。','url':'https://www.ssab.com/en/company/investors/debt-financing'}]
    extension=ext.get(code)
    for src in sources:
        src['source_kind']=src.get('source_kind','report_index')
    for i,material in enumerate(extension['materials']):
        sources.append({'source_id':f'{code}-user-{i+1}','title':material['title'],'metric_keys':[],'location':material.get('page') or '用户未填写页码','status':'user_submitted','hash_kind':'metadata_not_pdf','url':material['url'],'source_kind':'user_link'})
    if row:
        raw_amount=row.get('green_capex_abs_yi');raw_total=row.get('green_capex_total_yi')
        extension['attachment_investments']=[{'year':cur['year'],'amount_cny':raw_amount*1e8,'total_capex_cny':raw_total*1e8 if raw_total else None,'ratio_pct':raw_amount/raw_total*100 if raw_total else None,'classification':'environmental_spending','title':row.get('green_capex_note','附件环保投入'),'url':sources[0]['url'],'data_kind':'attachment_unverified','source_kind':'search'}] if raw_amount is not None else []
    else:extension['attachment_investments']=[]
    for investment in extension['investments']:
        investment['ratio_pct']=investment['amount_cny']/investment['total_capex_cny']*100 if investment.get('total_capex_cny') else None
        if investment['ratio_pct'] is not None and not math.isfinite(investment['ratio_pct']):investment['ratio_pct']=None
        investment['data_kind']='user_submitted'
    for plan in extension['plans']:
        plan['completion_pct']=plan['actual_value']/plan['target_value']*100 if plan.get('target_value') and plan.get('actual_value') is not None else None
        if plan['completion_pct'] is not None and not math.isfinite(plan['completion_pct']):plan['completion_pct']=None
        plan['data_kind']='user_submitted'
    radar={'kind':'base100','previous_year':prev.get('year'),'current_year':cur['year'],'ticks':[0,50,100,150,200],'axes':[{'key':k,'label':label,'index':(100+changes[k]['value']) if changes[k]['value'] is not None else None,'current_value':cur.get(k),'previous_value':prev.get(k),'unit':units[k]} for k,label in [('scope1','scope1'),('scope2','scope2'),('production','发电量'),('intensity','排放强度')]],'meaning':'基期=100的相对规模，不是绩效评分，不按面积评价好坏'}
    return {'extension':extension,'bank_assessment':ext.assessment(extension),'radar':radar,'code':code,'name':d['name'],'type':d['type'],'year':cur['year'],'previous_year':prev.get('year'),'data_kind':kind,'quality_label':label,'comparability':comparability,'scope2_method':'unknown','metrics':metrics,'changes':changes,'trend':trend,'sources':sources,'methods':methods(),'findings':findings,'context':{'optional_observations':extras,'bank_cases':bank_cases},'method_version':VERSION,'limitations':['不计算人为综合分或信用评级。','资料属于演示/附件，原报告未独立核验；只有公式可复算。','Scope1/2聚焦不是完整企业足迹或完整IFRS/GRI合规评估。','银行价值是版本核验、口径解释与待核事项，而不是已证实预测信用风险。']}
def companies():
    out=[]
    for code in ds.DISCLOSURES:
        p=profile(code);out.append({k:p[k] for k in ('code','name','type','year','data_kind','quality_label')}|{k:p['metrics'][k]['value'] for k in ('scope1','scope2','total')}|{'available_metrics':sum(v['value'] is not None for v in p['changes'].values())})
    return {'count':len(out),'companies':out}
