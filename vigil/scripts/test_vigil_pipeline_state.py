#!/usr/bin/env python3
"""Focused regression checks for VIGIL pipeline-state hygiene."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"

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
    "Interpretive provenance identifies the AI analytical reviewer, human governance editor, "
    "capability profile, source modality, primary-artefact access, and review limitations."
)


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), path
    return value


def record(record_id: str, folder: str) -> dict[str, Any]:
    return load(RECORDS / folder / "2026" / f"{record_id}.json")


def main() -> None:
    for folder in ("observations", "failures", "proposals", "patches"):
        for path in sorted((RECORDS / folder).rglob("*.json")):
            item = load(path)
            state = item.get("record_state")
            assert state in ALLOWED, f"{path}: non-canonical record_state {state!r}"

            record_type = item.get("record_type")
            if record_type in {"patch", "patch_note"} and item.get("date_implemented"):
                assert state == "closed-actioned", f"{path}: implemented patch must be closed-actioned"

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

            if record_type == "proposal" and state not in {"draft", "scaffolding"}:
                resolution = item.get("resolution_status", {})
                status = resolution.get("status") if isinstance(resolution, dict) else None
                expected = {
                    "resolved-by-patch": "closed-actioned",
                    "closed-no-action": "closed-no-action",
                    "deferred": "deferred",
                    "superseded": "superseded",
                    "open": "active",
                    "routed": "active",
                }.get(status)
                if expected is not None:
                    assert state == expected, f"{path}: {status} proposal must be {expected}"

    prop = record("VIGIL-2026-PROP-0001", "proposals")
    assert prop["record_state"] == "closed-actioned"
    assert prop["resolution_status"]["status"] == "resolved-by-patch"
    assert "VIGIL-2026-PATCH-0023" in prop["resolution_status"]["resolved_by"]
    assert (RECORDS / "patches" / "2026" / "VIGIL-2026-PATCH-0023.json").exists()

    fm8 = record("VIGIL-2026-FM-0008", "failures")
    assert fm8["failure_classification"]["failure_family"] == "governance"

    fm9 = record("VIGIL-2026-FM-0009", "failures")
    assert fm9["failure_classification"]["failure_family"] == "state-context"
    assert fm9["source_records"][0]["source_url"]
    assert not fm9["source_records"][0]["archive_url"]

    fm10 = record("VIGIL-2026-FM-0010", "failures")
    assert fm10["linked_records"]["related_failure_modes"] == [
        "VIGIL-2026-FM-0011",
        "VIGIL-2026-FM-0012",
        "VIGIL-2026-FM-0013",
        "VIGIL-2026-FM-0014",
        "VIGIL-2026-FM-0015",
    ]

    canonical_groups = {
        "execution",
        "arbitration",
        "epistemic",
        "relational",
        "security-integrity",
        "state-context",
        "ux-representation",
        "governance",
        "infrastructure-continuity",
        "classification",
        "economic-legitimacy",
        "provisional",
    }
    for record_id in ("VIGIL-2026-FM-0018", "VIGIL-2026-FM-0021", "VIGIL-2026-FM-0034"):
        item = record(record_id, "failures")
        groups = item["failure_classification"]["related_failure_groups"]
        assert set(groups) <= canonical_groups, f"{record_id}: non-canonical related group remains"

    obs6 = record("VIGIL-2026-OBS-0006", "observations")
    assert obs6["record_state"] == "closed-actioned"
    closure_note = (
        "The later governance pattern was promoted into VIGIL-2026-FM-0021; "
        "this observation is closed as actioned."
    )
    assert obs6["cam_internal"]["routing_note"].count(closure_note) == 1
    assert record("VIGIL-2026-OBS-0013", "observations")["record_state"] == "closed-actioned"
    assert record("VIGIL-2026-OBS-0007", "observations")["record_state"] == "active"

    schema = load(VIGIL / "VIGIL.Schema.json")
    assert str(schema.get("purpose", "")).count(PROVENANCE_PURPOSE) == 1
    source_rules = schema["source_evidence_rules"]["individual_records"]
    assert len(source_rules) == len(dict.fromkeys(source_rules))
    assert set(schema["record_state_rules"]["allowed_values"]) == ALLOWED

    print("VIGIL pipeline-state hygiene tests passed.")


if __name__ == "__main__":
    main()
