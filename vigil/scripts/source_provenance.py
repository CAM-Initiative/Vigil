#!/usr/bin/env python3
"""Shared source-provenance classification helpers for VIGIL records.

This module contains current reusable classification semantics. Historical corpus
backfill machinery belongs in Git history, not in the live scripts directory.
"""

from __future__ import annotations

import re
from typing import Any

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
VIGIL_INTERNAL_SOURCE_TYPES = {"governance-note", "linked-failure-mode", "linked-observation", "linked-proposal"}
LINKED_TYPES = {"linked-observation", "linked-failure-mode", "linked-proposal"}

EXTERNAL_INCIDENT_TYPES = {
    "news-report",
    "official-source",
    "social-platform-observation",
    "platform-behaviour-observation",
    "third-party-report",
    "repository-observation",
    "news report / regulatory reporting",
    "civil society safety assessment / public-interest report",
    "incident-database record",
    "ai incident database record",
}
RESEARCH_TYPES = {"research-source", "deep-research-agent", "academic preprint / empirical audit"}
STANDARDS_TYPES = {"standards-source"}


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


def role_text(source: dict[str, Any]) -> str:
    """Return bounded source semantics used to classify evidentiary role, not origin."""
    return " | ".join(
        text(source.get(field)).lower()
        for field in (
            "source_title",
            "author_or_publisher",
            "source_type",
            "source_context",
            "deployment_context",
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


def classify_residence(source: dict[str, Any]) -> str:
    """Return the current source-residence classification for an authored source."""
    looks_vigil, looks_cam = origin_markers(source)
    source_type = text(source.get("source_type")).lower()
    status = text(source.get("source_url_status")).lower()

    if looks_vigil:
        return "vigil-internal"
    if looks_cam:
        return "cam-internal"
    if "direct incident testimony" in status or "authenticated account holder" in status or source_type == "direct-testimony":
        return "user-supplied"
    if any(text(source.get(field)) for field in ("author_or_publisher", "source_url", "archive_url", "source_platform")):
        return "external"
    return "unknown"


def classify_role(source: dict[str, Any], record_type: str, residence: str) -> str:
    """Return the current source-role classification."""
    source_type = text(source.get("source_type")).lower()
    identity = identity_text(source)
    semantics = role_text(source)

    if residence == "vigil-internal" or source_type in LINKED_TYPES:
        return "record-cross-reference"
    if residence == "user-supplied":
        return "direct-testimony"
    if source_type in STANDARDS_TYPES or any(token in identity for token in ("standard", "regulation", "regulator", "legislation", " directive")):
        return "standards-or-regulatory-basis"
    if source_type in RESEARCH_TYPES:
        return "research-evidence"
    if source_type == "governance-note":
        return "governance-basis"

    if residence == "cam-internal":
        if any(token in semantics for token in ("taxonomy", "failure taxonomy", "operations-003-sup-01")):
            return "taxonomy-basis"
        if record_type == "patch":
            return "implementation-evidence"
        if record_type in {"proposal", "failure_mode"}:
            return "governance-basis"
        return "contextual-background"

    if source_type in EXTERNAL_INCIDENT_TYPES:
        if any(token in semantics for token in ("affected party", "affected-party", "victim", "incident disclosure")):
            return "affected-party-evidence"
        return "incident-evidence"
    if source_type in {"repository-source", "repository source"}:
        return "verification-evidence" if record_type == "patch" else "incident-evidence"
    if record_type == "patch":
        return "verification-evidence"
    if record_type in {"observation", "failure_mode"}:
        return "incident-evidence"
    if record_type == "proposal":
        return "contextual-background"
    return "unknown"
