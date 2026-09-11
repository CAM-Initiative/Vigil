#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_governance" / "requirements"
TARGETS = {
    "EXTREQ-528978BC3EB32446",
    "EXTREQ-BBE358DBC3A6FD24",
    "EXTREQ-C2FC30A1E260F4C1",
    "EXTREQ-4041B6E279EF30CC",
}
records = json.loads((REQ/"requirements"/"IEEE-7009"/"2024.json").read_text())
by_id = {r["requirement_id"]: r for r in records}
assert not (TARGETS & set(by_id))

ledger = json.loads((REQ/"metadata-review.json").read_text())
review = {e["requirement_id"]: e for e in ledger["entries"]}
assert not (TARGETS & set(review))

backlog = json.loads((REQ/"reextraction-backlog.json").read_text())
ieee = [e for e in backlog["entries"] if e["external_source_id"] == "IEEE-7009"]
assert not ieee

retirements = json.loads((REQ/"retirements"/"IEEE-7009-2024.json").read_text())
retired = {e["requirement_id"]: e for e in retirements["retired_requirements"]}
assert set(retired) == TARGETS
assert all(e["successor_requirement_ids"] for e in retired.values())
assert all(set(e["successor_requirement_ids"]) <= set(by_id) for e in retired.values())

fidelity = json.loads((REQ/"source-fidelity.json").read_text())
f = next(e for e in fidelity["entries"] if e["external_source_id"] == "IEEE-7009" and e["source_version"] == "2024")
assert f["fidelity_status"] == "assured"
assert f["effective_extraction_status"] == "complete"
assert not f["known_fidelity_gaps"]

assert len(records) == 63
print("IEEE 7009 legacy metadata retirement regression valid")
