"""Bounded registered-package differences, not fraud detection."""
def differences(registered,submitted,path='',limit=50):
 out=[]
 def visit(a,b,p):
  if len(out)>=limit:return
  if isinstance(a,dict) and isinstance(b,dict):
   for k in sorted(set(a)|set(b)):
    q=p+'.'+k if p else k
    if k not in a or k not in b:out.append({'path':q,'registered':a.get(k),'submitted':b.get(k)})
    else:visit(a[k],b[k],q)
    if len(out)>=limit:break
  elif isinstance(a,list) and isinstance(b,list):
   for i in range(max(len(a),len(b))):
    q=f'{p}[{i}]'
    if i>=len(a) or i>=len(b):out.append({'path':q,'registered':a[i] if i<len(a) else None,'submitted':b[i] if i<len(b) else None})
    else:visit(a[i],b[i],q)
    if len(out)>=limit:break
  elif type(a)!=type(b) or a!=b:out.append({'path':p,'registered':a,'submitted':b})
 visit(registered,submitted,path);return out
