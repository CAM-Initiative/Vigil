#!/usr/bin/env python3
"""Regression checks for the reviewed IEEE 7014-2024 tranche."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_governance" / "requirements"
SHARD = REQ / "requirements" / "IEEE-7014" / "2024.json"
DIGEST = "237d4d782aabf0585170e0eef8d0f313fc353b8f90cd4f94a2db0d993c45c43b"

ESTABLISHED_IDS = {
    "EXTREQ-02D226AB756E319A", "EXTREQ-0EC62DE00B448D8E", "EXTREQ-0EF26D6D174C2DCE",
    "EXTREQ-23EE57392E75BFB8", "EXTREQ-29B0D0B21F7E80D4", "EXTREQ-34FD56083CEA645E",
    "EXTREQ-38FD0063E98199E9", "EXTREQ-3DF5DD271DC23C92", "EXTREQ-3E6D02A72B66B9DC",
    "EXTREQ-42A1CFE7EF635572", "EXTREQ-4AFD90EB3C518B5F", "EXTREQ-55CAAB7FB9174CAF",
    "EXTREQ-62877173BD54BD9E", "EXTREQ-64E9E595CFF7DE6A", "EXTREQ-65D7E193EE4A942B",
    "EXTREQ-68B1E8EF3CF94A5C", "EXTREQ-6DC66967479E1698", "EXTREQ-6E38B5BF78558873",
    "EXTREQ-7033840016B023BC", "EXTREQ-719786837E5A6D9B", "EXTREQ-71E4BCCCB69D1E91",
    "EXTREQ-7C34BE7150B572DA", "EXTREQ-8C7DA8D83414FF85", "EXTREQ-915C1C74C7E78C60",
    "EXTREQ-9CB430C2CA057762", "EXTREQ-AAD0CB1FB151574D", "EXTREQ-B197A3D8996165B7",
    "EXTREQ-B8D7C1A87AFB24C8", "EXTREQ-BF238AD2E0373C07", "EXTREQ-C1CBAA44088FE2A3",
    "EXTREQ-CD5CDF96299089DE", "EXTREQ-D57F5E807D837AF8", "EXTREQ-D62D5EEFA80787DA",
    "EXTREQ-D7520BF14ED60A9B", "EXTREQ-D8BDF2032891259A", "EXTREQ-E20773A941B61CD4",
    "EXTREQ-E673B76B9E79C2FA", "EXTREQ-E7923A307C756F51", "EXTREQ-EBAA17D768C656E2",
    "EXTREQ-ED9ECFAF64B12C73", "EXTREQ-F0346554861A7BF3",
}

records = json.loads(SHARD.read_text())
assert len(records) == 59
ids = {r["requirement_id"] for r in records}
assert ESTABLISHED_IDS <= ids
assert sum(r["requirement_posture"] == "recommended-practice" for r in records) == 18
assert all(r["source_review_date"] == "2026-09-03" for r in records)
assert all(r["interpretation_provenance"]["reviewed_source_digest"] == DIGEST for r in records)

review = json.loads((REQ / "metadata-review.json").read_text())
by_id = {e["requirement_id"]: e for e in review["entries"]}
fields = (
    "applicable_actor", "governed_object", "timing_or_frequency", "required_artefacts",
    "evidence_expectation", "verification_method", "applicability_conditions",
    "exceptions_or_qualifications",
)
for r in records:
    assert r["requirement_id"] in by_id
    assert all(by_id[r["requirement_id"]]["field_status"][f] != "review-required" for f in fields)

fidelity = json.loads((REQ / "source-fidelity.json").read_text())
f = next(e for e in fidelity["entries"] if e["external_source_id"] == "IEEE-7014" and e["source_version"] == "2024")
assert f["fidelity_status"] == "assured"
assert f["effective_extraction_status"] == "complete"
assert set(f["audited_requirement_ids"]) == ids

assurance = json.loads((REQ / "source-review-assurance.json").read_text())
a = next(e for e in assurance["source_reviews"] if e["external_source_id"] == "IEEE-7014" and e["source_version"] == "2024")
assert a["reviewed_source_digest"]["digest"] == DIGEST
assert a["reviewed_source_digest"]["access_basis"] == "licensed-primary"

print("IEEE 7014 fidelity regression contract valid")
