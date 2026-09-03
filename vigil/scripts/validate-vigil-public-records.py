#!/usr/bin/env python3
"""Validate the Incident-only generated public VIGIL indexes."""

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
RETIRED_INDEXES = (
    "VIGIL.Failures.Index.json", "VIGIL.Observations.Index.json", "VIGIL.Research.Index.json",
    "VIGIL.Proposals.Index.json", "VIGIL.PatchNotes.Index.json", "VIGIL.Learn.Index.json",
)


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


def validate_generated_incident_evidence_facets(
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
        sources = [item for item in record.get("source_records", []) if isinstance(item, dict)]
        expected_statuses = sorted({str(item["evidence_status"]) for item in sources if item.get("evidence_status")})
        if entry.get("evidence_statuses") != expected_statuses:
            errors.append(f"{path}: {record_id} evidence_statuses disagree with canonical sources")
        preferred_url = record.get("preferred_evidence", {}).get("source_url")
        matches = [item for item in sources if item.get("source_url") == preferred_url]
        expected_preferred = matches[0].get("evidence_status") if len(matches) == 1 else None
        if entry.get("preferred_evidence_status") != expected_preferred:
            errors.append(f"{path}: {record_id} preferred_evidence_status is not deterministic")
        if entry.get("severity_assessment") != record.get("severity_assessment"):
            errors.append(f"{path}: {record_id} structured severity differs from canonical record")
        if "evidence_confidence" in entry:
            errors.append(f"{path}: {record_id} retains retired Incident evidence_confidence")
        if entry.get("record_type") != "incident":
            errors.append(f"{path}: {record_id} is not projected as an Incident")


def main() -> int:
    errors: list[str] = []
    for filename in RETIRED_INDEXES:
        if (VIGIL / filename).exists():
            errors.append(f"{VIGIL / filename}: retired record-class index must not exist")
    records = canonical_records()
    validate_generated_incident_evidence_facets(records, errors, INCIDENT_INDEX)
    validate_generated_incident_evidence_facets(records, errors, MASTER_INDEX)
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
    if errors:
        print("VIGIL public Incident index validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"VIGIL public Incident index validation passed: {len(records)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
