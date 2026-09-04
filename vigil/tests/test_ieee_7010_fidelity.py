#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQ=ROOT/"external_governance"/"requirements"
records=json.loads((REQ/"requirements"/"IEEE-7010"/"2020.json").read_text())
DIGEST="0402e2db473736dc08f280218b895547c37d0c1a9e97a92c0432e96f9d888342"
assert len(records)==18
ids={r["requirement_id"] for r in records}
assert len(ids)==18
assert all(r["requirement_posture"]=="recommended-practice" for r in records)
assert all(r["source_review_date"]=="2026-09-04" for r in records)
assert all(r["interpretation_provenance"]["reviewed_source_digest"]==DIGEST for r in records)
ledger=json.loads((REQ/"metadata-review.json").read_text())
by={e["requirement_id"]:e for e in ledger["entries"]}
fields=("applicable_actor","governed_object","timing_or_frequency","required_artefacts","evidence_expectation","verification_method","applicability_conditions","exceptions_or_qualifications")
for r in records:
    assert all(by[r["requirement_id"]]["field_status"][f]!="review-required" for f in fields)
fid=json.loads((REQ/"source-fidelity.json").read_text())
f=next(e for e in fid["entries"] if e["external_source_id"]=="IEEE-7010" and e["source_version"]=="2020")
assert f["fidelity_status"]=="assured" and f["effective_extraction_status"]=="complete"
assert set(f["audited_requirement_ids"])==ids
ass=json.loads((REQ/"source-review-assurance.json").read_text())
a=next(e for e in ass["source_reviews"] if e["external_source_id"]=="IEEE-7010" and e["source_version"]=="2020")
assert a["reviewed_source_digest"]["digest"]==DIGEST
assert a["reviewed_source_digest"]["access_basis"]=="licensed-primary"
print("IEEE 7010 fidelity regression contract valid")
