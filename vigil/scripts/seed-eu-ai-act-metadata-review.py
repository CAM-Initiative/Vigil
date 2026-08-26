#!/usr/bin/env python3
"""Seed metadata-review decisions for source-reviewed staged EU AI Act requirements.

This script is intentionally limited to the 27 July 2026 EU AI Act staged
re-extraction packages. It never treats existing canonical values as reviewed
merely because they are populated.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_requirements"
LEDGER = REQ / "metadata-review.json"
REEXTRACTIONS = REQ / "reextractions"

FIELDS = (
    "applicable_actor",
    "governed_object",
    "timing_or_frequency",
    "required_artefacts",
    "evidence_expectation",
    "verification_method",
    "applicability_conditions",
    "exceptions_or_qualifications",
)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def reviewed_staged_records():
    records = []
    for path in sorted(REEXTRACTIONS.glob("EU-AI-ACT-2026-07-27-*.json")):
        if path.name.endswith("metadata-normalization.json"):
            continue
        doc = load(path)
        if doc.get("status") != "migration-candidate":
            raise ValueError(f"unexpected staged package status in {path.name}")
        if doc.get("source", {}).get("source_version") != "2026-07-27":
            raise ValueError(f"unexpected EU AI Act source version in {path.name}")
        for record in doc.get("requirements", []):
            clone = {**record}
            for field in FIELDS:
                clone.setdefault(field, [])
            records.append(clone)
    overlay_path = REEXTRACTIONS / "EU-AI-ACT-2026-07-27-metadata-normalization.json"
    overlay = load(overlay_path).get("overrides", {}) if overlay_path.exists() else {}
    by_id = {r["requirement_id"]: r for r in records}
    for rid, patch in overlay.items():
        if rid not in by_id:
            raise ValueError(f"metadata overlay refers to unknown staged EU AI Act requirement {rid}")
        for field, value in patch.items():
            if field in FIELDS:
                by_id[rid][field] = value
    return records


def seed(write: bool) -> int:
    ledger = load(LEDGER)
    records = reviewed_staged_records()
    existing = {entry["requirement_id"]: entry for entry in ledger.get("entries", [])}
    seeded = 0
    for record in records:
        rid = record["requirement_id"]
        field_status = {}
        for field in FIELDS:
            value = record.get(field, [])
            field_status[field] = "populated-reviewed" if isinstance(value, list) and value else "not-specified-by-source"
        entry = {
            "requirement_id": rid,
            "reviewed_at": "2026-08-26",
            "review_basis": "direct-primary-text",
            "review_notes": [
                "Reviewed against the authoritative 27 July 2026 consolidated EU AI Act during semantic re-extraction and metadata-normalisation.",
                "Empty fidelity-critical fields are recorded as not-specified-by-source; this seeder does not infer not-applicable automatically."
            ],
            "field_status": field_status,
        }
        current = existing.get(rid)
        if current is not None and current != entry:
            raise ValueError(f"existing metadata-review decision differs for {rid}; manual reconciliation required")
        if current is None:
            existing[rid] = entry
            seeded += 1
    output = {
        "schema_version": ledger.get("schema_version", "1.0"),
        "updated_at": "2026-08-26",
        "entries": sorted(existing.values(), key=lambda x: x["requirement_id"]),
    }
    print(f"EU AI Act metadata-review seed valid: {len(records)} staged requirements; {seeded} new ledger entries")
    if write:
        LEDGER.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {LEDGER}")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    raise SystemExit(seed(args.write))


if __name__ == "__main__":
    main()
