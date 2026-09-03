#!/usr/bin/env python3
"""Source-origin helpers used by Incident provenance validation."""

from __future__ import annotations

import re
from typing import Any

VIGIL_ID_RE = re.compile(
    r"^(?:VIGIL-INC-\d{6}|VIGIL-\d{4}-(?:OBS|FM|PROP|PATCH|RESEARCH|LEARN)-\d{4})\b",
    re.I,
)
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
VIGIL_INTERNAL_SOURCE_TYPES = {
    "governance record", "observation record", "linked-failure-mode", "linked-observation",
    "linked-proposal",
}
LINKED_TYPES = {"linked-failure-mode", "linked-observation", "linked-proposal"}


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
    """Identify VIGIL/CAM origin from source identity, not relevance prose."""
    title = text(source.get("source_title"))
    author = text(source.get("author_or_publisher"))
    platform = text(source.get("source_platform")).lower()
    source_type = text(source.get("source_type")).lower()
    source_url = text(source.get("source_url")).lower()
    archive_url = text(source.get("archive_url")).lower()
    identity = identity_text(source)

    title_is_internal_vigil = source_type in VIGIL_INTERNAL_SOURCE_TYPES and title.lower().startswith("vigil ")
    looks_vigil = (
        VIGIL_ID_RE.match(title) is not None
        or VIGIL_AUTHOR_RE.match(author) is not None
        or platform == "vigil"
        or title_is_internal_vigil
        or source_type in LINKED_TYPES
        or any(hint in source_url or hint in archive_url for hint in VIGIL_URL_HINTS)
    )
    looks_cam = any(hint in identity for hint in CAM_HINTS)
    return looks_vigil, looks_cam
