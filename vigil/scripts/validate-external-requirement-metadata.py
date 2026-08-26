#!/usr/bin/env python3
"""Validate EXTREQ metadata review-state coverage and generate a review queue."""
from __future__ import annotations
import argparse, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_requirements"
CANONICAL = REQ / "requirements.json"
LEDGER = REQ / "metadata-review.json"
REEXTRACTIONS = REQ / "reextractions"
REPORT_JSON = REQ / "metadata-review-report.json"
REPORT_MD = REQ / "METADATA-REVIEW-REPORT.md"

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
STATUSES = {
    "populated-reviewed",
    "not-specified-by-source",
    "not-applicable",
    "review-required",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def staged_records():
    records = []
    for path in sorted(REEXTRACTIONS.glob("EU-AI-ACT-2026-07-27-*.json")):
        if path.name.endswith("metadata-normalization.json"):
            continue
        doc = load(path)
        for record in doc.get("requirements", []):
            clone = {**record}
            for field in FIELDS:
                clone.setdefault(field, [])
            records.append(clone)
    overlay_path = REEXTRACTIONS / "EU-AI-ACT-2026-07-27-metadata-normalization.json"
    if overlay_path.exists():
        overlay = load(overlay_path).get("overrides", {})
        by_id = {r["requirement_id"]: r for r in records}
        for rid, patch in overlay.items():
            if rid in by_id:
                for field, value in patch.items():
                    if field in FIELDS:
                        by_id[rid][field] = value
    return records


def validate(strict: bool, write_report: bool) -> int:
    canonical = load(CANONICAL).get("requirements", [])
    staged = staged_records()
    ledger_doc = load(LEDGER)
    entries = ledger_doc.get("entries", [])
    errors = []
    entry_by_id = {}
    for entry in entries:
        rid = entry.get("requirement_id")
        if rid in entry_by_id:
            errors.append(f"duplicate metadata-review entry {rid}")
            continue
        entry_by_id[rid] = entry
        statuses = entry.get("field_status", {})
        for field in FIELDS:
            if statuses.get(field) not in STATUSES:
                errors.append(f"{rid} invalid or missing review state for {field}")

    rows = []
    all_records = [("canonical", r) for r in canonical] + [("staged", r) for r in staged]
    record_ids = {r.get("requirement_id") for _, r in all_records}
    for rid in sorted(set(entry_by_id) - record_ids):
        errors.append(f"metadata-review entry does not resolve to canonical or staged requirement: {rid}")

    for surface, record in all_records:
        rid = record.get("requirement_id", "<missing>")
        entry = entry_by_id.get(rid)
        field_states = {}
        unresolved = []
        for field in FIELDS:
            value = record.get(field, [])
            status = entry.get("field_status", {}).get(field) if entry else "review-required"
            field_states[field] = status
            populated = isinstance(value, list) and len(value) > 0
            if status == "populated-reviewed" and not populated:
                errors.append(f"{rid} {field}: populated-reviewed but field is empty")
            if status in {"not-specified-by-source", "not-applicable"} and populated:
                errors.append(f"{rid} {field}: {status} but field contains values")
            if status == "review-required":
                unresolved.append(field)
        rows.append({
            "requirement_id": rid,
            "surface": surface,
            "unresolved_fields": unresolved,
            "metadata_complete": not unresolved,
            "field_status": field_states,
        })

    summary = Counter()
    for row in rows:
        summary["records"] += 1
        summary["canonical_records"] += row["surface"] == "canonical"
        summary["staged_records"] += row["surface"] == "staged"
        summary["metadata_complete"] += row["metadata_complete"]
        if not row["metadata_complete"]:
            summary["review_required_records"] += 1
        summary["review_required_fields"] += len(row["unresolved_fields"])

    report = {
        "schema_version": "1.0",
        "summary": dict(summary),
        "errors": errors,
        "review_queue": [r for r in rows if r["unresolved_fields"]],
    }
    if write_report:
        REPORT_JSON.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        lines = [
            "# External Requirement Metadata Review Report",
            "",
            f"- Records assessed: {summary['records']}",
            f"- Canonical records: {summary['canonical_records']}",
            f"- Staged records: {summary['staged_records']}",
            f"- Metadata-complete: {summary['metadata_complete']}",
            f"- Records requiring review: {summary['review_required_records']}",
            f"- Unresolved field decisions: {summary['review_required_fields']}",
            f"- Contract errors: {len(errors)}",
            "",
            "## Review queue",
            "",
            "| Requirement | Surface | Fields requiring review |",
            "|---|---|---|",
        ]
        for row in report["review_queue"]:
            lines.append(f"| `{row['requirement_id']}` | {row['surface']} | {', '.join(row['unresolved_fields'])} |")
        REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps(report["summary"], indent=2))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    if strict and summary["review_required_fields"]:
        print("ERROR: strict metadata review validation failed: unresolved review-required fields remain")
        return 2
    print("External requirement metadata review contract valid")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    raise SystemExit(validate(args.strict, args.write_report))


if __name__ == "__main__":
    main()
