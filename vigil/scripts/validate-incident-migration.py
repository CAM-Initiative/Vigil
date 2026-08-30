#!/usr/bin/env python3
"""Validate the INCIDENT-01 dataset, external references and FM/OBS crosswalk."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
CROSSWALK = VIGIL / "migrations" / "incident-registry" / "VIGIL.FM-OBS-to-INC.Crosswalk.json"
MIGRATION_STATUSES = {
    "migrated-to-incident", "decomposed", "partially-migrated",
    "non-incident-not-migrated", "requires-human-review",
}
SOURCE_DISPOSITIONS = {
    "migrated-to-incident", "non-incident-not-migrated", "requires-human-review",
    "absorbed-elsewhere", "duplicate-of-incident",
}
LEGACY_GOVERNANCE_FIELDS = {
    "summary", "why_it_matters_to_CAM", "failure_mode_definition", "failure_threshold",
    "failure_classification", "triage", "triage_history", "repair_status", "ecosystem_status",
    "corpus_coverage", "diagnostic_provenance", "possible_taxonomy_mapping", "next_action",
    "interpretive_provenance", "taxonomy_classification", "cam_internal", "system_context",
    "jurisdictional_context", "evidence_confidence", "linked_records",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    legacy_paths = sorted((RECORDS / "failures").rglob("*.json")) + sorted(
        (RECORDS / "observations").rglob("*.json")
    )
    legacy = {load(path)["id"]: load(path) for path in legacy_paths}
    incident_paths = sorted((RECORDS / "incidents").glob("*.json"))
    incidents = {load(path)["id"]: load(path) for path in incident_paths}
    crosswalk = load(CROSSWALK)
    entries = crosswalk.get("entries", [])
    if not isinstance(entries, list):
        errors.append("crosswalk.entries must be an array")
        entries = []
    by_legacy: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("crosswalk entry must be an object")
            continue
        legacy_id = entry.get("legacy_id")
        if legacy_id in by_legacy:
            errors.append(f"duplicate crosswalk entry for {legacy_id}")
        if isinstance(legacy_id, str):
            by_legacy[legacy_id] = entry
    missing = sorted(set(legacy) - set(by_legacy))
    extra = sorted(set(by_legacy) - set(legacy))
    if missing:
        errors.append(f"legacy records missing from crosswalk: {', '.join(missing)}")
    if extra:
        errors.append(f"crosswalk contains unknown legacy records: {', '.join(extra)}")
    if crosswalk.get("legacy_record_count") != len(legacy):
        errors.append("crosswalk legacy_record_count does not match corpus")
    if crosswalk.get("incident_record_count") != len(incidents):
        errors.append("crosswalk incident_record_count does not match corpus")

    for legacy_id, record in legacy.items():
        entry = by_legacy.get(legacy_id)
        if entry is None:
            continue
        if not entry.get("inventory_assessment") or not entry.get("migration_status") or not entry.get("decision_basis"):
            errors.append(f"{legacy_id}: incomplete disposition decision")
        if entry.get("migration_status") not in MIGRATION_STATUSES:
            errors.append(f"{legacy_id}: non-canonical migration_status {entry.get('migration_status')}")
        successors = entry.get("successor_incidents")
        if not isinstance(successors, list):
            errors.append(f"{legacy_id}: successor_incidents must be an array")
            successors = []
        for successor in successors:
            if successor not in incidents:
                errors.append(f"{legacy_id}: unknown successor {successor}")
        source_dispositions = entry.get("source_dispositions")
        sources = record.get("source_records", [])
        if not isinstance(source_dispositions, list) or len(source_dispositions) != len(sources):
            errors.append(f"{legacy_id}: every source_record requires exactly one source disposition")
            continue
        for position, disposition in enumerate(source_dispositions, 1):
            if not isinstance(disposition, dict):
                errors.append(f"{legacy_id}: source disposition {position} must be an object")
                continue
            if disposition.get("legacy_source_position") != position:
                errors.append(f"{legacy_id}: source disposition order mismatch at {position}")
            if not disposition.get("disposition"):
                errors.append(f"{legacy_id}: source disposition {position} is blank")
            elif disposition.get("disposition") not in SOURCE_DISPOSITIONS:
                errors.append(f"{legacy_id}: source disposition {position} is not canonical")
            if not disposition.get("decision_basis"):
                errors.append(f"{legacy_id}: source disposition {position} lacks a decision basis")
            migrated_to = disposition.get("successor_incidents", [])
            if not isinstance(migrated_to, list):
                errors.append(f"{legacy_id}: source disposition {position} successors must be an array")
                continue
            if any(incident_id not in successors for incident_id in migrated_to):
                errors.append(f"{legacy_id}: source disposition {position} points outside record successors")
            if disposition.get("disposition") == "migrated-to-incident" and not migrated_to:
                errors.append(f"{legacy_id}: migrated source disposition {position} has no successor")
            if (
                disposition.get("disposition") == "requires-human-review"
                and entry.get("migration_status") != "requires-human-review"
            ):
                warnings.append(f"{legacy_id} source {position}: semantic source review remains pending")
        if entry.get("migration_status") == "requires-human-review":
            warnings.append(f"{legacy_id}: semantic migration review remains pending")

    titles: dict[str, str] = {}
    external_ids: dict[tuple[str, str], str] = {}
    for incident_id, record in incidents.items():
        if not re.fullmatch(r"VIGIL-INC-\d{6}", incident_id):
            errors.append(f"invalid Incident ID {incident_id}")
        title = str(record.get("record_identity", {}).get("title", "")).strip().casefold()
        if not title:
            errors.append(f"{incident_id}: missing plain-English title")
        elif title in titles:
            errors.append(f"{incident_id}: duplicate normalised title with {titles[title]}")
        else:
            titles[title] = incident_id
        sources = record.get("source_records", [])
        source_urls = {item.get("source_url") for item in sources if isinstance(item, dict)}
        preferred_url = record.get("preferred_evidence", {}).get("source_url")
        if preferred_url not in source_urls:
            errors.append(f"{incident_id}: preferred evidence is not preserved in source_records")
        for reference in record.get("external_incident_references", []):
            if not isinstance(reference, dict):
                continue
            key = (
                str(reference.get("registry", "")).strip().casefold(),
                str(reference.get("external_id", "")).strip().casefold(),
            )
            previous = external_ids.get(key)
            if previous and previous != incident_id:
                errors.append(f"external incident identity {key} is duplicated by {previous} and {incident_id}")
            external_ids[key] = incident_id
        taxonomy = record.get("taxonomy_classification", {})
        mappings = [taxonomy.get("primary_classification"), *taxonomy.get("secondary_classifications", [])]
        for mapping in mappings:
            if isinstance(mapping, dict) and not str(mapping.get("classification_basis", "")).startswith("In this Incident,"):
                errors.append(f"{incident_id}: classification mapping basis is not Incident-specific")
        preserved_by_legacy = {
            item.get("legacy_id"): item.get("preserved_analysis", {})
            for item in record.get("legacy_governance_state", []) if isinstance(item, dict)
        }
        for provenance in record.get("legacy_provenance", []):
            if not isinstance(provenance, dict):
                continue
            legacy_id = provenance.get("legacy_id")
            entry = by_legacy.get(legacy_id)
            if entry is None:
                errors.append(f"{incident_id}: legacy provenance {legacy_id} has no crosswalk entry")
            elif incident_id not in entry.get("successor_incidents", []):
                errors.append(f"{incident_id}: crosswalk does not reciprocate legacy provenance {legacy_id}")
            preserved = preserved_by_legacy.get(legacy_id)
            if not isinstance(preserved, dict):
                errors.append(f"{incident_id}: legacy governance state missing for {legacy_id}")
            elif legacy_id in legacy:
                for field in LEGACY_GOVERNANCE_FIELDS:
                    if field in legacy[legacy_id] and preserved.get(field) != legacy[legacy_id][field]:
                        errors.append(f"{incident_id}: legacy governance field {legacy_id}.{field} was not preserved exactly")
        current_interpretation = str(record.get("vigil_assessment", {}).get("governance_interpretation", "")).strip()
        current_incident_text = " ".join([
            str(record.get("summary", "")),
            str(record.get("vigil_assessment", {}).get("factual_basis", "")),
            current_interpretation,
        ])
        if re.search(r"\b(?:VIGIL-\d{4}-)?(?:FM|OBS)-\d{4}\b", current_incident_text):
            errors.append(f"{incident_id}: current Incident narrative contains legacy FM/OBS process language")
        if current_interpretation.casefold().startswith("a failure mode in which"):
            errors.append(f"{incident_id}: current governance interpretation remains failure-mode pattern language")
        for preserved in record.get("legacy_governance_state", []):
            legacy_definition = str(
                preserved.get("preserved_analysis", {}).get("failure_mode_definition", "")
                if isinstance(preserved, dict) else ""
            ).strip()
            if legacy_definition and current_interpretation == legacy_definition:
                errors.append(f"{incident_id}: current governance interpretation duplicates legacy failure-mode definition")

    if crosswalk.get("migration_state") == "reconciled" and warnings:
        errors.append("reconciled migration state cannot retain requires-human-review dispositions")
    if errors:
        print("Incident migration validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "Incident migration validation passed: "
        f"{len(incidents)} Incidents, {len(legacy)} legacy dispositions, "
        f"{sum(len(item.get('source_records', [])) for item in legacy.values())} legacy sources accounted for; "
        f"{len(warnings)} genuinely ambiguous record/source reviews remain pending in {crosswalk.get('migration_state')} state."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
