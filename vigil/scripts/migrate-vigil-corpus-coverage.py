#!/usr/bin/env python3
"""Replace the ambiguous corpus-coverage value ``uncovered``.

``no-confirmed-coverage`` means that a corpus assessment was performed but no
sufficient direct current-corpus control was confirmed. It is distinct from
``verification-pending``, which means the assessment is incomplete.

The migration is deterministic and idempotent. It updates canonical failure
records, schema contracts, templates, validators, guidance, preserved migration
sources, and the retrospective patch note that used the old wording.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
FAILURES = VIGIL / "records" / "failures"
PATCHES = VIGIL / "records" / "patches"
DATE = "2026-07-17"
OLD = "uncovered"
NEW = "no-confirmed-coverage"


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


def replace_list_value(values: Any) -> bool:
    if not isinstance(values, list):
        return False
    changed = False
    for index, value in enumerate(values):
        if value == OLD:
            values[index] = NEW
            changed = True
    return changed


def migrate_failure_records() -> int:
    changed = 0
    for path in sorted(FAILURES.rglob("*.json")):
        record = load(path)
        coverage = record.get("corpus_coverage")
        if not isinstance(coverage, dict) or coverage.get("classification") != OLD:
            continue
        coverage["classification"] = NEW
        bump_identity(record)
        write_json(path, record)
        changed += 1
    return changed


def update_patch_wording() -> bool:
    path = PATCHES / "2026" / "VIGIL-2026-PATCH-0017.json"
    if not path.exists():
        return False
    record = load(path)
    before = json.dumps(record, ensure_ascii=False, sort_keys=True)
    replacements = {
        "rather than leaving the failure falsely marked uncovered.":
            "rather than leaving the failure falsely classified as having no confirmed coverage.",
    }
    for field in ("why_it_matters_to_CAM",):
        value = record.get(field)
        if isinstance(value, str):
            for old, new in replacements.items():
                value = value.replace(old, new)
            record[field] = value
    impact = record.get("impact_summary")
    if isinstance(impact, dict) and isinstance(impact.get("intended_effect"), str):
        value = impact["intended_effect"]
        for old, new in replacements.items():
            value = value.replace(old, new)
        impact["intended_effect"] = value
    after = json.dumps(record, ensure_ascii=False, sort_keys=True)
    if after == before:
        return False
    bump_identity(record)
    write_json(path, record)
    return True


def update_schema_contract() -> bool:
    path = VIGIL / "VIGIL.Schema.json"
    schema = load(path)
    before = json.dumps(schema, ensure_ascii=False, sort_keys=True)
    schema["version"] = "2.7-no-confirmed-coverage"
    failure = schema["record_classes"]["failure_mode"]
    replace_list_value(failure.get("allowed_corpus_coverage_values"))
    failure["corpus_coverage_interpretation"] = (
        "no-confirmed-coverage means a corpus assessment was performed and no sufficient direct "
        "current-corpus control was confirmed. verification-pending means the assessment remains "
        "incomplete. A missing corpus_coverage block is invalid rather than equivalent to either state."
    )
    interpretation = failure.get("repair_basis_interpretation")
    if isinstance(interpretation, str):
        failure["repair_basis_interpretation"] = interpretation.replace(
            "Corpus coverage terms such as uncovered and partial-coverage",
            "Corpus coverage states such as no-confirmed-coverage and partial-coverage",
        )
    lifecycle = schema.setdefault("lifecycle_rules", {})
    lifecycle["coverage_separation_rule"] = (
        "corpus_coverage.classification may be no-confirmed-coverage, partial-coverage, "
        "verification-pending, retrospective-coverage, implemented-repair, or not-applicable "
        "without being reused as repair provenance."
    )
    after = json.dumps(schema, ensure_ascii=False, sort_keys=True)
    if after == before:
        return False
    write_json(path, schema)
    return True


def update_failure_schema() -> bool:
    path = VIGIL / "schemas" / "VIGIL.FailureMode.Schema.json"
    schema = load(path)
    before = json.dumps(schema, ensure_ascii=False, sort_keys=True)
    values = schema["properties"]["corpus_coverage"]["properties"]["classification"]["enum"]
    replace_list_value(values)
    after = json.dumps(schema, ensure_ascii=False, sort_keys=True)
    if after == before:
        return False
    write_json(path, schema)
    return True


def update_template() -> bool:
    path = VIGIL / "templates" / "failure-mode-record-template.json"
    template = load(path)
    before = json.dumps(template, ensure_ascii=False, sort_keys=True)
    coverage = template.get("corpus_coverage")
    if isinstance(coverage, dict) and isinstance(coverage.get("classification"), str):
        coverage["classification"] = coverage["classification"].replace(OLD, NEW)
    after = json.dumps(template, ensure_ascii=False, sort_keys=True)
    if after == before:
        return False
    write_json(path, template)
    return True


def replace_text(path: Path, replacements: list[tuple[str, str]]) -> bool:
    text = path.read_text(encoding="utf-8")
    revised = text
    for old, new in replacements:
        revised = revised.replace(old, new)
    if revised == text:
        return False
    path.write_text(revised, encoding="utf-8")
    return True


def update_validator() -> bool:
    return replace_text(
        VIGIL / "scripts" / "validate-vigil-lifecycle.py",
        [
            ('    "uncovered",\n    "verification-pending",',
             '    "no-confirmed-coverage",\n    "verification-pending",'),
            ('{"partial-coverage", "uncovered", "verification-pending"}',
             '{"partial-coverage", "no-confirmed-coverage", "verification-pending"}'),
        ],
    )


def update_preserved_sources() -> int:
    changed = 0
    files_and_replacements = {
        VIGIL / "scripts" / "migrate-vigil-repair-basis.py": [
            ('coverage["classification"] = "uncovered"',
             'coverage["classification"] = "no-confirmed-coverage"'),
            ("Corpus coverage terms such as uncovered and partial-coverage",
             "Corpus coverage states such as no-confirmed-coverage and partial-coverage"),
            ("corpus_coverage.classification may be uncovered, partial-coverage, verification-pending,",
             "corpus_coverage.classification may be no-confirmed-coverage, partial-coverage, verification-pending,"),
        ],
        VIGIL / "scripts" / "reconcile-vigil-lifecycle.py": [
            ('"uncovered"', '"no-confirmed-coverage"'),
        ],
        VIGIL / "AGENTS.md": [
            ("* `uncovered` means no sufficient direct current-corpus control was identified.",
             "* `no-confirmed-coverage` means a corpus assessment was performed and no sufficient direct current-corpus control was confirmed; it is distinct from `verification-pending`."),
        ],
    }
    for path, replacements in files_and_replacements.items():
        if replace_text(path, replacements):
            changed += 1
    return changed


def main() -> None:
    changed_records = migrate_failure_records()
    changed_patch = int(update_patch_wording())
    changed_contracts = sum(
        (
            update_schema_contract(),
            update_failure_schema(),
            update_template(),
            update_validator(),
        )
    )
    changed_sources = update_preserved_sources()
    print(
        "VIGIL corpus-coverage vocabulary migration completed: "
        f"{changed_records} failure record(s), {changed_patch} patch record(s), "
        f"{changed_contracts} schema/validator/template contract(s), "
        f"{changed_sources} guidance or preserved source file(s)."
    )


if __name__ == "__main__":
    main()
