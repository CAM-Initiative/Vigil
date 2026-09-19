#!/usr/bin/env python3
"""Validate canonical Incident records in the Incident-only VIGIL corpus."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS_ROOT = VIGIL / "records"
INCIDENT_ROOT = RECORDS_ROOT / "incidents"
SCHEMA_PATH = VIGIL / "VIGIL.Schema.json"
HARM_MATRIX_PATH = VIGIL / "methodologies" / "VIGIL.HarmImpactMatrix.v1.0.0.json"
TAXONOMY_INDEX = VIGIL / "taxonomy" / "VIGIL.FailureTaxonomy.Index.json"
INCIDENT_ID = re.compile(r"^VIGIL-INC-\d{6}$")
EXTERNAL_ASSESSMENT_ID = re.compile(r"^VIGIL-EXTASSESS-\d{6}$")
HTTP_URL = re.compile(r"^https?://[^\s]+$", re.IGNORECASE)
HISTORICAL_ID = re.compile(r"VIGIL-\d{4}-(?:FM|OBS|RESEARCH|PROP|PATCH|LEARN)-\d{4}")
RETIRED_RECORD_DIRS = {"failures", "observations", "research", "proposals", "patches", "learn"}
RETIRED_INDEXES = {
    "VIGIL.Failures.Index.json", "VIGIL.Observations.Index.json", "VIGIL.Research.Index.json",
    "VIGIL.Proposals.Index.json", "VIGIL.PatchNotes.Index.json", "VIGIL.Learn.Index.json",
}
SEVERITY_RANK = {"S1": 1, "S2": 2, "S3": 3, "S4": 4, "S5": 5}
DIAGNOSTIC_REQUIRED = {
    "method", "diagnostic_date", "human_role", "ai_role", "ai_platform", "ai_model",
    "review_status", "authority_boundary",
}
REVIEW_REQUIRED = {
    "review_id", "reviewer_type", "reviewer_platform", "reviewer_model", "review_date",
    "review_scope", "capability_profile", "known_limitations", "review_outcome",
}
SOURCE_REQUIRED = {
    "source_title", "author_or_publisher", "source_date", "source_url", "retrieved_date",
    "source_type", "source_role", "source_residence", "source_platform", "source_url_status",
    "relevance_note", "evidence_modality", "primary_artefact_access", "interpretive_reliance",
    "evidence_status", "evidence_status_basis", "incident_source_order",
}
ACCESS_REQUIRED = {
    "access_status", "reviewing_system", "access_method", "direct_primary_artefact_review",
    "limitations",
}
EXTERNAL_ASSESSMENT_REQUIRED = {
    "assessment_id", "assessor", "assessment_title", "assessment_date", "assessment_url",
    "assessment_type", "relationship_to_incident", "assessment_summary", "reviewed_on",
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("expected one JSON object")
    return value


def schema(path: Path | None = None) -> dict[str, Any]:
    return load_json(path or SCHEMA_PATH)


def incident_contract(schema_path: Path | None = None) -> dict[str, Any]:
    return schema(schema_path)["record_classes"]["incident"]


def non_empty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def parse_date(value: Any) -> date | None:
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


def contains_key(value: Any, key: str) -> bool:
    if isinstance(value, dict):
        return key in value or any(contains_key(item, key) for item in value.values())
    if isinstance(value, list):
        return any(contains_key(item, key) for item in value)
    return False


def allowed_system_values(schema_path: Path | None = None) -> tuple[set[str], set[str]]:
    rules = schema(schema_path)["system_context_rules"]
    return set(rules["allowed_platform_or_vendor_values"]), set(rules["allowed_product_or_service_values"])


def taxonomy_catalogue() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    index = load_json(TAXONOMY_INDEX)
    families: dict[str, dict[str, Any]] = {}
    classes: dict[str, dict[str, Any]] = {}
    for entry in index.get("families", []):
        if not isinstance(entry, dict) or not isinstance(entry.get("family_id"), str):
            continue
        family = load_json(TAXONOMY_INDEX.parent / str(entry["file"])).get("family", {})
        families[entry["family_id"]] = family
        document = load_json(TAXONOMY_INDEX.parent / str(entry["file"]))
        for item in document.get("classes", []):
            if isinstance(item, dict) and isinstance(item.get("class_id"), str):
                classes[item["class_id"]] = item
    return families, classes


def retired_taxonomy_class_successors() -> dict[str, str]:
    index = load_json(TAXONOMY_INDEX)
    return {
        item["retired_id"]: item["successor_id"]
        for item in index.get("retired_class_mappings", [])
        if isinstance(item, dict) and isinstance(item.get("retired_id"), str)
        and isinstance(item.get("successor_id"), str)
    }


def validate_taxonomy_mapping(
    path: Path,
    mapping: Any,
    label: str,
    families: dict[str, dict[str, Any]],
    classes: dict[str, dict[str, Any]],
    retired: dict[str, str],
    errors: list[str],
) -> str | None:
    if not isinstance(mapping, dict):
        errors.append(f"{path}: {label} must be an object")
        return None
    required = {"family_id", "class_id", "classification_role", "classification_basis", "classification_confidence"}
    missing = sorted(required - set(mapping))
    if missing:
        errors.append(f"{path}: {label} missing {', '.join(missing)}")
    family_id = mapping.get("family_id")
    class_id = mapping.get("class_id")
    if family_id not in families:
        errors.append(f"{path}: {label} family ID {family_id!r} does not resolve")
    if class_id in retired:
        errors.append(f"{path}: {label} uses retired class {class_id}; use {retired[class_id]}")
    elif class_id not in classes:
        errors.append(f"{path}: {label} class ID {class_id!r} does not resolve")
    elif classes[class_id].get("family_id") != family_id:
        errors.append(f"{path}: {label} class {class_id} does not belong to {family_id}")
    if not non_empty(mapping.get("classification_basis")):
        errors.append(f"{path}: {label}.classification_basis must be non-empty")
    if mapping.get("classification_confidence") not in {"low", "medium", "high"}:
        errors.append(f"{path}: {label}.classification_confidence must be low, medium, or high")
    role = mapping.get("classification_role")
    if role not in {"failure-occurrence", "successful-invariant", "ambiguous-boundary"}:
        errors.append(
            f"{path}: {label}.classification_role must be failure-occurrence, successful-invariant or ambiguous-boundary"
        )
    return class_id if isinstance(class_id, str) else None


def validate_incident_taxonomy(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    block = record.get("taxonomy_classification")
    if not isinstance(block, dict):
        errors.append(f"{path}: taxonomy_classification must be an object")
        return
    contract = incident_contract()
    status = block.get("classification_status")
    if status not in set(contract["classification_status_values"]):
        errors.append(f"{path}: invalid taxonomy classification_status {status!r}")
        return
    role = block.get("classification_role")
    if role is not None and role not in set(contract["classification_role_values"]):
        errors.append(f"{path}: invalid taxonomy classification_role {role!r}")
    for field in ("taxonomy_version", "classification_basis"):
        if not non_empty(block.get(field)):
            errors.append(f"{path}: taxonomy_classification.{field} must be non-empty")
    if not isinstance(block.get("classification_review_provenance"), dict):
        errors.append(f"{path}: classification_review_provenance must be an object")
    primary = block.get("primary_classification")
    secondary = block.get("secondary_classifications")
    if not isinstance(secondary, list):
        errors.append(f"{path}: secondary_classifications must be an array")
        secondary = []
    if status in {"unclassified", "requires-human-review"}:
        if primary is not None or secondary:
            errors.append(f"{path}: {status} Incident must not assert taxonomy mappings")
        if role is not None:
            errors.append(f"{path}: {status} Incident must not assert classification_role")
        return
    if status not in {"classified", "provisionally-classified", "classification-disputed"}:
        return
    families, classes = taxonomy_catalogue()
    retired = retired_taxonomy_class_successors()
    primary_id = validate_taxonomy_mapping(path, primary, "primary_classification", families, classes, retired, errors)
    mappings: list[tuple[str | None, Any, str]] = [(primary_id, primary, "primary_classification")]
    seen = {primary_id} if primary_id else set()
    for index, mapping in enumerate(secondary):
        class_id = validate_taxonomy_mapping(
            path, mapping, f"secondary_classifications[{index}]", families, classes, retired, errors
        )
        if class_id in seen:
            errors.append(f"{path}: taxonomy class {class_id} is duplicated")
        if class_id:
            seen.add(class_id)
        mappings.append((class_id, mapping, f"secondary_classifications[{index}]"))

    nested_roles = {
        mapping.get("classification_role")
        for _, mapping, _ in mappings
        if isinstance(mapping, dict)
    }
    if role is not None and nested_roles != {role}:
        errors.append(
            f"{path}: legacy block-level classification_role must agree with every mapping-local role"
        )

    for class_id, mapping, label in mappings:
        if not isinstance(mapping, dict):
            continue
        mapping_role = mapping.get("classification_role")
        if mapping_role not in {"successful-invariant", "ambiguous-boundary"}:
            continue
        if status != "classified":
            errors.append(f"{path}: {label} {mapping_role} role requires classified status")
        exemplar_rows = classes.get(class_id, {}).get("invariant_exemplars", []) if class_id else []
        exemplar_match = any(
            isinstance(item, dict)
            and item.get("linked_incident_id") == record.get("id")
            and item.get("exemplar_type") == mapping_role
            and item.get("exemplar_status") == "admitted"
            for item in exemplar_rows
        )
        if not exemplar_match:
            errors.append(
                f"{path}: {label} {mapping_role} role must match an admitted taxonomy invariant_exemplar"
            )


def harm_matrix() -> dict[str, Any]:
    return load_json(HARM_MATRIX_PATH)


def financial_band_for_usd(value: float) -> str:
    if value < 0:
        raise ValueError("financial loss cannot be negative")
    if value < 10_000:
        return "S1"
    if value < 1_000_000:
        return "S2"
    if value < 100_000_000:
        return "S3"
    if value < 100_000_000_000:
        return "S4"
    return "S5"


def validate_harm_impact(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    assessment = record.get("harm_impact_assessment")
    if not isinstance(assessment, dict):
        errors.append(f"{path}: harm_impact_assessment must be an object")
        return
    contract = incident_contract()
    required = {
        "methodology_id", "methodology_version", "derivation_rule", "assessed_on",
        "overall_severity", "controlling_dimensions", "coverage_note", "dimensions",
    }
    missing = sorted(required - set(assessment))
    if missing:
        errors.append(f"{path}: harm_impact_assessment missing {', '.join(missing)}")
    if assessment.get("methodology_id") != contract["harm_impact_methodology_id"]:
        errors.append(f"{path}: harm impact methodology_id is not canonical")
    if assessment.get("methodology_version") != contract["harm_impact_methodology_version"]:
        errors.append(f"{path}: harm impact methodology_version is not canonical")
    if assessment.get("derivation_rule") != contract["harm_impact_derivation_rule"]:
        errors.append(f"{path}: harm impact derivation_rule is not canonical")
    if parse_date(assessment.get("assessed_on")) is None:
        errors.append(f"{path}: harm_impact_assessment.assessed_on must be an ISO date")
    if not non_empty(assessment.get("coverage_note")):
        errors.append(f"{path}: harm_impact_assessment.coverage_note must be non-empty")

    matrix = harm_matrix()
    dimensions_by_id = {item["dimension_id"]: item for item in matrix["dimensions"]}
    expected_ids = set(contract["harm_impact_dimension_ids"])
    rows = assessment.get("dimensions")
    if not isinstance(rows, list):
        errors.append(f"{path}: harm_impact_assessment.dimensions must be an array")
        return
    actual_ids = [row.get("dimension_id") for row in rows if isinstance(row, dict)]
    if len(actual_ids) != len(set(actual_ids)):
        errors.append(f"{path}: harm impact dimensions must be unique")
    if set(actual_ids) != expected_ids:
        errors.append(f"{path}: harm impact dimensions must contain every canonical dimension exactly once")

    assessed: list[tuple[str, str]] = []
    source_records = record.get("source_records")
    statuses = set(contract["harm_impact_status_values"])
    confidences = set(contract["harm_impact_evidence_confidence_values"])
    for index, row in enumerate(rows):
        label = f"{path}: harm_impact_assessment.dimensions[{index}]"
        if not isinstance(row, dict):
            errors.append(f"{label} must be an object")
            continue
        dimension_id = row.get("dimension_id")
        status = row.get("assessment_status")
        if dimension_id not in expected_ids:
            errors.append(f"{label}.dimension_id is not canonical")
        if status not in statuses:
            errors.append(f"{label}.assessment_status is not canonical")
        if not non_empty(row.get("assessment_basis")):
            errors.append(f"{label}.assessment_basis must be non-empty")
        if row.get("evidence_confidence") not in confidences:
            errors.append(f"{label}.evidence_confidence is not canonical")
        if status == "assessed":
            severity = row.get("severity")
            threshold_id = row.get("threshold_id")
            if severity not in SEVERITY_RANK:
                errors.append(f"{label}.severity must be S1-S5 when assessed")
            else:
                assessed.append((str(dimension_id), str(severity)))
                expected_threshold = dimensions_by_id.get(str(dimension_id), {}).get("thresholds", {}).get(str(severity), {}).get("threshold_id")
                if threshold_id != expected_threshold:
                    errors.append(f"{label}.threshold_id does not match the matrix dimension and band")
            refs = row.get("evidence_refs")
            if not isinstance(refs, list) or not refs or any(not isinstance(item, str) for item in refs):
                errors.append(f"{label}.evidence_refs must be a non-empty string array when assessed")
            elif isinstance(source_records, list):
                for ref in refs:
                    match = re.fullmatch(r"source_records\[(\d+)\]", ref)
                    if match is None:
                        errors.append(f"{label}.evidence_refs must use source_records[N] references")
                        continue
                    source_index = int(match.group(1))
                    if source_index >= len(source_records):
                        errors.append(f"{label}.evidence_refs points outside source_records")
                        continue
                    source = source_records[source_index]
                    if isinstance(source, dict) and source.get("source_role") == "record-cross-reference":
                        errors.append(f"{label}.evidence_refs must not cite a record-cross-reference source")
            values = row.get("observed_values")
            if not isinstance(values, list):
                errors.append(f"{label}.observed_values must be an array when assessed")
            elif dimension_id == "financial-economic" and severity in SEVERITY_RANK:
                for value in values:
                    if not isinstance(value, dict) or value.get("unit") != "USD":
                        continue
                    amount = value.get("value")
                    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
                        errors.append(f"{label}.observed_values USD value must be numeric")
                        continue
                    try:
                        expected_band = financial_band_for_usd(float(amount))
                    except ValueError:
                        errors.append(f"{label}.observed_values financial loss cannot be negative")
                        continue
                    if severity != expected_band:
                        errors.append(
                            f"{label}.severity must be {expected_band} for the reported USD value under canonical financial boundaries"
                        )
            if row.get("evidence_confidence") == "not-assessed":
                errors.append(f"{label}.evidence_confidence cannot be not-assessed when assessed")
        else:
            for field in ("severity", "threshold_id", "observed_values", "evidence_refs"):
                if field in row:
                    errors.append(f"{label}.{field} is forbidden when status is {status}")
            if row.get("evidence_confidence") != "not-assessed":
                errors.append(f"{label}.evidence_confidence must be not-assessed when status is {status}")

    overall = assessment.get("overall_severity")
    controlling = assessment.get("controlling_dimensions")
    if not isinstance(controlling, list) or any(item not in expected_ids for item in controlling):
        errors.append(f"{path}: controlling_dimensions must be a canonical dimension array")
        controlling = []
    if assessed:
        expected_overall = max((severity for _, severity in assessed), key=SEVERITY_RANK.__getitem__)
        expected_controlling = sorted(dimension for dimension, severity in assessed if severity == expected_overall)
        if overall != expected_overall:
            errors.append(f"{path}: overall_severity must equal highest supported assessed harm band {expected_overall}")
        if sorted(controlling) != expected_controlling:
            errors.append(f"{path}: controlling_dimensions must identify every dimension at the overall band")
        if overall == "S1" and not any(row.get("assessment_status") == "assessed" and row.get("severity") == "S1" for row in rows if isinstance(row, dict)):
            errors.append(f"{path}: S1 requires positive assessed evidence")
        if "assessment_gap" in assessment:
            errors.append(f"{path}: assessment_gap is reserved for SU")
        if "no_materialised_harm_basis" in assessment:
            errors.append(f"{path}: no_materialised_harm_basis is reserved for bounded S1 assessments with no materialised harm")
    else:
        if overall == "S1":
            if controlling:
                errors.append(f"{path}: no-materialised-harm S1 must not have controlling_dimensions")
            if not non_empty(assessment.get("no_materialised_harm_basis")):
                errors.append(f"{path}: no-materialised-harm S1 requires a concrete no_materialised_harm_basis")
            if "assessment_gap" in assessment:
                errors.append(f"{path}: assessment_gap is reserved for SU")
            if any(row.get("assessment_status") == "insufficient-evidence" for row in rows if isinstance(row, dict)):
                errors.append(f"{path}: no-materialised-harm S1 cannot contain insufficient-evidence dimensions")
        else:
            if overall != "SU":
                errors.append(f"{path}: no assessed dimension requires overall_severity SU or bounded no-materialised-harm S1")
            if controlling:
                errors.append(f"{path}: SU must not have controlling_dimensions")
            if not non_empty(assessment.get("assessment_gap")):
                errors.append(f"{path}: SU requires a concrete assessment_gap")
            if "no_materialised_harm_basis" in assessment:
                errors.append(f"{path}: no_materialised_harm_basis is reserved for bounded S1")


def validate_source_records(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    contract = incident_contract()
    allowed_status = set(contract["evidence_status_values"])
    allowed_types = set(contract["source_type_values"])
    source_records = record.get("source_records")
    if not isinstance(source_records, list) or not source_records:
        errors.append(f"{path}: source_records must be a non-empty array")
        return
    seen_orders: set[int] = set()
    for index, source in enumerate(source_records):
        label = f"{path}: source_records[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{label} must be an object")
            continue
        missing = sorted(SOURCE_REQUIRED - set(source))
        if missing:
            errors.append(f"{label} missing {', '.join(missing)}")
        if source.get("evidence_status") not in allowed_status:
            errors.append(f"{label}.evidence_status is not canonical")
        if source.get("source_type") not in allowed_types:
            errors.append(f"{label}.source_type is not canonical")
        if not non_empty(source.get("evidence_status_basis")):
            errors.append(f"{label}.evidence_status_basis must be non-empty")
        modalities = source.get("evidence_modality")
        if not isinstance(modalities, list) or not modalities or any(not non_empty(item) for item in modalities):
            errors.append(f"{label}.evidence_modality must be a non-empty string array")
        access = source.get("primary_artefact_access")
        if not isinstance(access, dict):
            errors.append(f"{label}.primary_artefact_access must be an object")
        else:
            access_missing = sorted(ACCESS_REQUIRED - set(access))
            if access_missing:
                errors.append(f"{label}.primary_artefact_access missing {', '.join(access_missing)}")
        order = source.get("incident_source_order")
        if not isinstance(order, int) or order < 1:
            errors.append(f"{label}.incident_source_order must be a positive integer")
        elif order in seen_orders:
            errors.append(f"{label}.incident_source_order must be unique")
        else:
            seen_orders.add(order)
    if seen_orders and seen_orders != set(range(1, len(source_records) + 1)):
        errors.append(f"{path}: incident_source_order must form a contiguous sequence from 1")
    preferred = record.get("preferred_evidence")
    if not isinstance(preferred, dict):
        errors.append(f"{path}: preferred_evidence must be an object")
    else:
        for field in ("source_url", "selection_basis", "selected_on"):
            if not non_empty(preferred.get(field)):
                errors.append(f"{path}: preferred_evidence.{field} must be non-empty")
        matches = [item for item in source_records if isinstance(item, dict) and item.get("source_url") == preferred.get("source_url")]
        if len(matches) != 1:
            errors.append(f"{path}: preferred_evidence.source_url must uniquely select one source_record")


def validate_external_assessments(
    path: Path,
    record: dict[str, Any],
    known_assessment_ids: set[str] | None,
    errors: list[str],
) -> None:
    assessments = record.get("external_assessments", [])
    if not isinstance(assessments, list):
        errors.append(f"{path}: external_assessments must be an array when present")
        return

    contract = incident_contract()
    allowed_types = set(contract["external_assessment_type_values"])
    allowed_relationships = set(contract["external_assessment_relationship_values"])
    allowed_statuses = set(contract["external_assessment_status_values"])
    source_records = record.get("source_records") if isinstance(record.get("source_records"), list) else []
    seen: set[str] = set()

    for index, assessment in enumerate(assessments):
        label = f"{path}: external_assessments[{index}]"
        if not isinstance(assessment, dict):
            errors.append(f"{label} must be an object")
            continue
        missing = sorted(EXTERNAL_ASSESSMENT_REQUIRED - set(assessment))
        if missing:
            errors.append(f"{label} missing {', '.join(missing)}")
        assessment_id = assessment.get("assessment_id")
        if not isinstance(assessment_id, str) or not EXTERNAL_ASSESSMENT_ID.fullmatch(assessment_id):
            errors.append(f"{label}.assessment_id must use VIGIL-EXTASSESS-NNNNNN")
        elif assessment_id in seen:
            errors.append(f"{label}.assessment_id must be unique within the Incident")
        else:
            seen.add(assessment_id)
        for field in ("assessor", "assessment_title", "assessment_summary"):
            if not non_empty(assessment.get(field)):
                errors.append(f"{label}.{field} must be non-empty")
        for field in ("assessment_date", "reviewed_on"):
            if parse_date(assessment.get(field)) is None:
                errors.append(f"{label}.{field} must be an ISO date")
        if not non_empty(assessment.get("assessment_url")) or not HTTP_URL.fullmatch(str(assessment.get("assessment_url", ""))):
            errors.append(f"{label}.assessment_url must be an HTTP(S) URL")
        if assessment.get("assessment_type") not in allowed_types:
            errors.append(f"{label}.assessment_type is not canonical")
        if assessment.get("relationship_to_incident") not in allowed_relationships:
            errors.append(f"{label}.relationship_to_incident is not canonical")
        if "assessment_status" in assessment and assessment.get("assessment_status") not in allowed_statuses:
            errors.append(f"{label}.assessment_status is not canonical")
        for field in ("scope_note", "vigil_comparison_note", "publication_or_institution", "assessment_version"):
            if field in assessment and not non_empty(assessment.get(field)):
                errors.append(f"{label}.{field} must be non-empty when present")

        rating = assessment.get("classification_or_rating")
        if rating is not None:
            if not isinstance(rating, dict):
                errors.append(f"{label}.classification_or_rating must be an object")
            else:
                for field in ("scheme", "value"):
                    if not non_empty(rating.get(field)):
                        errors.append(f"{label}.classification_or_rating.{field} must be non-empty")
                if "verbatim_label" in rating and not non_empty(rating.get("verbatim_label")):
                    errors.append(f"{label}.classification_or_rating.verbatim_label must be non-empty when present")

        refs = assessment.get("source_record_refs")
        if refs is not None:
            if not isinstance(refs, list) or not refs or any(not isinstance(ref, str) for ref in refs):
                errors.append(f"{label}.source_record_refs must be a non-empty string array when present")
            elif len(refs) != len(set(refs)):
                errors.append(f"{label}.source_record_refs must not contain duplicates")
            else:
                for ref in refs:
                    match = re.fullmatch(r"source_records\[(\d+)\]", ref)
                    if match is None:
                        errors.append(f"{label}.source_record_refs must use source_records[N] references")
                    elif int(match.group(1)) >= len(source_records):
                        errors.append(f"{label}.source_record_refs points outside source_records")

        supersedes = assessment.get("supersedes_assessment_id")
        if supersedes is not None:
            if not isinstance(supersedes, str) or not EXTERNAL_ASSESSMENT_ID.fullmatch(supersedes):
                errors.append(f"{label}.supersedes_assessment_id must use VIGIL-EXTASSESS-NNNNNN")
            elif supersedes == assessment_id:
                errors.append(f"{label}.supersedes_assessment_id must not self-reference")
            elif known_assessment_ids is not None and supersedes not in known_assessment_ids:
                errors.append(f"{label}.supersedes_assessment_id does not resolve")


def validate_provenance(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    diagnostic = record.get("diagnostic_provenance")
    if not isinstance(diagnostic, dict):
        errors.append(f"{path}: diagnostic_provenance must be an object")
    else:
        missing = sorted(DIAGNOSTIC_REQUIRED - set(diagnostic))
        if missing:
            errors.append(f"{path}: diagnostic_provenance missing {', '.join(missing)}")
        if parse_date(diagnostic.get("diagnostic_date")) is None:
            errors.append(f"{path}: diagnostic_provenance.diagnostic_date must be an ISO date")
    provenance = record.get("interpretive_provenance")
    if not isinstance(provenance, dict):
        errors.append(f"{path}: interpretive_provenance must be an object")
        return
    history = provenance.get("review_history")
    current = provenance.get("current_ai_review")
    if not isinstance(history, list) or not history:
        errors.append(f"{path}: review_history must be a non-empty array")
        history = []
    seen: set[str] = set()
    for index, review in enumerate(history):
        if not isinstance(review, dict):
            errors.append(f"{path}: review_history[{index}] must be an object")
            continue
        missing = sorted(REVIEW_REQUIRED - set(review))
        if missing:
            errors.append(f"{path}: review_history[{index}] missing {', '.join(missing)}")
        review_id = review.get("review_id")
        if not non_empty(review_id) or review_id in seen:
            errors.append(f"{path}: review_history[{index}] has missing or duplicate review_id")
        else:
            seen.add(review_id)
    if not isinstance(current, dict) or current.get("review_id") not in seen:
        errors.append(f"{path}: current_ai_review must resolve to review_history")

def validate_relationships_and_references(
    path: Path,
    record: dict[str, Any],
    known_ids: set[str] | None,
    errors: list[str],
) -> None:
    record_id = record.get("id")
    related = record.get("related_incidents")
    if not isinstance(related, list):
        errors.append(f"{path}: related_incidents must be an array")
    else:
        string_ids = [item for item in related if isinstance(item, str)]
        if len(string_ids) != len(set(string_ids)):
            errors.append(f"{path}: related_incidents must not contain duplicates")
        for index, incident_id in enumerate(related):
            if not isinstance(incident_id, str) or not INCIDENT_ID.fullmatch(incident_id):
                errors.append(f"{path}: related_incidents[{index}] must use VIGIL-INC-NNNNNN")
            elif incident_id == record_id:
                errors.append(f"{path}: related_incidents must not contain a self-link")
            elif known_ids is not None and incident_id not in known_ids:
                errors.append(f"{path}: related_incidents[{index}] does not resolve to an active Incident")

    research = record.get("research_references")
    if research is not None:
        if not isinstance(research, list) or not research:
            errors.append(f"{path}: research_references must be a non-empty array when present")
        else:
            for index, citation in enumerate(research):
                if not non_empty(citation):
                    errors.append(f"{path}: research_references[{index}] must be a non-empty string")
                elif HISTORICAL_ID.search(citation):
                    errors.append(f"{path}: research_references[{index}] contains a retired VIGIL record ID")

    standards = record.get("standards_and_regulatory_references")
    if standards is not None:
        if not isinstance(standards, list) or not standards:
            errors.append(f"{path}: standards_and_regulatory_references must be a non-empty array when present")
        else:
            for index, reference in enumerate(standards):
                valid = non_empty(reference) or (isinstance(reference, dict) and bool(reference))
                if not valid:
                    errors.append(
                        f"{path}: standards_and_regulatory_references[{index}] must be a non-empty string or object"
                    )
                elif HISTORICAL_ID.search(json.dumps(reference, ensure_ascii=False)):
                    errors.append(
                        f"{path}: standards_and_regulatory_references[{index}] contains a retired VIGIL record ID"
                    )


def validate_record(
    path: Path,
    record: dict[str, Any],
    known_ids: set[str] | None = None,
    known_assessment_ids: set[str] | None = None,
    errors: list[str] | None = None,
    warnings: list[str] | None = None,
    allowed_vendors: set[str] | None = None,
    allowed_products: set[str] | None = None,
    schema_path: Path | None = None,
) -> tuple[list[str], list[str]]:
    errors = errors if errors is not None else []
    warnings = warnings if warnings is not None else []
    contract = incident_contract(schema_path)
    if record.get("record_type") != "incident":
        errors.append(f"{path}: active VIGIL records must use record_type incident")
        return errors, warnings
    record_id = record.get("id")
    if not isinstance(record_id, str) or not INCIDENT_ID.fullmatch(record_id):
        errors.append(f"{path}: Incident id must use VIGIL-INC-NNNNNN")
    if path.resolve().is_relative_to(RECORDS_ROOT.resolve()) and path.parent.resolve() == INCIDENT_ROOT.resolve():
        if path.name != f"{record_id}.json":
            errors.append(f"{path}: filename must match Incident id")
    missing = sorted(set(contract["required_top_level_fields"]) - set(record))
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(missing)}")
    forbidden = sorted(field for field in contract["forbidden_top_level_fields"] if field in record)
    if forbidden:
        errors.append(f"{path}: forbidden Incident fields: {', '.join(forbidden)}")
    retired_nested = sorted(field for field in contract.get("forbidden_nested_fields", []) if contains_key(record, field))
    if retired_nested:
        errors.append(f"{path}: forbidden retired Incident fields: {', '.join(retired_nested)}")
    for field in contract.get("legacy_priority_fields", []):
        if contains_key(record, field):
            errors.append(f"{path}: legacy operational priority field {field!r} is prohibited")
    if contains_key(record, "source_data"):
        errors.append(f"{path}: source_data is retired; use source_records")
    if not non_empty(record.get("summary")):
        errors.append(f"{path}: summary must be non-empty")
    identity = record.get("record_identity")
    if not isinstance(identity, dict) or identity.get("record_id") != record_id or identity.get("record_type") != "incident":
        errors.append(f"{path}: record_identity must match the Incident id and type")
    incident = record.get("incident_identity")
    if not isinstance(incident, dict):
        errors.append(f"{path}: incident_identity must be an object")
    else:
        if incident.get("date_precision") not in set(contract["date_precision_values"]):
            errors.append(f"{path}: invalid incident_identity.date_precision")
        precision = incident.get("date_precision")
        start_value = incident.get("occurred_from")
        end_value = incident.get("occurred_to")
        if precision == "unknown":
            valid_dates = start_value in (None, "") and end_value in (None, "")
        elif precision == "month":
            valid_dates = isinstance(start_value, str) and re.fullmatch(r"\d{4}-(?:0[1-9]|1[0-2])", start_value) is not None and end_value in (None, "")
        elif precision == "year":
            valid_dates = isinstance(start_value, str) and re.fullmatch(r"\d{4}", start_value) is not None and end_value in (None, "")
        else:
            start = parse_date(start_value)
            end = parse_date(end_value) if end_value not in (None, "") else None
            valid_dates = start is not None and (end_value in (None, "") or end is not None) and (end is None or start <= end)
        if not valid_dates:
            errors.append(f"{path}: incident occurrence dates must be valid and ordered")
    vendors, products = allowed_system_values(schema_path)
    allowed_vendors = allowed_vendors or vendors
    allowed_products = allowed_products or products
    system = record.get("system_context")
    if not isinstance(system, dict):
        errors.append(f"{path}: system_context must be an object")
    else:
        for field in ("platform_or_vendor", "product_or_service", "specific_model_or_runtime", "interface_surface"):
            if field not in system or system[field] in (None, "", []):
                errors.append(f"{path}: system_context.{field} must be non-empty")
        if system.get("platform_or_vendor") not in allowed_vendors:
            errors.append(f"{path}: non-canonical platform_or_vendor")
        if system.get("product_or_service") not in allowed_products:
            errors.append(f"{path}: non-canonical product_or_service")
    validate_harm_impact(path, record, errors)
    validate_source_records(path, record, errors)
    validate_external_assessments(path, record, known_assessment_ids, errors)
    validate_incident_taxonomy(path, record, errors)
    validate_provenance(path, record, errors)
    validate_relationships_and_references(path, record, known_ids, errors)
    return errors, warnings


def record_files(root: Path | None = None) -> list[Path]:
    target = root or INCIDENT_ROOT
    if target.is_file():
        return [target]
    return sorted(target.rglob("*.json"), key=lambda item: item.as_posix())


def validate(root: Path | None = None, schema_path: Path | None = None) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    if root is None:
        for directory in sorted(RETIRED_RECORD_DIRS):
            if (RECORDS_ROOT / directory).exists():
                errors.append(f"{RECORDS_ROOT / directory}: retired record-class directory must not exist")
        for filename in sorted(RETIRED_INDEXES):
            if (VIGIL / filename).exists():
                errors.append(f"{VIGIL / filename}: retired generated index must not exist")
    paths = record_files(root)
    loaded: list[tuple[Path, dict[str, Any]]] = []
    for path in paths:
        try:
            record = load_json(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path}: unable to read JSON: {exc}")
            continue
        loaded.append((path, record))
    ids: set[str] = set()
    assessment_ids: set[str] = set()
    for path, record in loaded:
        record_id = record.get("id")
        if isinstance(record_id, str):
            if record_id in ids:
                errors.append(f"{path}: duplicate Incident id {record_id}")
            ids.add(record_id)
        assessments = record.get("external_assessments", [])
        if isinstance(assessments, list):
            for assessment in assessments:
                assessment_id = assessment.get("assessment_id") if isinstance(assessment, dict) else None
                if isinstance(assessment_id, str):
                    if assessment_id in assessment_ids:
                        errors.append(f"{path}: duplicate external assessment id {assessment_id}")
                    assessment_ids.add(assessment_id)
    for path, record in loaded:
        validate_record(path, record, ids, assessment_ids, errors, warnings, schema_path=schema_path)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    if errors:
        print("VIGIL Incident validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"VIGIL Incident validation passed: {len(paths)} canonical Incident records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate())
