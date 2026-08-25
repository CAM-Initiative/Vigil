#!/usr/bin/env python3
"""Validate VIGIL external-requirement semantic-fidelity state.

This validator intentionally distinguishes historical extraction completion from
semantic-fidelity assurance. A source recorded as extraction_status=complete is
only effectively complete for clause-level use when source-fidelity.json marks
that exact source/version as assured. Unlisted historical complete sources are
conservatively treated as fidelity-unassured/effectively partial.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
EXTREQ = ROOT / "vigil" / "external_requirements"
SCOPE_PATH = EXTREQ / "source-scope.json"
REQ_PATH = EXTREQ / "requirements.json"
FIDELITY_PATH = EXTREQ / "source-fidelity.json"
STRESS_DIR = EXTREQ / "fidelity-stress-tests"

VALID_FIDELITY = {
    "assured",
    "provisional",
    "requires-reextraction",
    "blocked",
    "not-applicable",
}


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def source_key(item: dict) -> tuple[str, str]:
    return item.get("vigil_source_id", ""), item.get("source_version", "")


def validate() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []

    scope = load(SCOPE_PATH)
    requirements = load(REQ_PATH)
    fidelity = load(FIDELITY_PATH)

    scope_entries = {source_key(item): item for item in scope.get("entries", [])}
    req_entries = requirements.get("requirements", requirements if isinstance(requirements, list) else [])
    req_by_id = {item.get("requirement_id"): item for item in req_entries}

    fidelity_entries = fidelity.get("entries", [])
    seen: set[tuple[str, str]] = set()
    fidelity_by_source: dict[tuple[str, str], dict] = {}

    policy = fidelity.get("policy", {})
    if policy.get("unlisted_complete_source_fidelity") != "fidelity-unassured":
        errors.append("source-fidelity policy must default unlisted complete sources to fidelity-unassured")
    if policy.get("effective_completion_rule") != "extraction-complete-and-fidelity-assured":
        errors.append("source-fidelity policy must use extraction-complete-and-fidelity-assured")

    for entry in fidelity_entries:
        key = source_key(entry)
        if key in seen:
            errors.append(f"duplicate source-fidelity entry: {key[0]} / {key[1]}")
            continue
        seen.add(key)
        fidelity_by_source[key] = entry

        if entry.get("fidelity_status") not in VALID_FIDELITY:
            errors.append(f"invalid fidelity_status for {key[0]} / {key[1]}")
        source = scope_entries.get(key)
        if source is None:
            errors.append(f"source-fidelity entry has no source-scope target: {key[0]} / {key[1]}")
            continue
        if entry.get("external_source_id") != source.get("external_source_id"):
            errors.append(f"external_source_id mismatch for {key[0]} / {key[1]}")

        status = entry.get("fidelity_status")
        effective = entry.get("effective_extraction_status")
        historical = source.get("extraction_status")
        if status == "assured":
            if historical != "complete":
                errors.append(f"assured source is not extraction-complete: {key[0]} / {key[1]}")
            if effective != "complete":
                errors.append(f"assured source must be effectively complete: {key[0]} / {key[1]}")
            if source.get("known_unreviewed_sections"):
                errors.append(f"assured source retains known_unreviewed_sections: {key[0]} / {key[1]}")
        elif historical == "complete" and effective == "complete":
            errors.append(
                f"non-assured source cannot remain effectively complete: {key[0]} / {key[1]} ({status})"
            )

        for requirement_id in entry.get("audited_requirement_ids", []):
            requirement = req_by_id.get(requirement_id)
            if requirement is None:
                errors.append(f"audited requirement does not exist: {requirement_id}")
                continue
            if source_key(requirement) != key:
                errors.append(
                    f"audited requirement {requirement_id} does not belong to {key[0]} / {key[1]}"
                )

    historical_complete = [
        item for item in scope.get("entries", []) if item.get("extraction_status") == "complete"
    ]
    effective_complete = 0
    effective_partial_due_fidelity = 0
    for source in historical_complete:
        key = source_key(source)
        decision = fidelity_by_source.get(key)
        if decision and decision.get("fidelity_status") == "assured":
            effective_complete += 1
        else:
            effective_partial_due_fidelity += 1
            warnings.append(
                "effective downgrade: "
                f"{source.get('external_source_id')} {source.get('source_version')} was historically complete "
                "but is not fidelity-assured"
            )

    for path in sorted(STRESS_DIR.glob("*.json")) if STRESS_DIR.exists() else []:
        test = load(path)
        for record in test.get("tested_records", []):
            keys: set[str] = set()
            for proposition in record.get("candidate_constituent_propositions", []):
                key = proposition.get("proposition_key")
                if not key:
                    errors.append(f"{path.name}: constituent proposition missing proposition_key")
                elif key in keys:
                    errors.append(f"{path.name}: duplicate constituent proposition key {key}")
                keys.add(key)
                if not proposition.get("source_locator") or not proposition.get("summary"):
                    errors.append(f"{path.name}: incomplete constituent proposition {key or '<unknown>'}")

    summary = {
        "historical_complete_sources": len(historical_complete),
        "fidelity_assured_effective_complete_sources": effective_complete,
        "effective_partial_due_fidelity": effective_partial_due_fidelity,
        "explicit_fidelity_entries": len(fidelity_entries),
    }
    return errors, warnings, summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict-unassured", action="store_true", help="treat unassured historical complete sources as errors")
    args = parser.parse_args()

    errors, warnings, summary = validate()
    if args.strict_unassured:
        errors.extend(warnings)
        warnings = []

    print(json.dumps(summary, indent=2, sort_keys=True))
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
