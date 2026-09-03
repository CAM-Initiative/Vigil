#!/usr/bin/env python3
"""Regression checks for the bounded IEEE 7009-2024 fidelity repair."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_governance" / "requirements"
DIGEST = "9fb640fd57202fcc1c90aec0b6b767bf5c4621bfdefa7911c5e102425a83b133"
COARSE = {
    "EXTREQ-528978BC3EB32446": {"EXTREQ-8204FA30873DD481", "EXTREQ-5306FB227197570A", "EXTREQ-95307E8CDBC1B4BE"},
    "EXTREQ-BBE358DBC3A6FD24": {"EXTREQ-09AC3C68DD3B9DA0", "EXTREQ-3197D476F0F03090"},
    "EXTREQ-C2FC30A1E260F4C1": {"EXTREQ-3CCDC8232F3887B6", "EXTREQ-1D3ECE3F78BA0638", "EXTREQ-81F4A4D7227B1970"},
    "EXTREQ-4041B6E279EF30CC": {"EXTREQ-4A98B446C4E83ECE", "EXTREQ-D400D6712209533C", "EXTREQ-2E3CBE869A1E2400"},
}
UNRESOLVED = {"timing_or_frequency", "required_artefacts", "evidence_expectation", "verification_method", "exceptions_or_qualifications"}

records = json.loads((REQ / "requirements" / "IEEE-7009" / "2024.json").read_text(encoding="utf-8"))
by_id = {record["requirement_id"]: record for record in records}
ledger = json.loads((REQ / "metadata-review.json").read_text(encoding="utf-8"))
review_by_id = {entry["requirement_id"]: entry for entry in ledger["entries"]}
backlog = json.loads((REQ / "reextraction-backlog.json").read_text(encoding="utf-8"))
fidelity = json.loads((REQ / "source-fidelity.json").read_text(encoding="utf-8"))

assert len(records) == 67
assert all(record["source_review_date"] == "2026-09-03" for record in records)
assert all(record["interpretation_provenance"]["reviewed_source_digest"] == DIGEST for record in records)
for legacy_id, successors in COARSE.items():
    assert legacy_id in by_id
    assert set(by_id[legacy_id]["related_external_requirements"]) == successors
assert by_id["EXTREQ-BA54F8982F880F93"]["clause_or_control"] == "9.3"
assert by_id["EXTREQ-BA54F8982F880F93"]["requirement_posture"] == "definitional"
for record in records:
    statuses = review_by_id[record["requirement_id"]]["field_status"]
    if record["requirement_id"] in COARSE:
        assert {field for field, status in statuses.items() if status == "review-required"} == UNRESOLVED
    else:
        assert all(status != "review-required" for status in statuses.values())
ieee_backlog = [entry for entry in backlog["entries"] if entry["external_source_id"] == "IEEE-7009"]
assert {entry["current_requirement_id"] for entry in ieee_backlog} == set(COARSE)
source_fidelity = next(entry for entry in fidelity["entries"] if entry["external_source_id"] == "IEEE-7009" and entry["source_version"] == "2024")
assert source_fidelity["fidelity_status"] == "requires-reextraction"
assert source_fidelity["effective_extraction_status"] == "partial"
print("IEEE 7009 bounded fidelity regression passed")
