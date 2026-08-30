#!/usr/bin/env python3
"""Build the deterministic FM/OBS-to-Incident migration crosswalk."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
MIGRATION = VIGIL / "migrations" / "incident-registry"
DECISIONS = MIGRATION / "Incident.Migration.Decisions.json"
OUTPUT = MIGRATION / "VIGIL.FM-OBS-to-INC.Crosswalk.json"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def legacy_records() -> list[tuple[Path, dict[str, Any]]]:
    output = []
    for folder in ("failures", "observations"):
        for path in sorted((RECORDS / folder).rglob("*.json")):
            record = load(path)
            output.append((path, record))
    return sorted(output, key=lambda item: item[1]["id"])


def incidents() -> dict[str, dict[str, Any]]:
    return {
        record["id"]: record
        for path in sorted((RECORDS / "incidents").glob("*.json"))
        if isinstance((record := load(path)), dict)
    }


def source_successors(
    legacy_id: str, source_url: str, successor_ids: list[str], incident_records: dict[str, dict[str, Any]]
) -> list[str]:
    output = []
    for incident_id in successor_ids:
        incident = incident_records.get(incident_id, {})
        for item in incident.get("source_records", []):
            if not isinstance(item, dict) or item.get("source_url") != source_url:
                continue
            origins = [item.get("migration_source_provenance"), *item.get("additional_legacy_source_origins", [])]
            if any(isinstance(origin, dict) and origin.get("legacy_id") == legacy_id for origin in origins):
                output.append(incident_id)
                break
    return output


def main() -> int:
    decisions = load(DECISIONS)
    default = decisions["default_disposition"]
    overrides = decisions["decisions"]
    incident_records = incidents()
    entries = []
    for path, record in legacy_records():
        legacy_id = record["id"]
        decision = {**default, **overrides.get(legacy_id, {})}
        successors = list(decision.get("successor_incidents", []))
        source_dispositions = []
        for index, item in enumerate(record.get("source_records", [])):
            url = item.get("source_url", "") if isinstance(item, dict) else ""
            migrated_to = source_successors(legacy_id, url, successors, incident_records)
            if migrated_to:
                disposition = "migrated-to-incident"
            elif decision["migration_status"] == "non-incident-not-migrated":
                disposition = "non-incident-not-migrated"
            elif decision["migration_status"] == "requires-human-review":
                disposition = "requires-human-review"
            else:
                disposition = "retained-in-legacy-pending-disentanglement"
            source_dispositions.append({
                "legacy_source_position": index + 1,
                "source_title": item.get("source_title", "") if isinstance(item, dict) else "",
                "source_url": url,
                "disposition": disposition,
                "successor_incidents": migrated_to,
            })
        entries.append({
            "legacy_id": legacy_id,
            "legacy_type": record.get("record_type"),
            "legacy_path": path.relative_to(ROOT).as_posix(),
            "inventory_assessment": decision["inventory_assessment"],
            "migration_status": decision["migration_status"],
            "successor_incidents": successors,
            "decision_basis": decision["decision_basis"],
            "source_dispositions": source_dispositions,
        })
    payload = {
        "migration_id": decisions["migration_id"],
        "migration_state": decisions["migration_state"],
        "baseline_commit": decisions["baseline_commit"],
        "generated_notice": "Deterministically generated from the complete legacy FM/OBS corpus, Incident pilot records and Incident.Migration.Decisions.json.",
        "legacy_record_count": len(entries),
        "incident_record_count": len(incident_records),
        "entries": entries,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Built Incident migration crosswalk for {len(entries)} legacy records and {len(incident_records)} Incidents.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
