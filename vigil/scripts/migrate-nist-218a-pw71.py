#!/usr/bin/env python3
"""Separate NIST SP 800-218A PW.7.1 R1 and C1 without losing R1 identity."""
from __future__ import annotations

import argparse
import copy
import hashlib

from external_requirements_io import load_requirements_document, write_requirements_document


R1_ID = "EXTREQ-CFC9864F6289630A"
C1_ID = "EXTREQ-1FFE1710582A469A"
SOURCE_ID = "EXT-65F7658B8B04"
SOURCE_VERSION = "2024"
SCOPE = (
    "Applies to AI model development, including data sourcing, design, training, "
    "fine-tuning, evaluation, and incorporation or integration into other software."
)
QUALIFICATIONS = [
    "The Profile supplements NIST SP 800-218 SSDF 1.1 and is not intended for standalone use.",
    "Organizations are expected to adapt, customize, and omit items as necessary through a risk-based approach because not all practices and tasks apply to every use case.",
    "Deployment and operation of AI systems and most of the data governance and management life cycle are outside the Profile's scope.",
]


def requirement_id(clause: str, identity: str) -> str:
    seed = "|".join((SOURCE_ID, SOURCE_VERSION, clause, identity))
    return "EXTREQ-" + hashlib.sha256(seed.encode()).hexdigest()[:16].upper()


def provenance(record: dict, clause: str) -> dict:
    value = copy.deepcopy(record["interpretation_provenance"])
    value["source_analysis_method"] = (
        "Direct primary-text modality review of NIST SP 800-218A Table 1; the distinct "
        "PW.7.1 recommendation and consideration were represented separately."
    )
    value["source_locator"] = f"https://doi.org/10.6028/NIST.SP.800-218A ({clause})"
    return value


def migrate(check_only: bool) -> None:
    document = load_requirements_document()
    records = document["requirements"]
    by_id = {record["requirement_id"]: record for record in records}
    r1 = by_id.get(R1_ID)
    if r1 is None:
        raise ValueError(f"PW.7.1 R1 record is absent: {R1_ID}")
    if (r1["vigil_source_id"], r1["source_version"], r1["identity_key"]) != (
        SOURCE_ID, SOURCE_VERSION, "pw.7.1-r1"
    ):
        raise ValueError("PW.7.1 R1 identity contract differs from the reviewed source")
    if requirement_id("PW.7.1 R1", "pw.7.1-r1") != R1_ID:
        raise ValueError("PW.7.1 R1 deterministic identity changed")
    if requirement_id("PW.7.1 C1", "pw.7.1-c1") != C1_ID:
        raise ValueError("PW.7.1 C1 deterministic identity changed")

    r1.update({
        "requirement_summary": "Code review and analysis policies or guidelines should include code for AI models and other related components.",
        "governance_expectation": "Code review and analysis policies or guidelines should include code for AI models and other related components.",
        "governed_object": ["Code review and analysis policies or guidelines for AI model code and related components"],
        "required_artefacts": ["Code review and analysis policies or guidelines covering AI model code and related components."],
        "evidence_expectation": ["Code review and analysis policies or guidelines covering AI model code and related components."],
        "verification_method": [],
        "applicability_conditions": [SCOPE],
        "exceptions_or_qualifications": QUALIFICATIONS,
        "governance_concepts": ["security", "testing-evaluation"],
        "related_external_requirements": [C1_ID],
        "source_review_date": "2026-08-28",
        "interpretation_provenance": provenance(r1, "PW.7.1 R1"),
    })

    c1 = copy.deepcopy(r1)
    c1.update({
        "requirement_id": C1_ID,
        "identity_key": "pw.7.1-c1",
        "clause_or_control": "PW.7.1 C1",
        "requirement_summary": "Consider performing scans of AI model code in addition to testing the AI models.",
        "requirement_posture": "informative-guidance",
        "governance_expectation": "Consider performing scans of AI model code in addition to testing the AI models.",
        "governed_object": ["AI model code"],
        "required_artefacts": [],
        "evidence_expectation": ["AI model code scan results, where the consideration is adopted."],
        "verification_method": ["Scanning AI model code in addition to testing the AI models."],
        "exceptions_or_qualifications": QUALIFICATIONS + [
            "Scanning is a consideration rather than a recommendation and supplements testing of the AI models."
        ],
        "related_external_requirements": [R1_ID],
        "interpretation_provenance": provenance(r1, "PW.7.1 C1"),
    })
    existing_c1 = by_id.get(C1_ID)
    if existing_c1 is not None:
        if (
            existing_c1.get("vigil_source_id") != SOURCE_ID
            or existing_c1.get("identity_key") != "pw.7.1-c1"
        ):
            raise ValueError(f"existing PW.7.1 C1 record conflicts with deterministic migration: {C1_ID}")
        existing_c1.update(c1)
    else:
        records.append(c1)
    records.sort(key=lambda record: record["requirement_id"])
    document["requirements"] = records
    document["requirement_count"] = len(records)
    document["updated_at"] = "2026-08-28"
    print(f"NIST SP 800-218A PW.7.1 migration valid: retained {R1_ID}; added {C1_ID}; {len(records)} total requirements")
    if not check_only:
        write_requirements_document(document)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    migrate(args.check_only)


if __name__ == "__main__":
    main()
