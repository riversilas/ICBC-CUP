import sys,tempfile,unittest,json,copy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'server'))
import carbon_profile as c,profile_evidence as e,chain
class ProfileTests(unittest.TestCase):
 def setUp(self):self.temp=tempfile.TemporaryDirectory();self.old=chain.LEDGER;chain.LEDGER=str(Path(self.temp.name)/'ledger.json')
 def tearDown(self):chain.LEDGER=self.old;self.temp.cleanup()
 def test_formula(self):
  p=c.profile('601991');r=p['metrics'];self.assertAlmostEqual(r['total']['value'],210925500);self.assertAlmostEqual(r['intensity']['value'],210925500/285153);self.assertEqual(p['comparability'],'assumed_comparable_for_demo_only');self.assertEqual(len(p['trend']),3)
 def test_known_gas_mismatch(self):
  r=c.annual({'scope1_tco2':100,'scope2_tco2':10,'power_gen_gwh':1,'scope1_gas_basis':'CO2','scope2_gas_basis':'CO2e'},2024);self.assertIsNone(r['total']);self.assertIsNone(r['intensity'])
 def test_missing_previous(self):
  p=c.profile('600011');self.assertTrue(all(x['value'] is None for x in p['changes'].values()));self.assertEqual(c.companies()['count'],8)
 def test_frozen_and_idempotent(self):
  a=e.freeze('601991',{});b=e.freeze('601991',{});self.assertEqual(a['digest'],b['digest']);self.assertEqual(len(chain._load()),1);self.assertIsNone(e.verify({'digest':a['digest']})['material_match']);self.assertTrue(e.verify({'digest':a['digest'],'manifest':a['payload']['manifest']})['material_match'])
 def test_demo_never_writes(self):
  a=e.freeze('601991',{});before=Path(chain.LEDGER).read_bytes();self.assertTrue(e.demo({'digest':a['digest'],'mode':'clean'})['material_match']);self.assertFalse(e.demo({'digest':a['digest'],'mode':'changed_value'})['material_match']);self.assertFalse(e.demo({'digest':a['digest'],'mode':'changed_base'})['material_match']);self.assertEqual(before,Path(chain.LEDGER).read_bytes())
 def test_versions(self):
  a=e.freeze('601991',{});b=e.freeze('601991',{'previous_digest':a['digest'],'change_reason':'重核口径，原数据未改，保留更正说明'});self.assertEqual(b['payload']['manifest']['version'],2);self.assertEqual(e.get(a['digest'])['version_status'],'superseded');self.assertEqual(e.get(a['digest'])['payload'],a['payload'])
 def test_guards(self):
  a=e.freeze('601991',{})
  with self.assertRaises(ValueError):e.freeze('600886',{'previous_digest':a['digest'],'change_reason':'bad'})
  with self.assertRaises(ValueError):e.freeze('601991',{'previous_digest':a['digest']})
  with self.assertRaises(ValueError):e.verify({'digest':a['digest'],'manifest':[]})
 def test_payload_tamper(self):
  a=e.freeze('601991',{});x=chain._load();x[0]['payload']['manifest']['profile']['metrics']['scope1']['value']+=1;self.assertEqual(chain.chain_integrity(x),'BROKEN@0')
if __name__=='__main__':unittest.main()
