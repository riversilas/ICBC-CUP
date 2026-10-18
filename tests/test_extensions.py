import sys,tempfile,os,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'server'))
import profile_extensions as e,carbon_profile as p,profile_evidence as pe,chain,chain_visual as cv
class ExtensionTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();self.env=os.environ.get('GREENCHAIN_EXTENSION_DB');os.environ['GREENCHAIN_EXTENSION_DB']=str(Path(self.t.name)/'e.sqlite3');self.old=chain.LEDGER;chain.LEDGER=str(Path(self.t.name)/'chain.json')
 def tearDown(self):
  chain.LEDGER=self.old
  if self.env is None:os.environ.pop('GREENCHAIN_EXTENSION_DB',None)
  else:os.environ['GREENCHAIN_EXTENSION_DB']=self.env
  self.t.cleanup()
 def body(self):return {'expected_revision':0,'reason':'测试补件','investments':[{'year':2024,'amount_cny':100,'total_capex_cny':1000,'classification':'transition_capex','basis':'测试分类依据','title':'测试报告','url':'https://example.org/report'}],'plans':[{'year':2024,'title':'测试风电','technology':'wind','target_value':10,'actual_value':12,'unit':'MW','status':'in_progress','source_title':'测试报告','url':'https://example.org/report'}]}
 def test_submission_and_ratios(self):
  x=e.save('601991',self.body());self.assertEqual(x['revision'],1);self.assertEqual(len(x['history']),1);z=p.profile('601991');self.assertEqual(z['extension']['investments'][0]['ratio_pct'],10);self.assertEqual(z['extension']['plans'][0]['completion_pct'],120);self.assertEqual(z['extension']['plans'][0]['status'],'in_progress')
 def test_conflict(self):
  e.save('601991',self.body())
  with self.assertRaises(e.Conflict):e.save('601991',self.body())
 def test_validation(self):
  b=self.body();b['investments'][0]['url']='javascript:alert(1)'
  with self.assertRaises(ValueError):e.save('601991',b)
  b=self.body();b['investments'][0]['amount_cny']=float('nan')
  with self.assertRaises(ValueError):e.save('601991',b)
 def test_bank_not_credit_approval(self):
  a=e.assessment(e.initial());self.assertEqual(a['stage'],'待补充材料');self.assertEqual(a['repayment']['status'],'待核验')
 def test_versions_auto_associate(self):
  a=pe.freeze('601991',{});e.save('601991',self.body());b=pe.freeze('601991',{});self.assertEqual(b['payload']['manifest']['previous_digest'],a['digest']);self.assertEqual(b['payload']['manifest']['version'],2);self.assertEqual(pe.get(a['digest'])['version_status'],'superseded')
 def test_chain_visual_no_write(self):
  a=pe.freeze('601991',{});original=Path(chain.LEDGER).read_bytes()
  for mode in ('edit_payload','break_link'):
   r=cv.demo({'digest':a['digest'],'mode':mode});self.assertNotEqual(r['after_integrity'],'OK')
  self.assertEqual(cv.demo({'digest':a['digest'],'mode':'recompute_all'})['after_integrity'],'OK');self.assertEqual(original,Path(chain.LEDGER).read_bytes());self.assertTrue(cv.map_chain()['chain_id'].startswith('local-'))
if __name__=='__main__':unittest.main()
