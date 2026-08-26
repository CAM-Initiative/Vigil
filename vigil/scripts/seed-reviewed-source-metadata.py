#!/usr/bin/env python3
"""Apply and seed the first directly reviewed non-EU metadata slices.

The decisions in this script are intentionally limited to NIST AI RMF 1.0,
CycloneDX 1.7 and NIST AI 600-1. They were made from the cited public primary
sources on 2026-08-26. This is not a generic empty-field classifier.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_requirements"
REQUIREMENTS = REQ / "requirements.json"
LEDGER = REQ / "metadata-review.json"
BACKLOG = REQ / "reextraction-backlog.json"

FIELDS = (
    "applicable_actor",
    "governed_object",
    "timing_or_frequency",
    "required_artefacts",
    "evidence_expectation",
    "verification_method",
    "applicability_conditions",
    "exceptions_or_qualifications",
)

NIST_RMF = "EXT-6442C7954667"
CYCLONEDX = "EXT-13FB945E8A06"
NIST_GAI = "EXT-DE4FDB52698E"
CYCLONEDX_MODALITY_DEFECT = "EXTREQ-FA1B882FFAD54D93"

# Curated after action-by-action comparison with NIST AI 600-1. Fifty-one
# records visibly truncate source-defined constituent content; the remaining
# nine preserve several independently meaningful steps only in prose.
NIST_GAI_CONSTITUENT_BACKLOG = {
    "EXTREQ-007D7BAAE8A25C9D", "EXTREQ-036F8B9FBBE33437",
    "EXTREQ-09A4C260900D6A83", "EXTREQ-0E404DEFECDA5FE0",
    "EXTREQ-11A6E84345FB4301", "EXTREQ-1269988FF25A00FD",
    "EXTREQ-13DCE314CA72D587", "EXTREQ-1AAAF9F63C4B77A8",
    "EXTREQ-210E95EA572DB5FC", "EXTREQ-25BDC1BF6A486355",
    "EXTREQ-3209D60A503A7B46", "EXTREQ-3287D5CADAAE2D71",
    "EXTREQ-383E0AAF594EFF28", "EXTREQ-38A00DC3A54A582F",
    "EXTREQ-3CF6BE0334DEC565", "EXTREQ-3DE000C1C7E37071",
    "EXTREQ-3F827BC2D6FB855C", "EXTREQ-4277B23509413079",
    "EXTREQ-42E00BFFFB610685", "EXTREQ-4935F57986DF9317",
    "EXTREQ-4972B48203D4A92C", "EXTREQ-4D5BF8BEA4A413B0",
    "EXTREQ-4FA48F69E0D84D76", "EXTREQ-56049F64C61351DF",
    "EXTREQ-572E8F9A8CA166B2", "EXTREQ-5CEC8E71C7C1373F",
    "EXTREQ-606A32149AB41BA4", "EXTREQ-62AE400907DF1A92",
    "EXTREQ-684FDF9FC22A253D", "EXTREQ-696F45AAD993A382",
    "EXTREQ-6C9AF8BEB0C00E2C", "EXTREQ-6F77B758D19B752C",
    "EXTREQ-6FB32C15D60F5ECA", "EXTREQ-7BC3EDE0976A4F5B",
    "EXTREQ-7E4ACD956465C7ED", "EXTREQ-7E7500D622B64943",
    "EXTREQ-7F3E164A4F5EB23A", "EXTREQ-80C57DEB7282DF1E",
    "EXTREQ-84B3A244B2A9DDD1", "EXTREQ-864ED9C1B56018A2",
    "EXTREQ-8943536BE57E678B", "EXTREQ-89EDF6573EDE84D8",
    "EXTREQ-A67E54A283E42597", "EXTREQ-AC5BA019342AFFE9",
    "EXTREQ-B0737DEC2D388821", "EXTREQ-B609E1D64C88DC3D",
    "EXTREQ-BA19F5BDCF5FA962", "EXTREQ-BA7B79BDE2DC32FB",
    "EXTREQ-C37E171E0EA8E0CA", "EXTREQ-C395266FE4929644",
    "EXTREQ-CDA0F3004234AF9C", "EXTREQ-D01548E276DC81C7",
    "EXTREQ-D038CD035E17057F", "EXTREQ-D81F0D37C92F766F",
    "EXTREQ-E6335E9335C8D367", "EXTREQ-E7CB2246EA0311DC",
    "EXTREQ-F0686AA575DC32B9", "EXTREQ-F5EE679C987F9F08",
    "EXTREQ-F7D150323DFB3260", "EXTREQ-FCDE17D3F0843F55",
}

GAI_ACTOR = "Organization or relevant AI actor applying NIST AI 600-1"
GAI_APPLICABILITY = (
    "Applicability is determined from organizational considerations and the "
    "organization's unique use of GAI systems."
)
ACTOR_TAG_SCHEME = "NIST AI 600-1 AI Actor Tasks (subcategory-level)"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_nist_gai_actor_metadata(record: dict) -> None:
    if not re.fullmatch(r"(?:GV|MP|MS|MG)-\d+\.\d+-\d{3}", record["clause_or_control"]):
        return
    current = record.get("applicable_actor", [])
    tags = record.setdefault("source_defined_tags", [])
    actor_tag = next((tag for tag in tags if tag.get("scheme") == ACTOR_TAG_SCHEME), None)
    if current != [GAI_ACTOR]:
        if len(current) != 1 or not current[0]:
            raise ValueError(f"unexpected NIST AI 600-1 actor metadata for {record['requirement_id']}")
        values = [value.strip() for value in current[0].split(",") if value.strip()]
        expected_tag = {"scheme": ACTOR_TAG_SCHEME, "values": values}
        if actor_tag is not None and actor_tag != expected_tag:
            raise ValueError(f"conflicting NIST AI 600-1 actor-task tag for {record['requirement_id']}")
        if actor_tag is None:
            tags.append(expected_tag)
        record["applicable_actor"] = [GAI_ACTOR]
    elif actor_tag is None:
        raise ValueError(f"normalized actor lacks preserved source actor-task tag for {record['requirement_id']}")

    conditions = record.get("applicability_conditions", [])
    if conditions not in ([], [GAI_APPLICABILITY]):
        raise ValueError(f"unexpected NIST AI 600-1 applicability metadata for {record['requirement_id']}")
    record["applicability_conditions"] = [GAI_APPLICABILITY]


def backlog_entries(records: list[dict]) -> list[dict]:
    by_id = {record["requirement_id"]: record for record in records}
    missing = sorted(NIST_GAI_CONSTITUENT_BACKLOG - set(by_id))
    if missing:
        raise ValueError(f"NIST AI 600-1 backlog IDs do not resolve: {missing}")
    entries = []
    affected = [
        "governed_object", "timing_or_frequency", "required_artefacts",
        "evidence_expectation", "verification_method", "applicability_conditions",
        "exceptions_or_qualifications",
    ]
    for rid in sorted(NIST_GAI_CONSTITUENT_BACKLOG):
        record = by_id[rid]
        truncated = "…" in record["requirement_summary"]
        entries.append({
            "current_requirement_id": rid,
            "vigil_source_id": record["vigil_source_id"],
            "external_source_id": record["external_source_id"],
            "source_version": record["source_version"],
            "clause_or_control": record["clause_or_control"],
            "reason": (
                "The current analytical summary truncates source-defined constituent content, so the action cannot support complete field-level fidelity decisions."
                if truncated else
                "The source-defined action contains several independently meaningful steps that remain preserved only in prose and require structured constituent enrichment."
            ),
            "detected_fidelity_defects": [
                "compound-normative-propositions", "constituent-semantics-loss"
            ],
            "affected_metadata_dimensions": affected,
            "review_status": "queued",
            "source_access_basis": "direct-public-primary",
            "recommended_repair": "constituent-enrichment-preserve-identity",
        })

    record = by_id[CYCLONEDX_MODALITY_DEFECT]
    entries.append({
        "current_requirement_id": record["requirement_id"],
        "vigil_source_id": record["vigil_source_id"],
        "external_source_id": record["external_source_id"],
        "source_version": record["source_version"],
        "clause_or_control": record["clause_or_control"],
        "reason": (
            "The current record combines the mandatory bom-ref uniqueness rule with the "
            "recommended reserved-prefix constraint and represents both as mandatory."
        ),
        "detected_fidelity_defects": [
            "compound-normative-propositions", "modality-loss"
        ],
        "affected_metadata_dimensions": ["exceptions_or_qualifications"],
        "review_status": "queued",
        "source_access_basis": "direct-public-primary",
        "recommended_repair": "semantic-decomposition-with-identity-migration",
    })
    return sorted(entries, key=lambda entry: entry["current_requirement_id"])


def seed(write: bool) -> int:
    req_doc = load(REQUIREMENTS)
    ledger = load(LEDGER)
    records = req_doc["requirements"]
    by_id = {record["requirement_id"]: record for record in records}
    selected = [record for record in records if record["vigil_source_id"] in {NIST_RMF, CYCLONEDX, NIST_GAI}]
    counts = {source: sum(record["vigil_source_id"] == source for record in selected) for source in (NIST_RMF, CYCLONEDX, NIST_GAI)}
    if counts != {NIST_RMF: 71, CYCLONEDX: 4, NIST_GAI: 223}:
        raise ValueError(f"unexpected reviewed source population: {counts}")

    for record in selected:
        if record["vigil_source_id"] == NIST_GAI:
            normalize_nist_gai_actor_metadata(record)
        record["source_review_date"] = "2026-08-26"

    backlog = backlog_entries(records)
    affected_by_id = {
        entry["current_requirement_id"]: set(entry["affected_metadata_dimensions"])
        for entry in backlog
    }
    existing = {entry["requirement_id"]: entry for entry in ledger.get("entries", [])}
    seeded = 0
    for record in selected:
        rid = record["requirement_id"]
        affected = affected_by_id.get(rid, set())
        field_status = {}
        for field in FIELDS:
            if field in affected:
                field_status[field] = "review-required"
            else:
                field_status[field] = (
                    "populated-reviewed" if record.get(field) else "not-specified-by-source"
                )
        if record["vigil_source_id"] == NIST_RMF:
            notes = [
                "Reviewed against NIST AI 100-1 Core Tables 1-4; the source-defined subcategory remains the assessable outcome unit.",
                "Populated metadata was checked against the cited subcategory and framework context; empty fields were resolved only after direct primary-text review."
            ]
        elif record["vigil_source_id"] == CYCLONEDX:
            notes = [
                "Reviewed against the CycloneDX 1.7 JSON schema at release commit 4b3f59453366e27c8073fd24e98bf21ef8892c8e.",
                "Normative modality, component-type applicability, model-card structure and bom-ref constraints were checked directly."
            ]
        else:
            notes = [
                "Reviewed against NIST AI 600-1; action identity, source-level actor applicability, timing, outputs and assessment language were checked directly.",
                "The source's subcategory-level AI Actor Tasks are preserved as source-defined tags rather than attributed to every suggested action.",
                "Fields affected by a queued constituent-semantics defect remain review-required instead of being padded with generic metadata."
            ]
        entry = {
            "requirement_id": rid,
            "reviewed_at": "2026-08-26",
            "review_basis": "direct-primary-text",
            "review_notes": notes,
            "field_status": field_status,
        }
        current = existing.get(rid)
        if current is not None and current != entry:
            raise ValueError(f"existing metadata-review decision differs for {rid}; manual reconciliation required")
        if current is None:
            existing[rid] = entry
            seeded += 1

    output_ledger = {
        "schema_version": ledger.get("schema_version", "1.0"),
        "updated_at": "2026-08-26",
        "entries": sorted(existing.values(), key=lambda entry: entry["requirement_id"]),
    }
    output_backlog = {"schema_version": "1.0", "updated_at": "2026-08-26", "entries": backlog}
    print(
        "Reviewed-source metadata seed valid: "
        f"{len(selected)} requirements; {seeded} new ledger entries; {len(backlog)} backlog entries"
    )
    if write:
        REQUIREMENTS.write_text(json.dumps(req_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        LEDGER.write_text(json.dumps(output_ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        BACKLOG.write_text(json.dumps(output_backlog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {REQUIREMENTS}")
        print(f"Wrote {LEDGER}")
        print(f"Wrote {BACKLOG}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    raise SystemExit(seed(args.write))


if __name__ == "__main__":
    main()
