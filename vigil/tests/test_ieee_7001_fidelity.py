#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_governance" / "requirements"
SHARD = REQ / "requirements" / "IEEE-7001" / "2021.json"
DIGEST = "2bf1a21360236fffa7d87a71d544cd47153dae2bbcdf7e48dffe19bda289006b"

records = json.loads(SHARD.read_text())
assert len(records) == 33
ids = {r["requirement_id"] for r in records}
assert len(ids) == 33
assert all(r["source_review_date"] == "2026-09-04" for r in records)
assert all(r["interpretation_provenance"]["reviewed_source_digest"] == DIGEST for r in records)

ledger = json.loads((REQ / "metadata-review.json").read_text())
by_id = {e["requirement_id"]: e for e in ledger["entries"]}
fields = (
    "applicable_actor","governed_object","timing_or_frequency","required_artefacts",
    "evidence_expectation","verification_method","applicability_conditions",
    "exceptions_or_qualifications",
)
for r in records:
    assert r["requirement_id"] in by_id
    assert all(by_id[r["requirement_id"]]["field_status"][f] != "review-required" for f in fields)

fidelity = json.loads((REQ / "source-fidelity.json").read_text())
f = next(e for e in fidelity["entries"] if e["external_source_id"] == "IEEE-7001" and e["source_version"] == "2021")
assert f["fidelity_status"] == "assured"
assert f["effective_extraction_status"] == "complete"
assert set(f["audited_requirement_ids"]) == ids

assurance = json.loads((REQ / "source-review-assurance.json").read_text())
a = next(e for e in assurance["source_reviews"] if e["external_source_id"] == "IEEE-7001" and e["source_version"] == "2021")
assert a["reviewed_source_digest"]["digest"] == DIGEST
assert a["reviewed_source_digest"]["access_basis"] == "licensed-primary"

assert sum(r["clause_or_control"].startswith("Table 1") for r in records) == 9
assert sum(r["clause_or_control"].startswith("Table 2") for r in records) == 5
assert sum(r["clause_or_control"].startswith("Table 3") for r in records) == 7
assert sum(r["clause_or_control"].startswith("Table 4") for r in records) == 6
assert sum(r["clause_or_control"].startswith("Table 5") for r in records) == 4
assert sum(r["clause_or_control"] == "5.2.2 principle" for r in records) == 1
assert sum(r["clause_or_control"] == "5.1.1 general" for r in records) == 1
print("IEEE 7001 fidelity regression contract valid")
