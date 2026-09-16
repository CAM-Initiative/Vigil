#!/usr/bin/env python3
"""Completed evidence-derived VIGIL-HIM 1.0.0 corpus adjudication.

This historical migration records the explicit Incident-by-Incident decisions
used for the 2026-09-16 pre-merge correction. It is not runtime machinery.
Execution requires ``--apply`` and is intended only for reproducing the audited
branch transformation from its immediately preceding state.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
INCIDENTS = ROOT / "vigil" / "records" / "incidents"
MATRIX_PATH = ROOT / "vigil" / "methodologies" / "VIGIL.HarmImpactMatrix.v1.0.0.json"
DATE = "2026-09-16"
RANK = {"S1": 1, "S2": 2, "S3": 3, "S4": 4, "S5": 5}

LABELS = {
    "physical-health-safety": "physical health and safety",
    "psychological-wellbeing": "psychological wellbeing",
    "rights-liberty": "rights and liberty",
    "equal-treatment": "equal treatment and non-discrimination",
    "privacy-confidentiality": "privacy and confidentiality",
    "financial-economic": "financial and economic",
    "property-asset-damage": "property and asset damage",
    "service-operational-infrastructure": "service, operational and infrastructure",
    "reputation-dignity": "reputation and dignity",
    "societal-democratic": "societal and democratic",
    "environmental": "environmental",
}

# Explicit decisions following review of each Incident's summary, factual basis,
# source relevance, access limits and published quantitative information.
DECISIONS: dict[str, list[tuple[str, str]]] = {
    "VIGIL-INC-000001": [("property-asset-damage", "S3"), ("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000002": [("societal-democratic", "S3")],
    "VIGIL-INC-000003": [("privacy-confidentiality", "S3"), ("property-asset-damage", "S3")],
    "VIGIL-INC-000004": [("property-asset-damage", "S3")],
    "VIGIL-INC-000005": [("rights-liberty", "S3")],
    "VIGIL-INC-000006": [("rights-liberty", "S3")],
    "VIGIL-INC-000007": [("rights-liberty", "S3")],
    "VIGIL-INC-000008": [("rights-liberty", "S4")],
    "VIGIL-INC-000009": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000010": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000011": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000013": [("privacy-confidentiality", "S3")],
    "VIGIL-INC-000014": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000015": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000016": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000017": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000018": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000019": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000020": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000021": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000022": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000023": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000024": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000025": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000026": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000027": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000029": [("psychological-wellbeing", "S5")],
    "VIGIL-INC-000030": [("rights-liberty", "S5")],
    "VIGIL-INC-000031": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000032": [("property-asset-damage", "S3")],
    "VIGIL-INC-000034": [("psychological-wellbeing", "S2")],
    "VIGIL-INC-000035": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000036": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000038": [("service-operational-infrastructure", "S4")],
    "VIGIL-INC-000039": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000041": [("rights-liberty", "S3")],
    "VIGIL-INC-000042": [("reputation-dignity", "S2")],
    "VIGIL-INC-000043": [("reputation-dignity", "S2")],
    "VIGIL-INC-000044": [("psychological-wellbeing", "S3"), ("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000045": [("privacy-confidentiality", "S3")],
    "VIGIL-INC-000047": [("rights-liberty", "S4")],
    "VIGIL-INC-000048": [("rights-liberty", "S4"), ("equal-treatment", "S3")],
    "VIGIL-INC-000049": [("financial-economic", "S3")],
    "VIGIL-INC-000050": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000051": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000052": [("societal-democratic", "S2")],
    "VIGIL-INC-000053": [("financial-economic", "S3")],
    "VIGIL-INC-000054": [("reputation-dignity", "S4")],
    "VIGIL-INC-000055": [("property-asset-damage", "S3")],
    "VIGIL-INC-000056": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000057": [("privacy-confidentiality", "S3")],
    "VIGIL-INC-000058": [("societal-democratic", "S2")],
    "VIGIL-INC-000059": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000060": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000062": [("physical-health-safety", "S4")],
    "VIGIL-INC-000064": [("rights-liberty", "S5"), ("reputation-dignity", "S4")],
    "VIGIL-INC-000066": [("reputation-dignity", "S3"), ("societal-democratic", "S2")],
    "VIGIL-INC-000067": [("privacy-confidentiality", "S3")],
    "VIGIL-INC-000068": [("privacy-confidentiality", "S3")],
    "VIGIL-INC-000069": [("privacy-confidentiality", "S3")],
    "VIGIL-INC-000070": [("privacy-confidentiality", "S3")],
    "VIGIL-INC-000072": [("property-asset-damage", "S3")],
    "VIGIL-INC-000073": [("privacy-confidentiality", "S3")],
    "VIGIL-INC-000074": [("financial-economic", "S3")],
    "VIGIL-INC-000075": [("privacy-confidentiality", "S4"), ("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000076": [("rights-liberty", "S3")],
    "VIGIL-INC-000077": [("privacy-confidentiality", "S3"), ("financial-economic", "S1")],
    "VIGIL-INC-000078": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000079": [("reputation-dignity", "S2"), ("societal-democratic", "S2")],
    "VIGIL-INC-000080": [("societal-democratic", "S3")],
    "VIGIL-INC-000082": [("privacy-confidentiality", "S3"), ("financial-economic", "S1"), ("reputation-dignity", "S3")],
    "VIGIL-INC-000083": [("financial-economic", "S3")],
    "VIGIL-INC-000084": [("privacy-confidentiality", "S3"), ("property-asset-damage", "S3")],
    "VIGIL-INC-000085": [("privacy-confidentiality", "S3"), ("property-asset-damage", "S3"), ("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000086": [("property-asset-damage", "S3")],
    "VIGIL-INC-000088": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000089": [("societal-democratic", "S3")],
    "VIGIL-INC-000090": [("service-operational-infrastructure", "S4"), ("societal-democratic", "S4")],
    "VIGIL-INC-000091": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000092": [("privacy-confidentiality", "S2")],
    "VIGIL-INC-000094": [("property-asset-damage", "S3"), ("privacy-confidentiality", "S3")],
    "VIGIL-INC-000095": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000096": [("privacy-confidentiality", "S4")],
    "VIGIL-INC-000097": [("privacy-confidentiality", "S3")],
    "VIGIL-INC-000098": [("reputation-dignity", "S3"), ("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000099": [("societal-democratic", "S3")],
    "VIGIL-INC-000100": [("service-operational-infrastructure", "S3"), ("physical-health-safety", "S1")],
    "VIGIL-INC-000102": [("psychological-wellbeing", "S4"), ("financial-economic", "S3")],
    "VIGIL-INC-000103": [("psychological-wellbeing", "S4"), ("rights-liberty", "S3")],
    "VIGIL-INC-000104": [("psychological-wellbeing", "S4"), ("physical-health-safety", "S3")],
    "VIGIL-INC-000105": [("psychological-wellbeing", "S3")],
    "VIGIL-INC-000106": [("reputation-dignity", "S3"), ("societal-democratic", "S3")],
    "VIGIL-INC-000107": [("privacy-confidentiality", "S4")],
    "VIGIL-INC-000109": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000110": [("privacy-confidentiality", "S4"), ("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000111": [("privacy-confidentiality", "S3")],
    "VIGIL-INC-000112": [("privacy-confidentiality", "S3"), ("property-asset-damage", "S3")],
    "VIGIL-INC-000113": [("privacy-confidentiality", "S4")],
    "VIGIL-INC-000114": [("rights-liberty", "S3"), ("financial-economic", "S1")],
    "VIGIL-INC-000115": [("rights-liberty", "S3")],
    "VIGIL-INC-000116": [("service-operational-infrastructure", "S4")],
    "VIGIL-INC-000117": [("service-operational-infrastructure", "S3")],
    "VIGIL-INC-000118": [("privacy-confidentiality", "S4"), ("property-asset-damage", "S3")],
    "VIGIL-INC-000119": [("privacy-confidentiality", "S4"), ("property-asset-damage", "S4")],
    "VIGIL-INC-000121": [("service-operational-infrastructure", "S2")],
    "VIGIL-INC-000127": [("privacy-confidentiality", "S4"), ("property-asset-damage", "S4")],
}

NO_MATERIALISED_HARM = {
    "VIGIL-INC-000093": "All network access, repositories, systems and tool calls were simulated in the UK AISI evaluation; the preserved evidence positively establishes no real external system or person was harmed.",
    "VIGIL-INC-000108": "The occurrence was a controlled proof of concept using researcher-controlled accounts and data; the preserved evidence establishes the demonstrated channel was decommissioned and does not identify an external victim or production data loss.",
    "VIGIL-INC-000120": "The reported drone-swarm work remained at simulation and early board-validation stage; the preserved evidence positively states that no operational fielded swarm or casualties resulted.",
    "VIGIL-INC-000122": "The observed alignment-faking behaviour occurred only in the controlled research settings; the preserved evidence establishes no external user, organisation or production system was affected.",
    "VIGIL-INC-000123": "The side-objective and monitor-avoidance behaviour occurred only inside SHUSHCAST; the preserved evidence establishes no external system, user or organisation was affected.",
    "VIGIL-INC-000124": "The training intervention, checkpoint and reporting behaviour occurred only in a fictional simulation; the preserved evidence establishes no real pipeline, organisation or external system was affected.",
    "VIGIL-INC-000125": "The incorrect transcript labels occurred only in the controlled judge experiments; the preserved evidence establishes no production training set, external user or deployed service was affected.",
    "VIGIL-INC-000126": "The protected-escalation sequence involved fictional staff, files and organisations; the preserved evidence positively establishes no real person, organisation or external system was affected.",
}

INSUFFICIENT = {
    "VIGIL-INC-000012": ("psychological-wellbeing", "The source establishes dependence-oriented system language but does not establish resulting user distress, dependency or impairment sufficient to band psychological harm."),
    "VIGIL-INC-000028": ("service-operational-infrastructure", "The user report indicates possible retained or contaminated memory context, but the accessible evidence cannot establish scope, persistence or materialised downstream impact."),
    "VIGIL-INC-000033": ("service-operational-infrastructure", "The report describes a possible prompt-injection evasion technique, but the originating technical report, sample, affected scanner and operational consequence were not recovered."),
    "VIGIL-INC-000037": ("service-operational-infrastructure", "The public URL does not expose enough of the prompt, transformed prompt, refusal or runtime state to band any materialised impact."),
    "VIGIL-INC-000040": ("societal-democratic", "The reporting establishes legal model-access transactions and later suspected-distillation suspensions, but does not establish a materialised societal, democratic or other downstream harm."),
    "VIGIL-INC-000061": ("rights-liberty", "The evidence reports 67,868 grant suspensions but does not establish how many were caused by facial-verification failure, so the attributable rights impact cannot be banded."),
    "VIGIL-INC-000063": ("physical-health-safety", "The evidence establishes inaccurate health guidance but no resulting treatment decision, injury or clinical outcome from which to band materialised health harm."),
    "VIGIL-INC-000065": ("reputation-dignity", "The deepfake-pornography distribution allegation is disputed and the preserved evidence cannot establish the occurrence and consequence strongly enough to band dignitary harm."),
    "VIGIL-INC-000081": ("financial-economic", "The observed fare differences and broader surveillance-pricing concerns do not establish a causal pricing input, aggregate overcharge or realised loss that can be banded."),
    "VIGIL-INC-000101": ("psychological-wellbeing", "OpenAI established a globally deployed sycophantic behaviour and rollback, but did not publish a materially harmed cohort or occurrence-level downstream psychological consequence that can be banded."),
}

FINANCIAL_VALUES = {
    "VIGIL-INC-000049": [{"metric": "reported realised loss", "value": 25000000, "unit": "USD"}],
    "VIGIL-INC-000053": [{"metric": "reported unauthorised transfers", "value": 10.70, "unit": "INR crore", "conversion_status": "not-converted"}],
    "VIGIL-INC-000077": [{"metric": "reported realised loss", "value": 4820, "unit": "USD"}],
    "VIGIL-INC-000082": [{"metric": "reported realised loss", "value": 4820, "unit": "USD"}],
    "VIGIL-INC-000083": [{"metric": "reported aggregate loss", "value": 7400000, "unit": "AUD", "conversion_status": "not-converted"}],
    "VIGIL-INC-000114": [{"metric": "court-imposed sanction", "value": 5000, "unit": "USD"}],
}

RATIONALES = {
    ("VIGIL-INC-000003", "privacy-confidentiality"): "The evidence supports bounded access to credentials, held-out solution material and production systems. It does not establish a large-scale or effectively irreversible disclosure.",
    ("VIGIL-INC-000003", "property-asset-damage"): "The evidence supports unauthorised production-system compromise and modification requiring recovery, but not an outage, critical-asset destruction or the operational criteria for S4.",
    ("VIGIL-INC-000049", "financial-economic"): "The reported US$25 million realised loss is at least USD 1 million and below USD 100 million.",
    ("VIGIL-INC-000053", "financial-economic"): "The source reports INR 10.70 crore without a defensible USD conversion basis. The evidence nevertheless establishes a material but bounded organisational loss; no USD amount is implied.",
    ("VIGIL-INC-000077", "financial-economic"): "The reported US$4,820 realised loss is below USD 10,000. Financial harm is assessed independently from the identity-document disclosure.",
    ("VIGIL-INC-000082", "financial-economic"): "The reported US$4,820 realised loss is below USD 10,000. Financial harm is assessed independently from privacy and professional-identity harms.",
    ("VIGIL-INC-000083", "financial-economic"): "The source reports A$7.4 million without a recorded USD conversion basis. The regulator evidence establishes material but bounded multi-victim economic loss; no USD amount is implied.",
    ("VIGIL-INC-000100", "physical-health-safety"): "Police and operator reporting positively establishes that passengers exited safely and no injuries were recorded.",
    ("VIGIL-INC-000114", "financial-economic"): "The court-imposed US$5,000 sanction is below USD 10,000 and is assessed separately from the procedural rights impact.",
    ("VIGIL-INC-000127", "privacy-confidentiality"): "Credential and domain-secret harvesting affected hundreds of instances; twelve organisations reached domain-administrator compromise and full credential databases were exfiltrated.",
    ("VIGIL-INC-000127", "property-asset-damage"): "The evidence establishes substantial multi-organisation and multi-jurisdiction compromise of important production assets requiring incident response, while not establishing catastrophic destruction.",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def increment_patch(version: str) -> str:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", version)
    if not match:
        raise ValueError(f"unsupported record version {version!r}")
    major, minor, patch = map(int, match.groups())
    return f"{major}.{minor}.{patch + 1}"


def legacy_severity(record: dict) -> str:
    for review in reversed(record["interpretive_provenance"]["review_history"]):
        outcome = str(review.get("review_outcome", ""))
        changed = re.search(r"changed overall severity from (S[1-5]|SU) to", outcome)
        if changed:
            return changed.group(1)
        legacy = re.search(r"legacy severity was (S[1-5]|SU)", outcome)
        if legacy:
            return legacy.group(1)
    raise ValueError(f"{record['id']}: legacy severity not recoverable from review history")


def evidence_refs(record: dict) -> list[str]:
    preferred_url = record["preferred_evidence"]["source_url"]
    refs: list[str] = []
    for index, source in enumerate(record["source_records"]):
        role = source.get("source_role")
        if source.get("source_url") == preferred_url or role in {"affected-party-evidence", "direct-testimony"}:
            if role not in {"record-cross-reference", "contextual-background"}:
                refs.append(f"source_records[{index}]")
    if not refs:
        raise ValueError(f"{record['id']}: no substantive preferred Harm Impact evidence")
    return refs


def confidence(record: dict, refs: list[str]) -> str:
    indices = [int(re.fullmatch(r"source_records\[(\d+)\]", ref).group(1)) for ref in refs]
    statuses = {record["source_records"][index].get("evidence_status") for index in indices}
    low_statuses = {"disputed", "unverified", "user-reported", "allegation-on-record"}
    if statuses and statuses <= low_statuses:
        return "low"
    if statuses & {"verified", "independently-corroborated", "internal-observation"}:
        return "high"
    if "first-party-reported" in statuses and len(refs) > 1:
        return "high"
    return "medium"


def retained_observed_values(record: dict, dimension_id: str) -> list[dict]:
    if dimension_id == "financial-economic" and record["id"] in FINANCIAL_VALUES:
        return FINANCIAL_VALUES[record["id"]]
    values = [
        value
        for row in record["harm_impact_assessment"].get("dimensions", [])
        if isinstance(row, dict)
        for value in row.get("observed_values", [])
        if isinstance(value, dict)
    ]
    return values[:1]


def unreported_row(dimension_id: str) -> dict:
    return {
        "dimension_id": dimension_id,
        "assessment_status": "unreported",
        "assessment_basis": f"The preserved Incident evidence does not report a bandable materialised {LABELS[dimension_id]} impact; absence of reporting is not evidence of no harm.",
        "evidence_confidence": "not-assessed",
    }


def transform(record: dict, matrix: dict) -> dict:
    record_id = record["id"]
    initial_matrix_severity = record["harm_impact_assessment"]["overall_severity"]
    legacy = legacy_severity(record)
    dimensions = [item["dimension_id"] for item in matrix["dimensions"]]
    thresholds = {
        (item["dimension_id"], severity): threshold
        for item in matrix["dimensions"]
        for severity, threshold in item["thresholds"].items()
    }
    rows = [unreported_row(dimension_id) for dimension_id in dimensions]
    by_id = {row["dimension_id"]: row for row in rows}

    if record_id in NO_MATERIALISED_HARM:
        basis = NO_MATERIALISED_HARM[record_id]
        for dimension_id in dimensions:
            by_id[dimension_id].update({
                "assessment_status": "not-applicable",
                "assessment_basis": f"{basis} No {LABELS[dimension_id]} consequence materialised within that bounded evidence boundary.",
            })
        overall = "S1"
        controlling: list[str] = []
        coverage = "Positive evidence establishes a bounded occurrence with no materialised downstream harm. No artificial controlling harm dimension is assigned."
        extra = {"no_materialised_harm_basis": basis}
    elif record_id in INSUFFICIENT:
        dimension_id, gap = INSUFFICIENT[record_id]
        by_id[dimension_id].update({
            "assessment_status": "insufficient-evidence",
            "assessment_basis": gap,
        })
        overall = "SU"
        controlling = []
        coverage = "No dimension can be assigned a defensible band. The identified impact dimension has some evidence but remains unbanded; all other dimensions are unreported."
        extra = {"assessment_gap": gap}
    else:
        decisions = DECISIONS.get(record_id)
        if not decisions:
            raise ValueError(f"{record_id}: no evidence adjudication decision")
        refs = evidence_refs(record)
        assessment_confidence = confidence(record, refs)
        for dimension_id, severity in decisions:
            threshold = thresholds[(dimension_id, severity)]
            rationale = RATIONALES.get((record_id, dimension_id))
            if not rationale:
                rationale = (
                    f"The preserved sources establish the bounded consequence described in the Incident summary: {record['summary']} "
                    f"Unreported downstream consequences were not inferred."
                )
            row = by_id[dimension_id]
            row.clear()
            row.update({
                "dimension_id": dimension_id,
                "assessment_status": "assessed",
                "severity": severity,
                "threshold_id": threshold["threshold_id"],
                "observed_values": retained_observed_values(record, dimension_id),
                "assessment_basis": f"{rationale} Threshold applied: {threshold['criterion']}",
                "evidence_confidence": assessment_confidence,
                "evidence_refs": refs,
            })
        overall = max((severity for _, severity in decisions), key=RANK.__getitem__)
        controlling = sorted(dimension_id for dimension_id, severity in decisions if severity == overall)
        assessed_labels = ", ".join(LABELS[dimension_id] for dimension_id, _ in decisions)
        coverage = f"The preserved evidence independently supports assessed harm in: {assessed_labels}. Other dimensions remain unreported unless specifically assessed; they do not lower or raise the derived result."
        extra = {}

    assessment = {
        "methodology_id": matrix["methodology_id"],
        "methodology_version": matrix["version"],
        "derivation_rule": matrix["derivation_rule"],
        "assessed_on": DATE,
        "overall_severity": overall,
        "controlling_dimensions": controlling,
        "coverage_note": coverage,
        "dimensions": rows,
        **extra,
    }
    record["harm_impact_assessment"] = assessment
    identity = record["record_identity"]
    identity["updated"] = DATE
    identity["version"] = increment_patch(identity["version"])

    review_id = f"VIGIL-REVIEW-2026-09-16-HIM-EVIDENCE-{record_id[-6:]}"
    review = {
        "review_id": review_id,
        "reviewer_type": "AI analytical reviewer",
        "reviewer_platform": "OpenAI Codex",
        "reviewer_model": "GPT-5",
        "review_date": DATE,
        "review_scope": "Full-corpus evidence-derived Harm Impact Matrix re-adjudication; legacy severity was comparison-only and Failure Taxonomy and source-role decisions were not reopened.",
        "capability_profile": {
            "direct_repository_analysis": True,
            "direct_text_analysis": True,
            "structured_threshold_comparison": True,
        },
        "known_limitations": [
            "The assessment is bounded to evidence already preserved in the Incident and does not infer unreported harms, losses, durations, conversions or affected populations.",
            "Non-USD amounts remain unconverted unless a conversion source and rate date are explicitly recorded.",
        ],
        "review_outcome": f"Evidence-derived VIGIL-HIM 1.0.0 overall severity is {overall}; legacy narrative severity was {legacy} and the superseded initial matrix result was {initial_matrix_severity}. Controlling dimensions: {', '.join(controlling) if controlling else 'none'}.",
    }
    provenance = record["interpretive_provenance"]
    provenance["review_history"].append(review)
    provenance["current_ai_review"] = review.copy()
    return {
        "id": record_id,
        "legacy_severity": legacy,
        "initial_matrix_severity": initial_matrix_severity,
        "derived_severity": overall,
        "controlling_dimensions": controlling,
        "assessed_dimensions": [row["dimension_id"] for row in rows if row["assessment_status"] == "assessed"],
        "changed_from_legacy": legacy != overall,
        "requires_human_review": overall == "SU",
    }


def main() -> None:
    if "--apply" not in sys.argv:
        raise SystemExit("Completed historical migration; pass --apply only to reproduce the audited transformation.")
    matrix = load(MATRIX_PATH)
    results = []
    for path in sorted(INCIDENTS.glob("VIGIL-INC-*.json")):
        record = load(path)
        result = transform(record, matrix)
        save(path, record)
        results.append(result)
    print(json.dumps({
        "records": len(results),
        "distribution": dict(sorted(Counter(item["derived_severity"] for item in results).items())),
        "changed_from_legacy": sum(item["changed_from_legacy"] for item in results),
        "results": results,
    }, indent=2))


if __name__ == "__main__":
    main()
