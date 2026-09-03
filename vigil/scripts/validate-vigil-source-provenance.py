#!/usr/bin/env python3
"""Validate source residence and role metadata across active public VIGIL records."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from source_provenance import origin_markers, text

SCRIPT_PATH = Path(__file__).resolve()
VIGIL_ROOT = SCRIPT_PATH.parents[1]
RECORDS_ROOT = VIGIL_ROOT / "records"
ACTIVE_RECORD_ROOTS = (RECORDS_ROOT / "incidents",)
SCHEMA_PATH = VIGIL_ROOT / "VIGIL.Schema.json"


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    defs = schema.get("$defs", {})
    allowed_residences = set(defs.get("source_residence", {}).get("enum", []))
    allowed_roles = set(defs.get("source_role", {}).get("enum", []))
    required = set(defs.get("source_record", {}).get("required", []))

    errors: list[str] = []
    if not allowed_residences:
        errors.append("VIGIL.Schema.json does not define $defs.source_residence.enum")
    if not allowed_roles:
        errors.append("VIGIL.Schema.json does not define $defs.source_role.enum")
    for field in ("source_residence", "source_role"):
        if field not in required:
            errors.append(f"VIGIL.Schema.json source_record.required is missing {field}")

    source_count = 0
    paths = [path for root in ACTIVE_RECORD_ROOTS for path in root.rglob("*.json")]
    for path in sorted(paths):
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: cannot parse JSON: {exc}")
            continue
        sources = record.get("source_records")
        if not isinstance(sources, list):
            continue
        for index, source in enumerate(sources):
            source_count += 1
            location = f"{path.relative_to(VIGIL_ROOT)}: source_records[{index}]"
            if not isinstance(source, dict):
                errors.append(f"{location} must be an object")
                continue
            residence = text(source.get("source_residence"))
            role = text(source.get("source_role"))

            if residence not in allowed_residences:
                errors.append(f"{location} invalid source_residence {residence!r}")
            if role not in allowed_roles:
                errors.append(f"{location} invalid source_role {role!r}")
            if residence == "unknown" or role == "unknown":
                errors.append(f"{location} unresolved source provenance is not permitted in canonical records")

            looks_vigil, looks_cam = origin_markers(source)
            source_url = text(source.get("source_url")).lower()
            source_platform = text(source.get("source_platform")).lower()
            externally_hosted = (
                source_url.startswith(("http://", "https://"))
                and "cam-initiative/vigil" not in source_url
                and "cam-initiative.org" not in source_url
                and source_platform not in {"vigil", "cam initiative"}
            )
            if residence == "external" and (looks_vigil or looks_cam) and not externally_hosted:
                errors.append(f"{location} is marked external but identifies CAM/VIGIL origin")
            if residence == "vigil-internal" and not (looks_vigil or looks_cam):
                errors.append(f"{location} is marked vigil-internal without a CAM/VIGIL origin marker")
            if residence == "cam-internal" and not looks_cam:
                errors.append(f"{location} is marked cam-internal without a CAM/Caelestis origin marker")
            if role == "record-cross-reference" and residence != "vigil-internal":
                errors.append(f"{location} record-cross-reference must use vigil-internal residence")
            if residence == "vigil-internal" and role not in {
                "record-cross-reference", "direct-testimony", "incident-evidence", "governance-basis"
            }:
                errors.append(f"{location} vigil-internal source uses an incompatible source role")

    if errors:
        print("VIGIL source provenance validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated source_residence and source_role on {source_count} active source record(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
