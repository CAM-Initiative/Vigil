#!/usr/bin/env python3
"""Validate the lightweight Incident public index and registry manifest."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
INCIDENTS = VIGIL / "records" / "incidents"
INCIDENT_INDEX = VIGIL / "VIGIL.Incidents.Index.json"
MASTER_INDEX = VIGIL / "VIGIL.Registry.Index.json"
REPOSITORY = "CAM-Initiative/Vigil"
BRANCH = "main"
RETIRED_INDEXES = (
    "VIGIL.Failures.Index.json", "VIGIL.Observations.Index.json", "VIGIL.Research.Index.json",
    "VIGIL.Proposals.Index.json", "VIGIL.PatchNotes.Index.json", "VIGIL.Learn.Index.json",
)
INDEX_ENTRY_KEYS = {
    "id",
    "record_type",
    "record_state",
    "record_version",
    "record_last_updated",
    "date_recorded",
    "title",
    "summary",
    "platform_or_vendor",
    "severity",
    "classification_status",
    "primary_class_id",
    "primary_family_id",
    "occurred_from",
    "search_terms",
    "path",
    "github_blob_url",
    "raw_url",
}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("expected one JSON object")
    return value


def canonical_records() -> dict[str, dict[str, Any]]:
    return {
        record["id"]: record
        for path in sorted(INCIDENTS.glob("VIGIL-INC-*.json"))
        if isinstance((record := load(path)).get("id"), str)
    }


def expected_projection(record: dict[str, Any]) -> dict[str, Any]:
    identity = record.get("record_identity") if isinstance(record.get("record_identity"), dict) else {}
    incident = record.get("incident_identity") if isinstance(record.get("incident_identity"), dict) else {}
    system = record.get("system_context") if isinstance(record.get("system_context"), dict) else {}
    taxonomy = record.get("taxonomy_classification") if isinstance(record.get("taxonomy_classification"), dict) else {}
    assessment = record.get("severity_assessment") if isinstance(record.get("severity_assessment"), dict) else {}
    primary = taxonomy.get("primary_classification") if isinstance(taxonomy.get("primary_classification"), dict) else {}
    if not primary:
        legacy_primary_class = taxonomy.get("primary_class")
        primary = legacy_primary_class if isinstance(legacy_primary_class, dict) else {}
    primary_family = taxonomy.get("primary_family") if isinstance(taxonomy.get("primary_family"), dict) else {}
    record_id = str(record["id"])
    path = f"vigil/records/incidents/{record_id}.json"
    return {
        "id": record_id,
        "record_type": "incident",
        "record_state": record.get("record_state"),
        "record_version": identity.get("version"),
        "record_last_updated": identity.get("updated"),
        "date_recorded": record.get("date_recorded"),
        "title": identity.get("title") or record.get("summary") or record_id,
        "summary": record.get("summary"),
        "platform_or_vendor": system.get("platform_or_vendor"),
        "severity": assessment.get("severity"),
        "classification_status": taxonomy.get("classification_status"),
        "primary_class_id": primary.get("class_id"),
        "primary_family_id": primary.get("family_id") or primary_family.get("family_id"),
        "occurred_from": incident.get("occurred_from"),
        "path": path,
        "github_blob_url": f"https://github.com/{REPOSITORY}/blob/{BRANCH}/{path}",
        "raw_url": f"https://raw.githubusercontent.com/{REPOSITORY}/{BRANCH}/{path}",
    }


def validate_generated_incident_projection(
    records_by_id: dict[str, dict[str, Any]],
    errors: list[str],
    index_path: Path | None = None,
) -> None:
    path = index_path or INCIDENT_INDEX
    try:
        index = load(path)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path}: unable to read generated index: {exc}")
        return

    entries = {
        item.get("id"): item
        for item in index.get("records", [])
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    if set(entries) != set(records_by_id):
        errors.append(f"{path}: generated Incident IDs do not exactly match canonical records")

    for record_id, record in records_by_id.items():
        entry = entries.get(record_id)
        if entry is None:
            continue

        unexpected = set(entry) - INDEX_ENTRY_KEYS
        if unexpected:
            errors.append(f"{path}: {record_id} contains non-index fields: {sorted(unexpected)}")

        expected = expected_projection(record)
        for key, value in expected.items():
            if value in (None, "", [], {}):
                if key in entry:
                    errors.append(f"{path}: {record_id} retains empty projected field {key}")
                continue
            if entry.get(key) != value:
                errors.append(f"{path}: {record_id} {key} disagrees with the canonical record")

        search_terms = entry.get("search_terms")
        if not isinstance(search_terms, list) or not search_terms or not all(
            isinstance(item, str) and item.strip() for item in search_terms
        ):
            errors.append(f"{path}: {record_id} search_terms must be a non-empty string array")

        for forbidden in (
            "source_records",
            "severity_assessment",
            "primary_classification",
            "secondary_classifications",
            "diagnostic_provenance_summary",
            "interpretive_provenance_summary",
            "evidence_access_summary",
            "external_incident_references",
            "legacy_provenance",
        ):
            if forbidden in entry:
                errors.append(f"{path}: {record_id} embeds canonical detail field {forbidden}")


def main() -> int:
    errors: list[str] = []
    for filename in RETIRED_INDEXES:
        if (VIGIL / filename).exists():
            errors.append(f"{VIGIL / filename}: retired record-class index must not exist")

    records = canonical_records()
    validate_generated_incident_projection(records, errors, INCIDENT_INDEX)

    try:
        incident_index = load(INCIDENT_INDEX)
        master = load(MASTER_INDEX)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"generated index parse failed: {exc}")
    else:
        if incident_index.get("registry_type") != "incidents":
            errors.append("VIGIL.Incidents.Index.json registry_type must be incidents")
        if incident_index.get("record_count") != len(records):
            errors.append("VIGIL.Incidents.Index.json record_count is stale")
        if master.get("registry_count") != 1 or set(master.get("registries", {})) != {"incidents"}:
            errors.append("VIGIL.Registry.Index.json must expose only the Incident registry")
        if master.get("record_count") != {"incidents": len(records), "total": len(records)}:
            errors.append("VIGIL.Registry.Index.json record_count is stale")
        if "records" in master:
            errors.append("VIGIL.Registry.Index.json must remain a registry manifest and must not duplicate Incident records")
        incident_manifest = master.get("registries", {}).get("incidents", {})
        if not isinstance(incident_manifest, dict):
            errors.append("VIGIL.Registry.Index.json incidents registry entry must be an object")
        else:
            if incident_manifest.get("path") != "vigil/VIGIL.Incidents.Index.json":
                errors.append("VIGIL.Registry.Index.json incidents path is incorrect")
            if incident_manifest.get("record_count") != len(records):
                errors.append("VIGIL.Registry.Index.json incidents record_count is stale")

    if errors:
        print("VIGIL public Incident index validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"VIGIL lightweight public Incident index validation passed: {len(records)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
