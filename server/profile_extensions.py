"""User-submitted evidence/plan/finance metadata. Never certification or credit approval."""
import json,math,os,sqlite3,threading
WRITE_LOCK=threading.RLock()
from pathlib import Path
from datetime import datetime
from urllib.parse import urlsplit
import data_store as ds
class Conflict(RuntimeError):pass
def connect():
 p=Path(os.environ.get('GREENCHAIN_EXTENSION_DB',str(Path(ds.PROJECT_ROOT())/'data/processed/profile_extensions.sqlite3')));p.parent.mkdir(parents=True,exist_ok=True)
 c=sqlite3.connect(str(p),timeout=15,isolation_level=None);c.row_factory=sqlite3.Row
 c.execute('CREATE TABLE IF NOT EXISTS extensions(code TEXT PRIMARY KEY, body TEXT NOT NULL)');return c
def initial():return {'revision':0,'materials':[],'investments':[],'plans':[],'bank':{},'history':[]}
def get(code):
 if code not in ds.DISCLOSURES:raise KeyError(code)
 c=connect()
 try:
  r=c.execute('SELECT body FROM extensions WHERE code=?',(code,)).fetchone();return json.loads(r['body']) if r else initial()
 finally:c.close()
def number(v,name,optional=True,signed=False):
 if v is None and optional:return
 if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or (not signed and v<0):raise ValueError(name+('须为有限数' if signed else '须为有限非负数'))
def link(url):
 if not isinstance(url,str) or len(url)>2048:raise ValueError('来源链接必填')
 u=urlsplit(url)
 if u.scheme not in ('http','https') or not u.hostname or u.username or u.password:raise ValueError('来源链接须为无凭据HTTP(S)地址')
def text(v,name):
 if not isinstance(v,str) or not v.strip() or len(v)>2000:raise ValueError(name+'必填且不超过2000字')
def year(v):
 if isinstance(v,bool) or not isinstance(v,int) or not 1990<=v<=2200:raise ValueError('年度无效')
def validate(body):
 allowed={'expected_revision','reason','materials','investments','plans','bank'}
 if set(body)-allowed:raise ValueError('未知补充字段')
 text(body.get('reason'),'补充原因')
 if isinstance(body.get('expected_revision'),bool) or not isinstance(body.get('expected_revision'),int):raise ValueError('修订号必填')
 for category in ('materials','investments','plans'):
  if category not in body:continue
  if not isinstance(body[category],list) or len(body[category])>100:raise ValueError('材料列表最多100条')
  for r in body[category]:
   if not isinstance(r,dict):raise ValueError('记录应为对象')
   year(r.get('year'));link(r.get('url'));text(r.get('source_title') if category=='plans' else r.get('title'),'来源标题' if category!='plans' else '来源报告标题')
   if category=='investments':
    number(r.get('amount_cny'),'投入金额',False);number(r.get('total_capex_cny'),'总资本支出')
    if r.get('classification') not in ('environmental_spending','transition_capex'):raise ValueError('投入分类无效')
    text(r.get('basis'),'分类依据')
    if r.get('total_capex_cny') is not None and (r['total_capex_cny']<=0 or r['amount_cny']>r['total_capex_cny']):raise ValueError('资本支出分母须为正且不小于分子')
   if category=='plans':
    text(r.get('title'),'项目名称');number(r.get('target_value'),'计划量');number(r.get('actual_value'),'实施量')
    if r.get('unit') not in ('MW','GWh','site','%') or r.get('technology') not in ('wind','solar','hydro','storage','efficiency','other') or r.get('status') not in ('planned','in_progress','completed'):raise ValueError('项目技术/单位/状态无效')
    if r['unit']=='%' and any(r.get(k) is not None and r[k]>100 for k in ('target_value','actual_value')):raise ValueError('百分比不能超过100')
 if 'bank' in body:
  b=body['bank']
  if not isinstance(b,dict):raise ValueError('银行记录须为对象')
  for k in ('loan_amount_cny','annual_debt_service_cny','operating_cashflow_cny','repaid_cny','contract_target','observed_value'):number(b.get(k),k,signed=k in ('operating_cashflow_cny','contract_target','observed_value'))
  for k in ('metric_name','metric_unit','assessment_period'):
   if k in b:text(b[k],k)
  if b:
   text(b.get('source_title'),'银行材料来源标题');link(b.get('url'))
   if b.get('due_date'):
    try:datetime.strptime(b['due_date'],'%Y-%m-%d')
    except (TypeError,ValueError):raise ValueError('到期日格式YYYY-MM-DD')
   if b.get('target_direction') not in (None,'le','ge'):raise ValueError('目标方向无效')
def save(code,body):
 with WRITE_LOCK:return _save_locked(code,body)
def _save_locked(code,body):
 if code not in ds.DISCLOSURES:raise KeyError(code)
 validate(body);c=connect()
 try:
  c.execute('BEGIN IMMEDIATE');r=c.execute('SELECT body FROM extensions WHERE code=?',(code,)).fetchone();old=json.loads(r['body']) if r else initial()
  if old['revision']!=body['expected_revision']:raise Conflict('修订冲突，请刷新后再保存')
  new=json.loads(json.dumps(old));before={k:old[k] for k in ('materials','investments','plans','bank')}
  for k in before:
   if k in body:new[k]=body[k]
  new['revision']+=1;new['history'].append({'revision':new['revision'],'created_at':datetime.now().isoformat(timespec='seconds'),'reason':body['reason'],'before':before,'after':{k:new[k] for k in before},'data_kind':'user_submitted'})
  c.execute('INSERT OR REPLACE INTO extensions VALUES(?,?)',(code,json.dumps(new,ensure_ascii=False,allow_nan=False)));c.commit();return new
 except Exception:c.rollback();raise
 finally:c.close()
def assessment(extension):
 b=extension['bank'];missing=[label for k,label in [('loan_amount_cny','贷款金额'),('annual_debt_service_cny','年度债务服务'),('operating_cashflow_cny','经营现金流'),('source_title','合同或财务材料')] if b.get(k) is None]
 loan=b.get('loan_amount_cny');paid=b.get('repaid_cny');target=b.get('contract_target');observed=b.get('observed_value');direction=b.get('target_direction')
 covenant='缺目标/观测'
 if target is not None and observed is not None and direction and all(b.get(k) for k in ('metric_name','metric_unit','assessment_period')):covenant='记录达到目标' if (observed<=target if direction=='le' else observed>=target) else '记录未达到目标'
 ratio=b.get('operating_cashflow_cny')/b['annual_debt_service_cny'] if b.get('annual_debt_service_cny') and b.get('operating_cashflow_cny') is not None else None
 if ratio is not None and not math.isfinite(ratio):ratio=None
 return {'stage':'待补充材料' if missing else '基础字段已填写，待人工核查','recommendation':'先补齐合同、财务、征信及担保材料再人工审查' if missing else '材料可进入人工审查；不自动建议批准贷款','repayment':{'status':'待核验' if loan is None or paid is None else ('所填已还金额达到所填贷款金额，待核验' if paid>=loan else '所填已还金额低于所填贷款金额，待核验'),'loan_amount_cny':loan,'repaid_cny':paid},'covenant':{'status':covenant,'target':target,'observed':observed},'cashflow_coverage':ratio,'missing_items':missing,'limitations':['仅对用户提交记录核查，未核银行流水与合同；不认定逾期或违约。','现金流覆盖为输入经营现金流/年度债务服务，不是已审计DSCR。']}
