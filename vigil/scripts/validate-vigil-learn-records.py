#!/usr/bin/env python3
"""Validate VIGIL LEARN records against the learning-closure extension contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL_DIR = ROOT / "vigil"
RECORDS_ROOT = VIGIL_DIR / "records"
LEARN_ROOT = RECORDS_ROOT / "learn"
SCHEMA_PATH = VIGIL_DIR / "VIGIL.Learn.Schema.json"

LEARN_ID = re.compile(r"^VIGIL-\d{4}-LEARN-\d{4}$")
FM_ID = re.compile(r"^VIGIL-\d{4}-FM-\d{4}$")
PROP_ID = re.compile(r"^VIGIL-\d{4}-PROP-\d{4}$")
PATCH_ID = re.compile(r"^VIGIL-\d{4}-PATCH-\d{4}$")
ANY_RECORD_ID = re.compile(r"^VIGIL-\d{4}-(?:OBS|FM|PROP|PATCH|RESEARCH|LEARN)-\d{4}$")
FAMILY_CODE = re.compile(r"^OPS\.FF\.[A-Z0-9_]+$")

REQUIRED_SECTIONS = {
    "section_01_observation",
    "section_02_record",
    "section_03_classification",
    "section_04_diagnosis",
    "section_05_repair",
    "section_06_learn",
}
TAXONOMY_STATUSES = {
    "pre-existing-taxonomy-applied",
    "established-by-linked-patch",
    "refined-by-linked-patch",
    "crosswalk-added-by-linked-patch",
    "provisional-classification",
}
FORBIDDEN_AUTHORITY_FIELDS = {
    "failure_mode_definition",
    "failure_threshold",
    "failure_classification",
    "proposal_rationale",
    "proposal_scope",
    "corpus_implementation",
    "change_classification",
    "change_details",
    "implementation_verification",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_string_array(
    errors: list[str], path: Path, label: str, value: Any, *, allow_empty: bool = False
) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{path}: {label} must be an array")
        return []
    if not allow_empty and not value:
        errors.append(f"{path}: {label} must not be empty")
    if any(not is_non_empty_string(item) for item in value):
        errors.append(f"{path}: {label} must contain only non-empty strings")
        return []
    return value


def canonical_record_ids() -> set[str]:
    ids: set[str] = set()
    for path in RECORDS_ROOT.rglob("*.json"):
        try:
            record = load_json(path)
        except Exception:
            continue
        record_id = record.get("id") if isinstance(record, dict) else None
        if isinstance(record_id, str):
            ids.add(record_id)
    for path in (RECORDS_ROOT / "research").rglob("*.md") if (RECORDS_ROOT / "research").exists() else []:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        end = text.find("\n---\n", 4)
        if end == -1:
            continue
        try:
            metadata = json.loads(text[4:end])
        except Exception:
            continue
        if isinstance(metadata, dict) and isinstance(metadata.get("id"), str):
            ids.add(metadata["id"])
    return ids


def validate_taxonomy_links(
    errors: list[str], path: Path, record: dict[str, Any], known_ids: set[str]
) -> None:
    links = record.get("failure_taxonomy_links")
    if not isinstance(links, list) or not links:
        errors.append(f"{path}: failure_taxonomy_links must be a non-empty array")
        return

    learning_basis = record.get("learning_basis") if isinstance(record.get("learning_basis"), dict) else {}
    primary_failure = learning_basis.get("primary_failure_mode")
    patch_records = set(learning_basis.get("patch_records", [])) if isinstance(learning_basis.get("patch_records"), list) else set()

    for index, link in enumerate(links):
        label = f"failure_taxonomy_links[{index}]"
        if not isinstance(link, dict):
            errors.append(f"{path}: {label} must be an object")
            continue
        required = {
            "failure_record_id",
            "primary_failure_family_code",
            "canonical_failure_name",
            "taxonomy_reference",
            "relationship",
            "taxonomy_status",
            "establishing_patch_id",
        }
        missing = sorted(field for field in required if field not in link)
        if missing:
            errors.append(f"{path}: {label} missing required keys: {', '.join(missing)}")

        failure_id = link.get("failure_record_id")
        if not isinstance(failure_id, str) or not FM_ID.fullmatch(failure_id):
            errors.append(f"{path}: {label}.failure_record_id must be a VIGIL FM id")
        elif failure_id not in known_ids:
            errors.append(f"{path}: {label}.failure_record_id {failure_id!r} cannot be resolved")
        elif primary_failure and failure_id != primary_failure:
            errors.append(f"{path}: {label}.failure_record_id must match learning_basis.primary_failure_mode")

        family_code = link.get("primary_failure_family_code")
        if not isinstance(family_code, str) or not FAMILY_CODE.fullmatch(family_code):
            errors.append(f"{path}: {label}.primary_failure_family_code is malformed")
        for field in ("canonical_failure_name", "taxonomy_reference"):
            if not is_non_empty_string(link.get(field)):
                errors.append(f"{path}: {label}.{field} must be a non-empty string")
        if link.get("relationship") != "lesson-derived-from":
            errors.append(f"{path}: {label}.relationship must be 'lesson-derived-from'")

        status = link.get("taxonomy_status")
        if status not in TAXONOMY_STATUSES:
            errors.append(f"{path}: {label}.taxonomy_status is not canonical")
        establishing_patch = link.get("establishing_patch_id")
        if status == "pre-existing-taxonomy-applied":
            if establishing_patch is not None:
                errors.append(f"{path}: {label}.establishing_patch_id must be null for pre-existing taxonomy")
        else:
            if not isinstance(establishing_patch, str) or not PATCH_ID.fullmatch(establishing_patch):
                errors.append(f"{path}: {label}.establishing_patch_id must be a VIGIL PATCH id")
            elif establishing_patch not in known_ids:
                errors.append(f"{path}: {label}.establishing_patch_id {establishing_patch!r} cannot be resolved")
            elif establishing_patch not in patch_records:
                errors.append(f"{path}: {label}.establishing_patch_id must appear in learning_basis.patch_records")


def validate_report_sections(
    errors: list[str], path: Path, record: dict[str, Any], known_ids: set[str]
) -> None:
    sections = record.get("report_section_sources")
    if not isinstance(sections, dict):
        errors.append(f"{path}: report_section_sources must be an object")
        return
    missing = sorted(REQUIRED_SECTIONS - set(sections))
    if missing:
        errors.append(f"{path}: report_section_sources missing: {', '.join(missing)}")
    for section_name in REQUIRED_SECTIONS:
        section = sections.get(section_name)
        if not isinstance(section, dict):
            errors.append(f"{path}: report_section_sources.{section_name} must be an object")
            continue
        record_ids = validate_string_array(
            errors, path, f"report_section_sources.{section_name}.record_ids", section.get("record_ids")
        )
        validate_string_array(
            errors, path, f"report_section_sources.{section_name}.source_fields", section.get("source_fields")
        )
        if not is_non_empty_string(section.get("basis")):
            errors.append(f"{path}: report_section_sources.{section_name}.basis must be a non-empty string")
        for record_id in record_ids:
            if not ANY_RECORD_ID.fullmatch(record_id):
                errors.append(f"{path}: report_section_sources.{section_name} contains malformed id {record_id!r}")
            elif record_id not in known_ids:
                errors.append(f"{path}: report_section_sources.{section_name} id {record_id!r} cannot be resolved")

    completion = record.get("chain_completion")
    if not isinstance(completion, dict):
        errors.append(f"{path}: chain_completion must be an object")
        return
    for section_name in REQUIRED_SECTIONS:
        if completion.get(section_name) != "complete":
            errors.append(f"{path}: chain_completion.{section_name} must be 'complete'")
    if completion.get("overall_status") != "complete":
        errors.append(f"{path}: chain_completion.overall_status must be 'complete'")
    if not is_non_empty_string(completion.get("completion_basis")):
        errors.append(f"{path}: chain_completion.completion_basis must be a non-empty string")


def validate_linked_records(
    errors: list[str], path: Path, record: dict[str, Any], known_ids: set[str]
) -> None:
    linked = record.get("linked_records")
    if not isinstance(linked, dict):
        errors.append(f"{path}: linked_records must be an object")
        return
    expected = {
        "related_observations": (re.compile(r"^VIGIL-\d{4}-OBS-\d{4}$"), True),
        "related_failure_modes": (FM_ID, False),
        "related_proposals": (PROP_ID, False),
        "related_patch_notes": (PATCH_ID, False),
        "related_learn_records": (LEARN_ID, True),
        "research": (re.compile(r"^VIGIL-\d{4}-RESEARCH-\d{4}$"), True),
        "standards": (None, True),
    }
    for field, (pattern, allow_empty) in expected.items():
        values = validate_string_array(errors, path, f"linked_records.{field}", linked.get(field), allow_empty=allow_empty)
        if pattern is None:
            continue
        for value in values:
            if not pattern.fullmatch(value):
                errors.append(f"{path}: linked_records.{field} contains malformed id {value!r}")
            elif value not in known_ids:
                errors.append(f"{path}: linked_records.{field} id {value!r} cannot be resolved")

    basis = record.get("learning_basis")
    if isinstance(basis, dict):
        if linked.get("related_failure_modes") != [basis.get("primary_failure_mode")]:
            errors.append(f"{path}: linked_records.related_failure_modes must match the primary learning basis")
        if linked.get("related_proposals") != basis.get("proposal_records"):
            errors.append(f"{path}: linked_records.related_proposals must match learning_basis.proposal_records")
        if linked.get("related_patch_notes") != basis.get("patch_records"):
            errors.append(f"{path}: linked_records.related_patch_notes must match learning_basis.patch_records")


def validate_record(path: Path, record: dict[str, Any], schema: dict[str, Any], known_ids: set[str]) -> list[str]:
    errors: list[str] = []
    required = schema.get("required", [])
    for field in required:
        if field not in record or record[field] in (None, "", [], {}):
            errors.append(f"{path}: missing required field {field}")

    record_id = record.get("id")
    if not isinstance(record_id, str) or not LEARN_ID.fullmatch(record_id):
        errors.append(f"{path}: id must use VIGIL-YYYY-LEARN-NNNN")
    elif path.stem != record_id:
        errors.append(f"{path}: filename stem does not match id")
    if record.get("record_type") != "learn":
        errors.append(f"{path}: record_type must be 'learn'")

    identity = record.get("record_identity")
    if not isinstance(identity, dict):
        errors.append(f"{path}: record_identity must be an object")
    else:
        if identity.get("record_id") != record_id:
            errors.append(f"{path}: record_identity.record_id does not match id")
        if identity.get("record_type") != "learn":
            errors.append(f"{path}: record_identity.record_type must be 'learn'")
        if identity.get("title") != record.get("report_title"):
            errors.append(f"{path}: record_identity.title must equal report_title")

    for field in ("report_title", "case_descriptor", "summary", "abstracted_learning", "generalisation_boundary"):
        if not is_non_empty_string(record.get(field)):
            errors.append(f"{path}: {field} must be a non-empty string")
    what_happened = record.get("what_happened")
    if what_happened is not None:
        statements = validate_string_array(errors, path, "what_happened", what_happened)
        if len(statements) != 3:
            errors.append(f"{path}: what_happened must contain exactly three factual statements")
    validate_string_array(errors, path, "must_not_be_forgotten", record.get("must_not_be_forgotten"))
    validate_string_array(errors, path, "future_application", record.get("future_application"))

    forbidden = sorted(field for field in FORBIDDEN_AUTHORITY_FIELDS if field in record)
    if forbidden:
        errors.append(
            f"{path}: LEARN contains authority-bearing fields reserved for FM, PROP, or PATCH: {', '.join(forbidden)}"
        )
    if record.get("source_records") not in (None, []):
        errors.append(f"{path}: LEARN must not duplicate incident evidence in source_records; link the chain instead")

    basis = record.get("learning_basis")
    if not isinstance(basis, dict):
        errors.append(f"{path}: learning_basis must be an object")
    else:
        primary = basis.get("primary_failure_mode")
        if not isinstance(primary, str) or not FM_ID.fullmatch(primary) or primary not in known_ids:
            errors.append(f"{path}: learning_basis.primary_failure_mode must resolve to a VIGIL FM")
        proposals = validate_string_array(errors, path, "learning_basis.proposal_records", basis.get("proposal_records"))
        patches = validate_string_array(errors, path, "learning_basis.patch_records", basis.get("patch_records"))
        for value, pattern, label in (
            *((value, PROP_ID, "proposal") for value in proposals),
            *((value, PATCH_ID, "patch") for value in patches),
        ):
            if not pattern.fullmatch(value) or value not in known_ids:
                errors.append(f"{path}: learning_basis contains unresolved or malformed {label} id {value!r}")
        if not is_non_empty_string(basis.get("basis_statement")):
            errors.append(f"{path}: learning_basis.basis_statement must be a non-empty string")

    validate_taxonomy_links(errors, path, record, known_ids)
    validate_report_sections(errors, path, record, known_ids)
    validate_linked_records(errors, path, record, known_ids)

    if record.get("knowledge_status") not in {"current", "under-review", "superseded"}:
        errors.append(f"{path}: knowledge_status is not canonical")
    if record.get("publication_status") not in {"draft", "published", "withdrawn"}:
        errors.append(f"{path}: publication_status is not canonical")
    if record.get("publication_status") == "published":
        if what_happened is None:
            errors.append(f"{path}: published LEARN records require what_happened")
        if record.get("chain_completion", {}).get("overall_status") != "complete":
            errors.append(f"{path}: published LEARN records require a complete chain")

    return errors


def main() -> int:
    errors: list[str] = []
    try:
        schema = load_json(SCHEMA_PATH)
    except Exception as exc:  # noqa: BLE001
        print(f"Unable to load LEARN schema: {exc}", file=sys.stderr)
        return 1
    if not isinstance(schema, dict):
        print("VIGIL.Learn.Schema.json must contain one JSON object", file=sys.stderr)
        return 1

    known_ids = canonical_record_ids()
    files = sorted(LEARN_ROOT.rglob("*.json"), key=lambda item: item.as_posix()) if LEARN_ROOT.exists() else []
    if not files:
        errors.append(f"{LEARN_ROOT}: no LEARN records found")

    for path in files:
        try:
            record = load_json(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path}: unable to read JSON: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"{path}: LEARN record must contain one JSON object")
            continue
        errors.extend(validate_record(path, record, schema, known_ids))

    if errors:
        print("VIGIL LEARN validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"VIGIL LEARN validation passed: {len(files)} record(s), {len(known_ids)} resolvable VIGIL ids.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
