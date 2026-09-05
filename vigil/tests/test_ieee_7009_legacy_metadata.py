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
FIELDS = (
    "applicable_actor","governed_object","timing_or_frequency","required_artefacts",
    "evidence_expectation","verification_method","applicability_conditions",
    "exceptions_or_qualifications",
)

records = json.loads((REQ/"requirements"/"IEEE-7009"/"2024.json").read_text())
by_id = {r["requirement_id"]: r for r in records}
assert TARGETS <= set(by_id)
for rid in TARGETS:
    r = by_id[rid]
    assert r["timing_or_frequency"]
    assert r["required_artefacts"]
    assert r["evidence_expectation"]
    assert r["verification_method"]
    assert r["exceptions_or_qualifications"]
    assert r["related_external_requirements"]

ledger = json.loads((REQ/"metadata-review.json").read_text())
review = {e["requirement_id"]: e for e in ledger["entries"]}
affected = {
    "timing_or_frequency", "required_artefacts", "evidence_expectation",
    "verification_method", "exceptions_or_qualifications",
}
for rid in TARGETS:
    s = review[rid]["field_status"]
    assert s["applicable_actor"] == "populated-reviewed"
    assert s["governed_object"] == "populated-reviewed"
    assert s["applicability_conditions"] == "populated-reviewed"
    assert all(s[f] == "review-required" for f in affected)

backlog = json.loads((REQ/"reextraction-backlog.json").read_text())
ieee = [e for e in backlog["entries"] if e["external_source_id"] == "IEEE-7009"]
assert {e["current_requirement_id"] for e in ieee} == TARGETS
assert all(e["review_status"] == "in-review" for e in ieee)
assert all(e["recommended_repair"] == "semantic-decomposition-with-identity-migration" for e in ieee)

fidelity = json.loads((REQ/"source-fidelity.json").read_text())
f = next(e for e in fidelity["entries"] if e["external_source_id"] == "IEEE-7009" and e["source_version"] == "2024")
assert f["fidelity_status"] == "requires-reextraction"
assert f["effective_extraction_status"] == "partial"
assert len(f["known_fidelity_gaps"]) == 2

assert len(records) == 67
print("IEEE 7009 legacy metadata closure regression valid")
