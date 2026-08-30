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
VIGIL_AUTHOR_RE = re.compile(r"^(?:cam initiative\s*/\s*)?vigil(?:\b|\s*/)", re.I)
CAM_HINTS = (
    "cam initiative",
    "cam-initiative",
    "caelestis",
    "cam governance catalogue",
    "cam-governance-catalogue",
    "cam-initiative.org",
    "office of the planetary custodian",
)
VIGIL_URL_HINTS = ("cam-initiative/vigil", "/vigil/", "cam-initiative.org/vigil")
VIGIL_INTERNAL_SOURCE_TYPES = {"governance-note", "linked-failure-mode"}


def text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return str(value).strip()
    return ""


def identity_text(source: dict[str, Any]) -> str:
    """Return source-origin fields only, excluding VIGIL interpretive commentary."""
    return " | ".join(
        text(source.get(field)).lower()
        for field in (
            "source_title",
            "author_or_publisher",
            "source_url",
            "archive_url",
            "source_platform",
            "source_type",
            "source_url_status",
        )
    )


def origin_markers(source: dict[str, Any]) -> tuple[bool, bool]:
    """Classify CAM/VIGIL origin from source identity, not relevance/interpretation prose."""
    title = text(source.get("source_title"))
    author = text(source.get("author_or_publisher"))
    platform = text(source.get("source_platform")).lower()
    source_type = text(source.get("source_type")).lower()
    source_url = text(source.get("source_url")).lower()
    archive_url = text(source.get("archive_url")).lower()
    identity = identity_text(source)

    title_is_internal_vigil = (
        source_type in VIGIL_INTERNAL_SOURCE_TYPES
        and title.lower().startswith("vigil ")
    )
    looks_vigil = (
        VIGIL_ID_RE.match(title) is not None
        or VIGIL_AUTHOR_RE.match(author) is not None
        or platform == "vigil"
        or title_is_internal_vigil
        or any(hint in source_url or hint in archive_url for hint in VIGIL_URL_HINTS)
    )
    looks_cam = any(hint in identity for hint in CAM_HINTS)
    return looks_vigil, looks_cam


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

            if residence not in allowed_residences:
                errors.append(f"{location} invalid source_residence {residence!r}")
            if role not in allowed_roles:
                errors.append(f"{location} invalid source_role {role!r}")
            if residence == "unknown" or role == "unknown":
                errors.append(f"{location} unresolved source provenance is not permitted in canonical records")

            looks_vigil, looks_cam = origin_markers(source)
            if residence == "external" and (looks_vigil or looks_cam):
                errors.append(f"{location} is marked external but identifies CAM/VIGIL origin")
            # VIGIL-internal provenance can be authored by the CAM Initiative when the
            # artefact is a VIGIL drafting/review source. CAM-internal is reserved for
            # CAM/Caelestis governance material rather than every CAM-authored note.
            if residence == "vigil-internal" and not (looks_vigil or looks_cam):
                errors.append(f"{location} is marked vigil-internal without a CAM/VIGIL origin marker")
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
