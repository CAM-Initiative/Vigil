#!/usr/bin/env python3
"""SUPERSEDED historical migration from narrative severity to VIGIL-HIM 1.0.0.

This file preserves the initial legacy-seeded migration for audit history. Its
default-to-legacy-severity and keyword dimension-selection logic was superseded
by the evidence-derived adjudication completed on 2026-09-16. It is not runtime
VIGIL machinery and is unsafe to run against the current corpus.
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

DIMENSION_RULES = [
    ("physical-health-safety", r"\b(death|died|killed|injur\w*|illness|medical|health|hospital|suicid\w*|self-harm|safety|kamikaze)\b"),
    ("psychological-wellbeing", r"\b(emotional|psychological|companion|dependency|distress|love|romantic|mental)\b"),
    ("rights-liberty-equal-treatment", r"\b(arrest\w*|detention|liberty|discrimin\w*|right\w*|child|teenager|pregnant|sexual\w*|porn\w*|essential care|benefit denial)\b"),
    ("privacy-confidentiality", r"\b(privacy|confidential|personal data|data exposure|data leak|conversation exposure|secret|credential)\b"),
    ("financial-economic-property", r"\b(financial|economic|property|fraud\w*|scam\w*|loss\w*|monetary|dollar|usd|£|€|livelihood|insolvency)\b"),
    ("reputation-dignity", r"\b(reputation|dignit|defam|humiliat|false attribution|fabricated quote|impersonat)\b"),
    ("societal-democratic-environmental", r"\b(election|democra|societ|propaganda|disinformation|influence campaign|public policy|environment|warfare)\b"),
    ("service-operational-infrastructure", r"\b(outage|login|sign-in|unavailable|availability|disruption|error|crash|database|infrastructure|service|production|account|access|capacity|workflow|task|code|system)\b"),
]

DIMENSION_LABELS = {
    "physical-health-safety": "physical health and safety",
    "psychological-wellbeing": "psychological wellbeing",
    "rights-liberty-equal-treatment": "rights, liberty and equal treatment",
    "privacy-confidentiality": "privacy and confidentiality",
    "financial-economic-property": "financial, economic and property",
    "service-operational-infrastructure": "service, operational and infrastructure",
    "reputation-dignity": "reputation and dignity",
    "societal-democratic-environmental": "societal, democratic and environmental",
}

# Record-level choices resolve genuine multi-dimensional wording after reading
# the preserved occurrence evidence; these are impact decisions, not taxonomy mappings.
OVERRIDES = {
    "VIGIL-INC-000001": "service-operational-infrastructure",
    "VIGIL-INC-000002": "societal-democratic-environmental",
    "VIGIL-INC-000003": "service-operational-infrastructure",
    "VIGIL-INC-000004": "service-operational-infrastructure",
    "VIGIL-INC-000005": "rights-liberty-equal-treatment",
    "VIGIL-INC-000006": "rights-liberty-equal-treatment",
    "VIGIL-INC-000007": "rights-liberty-equal-treatment",
    "VIGIL-INC-000008": "rights-liberty-equal-treatment",
    "VIGIL-INC-000029": "psychological-wellbeing",
    "VIGIL-INC-000030": "rights-liberty-equal-treatment",
    "VIGIL-INC-000033": "service-operational-infrastructure",
    "VIGIL-INC-000065": "rights-liberty-equal-treatment",
    "VIGIL-INC-000120": "physical-health-safety",
}

SEVERITY_OVERRIDES = {
    "VIGIL-INC-000004": ("S4", "Live organisational intrusions are substantial, but the record does not establish catastrophic or prolonged essential-service loss required for S5."),
    "VIGIL-INC-000005": ("S4", "Wrongful arrest is a substantial liberty deprivation, but this record does not establish prolonged or enduring detention required for S5."),
    "VIGIL-INC-000006": ("S4", "Wrongful arrest while pregnant is substantial, but the record does not establish grave injury or prolonged/enduring detention required for S5."),
    "VIGIL-INC-000007": ("S4", "Wrongful detention is substantial, but this record does not establish the prolonged or enduring deprivation required for S5."),
    "VIGIL-INC-000049": ("S4", "The reported US$25 million realised loss falls within the VIGIL S4 financial band."),
    "VIGIL-INC-000053": ("S3", "The reported ₹10.70 crore transfer loss supports meaningful bounded financial harm; no USD conversion or S4 qualitative override is evidenced."),
    "VIGIL-INC-000077": ("S3", "The reported US$4,820 loss and identity-document disclosure support meaningful bounded harm, not the S4 financial threshold."),
    "VIGIL-INC-000083": ("S3", "The reported A$7.4 million aggregate loss supports meaningful bounded financial harm; no USD conversion or S4 qualitative override is evidenced."),
}

OBSERVED_VALUE_OVERRIDES = {
    "VIGIL-INC-000049": [{"metric": "reported realised loss", "value": 25000000, "unit": "USD"}],
    "VIGIL-INC-000053": [{"metric": "reported unauthorised transfers", "value": 10.70, "unit": "INR crore", "conversion_status": "not-converted"}],
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


def select_dimension(record: dict, assessment: dict) -> str:
    if record["id"] in OVERRIDES:
        return OVERRIDES[record["id"]]
    text = " ".join(
        str(value) for value in (
            record.get("summary", ""),
            record.get("record_identity", {}).get("title", ""),
            assessment.get("materialised_consequence", ""),
        )
    ).casefold()
    for dimension_id, pattern in DIMENSION_RULES:
        if re.search(pattern, text, re.I):
            return dimension_id
    return "service-operational-infrastructure"


def observed_values(record: dict, assessment: dict) -> list[dict]:
    if record["id"] in OBSERVED_VALUE_OVERRIDES:
        return OBSERVED_VALUE_OVERRIDES[record["id"]]
    quantitative = str(assessment.get("quantitative_information", "")).strip()
    if quantitative and (re.search(r"\d|[$£€₹]", quantitative) or not re.search(r"does not (?:provide|quantify)|no reliable total|not (?:published|quantified|stated)", quantitative, re.I)):
        return [{"metric": "published quantitative information", "qualitative_value": quantitative}]
    return []


def apply_multi_dimension_overrides(record: dict, assessment: dict, matrix: dict) -> None:
    if record["id"] != "VIGIL-INC-000077":
        return
    rows = assessment["dimensions"]
    financial = next(row for row in rows if row["dimension_id"] == "financial-economic-property")
    privacy = next(row for row in rows if row["dimension_id"] == "privacy-confidentiality")
    fin_threshold = next(item for item in matrix["dimensions"] if item["dimension_id"] == "financial-economic-property")["thresholds"]["S2"]
    prv_threshold = next(item for item in matrix["dimensions"] if item["dimension_id"] == "privacy-confidentiality")["thresholds"]["S3"]
    refs = financial.get("evidence_refs") or [f"source_records[{index}]" for index, _ in enumerate(record.get("source_records", []))]
    financial.update({
        "assessment_status": "assessed",
        "severity": "S2",
        "threshold_id": fin_threshold["threshold_id"],
        "assessment_basis": f"The reported victim sent US$4,820. {fin_threshold['criterion']}",
        "evidence_confidence": "medium",
        "evidence_refs": refs,
    })
    privacy.clear()
    privacy.update({
        "dimension_id": "privacy-confidentiality",
        "assessment_status": "assessed",
        "severity": "S3",
        "threshold_id": prv_threshold["threshold_id"],
        "observed_values": [{"metric": "disclosed identity documents", "qualitative_value": "Social Security and residency documents"}],
        "assessment_basis": f"The victim reportedly disclosed Social Security and residency documents to the impersonator. {prv_threshold['criterion']}",
        "evidence_confidence": "medium",
        "evidence_refs": refs,
    })
    assessment["overall_severity"] = "S3"
    assessment["controlling_dimensions"] = ["privacy-confidentiality"]
    assessment["coverage_note"] = "Financial loss and privacy/confidentiality were assessed separately. Privacy controls the S3 overall result; other harm dimensions remain unreported."


def transform(record: dict, matrix: dict) -> tuple[dict, dict]:
    old = record.get("severity_assessment")
    if not isinstance(old, dict):
        current = record.get("harm_impact_assessment", {})
        rows = current.get("dimensions", [])
        old_primary = next((row.get("dimension_id") for row in rows if row.get("assessment_status") in {"assessed", "insufficient-evidence"}), None)
        primary = select_dimension(record, {"materialised_consequence": ""})
        current_severity = current.get("overall_severity")
        if old_primary and current_severity in {"S1", "S2", "S3", "S4", "S5"}:
            assessed_row = next((row for row in rows if row.get("assessment_status") == "assessed"), None)
            if assessed_row:
                canonical_threshold = next(item for item in matrix["dimensions"] if item["dimension_id"] == old_primary)["thresholds"][current_severity]
                basis_prefix = str(assessed_row.get("assessment_basis", "")).split(" Threshold applied:", 1)[0]
                assessed_row["threshold_id"] = canonical_threshold["threshold_id"]
                assessed_row["assessment_basis"] = f"{basis_prefix} Threshold applied: {canonical_threshold['criterion']}"
                if record["id"] in OBSERVED_VALUE_OVERRIDES:
                    assessed_row["observed_values"] = OBSERVED_VALUE_OVERRIDES[record["id"]]
        if old_primary and primary != old_primary:
            severity = current.get("overall_severity")
            source_row = next(row for row in rows if row.get("dimension_id") == old_primary)
            target_row = next(row for row in rows if row.get("dimension_id") == primary)
            status = source_row["assessment_status"]
            replacement = dict(source_row)
            replacement["dimension_id"] = primary
            if status == "assessed":
                new_threshold = next(item for item in matrix["dimensions"] if item["dimension_id"] == primary)["thresholds"][severity]
                replacement["threshold_id"] = new_threshold["threshold_id"]
                basis_prefix = str(replacement.get("assessment_basis", "")).split(" Threshold applied:", 1)[0]
                replacement["assessment_basis"] = f"{basis_prefix} Threshold applied: {new_threshold['criterion']}"
                current["controlling_dimensions"] = [primary]
            target_row.clear()
            target_row.update(replacement)
            old_status = "not-applicable" if severity == "S1" else "unreported"
            source_row.clear()
            source_row.update({
                "dimension_id": old_primary,
                "assessment_status": old_status,
                "assessment_basis": (
                    "The bounded occurrence and positive containment evidence establish no materialised downstream impact in this dimension."
                    if old_status == "not-applicable"
                    else "The preserved Incident evidence does not report a materialised impact in this dimension; absence of reporting is not evidence of no harm."
                ),
                "evidence_confidence": "not-assessed"
            })
            current["coverage_note"] = (
                f"The preserved evidence supports one controlling {DIMENSION_LABELS[primary]} assessment. Other relevant harm dimensions remain unreported and do not lower or raise the derived overall severity."
                if severity != "S1"
                else f"The preserved evidence positively supports S1 in the controlling {DIMENSION_LABELS[primary]} dimension within the bounded occurrence; other dimensions are outside that positively contained occurrence."
            )
            review = record["interpretive_provenance"]["current_ai_review"]
            review["review_outcome"] = f"Derived overall severity {severity} using VIGIL-HIM 1.0.0. The controlling dimension is {primary if severity != 'SU' else 'none'}; legacy severity was {severity}."
            for index, item in enumerate(record["interpretive_provenance"]["review_history"]):
                if item.get("review_id") == review.get("review_id"):
                    record["interpretive_provenance"]["review_history"][index] = review.copy()
        target_override = SEVERITY_OVERRIDES.get(record["id"])
        if target_override and current.get("overall_severity") != target_override[0]:
            legacy_severity = current.get("overall_severity")
            target_severity, reason = target_override
            assessed_row = next(row for row in rows if row.get("assessment_status") == "assessed")
            target_dimension = assessed_row["dimension_id"]
            target_threshold = next(item for item in matrix["dimensions"] if item["dimension_id"] == target_dimension)["thresholds"][target_severity]
            basis_prefix = str(assessed_row.get("assessment_basis", "")).split(" Threshold applied:", 1)[0]
            assessed_row["severity"] = target_severity
            assessed_row["threshold_id"] = target_threshold["threshold_id"]
            assessed_row["assessment_basis"] = f"{basis_prefix} {reason} Threshold applied: {target_threshold['criterion']}"
            if record["id"] in OBSERVED_VALUE_OVERRIDES:
                assessed_row["observed_values"] = OBSERVED_VALUE_OVERRIDES[record["id"]]
            current["overall_severity"] = target_severity
            current["controlling_dimensions"] = [target_dimension]
            review = record["interpretive_provenance"]["current_ai_review"]
            review["review_outcome"] = f"VIGIL-HIM 1.0.0 changed overall severity from {legacy_severity} to {target_severity}. {reason}"
            for index, item in enumerate(record["interpretive_provenance"]["review_history"]):
                if item.get("review_id") == review.get("review_id"):
                    record["interpretive_provenance"]["review_history"][index] = review.copy()
        apply_multi_dimension_overrides(record, current, matrix)
        return record, {
            "id": record["id"],
            "legacy_severity": target_override and target_override[0] != current_severity and current_severity or current.get("overall_severity"),
            "derived_severity": current.get("overall_severity"),
            "primary_dimension": primary,
            "changed": bool(target_override and target_override[0] != current_severity),
            "requires_human_review": current.get("overall_severity") == "SU",
        }
    legacy_severity = old["severity"]
    severity, override_reason = SEVERITY_OVERRIDES.get(record["id"], (legacy_severity, ""))
    dimensions = [item["dimension_id"] for item in matrix["dimensions"]]
    rows: list[dict] = []
    controlling: list[str] = []
    if severity == "SU":
        primary = select_dimension(record, old)
        for dimension_id in dimensions:
            if dimension_id == primary:
                rows.append({
                    "dimension_id": dimension_id,
                    "assessment_status": "insufficient-evidence",
                    "assessment_basis": old["assessment_gap"],
                    "evidence_confidence": "not-assessed"
                })
            else:
                rows.append({
                    "dimension_id": dimension_id,
                    "assessment_status": "unreported",
                    "assessment_basis": "The preserved Incident evidence does not report a materialised impact in this dimension; absence of reporting is not evidence of no harm.",
                    "evidence_confidence": "not-assessed"
                })
        overall = "SU"
        assessment_gap = old["assessment_gap"]
        coverage = "No harm dimension can be assigned a defensible band. One plausible impact dimension has some evidence but remains unbanded; all other dimensions are unreported."
    else:
        primary = select_dimension(record, old)
        controlling = [primary]
        for dimension_id in dimensions:
            if dimension_id == primary:
                threshold = next(item for item in matrix["dimensions"] if item["dimension_id"] == dimension_id)["thresholds"][severity]
                rows.append({
                    "dimension_id": dimension_id,
                    "assessment_status": "assessed",
                    "severity": severity,
                    "threshold_id": threshold["threshold_id"],
                    "observed_values": observed_values(record, old),
                    "assessment_basis": f"{old['materialised_consequence']} {old['seriousness_and_persistence']} {override_reason} Threshold applied: {threshold['criterion']}",
                    "evidence_confidence": "medium",
                    "evidence_refs": [f"source_records[{index}]" for index, _ in enumerate(record.get("source_records", []))]
                })
            else:
                status = "not-applicable" if severity == "S1" else "unreported"
                basis = (
                    "The bounded occurrence and positive containment evidence establish no materialised downstream impact in this dimension."
                    if status == "not-applicable"
                    else "The preserved Incident evidence does not report a materialised impact in this dimension; absence of reporting is not evidence of no harm."
                )
                rows.append({
                    "dimension_id": dimension_id,
                    "assessment_status": status,
                    "assessment_basis": basis,
                    "evidence_confidence": "not-assessed"
                })
        overall = severity
        assessment_gap = None
        coverage = f"The preserved evidence supports one controlling {DIMENSION_LABELS[primary]} assessment. Other relevant harm dimensions remain unreported and do not lower or raise the derived overall severity."
        if severity == "S1":
            coverage = f"The preserved evidence positively supports S1 in the controlling {DIMENSION_LABELS[primary]} dimension within the bounded occurrence; other dimensions are outside that positively contained occurrence."

    new_assessment = {
        "methodology_id": matrix["methodology_id"],
        "methodology_version": matrix["version"],
        "derivation_rule": matrix["derivation_rule"],
        "assessed_on": DATE,
        "overall_severity": overall,
        "controlling_dimensions": controlling,
        "coverage_note": coverage,
        "dimensions": rows,
    }
    if assessment_gap:
        new_assessment["assessment_gap"] = assessment_gap
    apply_multi_dimension_overrides(record, new_assessment, matrix)
    record["harm_impact_assessment"] = new_assessment
    del record["severity_assessment"]
    identity = record["record_identity"]
    identity["updated"] = DATE
    identity["version"] = increment_patch(identity["version"])
    review_id = f"VIGIL-REVIEW-2026-09-16-HIM-{record['id'][-6:]}"
    review = {
        "review_id": review_id,
        "reviewer_type": "AI analytical reviewer",
        "reviewer_platform": "OpenAI Codex",
        "reviewer_model": "GPT-5",
        "review_date": DATE,
        "review_scope": "Controlled full-corpus Harm Impact Matrix derivation from preserved Incident evidence; Failure Taxonomy adjudications were not reopened.",
        "capability_profile": {
            "direct_repository_analysis": True,
            "direct_text_analysis": True,
            "web_link_and_metadata_review": True
        },
        "known_limitations": [
            "The assessment is bounded to evidence already preserved in the Incident and does not infer unreported harms, losses, durations or affected populations.",
            "Unreported dimensions remain explicitly unreported and do not represent supported absence of harm."
        ],
        "review_outcome": f"Derived overall severity {overall} using VIGIL-HIM 1.0.0. The controlling dimension is {primary if overall != 'SU' else 'none'}; legacy severity was {legacy_severity}. {override_reason}".strip()
    }
    provenance = record["interpretive_provenance"]
    provenance["review_history"].append(review)
    provenance["current_ai_review"] = review.copy()
    return record, {
        "id": record["id"],
        "legacy_severity": legacy_severity,
        "derived_severity": overall,
        "primary_dimension": primary,
        "changed": legacy_severity != overall,
        "requires_human_review": overall == "SU",
    }


def main() -> None:
    if "--historical-replay" not in sys.argv:
        raise SystemExit(
            "Historical migration only; pass --historical-replay only in an isolated historical checkout."
        )
    matrix = load(MATRIX_PATH)
    results = []
    for path in sorted(INCIDENTS.glob("VIGIL-INC-*.json")):
        record, result = transform(load(path), matrix)
        save(path, record)
        results.append(result)
    counts = Counter(item.get("derived_severity") for item in results if item.get("derived_severity"))
    print(json.dumps({"records": len(results), "distribution": dict(sorted(counts.items())), "results": results}, indent=2))


if __name__ == "__main__":
    main()
