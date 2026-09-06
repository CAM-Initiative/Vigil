#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];REQ=ROOT/"external_governance"/"requirements"
records=json.loads((REQ/"requirements"/"IEEE-7007"/"2021.json").read_text())
DIGEST="8689b98d77141330e380394ce7eef5961c9539227340949357fc860c74e683d7"
assert len(records)==10 and len({r["requirement_id"] for r in records})==10
assert all(r["requirement_posture"]=="definitional" for r in records)
assert all(r["source_review_date"]=="2026-09-04" for r in records)
assert all(r["interpretation_provenance"]["reviewed_source_digest"]==DIGEST for r in records)
assert all(not r["timing_or_frequency"] and not r["required_artefacts"] and not r["evidence_expectation"] and not r["verification_method"] for r in records)
ledger=json.loads((REQ/"metadata-review.json").read_text());by={e["requirement_id"]:e for e in ledger["entries"]}
for r in records:
    s=by[r["requirement_id"]]["field_status"]
    assert s["applicable_actor"]=="populated-reviewed" and s["governed_object"]=="populated-reviewed"
    assert s["timing_or_frequency"]=="not-specified-by-source"
    assert s["required_artefacts"]=="not-specified-by-source"
    assert s["evidence_expectation"]=="not-specified-by-source"
    assert s["verification_method"]=="not-specified-by-source"
    assert s["applicability_conditions"]=="populated-reviewed"
    assert s["exceptions_or_qualifications"]=="populated-reviewed"
fid=json.loads((REQ/"source-fidelity.json").read_text());f=next(e for e in fid["entries"] if e["external_source_id"]=="IEEE-7007" and e["source_version"]=="2021")
assert f["fidelity_status"]=="assured" and f["effective_extraction_status"]=="complete"
assert set(f["audited_requirement_ids"])=={r["requirement_id"] for r in records}
print("IEEE 7007 fidelity regression contract valid")
