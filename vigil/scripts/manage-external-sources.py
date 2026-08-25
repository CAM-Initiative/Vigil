#!/usr/bin/env python3
"""Maintain VIGIL's canonical external governance source registry.

This module records external-source identity, version, lifecycle, durable public
governance knowledge, change state and source-review workflow. It does not assess
CAM applicability and it never edits CAM.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXT = ROOT / "external_sources"
MATRIX_PATH = EXT / "source-matrix.json"
REGISTRY_PATH = EXT / "source-registry.json"
SOURCE_SCOPE_PATH = ROOT / "external_requirements" / "source-scope.json"
QUEUE_PATH = EXT / "source-review-queue.json"
CATALOGUE_PATH = EXT / "SOURCE-CATALOGUE.md"
PROVENANCE_REF = "vigil/provenance/AUTHORSHIP-PROVENANCE.json"

DEFAULT_PROVENANCE = {
    "content_origin": "ai-authored",
    "generation_mode": "semi-autonomous",
    "human_role": "contract-approver",
    "human_authorship": False,
    "human_review_status": "not-reviewed",
    "human_verification_status": "not-verified",
    "declaration": PROVENANCE_REF,
}
GENERATED_PROVENANCE = {
    "content_origin": "deterministically-generated",
    "generation_mode": "deterministic-generation",
    "human_role": "contract-approver",
    "human_authorship": False,
    "human_review_status": "not-reviewed",
    "human_verification_status": "not-verified",
    "declaration": PROVENANCE_REF,
    "upstream_provenance": ["vigil/external_sources/source-registry.json"],
}

REVIEW_STATES = {"unassigned", "review-required", "reviewed", "superseded-before-review"}
CHANGE_STATES = {"new", "changed", "superseded", "withdrawn", "unchanged"}
REVIEW_FRESHNESS_DAYS = 90
REVIEW_METHOD_ACCESS = {
    "direct-public-primary": "direct-public-primary-review",
    "direct-licensed-primary": "direct-licensed-primary-review",
    "official-public-extract": "official-public-extract-review",
    "official-metadata-only": "official-metadata-only-review",
    "secondary-source-only": "secondary-source-only-review",
    "source-unavailable": "blocked-primary-text-review",
}
REVIEW_METHOD_SCOPE = {
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
REVIEW_EVENT_REQUIRED = {
    "review_event_id", "review_date", "review_system", "ai_role", "generation_mode",
    "review_method", "review_scope", "source_scope_reference", "limitations_reference",
    "human_role", "human_review_status", "human_verification_status",
}
AI_GOVERNANCE_RELEVANCE = {
    "accountability", "ai-literacy", "assurance", "change-management", "conformity",
    "data-governance", "documentation", "environmental-impact", "fairness-bias",
    "human-oversight", "impact-assessment", "incident-governance", "inventory",
    "lifecycle-governance", "monitoring", "privacy", "provenance", "risk-management",
    "robustness", "safety", "security", "supply-chain", "testing-evaluation",
    "traceability", "transparency", "worker-affected-person-rights",
}
LIFECYCLE_STAGES = {
    "governance", "design", "development", "data-acquisition", "training",
    "testing-evaluation", "conformity-assessment", "placing-on-market", "deployment",
    "operation-use", "monitoring", "incident-response", "change-management",
    "retirement", "supply-chain", "cross-lifecycle", "not-specified",
}
PUBLIC_NARRATIVE_PATTERNS = {
    "project or corpus context": re.compile(r"\b(?:VIGIL|CAM|Caelestis)\b", re.IGNORECASE),
    "repository workflow context": re.compile(
        r"\b(?:working branch|agent handoff|repository migration|schema migration|validator repair|ledger inclusion|reconciliation pass)\b",
        re.IGNORECASE,
    ),
    "maintainer tasking": re.compile(
        r"\b(?:TODO|semantic review required|alignment review required|review-required)\b",
        re.IGNORECASE,
    ),
}


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def source_map() -> dict[str, dict[str, Any]]:
    matrix = load_json(MATRIX_PATH)
    return {item["source_id"]: item for item in matrix["sources"]}


def stable_id(external_source_id: str) -> str:
    digest = hashlib.sha256(external_source_id.encode("utf-8")).hexdigest()[:12].upper()
    return f"EXT-{digest}"


def normalise_state(value: str) -> str:
    return str(value or "unknown").strip().lower().replace("_", "-").replace(" ", "-")


def review_eligible(source: dict[str, Any], lifecycle: str) -> bool:
    eligible = {normalise_state(v) for v in source.get("review_eligible_states", [])}
    return normalise_state(lifecycle) in eligible


def parse_review_date(value: Any) -> dt.date | None:
    if not isinstance(value, str):
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def review_is_due(entry: dict[str, Any], as_of: dt.date | None = None) -> bool:
    if not entry.get("review_eligible"):
        return False
    reviewed = parse_review_date(entry.get("last_substantive_reviewed"))
    if reviewed is None:
        return True
    return (as_of or dt.datetime.now(dt.timezone.utc).date()) >= reviewed + dt.timedelta(days=REVIEW_FRESHNESS_DAYS)


def next_substantive_review(entry: dict[str, Any]) -> str | None:
    reviewed = parse_review_date(entry.get("last_substantive_reviewed"))
    return (reviewed + dt.timedelta(days=REVIEW_FRESHNESS_DAYS)).isoformat() if reviewed else None


def current_review_event(entry: dict[str, Any]) -> dict[str, Any] | None:
    provenance = entry.get("substantive_review_provenance")
    if not isinstance(provenance, dict):
        return None
    current_id = provenance.get("current_review_event_id")
    return next(
        (event for event in provenance.get("review_events", []) if event.get("review_event_id") == current_id),
        None,
    )


def material_projection(item: dict[str, Any]) -> dict[str, Any]:
    keys = (
        "external_source_id", "source_version", "canonical_identifier", "title", "issuer",
        "jurisdiction", "source_class", "source_lifecycle_state", "publication_date",
        "effective_date", "official_locator", "upstream_record_id", "upstream_release",
    )
    return {key: item.get(key) for key in keys}


def metadata_fingerprint(item: dict[str, Any]) -> str:
    encoded = json.dumps(material_projection(item), sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def require(item: dict[str, Any], *fields: str) -> None:
    missing = [field for field in fields if item.get(field) in (None, "")]
    if missing:
        raise ValueError(f"normalised item missing required field(s): {', '.join(missing)}")


def canonicalise(raw: dict[str, Any], source_id: str, source: dict[str, Any]) -> dict[str, Any]:
    require(
        raw,
        "external_source_id", "source_version", "issuer", "jurisdiction", "source_class",
        "source_lifecycle_state", "official_locator",
    )
    canonical_identifier = raw.get("canonical_identifier")
    if not isinstance(canonical_identifier, dict) or not canonical_identifier.get("scheme") or not canonical_identifier.get("value"):
        raise ValueError("canonical_identifier must contain scheme and value")
    now = raw.get("observed_at") or utc_now()
    item = {
        "vigil_source_id": stable_id(str(raw["external_source_id"])),
        "external_source_id": str(raw["external_source_id"]),
        "source_version": str(raw["source_version"]),
        "canonical_identifier": {
            "scheme": str(canonical_identifier["scheme"]),
            "value": str(canonical_identifier["value"]),
        },
        "title": raw.get("title"),
        "issuer": str(raw["issuer"]),
        "jurisdiction": str(raw["jurisdiction"]),
        "source_class": str(raw["source_class"]),
        "source_lifecycle_state": normalise_state(str(raw["source_lifecycle_state"])),
        "publication_date": raw.get("publication_date"),
        "effective_date": raw.get("effective_date"),
        "official_locator": str(raw["official_locator"]),
        "upstream_source_id": source_id,
        "upstream_record_id": raw.get("upstream_record_id"),
        "upstream_release": raw.get("upstream_release"),
        "source_metadata_fingerprint": "",
        "change_state": "new",
        "review_state": "unassigned",
        "review_eligible": False,
        "first_seen": now,
        "last_seen": now,
        "public_summary": raw.get("public_summary"),
        "ai_governance_relevance": raw.get("ai_governance_relevance"),
        "applicable_lifecycle_stages": raw.get("applicable_lifecycle_stages"),
        "relevance_scope": raw.get("relevance_scope"),
        "last_substantive_reviewed": raw.get("last_substantive_reviewed"),
        "substantive_review_provenance": raw.get("substantive_review_provenance"),
        "notes": raw.get("notes"),
    }
    item["review_eligible"] = review_eligible(source, item["source_lifecycle_state"])
    item["source_metadata_fingerprint"] = metadata_fingerprint(item)
    if item["review_eligible"]:
        item["review_state"] = "review-required"
    return item


def entry_key(item: dict[str, Any]) -> tuple[str, str]:
    return str(item["external_source_id"]), str(item["source_version"])


def merge_item(existing: dict[str, Any] | None, incoming: dict[str, Any]) -> dict[str, Any]:
    if existing is None:
        return incoming
    merged = dict(incoming)
    merged["first_seen"] = existing["first_seen"]
    merged["last_seen"] = incoming["last_seen"]
    for field in (
        "public_summary", "ai_governance_relevance", "applicable_lifecycle_stages",
        "relevance_scope", "last_substantive_reviewed", "substantive_review_provenance", "notes",
    ):
        if merged.get(field) in (None, "", []):
            merged[field] = existing.get(field)
    if existing.get("source_metadata_fingerprint") == incoming.get("source_metadata_fingerprint"):
        merged["change_state"] = "unchanged"
        merged["review_state"] = existing.get("review_state", incoming["review_state"])
    else:
        state = incoming["source_lifecycle_state"]
        if state in {"withdrawn", "revoked"}:
            merged["change_state"] = "withdrawn"
        elif state in {"superseded", "replaced"}:
            merged["change_state"] = "superseded"
        else:
            merged["change_state"] = "changed"
        if incoming["review_eligible"]:
            merged["review_state"] = "review-required"
        else:
            merged["review_state"] = existing.get("review_state", "unassigned")
    return merged


def build_queue(registry: dict[str, Any] | None = None, as_of: dt.date | None = None) -> dict[str, Any]:
    registry = registry or load_json(REGISTRY_PATH)
    items = []
    for entry in registry.get("entries", []):
        due = review_is_due(entry, as_of=as_of)
        if entry.get("review_state") != "review-required" and not due:
            continue
        current = current_review_event(entry) or {}
        items.append({
            "vigil_source_id": entry["vigil_source_id"],
            "external_source_id": entry["external_source_id"],
            "source_version": entry["source_version"],
            "canonical_identifier": entry["canonical_identifier"],
            "title": entry.get("title"),
            "issuer": entry["issuer"],
            "jurisdiction": entry["jurisdiction"],
            "source_lifecycle_state": entry["source_lifecycle_state"],
            "official_locator": entry["official_locator"],
            "upstream_source_id": entry["upstream_source_id"],
            "change_state": entry["change_state"],
            "source_metadata_fingerprint": entry["source_metadata_fingerprint"],
            "last_substantive_reviewed": entry.get("last_substantive_reviewed"),
            "next_substantive_review": next_substantive_review(entry),
            "review_system": current.get("review_system"),
            "review_method": current.get("review_method"),
            "review_due": due,
            "required_action": "substantive-reassessment" if due else "semantic-source-review",
        })
    return {
        "schema_version": "1.1",
        "review_freshness_days": REVIEW_FRESHNESS_DAYS,
        "generated_at": registry.get("updated_at"),
        "authorship_provenance": GENERATED_PROVENANCE,
        "items": items,
    }


def render_catalogue(registry: dict[str, Any] | None = None) -> str:
    registry = registry or load_json(REGISTRY_PATH)
    entries = sorted(registry.get("entries", []), key=lambda x: (x["external_source_id"], x["source_version"]))
    due_count = sum(review_is_due(entry) for entry in entries)
    lines = [
        "# External Governance Sources", "",
        "Public knowledge catalogue of external governance sources and their bounded relevance to AI governance. The summaries describe source subject matter; they do not provide legal advice or establish that a source applies to any particular system or organisation.", "",
        f"- Source versions: {len(entries)}",
        f"- Review-due source versions: {due_count}",
        f"- Registry updated through: {registry.get('updated_at')}", "",
    ]
    for entry in entries:
        due = review_is_due(entry)
        current = current_review_event(entry) or {}
        system = current.get("review_system") or {}
        method = current.get("review_method") or {}
        lines += [
            f"## {entry.get('title') or entry['external_source_id']}", "",
            entry.get("public_summary") or "No public summary is available.", "",
            f"- **Issuer:** {entry['issuer']}",
            f"- **Version:** `{entry['source_version']}`",
            f"- **Lifecycle state:** `{entry['source_lifecycle_state']}`",
            f"- **AI-governance relevance:** {', '.join(entry.get('ai_governance_relevance') or [])}",
            f"- **Applicable lifecycle stages:** {', '.join(entry.get('applicable_lifecycle_stages') or [])}",
            f"- **Relevance scope:** {entry.get('relevance_scope') or 'Not assessed.'}",
            f"- **Last substantive review:** {entry.get('last_substantive_reviewed') or 'not recorded'}",
            f"- **Next substantive review:** {next_substantive_review(entry) or 'not scheduled'}",
            f"- **Substantive reviewer:** {system.get('provider', 'not recorded')} / {system.get('platform', 'not recorded')} / {system.get('model', 'not recorded')}",
            f"- **Review method:** {method.get('access_method', 'not recorded')} · {method.get('scope_method', 'not recorded')}",
            f"- **Review freshness:** {'review due' if due else 'current'}",
            f"- **Official source:** {entry['official_locator']}", "",
        ]
    lines += [
        "",
        "The metadata fingerprint is a SHA-256 of material source identity and lifecycle metadata. It is not a digest of a reviewed PDF, HTML capture or licensed standard artefact.",
        "",
        "## Authorship provenance", "",
        f"This catalogue is deterministically generated from `source-registry.json`. No human review or verification is implied. See `{PROVENANCE_REF}`.", "",
    ]
    return "\n".join(lines)


def ingest(source_id: str, input_path: Path) -> None:
    sources = source_map()
    if source_id not in sources:
        raise ValueError(f"unknown source_id: {source_id}")
    source = sources[source_id]
    raw = load_json(input_path)
    if not isinstance(raw, list):
        raise ValueError("ingest input must be a JSON array of normalised source items")
    registry = load_json(REGISTRY_PATH)
    current = {entry_key(item): item for item in registry.get("entries", [])}
    for raw_item in raw:
        incoming = canonicalise(raw_item, source_id, source)
        key = entry_key(incoming)
        current[key] = merge_item(current.get(key), incoming)
    registry["updated_at"] = utc_now()
    registry["entries"] = sorted(current.values(), key=lambda x: (x["external_source_id"], x["source_version"]))
    dump_json(REGISTRY_PATH, registry)
    build()


def validate(check_generated: bool = False) -> None:
    matrix = load_json(MATRIX_PATH)
    registry = load_json(REGISTRY_PATH)
    errors: list[str] = []
    warnings: list[str] = []
    scope_document = load_json(SOURCE_SCOPE_PATH)
    scopes = {
        (item["vigil_source_id"], item["source_version"]): item
        for item in scope_document.get("entries", [])
    }
    source_ids = [s["source_id"] for s in matrix.get("sources", [])]
    if len(source_ids) != len(set(source_ids)):
        errors.append("duplicate source_id in source matrix")
    if "vorp" in json.dumps(matrix).lower() and not matrix.get("design_rules", {}).get("vorp_labs_excluded"):
        errors.append("Vorp provenance boundary is not explicit")
    seen = set()
    forbidden = {"fingerprint", "alignment_state", "alignment_eligible", "caelestis_assessed_commit", "caelestis_crosswalk_refs"}
    for entry in registry.get("entries", []):
        key = entry_key(entry)
        if key in seen:
            errors.append(f"duplicate registry key: {key}")
        seen.add(key)
        if forbidden.intersection(entry):
            errors.append(f"legacy source-registry fields remain for {key}: {sorted(forbidden.intersection(entry))}")
        if entry.get("review_state") not in REVIEW_STATES:
            errors.append(f"invalid review_state for {key}")
        if entry.get("change_state") not in CHANGE_STATES:
            errors.append(f"invalid change_state for {key}")
        if entry.get("source_metadata_fingerprint") != metadata_fingerprint(entry):
            errors.append(f"source metadata fingerprint mismatch for {key}")
        if not isinstance(entry.get("review_eligible"), bool):
            errors.append(f"review_eligible must be boolean for {key}")
        if entry.get("review_eligible"):
            summary = entry.get("public_summary")
            relevance_scope = entry.get("relevance_scope")
            themes = entry.get("ai_governance_relevance")
            stages = entry.get("applicable_lifecycle_stages")
            reviewed = parse_review_date(entry.get("last_substantive_reviewed"))
            provenance = entry.get("substantive_review_provenance")
            if not isinstance(summary, str) or len(summary.split()) < 50:
                errors.append(f"active source requires a meaningful public_summary of at least 50 words for {key}")
            elif not 80 <= len(summary.split()) <= 180:
                warnings.append(f"public_summary outside the preferred 80-180 word range for {key}")
            if not isinstance(relevance_scope, str) or len(relevance_scope.split()) < 10:
                errors.append(f"active source requires a substantive relevance_scope for {key}")
            if not isinstance(themes, list) or not themes:
                errors.append(f"active source requires ai_governance_relevance for {key}")
            elif invalid := set(themes) - AI_GOVERNANCE_RELEVANCE:
                errors.append(f"invalid ai_governance_relevance for {key}: {sorted(invalid)}")
            if not isinstance(stages, list) or not stages:
                errors.append(f"active source requires applicable_lifecycle_stages for {key}")
            elif invalid := set(stages) - LIFECYCLE_STAGES:
                errors.append(f"invalid applicable_lifecycle_stages for {key}: {sorted(invalid)}")
            if reviewed is None:
                errors.append(f"active source requires ISO-date last_substantive_reviewed for {key}")
            elif reviewed > dt.datetime.now(dt.timezone.utc).date():
                errors.append(f"last_substantive_reviewed cannot be in the future for {key}")
            elif review_is_due(entry):
                warnings.append(f"substantive review is due for {key}")
            if not isinstance(provenance, dict):
                errors.append(f"active source requires substantive_review_provenance for {key}")
            else:
                events = provenance.get("review_events")
                if not isinstance(events, list) or not events:
                    errors.append(f"substantive_review_provenance requires review_events for {key}")
                else:
                    dates = []
                    event_ids = set()
                    for event in events:
                        if not isinstance(event, dict):
                            errors.append(f"substantive review event must be an object for {key}")
                            continue
                        missing = REVIEW_EVENT_REQUIRED - set(event)
                        if missing:
                            errors.append(f"substantive review event missing {sorted(missing)} for {key}")
                        event_id = event.get("review_event_id")
                        if event_id in event_ids:
                            errors.append(f"duplicate substantive review event id for {key}")
                        event_ids.add(event_id)
                        event_date = parse_review_date(event.get("review_date"))
                        if event_date is None:
                            errors.append(f"invalid substantive review event date for {key}")
                        else:
                            dates.append(event_date)
                        system = event.get("review_system")
                        if not isinstance(system, dict) or any(not system.get(x) for x in ("provider", "platform", "model")):
                            errors.append(f"substantive review event requires provider/platform/model for {key}")
                        if event.get("human_role") != "contract-approver":
                            errors.append(f"substantive review event human_role must remain contract-approver for {key}")
                        if event.get("human_review_status") != "not-reviewed":
                            errors.append(f"substantive review event must not inflate human review for {key}")
                        if event.get("human_verification_status") != "not-verified":
                            errors.append(f"substantive review event must not inflate human verification for {key}")
                    if reviewed and dates and max(dates) != reviewed:
                        errors.append(f"last_substantive_reviewed must equal latest review event for {key}")
                    if provenance.get("current_review_event_id") != events[-1].get("review_event_id"):
                        errors.append(f"current_review_event_id must identify final chronological event for {key}")
                scope = scopes.get((entry.get("vigil_source_id"), entry.get("source_version")))
                if scope is None:
                    errors.append(f"substantive review provenance cannot resolve source-scope entry for {key}")
                elif isinstance(provenance.get("review_events"), list):
                    for event in provenance["review_events"]:
                        if not isinstance(event, dict):
                            continue
                        method = event.get("review_method")
                        expected = {
                            "access_method": REVIEW_METHOD_ACCESS.get(scope.get("source_access_status")),
                            "scope_method": REVIEW_METHOD_SCOPE.get(scope.get("extraction_status")),
                        }
                        if method != expected:
                            errors.append(f"substantive review method conflicts with source-scope for {key}")
            for field in ("public_summary", "relevance_scope"):
                value = entry.get(field)
                if not isinstance(value, str):
                    continue
                for label, pattern in PUBLIC_NARRATIVE_PATTERNS.items():
                    if pattern.search(value):
                        errors.append(f"{field} contains {label} for {key}")
    expected_queue = build_queue(registry)
    expected_catalogue = render_catalogue(registry)
    if check_generated:
        actual_queue = load_json(QUEUE_PATH) if QUEUE_PATH.exists() else None
        if actual_queue != expected_queue:
            errors.append("source review queue is stale; run build")
        actual_catalogue = CATALOGUE_PATH.read_text(encoding="utf-8") if CATALOGUE_PATH.exists() else ""
        if actual_catalogue != expected_catalogue:
            errors.append("source catalogue is stale; run build")
    if errors:
        raise ValueError("\n".join(errors))
    print(
        f"External source registry valid: {len(seen)} source versions, "
        f"{len(expected_queue['items'])} review-required or review-due"
    )
    for warning in warnings:
        print(f"WARNING: {warning}")


def build() -> None:
    registry = load_json(REGISTRY_PATH)
    dump_json(QUEUE_PATH, build_queue(registry))
    CATALOGUE_PATH.write_text(render_catalogue(registry), encoding="utf-8")
    validate(check_generated=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(dest="command", required=True)
    subs.add_parser("build")
    validate_parser = subs.add_parser("validate")
    validate_parser.add_argument("--check-generated", action="store_true")
    ingest_parser = subs.add_parser("ingest")
    ingest_parser.add_argument("--source", required=True)
    ingest_parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    if args.command == "build":
        build()
    elif args.command == "validate":
        validate(args.check_generated)
    else:
        ingest(args.source, args.input)


if __name__ == "__main__":
    main()
