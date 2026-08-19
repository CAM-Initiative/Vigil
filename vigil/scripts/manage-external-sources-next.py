#!/usr/bin/env python3
"""Maintain VIGIL's canonical external governance source registry.

This module records external-source identity, version, lifecycle, change state and
source-review workflow. It does not assess CAM applicability and it never edits CAM.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXT = ROOT / "external_sources"
MATRIX_PATH = EXT / "source-matrix.json"
REGISTRY_PATH = EXT / "source-registry.json"
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


def build_queue(registry: dict[str, Any] | None = None) -> dict[str, Any]:
    registry = registry or load_json(REGISTRY_PATH)
    items = []
    for entry in registry.get("entries", []):
        if entry.get("review_state") != "review-required":
            continue
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
            "required_action": "semantic-source-review",
        })
    return {
        "schema_version": "1.0",
        "generated_at": registry.get("updated_at"),
        "authorship_provenance": GENERATED_PROVENANCE,
        "items": items,
    }


def render_catalogue(registry: dict[str, Any] | None = None) -> str:
    registry = registry or load_json(REGISTRY_PATH)
    entries = sorted(registry.get("entries", []), key=lambda x: (x["external_source_id"], x["source_version"]))
    lines = [
        "# External Governance Sources", "",
        "Canonical VIGIL registry of external governance source identities and versions. Inclusion is inventory only and does not assert CAM applicability, coverage, compliance, conformance or alignment.", "",
        f"- Source versions: {len(entries)}",
        f"- Updated through: {registry.get('updated_at')}", "",
        "| VIGIL Source | External Source | Version | Issuer | Lifecycle | Review state | Canonical identifier | Metadata fingerprint |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        lines.append(
            f"| `{entry['vigil_source_id']}` | {entry.get('title') or ''} | `{entry['source_version']}` | {entry['issuer']} | "
            f"`{entry['source_lifecycle_state']}` | `{entry['review_state']}` | `{entry['canonical_identifier']['value']}` | "
            f"`{entry['source_metadata_fingerprint'][:12]}…` |"
        )
    lines += [
        "",
        "The metadata fingerprint is a SHA-256 of VIGIL's material source-metadata projection. It is not a digest of a reviewed PDF, HTML capture or licensed standard artefact.",
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
        if entry.get("review_eligible") is not isinstance(entry.get("review_eligible"), bool):
            errors.append(f"review_eligible must be boolean for {key}")
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
    print(f"External source registry valid: {len(seen)} source versions, {len(expected_queue['items'])} review-required")


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
