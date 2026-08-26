#!/usr/bin/env python3
"""Apply and seed the directly reviewed non-EU metadata slices.

The decisions in this script are intentionally limited to NIST AI RMF 1.0,
CycloneDX 1.7, NIST AI 600-1 and IMDA Agentic AI MGF 1.5. They were made from
the cited public primary sources on 2026-08-26. This is not a generic
empty-field classifier.
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
IMDA_AGENTIC = "EXT-3CCBC407EAC8"
CYCLONEDX_MODALITY_DEFECT = "EXTREQ-FA1B882FFAD54D93"

IMDA_SCOPE = (
    "The framework applies to organizations looking to deploy agentic AI, "
    "whether they develop agents in-house or use third-party agentic solutions."
)

# Direct review of IMDA MGF 1.5 found eight semantically over-compressed 2.1
# records and twelve records whose section-level locator masks the actual
# subsection proposition. Affected fields stay unresolved; the canonical
# records are not silently repaired in this metadata pass.
IMDA_BACKLOG = {
    "EXTREQ-14B4DA1E7646754E": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse"],
        ["governed_object", "timing_or_frequency", "required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary adds number, value and duration limits that are not the cited section's general agent-limits proposition and combines them with scope-of-impact controls.",
    ),
    "EXTREQ-3B91F9DF01838676": (
        ["constituent-semantics-loss", "condition-loss"],
        ["timing_or_frequency", "applicability_conditions", "exceptions_or_qualifications"],
        "The source requires evaluation of whether residual risk is tolerable and can be accepted; the summary adds further-treatment and avoidance alternatives not stated in that proposition.",
    ),
    "EXTREQ-3E386D665B98BDEA": (
        ["compound-normative-propositions", "constituent-semantics-loss"],
        ["governed_object", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary recombines distinct impact factors for sensitive data and external-system access and adds tool criticality without preserving the source-defined factor boundaries.",
    ),
    "EXTREQ-7B1019B56EF6F868": (
        ["constituent-semantics-loss", "condition-loss"],
        ["governed_object", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary adds consequences for affected parties while compressing the source's distinct domain, error-tolerance and business-process criticality considerations.",
    ),
    "EXTREQ-5513796D63BEB71E": (
        ["constituent-semantics-loss", "output-or-artefact-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The source calls for centrally issuing and tracking agent identities and attendant permissions; the summary adds owners, purposes and operating status.",
    ),
    "EXTREQ-844AFD2FC9FB59FD": (
        ["compound-normative-propositions", "constituent-semantics-loss", "output-or-artefact-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "applicability_conditions", "exceptions_or_qualifications"],
        "The source requires recording the capacities in which an agent acts for auditability; the summary adds distinguishability in interactions and does not preserve the record's content boundary.",
    ),
    "EXTREQ-F3EBD6E34FEFE18E": (
        ["constituent-semantics-loss", "output-or-artefact-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "applicability_conditions", "exceptions_or_qualifications"],
        "The source requires delegations of authority to be clearly recorded; the summary adds sub-delegation chains and a separate attribution outcome.",
    ),
    "EXTREQ-F477502DEE0603FE": (
        ["actor-loss", "condition-loss", "constituent-semantics-loss"],
        ["applicable_actor", "governed_object", "applicability_conditions", "exceptions_or_qualifications"],
        "The source limits what an authorising human user may set for an agent; the summary changes the actor and extends the rule to organisational authority generally.",
    ),
    "EXTREQ-2DC8F2B745E464D5": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse", "condition-loss"],
        ["required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The section-level summary combines responsibility allocation with several separate external-party transparency and information-sharing practices from subsection 2.2.1.",
    ),
    "EXTREQ-82D791A7B54305B0": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse"],
        ["applicability_conditions", "exceptions_or_qualifications"],
        "The section-level locator compresses multiple source-defined internal roles and lifecycle responsibilities in subsection 2.2.1.",
    ),
    "EXTREQ-90553A3F265B9C63": (
        ["constituent-semantics-loss", "locator-too-coarse", "output-or-artefact-loss", "condition-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The source addresses security arrangements, performance guarantees and data protection in terms or contracts; the summary substitutes access and response obligations.",
    ),
    "EXTREQ-DB1BC74DC84D4718": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse", "timing-loss"],
        ["timing_or_frequency", "required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary compresses subsection 2.2.2's separate approval-boundary, approval-quality, oversight-audit, training and automated-monitoring propositions.",
    ),
    "EXTREQ-1F35B4A263EF7055": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse", "output-or-artefact-loss"],
        ["required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary omits subsection 2.3.3's express logging, reporting, failsafe, intervention, debugging and periodic-audit outputs while using a whole-section locator.",
    ),
    "EXTREQ-99712BA8308E32FF": (
        ["locator-too-coarse"], [],
        "The proposition is supported by subsection 2.3.2, but the current locator identifies only section 2.3.",
    ),
    "EXTREQ-DCFA4FF526B6439C": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse"],
        ["governed_object", "applicability_conditions", "exceptions_or_qualifications"],
        "The generic whole-section summary does not preserve subsection 2.3.1's distinct control-selection propositions for agent components, security surfaces and multi-agent interactions.",
    ),
    "EXTREQ-DFAE10B7FA4CAEEF": (
        ["timing-loss", "constituent-semantics-loss", "locator-too-coarse"],
        ["timing_or_frequency", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The source separately requires continuous post-deployment testing and change reviews triggered by technical, environmental, performance or regulatory changes; the summary conflates those propositions.",
    ),
    "EXTREQ-FE078DDB1FABA3AF": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse", "condition-loss"],
        ["governed_object", "timing_or_frequency", "required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary combines distinct runtime intervention, human-approval, termination and fallback practices and adds revocation without a precise subsection locator.",
    ),
    "EXTREQ-24F5ABCB4CAFC499": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse", "condition-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary combines information for interacting users and training for integrating users, which have different source-defined applicability in subsections 2.4.2 and 2.4.3.",
    ),
    "EXTREQ-4253F163EB11C1C9": (
        ["constituent-semantics-loss", "locator-too-coarse", "condition-loss"],
        ["governed_object", "applicability_conditions", "exceptions_or_qualifications"],
        "The source requires point-of-interaction disclosure to users who interact with agents; the summary adds people materially affected by a system.",
    ),
    "EXTREQ-47EE577CC52EF131": (
        ["constituent-semantics-loss", "locator-too-coarse", "output-or-artefact-loss", "condition-loss"],
        ["required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The source calls for responsible human contact points for malfunction or dissatisfaction; the summary adds help, reporting and challenge channels and the metadata invents a required report.",
    ),
}

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


def set_reviewed_metadata(record: dict, field: str, values: list[str]) -> None:
    current = record.get(field, [])
    if current not in ([], values):
        raise ValueError(
            f"unexpected {field} metadata for {record['requirement_id']}: {current!r}"
        )
    record[field] = values


def normalize_imda_metadata(record: dict) -> None:
    set_reviewed_metadata(record, "applicability_conditions", [IMDA_SCOPE])
    rid = record["requirement_id"]
    if rid == "EXTREQ-4B28B179BF91F130":
        set_reviewed_metadata(
            record,
            "timing_or_frequency",
            ["Before deciding to develop or deploy an agentic AI use case."],
        )
    elif rid == "EXTREQ-99712BA8308E32FF":
        set_reviewed_metadata(
            record,
            "required_artefacts",
            ["Agent safety and security test results."],
        )
        set_reviewed_metadata(
            record,
            "verification_method",
            [
                "Pre-deployment testing of complete workflows, individual and multi-agent behavior, realistic environments, varied datasets and repeated runs."
            ],
        )
    elif rid == "EXTREQ-C867BF4ECD4B5161":
        set_reviewed_metadata(
            record,
            "verification_method",
            ["Threat modelling supported by taint tracing of workflows, interactions and untrusted-data flows."],
        )


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

    migrate = {
        "EXTREQ-14B4DA1E7646754E", "EXTREQ-2DC8F2B745E464D5",
        "EXTREQ-DB1BC74DC84D4718", "EXTREQ-1F35B4A263EF7055",
        "EXTREQ-DCFA4FF526B6439C", "EXTREQ-DFAE10B7FA4CAEEF",
        "EXTREQ-FE078DDB1FABA3AF", "EXTREQ-24F5ABCB4CAFC499",
    }
    for rid, (defects, affected, reason) in sorted(IMDA_BACKLOG.items()):
        record = by_id.get(rid)
        if record is None or record.get("vigil_source_id") != IMDA_AGENTIC:
            raise ValueError(f"IMDA backlog ID does not resolve to the reviewed source: {rid}")
        entries.append({
            "current_requirement_id": rid,
            "vigil_source_id": record["vigil_source_id"],
            "external_source_id": record["external_source_id"],
            "source_version": record["source_version"],
            "clause_or_control": record["clause_or_control"],
            "reason": reason,
            "detected_fidelity_defects": defects,
            "affected_metadata_dimensions": affected,
            "review_status": "queued",
            "source_access_basis": "direct-public-primary",
            "recommended_repair": (
                "semantic-decomposition-with-identity-migration"
                if rid in migrate else
                "constituent-enrichment-preserve-identity"
            ),
        })
    return sorted(entries, key=lambda entry: entry["current_requirement_id"])


def seed(write: bool) -> int:
    req_doc = load(REQUIREMENTS)
    ledger = load(LEDGER)
    records = req_doc["requirements"]
    by_id = {record["requirement_id"]: record for record in records}
    reviewed_sources = {NIST_RMF, CYCLONEDX, NIST_GAI, IMDA_AGENTIC}
    selected = [record for record in records if record["vigil_source_id"] in reviewed_sources]
    counts = {
        source: sum(record["vigil_source_id"] == source for record in selected)
        for source in reviewed_sources
    }
    if counts != {NIST_RMF: 71, CYCLONEDX: 4, NIST_GAI: 223, IMDA_AGENTIC: 32}:
        raise ValueError(f"unexpected reviewed source population: {counts}")

    for record in selected:
        if record["vigil_source_id"] == NIST_GAI:
            normalize_nist_gai_actor_metadata(record)
        elif record["vigil_source_id"] == IMDA_AGENTIC:
            normalize_imda_metadata(record)
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
        elif record["vigil_source_id"] == NIST_GAI:
            notes = [
                "Reviewed against NIST AI 600-1; action identity, source-level actor applicability, timing, outputs and assessment language were checked directly.",
                "The source's subcategory-level AI Actor Tasks are preserved as source-defined tags rather than attributed to every suggested action.",
                "Fields affected by a queued constituent-semantics defect remain review-required instead of being padded with generic metadata."
            ]
        else:
            notes = [
                "Reviewed against IMDA Model AI Governance Framework for Agentic AI version 1.5, published 20 May 2026 and updated 5 June 2026.",
                "The official PDF was retrieved directly from IMDA; SHA-256 2636e19ff1c86e862394d2fc900592e97b83c04cc35e3c8443108114b7f1dfba.",
                "The framework-wide deployment scope is source-explicit; fields affected by over-compression or a section-level locator remain review-required pending deterministic re-extraction."
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
