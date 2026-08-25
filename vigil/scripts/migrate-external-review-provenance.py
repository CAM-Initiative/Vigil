#!/usr/bin/env python3
"""Apply the bounded August 2026 EXTREQ substantive-review provenance migration."""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "external_sources" / "source-registry.json"
SCOPE_PATH = ROOT / "external_requirements" / "source-scope.json"
REQUIREMENTS_PATH = ROOT / "external_requirements" / "requirements.json"

REVIEW_SYSTEM = {"provider": "OpenAI", "platform": "ChatGPT", "model": "GPT-5.6 Sol"}
ACCESS_METHOD = {
    "direct-public-primary": "direct-public-primary-review",
    "direct-licensed-primary": "direct-licensed-primary-review",
    "official-public-extract": "official-public-extract-review",
    "official-metadata-only": "official-metadata-only-review",
    "secondary-source-only": "secondary-source-only-review",
    "source-unavailable": "blocked-primary-text-review",
}
SCOPE_METHOD = {
    "complete": "bounded-complete-review",
    "partial": "partial-review",
    "in-progress": "partial-review",
    "supporting-only": "supporting-only-review",
    "context-only": "context-only-review",
    "blocked-access": "blocked-primary-text-review",
    "not-started": "not-started",
    "excluded": "excluded",
    "superseded-version": "superseded-version-review",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def event_id(vigil_source_id: str, source_version: str, review_date: str, event_kind: str) -> str:
    material = "|".join((vigil_source_id, source_version, review_date, event_kind))
    return "EXTREV-" + hashlib.sha256(material.encode("utf-8")).hexdigest()[:16].upper()


def review_event(entry: dict[str, Any], scope: dict[str, Any], review_date: str, event_kind: str) -> dict[str, Any]:
    if event_kind == "structured-requirement-extraction":
        review_scope = (
            "Structured requirement extraction and analytical paraphrase of governance-significant material "
            "represented in canonical external-requirement records under the source-specific extraction scope."
        )
    else:
        review_scope = (
            "Substantive reassessment of source currency, public summary, AI-governance relevance, lifecycle "
            "applicability, relevance scope and source-specific qualifications."
        )
    return {
        "review_event_id": event_id(entry["vigil_source_id"], entry["source_version"], review_date, event_kind),
        "review_date": review_date,
        "review_system": REVIEW_SYSTEM,
        "ai_role": "substantive-analytical-reviewer",
        "generation_mode": "semi-autonomous",
        "review_method": {
            "access_method": ACCESS_METHOD[scope["source_access_status"]],
            "scope_method": SCOPE_METHOD[scope["extraction_status"]],
        },
        "review_scope": review_scope,
        "source_scope_reference": "vigil/external_requirements/source-scope.json",
        "limitations_reference": [
            "source_access_notes",
            "extraction_scope_notes",
            "inaccessible_sections",
            "known_unreviewed_sections",
        ],
        "human_role": "contract-approver",
        "human_review_status": "not-reviewed",
        "human_verification_status": "not-verified",
    }


def migrate() -> dict[str, int]:
    registry = load(REGISTRY_PATH)
    scopes = {
        (item["vigil_source_id"], item["source_version"]): item
        for item in load(SCOPE_PATH)["entries"]
    }
    extraction_dates: dict[tuple[str, str], set[str]] = defaultdict(set)
    for requirement in load(REQUIREMENTS_PATH)["requirements"]:
        extraction_dates[(requirement["vigil_source_id"], requirement["source_version"])].add(
            requirement["source_review_date"]
        )

    event_count = 0
    extraction_event_count = 0
    for entry in registry["entries"]:
        key = (entry["vigil_source_id"], entry["source_version"])
        scope = scopes[key]
        events = []
        for review_date in sorted(extraction_dates.get(key, set())):
            events.append(review_event(entry, scope, review_date, "structured-requirement-extraction"))
            extraction_event_count += 1
        events.append(review_event(entry, scope, entry["last_substantive_reviewed"], "public-governance-knowledge-review"))
        entry["substantive_review_provenance"] = {
            "current_review_event_id": events[-1]["review_event_id"],
            "review_events": events,
        }
        event_count += len(events)

    registry["schema_version"] = "1.2"
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "sources": len(registry["entries"]),
        "events": event_count,
        "requirement_extraction_events": extraction_event_count,
    }


if __name__ == "__main__":
    print(json.dumps(migrate(), sort_keys=True))
