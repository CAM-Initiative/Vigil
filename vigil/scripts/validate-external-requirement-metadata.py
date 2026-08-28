#!/usr/bin/env python3
"""Validate EXTREQ metadata review-state coverage and generate a source-level review queue."""
from __future__ import annotations
import argparse, json
from collections import Counter, defaultdict
from pathlib import Path

from external_requirements_io import load_requirements_document

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_requirements"
LEDGER = REQ / "metadata-review.json"
BACKLOG = REQ / "reextraction-backlog.json"
SOURCE_SCOPE = REQ / "source-scope.json"
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
            clone["_staged_package"] = path.name
            clone.setdefault("vigil_source_id", doc.get("source", {}).get("vigil_source_id"))
            clone.setdefault("external_source_id", doc.get("source", {}).get("external_source_id"))
            clone.setdefault("source_version", doc.get("source", {}).get("source_version"))
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


def source_key(record):
    return "|".join((
        str(record.get("vigil_source_id") or "<missing-source>"),
        str(record.get("source_version") or "<missing-version>"),
    ))


def validate(strict: bool, write_report: bool) -> int:
    canonical = load_requirements_document().get("requirements", [])
    staged = staged_records()
    ledger_doc = load(LEDGER)
    entries = ledger_doc.get("entries", [])
    backlog_doc = load(BACKLOG) if BACKLOG.exists() else {"entries": []}
    backlog_entries = backlog_doc.get("entries", [])
    source_scope = load(SOURCE_SCOPE).get("entries", [])
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
    canonical_by_id = {r.get("requirement_id"): r for r in canonical}
    for rid in sorted(set(entry_by_id) - record_ids):
        errors.append(f"metadata-review entry does not resolve to canonical or staged requirement: {rid}")

    backlog_by_id = {}
    for backlog_entry in backlog_entries:
        rid = backlog_entry.get("current_requirement_id")
        if rid in backlog_by_id:
            errors.append(f"duplicate re-extraction backlog entry {rid}")
            continue
        backlog_by_id[rid] = backlog_entry
        record = canonical_by_id.get(rid)
        if record is None:
            errors.append(f"re-extraction backlog entry does not resolve to canonical requirement: {rid}")
            continue
        for field in ("vigil_source_id", "external_source_id", "source_version", "clause_or_control"):
            if backlog_entry.get(field) != record.get(field):
                errors.append(f"{rid} re-extraction backlog {field} differs from canonical requirement")
        affected = backlog_entry.get("affected_metadata_dimensions", [])
        unknown = sorted(set(affected) - set(FIELDS))
        if unknown:
            errors.append(f"{rid} re-extraction backlog has unknown metadata dimensions: {unknown}")
        ledger_entry = entry_by_id.get(rid)
        for field in affected:
            if ledger_entry and ledger_entry.get("field_status", {}).get(field) != "review-required":
                errors.append(f"{rid} {field}: re-extraction-affected field must remain review-required")

    for surface, record in all_records:
        rid = record.get("requirement_id", "<missing>")
        entry = entry_by_id.get(rid)
        field_states = {}
        field_observations = {}
        unresolved = []
        for field in FIELDS:
            value = record.get(field, [])
            status = entry.get("field_status", {}).get(field) if entry else "review-required"
            field_states[field] = status
            populated = isinstance(value, list) and len(value) > 0
            field_observations[field] = "populated" if populated else "empty"
            if status == "populated-reviewed" and not populated:
                errors.append(f"{rid} {field}: populated-reviewed but field is empty")
            if status in {"not-specified-by-source", "not-applicable"} and populated:
                errors.append(f"{rid} {field}: {status} but field contains values")
            if status == "review-required":
                unresolved.append(field)
        rows.append({
            "requirement_id": rid,
            "surface": surface,
            "source_key": source_key(record),
            "vigil_source_id": record.get("vigil_source_id"),
            "external_source_id": record.get("external_source_id"),
            "source_version": record.get("source_version"),
            "clause_or_control": record.get("clause_or_control"),
            "staged_package": record.get("_staged_package"),
            "unresolved_fields": unresolved,
            "metadata_complete": not unresolved,
            "field_status": field_states,
            "field_observation": field_observations,
        })

    summary = Counter()
    field_summary = {field: Counter() for field in FIELDS}
    by_source = defaultdict(lambda: {
        "records": 0,
        "metadata_complete": 0,
        "review_required_records": 0,
        "review_required_fields": 0,
        "field_counts": {field: Counter() for field in FIELDS},
        "reextraction_records": 0,
    })
    for row in rows:
        summary["records"] += 1
        summary["canonical_records"] += row["surface"] == "canonical"
        summary["staged_records"] += row["surface"] == "staged"
        summary["metadata_complete"] += row["metadata_complete"]
        if not row["metadata_complete"]:
            summary["review_required_records"] += 1
        summary["review_required_fields"] += len(row["unresolved_fields"])
        source = by_source[row["source_key"]]
        source["records"] += 1
        source["metadata_complete"] += row["metadata_complete"]
        source["review_required_records"] += bool(row["unresolved_fields"])
        source["review_required_fields"] += len(row["unresolved_fields"])
        source["reextraction_records"] += row["requirement_id"] in backlog_by_id
        for field in FIELDS:
            status = row["field_status"][field]
            observation = row["field_observation"][field]
            source["field_counts"][field][f"{status}:{observation}"] += 1
            field_summary[field][f"{status}:{observation}"] += 1

    summary["reextraction_backlog_entries"] = len(backlog_entries)
    summary["records_flagged_for_reextraction"] = len(backlog_by_id)
    defect_categories = Counter(
        defect
        for entry in backlog_entries
        for defect in entry.get("detected_fidelity_defects", [])
    )

    source_summary = []
    for key, value in sorted(by_source.items(), key=lambda item: (-item[1]["review_required_fields"], item[0])):
        if value["metadata_complete"] == value["records"]:
            review_status = "fully-metadata-reviewed"
        elif value["metadata_complete"] or value["review_required_fields"] < value["records"] * len(FIELDS):
            review_status = "partially-metadata-reviewed"
        else:
            review_status = "unreviewed"
        source_summary.append({
            "source_key": key,
            "records": value["records"],
            "metadata_complete": value["metadata_complete"],
            "review_required_records": value["review_required_records"],
            "review_required_fields": value["review_required_fields"],
            "review_status": review_status,
            "reextraction_records": value["reextraction_records"],
            "field_counts": {field: dict(counts) for field, counts in value["field_counts"].items()},
        })

    represented_source_keys = set(by_source)
    blocked_sources = []
    for source in source_scope:
        key = "|".join((str(source.get("vigil_source_id")), str(source.get("source_version"))))
        if source.get("source_role") != "primary-ai-governance":
            continue
        if source.get("extraction_status") == "blocked-access" or source.get("source_access_status") in {
            "official-metadata-only", "secondary-source-only", "source-unavailable"
        }:
            blocked_sources.append({
                "source_key": key,
                "external_source_id": source.get("external_source_id"),
                "source_access_status": source.get("source_access_status"),
                "extraction_status": source.get("extraction_status"),
                "represented_in_report": key in represented_source_keys,
            })

    report = {
        "schema_version": "1.1",
        "summary": dict(summary),
        "errors": errors,
        "field_summary": {field: dict(counts) for field, counts in field_summary.items()},
        "reextraction_defect_categories": dict(sorted(defect_categories.items())),
        "blocked_sources": sorted(blocked_sources, key=lambda item: item["source_key"]),
        "source_summary": source_summary,
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
            f"- Records flagged for re-extraction: {summary['records_flagged_for_reextraction']}",
            f"- Primary sources blocked by access: {len(blocked_sources)}",
            f"- Contract errors: {len(errors)}",
            "",
            "## Field-level decision state",
            "",
            "| Field | Populated, reviewed | Populated, unreviewed | Empty, unreviewed | Not specified by source | Not applicable |",
            "|---|---:|---:|---:|---:|---:|",
        ]
        for field in FIELDS:
            counts = field_summary[field]
            lines.append(
                f"| `{field}` | {counts['populated-reviewed:populated']} | "
                f"{counts['review-required:populated']} | {counts['review-required:empty']} | "
                f"{counts['not-specified-by-source:empty']} | {counts['not-applicable:empty']} |"
            )
        lines.extend([
            "",
            "## Source-level review backlog",
            "",
            "| Source/version | Status | Records | Complete | Records requiring review | Unresolved fields | Re-extraction |",
            "|---|---|---:|---:|---:|---:|---:|",
        ])
        for source in source_summary:
            lines.append(
                f"| `{source['source_key']}` | `{source['review_status']}` | {source['records']} | "
                f"{source['metadata_complete']} | {source['review_required_records']} | "
                f"{source['review_required_fields']} | {source['reextraction_records']} |"
            )
        lines.extend([
            "",
            "## Re-extraction findings",
            "",
            f"- Backlog records: {len(backlog_entries)}",
        ])
        for defect, count in sorted(defect_categories.items()):
            lines.append(f"- `{defect}`: {count}")
        lines.extend([
            "",
            "## Primary sources blocked by access",
            "",
            "| Source/version | Access | Extraction | Represented requirements |",
            "|---|---|---|---|",
        ])
        for source in blocked_sources:
            lines.append(
                f"| `{source['source_key']}` | `{source['source_access_status']}` | "
                f"`{source['extraction_status']}` | {'yes' if source['represented_in_report'] else 'no'} |"
            )
        lines.extend([
            "",
            "## Requirement-level review queue",
            "",
            "| Requirement | Source/version | Surface | Clause/control | Fields requiring review |",
            "|---|---|---|---|---|",
        ])
        for row in report["review_queue"]:
            lines.append(
                f"| `{row['requirement_id']}` | `{row['source_key']}` | {row['surface']} | "
                f"{row.get('clause_or_control') or ''} | {', '.join(row['unresolved_fields'])} |"
            )
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
