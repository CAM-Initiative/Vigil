#!/usr/bin/env python3
"""Separate CycloneDX 1.7 modelCard bom-ref MUST and SHOULD propositions."""
from __future__ import annotations

import argparse
import copy
import hashlib

from external_requirements_io import load_requirements_document, write_requirements_document


UNIQUE_ID = "EXTREQ-FA1B882FFAD54D93"
PREFIX_ID = "EXTREQ-F2C81603A7B306F6"
SOURCE_ID = "EXT-13FB945E8A06"
SOURCE_VERSION = "1.7"
CLAUSE = "modelCard.bom-ref"


def requirement_id(identity: str) -> str:
    seed = "|".join((SOURCE_ID, SOURCE_VERSION, CLAUSE, identity))
    return "EXTREQ-" + hashlib.sha256(seed.encode()).hexdigest()[:16].upper()


def reviewed_provenance(record: dict) -> dict:
    value = copy.deepcopy(record["interpretation_provenance"])
    value["source_analysis_method"] = (
        "Direct modality review of modelCard.bom-ref in the CycloneDX 1.7 JSON schema "
        "at release commit 4b3f59453366e27c8073fd24e98bf21ef8892c8e."
    )
    value["source_locator"] = (
        "https://github.com/CycloneDX/specification/blob/"
        "4b3f59453366e27c8073fd24e98bf21ef8892c8e/schema/bom-1.7.schema.json#L3263-L3274"
    )
    return value


def migrate(check_only: bool) -> None:
    document = load_requirements_document()
    records = document["requirements"]
    by_id = {record["requirement_id"]: record for record in records}
    unique = by_id.get(UNIQUE_ID)
    if unique is None or unique.get("identity_key") != "model-card-bom-ref-unique":
        raise ValueError("CycloneDX model-card bom-ref uniqueness identity is absent or changed")
    if requirement_id("model-card-bom-ref-unique") != UNIQUE_ID:
        raise ValueError("CycloneDX uniqueness identity is not deterministic")
    if requirement_id("model-card-bom-ref-reserved-prefix") != PREFIX_ID:
        raise ValueError("CycloneDX reserved-prefix identity is not deterministic")

    unique.update({
        "requirement_summary": "If a model-card bom-ref is supplied, it must be unique within the BOM.",
        "governance_expectation": "If a model-card bom-ref is supplied, it must be unique within the BOM.",
        "evidence_expectation": ["A model-card bom-ref that is unique within the BOM."],
        "verification_method": ["BOM-wide uniqueness validation for the supplied model-card bom-ref."],
        "exceptions_or_qualifications": [],
        "related_external_requirements": [PREFIX_ID],
        "source_review_date": "2026-08-28",
        "interpretation_provenance": reviewed_provenance(unique),
    })

    prefix = copy.deepcopy(unique)
    prefix.update({
        "requirement_id": PREFIX_ID,
        "identity_key": "model-card-bom-ref-reserved-prefix",
        "requirement_summary": "If a model-card bom-ref is supplied, it should not start with the BOM-Link intro urn:cdx: to avoid conflicts with BOM-Links.",
        "requirement_posture": "recommended-practice",
        "expectation_type": "guidance",
        "governance_expectation": "If a model-card bom-ref is supplied, it should not start with the BOM-Link intro urn:cdx: to avoid conflicts with BOM-Links.",
        "evidence_expectation": ["A supplied model-card bom-ref that does not start with urn:cdx:."],
        "verification_method": ["Prefix inspection of the supplied model-card bom-ref."],
        "exceptions_or_qualifications": [
            "The reserved-prefix constraint is a SHOULD recommendation; CycloneDX 1.7 does not enforce it through the referenced refType schema pattern."
        ],
        "related_external_requirements": [UNIQUE_ID],
        "interpretation_provenance": reviewed_provenance(unique),
    })
    existing = by_id.get(PREFIX_ID)
    if existing is not None and existing != prefix:
        raise ValueError(f"existing reserved-prefix record conflicts with deterministic migration: {PREFIX_ID}")
    if existing is None:
        records.append(prefix)
    records.sort(key=lambda record: record["requirement_id"])
    document["requirements"] = records
    document["requirement_count"] = len(records)
    document["updated_at"] = "2026-08-28"
    print(f"CycloneDX bom-ref migration valid: retained {UNIQUE_ID}; added {PREFIX_ID}; {len(records)} total requirements")
    if not check_only:
        write_requirements_document(document)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    migrate(args.check_only)


if __name__ == "__main__":
    main()
