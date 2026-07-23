#!/usr/bin/env python3
"""Reconcile VIGIL maintainer-pipeline state and bounded validator hygiene.

Top-level record_state is the maintainer workflow state. It is separate from
failure repair_status, failure ecosystem_status, proposal resolution_status,
and corpus_coverage. This migration is deterministic and idempotent.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
DATE = "2026-07-17"
PATCH_ID = "VIGIL-2026-PATCH-0023"
CAELESTIS_COMMIT = "40113eea5428478ba0734b3980600bfcece425a0"

ALLOWED_RECORD_STATES = [
    "draft",
    "scaffolding",
    "active",
    "monitoring",
    "closed-actioned",
    "closed-no-action",
    "deferred",
    "superseded",
]

PROVENANCE_PURPOSE = (
    "Interpretive provenance identifies the AI analytical reviewer, human governance editor, "
    "capability profile, source modality, primary-artefact access, and review limitations."
)
PROVENANCE_SOURCE_RULES = [
    "Each source record must state evidence_modality.",
    "Each source record must state primary_artefact_access, including whether direct primary review occurred.",
    "A transcript, screenshot, summary, or human description must not be represented as equivalent to direct audiovisual or interaction review.",
]

OBSERVATION_STATE_OVERRIDES = {
    "VIGIL-2026-OBS-0004": "monitoring",
    "VIGIL-2026-OBS-0005": "monitoring",
    "VIGIL-2026-OBS-0006": "closed-actioned",
    "VIGIL-2026-OBS-0010": "monitoring",
    "VIGIL-2026-OBS-0011": "monitoring",
    "VIGIL-2026-OBS-0012": "monitoring",
    "VIGIL-2026-OBS-0013": "closed-actioned",
    "VIGIL-2026-OBS-0014": "monitoring",
}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def write(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def bump_identity(record: dict[str, Any]) -> None:
    identity = record.get("record_identity")
    if not isinstance(identity, dict):
        return
    identity["updated"] = DATE
    version = str(identity.get("version", "1.0"))
    try:
        major, minor = version.split(".", 1)
        identity["version"] = f"{major}.{int(minor) + 1}"
    except (TypeError, ValueError):
        identity["version"] = "1.1"


def canonical_state(record: dict[str, Any]) -> str:
    record_type = record.get("record_type")
    current = str(record.get("record_state", "active"))

    if current in {"draft", "scaffolding"}:
        return current

    if record_type in {"patch", "patch_note"}:
        return "closed-actioned" if record.get("date_implemented") else current

    if record_type == "proposal":
        resolution = record.get("resolution_status")
        status = resolution.get("status") if isinstance(resolution, dict) else None
        return {
            "resolved-by-patch": "closed-actioned",
            "closed-no-action": "closed-no-action",
            "deferred": "deferred",
            "superseded": "superseded",
            "open": "active",
            "routed": "active",
        }.get(status, current if current in ALLOWED_RECORD_STATES else "active")

    if record_type == "failure_mode":
        repair = record.get("repair_status")
        status = repair.get("status") if isinstance(repair, dict) else None
        return {
            "repaired": "monitoring",
            "partially-repaired": "active",
            "unrepaired": "active",
            "not-actionable": "closed-no-action",
            "superseded": "superseded",
        }.get(status, current if current in ALLOWED_RECORD_STATES else "active")

    if record_type == "observation":
        record_id = str(record.get("id", ""))
        if record_id in OBSERVATION_STATE_OVERRIDES:
            return OBSERVATION_STATE_OVERRIDES[record_id]
        if current == "watching":
            return "monitoring"
        return current if current in ALLOWED_RECORD_STATES else "active"

    return current if current in ALLOWED_RECORD_STATES else "active"


def clean_warning_records(record: dict[str, Any]) -> None:
    record_id = record.get("id")

    if record_id == "VIGIL-2026-FM-0008":
        classification = record.get("failure_classification")
        if isinstance(classification, dict):
            classification["failure_family"] = "governance"

    elif record_id == "VIGIL-2026-FM-0009":
        sources = record.get("source_records")
        if isinstance(sources, list) and sources and isinstance(sources[0], dict):
            source = sources[0]
            if not source.get("source_url") and source.get("archive_url"):
                source["source_url"] = source["archive_url"]
                source["archive_url"] = ""
        classification = record.get("failure_classification")
        if isinstance(classification, dict):
            classification["failure_family"] = "state-context"

    elif record_id == "VIGIL-2026-FM-0010":
        linked = record.get("linked_records")
        if isinstance(linked, dict):
            linked["related_failure_modes"] = [
                "VIGIL-2026-FM-0011",
                "VIGIL-2026-FM-0012",
                "VIGIL-2026-FM-0013",
                "VIGIL-2026-FM-0014",
                "VIGIL-2026-FM-0015",
            ]
            linked.pop("potential_child_records", None)
            linked.pop("potential_patch_records", None)

    elif record_id == "VIGIL-2026-FM-0018":
        classification = record.get("failure_classification")
        if isinstance(classification, dict):
            classification["related_failure_groups"] = [
                "governance",
                "state-context",
                "ux-representation",
                "infrastructure-continuity",
            ]

    elif record_id == "VIGIL-2026-FM-0021":
        classification = record.get("failure_classification")
        if isinstance(classification, dict):
            classification["related_failure_groups"] = [
                "state-context",
                "infrastructure-continuity",
                "classification",
                "security-integrity",
            ]

    elif record_id == "VIGIL-2026-FM-0034":
        classification = record.get("failure_classification")
        if isinstance(classification, dict):
            classification["related_failure_groups"] = [
                "epistemic",
                "arbitration",
                "security-integrity",
                "state-context",
                "infrastructure-continuity",
                "classification",
            ]


def close_mentis_proposal(record: dict[str, Any]) -> None:
    if record.get("id") != "VIGIL-2026-PROP-0001":
        return

    linked = record.setdefault("linked_records", {})
    patch_ids = linked.setdefault("related_patch_notes", [])
    if PATCH_ID not in patch_ids:
        patch_ids.append(PATCH_ID)

    cam = record.setdefault("cam_internal", {})
    cam["drafting_status"] = "accepted"
    cam["routing_note"] = (
        "The MENTIS domain has been established in Caelestis through "
        "CAM-EQ2026-MENTIS-001-PLATINUM and CAM-EQ2026-MENTIS-002-PLATINUM. "
        "Those instruments remain developmental Draft/Interpretive instruments; future MENTIS expansion "
        "should be tracked through new proposals rather than leaving this domain-creation proposal open."
    )

    record["next_action"] = (
        "No further action under this proposal. Treat future MENTIS instrument development, enforceability "
        "changes, or cross-domain expansion as separate proposals or patches."
    )
    record["resolution_status"] = {
        "status": "resolved-by-patch",
        "resolved_by": [PATCH_ID],
        "resolution_note": (
            "Resolved retrospectively: the MENTIS domain exists in current Caelestis through MENTIS-001 "
            "and MENTIS-002. Closure records domain establishment, not finalisation or enforceability of "
            "every planned MENTIS instrument."
        ),
    }
    record["coverage_reconciliation"] = {
        "status": "resolved-by-current-corpus",
        "assessed_date": DATE,
        "corpus_commit": CAELESTIS_COMMIT,
        "resolved_by": [PATCH_ID],
        "remaining_scope": [],
        "note": (
            "The proposal objective was establishment of the human cognitive integrity domain. Current "
            "Caelestis contains the source-authoritative MENTIS charter and an operational cognitive-inference "
            "and neurodata instrument."
        ),
    }


def reconcile_observation(record: dict[str, Any]) -> None:
    record_id = record.get("id")
    status = record.get("observation_status")
    if not isinstance(status, dict):
        status = {}
        record["observation_status"] = status

    if record_id == "VIGIL-2026-OBS-0006":
        status.update(
            {
                "current_status": "closed-actioned",
                "resolution_status": "routed to VIGIL-2026-FM-0021",
                "repair_linkage": (
                    "The observation was promoted into VIGIL-2026-FM-0021. Ongoing ecosystem monitoring "
                    "and any repair work belong on the failure record."
                ),
                "monitoring_note": "No further action is required at the observation level.",
            }
        )
        record["next_action"] = (
            "No further action at the observation level. Monitor access restoration, proportionality, "
            "technical-basis disclosure, and scoped sovereign controls through VIGIL-2026-FM-0021."
        )
        cam = record.get("cam_internal")
        if isinstance(cam, dict):
            cam["possible_future_failure_mode"] = "Actioned as VIGIL-2026-FM-0021"
            cam["possible_future_proposal"] = (
                "Retain only if FM-0021 review identifies a distinct unresolved CAM corpus gap."
            )
            notes = cam.get("routing_note")
            if isinstance(notes, list):
                closure_note = (
                    "The later governance pattern was promoted into VIGIL-2026-FM-0021; "
                    "this observation is closed as actioned."
                )
                notes = [
                    note
                    for note in notes
                    if "later failure-mode record may be warranted" not in note.lower()
                    and "later proposal may be warranted" not in note.lower()
                    and note != closure_note
                ]
                notes.append(closure_note)
                cam["routing_note"] = notes

    elif record_id == "VIGIL-2026-OBS-0013":
        status.update(
            {
                "current_status": "closed-actioned",
                "resolution_status": "routed to linked failure and proposal records",
                "repair_linkage": (
                    "The governance distinction is represented in VIGIL-2026-FM-0031, "
                    "VIGIL-2026-FM-0032, and VIGIL-2026-PROP-0013."
                ),
                "monitoring_note": (
                    "Residual source-video validation and cross-role testing belong in the linked records; "
                    "the originating observation requires no separate pipeline action."
                ),
            }
        )
        record["next_action"] = (
            "No further action at the observation level. Continue source validation, cross-role testing, "
            "and CAM design through VIGIL-2026-FM-0031, VIGIL-2026-FM-0032, and VIGIL-2026-PROP-0013."
        )

    elif canonical_state(record) == "monitoring" and status:
        status["current_status"] = "monitoring"


def normalize_record(path: Path) -> bool:
    record = load(path)
    before = json.dumps(record, ensure_ascii=False, sort_keys=True)

    clean_warning_records(record)
    close_mentis_proposal(record)
    record["record_state"] = canonical_state(record)

    if record.get("record_type") == "observation":
        reconcile_observation(record)

    after = json.dumps(record, ensure_ascii=False, sort_keys=True)
    if after != before:
        bump_identity(record)
        write(path, record)
        return True
    return False


def update_schema_contracts() -> int:
    changed = 0

    path = VIGIL / "VIGIL.Schema.json"
    schema = load(path)
    before = json.dumps(schema, ensure_ascii=False, sort_keys=True)

    purpose = str(schema.get("purpose", "")).replace(PROVENANCE_PURPOSE, " ")
    schema["purpose"] = (" ".join(purpose.split()) + " " + PROVENANCE_PURPOSE).strip()

    rules = schema.setdefault("source_evidence_rules", {}).setdefault("individual_records", [])
    deduped: list[str] = []
    for rule in rules:
        if isinstance(rule, str) and rule not in deduped:
            deduped.append(rule)
    for rule in PROVENANCE_SOURCE_RULES:
        if rule not in deduped:
            deduped.append(rule)
    schema["source_evidence_rules"]["individual_records"] = deduped

    schema["version"] = "2.8-pipeline-state-hygiene"
    schema["record_state_rules"] = {
        "purpose": (
            "Top-level record_state is the maintainer workflow and pipeline state. It must not be used as a "
            "proxy for external ecosystem conditions, CAM repair status, proposal resolution, or corpus coverage."
        ),
        "allowed_values": ALLOWED_RECORD_STATES,
        "semantics": {
            "draft": "Record is being authored and is not yet ready for triage.",
            "scaffolding": "Temporary incomplete record retained only for construction or migration.",
            "active": "A governance decision, evidence action, proposal, or CAM repair still requires attention.",
            "monitoring": (
                "The immediate VIGIL/CAM action is complete or bounded, but recurrence, implementation, "
                "or external conformity remains under observation."
            ),
            "closed-actioned": (
                "The record has been routed, implemented, or otherwise actioned and no longer belongs "
                "in the active work queue."
            ),
            "closed-no-action": "The evidence is retained but no further action is justified.",
            "deferred": "Action is intentionally postponed and should not appear as current active work.",
            "superseded": "A successor record now carries the active governance work.",
        },
        "class_rules": {
            "failure_mode": (
                "Unrepaired or partially-repaired failures are active; repaired failures are monitoring; "
                "not-actionable failures are closed-no-action; superseded failures are superseded."
            ),
            "proposal": (
                "Open or routed proposals are active; resolved-by-patch proposals are closed-actioned; "
                "closed-no-action, deferred, and superseded resolution states map directly."
            ),
            "patch": (
                "Implemented patch records are closed-actioned. Ecosystem monitoring remains on linked "
                "failure or observation records."
            ),
            "observation": (
                "Observations requiring evidence or routing work are active; routed or actioned observations "
                "close; unresolved recurrence or positive-control follow-up is monitoring."
            ),
        },
    }

    after = json.dumps(schema, ensure_ascii=False, sort_keys=True)
    if after != before:
        write(path, schema)
        changed += 1

    path = VIGIL / "schemas" / "VIGIL.Base.Schema.json"
    base = load(path)
    before = json.dumps(base, ensure_ascii=False, sort_keys=True)
    base.setdefault("properties", {})["record_state"] = {
        "type": "string",
        "enum": ALLOWED_RECORD_STATES,
        "description": (
            "VIGIL maintainer workflow state, separate from ecosystem_status, repair_status, "
            "resolution_status, and corpus_coverage."
        ),
    }
    after = json.dumps(base, ensure_ascii=False, sort_keys=True)
    if after != before:
        write(path, base)
        changed += 1

    return changed


def patch_provenance_migration() -> bool:
    path = VIGIL / "scripts" / "migrate-vigil-interpretive-provenance.py"
    text = path.read_text(encoding="utf-8")
    revised = text

    old_purpose = (
        '    schema["purpose"] = schema.get("purpose", "") + '
        '" Interpretive provenance identifies the AI analytical reviewer, human governance editor, capability profile, '
        'source modality, primary-artefact access, and review limitations."\n'
    )
    new_purpose = (
        f"    purpose_sentence = {PROVENANCE_PURPOSE!r}\n"
        '    purpose = str(schema.get("purpose", "")).replace(purpose_sentence, " ")\n'
        '    schema["purpose"] = (" ".join(purpose.split()) + " " + purpose_sentence).strip()\n'
    )
    if old_purpose in revised:
        revised = revised.replace(old_purpose, new_purpose, 1)

    old_rules = (
        '    schema["source_evidence_rules"]["individual_records"].extend([\n'
        '        "Each source record must state evidence_modality.",\n'
        '        "Each source record must state primary_artefact_access, including whether direct primary review occurred.",\n'
        '        "A transcript, screenshot, summary, or human description must not be represented as equivalent to direct audiovisual or interaction review.",\n'
        '    ])\n'
    )
    new_rules = (
        '    source_rules = schema["source_evidence_rules"]["individual_records"]\n'
        '    for rule in (\n'
        '        "Each source record must state evidence_modality.",\n'
        '        "Each source record must state primary_artefact_access, including whether direct primary review occurred.",\n'
        '        "A transcript, screenshot, summary, or human description must not be represented as equivalent to direct audiovisual or interaction review.",\n'
        '    ):\n'
        '        if rule not in source_rules:\n'
        '            source_rules.append(rule)\n'
    )
    if old_rules in revised:
        revised = revised.replace(old_rules, new_rules, 1)

    if revised != text:
        path.write_text(revised, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed_records = 0
    for folder in ("observations", "failures", "proposals", "patches"):
        for path in sorted((RECORDS / folder).rglob("*.json")):
            if normalize_record(path):
                changed_records += 1

    changed_contracts = update_schema_contracts()
    patched_legacy = patch_provenance_migration()
    print(
        "VIGIL pipeline-state hygiene completed: "
        f"changed_records={changed_records}; changed_contracts={changed_contracts}; "
        f"patched_legacy_migration={patched_legacy}."
    )


if __name__ == "__main__":
    main()
