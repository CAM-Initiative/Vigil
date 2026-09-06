#!/usr/bin/env python3
"""Regression checks for the Incident-only VIGIL runtime boundary."""


import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
WORKFLOW = ROOT / ".github" / "workflows" / "vigil-records.yml"
RETIRED = {"failures", "observations", "research", "proposals", "patches", "learn"}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    self_records = {path.name for path in RECORDS.iterdir() if path.is_dir()}
    assert self_records == {"incidents"}, self_records
    incident_count = len(list((RECORDS / "incidents").glob("VIGIL-INC-*.json")))
    assert incident_count > 0

    schema = load(VIGIL / "VIGIL.Schema.json")
    assert set(schema["record_classes"]) == {"incident"}
    assert schema["$defs"]["record_type"]["enum"] == ["incident"]
    assert "triage_model_rules" not in schema
    assert "patch_trace_rules" not in schema
    assert "runtime_conformance_rules" not in schema

    master = load(VIGIL / "VIGIL.Registry.Index.json")
    assert master["registry_count"] == 1
    assert set(master["registries"]) == {"incidents"}
    assert master["record_count"] == {"incidents": incident_count, "total": incident_count}
    assert all(item["record_type"] == "incident" for item in master["records"])

    workflow = WORKFLOW.read_text(encoding="utf-8")
    required = {
        "build-vigil-public-records.py", "validate-vigil-records.py",
        "validate-vigil-public-records.py", "validate-vigil-source-provenance.py",
    }
    assert all(value in workflow for value in required)
    forbidden = {
        "build-vigil-records.py", "enrich-vigil-indexes.py", "route-vigil-records.py",
        "build-incident-migration", "validate-incident-migration.py", "VIGIL.Observations.Index.json",
        "VIGIL.Research.Index.json", "VIGIL.Failures.Index.json", "run-vigil-lifecycle-validation.py",
    }
    assert all(value not in workflow for value in forbidden)

    for name in RETIRED:
        assert not (RECORDS / name).exists()
    assert not (VIGIL / "migrations" / "incident-registry").exists()
    print("VIGIL Incident-only pipeline-state tests passed.")


if __name__ == "__main__":
    main()
