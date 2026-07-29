#!/usr/bin/env python3
"""Validate source residence and role metadata across canonical VIGIL records."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
VIGIL_ROOT = SCRIPT_PATH.parents[1]
RECORDS_ROOT = VIGIL_ROOT / "records"
SCHEMA_PATH = VIGIL_ROOT / "VIGIL.Schema.json"

VIGIL_ID_RE = re.compile(r"^VIGIL-\d{4}-(?:OBS|FM|PROP|PATCH|RESEARCH|LEARN)-\d{4}\b", re.I)
CAM_HINTS = (
    "cam initiative",
    "cam-initiative",
    "caelestis",
    "cam governance catalogue",
    "cam-governance-catalogue",
    "cam-initiative.org",
    "office of the planetary custodian",
)
VIGIL_HINTS = ("vigil", "cam-initiative/vigil")


def text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return str(value).strip()
    return ""


def source_text(source: dict[str, Any]) -> str:
    return " | ".join(
        text(source.get(field)).lower()
        for field in (
            "source_title",
            "author_or_publisher",
            "source_url",
            "archive_url",
            "source_platform",
            "system_or_product",
            "model_or_algorithm",
            "deployment_context",
            "source_context",
            "relevance_note",
            "source_type",
            "source_url_status",
        )
    )


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
    for path in sorted(RECORDS_ROOT.rglob("*.json")):
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
            title = text(source.get("source_title"))
            haystack = source_text(source)

            if residence not in allowed_residences:
                errors.append(f"{location} invalid source_residence {residence!r}")
            if role not in allowed_roles:
                errors.append(f"{location} invalid source_role {role!r}")
            if residence == "unknown" or role == "unknown":
                errors.append(f"{location} unresolved source provenance is not permitted in canonical records")

            looks_vigil = VIGIL_ID_RE.match(title) is not None or any(hint in haystack for hint in VIGIL_HINTS)
            looks_cam = any(hint in haystack for hint in CAM_HINTS)
            if residence == "external" and (looks_vigil or looks_cam):
                errors.append(f"{location} is marked external but identifies CAM/VIGIL origin")
            if residence == "vigil-internal" and not looks_vigil:
                errors.append(f"{location} is marked vigil-internal without a VIGIL origin marker")
            if residence == "cam-internal" and not looks_cam:
                errors.append(f"{location} is marked cam-internal without a CAM/Caelestis origin marker")
            if role == "record-cross-reference" and residence != "vigil-internal":
                errors.append(f"{location} record-cross-reference must use vigil-internal residence")
            if residence == "vigil-internal" and role != "record-cross-reference":
                errors.append(f"{location} vigil-internal source must use record-cross-reference role")

    if errors:
        print("VIGIL source provenance validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated source_residence and source_role on {source_count} source record(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
