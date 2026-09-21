#!/usr/bin/env python3
"""Migrate the reviewed EU AI Act re-extraction into canonical EXTREQ shards.

The re-extraction packages remain as source-fidelity review inputs. This script
performs the identity transaction against the canonical sharded corpus through
``external_requirements_io`` and writes the durable retirement map. It is
idempotent: a second check confirms the already-migrated state rather than
attempting to retire or insert records again.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from external_requirements_io import load_json, load_requirements_document, write_requirements_document


ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_governance" / "requirements"
SOURCES = ROOT / "external_governance" / "sources"
REEXTRACTIONS = REQ / "reextractions"
METADATA_NORMALIZATION = REEXTRACTIONS / "EU-AI-ACT-2026-07-27-metadata-normalization.json"
RETIREMENTS = REQ / "retirements" / "EU-AI-ACT-2024-1689.json"

SOURCE_ID = "EU-AI-ACT-2024-1689"
SOURCE_VERSION = "2026-07-27"
MIGRATION_DATE = "2026-09-20"
EXPECTED_CANDIDATE_COUNT = 102
EXPECTED_RETIRED_IDS = {
    "EXTREQ-F30E6B9A906370B9",
    "EXTREQ-44B7BB17CB030468",
    "EXTREQ-09AD2F5442A55B55",
    "EXTREQ-901AD2C0A909E790",
    "EXTREQ-33898CCD26FBF5D5",
    "EXTREQ-126CB22D1FF08066",
    "EXTREQ-1B4CA7A04D63F038",
    "EXTREQ-E640D3CE18685E25",
}
OVERLAY_FIELDS = {
    "applicable_actor",
    "governed_object",
    "lifecycle_stage",
    "evidence_expectation",
    "timing_or_frequency",
    "required_artefacts",
    "verification_method",
    "applicability_conditions",
    "exceptions_or_qualifications",
}


def json_text(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def source_key(value: dict[str, Any]) -> tuple[str, str]:
    return str(value.get("vigil_source_id", "")), str(value.get("source_version", ""))


def requirement_id(source_id: str, version: str, clause: str, identity: str) -> str:
    seed = "|".join((source_id, version, clause.strip(), identity.strip()))
    return "EXTREQ-" + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16].upper()


def parent_for(clause: str) -> str:
    parents = {
        "Article 4a": "Article 4a — Processing of special categories of personal data for bias detection and correction",
        "Article 9": "Article 9 — Risk management system",
        "Article 10": "Article 10 — Data and data governance",
        "Article 11": "Article 11 — Technical documentation",
        "Article 12": "Article 12 — Record-keeping",
        "Article 13": "Article 13 — Transparency and provision of information to deployers",
        "Article 14": "Article 14 — Human oversight",
        "Article 15": "Article 15 — Accuracy, robustness and cybersecurity",
    }
    for prefix, parent in parents.items():
        if clause == prefix or clause.startswith(prefix + "("):
            return parent
    raise ValueError(f"unsupported staged EU AI Act clause: {clause}")


def apply_metadata_overlay(candidate: dict[str, Any], overrides: dict[str, dict[str, Any]]) -> dict[str, Any]:
    normalized = dict(candidate)
    override = overrides.get(candidate["requirement_id"], {})
    unexpected = set(override) - OVERLAY_FIELDS
    if unexpected:
        raise ValueError(
            f"unsupported metadata override fields for {candidate['requirement_id']}: {sorted(unexpected)}"
        )
    normalized.update(override)
    return normalized


def expand(
    candidate: dict[str, Any],
    source: dict[str, Any],
    scope: dict[str, Any],
    package: dict[str, Any],
    overrides: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    candidate = apply_metadata_overlay(candidate, overrides)
    clause = candidate["clause_or_control"]
    identity = candidate["identity_key"]
    expected = requirement_id(source["vigil_source_id"], source["source_version"], clause, identity)
    if candidate["requirement_id"] != expected:
        raise ValueError(f"non-deterministic candidate {candidate['requirement_id']}; expected {expected}")

    record = {
        "requirement_id": candidate["requirement_id"],
        "identity_key": identity,
        "vigil_source_id": source["vigil_source_id"],
        "external_source_id": source["external_source_id"],
        "source_version": source["source_version"],
        "canonical_source_identifier": source["canonical_identifier"],
        "issuer": source["issuer"],
        "jurisdiction": source["jurisdiction"],
        "source_class": source["source_class"],
        "source_lifecycle_state": source["source_lifecycle_state"],
        "source_role": scope["source_role"],
        "authoritative_locator": source["official_locator"],
        "clause_or_control": clause,
        "parent_section_or_group": parent_for(clause),
        "source_access_status": scope["source_access_status"],
        "source_review_date": package["reviewed_at"],
        "source_access_notes": "Authoritative consolidated public text directly reviewed on EUR-Lex for semantic re-extraction.",
        "requirement_summary": candidate["requirement_summary"],
        "requirement_posture": candidate.get("requirement_posture", "mandatory-normative"),
        "expectation_type": candidate.get("expectation_type", "positive-duty"),
        "normative_force": "binding-law",
        "alignment_relationship": "compliance",
        "applicable_actor": candidate["applicable_actor"],
        "governed_object": candidate["governed_object"],
        "lifecycle_stage": candidate["lifecycle_stage"],
        "governance_expectation": candidate.get("governance_expectation", candidate["requirement_summary"]),
        "evidence_expectation": candidate.get("evidence_expectation", []),
        "timing_or_frequency": candidate.get("timing_or_frequency", []),
        "required_artefacts": candidate.get("required_artefacts", []),
        "verification_method": candidate.get("verification_method", []),
        "applicability_conditions": candidate.get("applicability_conditions", []),
        "exceptions_or_qualifications": candidate.get("exceptions_or_qualifications", []),
        "governance_concepts": candidate["governance_concepts"],
        "source_defined_tags": [],
        "related_external_requirements": [],
        "interpretation_status": "reviewed-analytical-summary",
        "interpretation_provenance": {
            "basis": "direct-primary-text",
            "content_origin": "ai-authored",
            "generated_by": "ai",
            "generation_mode": "semi-autonomous",
            "human_role": "contract-approver",
            "human_authorship": False,
            "human_review_status": "not-reviewed",
            "human_verification_status": "not-verified",
            "source_analysis_method": "Semantic-atomicity re-extraction from the authoritative consolidated EUR-Lex text under SOURCE-FIDELITY-METHODOLOGY.md, with source-explicit metadata normalization.",
            "source_locator": source["official_locator"],
            "source_metadata_fingerprint": source["source_metadata_fingerprint"],
            "reviewed_source_digest": None,
            "reviewed_source_digest_algorithm": None,
            "reviewed_source_digest_status": "not-recorded",
        },
        "assurance_provenance": [],
        "review_limitations": [
            "Consolidated EUR-Lex text is a documentation tool; authentic amending acts remain the legal source of record."
        ],
        "semantic_atomicity": candidate["semantic_atomicity"],
    }
    if candidate["semantic_atomicity"] == "source-defined-compound":
        record["constituent_propositions"] = candidate["constituent_propositions"]
    return record


def package_paths() -> list[Path]:
    paths = sorted(
        path
        for path in REEXTRACTIONS.glob("EU-AI-ACT-2026-07-27-*.json")
        if path.name != METADATA_NORMALIZATION.name
    )
    if not paths:
        raise ValueError("no staged EU AI Act re-extraction packages found")
    return paths


def load_inputs() -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    packages = [load_json(path) for path in package_paths()]
    normalization = load_json(METADATA_NORMALIZATION)
    overrides = normalization.get("overrides", {})
    registry = load_json(SOURCES / "source-registry.json")["entries"]
    scopes = load_json(REQ / "source-scope.json")["entries"]
    registry_by_key = {source_key(entry): entry for entry in registry}
    scope_by_key = {source_key(entry): entry for entry in scopes}
    source = registry_by_key.get(("EXT-7DB18E82C9D3", SOURCE_VERSION))
    scope = scope_by_key.get(("EXT-7DB18E82C9D3", SOURCE_VERSION))
    if source is None or scope is None:
        raise ValueError("EU AI Act 27 July 2026 source/version is not registered")
    if source["external_source_id"] != SOURCE_ID:
        raise ValueError("registered EU AI Act source has unexpected external_source_id")

    expected_source_fields = {
        "vigil_source_id": source["vigil_source_id"],
        "external_source_id": source["external_source_id"],
        "source_version": source["source_version"],
        "canonical_source_identifier": source["canonical_identifier"],
        "authoritative_locator": source["official_locator"],
        "source_metadata_fingerprint": source["source_metadata_fingerprint"],
    }
    retired: list[dict[str, Any]] = []
    candidates: list[dict[str, Any]] = []
    package_keys: set[tuple[str, str]] = set()
    for package in packages:
        package_source = package.get("source", {})
        package_keys.add(source_key(package_source))
        mismatches = {
            key: (package_source.get(key), value)
            for key, value in expected_source_fields.items()
            if package_source.get(key) != value
        }
        if mismatches:
            raise ValueError(f"source metadata mismatch in staged package: {mismatches}")
        if package.get("status") != "migration-candidate":
            raise ValueError(f"unexpected staged package status: {package.get('status')!r}")
        retired.extend(package.get("retired_requirements", []))
        candidates.extend(expand(record, source, scope, package, overrides) for record in package.get("requirements", []))

    if package_keys != {(source["vigil_source_id"], source["source_version"])}:
        raise ValueError(f"staged packages resolve to multiple source/version keys: {sorted(package_keys)}")
    retired_ids = {item["requirement_id"] for item in retired}
    if retired_ids != EXPECTED_RETIRED_IDS:
        raise ValueError(f"retirement set differs from the approved eight-record transaction: {sorted(retired_ids)}")
    if len(candidates) != EXPECTED_CANDIDATE_COUNT:
        raise ValueError(f"expected {EXPECTED_CANDIDATE_COUNT} staged candidates, found {len(candidates)}")
    candidate_ids = [record["requirement_id"] for record in candidates]
    if len(candidate_ids) != len(set(candidate_ids)):
        raise ValueError("duplicate successor requirement IDs across staged packages")
    orphan_overrides = sorted(set(overrides) - set(candidate_ids))
    if orphan_overrides:
        raise ValueError(f"metadata normalization references non-staged requirement IDs: {orphan_overrides}")
    for rid, override in overrides.items():
        unexpected = set(override) - OVERLAY_FIELDS
        if unexpected:
            raise ValueError(f"unsupported metadata override fields for {rid}: {sorted(unexpected)}")
    return source, packages, overrides, candidates, {"retired": retired, "scope": scope}


def retirement_document(source: dict[str, Any], retired: list[dict[str, Any]], candidates: list[dict[str, Any]]) -> dict[str, Any]:
    successor_by_article: dict[str, list[str]] = {}
    for item in retired:
        prefix = item["clause_or_control"]
        successors = sorted(
            record["requirement_id"]
            for record in candidates
            if record["clause_or_control"] == prefix or record["clause_or_control"].startswith(prefix + "(")
        )
        if not successors:
            raise ValueError(f"no successor candidates resolve to retired clause {prefix}")
        successor_by_article[item["requirement_id"]] = successors

    return {
        "schema_version": "1.0",
        "source": {
            "vigil_source_id": source["vigil_source_id"],
            "external_source_id": source["external_source_id"],
            "source_version": source["source_version"],
        },
        "retired_at": MIGRATION_DATE,
        "retirement_basis": "explicit-maintainer-approved-semantic-decomposition",
        "retirement_scope": "Articles 4a and 9-15 atomic/source-defined-compound reconciliation",
        "retired_requirements": [
            {
                "requirement_id": item["requirement_id"],
                "identity_key": item["identity_key"],
                "clause_or_control": item["clause_or_control"],
                "successor_requirement_ids": successor_by_article[item["requirement_id"]],
                "reason": item["reason"],
                "historical_record_preservation": "git-history-and-retirement-map",
            }
            for item in sorted(retired, key=lambda value: value["requirement_id"])
        ],
    }


def migrate(check_only: bool = False) -> dict[str, Any]:
    source, packages, overrides, candidates, details = load_inputs()
    document = load_requirements_document()
    requirements = document["requirements"]
    by_id = {record["requirement_id"]: record for record in requirements}
    retired = details["retired"]
    retired_ids = {item["requirement_id"] for item in retired}
    candidate_ids = {record["requirement_id"] for record in candidates}

    for item in retired:
        current = by_id.get(item["requirement_id"])
        if current is not None:
            if (current.get("external_source_id"), current.get("source_version")) != (SOURCE_ID, SOURCE_VERSION):
                raise ValueError(f"retired requirement belongs to another source/version: {item['requirement_id']}")
            if current.get("identity_key") != item.get("identity_key") or current.get("clause_or_control") != item.get("clause_or_control"):
                raise ValueError(f"retired requirement metadata differs from staged declaration: {item['requirement_id']}")

    collisions = sorted(candidate_ids & set(by_id) - retired_ids)
    already_migrated_shape = (
        retired_ids.isdisjoint(set(by_id)) and collisions == sorted(candidate_ids)
    )
    if collisions and not already_migrated_shape:
        raise ValueError(f"successor identity collision with a live canonical requirement: {collisions}")

    migrated = [record for record in requirements if record["requirement_id"] not in retired_ids] + candidates
    migrated.sort(key=lambda record: record["requirement_id"])
    expected = dict(document)
    expected["requirements"] = migrated
    expected["requirement_count"] = len(migrated)
    expected["updated_at"] = MIGRATION_DATE

    current_eu = [record for record in requirements if source_key(record) == (source["vigil_source_id"], SOURCE_VERSION)]
    present_retired = retired_ids & set(by_id)
    present_candidates = candidate_ids & set(by_id)
    if present_retired and present_candidates:
        raise ValueError("canonical corpus is in a mixed EU AI Act migration state")
    if not present_retired and present_candidates != candidate_ids:
        raise ValueError("canonical corpus is neither pre-migration nor fully migrated")
    if present_retired and present_retired != retired_ids:
        raise ValueError("canonical corpus has a partial retired-identity set")
    already_migrated = not present_retired
    if len(current_eu) not in {81, 175}:
        raise ValueError(f"unexpected EU AI Act count {len(current_eu)}; expected the 81-record pre-migration or 175-record migrated state")
    if len(current_eu) == 81 and already_migrated:
        raise ValueError("EU AI Act count is 81 but the canonical identity state appears migrated")
    if len(current_eu) == 175 and not already_migrated:
        raise ValueError("EU AI Act count is 175 but the canonical identity state is not fully migrated")
    expected_eu_count = 175 if already_migrated else len(current_eu) - len(retired_ids) + len(candidates)
    if already_migrated:
        current_by_id = {record["requirement_id"]: record for record in requirements}
        expected_by_id = {record["requirement_id"]: record for record in candidates}
        for rid in candidate_ids:
            if current_by_id[rid] != expected_by_id[rid]:
                raise ValueError(f"canonical successor record differs from deterministic staged migration: {rid}")

    retirement = retirement_document(source, retired, candidates)
    print(
        "EU AI Act atomic migration valid: "
        f"start {len(current_eu)}, retire {len(retired_ids)}, add {len(candidates)}, "
        f"apply {len(overrides)} metadata normalizations, result {expected_eu_count}; "
        f"state={'already-migrated' if already_migrated else 'pre-migration'}"
    )
    if check_only:
        return {"source": source, "packages": packages, "document": expected, "retirement": retirement}

    if not already_migrated:
        write_requirements_document(expected)
        print("Wrote canonical source/version shards, requirements manifest and compatibility aggregate")
    RETIREMENTS.parent.mkdir(parents=True, exist_ok=True)
    RETIREMENTS.write_text(json_text(retirement), encoding="utf-8")
    print(f"Wrote {RETIREMENTS}")
    return {"source": source, "packages": packages, "document": expected, "retirement": retirement}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    migrate(check_only=args.check_only)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
