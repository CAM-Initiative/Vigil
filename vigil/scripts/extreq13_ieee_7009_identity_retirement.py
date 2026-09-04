#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_governance" / "requirements"
SHARD = REQ / "requirements" / "IEEE-7009" / "2024.json"
LEDGER = REQ / "metadata-review.json"
BACKLOG = REQ / "reextraction-backlog.json"
FIDELITY = REQ / "source-fidelity.json"
RETIRE_DIR = REQ / "retirements"
RETIRE = RETIRE_DIR / "IEEE-7009-2024.json"

DATE = "2026-09-04"
SOURCE_ID = "EXT-564A4CAA4F00"
EXTERNAL_ID = "IEEE-7009"
VERSION = "2024"

RETIREMENTS = {
    "EXTREQ-528978BC3EB32446": {
        "identity_key": "7009-monitor-detect-identify-anomaly",
        "clause_or_control": "6.1(a-c)",
        "successor_requirement_ids": [
            "EXTREQ-8204FA30873DD481",
            "EXTREQ-5306FB227197570A",
            "EXTREQ-95307E8CDBC1B4BE",
        ],
        "reason": "Legacy aggregate compressed three independently assessable source-native requirements.",
    },
    "EXTREQ-BBE358DBC3A6FD24": {
        "identity_key": "7009-moderate-modify-behavior",
        "clause_or_control": "6.1(d-e)",
        "successor_requirement_ids": [
            "EXTREQ-09AC3C68DD3B9DA0",
            "EXTREQ-3197D476F0F03090",
        ],
        "reason": "Legacy aggregate compressed two independently assessable source-native requirements.",
    },
    "EXTREQ-C2FC30A1E260F4C1": {
        "identity_key": "7009-operational-monitor-diagnose",
        "clause_or_control": "8.3 DIOP1-3",
        "successor_requirement_ids": [
            "EXTREQ-3CCDC8232F3887B6",
            "EXTREQ-1D3ECE3F78BA0638",
            "EXTREQ-81F4A4D7227B1970",
        ],
        "reason": "Legacy aggregate compressed DIOP1 through DIOP3 into one analytical identity.",
    },
    "EXTREQ-4041B6E279EF30CC": {
        "identity_key": "7009-operational-moderate-modify-evaluate",
        "clause_or_control": "8.3 DIOP4-6",
        "successor_requirement_ids": [
            "EXTREQ-4A98B446C4E83ECE",
            "EXTREQ-D400D6712209533C",
            "EXTREQ-2E3CBE869A1E2400",
        ],
        "reason": "Legacy aggregate compressed DIOP4 through DIOP6 into one analytical identity.",
    },
}

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def dump(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

records = load(SHARD)
by_id = {r["requirement_id"]: r for r in records}
assert len(records) == 67
assert set(RETIREMENTS) <= set(by_id)

# Verify the mapped atomic successors are already canonical and source-aligned.
all_successors = set()
for rid, spec in RETIREMENTS.items():
    r = by_id[rid]
    assert r["identity_key"] == spec["identity_key"]
    assert r["clause_or_control"] == spec["clause_or_control"]
    assert set(r["related_external_requirements"]) == set(spec["successor_requirement_ids"])
    for sid in spec["successor_requirement_ids"]:
        assert sid in by_id, (rid, sid)
        s = by_id[sid]
        assert s["external_source_id"] == EXTERNAL_ID and s["source_version"] == VERSION
        all_successors.add(sid)

# Durable retirement map preserves immutable historical identities and successor resolution.
retirement_doc = {
    "schema_version": "1.0",
    "source": {
        "vigil_source_id": SOURCE_ID,
        "external_source_id": EXTERNAL_ID,
        "source_version": VERSION,
    },
    "retired_at": DATE,
    "retirement_basis": "explicit-maintainer-approved-semantic-decomposition",
    "retired_requirements": [
        {
            "requirement_id": rid,
            "identity_key": spec["identity_key"],
            "clause_or_control": spec["clause_or_control"],
            "successor_requirement_ids": spec["successor_requirement_ids"],
            "reason": spec["reason"],
            "historical_record_preservation": "git-history-and-retirement-map",
        }
        for rid, spec in RETIREMENTS.items()
    ],
}
dump(RETIRE, retirement_doc)

# Remove only the four approved aggregates from the live canonical source shard.
records = [r for r in records if r["requirement_id"] not in RETIREMENTS]
assert len(records) == 63
assert not (set(RETIREMENTS) & {r["requirement_id"] for r in records})
assert all_successors <= {r["requirement_id"] for r in records}
dump(SHARD, records)

# Retired identities are no longer live metadata-review subjects.
ledger = load(LEDGER)
ledger["updated_at"] = DATE
ledger["entries"] = [e for e in ledger["entries"] if e["requirement_id"] not in RETIREMENTS]
assert not (set(RETIREMENTS) & {e["requirement_id"] for e in ledger["entries"]})
dump(LEDGER, ledger)

# The four re-extraction defects are resolved by approved identity retirement.
backlog = load(BACKLOG)
before = len(backlog["entries"])
backlog["entries"] = [
    e for e in backlog["entries"]
    if not (
        e.get("external_source_id") == EXTERNAL_ID
        and e.get("source_version") == VERSION
        and e.get("current_requirement_id") in RETIREMENTS
    )
]
assert before - len(backlog["entries"]) == 4
assert not [e for e in backlog["entries"] if e.get("external_source_id") == EXTERNAL_ID and e.get("source_version") == VERSION]
dump(BACKLOG, backlog)

# Promote source fidelity only after aggregate identities are no longer canonical.
fidelity = load(FIDELITY)
fidelity["reviewed_at"] = DATE
for e in fidelity["entries"]:
    if e["external_source_id"] == EXTERNAL_ID and e["source_version"] == VERSION:
        e["fidelity_status"] = "assured"
        e["effective_extraction_status"] = "complete"
        e["assessment_basis"] = (
            "Direct licensed-primary review established source-native atomic coverage. "
            "On explicit maintainer approval, the four legacy aggregate identities for Clause 6.1(a-c), Clause 6.1(d-e), DIOP1-3 and DIOP4-6 were retired from the live corpus to their already-canonical linked atomic successors. "
            "The remaining 63 IEEE 7009-2024 records are the live bounded analytical corpus; no known semantic-fidelity gap remains."
        )
        e["known_fidelity_gaps"] = []
        e["audited_requirement_ids"] = sorted(r["requirement_id"] for r in records)
        e["next_action"] = "Retain the 63 live reviewed identities and the durable retirement map; repeat fidelity review on material revision of IEEE 7009."
        break
else:
    raise AssertionError("IEEE-7009 fidelity entry missing")
dump(FIDELITY, fidelity)

print("IEEE 7009 identity retirement staged: 4 legacy aggregates retired to 11 existing atomic successors; 63 live records remain.")
