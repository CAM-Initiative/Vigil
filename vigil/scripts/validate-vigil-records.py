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
LEGACY_OUTPUT_PATH = VIGIL_DIR / "VIGIL.Records.json"
OPEN_DIR = RECORDS_ROOT / "open"
CLUSTERS_DIR = RECORDS_ROOT / "clusters"
CLOSED_DIR = RECORDS_ROOT / "closed"
RECORD_DIRS = [OPEN_DIR, CLUSTERS_DIR, CLOSED_DIR]

RECORD_TYPES = {"observation", "failure_mode", "proposal", "patch"}
ID_PREFIX = {
    "observation": "OBS",
    "failure_mode": "FM",
    "proposal": "PROP",
    "patch": "PATCH",
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
PROP_REQUIRED = {"proposal_rationale", "proposal_scope", "implementation_notes", "external_relevance", "next_action"}
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
    for directory in RECORD_DIRS:
        if directory.exists():
            files.extend(directory.glob("*.json"))
    return sorted(files, key=lambda path: path.as_posix())


def is_blank(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def add_missing(errors: list[str], path: Path, record: dict[str, Any], fields: set[str]) -> None:
    missing = sorted(field for field in fields if is_blank(record.get(field)))
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(missing)}")


def source_urls(record: dict[str, Any]) -> set[str]:
    urls: set[str] = set()
    for source in record.get("source_records", []):
        if isinstance(source, dict):
            for key in ("source_url", "archive_url", "url"):
                if source.get(key):
                    urls.add(source[key])
    return urls


def validate_record(path: Path, record: dict[str, Any], known_ids: set[str], errors: list[str], warnings: list[str]) -> None:
    record_id = record.get("id")
    record_type = record.get("record_type")

    add_missing(errors, path, record, REQUIRED_COMMON)

    if "source_data" in record:
        errors.append(f"{path}: source_data is forbidden in individual records; use source_records only")
        if isinstance(record.get("source_data"), dict) and "sources" in record["source_data"]:
            errors.append(f"{path}: source_data.sources is forbidden in individual records; use source_records only")

    if not record_id:
        errors.append(f"{path}: missing required id")
    elif path.stem != record_id:
        errors.append(f"{path}: filename stem does not match id {record_id!r}")

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

    sources = record.get("source_records")
    if not isinstance(sources, list):
        errors.append(f"{path}: source_records must be an array")
    else:
        for index, source in enumerate(sources):
            if not isinstance(source, dict):
                errors.append(f"{path}: source_records[{index}] must be an object")
                continue
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
        if record_type == "proposal" and not linked.get("standards"):
            warnings.append(f"{path}: external standards are absent from proposal linked_records.standards")

    jurisdiction = record.get("jurisdictional_context")
    if isinstance(jurisdiction, dict):
        if str(jurisdiction.get("primary_jurisdiction", "")).lower() in {"unknown", "to be assessed"}:
            warnings.append(f"{path}: jurisdictional_context.primary_jurisdiction uses unknown/to be assessed")
    cam = record.get("cam_internal")
    if isinstance(cam, dict):
        for key, value in cam.items():
            if isinstance(value, list) and not value:
                warnings.append(f"{path}: cam_internal.{key} array is empty")

    if record_type == "observation":
        present = sorted(field for field in OBS_FORBIDDEN if field in record)
        if present:
            errors.append(f"{path}: OBS contains forbidden record-class fields: {', '.join(present)}")
    elif record_type == "failure_mode":
        add_missing(errors, path, record, FM_REQUIRED)
    elif record_type == "proposal":
        add_missing(errors, path, record, PROP_REQUIRED)
        state = str(record.get("record_state", "")).lower()
        patch_status = str(record.get("patch_status", "")).lower()
        if state in {"implemented", "completed", "closed-actioned"} or "implemented" in patch_status or "completed" in patch_status:
            errors.append(f"{path}: PROP claims implementation as completed patch")
    elif record_type == "patch":
        add_missing(errors, path, record, PATCH_REQUIRED)
        verification = record.get("implementation_verification")
        evidence = verification.get("evidence") if isinstance(verification, dict) else ""
        if not record.get("source_records") and not evidence:
            errors.append(f"{path}: PATCH lacks implemented-change evidence")


def validate(root: Path | None = None) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if root is None and LEGACY_OUTPUT_PATH.exists():
        errors.append(f"{LEGACY_OUTPUT_PATH}: deprecated legacy aggregate must not exist")

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
        validate_record(path, record, ids, errors, warnings)

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
