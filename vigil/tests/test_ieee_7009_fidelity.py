#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQ=ROOT/"external_governance"/"requirements"
DIGEST="9fb640fd57202fcc1c90aec0b6b767bf5c4621bfdefa7911c5e102425a83b133"
RETIRED={"EXTREQ-528978BC3EB32446","EXTREQ-BBE358DBC3A6FD24","EXTREQ-C2FC30A1E260F4C1","EXTREQ-4041B6E279EF30CC"}
records=json.loads((REQ/"requirements"/"IEEE-7009"/"2024.json").read_text())
ids={r["requirement_id"] for r in records}
assert len(records)==63
assert not (RETIRED & ids)
assert all(r["source_review_date"]=="2026-09-03" for r in records)
assert all(r["interpretation_provenance"]["reviewed_source_digest"]==DIGEST for r in records)
retire=json.loads((REQ/"retirements"/"IEEE-7009-2024.json").read_text())
assert {r["requirement_id"] for r in retire["retired_requirements"]}==RETIRED
successors={sid for r in retire["retired_requirements"] for sid in r["successor_requirement_ids"]}
assert successors <= ids
ledger=json.loads((REQ/"metadata-review.json").read_text())
review_ids={e["requirement_id"] for e in ledger["entries"]}
assert not (RETIRED & review_ids)
backlog=json.loads((REQ/"reextraction-backlog.json").read_text())
assert not [e for e in backlog["entries"] if e.get("external_source_id")=="IEEE-7009" and e.get("source_version")=="2024"]
fidelity=json.loads((REQ/"source-fidelity.json").read_text())
f=next(e for e in fidelity["entries"] if e["external_source_id"]=="IEEE-7009" and e["source_version"]=="2024")
assert f["fidelity_status"]=="assured"
assert f["effective_extraction_status"]=="complete"
assert not f["known_fidelity_gaps"]
assert set(f["audited_requirement_ids"])==ids
print("IEEE 7009 identity retirement regression valid")
