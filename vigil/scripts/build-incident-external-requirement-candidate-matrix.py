#!/usr/bin/env python3
"""Build a deterministic, taxonomy-led candidate matrix for Incident EXTREQ assessment."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
INCIDENT_ROOT = VIGIL / "records" / "incidents"
TAXONOMY_INDEX = VIGIL / "taxonomy" / "VIGIL.FailureTaxonomy.Index.json"
DEFAULT_OUTPUT = VIGIL / "docs" / "audits" / "external-requirements"
REQUIREMENT_ID = re.compile(r"^EXTREQ-[A-F0-9]{16}$")
TEXT_REQUIREMENT_ID = re.compile(r"EXTREQ-[A-F0-9]{16}")
CURRENT_STATES = {"active", "monitoring"}
CSV_FIELDS = [
    "incident_id",
    "incident_title",
    "requirement_id",
    "external_source_id",
    "canonical_instrument",
    "source_version",
    "clause_or_control",
    "derived_from_class_ids",
    "taxonomy_reference_roles",
    "adjudication_status",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def requirement_catalogue() -> dict[str, dict[str, Any]]:
    helper_path = VIGIL / "scripts" / "external_requirements_io.py"
    spec = importlib.util.spec_from_file_location("vigil_external_requirements_io", helper_path)
    if spec is None or spec.loader is None:
        raise ValueError(f"unable to load external requirements reader: {helper_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return {item["requirement_id"]: item for item in module.load_requirements()}


def taxonomy_catalogue() -> dict[str, dict[str, Any]]:
    index = load_json(TAXONOMY_INDEX)
    classes: dict[str, dict[str, Any]] = {}
    for entry in index.get("families", []):
        if not isinstance(entry, dict) or not isinstance(entry.get("file"), str):
            continue
        path = TAXONOMY_INDEX.parent / entry["file"]
        family_document = load_json(path)
        family = family_document.get("family", {})
        for item in family_document.get("classes", []):
            if isinstance(item, dict) and isinstance(item.get("class_id"), str):
                classes[item["class_id"]] = {**item, "family_id": item.get("family_id") or family.get("family_id")}
    return classes


def incident_mappings(record: dict[str, Any]) -> dict[str, str]:
    block = record.get("taxonomy_classification")
    if not isinstance(block, dict):
        return {}
    mappings = [block.get("primary_classification")]
    secondary = block.get("secondary_classifications")
    if isinstance(secondary, list):
        mappings.extend(secondary)
    result: dict[str, str] = {}
    for mapping in mappings:
        if not isinstance(mapping, dict):
            continue
        class_id = mapping.get("class_id")
        if isinstance(class_id, str):
            result[class_id] = str(mapping.get("classification_role", "unknown"))
    return result


def citation_key(reference: dict[str, Any]) -> tuple[str, ...]:
    """Stable identity for unstructured class-level citations, excluding explanatory notes."""
    return tuple(str(reference.get(key, "")) for key in ("title", "publisher", "date", "url", "reference_role"))


def build_candidates(
    records: list[dict[str, Any]],
    classes: dict[str, dict[str, Any]],
    requirements: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    current = [record for record in records if record.get("record_state") in CURRENT_STATES]
    rows_by_pair: dict[tuple[str, str], dict[str, Any]] = {}
    mapped_incidents: set[str] = set()
    unmapped_exposures: list[tuple[str, str, dict[str, Any]]] = []
    unresolved: dict[str, dict[str, Any]] = {}
    malformed_exposures: list[tuple[str, str, Any]] = []
    context_records: list[dict[str, Any]] = []
    context_entry_count = 0
    context_requirement_ids: set[str] = set()
    taxonomy_reference_rows = [
        (class_id, reference)
        for class_id, class_record in classes.items()
        for reference in (class_record.get("external_references", []) if isinstance(class_record.get("external_references"), list) else [])
        if isinstance(reference, dict)
    ]
    unmapped_class_references = [
        (class_id, reference) for class_id, reference in taxonomy_reference_rows
        if not reference.get("requirement_id")
    ]
    structured_id_references = [
        (class_id, reference) for class_id, reference in taxonomy_reference_rows
        if isinstance(reference.get("requirement_id"), str)
        and REQUIREMENT_ID.fullmatch(reference["requirement_id"])
    ]
    unresolved_class_references = [
        (class_id, reference) for class_id, reference in structured_id_references
        if reference["requirement_id"] not in requirements
    ]
    malformed_class_references = [
        (class_id, reference.get("requirement_id")) for class_id, reference in taxonomy_reference_rows
        if reference.get("requirement_id") not in (None, "")
        and (not isinstance(reference.get("requirement_id"), str) or not REQUIREMENT_ID.fullmatch(reference["requirement_id"]))
    ]

    for record in sorted(current, key=lambda item: str(item.get("id", ""))):
        incident_id = str(record.get("id", ""))
        title = str((record.get("record_identity") or {}).get("title", ""))
        mappings = incident_mappings(record)
        if mappings:
            mapped_incidents.add(incident_id)
        for class_id in sorted(mappings):
            class_record = classes.get(class_id, {})
            refs = class_record.get("external_references", [])
            if not isinstance(refs, list):
                continue
            for reference in refs:
                if not isinstance(reference, dict):
                    continue
                requirement_id = reference.get("requirement_id")
                if requirement_id is None or requirement_id == "":
                    unmapped_exposures.append((incident_id, class_id, reference))
                    continue
                if not isinstance(requirement_id, str) or not REQUIREMENT_ID.fullmatch(requirement_id):
                    malformed_exposures.append((incident_id, class_id, requirement_id))
                    continue
                requirement = requirements.get(requirement_id)
                if requirement is None:
                    entry = unresolved.setdefault(requirement_id, {"class_ids": set(), "incident_ids": set(), "references": []})
                    entry["class_ids"].add(class_id)
                    entry["incident_ids"].add(incident_id)
                    entry["references"].append({"title": reference.get("title"), "url": reference.get("url")})
                    continue
                pair = (incident_id, requirement_id)
                candidate = rows_by_pair.setdefault(pair, {
                    "incident_id": incident_id,
                    "incident_title": title,
                    "requirement_id": requirement_id,
                    "external_source_id": str(requirement.get("external_source_id", "")),
                    "canonical_instrument": str((requirement.get("canonical_source_identifier") or {}).get("value", "")),
                    "source_version": str(requirement.get("source_version", "")),
                    "derived_from_class_ids": set(),
                    "taxonomy_reference_roles": set(),
                    "clause_or_control": set(),
                    "adjudication_status": "needs-applicability-adjudication",
                })
                candidate["derived_from_class_ids"].add(class_id)
                ref_role = reference.get("reference_role")
                if isinstance(ref_role, str) and ref_role:
                    candidate["taxonomy_reference_roles"].add(ref_role)
                clause = reference.get("clause_or_control")
                if isinstance(clause, str) and clause:
                    candidate["clause_or_control"].add(clause)

        context = record.get("standards_and_regulatory_references")
        if isinstance(context, list) and context:
            context_records.append(record)
            context_entry_count += len(context)
            for match in TEXT_REQUIREMENT_ID.findall(json.dumps(context, ensure_ascii=False)):
                context_requirement_ids.add(match)

    rows: list[dict[str, Any]] = []
    for pair in sorted(rows_by_pair):
        candidate = rows_by_pair[pair]
        rows.append({
            **candidate,
            "derived_from_class_ids": sorted(candidate["derived_from_class_ids"]),
            "taxonomy_reference_roles": sorted(candidate["taxonomy_reference_roles"]),
            "clause_or_control": sorted(candidate["clause_or_control"]),
        })

    source_breakdown: dict[str, dict[str, Any]] = {}
    for row in rows:
        source = row["external_source_id"]
        group = source_breakdown.setdefault(source, {"incident_requirement_relationships": 0, "unique_requirement_ids": set()})
        group["incident_requirement_relationships"] += 1
        group["unique_requirement_ids"].add(row["requirement_id"])
    source_breakdown = {
        source: {
            "incident_requirement_relationships": data["incident_requirement_relationships"],
            "unique_requirement_ids": len(data["unique_requirement_ids"]),
        }
        for source, data in sorted(source_breakdown.items())
    }

    candidate_incident_ids = {row["incident_id"] for row in rows}
    summary = {
        "current_incident_records": len(current),
        "canonical_requirement_records": len(requirements),
        "record_state_breakdown": {
            state: sum(record.get("record_state") == state for record in current)
            for state in sorted({str(record.get("record_state")) for record in current})
        },
        "taxonomy_mapped_incidents": len(mapped_incidents),
        "unique_incident_requirement_relationships": len(rows),
        "unique_requirement_ids": len({row["requirement_id"] for row in rows}),
        "relationships_derived_from_multiple_fidelity_classes": sum(len(row["derived_from_class_ids"]) > 1 for row in rows),
        "taxonomy_external_reference_rows": len(taxonomy_reference_rows),
        "taxonomy_references_with_valid_structured_ids": len(structured_id_references),
        "unresolved_structured_taxonomy_reference_rows": len(unresolved_class_references),
        "unmapped_external_reference_rows_without_requirement_id": len(unmapped_class_references),
        "unique_unmapped_class_citations": len({citation_key(item[1]) for item in unmapped_class_references}),
        "incident_exposures_through_unmapped_references": len(unmapped_exposures),
        "malformed_requirement_id_reference_rows": len(malformed_class_references),
        "incident_exposures_through_malformed_references": len(malformed_exposures),
        "unresolved_structured_requirement_ids": {
            key: {
                "mapped_class_ids": sorted(value["class_ids"]),
                "incident_ids": sorted(value["incident_ids"]),
                "incident_count": len(value["incident_ids"]),
                "mapped_class_exposure_count": len(value["references"]),
            }
            for key, value in sorted(unresolved.items())
        },
        "source_breakdown": source_breakdown,
        "standards_and_regulatory_context_overlap": {
            "incidents_with_context_references": len(context_records),
            "context_reference_entries": context_entry_count,
            "context_incidents_also_in_candidate_matrix": sum(record.get("id") in candidate_incident_ids for record in context_records),
            "explicit_requirement_ids_in_context_text_only": sorted(context_requirement_ids),
            "context_references_drive_candidate_generation": False,
        },
    }
    return rows, summary


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({
                **row,
                "derived_from_class_ids": ";".join(row["derived_from_class_ids"]),
                "taxonomy_reference_roles": ";".join(row["taxonomy_reference_roles"]),
                "clause_or_control": ";".join(row["clause_or_control"]),
            })


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_OUTPUT / "incident-requirement-candidate-matrix.csv")
    parser.add_argument("--summary", type=Path, default=DEFAULT_OUTPUT / "incident-requirement-candidate-summary.json")
    args = parser.parse_args()

    records = [load_json(path) for path in sorted(INCIDENT_ROOT.glob("*.json"))]
    classes = taxonomy_catalogue()
    requirements = requirement_catalogue()
    rows, summary = build_candidates(records, classes, requirements)
    write_csv(args.csv, rows)
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
