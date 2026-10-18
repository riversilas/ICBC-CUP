# -*- coding: utf-8 -*-
"""绿鉴MVP - API层 FastAPI (接口清单见 TECH_DOC.md §4)"""
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response
from pathlib import Path
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from version import APP_VERSION
import data_store as ds
import engine
import chain
import carbon_profile
import profile_evidence
import profile_extensions
import chain_visual

app = FastAPI(title="绿碳链证 — 可信 ESG 数据平台", version=APP_VERSION)

STATIC = Path(__file__).parent / "static"


@app.get("/")
def index():
    return FileResponse(STATIC / "app.html")


def profile_call(fn,*args):
    try: return fn(*args)
    except KeyError as e: raise HTTPException(404, '未找到客户或凭证')
    except ValueError as e: raise HTTPException(422, str(e))
    except RuntimeError as e: raise HTTPException(409, str(e))

@app.get('/api/evidence/chain-map')
def evidence_chain_map(): return profile_call(chain_visual.map_chain)
@app.post('/api/evidence/chain-demo')
def evidence_chain_demo(body:dict): return profile_call(chain_visual.demo,body)
@app.get('/api/carbon-profile/{code}/supplements')
def supplements(code:str): return profile_call(profile_extensions.get,code)
@app.post('/api/carbon-profile/{code}/supplements')
def save_supplements(code:str,body:dict): return profile_call(profile_extensions.save,code,body)

@app.get('/api/carbon-profile/{code}/freeze-preview')
def freeze_preview(code:str): return profile_call(profile_evidence.preview,code)

@app.get('/api/carbon-profiles')
def carbon_profiles(): return profile_call(carbon_profile.companies)
@app.get('/api/carbon-profile/{code}')
def carbon_detail(code:str): return profile_call(carbon_profile.profile,code)
@app.post('/api/carbon-profile/{code}/freeze')
def carbon_freeze(code:str,body:dict): return profile_call(profile_evidence.freeze,code,body)
@app.get('/api/evidence/recent')
def recent_evidence(): return profile_call(profile_evidence.recent)
@app.post('/api/evidence/verify')
def material_verify(body:dict): return profile_call(profile_evidence.verify,body)
@app.post('/api/evidence/demo')
def material_demo(body:dict): return profile_call(profile_evidence.demo,body)
@app.get('/api/evidence/{digest}/manifest')
def download_manifest(digest:str):
    r=profile_call(profile_evidence.get,digest)
    raw=__import__('json').dumps(r['payload']['manifest'],ensure_ascii=False,sort_keys=True,allow_nan=False)
    return Response(raw.encode('utf-8'),media_type='application/json',headers={'Content-Disposition':'attachment; filename="carbon-manifest.json"'})
@app.get('/api/evidence/{digest}')
def get_evidence(digest:str): return profile_call(profile_evidence.get,digest)

@app.get('/api/version')
def application_version():
    return {'application_version': APP_VERSION}

@app.get("/api/companies", deprecated=True)
def companies():
    """Legacy metric-list compatibility; active raw profiles use /api/carbon-profiles."""
    out = []
    for code, d in ds.DISCLOSURES.items():
        a = engine.analyze(code)
        out.append({"code": code, "name": d["name"], "type": d["type"],
                    "reports_count": len(ds.load_reports_index().get(code, {}).get("reports", [])),
                    **a["metrics"]})
    return {"count": len(out), "companies": out}


@app.get("/api/company/{code}", deprecated=True)
def company(code: str):
    """Historical four-variable analysis only; not the current profile result."""
    a = engine.analyze(code)
    if not a:
        return {"error": "not found", "code": code}
    # 附报告存证索引
    idx = ds.load_reports_index().get(code, {})
    a["reports_count"] = len(idx.get("reports", []))
    a["reports"] = idx.get("reports", [])
    return a


@app.get("/api/reports/{code}")
def reports(code: str):
    idx = ds.load_reports_index().get(code, {})
    recs = ds.report_digest_index()
    return {"code": code, "name": idx.get("name"),
            "reports": idx.get("reports", []),
            "digest_records": [r for r in recs if r["code"] == code]}


@app.post("/api/bank/query",deprecated=True)
def bank_query(body: dict):
    """工行系统对接接口: 批量查询企业环境指标+绿色表现参考"""
    codes = body.get("codes") or []
    out = []
    for c in codes:
        a = engine.analyze(c)
        if a:
            m = a["metrics"]
            out.append({"code": c, "name": a["name"],
                        "emission_intensity": m["emission_intensity_tco2_per_gwh"],
                        "green_flag": m["green_flag"],
                        "completeness_pct": m["completeness_pct"],
                        "risk_levels": [r["level"] for r in a["risks"]]})
    return {"legacy": True, "api_version": "historical-v1", "bank_facing": True, "disclaimer": "数据参考, 不构成授信结论",
            "results": out}


# ---------- 存证 ----------
@app.post("/api/attest/company/{code}", deprecated=True)
def attest_company(code: str):
    """Historical analysis attestation compatibility; current reports use profile freeze."""
    a = engine.analyze(code)
    if not a:
        return {"error": "not found"}
    cm = a["carbon_model"]
    payload = {
        "company": code, "name": a["name"],
        "final_score": cm["final_score"],
        "confidence_grade": cm["confidence_grade"],
        "model_version": cm["model_version"],
        "weight_version": cm["weight_version"],
        "pathway_version": cm["pathway_version"],
        "metrics": a["metrics"],
    }
    rec = chain.publish(payload, "analysis")
    return rec


@app.get("/api/chain/blocks")
def chain_blocks():
    """链上全部区块(简化视图, 供前端哈希链可视化)"""
    recs = chain._load()
    integrity = chain.chain_integrity(recs)
    broken_at = None
    if integrity != "OK":
        broken_at = int(integrity.split("@")[1])
    return [
        {"index": r["index"], "digest": r["digest"],
         "prev_hash": r["prev_hash"], "block_hash": r["block_hash"],
         "created_at": r["created_at"], "type": r["type"],
         "integrity_bad": (broken_at is not None and r["index"] >= broken_at)}
        for r in recs
    ]


@app.get("/api/chain")
def chain_info():
    """链状态: 高度/完整性/最新块哈希 — 现场演示区块链结构"""
    return chain.chain_stats()


@app.get("/api/verify/{digest}")
def verify(digest: str):
    return chain.verify(digest)


app.mount("/static", StaticFiles(directory=str(STATIC)), name="static")

# Root main quantification retained separately from local evidence/profile APIs.
import legacy_main as _legacy_main
@app.get('/app')
def workspace_page(): return FileResponse(str(Path(__file__).resolve().parent / 'static' / 'app.html'))
@app.get('/api/legacy-evidence/{digest}')
def legacy_evidence(digest:str):
    return _legacy_main.verify(digest)

@app.get('/api/main-quant/{code}', deprecated=True)
def main_quant(code:str):
    """Historical V3.2 compatibility only; not the active Scope 1/2 profile."""
    if code not in _legacy_main.BY_CODE: raise HTTPException(status_code=404,detail='主线未收录该企业的量化数据')
    return _legacy_main.company_payload(code)
