#!/usr/bin/env python3
"""Backfill and verify source_residence/source_role on canonical VIGIL sources.

The migration is deliberately conservative.  A source is treated as external only
when it does not identify VIGIL, Caelestis, the CAM Initiative, or the Office of
the Planetary Custodian as its origin.  The generated report can therefore use
``source_residence == external`` as an affirmative eligibility signal rather
than trying to infer externality from a title or URL at render time.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

SCRIPT_PATH = Path(__file__).resolve()
VIGIL_ROOT = SCRIPT_PATH.parents[1]
RECORDS_ROOT = VIGIL_ROOT / "records"
SCHEMA_PATH = VIGIL_ROOT / "VIGIL.Schema.json"
MIGRATION_REPORT_PATH = VIGIL_ROOT / "migrations" / "source-provenance-migration-2026-07-29.json"

SOURCE_RESIDENCE_VALUES = (
    "external",
    "cam-internal",
    "vigil-internal",
    "user-supplied",
    "unknown",
)

SOURCE_ROLE_VALUES = (
    "incident-evidence",
    "affected-party-evidence",
    "research-evidence",
    "standards-or-regulatory-basis",
    "governance-basis",
    "taxonomy-basis",
    "implementation-evidence",
    "verification-evidence",
    "contextual-background",
    "record-cross-reference",
    "direct-testimony",
    "unknown",
)

VIGIL_ID_RE = re.compile(r"^VIGIL-\d{4}-(?:OBS|FM|PROP|PATCH|RESEARCH|LEARN)-\d{4}\b", re.I)

VIGIL_MARKERS = (
    "vigil",
    "cam-initiative/vigil",
)
CAM_MARKERS = (
    "cam initiative",
    "cam-initiative",
    "caelestis",
    "cam governance catalogue",
    "cam-governance-catalogue",
    "cam-initiative.org",
    "office of the planetary custodian",
)

EXTERNAL_INCIDENT_TYPES = {
    "news-report",
    "official-source",
    "social-platform-observation",
    "platform-behaviour-observation",
    "third-party-report",
    "repository-observation",
    "news report / regulatory reporting",
    "civil society safety assessment / public-interest report",
}
RESEARCH_TYPES = {
    "research-source",
    "deep-research-agent",
    "academic preprint / empirical audit",
}
STANDARDS_TYPES = {"standards-source"}
LINKED_TYPES = {
    "linked-observation",
    "linked-failure-mode",
    "linked-proposal",
}


def text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return str(value).strip()
    return ""


def combined_source_text(source: dict[str, Any]) -> str:
    fields = (
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
    return " | ".join(text(source.get(field)).lower() for field in fields)


def classify_residence(source: dict[str, Any]) -> str:
    title = text(source.get("source_title"))
    source_type = text(source.get("source_type")).lower()
    haystack = combined_source_text(source)

    if VIGIL_ID_RE.match(title) or source_type in LINKED_TYPES:
        return "vigil-internal"
    if any(marker in haystack for marker in VIGIL_MARKERS):
        return "vigil-internal"
    if any(marker in haystack for marker in CAM_MARKERS):
        return "cam-internal"
    if "direct incident testimony" in haystack or "authenticated account holder" in haystack:
        return "user-supplied"

    publisher = text(source.get("author_or_publisher"))
    url = text(source.get("source_url")) or text(source.get("archive_url"))
    platform = text(source.get("source_platform"))
    if publisher or url or platform:
        return "external"
    return "unknown"


def classify_role(source: dict[str, Any], record_type: str, residence: str) -> str:
    source_type = text(source.get("source_type")).lower()
    haystack = combined_source_text(source)

    if residence == "vigil-internal" or source_type in LINKED_TYPES:
        return "record-cross-reference"
    if residence == "user-supplied":
        return "direct-testimony"
    if source_type in STANDARDS_TYPES or any(token in haystack for token in ("standard", "regulation", "regulator", "legislation", " act ", "directive")):
        return "standards-or-regulatory-basis"
    if source_type in RESEARCH_TYPES:
        return "research-evidence"
    if source_type == "governance-note":
        return "governance-basis"

    if residence == "cam-internal":
        if any(token in haystack for token in ("taxonomy", "failure taxonomy", "operations-003-sup-01")):
            return "taxonomy-basis"
        if record_type == "patch":
            if any(token in haystack for token in ("verify", "verification", "exact text", "commit", "canonical main")):
                return "verification-evidence"
            return "implementation-evidence"
        if record_type == "proposal":
            return "governance-basis"
        if record_type == "failure_mode":
            return "governance-basis"
        return "contextual-background"

    if source_type in EXTERNAL_INCIDENT_TYPES:
        if any(token in haystack for token in ("affected party", "affected-party", "victim", "incident disclosure")):
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


def iter_record_paths() -> Iterable[Path]:
    yield from sorted(RECORDS_ROOT.rglob("*.json"))


def classify_record(path: Path, *, write: bool) -> tuple[bool, list[dict[str, Any]]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    record_type = text(data.get("record_type")).lower()
    sources = data.get("source_records")
    if not isinstance(sources, list):
        return False, []

    changed = False
    rows: list[dict[str, Any]] = []
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            continue
        residence = classify_residence(source)
        role = classify_role(source, record_type, residence)
        if source.get("source_residence") != residence:
            source["source_residence"] = residence
            changed = True
        if source.get("source_role") != role:
            source["source_role"] = role
            changed = True
        rows.append({
            "record_id": data.get("id") or data.get("record_identity", {}).get("record_id"),
            "path": str(path.relative_to(VIGIL_ROOT)),
            "source_index": index,
            "source_title": source.get("source_title"),
            "source_residence": residence,
            "source_role": role,
        })

    if changed and write:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return changed, rows


def update_schema(*, write: bool) -> bool:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    changed = False

    rules = schema.setdefault("source_evidence_rules", {}).setdefault("individual_records", [])
    additions = [
        "Each source record must state source_residence so external incident evidence is distinguishable from CAM/VIGIL provenance.",
        "Each source record must state source_role so evidence, governance basis, taxonomy basis, implementation evidence, verification evidence, and record cross-references are not rendered interchangeably.",
        "External-evidence interfaces must require source_residence external; absence of a VIGIL identifier is not sufficient evidence of external residence.",
        "CAM-internal and VIGIL-internal sources remain valid provenance but must not be rendered as external incident evidence.",
    ]
    for rule in additions:
        if rule not in rules:
            rules.append(rule)
            changed = True

    defs = schema.setdefault("$defs", {})
    expected_residence = {"enum": list(SOURCE_RESIDENCE_VALUES)}
    expected_role = {"enum": list(SOURCE_ROLE_VALUES)}
    if defs.get("source_residence") != expected_residence:
        defs["source_residence"] = expected_residence
        changed = True
    if defs.get("source_role") != expected_role:
        defs["source_role"] = expected_role
        changed = True

    required = defs.setdefault("source_record", {}).setdefault("required", [])
    for field in ("source_residence", "source_role"):
        if field not in required:
            insert_at = required.index("source_type") + 1 if "source_type" in required else len(required)
            required.insert(insert_at, field)
            changed = True

    if changed and write:
        SCHEMA_PATH.write_text(json.dumps(schema, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return changed


def update_templates(*, write: bool) -> list[str]:
    changed_paths: list[str] = []
    for path in sorted((VIGIL_ROOT / "templates").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        sources = data.get("source_records")
        if not isinstance(sources, list):
            continue
        changed = False
        for source in sources:
            if not isinstance(source, dict):
                continue
            if "source_residence" not in source:
                source["source_residence"] = "external"
                changed = True
            if "source_role" not in source:
                source["source_role"] = "incident-evidence"
                changed = True
        if changed:
            changed_paths.append(str(path.relative_to(VIGIL_ROOT)))
            if write:
                path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return changed_paths


def build_report(rows: list[dict[str, Any]], changed_paths: list[str]) -> dict[str, Any]:
    residence_counts = Counter(row["source_residence"] for row in rows)
    role_counts = Counter(row["source_role"] for row in rows)
    unresolved = [row for row in rows if row["source_residence"] == "unknown" or row["source_role"] == "unknown"]
    return {
        "migration": "source-residence-and-role",
        "migration_date": "2026-07-29",
        "scope": "Canonical JSON records containing source_records; LEARN records inherit evidence through their linked Failure Mode and do not duplicate incident sources.",
        "classification_policy": {
            "externality_rule": "A source is externally resident only when it does not identify VIGIL, Caelestis, CAM Initiative, CAM Governance Catalogue, cam-initiative.org, or the Office of the Planetary Custodian as its origin.",
            "rendering_rule": "External-evidence interfaces must affirmatively require source_residence == external; source_role supplies the purpose of the source within the chain.",
            "conservative_default": "Sources without sufficient origin metadata are classified unknown and are ineligible for external-evidence rendering until reviewed.",
        },
        "source_count": len(rows),
        "residence_counts": dict(sorted(residence_counts.items())),
        "role_counts": dict(sorted(role_counts.items())),
        "changed_record_paths": changed_paths,
        "unresolved_sources": unresolved,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail when migration output is not already applied.")
    args = parser.parse_args()
    write = not args.check

    rows: list[dict[str, Any]] = []
    changed_paths: list[str] = []
    for path in iter_record_paths():
        changed, record_rows = classify_record(path, write=write)
        rows.extend(record_rows)
        if changed:
            changed_paths.append(str(path.relative_to(VIGIL_ROOT)))

    schema_changed = update_schema(write=write)
    template_changes = update_templates(write=write)
    report = build_report(rows, changed_paths)
    report["schema_changed"] = schema_changed
    report["changed_template_paths"] = template_changes

    expected_report = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    existing_report = MIGRATION_REPORT_PATH.read_text(encoding="utf-8") if MIGRATION_REPORT_PATH.exists() else None
    report_changed = existing_report != expected_report
    if write:
        MIGRATION_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        MIGRATION_REPORT_PATH.write_text(expected_report, encoding="utf-8")

    unresolved = report["unresolved_sources"]
    if unresolved:
        for row in unresolved:
            print(f"UNRESOLVED {row['path']} source_records[{row['source_index']}]: {row['source_title']}")

    if args.check and (changed_paths or schema_changed or template_changes or report_changed):
        print("Source provenance migration is not fully applied.")
        for path in changed_paths:
            print(f"  record requires migration: {path}")
        for path in template_changes:
            print(f"  template requires migration: {path}")
        if schema_changed:
            print("  schema requires migration")
        if report_changed:
            print("  migration report requires rebuild")
        return 1
    if unresolved:
        print(f"Source provenance classification has {len(unresolved)} unresolved source(s).")
        return 2

    print(f"Classified {len(rows)} source record(s): {dict(Counter(row['source_residence'] for row in rows))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
