#!/usr/bin/env python3
"""Validate individual VIGIL record JSON files.

This intentionally uses only the Python standard library so the VIGIL layer stays
small and inspectable.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL_DIR = ROOT / "vigil"
SCHEMA_PATH = VIGIL_DIR / "VIGIL.Schema.json"
RECORD_DIRS = [
    VIGIL_DIR / "records" / "open",
    VIGIL_DIR / "records" / "clusters",
    VIGIL_DIR / "records" / "closed",
]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_defs(schema: dict[str, Any]) -> dict[str, Any]:
    return schema.get("$defs", {})


def enum_values(defs: dict[str, Any], name: str) -> set[str]:
    return set(defs.get(name, {}).get("enum", []))


def required_fields(defs: dict[str, Any], name: str) -> set[str]:
    return set(defs.get(name, {}).get("required", []))


def record_files() -> list[Path]:
    files: list[Path] = []
    for directory in RECORD_DIRS:
        if directory.exists():
            files.extend(directory.glob("*.json"))
    return sorted(files, key=lambda path: path.as_posix())


def validate() -> int:
    errors: list[str] = []

    try:
        schema = load_json(SCHEMA_PATH)
    except Exception as exc:  # noqa: BLE001 - report concise validation error
        print(f"ERROR: unable to load schema {SCHEMA_PATH}: {exc}", file=sys.stderr)
        return 1

    defs = schema_defs(schema)
    record_required = required_fields(defs, "vigil_record")
    source_required = required_fields(defs, "source_record")
    record_type_enum = enum_values(defs, "record_type")
    status_enum = enum_values(defs, "status")
    evidence_enum = enum_values(defs, "evidence_confidence")
    source_type_enum = enum_values(defs, "source_type")

    records: dict[str, dict[str, Any]] = {}
    cluster_paths: list[Path] = []
    files = record_files()

    for path in files:
        try:
            record = load_json(path)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue
        except Exception as exc:  # noqa: BLE001 - report concise validation error
            errors.append(f"{path}: unable to read JSON: {exc}")
            continue

        if not isinstance(record, dict):
            errors.append(f"{path}: individual record file must contain one JSON object")
            continue

        record_id = record.get("id")
        if not record_id:
            errors.append(f"{path}: missing required id")
        elif path.stem != record_id:
            errors.append(f"{path}: filename stem does not match record id {record_id!r}")

        missing = sorted(field for field in record_required if field not in record)
        if missing:
            errors.append(f"{path}: missing required fields: {', '.join(missing)}")

        if record_id:
            if record_id in records:
                errors.append(f"{path}: duplicate id {record_id!r}")
            records[record_id] = record

        if record.get("record_type") not in record_type_enum:
            errors.append(f"{path}: invalid record_type {record.get('record_type')!r}")
        if record.get("status") not in status_enum:
            errors.append(f"{path}: invalid status {record.get('status')!r}")
        if record.get("evidence_confidence") not in evidence_enum:
            errors.append(
                f"{path}: invalid evidence_confidence {record.get('evidence_confidence')!r}"
            )

        source_records = record.get("source_records")
        if not isinstance(source_records, list):
            errors.append(f"{path}: source_records must be an array")
        else:
            for index, source in enumerate(source_records):
                if not isinstance(source, dict):
                    errors.append(f"{path}: source_records[{index}] must be an object")
                    continue
                source_missing = sorted(field for field in source_required if field not in source)
                if source_missing:
                    errors.append(
                        f"{path}: source_records[{index}] missing required fields: "
                        + ", ".join(source_missing)
                    )
                if source.get("source_type") not in source_type_enum:
                    errors.append(
                        f"{path}: source_records[{index}] invalid source_type "
                        f"{source.get('source_type')!r}"
                    )

        for array_field in (
            "possible_CAM_mapping",
            "affected_domains",
            "affected_instruments",
            "related_record_ids",
            "supersedes_record_ids",
        ):
            if array_field in record and not isinstance(record[array_field], list):
                errors.append(f"{path}: {array_field} must be an array when present")

        if record.get("record_type") == "cluster":
            cluster_paths.append(path)

    for path in cluster_paths:
        record = records.get(path.stem, {})
        related = record.get("related_record_ids", [])
        if not isinstance(related, list):
            continue
        for related_id in related:
            if related_id not in records:
                errors.append(f"{path}: related_record_ids references missing id {related_id!r}")

    if errors:
        print("VIGIL record validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"VIGIL record validation passed: {len(files)} files, "
        f"{len(records)} unique records, {len(cluster_paths)} clusters."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(validate())
