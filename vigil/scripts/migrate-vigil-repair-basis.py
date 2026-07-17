#!/usr/bin/env python3
'''Migrate VIGIL failure repair-basis semantics without conflating corpus coverage.

This migration separates:
- corpus_coverage.classification: whether CAM already covers the failure; and
- repair_status.repair_basis: what establishes an actual CAM-side repair.

It is deterministic and idempotent. It updates failure records, schemas,
templates, validators, and preserved reconciliation scripts so deprecated
coverage terms cannot be reintroduced as repair provenance.
'''

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records" / "failures"
DATE = "2026-07-17"

REPAIR_BASES = [
    "not-yet-established",
    "pre-existing-coverage-identified",
    "patch-implemented",
    "cross-domain-repair-assembled",
    "not-actionable",
    "superseded",
]
DEPRECATED_BASES = {"uncovered", "partial-coverage", "no-confirmed-repair", "", None}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
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


def normalize_failure(record: dict[str, Any]) -> bool:
    repair = record.get("repair_status")
    if not isinstance(repair, dict):
        return False

    before = json.dumps(record, ensure_ascii=False, sort_keys=True)
    status = repair.get("status")
    repaired_by = repair.get("repaired_by")
    if not isinstance(repaired_by, list):
        repaired_by = []
        repair["repaired_by"] = repaired_by
    valid_patch_ids = [item for item in repaired_by if isinstance(item, str) and item.strip()]
    old_basis = repair.get("repair_basis")

    if status == "unrepaired":
        repair["repaired_by"] = []
        repair["date_repaired"] = ""
        repair["repair_basis"] = "not-yet-established"
        if repair.get("verification_status") not in {"unverified", "not-applicable"}:
            repair["verification_status"] = "unverified"

    elif status == "partially-repaired":
        if valid_patch_ids:
            if old_basis in DEPRECATED_BASES or old_basis == "not-yet-established":
                repair["repair_basis"] = "patch-implemented"
        else:
            repair["status"] = "unrepaired"
            repair["repaired_by"] = []
            repair["date_repaired"] = ""
            repair["verification_status"] = "unverified"
            repair["repair_basis"] = "not-yet-established"

    elif status == "repaired":
        if valid_patch_ids and (old_basis in DEPRECATED_BASES or old_basis == "not-yet-established"):
            repair["repair_basis"] = "patch-implemented"

    elif status == "not-actionable":
        repair["repair_basis"] = "not-actionable"

    elif status == "superseded":
        repair["repair_basis"] = "superseded"

    record_id = record.get("id")
    if record_id == "VIGIL-2026-FM-0034":
        repair.update(
            {
                "status": "unrepaired",
                "repaired_by": [],
                "date_repaired": "",
                "verification_status": "unverified",
                "repair_basis": "not-yet-established",
            }
        )
        triage = record.get("triage")
        if isinstance(triage, dict):
            triage["mitigation_status"] = (
                "Unresolved — no CAM patch or confirmed corpus coverage has been established. "
                "Potentially relevant instruments remain routed for future assessment only."
            )
        coverage = record.get("corpus_coverage")
        if isinstance(coverage, dict):
            coverage["classification"] = "no-confirmed-coverage"
            coverage["coverage_summary"] = (
                "No confirmed CAM repair or direct corpus coverage has been established for this newly recorded "
                "failure mode. Potentially relevant instruments remain listed only under cam_internal for future review."
            )
            coverage["covered_by"] = []

    if record_id == "VIGIL-2026-FM-0035":
        repair.update(
            {
                "status": "unrepaired",
                "repaired_by": [],
                "date_repaired": "",
                "verification_status": "unverified",
                "repair_basis": "not-yet-established",
            }
        )

    after = json.dumps(record, ensure_ascii=False, sort_keys=True)
    if after != before:
        bump_identity(record)
        return True
    return False


def migrate_records() -> int:
    changed = 0
    for path in sorted(RECORDS.rglob("*.json")):
        record = load(path)
        if normalize_failure(record):
            write_json(path, record)
            changed += 1
    return changed


def update_failure_schema() -> bool:
    path = VIGIL / "schemas" / "VIGIL.FailureMode.Schema.json"
    schema = load(path)
    before = json.dumps(schema, ensure_ascii=False, sort_keys=True)
    repair = schema["properties"]["repair_status"]
    repair["properties"]["repair_basis"] = {"enum": REPAIR_BASES}
    after = json.dumps(schema, ensure_ascii=False, sort_keys=True)
    if after != before:
        write_json(path, schema)
        return True
    return False


def update_schema_contract() -> bool:
    path = VIGIL / "VIGIL.Schema.json"
    schema = load(path)
    before = json.dumps(schema, ensure_ascii=False, sort_keys=True)
    schema["version"] = "2.7-no-confirmed-coverage"
    failure = schema["record_classes"]["failure_mode"]
    failure["allowed_repair_basis_values"] = REPAIR_BASES
    failure["repair_basis_interpretation"] = (
        "repair_status.repair_basis identifies what establishes an actual CAM-side repair. "
        "Corpus coverage states such as no-confirmed-coverage and partial-coverage belong only in "
        "corpus_coverage.classification."
    )
    lifecycle = schema.setdefault("lifecycle_rules", {})
    lifecycle["no_patch_no_repair_rule"] = (
        "A failure with no linked repairing PATCH remains unrepaired and uses repair_basis not-yet-established, "
        "even where corpus_coverage identifies adjacent or partial doctrine."
    )
    lifecycle["coverage_separation_rule"] = (
        "corpus_coverage.classification may be no-confirmed-coverage, partial-coverage, verification-pending, "
        "retrospective-coverage, implemented-repair, or not-applicable without being reused as repair provenance."
    )
    after = json.dumps(schema, ensure_ascii=False, sort_keys=True)
    if after != before:
        write_json(path, schema)
        return True
    return False


def update_template() -> bool:
    path = VIGIL / "templates" / "failure-mode-record-template.json"
    template = load(path)
    before = json.dumps(template, ensure_ascii=False, sort_keys=True)
    repair = template.setdefault("repair_status", {})
    repair["status"] = "unrepaired"
    repair["repaired_by"] = []
    repair["date_repaired"] = ""
    repair["verification_status"] = "unverified"
    repair["repair_basis"] = "not-yet-established"
    after = json.dumps(template, ensure_ascii=False, sort_keys=True)
    if after != before:
        write_json(path, template)
        return True
    return False


def replace_text(path: Path, old: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        return False
    path.write_text(text.replace(old, new), encoding="utf-8")
    return True


def update_validator_source() -> bool:
    path = VIGIL / "scripts" / "validate-vigil-lifecycle.py"
    changed = False
    changed |= replace_text(
        path,
        '''REPAIR_BASES = {
    "uncovered",
    "pre-existing-coverage-identified",
    "partial-coverage",
    "patch-implemented",
    "cross-domain-repair-assembled",
    "not-actionable",
    "superseded",
}''',
        '''REPAIR_BASES = {
    "not-yet-established",
    "pre-existing-coverage-identified",
    "patch-implemented",
    "cross-domain-repair-assembled",
    "not-actionable",
    "superseded",
}''',
    )
    changed |= replace_text(
        path,
        '''    if repair.get("status") == "repaired" and not repaired_by:
        errors.append(f"{path}: repaired CAM status requires at least one repairing patch")
''',
        '''    status = repair.get("status")
    if status == "unrepaired":
        if basis != "not-yet-established":
            errors.append(f"{path}: unrepaired CAM status requires repair_basis 'not-yet-established'")
        if repaired_by:
            errors.append(f"{path}: unrepaired CAM status cannot name a repairing patch")
        if non_empty_string(repair.get("date_repaired")):
            errors.append(f"{path}: unrepaired CAM status cannot have date_repaired")
    elif status in {"partially-repaired", "repaired"}:
        if not repaired_by:
            errors.append(f"{path}: {status} CAM status requires at least one repairing patch")
        if basis == "not-yet-established":
            errors.append(f"{path}: {status} CAM status cannot use repair_basis 'not-yet-established'")
    elif status == "not-actionable" and basis != "not-actionable":
        errors.append(f"{path}: not-actionable CAM status requires repair_basis 'not-actionable'")
    elif status == "superseded" and basis != "superseded":
        errors.append(f"{path}: superseded CAM status requires repair_basis 'superseded'")

    if basis in {
        "pre-existing-coverage-identified",
        "patch-implemented",
        "cross-domain-repair-assembled",
    } and not repaired_by:
        errors.append(f"{path}: repair_basis {basis!r} requires at least one linked repairing patch")
''',
    )
    return changed


def update_reconciliation_sources() -> int:
    changed = 0
    lifecycle = VIGIL / "scripts" / "reconcile-vigil-lifecycle.py"
    if replace_text(
        lifecycle,
        '''        elif status == "partially-repaired":
            repair.setdefault("repair_basis", "partial-coverage")
        elif status == "unrepaired":
            repair.setdefault("repair_basis", "partial-coverage" if record.get("existing_cam_coverage") else "uncovered")
''',
        '''        elif status == "partially-repaired":
            if repair.get("repaired_by"):
                repair["repair_basis"] = "patch-implemented"
            else:
                repair["status"] = "unrepaired"
                repair["repaired_by"] = []
                repair["date_repaired"] = ""
                repair["verification_status"] = "unverified"
                repair["repair_basis"] = "not-yet-established"
        elif status == "unrepaired":
            repair["repaired_by"] = []
            repair["date_repaired"] = ""
            repair["repair_basis"] = "not-yet-established"
''',
    ):
        changed += 1
    if replace_text(
        lifecycle,
        '''            "uncovered",
            "pre-existing-coverage-identified",
            "partial-coverage",
            "patch-implemented",''',
        '''            "not-yet-established",
            "pre-existing-coverage-identified",
            "patch-implemented",''',
    ):
        changed += 1
    if replace_text(
        lifecycle,
        '''        repair["repair_basis"] = "uncovered"''',
        '''        repair["repair_basis"] = "not-yet-established"''',
    ):
        changed += 1

    runner = VIGIL / "scripts" / "run-vigil-reconciliation.py"
    runner_text = runner.read_text(encoding="utf-8")
    revised = runner_text.replace('"status": "partially-repaired",', '"status": "unrepaired",', 1)
    revised = revised.replace('"repair_basis": "partial-coverage",', '"repair_basis": "not-yet-established",', 1)
    if revised != runner_text:
        runner.write_text(revised, encoding="utf-8")
        changed += 1

    provenance = VIGIL / "scripts" / "migrate-vigil-interpretive-provenance.py"
    provenance_text = provenance.read_text(encoding="utf-8")
    revised = provenance_text.replace('"status": "partially-repaired",', '"status": "unrepaired",', 1)
    revised = revised.replace('"repair_basis": "partial-coverage",', '"repair_basis": "not-yet-established",', 1)
    if revised != provenance_text:
        provenance.write_text(revised, encoding="utf-8")
        changed += 1
    return changed


def main() -> None:
    changed_records = migrate_records()
    changed_contracts = sum(
        (
            update_failure_schema(),
            update_schema_contract(),
            update_template(),
            update_validator_source(),
        )
    )
    changed_sources = update_reconciliation_sources()
    print(
        "VIGIL repair-basis migration completed: "
        f"{changed_records} failure record(s), "
        f"{changed_contracts} schema/validator/template contract(s), "
        f"{changed_sources} reconciliation source update(s)."
    )


if __name__ == "__main__":
    main()
