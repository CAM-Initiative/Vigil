#!/usr/bin/env python3
"""Regression checks for the EXTREQ metadata-review contract."""
from __future__ import annotations
import importlib.util
import json
import tempfile
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


def load_script(name: str):
    path = SCRIPTS / name
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def assert_conflict_intolerant(script_name: str, requirement_id: str) -> None:
    module = load_script(script_name)
    ledger = json.loads((REQ / "metadata-review.json").read_text(encoding="utf-8"))
    target = next(entry for entry in ledger["entries"] if entry["requirement_id"] == requirement_id)
    field = "applicable_actor"
    target["field_status"][field] = (
        "review-required" if target["field_status"][field] != "review-required" else "populated-reviewed"
    )
    with tempfile.TemporaryDirectory() as directory:
        conflict = Path(directory) / "metadata-review.json"
        conflict.write_text(json.dumps(ledger), encoding="utf-8")
        module.LEDGER = conflict
        try:
            module.seed(False)
        except ValueError as error:
            assert "manual reconciliation required" in str(error)
        else:
            raise AssertionError(f"{script_name} accepted a conflicting review decision")


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
    assert len(ids) == 400

    backlog_schema = json.loads((REQ / "reextraction-backlog.schema.json").read_text(encoding="utf-8"))
    backlog = json.loads((REQ / "reextraction-backlog.json").read_text(encoding="utf-8"))
    assert backlog_schema["properties"]["schema_version"]["const"] == "1.0"
    backlog_ids = [entry["current_requirement_id"] for entry in backlog["entries"]]
    assert len(backlog_ids) == len(set(backlog_ids)) == 61
    assert sum(entry["external_source_id"] == "NIST-AI-600-1" for entry in backlog["entries"]) == 60
    assert sum(entry["external_source_id"] == "CYCLONEDX-SPEC" for entry in backlog["entries"]) == 1

    validator = (SCRIPTS / "validate-external-requirement-metadata.py").read_text(encoding="utf-8")
    assert '"source_summary"' in validator
    assert '"field_observation"' in validator
    assert '"field_summary"' in validator
    assert '"blocked_sources"' in validator
    assert '"reextraction_defect_categories"' in validator
    assert "--write-report" in validator
    assert "--strict" in validator

    seeder = (SCRIPTS / "seed-eu-ai-act-metadata-review.py").read_text(encoding="utf-8")
    assert '"direct-primary-text"' in seeder
    assert '"not-specified-by-source"' in seeder
    assert "manual reconciliation required" in seeder
    assert "--write" in seeder

    reviewed_seeder = (SCRIPTS / "seed-reviewed-source-metadata.py").read_text(encoding="utf-8")
    assert "NIST_GAI_CONSTITUENT_BACKLOG" in reviewed_seeder
    assert "AI Actor Tasks (subcategory-level)" in reviewed_seeder
    assert "manual reconciliation required" in reviewed_seeder
    assert "--write" in reviewed_seeder

    assert_conflict_intolerant("seed-eu-ai-act-metadata-review.py", "EXTREQ-8406A6A9A7ECFCB6")
    assert_conflict_intolerant("seed-reviewed-source-metadata.py", "EXTREQ-0055BCF6AB20FDB7")

    print("External requirement metadata-review contract regression passed")


if __name__ == "__main__":
    main()
