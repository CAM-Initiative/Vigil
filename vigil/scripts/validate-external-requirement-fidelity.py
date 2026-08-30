#!/usr/bin/env python3
"""Validate VIGIL external-requirement semantic-fidelity state.

Historical extraction completion is distinct from semantic-fidelity assurance.
Staged re-extractions are also checked for deterministic identity and explicit
semantic-atomicity treatment before they may be migrated into requirements.json.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

from external_requirements_io import load_requirements_document

ROOT = Path(__file__).resolve().parents[2]
EXTREQ = ROOT / "vigil" / "external_governance" / "requirements"
SCOPE_PATH = EXTREQ / "source-scope.json"
FIDELITY_PATH = EXTREQ / "source-fidelity.json"
STRESS_DIR = EXTREQ / "fidelity-stress-tests"
REEXTRACTION_DIR = EXTREQ / "reextractions"

VALID_FIDELITY = {"assured", "provisional", "requires-reextraction", "blocked", "not-applicable"}
VALID_ATOMICITY = {"atomic", "source-defined-compound"}


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def source_key(item: dict) -> tuple[str, str]:
    return item.get("vigil_source_id", ""), item.get("source_version", "")


def requirement_id(source_id: str, version: str, clause: str, identity: str) -> str:
    seed = "|".join((source_id, version, clause.strip(), identity.strip()))
    return "EXTREQ-" + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16].upper()


def validate() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    scope = load(SCOPE_PATH)
    requirements = load_requirements_document()
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
            errors.append(f"non-assured source cannot remain effectively complete: {key[0]} / {key[1]} ({status})")
        for audited_id in entry.get("audited_requirement_ids", []):
            requirement = req_by_id.get(audited_id)
            if requirement is None:
                errors.append(f"audited requirement does not exist: {audited_id}")
            elif source_key(requirement) != key:
                errors.append(f"audited requirement {audited_id} does not belong to {key[0]} / {key[1]}")

    historical_complete = [item for item in scope.get("entries", []) if item.get("extraction_status") == "complete"]
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
                f"effective downgrade: {source.get('external_source_id')} {source.get('source_version')} "
                "was historically complete but is not fidelity-assured"
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

    staged_ids: set[str] = set()
    retired_ids: set[str] = set()
    staged_requirement_count = 0
    for path in sorted(REEXTRACTION_DIR.glob("*.json")) if REEXTRACTION_DIR.exists() else []:
        if path.name.endswith("-metadata-normalization.json"):
            continue
        package = load(path)
        source = package.get("source", {})
        key = source_key(source)
        if key not in scope_entries:
            errors.append(f"{path.name}: staged source/version does not resolve to source-scope")
        if package.get("status") != "migration-candidate":
            errors.append(f"{path.name}: staged package must be migration-candidate")
        for retired in package.get("retired_requirements", []):
            rid = retired.get("requirement_id")
            if rid in retired_ids:
                errors.append(f"{path.name}: retired requirement appears in multiple packages: {rid}")
            retired_ids.add(rid)
            current = req_by_id.get(rid)
            if current is None:
                errors.append(f"{path.name}: retired requirement is absent from canonical corpus: {rid}")
            elif source_key(current) != key:
                errors.append(f"{path.name}: retired requirement belongs to another source/version: {rid}")
        for record in package.get("requirements", []):
            staged_requirement_count += 1
            rid = record.get("requirement_id")
            expected = requirement_id(key[0], key[1], record.get("clause_or_control", ""), record.get("identity_key", ""))
            if rid != expected:
                errors.append(f"{path.name}: non-deterministic staged requirement {rid}; expected {expected}")
            if rid in staged_ids:
                errors.append(f"{path.name}: duplicate staged requirement ID {rid}")
            staged_ids.add(rid)
            atomicity = record.get("semantic_atomicity")
            if atomicity not in VALID_ATOMICITY:
                errors.append(f"{path.name}: invalid semantic_atomicity for {rid}")
            if atomicity == "source-defined-compound" and not record.get("constituent_propositions"):
                errors.append(f"{path.name}: source-defined compound lacks constituent propositions: {rid}")
            if atomicity == "atomic" and record.get("constituent_propositions"):
                errors.append(f"{path.name}: atomic record unexpectedly carries constituent propositions: {rid}")

    summary = {
        "historical_complete_sources": len(historical_complete),
        "fidelity_assured_effective_complete_sources": effective_complete,
        "effective_partial_due_fidelity": effective_partial_due_fidelity,
        "explicit_fidelity_entries": len(fidelity_entries),
        "staged_reextraction_retirements": len(retired_ids),
        "staged_reextraction_requirements": staged_requirement_count,
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
