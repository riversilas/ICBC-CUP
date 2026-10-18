"""Cross-platform startup smoke test; no writes to evidence or supplements."""
from pathlib import Path
import json
import math
import socket
import subprocess
import sys
import time
import urllib.request

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
from version import APP_VERSION
with socket.socket() as sock:
    sock.bind(('127.0.0.1', 0))
    port = sock.getsockname()[1]
proc = subprocess.Popen([sys.executable, str(root / 'app.py'), '--port', str(port), '--no-browser'], cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
try:
    deadline = time.monotonic() + 25
    base = f'http://127.0.0.1:{port}'
    while True:
        if proc.poll() is not None:
            raise RuntimeError(proc.stdout.read().decode('utf-8', errors='replace'))
        try:
            with urllib.request.urlopen(base + '/api/carbon-profiles', timeout=1) as res:
                data = json.load(res)
            break
        except (OSError, ValueError):
            if time.monotonic() > deadline:
                raise RuntimeError('Startup timed out')
            # Bounded readiness retry, not a scheduled task or reminder.
            time.sleep(0.2)
    assert data['count'] == 8
    for endpoint in ['/', '/app', '/static/logo-mark.svg', '/static/novice-audit.css']:
        with urllib.request.urlopen(base + endpoint, timeout=5) as res:
            assert res.status == 200, endpoint
    with urllib.request.urlopen(base + '/api/version', timeout=5) as res:
        assert json.load(res)['application_version'] == APP_VERSION
    with urllib.request.urlopen(base + '/openapi.json', timeout=5) as res:
        schema = json.load(res)
    assert schema['info']['version'] == APP_VERSION
    assert '/api/weight-basis' not in schema['paths']
    assert schema['paths']['/api/main-quant/{code}']['get']['deprecated'] is True
    with urllib.request.urlopen(base + '/api/carbon-profile/601991', timeout=5) as res:
        profile = json.load(res)
    metrics = profile['metrics']
    assert profile['data_kind'] == 'attachment_unverified'
    assert profile['scope2_method'] == 'unknown'
    assert profile['comparability'] == 'assumed_comparable_for_demo_only'
    assert metrics['scope1']['value'] is not None
    assert metrics['scope2']['value'] is not None
    assert math.isclose(metrics['total']['value'], metrics['scope1']['value'] + metrics['scope2']['value'])
    assert math.isclose(metrics['intensity']['value'], metrics['total']['value'] / metrics['production']['value'])
    assert len(profile['trend']) == 3
    assert profile['sources'] and profile['method_version']
    assert not {'rating', 'carbon_score', 'transparent_score', 'completed_dimensions'} & profile.keys()
    with urllib.request.urlopen(base + '/api/companies', timeout=5) as res:
        companies = json.load(res)['companies']
    assert all(not {'final_score', 'transparent_score', 'completed_dimensions'} & row.keys() for row in companies)
    print('PASS startup, 8 profiles, static resources, shared application version and raw Scope 1/2 profile')
finally:
    if proc.poll() is None:
        proc.terminate()
    try:
        proc.communicate(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.communicate()
