# -*- coding: utf-8 -*-
"""绿鉴(绿碳链证)MVP - 存证层: SHA256 哈希链账本 (按 TECH_DOC §6)

竞赛阶段用本地哈希链模拟联盟链; 替换 publish_to_bcos() 即接入 FISCO BCOS。

V1.5 升级: 从"孤立摘要列表"升级为真正的【哈希链(Blockchain 结构)】:
  - 每个区块包含 prev_hash(前块哈希), 形成链式结构
  - block_hash = SHA256(index|timestamp|type|payload_digest|prev_hash)
  - 任何历史记录被篡改 → 该块 block_hash 变化 → 后续所有块 prev_hash 失配
    → chain_integrity() 校验失败 → 篡改可被数学证明
这使"防篡改"从口号变为可现场演示的数学性质。

路径兼容开发与 PyInstaller 打包: 账本写在 exe 同目录, 保证可写。
"""
import json, os, sys, hashlib, threading, tempfile
_WRITE_LOCK = threading.RLock()
from datetime import datetime


def _ledger_path():
    if getattr(sys, "frozen", False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "processed"))
    return os.path.join(base, "chain_ledger.json")


LEDGER = _ledger_path()

GENESIS_PREV = "0" * 64


def _sha(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


def digest_payload(payload: dict) -> str:
    """业务数据摘要: 对payload做规范JSON后SHA256"""
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return _sha(raw)


def _load() -> list:
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8") as f:
            records = json.load(f)
        return _migrate(records)
    return []


def _migrate(records: list) -> list:
    """V1.4→V1.5 账本格式迁移: 旧孤立摘要记录按原序重建为哈希链区块。
    保留原 digest/type/created_at/payload, 补算 prev_hash/block_hash。
    迁移结果不写回磁盘(下次 publish 时自然以新格式追加), 但本次内存中链完整。"""
    if not records or "block_hash" in records[0]:
        return records
    prev = GENESIS_PREV
    migrated = []
    for i, r in enumerate(records):
        pj = json.dumps(r.get("payload", {}), ensure_ascii=False, sort_keys=True)
        digest = r.get("digest") or _sha(pj)
        created = r.get("created_at", "")
        btype = r.get("type", "legacy")
        migrated.append({
            "index": i, "digest": digest, "type": btype,
            "created_at": created, "prev_hash": prev,
            "block_hash": _block_hash(i, created, btype, digest, pj, prev),
            "payload": r.get("payload", {}),
        })
        prev = migrated[-1]["block_hash"]
    return migrated


def _save(records: list):
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix='ledger-', suffix='.tmp', dir=os.path.dirname(LEDGER))
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False, indent=1, allow_nan=False)
            f.flush(); os.fsync(f.fileno())
        os.replace(temp, LEDGER)
    finally:
        if os.path.exists(temp): os.unlink(temp)


def _block_hash(index, created_at, btype, digest, payload_json, prev_hash) -> str:
    """块哈希覆盖全部内容(含 payload 原文): 篡改任一字段都会导致哈希失配"""
    raw = f"{index}|{created_at}|{btype}|{digest}|{payload_json}|{prev_hash}"
    return _sha(raw)


def publish(payload: dict, payload_type: str) -> dict:
    with _WRITE_LOCK:
        return _publish_locked(payload, payload_type)

def _publish_locked(payload: dict, payload_type: str) -> dict:
    """生成业务摘要并作为新区块写入哈希链(幂等: 同payload返回已有区块)"""
    records = _load()  # 旧格式账本在此处内存迁移为哈希链
    payload_json = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    digest = _sha(payload_json)
    for r in records:
        if r["digest"] == digest:
            _persist_migration(records)  # 命中旧记录 → 账本一次性落盘为新格式
            return r
    return _publish_new(payload, payload_type, payload_json, digest)


def _persist_migration(records: list):
    """若磁盘账本仍是旧格式而内存已迁移, 则以新格式重写(一次性迁移落盘)"""
    if not records or not os.path.exists(LEDGER):
        return
    with open(LEDGER, encoding="utf-8") as f:
        disk = json.load(f)
    if disk and "block_hash" not in disk[0]:
        _save(records)


def _publish_new(payload: dict, payload_type: str, payload_json: str, digest: str) -> dict:
    records = _load()
    index = len(records)
    created_at = datetime.now().isoformat(timespec="seconds")
    prev_hash = records[-1]["block_hash"] if records else GENESIS_PREV
    rec = {
        "index": index,
        "digest": digest,          # 业务数据摘要(供查验)
        "type": payload_type,
        "created_at": created_at,
        "prev_hash": prev_hash,    # 前块哈希 → 链式结构
        "block_hash": _block_hash(index, created_at, payload_type, digest, payload_json, prev_hash),
        "payload": payload,
    }
    records.append(rec)
    _save(records)
    return rec


def verify(digest: str) -> dict:
    """查验: 找到摘要对应区块, 并校验整条链完整性"""
    records = _load()
    integrity = chain_integrity(records)
    for r in records:
        if r["digest"] == digest:
            return {
                "valid": True,
                "integrity": integrity,   # "OK" 或 "BROKEN@n"
                "record": r,
            }
    return {"valid": False, "integrity": integrity, "record": None}


def chain_integrity(records: list = None) -> str:
    """校验哈希链完整性: 重算每块 block_hash(含payload原文) 并核对 prev_hash 链接。
    返回 'OK' 或 'BROKEN@<区块号>' —— 篡改任一历史块即可现场演示侦测。"""
    if records is None:
        records = _load()
    prev = GENESIS_PREV
    for r in records:
        pj = json.dumps(r["payload"], ensure_ascii=False, sort_keys=True)
        expect = _block_hash(r["index"], r["created_at"], r["type"], r["digest"], pj, r["prev_hash"])
        if r["prev_hash"] != prev or r["block_hash"] != expect:
            return f"BROKEN@{r['index']}"
        if digest_payload(r["payload"]) != r["digest"]:
            return f"BROKEN@{r['index']}"
        prev = r["block_hash"]
    return "OK"


def chain_stats() -> dict:
    records = _load()
    return {"height": len(records), "integrity": chain_integrity(records),
            "last_hash": records[-1]["block_hash"][:16] + "…" if records else "-"}


def publish_to_bcos(payload_digest: str) -> str:
    """[预留] FISCO BCOS 存证合约调用。竞赛演示不启用。
    实现要点: 通过 WeBASE REST API 调用存证合约 record(string digest) 方法,
    返回交易哈希写入区块的 tx 字段; 联盟链进一步提供多节点共识背书。"""
    raise NotImplementedError("竞赛阶段使用本地哈希链; 上链为 V1.5+ 功能")
