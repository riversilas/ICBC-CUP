"""Regression contract after retirement of the unused transparent-score module."""
import importlib.util
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'server'))
sys.path.insert(0, str(ROOT))
import engine
import carbon_profile
from version import APP_VERSION

# The root launcher is also named app.py; load the API under a distinct name.
spec = importlib.util.spec_from_file_location('backend_cleanup_api', ROOT / 'server' / 'app.py')
api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api)


class RankTests(unittest.TestCase):
    def test_average_ties_and_input_order(self):
        self.assertEqual(engine._rank([30, 10, 20, 20]), [4, 1, 2.5, 2.5])
        self.assertEqual(engine._rank([5, 5, 5]), [2, 2, 2])
        self.assertEqual(engine._rank([]), [])
        self.assertEqual(engine._rank([7]), [1])

    def test_spearman_tied_fixture(self):
        codes = list(engine.DISCLOSURES)
        # Tied ranks use Pearson correlation of midranks, not minimum ranks.
        a = [1, 1, 2, 3, 4, 5, 6, 7]
        b = [1, 2, 2, 3, 4, 5, 6, 7]
        scores = {'a': dict(zip(codes, a)), 'b': dict(zip(codes, b))}
        _, redundancy = engine.spearman_adjust(scores, {'a': .5, 'b': .5})
        ra, rb = engine._rank(a), engine._rank(b)
        mean = 4.5
        rho = sum((x-mean)*(y-mean) for x, y in zip(ra, rb)) / (
            sum((x-mean)**2 for x in ra)*sum((y-mean)**2 for y in rb))**.5
        self.assertAlmostEqual(redundancy['a'], 1-rho)
        self.assertAlmostEqual(rho, 0.9819277108433735)


class BackendCleanupTests(unittest.TestCase):
    def test_shared_application_version_not_method_version(self):
        self.assertEqual(api.app.version, APP_VERSION)
        self.assertEqual(api.application_version(), {'application_version': APP_VERSION})
        self.assertEqual(carbon_profile.VERSION, 'scope12-transition-1.9.4')
        self.assertEqual(engine.MODEL_VERSION, 'Carbon-Model-V1.0-Adapted-Power')
        self.assertEqual(api._legacy_main.MODEL_VERSION, 'GreenTrace-Power V3.2 (等权五维雷达)')

    def test_removed_diagnostic_and_weight_route(self):
        self.assertFalse((ROOT / 'server' / 'radar_diagnostic.py').exists())
        self.assertNotIn('/api/weight-basis', {r.path for r in api.app.routes})
        self.assertNotIn('radar_diagnostic', vars(api))
        self.assertNotIn('radar-addon.js', (ROOT / 'server' / 'static' / 'app.html').read_text(encoding='utf-8'))

    def test_company_list_no_score_fields(self):
        response = api.companies()
        self.assertEqual(response['count'], 8)
        for row in response['companies']:
            self.assertFalse({'final_score', 'transparent_score', 'completed_dimensions'} & row.keys())
        self.assertNotIn('radar_diagnostic', api.company('601991'))

    def test_legacy_attestation_no_diagnostic_fields(self):
        with patch.object(api.chain, 'publish', side_effect=lambda payload, kind: payload):
            payload = api.attest_company('601991')
        self.assertFalse({'score_version', 'transparent_score', 'radar_version', 'radar_diagnostic'} & payload.keys())
        self.assertIn('model_version', payload)

    def test_legacy_quantification_retained_explicitly_deprecated(self):
        route = next(r for r in api.app.routes if r.path == '/api/main-quant/{code}')
        self.assertTrue(route.deprecated)
        payload = api.main_quant('601991')
        self.assertEqual(set(payload), {'code', 'name', 'type', 'carbon', 'scoring_method', 'evidence', 'reports_count', 'reports'})
        self.assertEqual(payload['carbon']['model_version'], api._legacy_main.MODEL_VERSION)
        self.assertIn('rating', payload['carbon'])

    def test_active_profile_is_raw_and_preserves_data(self):
        p = carbon_profile.profile('601991')
        self.assertFalse({'rating', 'carbon_score', 'transparent_score', 'completed_dimensions'} & p.keys())
        self.assertEqual(p['metrics']['total']['value'], 210925500)
        self.assertEqual(p['data_kind'], 'attachment_unverified')
        self.assertEqual(p['scope2_method'], 'unknown')
        json.dumps(p, allow_nan=False)


if __name__ == '__main__':
    unittest.main()
