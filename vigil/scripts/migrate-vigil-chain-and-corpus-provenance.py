#!/usr/bin/env python3
"""Repair OBS-0021 chain routing and add PATCH corpus release provenance.

This migration is deterministic and conservative. It records exact Git provenance
where available and does not infer that a published archive release existed at
implementation time.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PATCH_DIR = ROOT / "records" / "patches" / "2026"
OBS_PATH = ROOT / "records" / "observations" / "2026" / "VIGIL-2026-OBS-0021.json"
TEMPLATE_PATH = ROOT / "templates" / "patch-note-record-template.json"
SCHEMA_PATH = ROOT / "VIGIL.Schema.json"
MIGRATION_PATH = ROOT / "migrations" / "patch-corpus-release-provenance-2026-07-29.json"

COMMIT_RE = re.compile(r"\b[0-9a-f]{40}\b", re.I)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def collect_commits(value: Any) -> list[str]:
    commits: list[str] = []
    if isinstance(value, str):
        commits.extend(match.lower() for match in COMMIT_RE.findall(value))
    elif isinstance(value, list):
        for item in value:
            commits.extend(collect_commits(item))
    elif isinstance(value, dict):
        for item in value.values():
            commits.extend(collect_commits(item))
    return commits


def primary_commit(record: dict[str, Any]) -> str | None:
    implementation = record.get("corpus_implementation")
    commits = collect_commits(implementation)
    if not commits:
        commits = collect_commits(record.get("decision_trace"))
    if not commits:
        return None
    return Counter(commits).most_common(1)[0][0]


def provenance_for(record: dict[str, Any]) -> dict[str, Any]:
    implementation = record.get("corpus_implementation") or {}
    reconstruction = record.get("record_reconstruction") or {}
    canonical_state = str(implementation.get("canonical_state") or "unverified")
    commit = primary_commit(record)
    implementation_date = record.get("date_implemented") or record.get("date_recorded")
    reconstructed = reconstruction.get("reconstructed") is True

    if canonical_state == "canonical-main":
        implementation_ref = "main"
        canonical_ref = "main"
        canonical_commit = commit
    elif canonical_state == "historical-canonical":
        implementation_ref = "historical canonical ref recorded in implementation trace"
        canonical_ref = "historical-canonical"
        canonical_commit = commit
    elif canonical_state == "branch-only":
        implementation_ref = "working branch recorded in implementation trace"
        canonical_ref = None
        canonical_commit = None
    else:
        implementation_ref = "unverified or not recoverable from surviving trace"
        canonical_ref = None
        canonical_commit = None

    limitations = []
    if not commit:
        limitations.append("No unique 40-character Caelestis commit could be recovered automatically from the surviving PATCH trace.")
    limitations.append(
        "The current Caelestis v1.1.0 public archive is not treated as the historical implementation version unless release inclusion is separately verified."
    )

    return {
        "corpus_name": "Caelestis Architecture Model",
        "repository": "CAM-Initiative/Caelestis",
        "provenance_mode": "retrospective-reconstruction" if reconstructed else "contemporaneous-vigil-trace",
        "implementation_corpus_state": {
            "implementation_date": implementation_date,
            "repository_ref": implementation_ref,
            "commit": commit,
            "canonical_state_at_recording": canonical_state,
        },
        "canonical_corpus_state": {
            "repository_ref": canonical_ref,
            "commit": canonical_commit,
        },
        "published_release_at_implementation": {
            "status": "not-established-from-current-record",
            "version": None,
            "citation": None,
            "doi": None,
        },
        "current_public_archive_reference": {
            "version": "1.1.0",
            "citation": "O'Rourke, M. (2026). Caelestis Architecture Model — Public Archive (Version 1.1.0) [Computer software]. Zenodo.",
            "doi": "10.5281/zenodo.20686316",
            "relationship": "current-public-archive-reference; release inclusion for this PATCH is not asserted without separate verification",
        },
        "limitations": limitations,
    }


def repair_observation() -> None:
    record = load(OBS_PATH)
    linked = record["linked_records"]
    linked["related_failure_modes"] = ["VIGIL-2026-FM-0017"]
    linked["related_patch_notes"] = ["VIGIL-2026-PATCH-0019"]
    linked["contextual_relations"] = [
        {
            "record_id": "VIGIL-2026-FM-0007",
            "relationship": "parallel-reliability-workstream",
            "chain_inclusion": False,
            "rationale": "The observation contains reliability evidence, but FM-0007 is a separate monitoring workstream and is not repaired through the refusal pathway carried by this report.",
        },
        {
            "record_id": "VIGIL-2026-PATCH-0003",
            "relationship": "parallel-reliability-repair-context",
            "chain_inclusion": False,
            "rationale": "PATCH-0003 is relevant background to the reliability workstream but is not part of OBS-0021's authoritative refusal evidence-to-repair pathway.",
        },
        {
            "record_id": "VIGIL-2026-FM-0008",
            "relationship": "parallel-access-state-workstream",
            "chain_inclusion": False,
            "rationale": "The observation contains access-state evidence, but FM-0008 remains a distinct workstream rather than a failure repaired through PATCH-0019.",
        },
        {
            "record_id": "VIGIL-2026-PATCH-0005",
            "relationship": "parallel-access-state-repair-context",
            "chain_inclusion": False,
            "rationale": "PATCH-0005 is relevant access-state repair context and must not expand the authoritative refusal chain.",
        },
        {
            "record_id": "VIGIL-2026-FM-0028",
            "relationship": "parallel-entitlement-opacity-workstream",
            "chain_inclusion": False,
            "rationale": "Entitlement opacity is monitored separately from the scalar refusal mechanism identified as the primary failure pathway for OBS-0021.",
        },
        {
            "record_id": "VIGIL-2026-PATCH-0015",
            "relationship": "parallel-entitlement-repair-context",
            "chain_inclusion": False,
            "rationale": "PATCH-0015 is relevant entitlement repair context but is not an authoritative repair link for the refusal pathway.",
        },
    ]
    record["record_identity"]["updated"] = "2026-07-29"
    record["record_identity"]["version"] = "1.1"
    save(OBS_PATH, record)


def migrate_patches() -> list[str]:
    changed: list[str] = []
    for path in sorted(PATCH_DIR.glob("VIGIL-*-PATCH-*.json")):
        record = load(path)
        new_value = provenance_for(record)
        if record.get("corpus_release_provenance") != new_value:
            record["corpus_release_provenance"] = new_value
            save(path, record)
            changed.append(str(path.relative_to(ROOT)))
    return changed


def update_template() -> None:
    template = load(TEMPLATE_PATH)
    template["corpus_release_provenance"] = {
        "corpus_name": "Caelestis Architecture Model",
        "repository": "CAM-Initiative/Caelestis",
        "provenance_mode": "contemporaneous-vigil-trace | retrospective-reconstruction",
        "implementation_corpus_state": {
            "implementation_date": "YYYY-MM-DD",
            "repository_ref": "main | named working branch | historical canonical ref | unverified",
            "commit": "40-character commit SHA or null",
            "canonical_state_at_recording": "canonical-main | historical-canonical | branch-only | unverified",
        },
        "canonical_corpus_state": {
            "repository_ref": "main | historical-canonical | null",
            "commit": "40-character canonical commit SHA or null",
        },
        "published_release_at_implementation": {
            "status": "verified | not-established-from-current-record | not-applicable",
            "version": None,
            "citation": None,
            "doi": None,
        },
        "current_public_archive_reference": {
            "version": "1.1.0",
            "citation": "O'Rourke, M. (2026). Caelestis Architecture Model — Public Archive (Version 1.1.0) [Computer software]. Zenodo.",
            "doi": "10.5281/zenodo.20686316",
            "relationship": "current-public-archive-reference; do not imply historical release inclusion without verification",
        },
        "limitations": [],
    }
    save(TEMPLATE_PATH, template)


def update_schema() -> None:
    schema = load(SCHEMA_PATH)
    patch_rules = schema.setdefault("patch_trace_rules", [])
    rule = (
        "Every PATCH must preserve corpus_release_provenance distinguishing the exact implementation corpus state, later canonical state, and published archive release. A current archive citation must not be represented as the historical implementation version without verified release inclusion."
    )
    if rule not in patch_rules:
        patch_rules.append(rule)
    save(SCHEMA_PATH, schema)


def main() -> None:
    repair_observation()
    changed = migrate_patches()
    update_template()
    update_schema()
    save(MIGRATION_PATH, {
        "migration": "authoritative-chain-and-patch-corpus-release-provenance",
        "migration_date": "2026-07-29",
        "observation_repaired": "VIGIL-2026-OBS-0021",
        "authoritative_failure_mode": "VIGIL-2026-FM-0017",
        "authoritative_patch": "VIGIL-2026-PATCH-0019",
        "contextual_records_excluded_from_chain": [
            "VIGIL-2026-FM-0007", "VIGIL-2026-PATCH-0003",
            "VIGIL-2026-FM-0008", "VIGIL-2026-PATCH-0005",
            "VIGIL-2026-FM-0028", "VIGIL-2026-PATCH-0015",
        ],
        "patch_records_migrated": len(changed),
        "patch_paths": changed,
        "archive_policy": "Version 1.1.0 is recorded as the current public archive reference only. Historical implementation-release inclusion remains unasserted unless separately verified.",
    })
    print(f"Repaired OBS-0021 and migrated {len(changed)} PATCH record(s).")


if __name__ == "__main__":
    main()
