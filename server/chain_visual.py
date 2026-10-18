"""Read-only visualization and in-memory ledger attack experiments."""
import copy,json
import chain

def map_chain():
 rs=chain._load();first=rs[0] if rs else None
 blocks=[]
 for r in rs:
  m=r.get('payload',{}).get('manifest',{})
  blocks.append({k:r[k] for k in ('index','digest','block_hash','prev_hash','type','created_at')}|{'company_name':m.get('name',r.get('payload',{}).get('name')),'version':m.get('version')})
 return {'chain_id':'local-'+(first['block_hash'][:16] if first else 'not-created'),'chain_name':'绿碳链证本机演示链','identity_kind':'local_demo','genesis':{'index':first['index'],'prev_hash':first['prev_hash'],'created_at':first['created_at']} if first else None,'height':len(rs),'integrity':chain.chain_integrity(rs),'blocks':blocks,'hash_recipe':'记录摘要=SHA256(规范JSON材料)；区块哈希=SHA256(序号|时间|类型|记录摘要|材料|前块哈希)','explanations':['首块前哈希为64个0，后块引用前块哈希。','链标识由已有首块哈希派生，不是全网唯一名称或独立节点身份。']}
def demo(body):
 rs=copy.deepcopy(chain._load());before=chain.chain_integrity(rs);d=body.get('digest');r=next((x for x in rs if x['digest']==d),None)
 if not r:raise KeyError(d)
 mode=body.get('mode')
 if mode=='break_link':r['prev_hash']='f'*64
 elif mode in ('edit_payload','recompute_all'):r['payload']['demo_change']='内存修改，不写原记录'
 else:raise ValueError('未知链演示模式')
 if mode=='recompute_all':
  prev='0'*64
  for x in rs:
   x['digest']=chain.digest_payload(x['payload']);x['prev_hash']=prev
   pj=json.dumps(x['payload'],ensure_ascii=False,sort_keys=True)
   x['block_hash']=chain._block_hash(x['index'],x['created_at'],x['type'],x['digest'],pj,prev);prev=x['block_hash']
 after=chain.chain_integrity(rs);bad=int(after.split('@')[1]) if after!='OK' else None
 return {'before_integrity':before,'after_integrity':after,'changed_index':r['index'],'mode':mode,'explanation':'全链控制者重算可恢复内部一致性；本机链未外部锚定，演示此限制。' if mode=='recompute_all' else '修改记录或前块引用后重算校验失败；仅在内存副本进行，真实账本未改。','blocks':[{'index':x['index'],'status':'affected' if bad is not None and x['index']>=bad else 'ok'} for x in rs]}
