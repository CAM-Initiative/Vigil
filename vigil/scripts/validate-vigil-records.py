#!/usr/bin/env python3
"""Validate individual VIGIL record JSON files for the clean record design."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL_DIR = ROOT / "vigil"
RECORDS_ROOT = VIGIL_DIR / "records"
SCHEMA_PATH = VIGIL_DIR / "VIGIL.Schema.json"
DEPRECATED_OUTPUT_PATHS = [
    VIGIL_DIR / "VIGIL.ActiveRecords.json",
    VIGIL_DIR / "VIGIL.ClosedRecords.json",
    VIGIL_DIR / "VIGIL.Records.Index.json",
    VIGIL_DIR / "VIGIL.Records.json",
]
RECORD_TYPE_DIRS = [
    RECORDS_ROOT / "observations",
    RECORDS_ROOT / "failures",
    RECORDS_ROOT / "proposals",
    RECORDS_ROOT / "patches",
]

RECORD_TYPES = {"observation", "failure_mode", "proposal", "patch", "patch_note"}
CAM_INSTRUMENT_PREFIXES = ("CAM-BS", "CAM-EQ")
FALLBACK_ALLOWED_CANONICAL_FAILURE_GROUPS = {
    # Fallback only. The primary VIGIL taxonomy source is
    # VIGIL.Schema.json / cam_failure_taxonomy.allowed_canonical_failure_group_values,
    # derived from CAM-EQ2026-OPERATIONS-003-SUP-01 Appendix B.
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
SYSTEM_CONTEXT_REQUIRED = {
    "product_family",
    "product_or_service",
    "specific_model",
    "interface_surface",
}
ID_PREFIX = {
    "observation": "OBS",
    "failure_mode": "FM",
    "proposal": "PROP",
    "patch": "PATCH",
    "patch_note": "PATCH",
}
TYPE_DIR = {
    "observation": "observations",
    "failure_mode": "failures",
    "proposal": "proposals",
    "patch": "patches",
    "patch_note": "patches",
}
REQUIRED_COMMON = {
    "id",
    "record_type",
    "record_state",
    "date_recorded",
    "record_identity",
    "summary",
    "evidence_confidence",
    "source_records",
    "system_context",
    "jurisdictional_context",
    "linked_records",
    "cam_internal",
}
OBS_FORBIDDEN = {
    "failure_classification",
    "triage",
    "proposal_scope",
    "change_classification",
    "date_implemented",
    "proposal_rationale",
    "implementation_notes",
    "external_relevance",
    "change_details",
    "implementation_verification",
    "impact_summary",
    "remaining_work",
    "failure_mode_definition",
    "failure_threshold",
}
FM_REQUIRED = {"failure_mode_definition", "failure_threshold", "failure_classification", "triage"}
PROP_REQUIRED = {"proposal_rationale", "proposal_type", "proposal_scope", "implementation_notes", "external_relevance", "next_action"}
PATCH_REQUIRED = {
    "date_implemented",
    "change_classification",
    "change_details",
    "implementation_verification",
    "impact_summary",
    "remaining_work",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def record_files(root: Path | None = None) -> list[Path]:
    if root is not None:
        if root.is_file():
            return [root]
        return sorted(root.rglob("*.json"), key=lambda path: path.as_posix())
    files: list[Path] = []
    for directory in RECORD_TYPE_DIRS:
        if directory.exists():
            files.extend(directory.rglob("*.json"))
    return sorted(files, key=lambda path: path.as_posix())


def is_blank(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}



def contains_key(value: Any, key: str) -> bool:
    if isinstance(value, dict):
        return key in value or any(contains_key(item, key) for item in value.values())
    if isinstance(value, list):
        return any(contains_key(item, key) for item in value)
    return False

def add_missing(errors: list[str], path: Path, record: dict[str, Any], fields: set[str]) -> None:
    missing = sorted(field for field in fields if is_blank(record.get(field)))
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(missing)}")




def load_allowed_canonical_failure_groups(schema_path: Path = SCHEMA_PATH) -> set[str]:
    """Load canonical failure groups from the VIGIL schema-derived CAM taxonomy registry."""
    try:
        schema = load_json(schema_path)
        values = schema.get("cam_failure_taxonomy", {}).get("allowed_canonical_failure_group_values", [])
        loaded = {value for value in values if isinstance(value, str) and value}
        return loaded or set(FALLBACK_ALLOWED_CANONICAL_FAILURE_GROUPS)
    except Exception:  # noqa: BLE001 - validator must retain a labelled offline fallback
        return set(FALLBACK_ALLOWED_CANONICAL_FAILURE_GROUPS)


def source_urls(record: dict[str, Any]) -> set[str]:
    urls: set[str] = set()
    for source in record.get("source_records", []):
        if isinstance(source, dict):
            for key in ("source_url", "archive_url"):
                if source.get(key):
                    urls.add(source[key])
    return urls




def standards_reference_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        for key in ("standard_id", "id", "title"):
            text = value.get(key)
            if isinstance(text, str) and text:
                return text
    return ""


def is_cam_instrument_reference(value: Any) -> bool:
    return standards_reference_text(value).startswith(CAM_INSTRUMENT_PREFIXES)


def validate_canonical_path(path: Path, record_id: Any, record_type: Any, errors: list[str]) -> None:
    """Validate canonical repository paths while allowing standalone fixture files."""
    try:
        relative = path.resolve().relative_to(RECORDS_ROOT.resolve())
    except ValueError:
        return
    if not isinstance(record_id, str) or record_type not in TYPE_DIR:
        return
    parts = record_id.split("-")
    if len(parts) < 4:
        return
    expected = Path(TYPE_DIR[record_type]) / parts[1] / f"{record_id}.json"
    if relative != expected:
        errors.append(f"{path}: record path must be vigil/records/{expected.as_posix()} for id/type")


def validate_record(
    path: Path,
    record: dict[str, Any],
    known_ids: set[str],
    errors: list[str],
    warnings: list[str],
    allowed_canonical_failure_groups: set[str],
) -> None:
    record_id = record.get("id")
    record_type = record.get("record_type")

    common_required = set(REQUIRED_COMMON)
    # Temporary patch scaffolds may intentionally carry an empty source_records array;
    # source_records still must be present and typed as an array below.
    if record_type in {"patch", "patch_note"} and str(record.get("record_state", "")).lower() == "scaffolding":
        common_required.discard("source_records")
    add_missing(errors, path, record, common_required)

    if contains_key(record, "source_data"):
        errors.append(f"{path}: source_data is forbidden anywhere in individual records; use source_records only")
        if isinstance(record.get("source_data"), dict) and "sources" in record["source_data"]:
            errors.append(f"{path}: source_data.sources is forbidden in individual records; use source_records only")

    if not record_id:
        errors.append(f"{path}: missing required id")
    elif path.stem != record_id:
        errors.append(f"{path}: filename stem does not match id {record_id!r}")
    validate_canonical_path(path, record_id, record_type, errors)

    if record_type not in RECORD_TYPES:
        errors.append(f"{path}: invalid record_type {record_type!r}")
    elif record_id:
        expected = f"VIGIL-"
        prefix = ID_PREFIX[record_type]
        parts = str(record_id).split("-")
        if len(parts) < 3 or not str(record_id).startswith(expected) or parts[2] != prefix:
            errors.append(f"{path}: ID prefix must be {prefix!r} for record_type {record_type!r}")

    identity = record.get("record_identity")
    if not isinstance(identity, dict):
        errors.append(f"{path}: record_identity must be an object")
    else:
        if identity.get("record_id") != record_id:
            errors.append(f"{path}: record_identity.record_id does not match id")
        if identity.get("record_type") != record_type:
            errors.append(f"{path}: record_identity.record_type does not match record_type")
        if "status" in identity:
            errors.append(f"{path}: record_identity.status is deprecated; use top-level record_state only")

    sources = record.get("source_records")
    if not isinstance(sources, list):
        errors.append(f"{path}: source_records must be an array")
    else:
        for index, source in enumerate(sources):
            if not isinstance(source, dict):
                errors.append(f"{path}: source_records[{index}] must be an object")
                continue
            legacy_keys = sorted({key for key in ("title", "url", "platform") if key in source})
            if legacy_keys:
                mapping = {"title": "source_title", "url": "source_url", "platform": "source_platform"}
                replacements = ", ".join(f"{key}->{mapping[key]}" for key in legacy_keys)
                errors.append(f"{path}: source_records[{index}] uses legacy source key(s): {replacements}")
            if not source.get("source_url") and source.get("archive_url"):
                warnings.append(f"{path}: source_records[{index}] source_url is blank but archive_url is present")

    linked = record.get("linked_records")
    if not isinstance(linked, dict):
        errors.append(f"{path}: linked_records must be an object")
    else:
        primary_urls = source_urls(record)
        for index, ref in enumerate(linked.get("external_references", [])):
            if isinstance(ref, dict) and (ref.get("url") in primary_urls or ref.get("source_url") in primary_urls):
                errors.append(f"{path}: linked_records.external_references[{index}] duplicates a primary source_records URL")
        for field in ("related_observations", "related_failure_modes", "related_proposals", "related_patch_notes"):
            value = linked.get(field, [])
            if not isinstance(value, list):
                errors.append(f"{path}: linked_records.{field} must be an array")
                continue
            for linked_id in value:
                if isinstance(linked_id, str) and linked_id and linked_id not in known_ids:
                    warnings.append(f"{path}: linked record id {linked_id!r} in {field} cannot be resolved; it may be a future record")
        standards = linked.get("standards", [])
        if isinstance(standards, list):
            for index, standard in enumerate(standards):
                if is_cam_instrument_reference(standard):
                    errors.append(
                        f"{path}: linked_records.standards[{index}] contains a CAM instrument ID; "
                        "CAM instrument IDs belong in cam_internal routing fields, not linked_records.standards."
                    )
        if record_type == "proposal" and record.get("external_standards_required") is True and not linked.get("standards"):
            warnings.append(f"{path}: external standards are marked required but absent from proposal linked_records.standards")

    system_context = record.get("system_context")
    if not isinstance(system_context, dict):
        errors.append(f"{path}: system_context must be an object")
    else:
        add_missing(errors, path, system_context, SYSTEM_CONTEXT_REQUIRED)

    jurisdiction = record.get("jurisdictional_context")
    if isinstance(jurisdiction, dict):
        if str(jurisdiction.get("primary_jurisdiction", "")).lower() in {"unknown", "to be assessed"}:
            warnings.append(f"{path}: jurisdictional_context.primary_jurisdiction uses unknown/to be assessed")
    cam = record.get("cam_internal")
    if isinstance(cam, dict):
        # Empty CAM routing arrays are schema-valid optional routing fields. Do not warn
        # merely because an optional affected/target/changed route has no current value.
        pass

    if record_type == "observation":
        present = sorted(field for field in OBS_FORBIDDEN if field in record)
        if present:
            errors.append(f"{path}: OBS contains forbidden record-class fields: {', '.join(present)}")
        if contains_key(record, "patch_status"):
            errors.append(f"{path}: OBS contains forbidden patch_status; patch state belongs in PATCH records")
    elif record_type == "failure_mode":
        add_missing(errors, path, record, FM_REQUIRED)
        classification = record.get("failure_classification")
        if isinstance(classification, dict):
            if is_blank(classification.get("failure_family")):
                errors.append(f"{path}: FM failure_classification.failure_family is required")
            canonical_group = classification.get("canonical_failure_group")
            if is_blank(canonical_group):
                errors.append(f"{path}: FM failure_classification.canonical_failure_group is required")
            elif canonical_group not in allowed_canonical_failure_groups:
                allowed = ", ".join(sorted(allowed_canonical_failure_groups))
                errors.append(
                    f"{path}: FM failure_classification.canonical_failure_group {canonical_group!r} "
                    f"is not in allowed CAM taxonomy groups: {allowed}"
                )
            failure_family = classification.get("failure_family")
            if (
                isinstance(failure_family, str)
                and failure_family
                and canonical_group in allowed_canonical_failure_groups
                and failure_family not in allowed_canonical_failure_groups
            ):
                warnings.append(
                    f"{path}: FM failure_classification.failure_family {failure_family!r} is not a canonical "
                    "group; treating it as a local family/subtype routed through canonical_failure_group"
                )
            related_groups = classification.get("related_failure_groups")
            if isinstance(related_groups, list):
                for related_group in related_groups:
                    if isinstance(related_group, str) and related_group and related_group not in allowed_canonical_failure_groups:
                        warnings.append(
                            f"{path}: FM failure_classification.related_failure_groups contains "
                            f"non-canonical value {related_group!r}; move local concepts to harm_vectors, "
                            "routing_note, or subtype fields"
                        )
            add_missing(
                errors,
                path,
                classification,
                {"taxonomy_reference", "related_failure_groups", "persistence", "reproducibility", "visibility"},
            )
    elif record_type == "proposal":
        add_missing(errors, path, record, PROP_REQUIRED)
        state = str(record.get("record_state", "")).lower()
        if contains_key(record, "patch_status"):
            errors.append(f"{path}: PROP contains forbidden patch_status; implemented work belongs in PATCH records")
        if is_blank(record.get("proposal_scope")):
            errors.append(f"{path}: PROP proposal_scope must not be empty")
        if state in {"implemented", "completed", "closed-actioned"}:
            errors.append(f"{path}: PROP claims implementation as completed patch")
    elif record_type in {"patch", "patch_note"}:
        add_missing(errors, path, record, PATCH_REQUIRED)
        if is_blank(record.get("date_implemented")):
            errors.append(f"{path}: PATCH date_implemented is required")
        if is_blank(record.get("change_details")) or is_blank(record.get("implementation_verification")):
            errors.append(f"{path}: PATCH changed/implementation fields are required")
        verification = record.get("implementation_verification")
        evidence = verification.get("evidence") if isinstance(verification, dict) else ""
        if not record.get("source_records") and not evidence:
            errors.append(f"{path}: PATCH lacks implemented-change evidence")


def validate(root: Path | None = None) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if root is None:
        for deprecated_path in DEPRECATED_OUTPUT_PATHS:
            if deprecated_path.exists():
                errors.append(f"{deprecated_path}: deprecated generated file must not exist")

    allowed_canonical_failure_groups = load_allowed_canonical_failure_groups()

    files = record_files(root)
    records_by_path: dict[Path, dict[str, Any]] = {}
    ids: set[str] = set()
    for path in files:
        try:
            record = load_json(path)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path}: unable to read JSON: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"{path}: individual record file must contain one JSON object")
            continue
        if "records" in record or "generated_notice" in record:
            errors.append(f"{path}: individual record file must not contain a generated aggregate wrapper")
        records_by_path[path] = record
        if isinstance(record.get("id"), str):
            if record["id"] in ids:
                errors.append(f"{path}: duplicate id {record['id']!r}")
            ids.add(record["id"])

    for path, record in records_by_path.items():
        validate_record(path, record, ids, errors, warnings, allowed_canonical_failure_groups)

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)

    if errors:
        print("VIGIL record validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"VIGIL record validation passed: {len(records_by_path)} files, {len(ids)} unique records.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", help="Optional record or fixture directory to validate.")
    args = parser.parse_args()
    return validate(Path(args.path) if args.path else None)


if __name__ == "__main__":
    raise SystemExit(main())
