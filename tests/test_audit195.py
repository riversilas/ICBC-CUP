import sys,unittest,copy,json
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'server'))
from test_extensions import ExtensionTests
import profile_extensions as e,carbon_profile as cp,profile_evidence as pe,chain,chain_visual as cv
class Audit195Tests(ExtensionTests):
 def test_signed_finance(self):
  b={'expected_revision':0,'reason':'负现金流测试','bank':{'operating_cashflow_cny':-50,'contract_target':-10,'observed_value':-20,'target_direction':'le','metric_name':'现金流变化','metric_unit':'%','assessment_period':'2024','source_title':'测试财报','url':'https://example.org/report'}};x=e.save('601991',b);self.assertEqual(e.assessment(x)['covenant']['status'],'记录达到目标')
 def test_freeze_revision(self):
  with self.assertRaises(RuntimeError):pe.freeze('601991',{'expected_revision':1})
  a=pe.freeze('601991',{'expected_revision':0});self.assertEqual(a['operation'],'created');self.assertEqual(pe.freeze('601991',{'expected_revision':0})['operation'],'reused')
 def test_structured_differences(self):
  a=pe.freeze('601991',{});m=copy.deepcopy(a['payload']['manifest']);m['profile']['metrics']['scope1']['value']+=1
  v=pe.verify({'digest':a['digest'],'manifest':m});self.assertFalse(v['material_match']);self.assertTrue(any(d['path'].endswith('scope1.value') for d in v['differences']))
 def test_radar_same_guard(self):
  original=json.loads((Path(cp.ds.PROC_RESOURCE)/'radar_attachment_snapshot.json').read_text(encoding='utf-8'));raw=copy.deepcopy(original);row=next(x for x in raw['companies'] if x['code']=='601991');row['years']['2023']['scope2_method']='location';row['years']['2024']['scope2_method']='market'
  with patch.object(cp.json,'loads',return_value=raw):
   with patch.object(cp.ext,'get',return_value=e.initial()):p=cp.profile('601991')
  self.assertTrue(all(v['value'] is None for v in p['changes'].values()));self.assertTrue(all(a['index'] is None for a in p['radar']['axes']))
 def test_break_link_single_variable(self):
  a=pe.freeze('601991',{});captured=[];original=chain.chain_integrity
  def capture(rs=None):
   if rs is not None:captured.append(copy.deepcopy(rs))
   return original(rs)
  with patch.object(chain,'chain_integrity',side_effect=capture):cv.demo({'digest':a['digest'],'mode':'break_link'})
  self.assertEqual(captured[-1][0]['payload'],a['payload']);self.assertNotEqual(captured[-1][0]['prev_hash'],a['prev_hash'])
if __name__=='__main__':unittest.main()
