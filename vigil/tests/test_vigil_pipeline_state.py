#!/usr/bin/env python3
"""Focused regression checks for VIGIL pipeline-state hygiene."""

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
    "vigil/provenance/AUTHORSHIP-PROVENANCE.json."
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

    master = load(VIGIL / "VIGIL.Registry.Index.json")
    assert set(master.get("registries", {})) == {"failure_modes", "observations", "research"}
    counts = master.get("record_count", {})
    assert set(counts) == {"failure_modes", "observations", "research", "total"}
    assert not any(
        isinstance(item, dict)
        and item.get("record_type") in {"proposal", "patch", "patch_note", "learn"}
        for item in master.get("records", [])
    ), "withdrawn record classes must not appear in the public master registry"

    for folder in ("observations", "failures"):
        for path in sorted((RECORDS / folder).rglob("*.json")):
            item = load(path)
            state = item.get("record_state")
            assert state in ALLOWED, f"{path}: non-canonical record_state {state!r}"

            record_type = item.get("record_type")
            if record_type == "failure_mode" and state not in {"draft", "scaffolding"}:
                repair = item.get("repair_status", {})
                status = repair.get("status") if isinstance(repair, dict) else None
                expected = {
                    "repaired": "monitoring",
                    "partially-repaired": "active",
                    "unrepaired": "active",
                    "not-actionable": "closed-no-action",
                    "superseded": "superseded",
                }.get(status)
                if expected is not None:
                    assert state == expected, f"{path}: {status} failure must be {expected}"

    fm9 = record("VIGIL-2026-FM-0009", "failures")
    assert fm9["source_records"][0]["source_url"]
    assert not fm9["source_records"][0]["archive_url"]

    retired_taxonomy_fields = {
        "failure_family", "failure_subtype", "canonical_failure_group", "taxonomy_reference",
        "related_failure_groups", "allowed_canonical_failure_group_values", "classification_status",
    }
    for path in sorted((RECORDS / "failures").rglob("*.json")):
        item = load(path)
        classification = item["failure_classification"]
        assert not retired_taxonomy_fields.intersection(classification), path
        assert "related_failure_modes" not in item["linked_records"], path
        assert item["taxonomy_classification"]["classification_status"] in {
            "classified", "family-only", "candidate-new-class", "unmapped", "deferred"
        }, path

    obs6 = record("VIGIL-2026-OBS-0006", "observations")
    assert obs6["record_state"] == "closed-actioned"
    closure_note = (
        "The later governance pattern was promoted into VIGIL-2026-FM-0021; "
        "this observation is closed as actioned."
    )
    assert obs6["cam_internal"]["routing_note"].count(closure_note) == 1
    assert record("VIGIL-2026-OBS-0013", "observations")["record_state"] == "closed-actioned"
    assert record("VIGIL-2026-OBS-0007", "observations")["record_state"] == "active"

    fm44 = record("VIGIL-2026-FM-0044", "failures")
    assert fm44["record_state"] == "monitoring"
    assert fm44["repair_status"]["status"] == "repaired"
    assert fm44["corpus_coverage"]["classification"] == "implemented-repair"
    assert fm44["ecosystem_status"]["status"] == "active"
    assert fm44["repair_status"]["remaining_gaps"]

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
    ):
        assert forbidden not in workflow, f"workflow must not publish or broadly stage withdrawn material: {forbidden}"
    assert "route-vigil-records.py --check" in workflow
    assert "build-vigil-public-records.py" in workflow
    assert "Build and enrich public VIGIL registry indexes" in workflow

    print("VIGIL pipeline-state hygiene tests passed.")


if __name__ == "__main__":
    main()
