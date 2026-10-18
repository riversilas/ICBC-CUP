# -*- coding: utf-8 -*-
"""Public-only offline export from Git HEAD, never from local runtime stores."""
from pathlib import Path
import subprocess,tempfile,os,sys,json,html,hashlib,math,csv,io
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/data-report'
INPUTS=['carbon_model.py','legacy_main.py','miniserver.py','server/data_store.py','server/carbon_profile.py','server/profile_extensions.py','data/companies.json','data/companies_multiyear.json','data/carbon_disclosure_ledger.json','data/esg_announcements.json','data/raw/esg_announcements.json','data/processed/radar_attachment_snapshot.json','data/待填_多年度环境绩效.csv']
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
def dump(x):return json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)
def esc(x):return html.escape(str(x),quote=True)
def flat(x,path=''):
 if isinstance(x,dict):
  if not x:yield path,{}
  for k,v in x.items():yield from flat(v,f'{path}.{k}' if path else k)
 elif isinstance(x,list):
  if not x:yield path,[]
  for i,v in enumerate(x):yield from flat(v,f'{path}[{i}]')
 else:yield path,x
def value(x):return '<b class="missing">缺失 / 未取得（null）</b>' if x is None else esc(json.dumps(x,ensure_ascii=False) if isinstance(x,(list,dict,bool)) else x)
def table(x):return '<div class="scroll"><table><thead><tr><th>字段路径 / 年份（原单位）</th><th>原始值</th></tr></thead><tbody>'+''.join(f'<tr><td><code>{esc(k)}</code></td><td>{value(v)}</td></tr>' for k,v in flat(x))+'</tbody></table></div>'
def radar(rows,prev,title):
 def pt(i,s):
  a=-math.pi/2+i*2*math.pi/5
  return 260+135*s/100*math.cos(a),215+135*s/100*math.sin(a)
 s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 440" role="img" aria-label="{esc(title)}"><title>{esc(title)}；0—100参考分；缺值不跨轴连线</title>'
 for tick in [20,40,60,80,100]:
  points=' '.join('%.2f,%.2f'%pt(i,tick) for i in range(5))
  s+=f'<polygon points="{points}" fill="none" stroke="#cedbce"/><text x="265" y="{215-135*tick/100}" font-size="11" fill="#65796d">{tick}</text>'
 for i,row in enumerate(rows):
  x,y=pt(i,100);lx,ly=pt(i,130)
  s+=f'<path d="M260 215L{x} {y}" stroke="#cedbce"/><text x="{lx}" y="{ly}" text-anchor="middle" font-size="13" fill="#173f2e">{esc(row["short"])}</text>'
 for axes,color in [(prev,'#a68b4c'),(rows,'#166447')]:
  for i,row in enumerate(axes):
   score=row.get('score')
   if score is None:continue
   assert 0<=score<=100
   x,y=pt(i,score);nxt=axes[(i+1)%5].get('score')
   if nxt is not None:
    xx,yy=pt((i+1)%5,nxt)
    s+=f'<line data-valid-edge="1" x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="{color}" stroke-width="2.5"/>'
   s+=f'<circle cx="{x}" cy="{y}" r="4" fill="{color}"><title>{esc(row["label"])}：原值 {esc(row["value"])} {esc(row["unit"])}；参考分 {score}</title></circle>'
 return s+'</svg>'
def main():
 ref=git('rev-parse','HEAD').decode().strip();branch=git('branch','--show-current').decode().strip()
 before={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS}
 with tempfile.TemporaryDirectory(prefix='greenchain-public-report-') as td:
  t=Path(td);hashes={}
  for p in INPUTS:
   b=git('show',f'{ref}:{p}');q=t/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(b);hashes[p]=hashlib.sha256(b).hexdigest()
  os.environ['GREENCHAIN_EXTENSION_DB']=str(t/'empty-extension.sqlite3');sys.path[:0]=[str(t/'server'),str(t)]
  import carbon_profile as cp
  import data_store as ds
  import legacy_main as lm
  import carbon_model as cm
  sources={p:json.loads((t/p).read_text(encoding='utf-8')) for p in INPUTS if p.endswith('.json')}
  sources['data/待填_多年度环境绩效.csv']=list(csv.DictReader(io.StringIO((t/'data/待填_多年度环境绩效.csv').read_text(encoding='utf-8-sig'))))
  sources['server/data_store.py::DISCLOSURES']=ds.DISCLOSURES
  companies=[]
  for code in ds.DISCLOSURES:
   p=cp.profile(code);e=p['extension'];assert e['revision']==0 and all(not e[k] for k in ['materials','investments','plans','bank','history'])
   # Strict public field selection excludes even empty runtime categories.
   profile={k:p[k] for k in ['radar','code','name','type','year','previous_year','data_kind','quality_label','comparability','scope2_method','metrics','changes','trend','sources','methods','findings','method_version','limitations']}
   profile['optional_observations']=p['context']['optional_observations'];assert not any(s.get('source_kind')=='user_link' for s in profile['sources'])
   quant=lm.company_payload(code) if code in lm.BY_CODE else None
   axes=quant['carbon'].get('radar') if quant else None
   if not axes:axes=[dict(spec,value=None,score=None,available=False,note='未取得当前V3.2可复算年度输入；不以演示值替代') for spec in cm.RADAR_DIMS]
   records={}
   for path,body in sources.items():
    if path.endswith('::DISCLOSURES'):records[path]=body.get(code)
    elif isinstance(body,dict) and 'companies' in body:records[path]=next((r for r in body['companies'] if r['code']==code),None)
    elif isinstance(body,dict):records[path]=body.get(code)
    else:records[path]=[r for r in body if code in r.values()]
   if quant:assert all(r.get('scope1_tco2') is not None and r.get('scope2_tco2') is not None for r in records['data/carbon_disclosure_ledger.json']['years'].values())
   companies.append({'code':code,'name':p['name'],'profile':profile,'main_quant':quant,'radar_v32':axes,'public_source_records':records})
  notices=[
   '当前公开数据汇总，不是正式登记报告；未生成、冻结或登记新凭证；不宣称独立核验。',
   '基于Git HEAD已跟踪白名单文件在临时目录复算；未使用运行API、原机数据库、补充数据、银行记录或历史凭证账本。',
   '全部8家画像；当前V3.2主线只收录3家可复算企业，另5家五维为null，不评分、不补零、不排行。3家附件观测未独立核验，5家演示值年度未确认。',
   '五维图只使用main-quant V3.2的0—100参考分。画像JSON保留base100字段但不绘制；基期100是相对规模，不可与参考分混用。',
   'V3.2历史项目模型把一般环保费用用于投入轴、把清洁装机份额用于结构轴；不证明转型CapEx或低碳发电份额。碳合规轴不证明实际配额盈缺/履约成本。',
   '源模型缺维会重新归一化；旧输入适配器存在Scope2缺值转0和total_tco2e转Scope1+Scope2=0逻辑。本次3家年度Scope1/2均非空，该补零分支未触发；本报告不自行补值。',
   '历史字段不生效：原始JSON中的carbon.credit（例如大唐+16 BP）、评级、action、disclosure_status=verified均仅为历史模型元数据，不作为本报告建议、授信意见、真实定价或独立核验结论。后续核对已另行记录；本次不修改模型。参数、权重与预测力未经独立实证验证。',
   'carbon_compliance的正负描述可能存在矛盾：本报告只列源模型原始数值与规则，未经专业验证，不据此断言实际配额结余、缺口或收益。',
   '原文件status=verified只是历史标签；来源标题、URL为索引/检索线索，未下载逐页核对PDF、组织边界、气体口径及Scope2地点法/市场法。',
   '画像、演示记录、主线披露提取、附件快照同企业可有不同值；分开保留，不静默合并/覆盖。所有字段和年度均列示，真实0保留、null不补0。',
   '主线evidence结构轴文字权重0.25与实际等权0.20冲突，原输出保留，以scoring_method及weights_applied为准；元数据自称8家/V3.1等可能陈旧，以实际数组及代码输出计数。',
   '五维线只连相邻已知轴；不跨缺值闭合。未取得模型输入的企业显示空框而非零分。森林绿本期、哑金上期。'
  ]
  data={'title':'绿碳链证｜当前公开数据汇总与五维雷达视图','report_date':'2026-10-17','baseline':{'commit':ref,'branch':branch,'selection':'Git HEAD exact allowlist / empty temporary extension DB'},'notices':notices,'source_sha256':hashes,'company_count':8,'main_quant_count':3,'model_method':lm.scoring_method(),'company_index':cp.companies(),'companies':companies,'public_source_files':sources}
  forbidden={'extension','bank_assessment','bank','bank_cases','history','materials','investments','plans','user_submitted'}
  def scan(v):
   if isinstance(v,dict):
    assert not set(v)&forbidden
    for x in v.values():scan(x)
   elif isinstance(v,list):
    for x in v:scan(x)
  scan(data);assert len(companies)==8 and sum(c['main_quant'] is not None for c in companies)==3
  for p,h in before.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
  verification={'company_count':8,'main_quant_count':3,'null_preserved':sum(v is None for _,v in flat(data)),'private_key_scan':'PASS','original_source_hashes_unchanged':True,'source_scope':'Git HEAD allowlist only; no original runtime DB or historical attest ledger accessed','scope2_fallback_triggered':False,'no_freeze_or_network_calls':True,'radar':'only adjacent non-null score vertices joined; all-null companies have no data lines','unverified':['未进行浏览器交互/打印与跨设备实际渲染测试','未核验原PDF、边界、气体和Scope2方法','未验证模型预测力、配额合规或真实授信适用性'],'priority_advice':['P0：正式使用前逐项对照公开披露原文与年度边界','P1：区分环保费用与转型CapEx、装机与发电份额','P1：旧模型零替代/证据权重文字需另行授权处理；本任务不改业务代码','P2：扩大可比样本并评估权重、档位和增量预测能力']}
  OUT.mkdir(parents=True,exist_ok=True)
  (OUT/'public-data.json').write_text(dump(data),encoding='utf-8');(OUT/'data.json').write_text(dump(data),encoding='utf-8');(OUT/'validation.json').write_text(dump(verification),encoding='utf-8')
  css='''*{box-sizing:border-box}body{margin:0;background:#eef3ee;color:#183d2c;font:15px/1.7 system-ui,"Microsoft YaHei",sans-serif}header{background:#103e2e;color:white;padding:40px 5vw;border-bottom:5px solid #ae955a}h1{font-size:clamp(25px,4vw,42px)}main{max-width:1260px;margin:auto;padding:24px;min-width:0}header{overflow-wrap:anywhere}.grid>div{min-width:0}section{background:#fffefa;border:1px solid #dce4da;border-radius:16px;margin:22px 0;padding:25px;scroll-margin-top:110px}h2{border-left:5px solid #ae955a;padding-left:13px}a{color:#146044}nav{position:sticky;top:0;background:#fffefa;z-index:2;padding:12px;display:flex;gap:12px;flex-wrap:wrap}nav a{padding:4px 10px;border:1px solid #dbe3d5;border-radius:7px;text-decoration:none}.scroll{overflow:auto;max-height:680px;max-width:100%}section{overflow:hidden}table{border-collapse:collapse;width:100%;font-size:13px}th,td{border:1px solid #dfe5da;padding:9px;text-align:left;vertical-align:top}th{background:#e8efe7;position:sticky;top:0}td{word-break:break-word}td:first-child{min-width:230px}pre{white-space:pre-wrap;word-break:break-all;background:#f0f4ef;padding:15px;max-height:650px;overflow:auto;font-size:12px}details{margin:15px 0;border:1px solid #dbe3d6;border-radius:9px;padding:12px}summary{cursor:pointer;font-weight:600}.missing{color:#896e30}.notice{background:#f4efdf;border-left:4px solid #ad9353;padding:15px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}svg{max-width:620px;width:100%}.gold{color:#9e813d}button{background:#e1d4a6;color:#153e2c;border:0;padding:10px 18px;border-radius:8px;cursor:pointer}@media(max-width:800px){.grid{display:block}nav{position:static}section{padding:16px}main{padding:12px}}@media print{nav,button{display:none}.scroll,pre{max-height:none}section{break-before:page}body,header{background:white;color:#123d2d}}'''
  parts=['<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',f'<title>{esc(data["title"])}</title><style>{css}</style><header><p>GREENCHAIN / PUBLIC DATA REVIEW · 2026.10.17</p><h1>全数据报告与五维雷达视图</h1><p>当前公开数据汇总 · 非正式登记报告 · 独立离线阅读</p><p>{ref} / {esc(branch)}</p><button id="download">下载完整公开JSON</button></header>','<nav><a href="#baseline">基线与结论</a>'+''.join(f'<a href="#c{c["code"]}">{esc(c["name"])}</a>' for c in companies)+'<a href="#sources">全部源字段</a><a href="#verification">验证与待核</a></nav><main>','<section id="baseline"><h2>背景基线与结论</h2><p>8家企业画像 · 3家V3.2可复算模型 · 5家未准入模型 · 0新登记记录</p><ol>'+''.join('<li>'+esc(n)+'</li>' for n in notices)+'</ol><h3>同基线模型定义</h3>'+table(data['model_method'])+'</section>']
  md=['# '+data['title'],'\n## 背景与基线',f'- 日期：2026-10-17\n- Git：`{ref}`\n- 分支：`{branch}`\n- 8家公开画像，3家V3.2模型，5家未准入。','\n## 结论与解读边界']+['- '+n for n in notices]
  for c in companies:
   code=c['code'];p=c['profile'];q=c['main_quant'];rows=c['radar_v32'];prev=q['carbon'].get('radar_prev') or [] if q else []
   svg=radar(rows,prev,c['name']+' V3.2五维参考分');(OUT/f'radar-{code}.svg').write_text(svg,encoding='utf-8')
   summary=f'{p["quality_label"]} / 年度：{p["year"]} / V3.2：'+(f'{q["carbon"].get("year")}；综合参考分 {q["carbon"].get("carbon_score")}（非信用结论）' if q else '未取得可复算输入')
   axis_table='<table><tr><th>模型轴 / 单位</th><th>本期原始值</th><th>本期参考分</th><th>上期原始值</th><th>上期参考分</th></tr>'
   for i,a in enumerate(rows):axis_table+='<tr>'+''.join('<td>'+value(v)+'</td>' for v in [a['label']+' / '+a['unit'],a['value'],a['score'],prev[i]['value'] if prev else None,prev[i]['score'] if prev else None])+'</tr>'
   axis_table+='</table>'
   parts+=[f'<section class="company" id="c{code}" data-code="{code}"><h2>{esc(c["name"])} · {code}</h2><p class="notice">{esc(summary)}</p><h3>V3.2五维雷达：0—100参考分</h3><p>不使用画像基期100标尺；只连相邻已知轴，缺失不补零、不跨缺值闭合。</p><div class="grid"><div>{svg}<p>森林绿：本期　<span class="gold">哑金：上期（如取得）</span></p></div><div>{axis_table}</div></div><h3>画像全部字段 / 全部年度</h3>'+table(p),'<h3>主线模型全部输出（包括上期原值与分数）</h3><p class="notice">历史字段不生效：credit/BP、评级、action、verified仅为旧模型元数据，不是当前建议或独立核验结论。carbon_compliance正负说明待核，原始数值和规则未经专业验证。</p>'+table(q),'<h3>各公开数据来源：全字段 / 全部年份</h3>']
   for path,record in c['public_source_records'].items():parts.append(f'<details><summary>{esc(path)}</summary>{table(record)}</details>')
   parts.append('<details><summary>完整公开JSON（本企业）</summary><pre>'+esc(dump(c))+'</pre></details></section>')
   md+=[f'\n## {c["name"]}（{code}）',summary,'\n### 原始轴值与参考分','|轴|单位|本期原始值|本期参考分|上期原始值|上期参考分|','|---|---|---|---|---|---|']
   for i,a in enumerate(rows):md.append('| '+' | '.join('缺失（null）' if v is None else str(v) for v in [a['label'],a['unit'],a['value'],a['score'],prev[i]['value'] if prev else None,prev[i]['score'] if prev else None])+' |')
   md+=['\n### 画像 / 全部年度 / 全源字段 / 全模型输出','```json',dump(c),'```']
  parts.append('<section id="sources"><h2>数据来源与性质：全部公开源字段</h2><p>旧版状态/数量/版本文字按源保留，不能视为独立核验。数据文件中的历史公司观测属于公开输入，不是运行凭证账本。</p>')
  for path,body in sources.items():parts.append('<details><summary>'+esc(path)+'</summary>'+table(body)+'<details><summary>原始JSON</summary><pre>'+esc(dump(body))+'</pre></details></details>')
  parts+=['<h3>Git基线输入SHA-256（非PDF哈希）</h3>'+table(hashes)+'</section>','<section id="verification"><h2>验证、优先级、执行建议与未验证事项</h2>'+table(verification)+'</section><footer>绿碳链证 · 当前公开数据汇总 · 非登记 / 非独立核验 / 非授信结论</footer></main>']
  raw=dump(data).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
  parts.append('<script id="public-json" type="application/json">'+raw+'</script><script>document.getElementById("download").onclick=function(){const b=new Blob([document.getElementById("public-json").textContent],{type:"application/json;charset=utf-8"});const u=URL.createObjectURL(b);const a=document.createElement("a");a.href=u;a.download="greenchain-public-data-20261017.json";a.click();setTimeout(()=>URL.revokeObjectURL(u),1000)};</script></html>')
  page=''.join(parts);assert page.count('class="company"')==8 and '<script src=' not in page and 'https://cdn' not in page
  (OUT/'index.html').write_text(page,encoding='utf-8')
  md+=['\n## 全部公开数据源（全字段与全部年份）','```json',dump(sources),'```','\n## 基线输入SHA-256','```json',dump(hashes),'```','\n## 验证、问题优先级、执行建议与未验证事项','```json',dump(verification),'```','\n## 验收标准','- 8家企业全部公开字段与年份、3家main-quant完整输出均列示。','- null未补0；真实0保留；缺轴不跨越闭合；0—100参考分不与基期100混用。','- HTML内联CSS/SVG/JSON，无CDN依赖；JSON支持从内嵌数据离线下载。','- 仅Git跟踪白名单，临时空扩展库；无用户补充/银行/历史凭证数据。','- 旁文件：public-data.json、validation.json、radar-{code}.svg。']
  report='\n'.join(md)+'\n';(OUT/'report.md').write_text(report,encoding='utf-8')
  desktop=Path.home()/'Desktop';stem='绿碳链证_全数据报告与雷达视图_20261017'
  (desktop/(stem+'.html')).write_text(page,encoding='utf-8');(desktop/(stem+'.md')).write_text(report,encoding='utf-8')
  print(json.dumps({'companies':8,'main_quant':3,'validation':'PASS','null_count':verification['null_preserved'],'output':'docs/data-report/index.html'}))
if __name__=='__main__':main()
