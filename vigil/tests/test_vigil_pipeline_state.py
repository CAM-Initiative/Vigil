#!/usr/bin/env python3
"""Focused regression checks for VIGIL active pipeline-state hygiene."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
DRAFTS = VIGIL / "drafts"
WORKFLOW = ROOT / ".github" / "workflows" / "vigil-records.yml"

ALLOWED = {
    "draft",
    "scaffolding",
    "active",
    "monitoring",
    "closed-actioned",
    "closed-no-action",
    "deferred",
    "superseded",
}

PROVENANCE_PURPOSE = (
    "Interpretive provenance identifies AI source analysis, capability profile, source modality, "
    "primary-artefact access, review limitations, and historical authority context. Authorship, "
    "human-review, and human-verification status are governed separately by "
    "vigil/scripts/validate-authorship-provenance.py."
)


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), path
    return value


def record(record_id: str, folder: str) -> dict[str, Any]:
    return load(RECORDS / folder / "2026" / f"{record_id}.json")


def main() -> None:
    for withdrawn in ("proposals", "patches", "learn"):
        assert not (RECORDS / withdrawn).exists(), f"{withdrawn} must not be in the public record tree"
        assert (DRAFTS / withdrawn).exists(), f"{withdrawn} draft archive is missing"

    # Failure Modes remain preserved as legacy migration inputs only. They must not
    # appear in the active public registry surface or generated-index workflow.
    assert not (VIGIL / "VIGIL.Failures.Index.json").exists(), "retired Failure Mode index must not exist"
    master = load(VIGIL / "VIGIL.Registry.Index.json")
    assert set(master.get("registries", {})) == {"incidents", "observations", "research"}
    counts = master.get("record_count", {})
    assert set(counts) == {"incidents", "observations", "research", "total"}
    assert not any(
        isinstance(item, dict)
        and item.get("record_type") in {"failure_mode", "proposal", "patch", "patch_note", "learn"}
        for item in master.get("records", [])
    ), "legacy/withdrawn record classes must not appear in the active public master registry"

    for folder in ("incidents", "observations"):
        for path in sorted((RECORDS / folder).rglob("*.json")):
            item = load(path)
            state = item.get("record_state")
            assert state in ALLOWED, f"{path}: non-canonical record_state {state!r}"

    incident = load(RECORDS / "incidents" / "VIGIL-INC-000002.json")
    assert incident["taxonomy_classification"]["classification_status"] == "unclassified"
    assert incident["taxonomy_classification"]["primary_classification"] is None

    obs6 = record("VIGIL-2026-OBS-0006", "observations")
    assert obs6["record_state"] == "closed-actioned"
    assert record("VIGIL-2026-OBS-0013", "observations")["record_state"] == "closed-actioned"
    assert record("VIGIL-2026-OBS-0007", "observations")["record_state"] == "active"

    schema = load(VIGIL / "VIGIL.Schema.json")
    assert str(schema.get("purpose", "")).count(PROVENANCE_PURPOSE) == 1
    source_rules = schema["source_evidence_rules"]["individual_records"]
    assert len(source_rules) == len(dict.fromkeys(source_rules))
    assert set(schema["record_state_rules"]["allowed_values"]) == ALLOWED

    workflow = WORKFLOW.read_text(encoding="utf-8")
    for forbidden in (
        "migrate-vigil-",
        "reconcile-vigil-",
        "run-vigil-reconciliation.py",
        "git add vigil\n",
        "build-vigil-learn-records.py",
        "vigil/VIGIL.Proposals.Index.json",
        "vigil/VIGIL.PatchNotes.Index.json",
        "vigil/VIGIL.Learn.Index.json",
        "vigil/VIGIL.Failures.Index.json",
        "reconcile-fm-system-context",
        "validate-failure-mode-facets.py",
        "test_failure_mode_facets.py",
        "test_fm0047_repaired_monitoring_state.py",
    ):
        assert forbidden not in workflow, f"workflow must not run retired/withdrawn machinery: {forbidden}"
    assert "route-vigil-records.py --check" in workflow
    assert "build-vigil-public-records.py" in workflow
    assert "Build and enrich active public VIGIL registry indexes" in workflow

    print("VIGIL active pipeline-state hygiene tests passed.")


if __name__ == "__main__":
    main()
