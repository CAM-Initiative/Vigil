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
TAXONOMY_INDEX = VIGIL / "taxonomy" / "VIGIL.FailureTaxonomy.Index.json"
INCIDENT_ID = re.compile(r"^VIGIL-INC-\d{6}$")
HISTORICAL_ID = re.compile(r"^VIGIL-\d{4}-(?:FM|OBS|RESEARCH|PROP|PATCH|LEARN)-\d{4}$")
RETIRED_RECORD_DIRS = {"failures", "observations", "research", "proposals", "patches", "learn"}
RETIRED_INDEXES = {
    "VIGIL.Failures.Index.json", "VIGIL.Observations.Index.json", "VIGIL.Research.Index.json",
    "VIGIL.Proposals.Index.json", "VIGIL.PatchNotes.Index.json", "VIGIL.Learn.Index.json",
}
STRUCTURED_SEVERITY_FIELDS = (
    "materialised_consequence", "affected_scope", "seriousness_and_persistence",
    "quantitative_information", "evidentiary_limits", "band_rationale",
)
GENERIC_SEVERITY_TEXT = (
    "state the consequence or harm that actually materialised",
    "state the record-specific people, systems, organisations",
    "explain the seriousness, duration, persistence",
    "preserve supported counts, loss, duration",
    "state the occurrence-specific limits on causal mechanism",
    "explain why s3 is supported over s2 and s4",
    "the assessment is confined to the people, systems, organisations, service cohort",
)
ADJACENT_BANDS = {
    "S1": {"S2"}, "S2": {"S1", "S3"}, "S3": {"S2", "S4"}, "S4": {"S3"},
}
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
    required = {"family_id", "class_id", "classification_basis", "classification_confidence"}
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
        return
    if status not in {"classified", "provisionally-classified", "classification-disputed"}:
        return
    families, classes = taxonomy_catalogue()
    retired = retired_taxonomy_class_successors()
    primary_id = validate_taxonomy_mapping(path, primary, "primary_classification", families, classes, retired, errors)
    seen = {primary_id} if primary_id else set()
    for index, mapping in enumerate(secondary):
        class_id = validate_taxonomy_mapping(
            path, mapping, f"secondary_classifications[{index}]", families, classes, retired, errors
        )
        if class_id in seen:
            errors.append(f"{path}: taxonomy class {class_id} is duplicated")
        if class_id:
            seen.add(class_id)


def validate_severity(path: Path, assessment: Any, errors: list[str]) -> None:
    if not isinstance(assessment, dict):
        errors.append(f"{path}: severity_assessment must be an object")
        return
    contract = incident_contract()
    required = set(contract["severity_assessment_required_fields"])
    missing = sorted(required - set(assessment))
    if missing:
        errors.append(f"{path}: severity_assessment missing {', '.join(missing)}")
    severity = assessment.get("severity")
    status = assessment.get("assessment_status")
    if severity not in set(contract["severity_values"]):
        errors.append(f"{path}: invalid Incident severity {severity!r}")
    if status not in set(contract["severity_assessment_status_values"]):
        errors.append(f"{path}: invalid severity assessment_status {status!r}")
    if parse_date(assessment.get("assessed_on")) is None:
        errors.append(f"{path}: severity_assessment.assessed_on must be an ISO date")
    legacy_sources = assessment.get("legacy_sources")
    if not isinstance(legacy_sources, list) or any(
        not isinstance(item, str) or not HISTORICAL_ID.fullmatch(item) for item in legacy_sources
    ):
        errors.append(f"{path}: severity_assessment.legacy_sources must contain historical IDs only")
    if "assessment_basis" in assessment:
        errors.append(f"{path}: assessment_basis is retired from canonical Incident authoring")
    if severity == "SU":
        if status != "requires-incident-review":
            errors.append(f"{path}: SU requires requires-incident-review")
        if not non_empty(assessment.get("assessment_gap")):
            errors.append(f"{path}: SU requires a concrete assessment_gap")
        for field in STRUCTURED_SEVERITY_FIELDS:
            if field in assessment:
                errors.append(f"{path}: SU must not fabricate {field}")
        return
    if status != "incident-assessed":
        errors.append(f"{path}: assessed severity requires incident-assessed status")
    for field in STRUCTURED_SEVERITY_FIELDS:
        value = assessment.get(field)
        if not non_empty(value):
            errors.append(f"{path}: severity_assessment.{field} must be non-empty")
            continue
        lowered = value.casefold()
        if any(fragment in lowered for fragment in GENERIC_SEVERITY_TEXT):
            errors.append(f"{path}: severity_assessment.{field} contains generic/template text")
    rationale = str(assessment.get("band_rationale", ""))
    if re.search(rf"\b{re.escape(str(severity))}\s+because\s+(?:this|it)\s+is\s+(?:an?\s+)?{re.escape(str(severity))}\b", rationale, re.I):
        errors.append(f"{path}: band_rationale is circular")
    adjacent = ADJACENT_BANDS.get(str(severity), set())
    if adjacent and not any(re.search(rf"\b{band}\b", rationale) for band in adjacent):
        errors.append(f"{path}: band_rationale must distinguish at least one adjacent band")


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

def validate_legacy_provenance(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    legacy = record.get("legacy_provenance")
    if not isinstance(legacy, list):
        errors.append(f"{path}: legacy_provenance must be an array")
        return
    for index, item in enumerate(legacy):
        if not isinstance(item, dict):
            errors.append(f"{path}: legacy_provenance[{index}] must be an object")
            continue
        if item.get("legacy_type") not in {"failure_mode", "observation"}:
            errors.append(f"{path}: legacy_provenance[{index}].legacy_type is invalid")
        if not isinstance(item.get("legacy_id"), str) or not HISTORICAL_ID.fullmatch(item["legacy_id"]):
            errors.append(f"{path}: legacy_provenance[{index}].legacy_id is malformed")
        for field in ("relationship", "preservation_note"):
            if not non_empty(item.get(field)):
                errors.append(f"{path}: legacy_provenance[{index}].{field} must be non-empty")
    # Historical tokens deliberately are not resolved to retired record files.


def validate_record(
    path: Path,
    record: dict[str, Any],
    known_ids: set[str] | None = None,
    errors: list[str] | None = None,
    warnings: list[str] | None = None,
    allowed_vendors: set[str] | None = None,
    allowed_products: set[str] | None = None,
    schema_path: Path | None = None,
) -> tuple[list[str], list[str]]:
    del known_ids
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
    validate_severity(path, record.get("severity_assessment"), errors)
    validate_source_records(path, record, errors)
    validate_incident_taxonomy(path, record, errors)
    validate_provenance(path, record, errors)
    validate_legacy_provenance(path, record, errors)
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
    ids: set[str] = set()
    for path in paths:
        try:
            record = load_json(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path}: unable to read JSON: {exc}")
            continue
        record_id = record.get("id")
        if isinstance(record_id, str):
            if record_id in ids:
                errors.append(f"{path}: duplicate Incident id {record_id}")
            ids.add(record_id)
        validate_record(path, record, ids, errors, warnings, schema_path=schema_path)
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
