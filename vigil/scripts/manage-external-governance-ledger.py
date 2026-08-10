#!/usr/bin/env python3
"""Deterministic external-governance source ledger maintenance.

This script never performs substantive CAM alignment and never edits Caelestis.
It consumes already-normalised source items, canonicalises state, fingerprints
material metadata, updates the maintenance ledger, and regenerates the review queue.
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
LEDGER_PATH = EXT / "ledger.json"
QUEUE_PATH = EXT / "alignment-queue.json"

ALIGNMENT_STATES = {
    "unassigned", "review-required", "mapped", "patch-required", "patched",
    "verified", "no-change-required", "not-applicable", "superseded-before-review",
}
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


def lifecycle_eligible(source: dict[str, Any], lifecycle: str) -> bool:
    eligible = {normalise_state(v) for v in source.get("alignment_eligible_states", [])}
    return normalise_state(lifecycle) in eligible


def material_projection(item: dict[str, Any]) -> dict[str, Any]:
    keys = (
        "external_source_id", "source_version", "canonical_identifier", "title", "issuer",
        "jurisdiction", "source_class", "source_lifecycle_state", "publication_date",
        "effective_date", "official_locator", "upstream_record_id", "upstream_release",
    )
    return {key: item.get(key) for key in keys}


def fingerprint(item: dict[str, Any]) -> str:
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

    now = utc_now()
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
        "fingerprint": "",
        "change_state": "new",
        "alignment_state": "unassigned",
        "alignment_eligible": False,
        "caelestis_assessed_commit": None,
        "caelestis_crosswalk_refs": [],
        "first_seen": raw.get("observed_at") or now,
        "last_seen": raw.get("observed_at") or now,
        "notes": raw.get("notes"),
    }
    item["alignment_eligible"] = lifecycle_eligible(source, item["source_lifecycle_state"])
    item["fingerprint"] = fingerprint(item)
    if item["alignment_eligible"]:
        item["alignment_state"] = "review-required"
    return item


def entry_key(item: dict[str, Any]) -> tuple[str, str]:
    return str(item["external_source_id"]), str(item["source_version"])


def merge_item(existing: dict[str, Any] | None, incoming: dict[str, Any]) -> dict[str, Any]:
    if existing is None:
        return incoming

    merged = dict(incoming)
    merged["first_seen"] = existing["first_seen"]
    merged["last_seen"] = incoming["last_seen"]
    merged["caelestis_assessed_commit"] = existing.get("caelestis_assessed_commit")
    merged["caelestis_crosswalk_refs"] = existing.get("caelestis_crosswalk_refs", [])

    if existing.get("fingerprint") == incoming.get("fingerprint"):
        merged["change_state"] = "unchanged"
        merged["alignment_state"] = existing.get("alignment_state", incoming["alignment_state"])
    else:
        state = incoming["source_lifecycle_state"]
        if state in {"withdrawn", "revoked"}:
            merged["change_state"] = "withdrawn"
        elif state in {"superseded", "replaced"}:
            merged["change_state"] = "superseded"
        else:
            merged["change_state"] = "changed"

        if incoming["alignment_eligible"]:
            # A materially changed final/adopted source must be reviewed again.
            merged["alignment_state"] = "review-required"
        else:
            # Draft/consultation changes do not erase an existing human disposition.
            merged["alignment_state"] = existing.get("alignment_state", "unassigned")

    return merged


def ingest(source_id: str, input_path: Path) -> None:
    sources = source_map()
    if source_id not in sources:
        raise ValueError(f"unknown source_id: {source_id}")
    source = sources[source_id]
    raw = load_json(input_path)
    if not isinstance(raw, list):
        raise ValueError("ingest input must be a JSON array of normalised source items")

    ledger = load_json(LEDGER_PATH)
    current = {entry_key(item): item for item in ledger.get("entries", [])}
    for raw_item in raw:
        incoming = canonicalise(raw_item, source_id, source)
        key = entry_key(incoming)
        current[key] = merge_item(current.get(key), incoming)

    ledger["updated_at"] = utc_now()
    ledger["entries"] = sorted(current.values(), key=lambda x: (x["external_source_id"], x["source_version"]))
    dump_json(LEDGER_PATH, ledger)
    build_queue()


def build_queue() -> None:
    ledger = load_json(LEDGER_PATH)
    items = []
    for entry in ledger.get("entries", []):
        if entry.get("alignment_state") != "review-required":
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
            "fingerprint": entry["fingerprint"],
            "required_action": "human-semantic-alignment-review",
        })
    dump_json(QUEUE_PATH, {"schema_version": "1.0", "generated_at": utc_now(), "items": items})


def validate() -> None:
    matrix = load_json(MATRIX_PATH)
    ledger = load_json(LEDGER_PATH)
    queue = load_json(QUEUE_PATH)
    source_ids = [s["source_id"] for s in matrix.get("sources", [])]
    if len(source_ids) != len(set(source_ids)):
        raise ValueError("duplicate source_id in source matrix")
    if "vorp" in json.dumps(matrix).lower() and not matrix.get("design_rules", {}).get("vorp_labs_excluded"):
        raise ValueError("Vorp provenance boundary is not explicit")
    seen = set()
    for entry in ledger.get("entries", []):
        key = entry_key(entry)
        if key in seen:
            raise ValueError(f"duplicate ledger key: {key}")
        seen.add(key)
        if entry.get("alignment_state") not in ALIGNMENT_STATES:
            raise ValueError(f"invalid alignment_state for {key}")
        if entry.get("change_state") not in CHANGE_STATES:
            raise ValueError(f"invalid change_state for {key}")
        if entry.get("fingerprint") != fingerprint(entry):
            raise ValueError(f"fingerprint mismatch for {key}")
    expected = {(e["external_source_id"], e["source_version"]) for e in ledger.get("entries", []) if e.get("alignment_state") == "review-required"}
    actual = {(e["external_source_id"], e["source_version"]) for e in queue.get("items", [])}
    if expected != actual:
        raise ValueError("alignment queue is stale; run queue")
    print(f"External governance ledger valid: {len(seen)} entries, {len(actual)} review-required")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    sub.add_parser("queue")
    ingest_p = sub.add_parser("ingest")
    ingest_p.add_argument("--source", required=True)
    ingest_p.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()

    if args.command == "validate":
        validate()
    elif args.command == "queue":
        build_queue()
        validate()
    elif args.command == "ingest":
        ingest(args.source, args.input)
        validate()


if __name__ == "__main__":
    main()
