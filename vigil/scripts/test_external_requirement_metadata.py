#!/usr/bin/env python3
"""Regression checks for the EXTREQ metadata-review contract."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_requirements"
SCRIPTS = ROOT / "scripts"
FIELDS = {
    "applicable_actor",
    "governed_object",
    "timing_or_frequency",
    "required_artefacts",
    "evidence_expectation",
    "verification_method",
    "applicability_conditions",
    "exceptions_or_qualifications",
}
STATUSES = {
    "populated-reviewed",
    "not-specified-by-source",
    "not-applicable",
    "review-required",
}


def main():
    schema = json.loads((REQ / "metadata-review.schema.json").read_text(encoding="utf-8"))
    ledger = json.loads((REQ / "metadata-review.json").read_text(encoding="utf-8"))
    assert schema["properties"]["schema_version"]["const"] == "1.0"
    required = set(schema["properties"]["entries"]["items"]["properties"]["field_status"]["required"])
    assert required == FIELDS
    enum = set(schema["$defs"]["status"]["enum"])
    assert enum == STATUSES
    assert ledger["schema_version"] == "1.0"
    assert isinstance(ledger["entries"], list)
    ids = [entry["requirement_id"] for entry in ledger["entries"]]
    assert len(ids) == len(set(ids))

    validator = (SCRIPTS / "validate-external-requirement-metadata.py").read_text(encoding="utf-8")
    assert '"source_summary"' in validator
    assert '"field_observation"' in validator
    assert "--write-report" in validator
    assert "--strict" in validator

    seeder = (SCRIPTS / "seed-eu-ai-act-metadata-review.py").read_text(encoding="utf-8")
    assert '"direct-primary-text"' in seeder
    assert '"not-specified-by-source"' in seeder
    assert "manual reconciliation required" in seeder
    assert "--write" in seeder

    print("External requirement metadata-review contract regression passed")


if __name__ == "__main__":
    main()
