#!/usr/bin/env python3
"""Apply staged semantic-atomicity replacements for the consolidated EU AI Act.

This migration is intentionally source-specific. It retires coarse immutable EXTREQ
identities only when an approved re-extraction package supplies deterministic
replacement identities. It does not mark the source fidelity-assured; the wider Act
must still be reviewed under SOURCE-FIDELITY-METHODOLOGY.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_requirements"
SOURCES = ROOT / "external_sources"
REQUIREMENTS = REQ / "requirements.json"
REGISTRY = SOURCES / "source-registry.json"
SCOPE = REQ / "source-scope.json"
PACKAGE = REQ / "reextractions" / "EU-AI-ACT-2026-07-27-articles-10-13.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def requirement_id(vigil_source_id: str, source_version: str, clause: str, identity_key: str) -> str:
    seed = "|".join((vigil_source_id, source_version, clause.strip(), identity_key.strip()))
    return "EXTREQ-" + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16].upper()


def source_key(value):
    return value["vigil_source_id"], value["source_version"]


def expand(candidate, source, scope, package):
    clause = candidate["clause_or_control"]
    identity = candidate["identity_key"]
    expected = requirement_id(source["vigil_source_id"], source["source_version"], clause, identity)
    if candidate["requirement_id"] != expected:
        raise ValueError(f"non-deterministic candidate identity {candidate['requirement_id']}; expected {expected}")

    parent = "Article 10 — Data and data governance" if clause.startswith("Article 10") else "Article 13 — Transparency and provision of information to deployers"
    return {
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
        "parent_section_or_group": parent,
        "source_access_status": scope["source_access_status"],
        "source_review_date": package["reviewed_at"],
        "source_access_notes": "Authoritative consolidated public text directly reviewed on EUR-Lex for semantic re-extraction.",
        "requirement_summary": candidate["requirement_summary"],
        "requirement_posture": "mandatory-normative",
        "expectation_type": candidate["expectation_type"],
        "normative_force": "binding-law",
        "alignment_relationship": "compliance",
        "applicable_actor": candidate["applicable_actor"],
        "governed_object": candidate["governed_object"],
        "lifecycle_stage": candidate["lifecycle_stage"],
        "governance_expectation": candidate["governance_expectation"],
        "evidence_expectation": candidate["evidence_expectation"],
        "timing_or_frequency": candidate["timing_or_frequency"],
        "required_artefacts": candidate["required_artefacts"],
        "verification_method": candidate["verification_method"],
        "applicability_conditions": candidate["applicability_conditions"],
        "exceptions_or_qualifications": candidate["exceptions_or_qualifications"],
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
            "source_analysis_method": "Semantic-atomicity re-extraction from the authoritative consolidated EUR-Lex text under SOURCE-FIDELITY-METHODOLOGY.md.",
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
    }


def migrate(check_only: bool) -> None:
    package = load(PACKAGE)
    req_doc = load(REQUIREMENTS)
    registry = load(REGISTRY)["entries"]
    scopes = load(SCOPE)["entries"]

    key = source_key(package["source"])
    source = next((item for item in registry if source_key(item) == key), None)
    scope = next((item for item in scopes if source_key(item) == key), None)
    if source is None or scope is None:
        raise ValueError(f"EU AI Act source/version not registered: {key}")
    if source["external_source_id"] != package["source"]["external_source_id"]:
        raise ValueError("re-extraction package external_source_id differs from registry")
    if source["source_metadata_fingerprint"] != package["source"]["source_metadata_fingerprint"]:
        raise ValueError("re-extraction package source fingerprint differs from registry")

    requirements = req_doc["requirements"]
    by_id = {item["requirement_id"]: item for item in requirements}
    retired = {item["requirement_id"] for item in package["retired_requirements"]}
    missing = sorted(retired - set(by_id))
    if missing:
        raise ValueError(f"retired requirement IDs absent from canonical corpus: {missing}")
    for item in package["retired_requirements"]:
        current = by_id[item["requirement_id"]]
        if current["vigil_source_id"] != key[0] or current["source_version"] != key[1]:
            raise ValueError(f"retired identity belongs to another source/version: {item['requirement_id']}")

    replacements = [expand(item, source, scope, package) for item in package["requirements"]]
    replacement_ids = [item["requirement_id"] for item in replacements]
    if len(replacement_ids) != len(set(replacement_ids)):
        raise ValueError("duplicate replacement requirement IDs")
    collisions = sorted((set(replacement_ids) & set(by_id)) - retired)
    if collisions:
        raise ValueError(f"replacement identities collide with existing requirements: {collisions}")

    migrated = [item for item in requirements if item["requirement_id"] not in retired] + replacements
    migrated.sort(key=lambda item: item["requirement_id"])
    req_doc["requirements"] = migrated
    req_doc["requirement_count"] = len(migrated)
    req_doc["updated_at"] = package["reviewed_at"]

    print(f"EU AI Act migration valid: retire {len(retired)}, add {len(replacements)}, resulting count {len(migrated)}")
    if check_only:
        return
    REQUIREMENTS.write_text(json.dumps(req_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {REQUIREMENTS}")
    print("Next: python vigil/scripts/manage-external-requirements.py build")
    print("Then: python vigil/scripts/manage-external-requirements.py validate --check-generated")
    print("Then: python vigil/scripts/validate-external-requirement-fidelity.py")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true", help="Validate the staged migration without writing requirements.json")
    args = parser.parse_args()
    migrate(args.check_only)


if __name__ == "__main__":
    main()
