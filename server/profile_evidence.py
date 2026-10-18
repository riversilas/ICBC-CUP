"""Frozen profile manifests with submitted-material verification; local consistency only."""
import copy,json,re,threading
from datetime import datetime
import chain
import carbon_profile as cp
import profile_extensions as ext
from evidence_diff import differences
LOCK=threading.RLock()
LIMITS=['材料匹配不保证企业最初提供的数据真实。','本地链是内部一致性，不抵御全链重算或删尾；没有外部锚定或独立节点。','本次核验的是manifest，不是原报告PDF字节或专业鉴证。']
def check_digest(d):
    if not isinstance(d,str) or not re.fullmatch('[0-9a-f]{64}',d):raise ValueError('digest需64位小写hex')
def records():return [r for r in chain._load() if r.get('payload',{}).get('kind')=='carbon-profile']
def status(d):
    s=next((r['digest'] for r in records() if r['payload']['manifest'].get('previous_digest')==d),None)
    return ('superseded' if s else 'current'),s
def get(d):
    check_digest(d);r=chain.verify(d)
    if not r['valid'] or r['record']['payload'].get('kind')!='carbon-profile':raise KeyError(d)
    out=copy.deepcopy(r['record']);out['version_status'],out['superseded_by']=status(d);out['chain_integrity']=r['integrity']
    m=out['payload']['manifest'];prev=m.get('previous_digest');old=next((x for x in records() if x['digest']==prev),None)
    out['version_changes']=differences(old['payload']['manifest']['profile'],m['profile']) if old else []
    return out
def freeze(code,body):
    with LOCK, ext.WRITE_LOCK:
        if chain.chain_integrity()!='OK':raise RuntimeError('账本内部损坏，禁止新增')
        p=cp.profile(code);prev=body.get('previous_digest');reason=str(body.get('change_reason') or '').strip()
        if 'expected_revision' in body and (isinstance(body['expected_revision'],bool) or not isinstance(body['expected_revision'],int) or body['expected_revision']!=p['extension']['revision']):raise RuntimeError('草稿修订已变化，请读取最新修订再生成报告')
        if len(reason)>2000:raise ValueError('更正原因不能超过2000字')
        prior=None
        if prev:
            prior=get(prev)
            if prior['payload']['manifest']['company_id']!=code:raise ValueError('上一版本企业不匹配')
            if prior['version_status']!='current':raise RuntimeError('旧版本已被替代，先读取当前版本')
            if not reason:raise ValueError('更正版本必须说明原因')
        else:
            existing=[r for r in records() if r['payload']['manifest']['company_id']==code]
            current=next((r for r in reversed(existing) if status(r['digest'])[0]=='current'),None)
            if current:
                if chain.digest_payload(current['payload']['manifest']['profile'])==chain.digest_payload(p):return get(current['digest'])|{'operation':'reused','frozen_revision':p['extension']['revision']}
                prior=get(current['digest']);prev=current['digest'];reason=reason or '画像或补充材料更新，追加新版本'
        m={'schema_version':cp.VERSION,'company_id':code,'name':p['name'],'year':p['year'],'profile':p,'version':prior['payload']['manifest']['version']+1 if prior else 1,'previous_digest':prev,'change_reason':reason,'created_at':datetime.now().isoformat(timespec='seconds'),'local_identity':'演示提交人'}
        return get(chain.publish({'kind':'carbon-profile','manifest':m},'carbon-profile')['digest'])|{'operation':'created','frozen_revision':p['extension']['revision']}
def recent():
    out=[]
    for r in reversed(records()):
        m=r['payload']['manifest'];out.append({'digest':r['digest'],'code':m['company_id'],'name':m['name'],'version':m['version'],'year':m['year'],'index':r['index'],'created_at':r['created_at'],'status':status(r['digest'])[0],'previous_digest':m['previous_digest']})
    return {'records':out}
def verify(body):
    d=body.get('digest');check_digest(d)
    try:r=get(d)
    except KeyError:return {'registered':False,'material_match':None,'chain_integrity':chain.chain_integrity(),'version_status':'not_found','external_anchor':False,'limitations':LIMITS}
    m=r['payload']['manifest'];match=None
    if 'manifest' in body:
        if not isinstance(body['manifest'],dict):raise ValueError('manifest必须JSON对象')
        json.dumps(body['manifest'],allow_nan=False)
        match=chain.digest_payload(body['manifest'])==chain.digest_payload(m)
    return {'registered':True,'material_match':match,'material_digest':chain.digest_payload(body['manifest']) if 'manifest' in body else None,'registered_material_digest':chain.digest_payload(m),'chain_integrity':r['chain_integrity'],'version_status':r['version_status'],'external_anchor':False,'record':r,'differences':differences(m,body['manifest']) if 'manifest' in body else [],'limitations':LIMITS}
def demo(body):
    r=get(body.get('digest'));m=copy.deepcopy(r['payload']['manifest']);mode=body.get('mode')
    if mode=='changed_value':m['profile']['metrics']['scope1']['value']+=100
    elif mode=='changed_base':
        if len(m['profile']['trend'])<2:raise ValueError('该客户无基期记录，不能进行基期演示')
        m['profile']['trend'][0]['scope1']+=100
    elif mode!='clean':raise ValueError('未知演示模式')
    result=verify({'digest':r['digest'],'manifest':m});result['demonstration']='内存材料副本试验，不写账本，不代表真实企业造假；更改基期或本期字段都会导致材料摘要不匹配。';return result

def preview(code):
    p=cp.profile(code)
    latest=next((r for r in reversed(records()) if r['payload']['manifest']['company_id']==code and status(r['digest'])[0]=='current'),None)
    old=latest['payload']['manifest']['profile'] if latest else {}
    a=old.get('extension',{});b=p['extension']
    counts={k:len(differences(a.get(k,[] if k!='bank' else {}),b.get(k,[] if k!='bank' else {}))) for k in ('materials','investments','plans','bank')}
    return {'draft_revision':b['revision'],'frozen_revision':a.get('revision'),'previous_version':latest['payload']['manifest']['version'] if latest else None,'change_counts':counts,'has_changes':chain.digest_payload(old)!=chain.digest_payload(p)}
