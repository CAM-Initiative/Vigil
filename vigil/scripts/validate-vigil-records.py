#!/usr/bin/env python3
"""Validate individual VIGIL record JSON files for the clean record design."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
VIGIL_DIR = ROOT / "vigil"
RECORDS_ROOT = VIGIL_DIR / "records"
SCHEMA_PATH = VIGIL_DIR / "VIGIL.Schema.json"
DEPRECATED_OUTPUT_PATHS = [
    VIGIL_DIR / "VIGIL.ActiveRecords.json",
    VIGIL_DIR / "VIGIL.ClosedRecords.json",
    VIGIL_DIR / "VIGIL.Records.Index.json",
    VIGIL_DIR / "VIGIL.Records.json",
]
DEFAULT_RECORD_TYPE_DIRS = [
    RECORDS_ROOT / "observations",
    RECORDS_ROOT / "failures",
    RECORDS_ROOT / "proposals",
    RECORDS_ROOT / "patches",
]
RECORD_TYPE_DIRS = list(DEFAULT_RECORD_TYPE_DIRS)
RESEARCH_ROOT = RECORDS_ROOT / "research"
RESEARCH_REQUIRED_SECTIONS = (
    "Research question",
    "Scope and methodology",
    "Findings",
    "Counter-evidence and alternative explanations",
    "Limitations",
    "Governance implications",
    "Open questions",
    "Bibliography and Primary Sources",
)
RESEARCH_MINIMUM_PUBLISHED_WORDS = 1500
RESEARCH_MINIMUM_SOURCE_CORPUS_ENTRIES = 4

TRIAGE_MODEL_VERSION = "2.0"
ALLOWED_TRIAGE_PRIORITIES = {"P0", "P1", "P2", "P3", "PN", "PU"}
ACTIVE_TRIAGE_PRIORITIES = {"P0", "P1", "P2", "P3"}
ALLOWED_TRIAGE_STATUSES = {
    "intake",
    "under-assessment",
    "action-required",
    "repair-in-progress",
    "verification-pending",
    "monitoring",
    "blocked",
    "closed-actioned",
    "closed-no-action",
    "superseded",
}
PN_FORBIDDEN_STATUSES = {"action-required", "repair-in-progress", "verification-pending"}
CLOSED_TRIAGE_STATUSES = {"closed-actioned", "closed-no-action", "superseded"}
CLOSED_RECORD_STATES = {"closed", "closed-actioned", "closed-no-action", "superseded"}
ALLOWED_SEVERITIES = {"S0", "S1", "S2", "S3", "S4", "SU"}
TRIAGE_HISTORY_REQUIRED = {
    "date",
    "from",
    "to",
    "reason",
    "action_basis",
    "trigger",
    "assessed_by",
    "next_review",
}

RECORD_TYPES = {"observation", "failure_mode", "proposal", "patch", "patch_note"}
CAM_INTERNAL_REFERENCE_PREFIXES = ("CAM-BS", "CAM-EQ", "VIGIL-")
VIGIL_RECORD_ID_PATTERN = re.compile(r"^VIGIL-\d{4}-(?:OBS|FM|PROP|PATCH|RESEARCH)-\d{4}$")
RETIRED_FM_TAXONOMY_FIELDS = {
    "failure_family",
    "failure_subtype",
    "canonical_failure_group",
    "taxonomy_reference",
    "related_failure_groups",
    "allowed_canonical_failure_group_values",
    "classification_status",
}
FALLBACK_ALLOWED_PLATFORM_OR_VENDOR_VALUES = {
    # Fallback only. The primary VIGIL system-context source is
    # VIGIL.Schema.json / system_context_rules.allowed_platform_or_vendor_values.
    "OpenAI",
    "xAI",
    "Anthropic",
    "Meta",
    "Google",
    "DeepSeek",
    "Kimi",
    "Sesame",
    "Cohere",
    "Perplexity",
    "Mistral",
    "Microsoft",
    "GitHub",
    "TikTok",
    "Apple",
    "Amazon",
    "Nvidia",
    "Hugging Face",
    "Stability AI",
    "Runway",
    "Midjourney",
    "Adobe",
    "Character.AI",
    "Replit",
    "Notion",
    "Cursor",
    "Replika",
    "Nomi",
    "Chai",
    "Chub.ai",
    "Candy AI",
    "Kindroid",
    "Pi",
    "HammerAI",
    "Snap",
    "Google Play",
    "CAM Initiative",
    "Multi Vendor",
    "Other",
    "Unknown",
    "Not applicable",
}
FALLBACK_ALLOWED_PRODUCT_OR_SERVICE_VALUES = {
    # Fallback only. The primary VIGIL system-context source is
    # VIGIL.Schema.json / system_context_rules.allowed_product_or_service_values.
    "ChatGPT",
    "Claude",
    "Gemini",
    "Grok",
    "Copilot",
    "Codex",
    "Claude Code",
    "Deep Research",
    "Perplexity Assistant",
    "Llama",
    "Le Chat",
    "GitHub Copilot",
    "TikTok",
    "X",
    "Replit Agent",
    "Cursor",
    "Midjourney",
    "Runway",
    "Firefly",
    "Character.AI",
    "Replika",
    "Nomi",
    "Chai",
    "Chub.ai",
    "Candy AI",
    "Kindroid",
    "Pi",
    "HammerAI",
    "Snapchat",
    "Google Play",
    "Caelestis Architecture Model",
    "VIGIL",
    "Other",
    "Unknown",
    "Not applicable",
}
SYSTEM_CONTEXT_REQUIRED = {
    "platform_or_vendor",
    "product_or_service",
    "specific_model_or_runtime",
    "interface_surface",
}


FM_EVIDENCE_SCOPE_VALUES = {
    "single-provider",
    "multi-provider",
    "provider-unresolved",
    "system-unresolved",
    "not-applicable",
}
FM_EVIDENCE_CONTEXT_REQUIRED = {
    "evidence_scope",
    "evidenced_vendors",
    "evidenced_products_or_services",
    "evidenced_models_or_runtimes",
    "evidenced_systems",
    "evidence_projection",
}
FM_EVIDENCE_PROJECTION_REQUIRED = {
    "basis",
    "method",
    "reconciled_on",
    "inference_boundary",
}
ID_PREFIX = {
    "observation": "OBS",
    "failure_mode": "FM",
    "proposal": "PROP",
    "patch": "PATCH",
    "patch_note": "PATCH",
}
TYPE_DIR = {
    "observation": "observations",
    "failure_mode": "failures",
    "proposal": "proposals",
    "patch": "patches",
    "patch_note": "patches",
}
REQUIRED_COMMON = {
    "id",
    "record_type",
    "record_state",
    "date_recorded",
    "record_identity",
    "summary",
    "evidence_confidence",
    "source_records",
    "system_context",
    "jurisdictional_context",
    "linked_records",
    "cam_internal",
}
OBS_FORBIDDEN = {
    "failure_classification",
    "triage",
    "proposal_scope",
    "change_classification",
    "date_implemented",
    "proposal_rationale",
    "implementation_notes",
    "external_relevance",
    "change_details",
    "implementation_verification",
    "impact_summary",
    "remaining_work",
    "failure_mode_definition",
    "failure_threshold",
}
FM_REQUIRED = {"failure_mode_definition", "failure_threshold", "failure_classification", "triage", "repair_status"}
PROP_REQUIRED = {"proposal_rationale", "proposal_type", "proposal_scope", "implementation_notes", "external_relevance", "next_action"}
PATCH_REQUIRED = {
    "date_implemented",
    "decision_trace",
    "corpus_implementation",
    "record_reconstruction",
    "change_classification",
    "change_details",
    "implementation_verification",
    "impact_summary",
    "remaining_work",
}
DECISION_TRACE_ORIGINS = {
    "failure-response",
    "proposal-implementation",
    "research-integration",
    "retrospective-coverage",
}
DECISION_EVENT_TYPES = {
    "evidence-recorded",
    "failure-identified",
    "proposal-recorded",
    "proposal-approved",
    "corpus-reviewed",
    "implementation-committed",
    "implementation-verified",
    "canonicalised",
    "ledger-reconciled",
    "reconstructed",
}
CORPUS_IMPLEMENTATION_TYPES = {"corpus-amendment", "pre-existing-control", "mixed"}
CORPUS_CANONICAL_STATES = {"canonical-main", "historical-canonical", "branch-only", "unverified"}
CORPUS_CHANGE_KINDS = {"added", "amended", "removed", "relied-upon"}
CORPUS_PRIOR_TEXT_STATES = {
    "captured",
    "new-clause",
    "not-material",
    "unavailable",
    "not-applicable",
}
CORPUS_VERIFICATION_STATES = {
    "verified-canonical",
    "verified-historical",
    "verified-branch-only",
    "unresolved",
}
CORPUS_CURRENT_CLAUSE_STATES = {"current", "later-amended", "repealed", "unknown"}
REPAIR_STATUS_ALLOWED = {"unrepaired", "partially-repaired", "repaired", "superseded", "not-actionable"}
REPAIR_STATUS_REQUIRED = {"status", "repaired_by", "date_repaired", "verification_status", "monitoring_status"}
RESOLUTION_STATUS_ALLOWED = {"open", "routed", "resolved-by-patch", "deferred", "superseded", "closed-no-action"}
RESOLUTION_STATUS_REQUIRED = {"status", "resolved_by", "resolution_note"}
RUNTIME_CONFORMANCE_STATUS_ALLOWED = {"confirmed", "mixed", "unknown", "not-applicable"}
RUNTIME_CONFORMANCE_COUNT_FIELDS = {
    "confirming_runtimes": "confirming_count",
    "non_confirming_runtimes": "non_confirming_count",
    "unknown_runtimes": "unknown_count",
}
PROPOSAL_PATCH_IMPLEMENTATION_FIELDS = {
    "patch_status",
    "date_implemented",
    "change_classification",
    "implementation_verification",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_research_document(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("research record must begin with JSON front matter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("research record has unterminated JSON front matter")
    metadata = json.loads(text[4:end])
    if not isinstance(metadata, dict):
        raise TypeError("research front matter must contain one JSON object")
    return metadata, text[end + 5 :]


def load_research_metadata(path: Path) -> dict[str, Any]:
    metadata, _ = load_research_document(path)
    return metadata


def record_files(root: Path | None = None) -> list[Path]:
    if root is not None:
        if root.is_file():
            return [root]
        return sorted(root.rglob("*.json"), key=lambda path: path.as_posix())
    files: list[Path] = []
    for directory in RECORD_TYPE_DIRS:
        if directory.exists():
            files.extend(directory.rglob("*.json"))
    return sorted(files, key=lambda path: path.as_posix())


def is_blank(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}



def contains_key(value: Any, key: str) -> bool:
    if isinstance(value, dict):
        return key in value or any(contains_key(item, key) for item in value.values())
    if isinstance(value, list):
        return any(contains_key(item, key) for item in value)
    return False


def add_missing(errors: list[str], path: Path, record: dict[str, Any], fields: set[str]) -> None:
    missing = sorted(field for field in fields if is_blank(record.get(field)))
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(missing)}")


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_non_empty_string_array(path: Path, field: str, value: Any, errors: list[str]) -> list[str]:
    if not isinstance(value, list) or any(not is_non_empty_string(item) for item in value):
        errors.append(f"{path}: {field} must be an array of non-empty strings")
        return []
    return value


def validate_patch_trace_structure(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    decision = record.get("decision_trace")
    if not isinstance(decision, dict):
        errors.append(f"{path}: PATCH decision_trace must be an object")
    else:
        if decision.get("origin") not in DECISION_TRACE_ORIGINS:
            errors.append(f"{path}: decision_trace.origin is not canonical")
        validate_non_empty_string_array(
            path,
            "decision_trace.trigger_records",
            decision.get("trigger_records"),
            errors,
        )
        if not is_non_empty_string(decision.get("decision_summary")):
            errors.append(f"{path}: decision_trace.decision_summary must be a non-empty string")
        events = decision.get("events")
        if not isinstance(events, list) or not events:
            errors.append(f"{path}: decision_trace.events must be a non-empty array")
        else:
            for index, event in enumerate(events):
                prefix = f"decision_trace.events[{index}]"
                if not isinstance(event, dict):
                    errors.append(f"{path}: {prefix} must be an object")
                    continue
                for field in ("date", "description", "authority_role"):
                    if not is_non_empty_string(event.get(field)):
                        errors.append(f"{path}: {prefix}.{field} must be a non-empty string")
                if event.get("event_type") not in DECISION_EVENT_TYPES:
                    errors.append(f"{path}: {prefix}.event_type is not canonical")
                references = validate_non_empty_string_array(
                    path,
                    f"{prefix}.evidence_references",
                    event.get("evidence_references"),
                    errors,
                )
                if not references:
                    errors.append(f"{path}: {prefix}.evidence_references must not be empty")

    implementation = record.get("corpus_implementation")
    if not isinstance(implementation, dict):
        errors.append(f"{path}: PATCH corpus_implementation must be an object")
    else:
        if implementation.get("implementation_type") not in CORPUS_IMPLEMENTATION_TYPES:
            errors.append(f"{path}: corpus_implementation.implementation_type is not canonical")
        if implementation.get("canonical_state") not in CORPUS_CANONICAL_STATES:
            errors.append(f"{path}: corpus_implementation.canonical_state is not canonical")
        if not is_non_empty_string(implementation.get("implementation_outcome")):
            errors.append(f"{path}: corpus_implementation.implementation_outcome must be a non-empty string")
        entries = implementation.get("entries")
        if not isinstance(entries, list) or not entries:
            errors.append(f"{path}: corpus_implementation.entries must be a non-empty array")
        else:
            for index, entry in enumerate(entries):
                prefix = f"corpus_implementation.entries[{index}]"
                if not isinstance(entry, dict):
                    errors.append(f"{path}: {prefix} must be an object")
                    continue
                for field in ("instrument_id", "canonical_path", "section", "section_heading", "resulting_text"):
                    if not is_non_empty_string(entry.get(field)):
                        errors.append(f"{path}: {prefix}.{field} must be a non-empty string")
                canonical_path = entry.get("canonical_path")
                if is_non_empty_string(canonical_path) and not (
                    canonical_path.startswith("Governance/Charters/")
                    or canonical_path.startswith("Governance/Constitution/")
                ):
                    errors.append(f"{path}: {prefix}.canonical_path must be a canonical Caelestis governance path")
                if entry.get("change_kind") not in CORPUS_CHANGE_KINDS:
                    errors.append(f"{path}: {prefix}.change_kind is not canonical")
                prior_status = entry.get("prior_text_status")
                if prior_status not in CORPUS_PRIOR_TEXT_STATES:
                    errors.append(f"{path}: {prefix}.prior_text_status is not canonical")
                prior_text = entry.get("prior_text")
                if prior_status == "captured" and not is_non_empty_string(prior_text):
                    errors.append(f"{path}: {prefix}.prior_text must contain literal wording when status is captured")
                if prior_status != "captured" and prior_text is not None:
                    errors.append(f"{path}: {prefix}.prior_text must be null unless prior_text_status is captured")

                source = entry.get("source")
                if not isinstance(source, dict):
                    errors.append(f"{path}: {prefix}.source must be an object")
                else:
                    repository = source.get("repository")
                    commit = source.get("commit")
                    source_path = source.get("path")
                    direct_url = source.get("direct_url")
                    if repository != "CAM-Initiative/Caelestis":
                        errors.append(f"{path}: {prefix}.source.repository must be CAM-Initiative/Caelestis")
                    if not isinstance(commit, str) or len(commit) != 40 or any(
                        character not in "0123456789abcdef" for character in commit
                    ):
                        errors.append(f"{path}: {prefix}.source.commit must be a lowercase 40-character SHA")
                    if source_path != canonical_path:
                        errors.append(f"{path}: {prefix}.source.path must equal canonical_path")
                    expected_url = (
                        f"https://github.com/{repository}/blob/{commit}/{source_path}"
                        if all(isinstance(value, str) for value in (repository, commit, source_path))
                        else ""
                    )
                    if direct_url != expected_url:
                        errors.append(f"{path}: {prefix}.source.direct_url must be the exact commit-addressed file URL")

                verification = entry.get("verification")
                if not isinstance(verification, dict):
                    errors.append(f"{path}: {prefix}.verification must be an object")
                else:
                    status = verification.get("status")
                    if status not in CORPUS_VERIFICATION_STATES:
                        errors.append(f"{path}: {prefix}.verification.status is not canonical")
                    for field in ("verified_on", "review_id"):
                        if not is_non_empty_string(verification.get(field)):
                            errors.append(f"{path}: {prefix}.verification.{field} must be a non-empty string")
                    if not isinstance(verification.get("exact_text_match"), bool):
                        errors.append(f"{path}: {prefix}.verification.exact_text_match must be boolean")
                    if status != "unresolved" and verification.get("exact_text_match") is not True:
                        errors.append(f"{path}: {prefix} verified wording requires exact_text_match true")
                    if verification.get("current_clause_status") not in CORPUS_CURRENT_CLAUSE_STATES:
                        errors.append(f"{path}: {prefix}.verification.current_clause_status is not canonical")

    reconstruction = record.get("record_reconstruction")
    if not isinstance(reconstruction, dict):
        errors.append(f"{path}: PATCH record_reconstruction must be an object")
    else:
        if not isinstance(reconstruction.get("reconstructed"), bool):
            errors.append(f"{path}: record_reconstruction.reconstructed must be boolean")
        for field in ("reconstruction_date", "reason", "review_id", "method"):
            if not is_non_empty_string(reconstruction.get(field)):
                errors.append(f"{path}: record_reconstruction.{field} must be a non-empty string")
        validate_non_empty_string_array(
            path,
            "record_reconstruction.limitations",
            reconstruction.get("limitations"),
            errors,
        )


def load_allowed_system_context_values(
    field_name: str,
    fallback_values: set[str],
    schema_path: Path | None = None,
) -> set[str]:
    """Load an allowed system_context value list from the VIGIL schema-rules contract."""
    try:
        schema = load_json(schema_path or SCHEMA_PATH)
        values = schema.get("system_context_rules", {}).get(field_name, [])
        loaded = {value for value in values if isinstance(value, str) and value}
        return loaded or set(fallback_values)
    except Exception:  # noqa: BLE001 - validator must retain a labelled offline fallback
        return set(fallback_values)


def load_allowed_platform_or_vendor_values(schema_path: Path | None = None) -> set[str]:
    """Load canonical platform/vendor values from VIGIL.Schema.json."""
    return load_allowed_system_context_values(
        "allowed_platform_or_vendor_values",
        FALLBACK_ALLOWED_PLATFORM_OR_VENDOR_VALUES,
        schema_path,
    )


def load_allowed_product_or_service_values(schema_path: Path | None = None) -> set[str]:
    """Load canonical product/service values from VIGIL.Schema.json."""
    return load_allowed_system_context_values(
        "allowed_product_or_service_values",
        FALLBACK_ALLOWED_PRODUCT_OR_SERVICE_VALUES,
        schema_path,
    )


def source_urls(record: dict[str, Any]) -> set[str]:
    urls: set[str] = set()
    for source in record.get("source_records", []):
        if isinstance(source, dict):
            for key in ("source_url", "archive_url"):
                if source.get(key):
                    urls.add(source[key])
    return urls


def related_patch_notes(record: dict[str, Any]) -> list[str]:
    linked = record.get("linked_records")
    if not isinstance(linked, dict):
        return []
    patches = linked.get("related_patch_notes", [])
    if not isinstance(patches, list):
        return []
    return [patch for patch in patches if isinstance(patch, str) and patch]


def validate_relationship_scope(
    path: Path,
    record: dict[str, Any],
    known_ids: set[str],
    errors: list[str],
    warnings: list[str] | None = None,
) -> None:
    record_type = record.get("record_type")
    linked = record.get("linked_records")
    if not isinstance(linked, dict):
        return

    authoritative_ids: set[str] = set()
    for field in (
        "related_observations",
        "related_failure_modes",
        "related_proposals",
        "related_patch_notes",
        "research",
    ):
        values = linked.get(field, [])
        if isinstance(values, list):
            authoritative_ids.update(value for value in values if isinstance(value, str) and value)

    contextual = linked.get("contextual_relations", [])
    if not isinstance(contextual, list):
        errors.append(f"{path}: linked_records.contextual_relations must be an array")
    else:
        seen_contextual: set[str] = set()
        for index, relation in enumerate(contextual):
            label = f"{path}: linked_records.contextual_relations[{index}]"
            if not isinstance(relation, dict):
                errors.append(f"{label} must be an object")
                continue
            missing = sorted(
                field
                for field in ("record_id", "relationship", "chain_inclusion", "rationale")
                if field not in relation
            )
            if missing:
                errors.append(f"{label} missing required keys: {', '.join(missing)}")
            record_id = relation.get("record_id")
            if not isinstance(record_id, str) or not record_id:
                errors.append(f"{label}.record_id must be a non-empty string")
            else:
                if record_id in seen_contextual:
                    errors.append(f"{label}.record_id duplicates contextual relation {record_id!r}")
                seen_contextual.add(record_id)
                if record_id in authoritative_ids:
                    errors.append(
                        f"{label}.record_id {record_id!r} is also present in an authoritative linked_records "
                        "array; a record cannot be both contextual and chain-included"
                    )
                if record_id not in known_ids and warnings is not None:
                    warnings.append(f"{label}.record_id {record_id!r} cannot be resolved; it may be a future record")
            if relation.get("chain_inclusion") is not False:
                errors.append(f"{label}.chain_inclusion must be false")
            if not isinstance(relation.get("rationale"), str) or not relation["rationale"].strip():
                errors.append(f"{label}.rationale must be a non-empty string")

    repair_scope = record.get("repair_scope")
    related_failures = linked.get("related_failure_modes", [])
    if not isinstance(related_failures, list):
        related_failures = []
    if repair_scope is None:
        if record_type in {"proposal", "patch", "patch_note"} and len(related_failures) > 1:
            errors.append(
                f"{path}: multiple authoritative failure-mode links require repair_scope and an explicit "
                "multi-failure-mode exception"
            )
        return
    if record_type not in {"proposal", "patch", "patch_note"}:
        errors.append(f"{path}: repair_scope is permitted only on proposal and PATCH records")
        return
    if not isinstance(repair_scope, dict):
        errors.append(f"{path}: repair_scope must be an object")
        return

    required = {
        "primary_failure_mode",
        "additional_resolved_failure_modes",
        "multi_failure_mode_exception",
        "exception_rationale",
        "verification_by_failure_mode",
    }
    missing = sorted(required - set(repair_scope))
    if missing:
        errors.append(f"{path}: repair_scope missing required keys: {', '.join(missing)}")

    primary = repair_scope.get("primary_failure_mode")
    if primary is not None and (not isinstance(primary, str) or not primary.startswith("VIGIL-") or "-FM-" not in primary):
        errors.append(f"{path}: repair_scope.primary_failure_mode must be a VIGIL FM id or null")
        primary = None
    additional = repair_scope.get("additional_resolved_failure_modes")
    if not isinstance(additional, list) or any(not isinstance(item, str) or "-FM-" not in item for item in additional):
        errors.append(f"{path}: repair_scope.additional_resolved_failure_modes must contain only VIGIL FM ids")
        additional = []
    elif len(additional) != len(set(additional)):
        errors.append(f"{path}: repair_scope.additional_resolved_failure_modes must not contain duplicates")

    resolved = ([primary] if primary else []) + additional
    if primary and primary in additional:
        errors.append(f"{path}: repair_scope primary failure mode must not be repeated as an additional failure")
    if related_failures != resolved:
        errors.append(
            f"{path}: linked_records.related_failure_modes must exactly match repair_scope authoritative order "
            f"{resolved!r}"
        )
    for failure_id in resolved:
        if failure_id not in known_ids and warnings is not None:
            warnings.append(f"{path}: repair_scope failure id {failure_id!r} cannot be resolved; it may be a future record")

    exception = repair_scope.get("multi_failure_mode_exception")
    rationale = repair_scope.get("exception_rationale")
    if not isinstance(exception, bool):
        errors.append(f"{path}: repair_scope.multi_failure_mode_exception must be boolean")
    elif exception:
        if not additional:
            errors.append(f"{path}: multi-failure-mode exception requires at least one additional resolved failure")
        if not isinstance(rationale, str) or not rationale.strip():
            errors.append(f"{path}: multi-failure-mode exception requires a non-empty exception_rationale")
    elif additional:
        errors.append(f"{path}: additional resolved failures require multi_failure_mode_exception true")

    verification = repair_scope.get("verification_by_failure_mode")
    if not isinstance(verification, dict):
        errors.append(f"{path}: repair_scope.verification_by_failure_mode must be an object")
    elif record_type in {"patch", "patch_note"} and set(verification) != set(resolved):
        errors.append(
            f"{path}: PATCH repair_scope.verification_by_failure_mode must contain exactly one result for "
            "each authoritative failure mode"
        )
    elif record_type == "proposal" and verification:
        errors.append(f"{path}: proposal repair_scope.verification_by_failure_mode must remain empty")


def validate_repair_status(
    path: Path,
    record: dict[str, Any],
    errors: list[str],
    warnings: list[str],
) -> None:
    repair_status = record.get("repair_status")
    if not isinstance(repair_status, dict):
        errors.append(f"{path}: FM repair_status must be an object")
        return
    missing = sorted(field for field in REPAIR_STATUS_REQUIRED if field not in repair_status)
    if missing:
        errors.append(f"{path}: FM repair_status missing required keys: {', '.join(missing)}")
    status = repair_status.get("status")
    if status not in REPAIR_STATUS_ALLOWED:
        allowed = ", ".join(sorted(REPAIR_STATUS_ALLOWED))
        errors.append(f"{path}: FM repair_status.status {status!r} is not allowed; allowed values: {allowed}")
    repaired_by = repair_status.get("repaired_by")
    if not isinstance(repaired_by, list):
        errors.append(f"{path}: FM repair_status.repaired_by must be an array")
        repaired_by = []
    elif any(not isinstance(item, str) or not item for item in repaired_by):
        errors.append(f"{path}: FM repair_status.repaired_by must contain only non-empty strings")
    if status in {"repaired", "superseded"} and not repaired_by:
        warnings.append(f"{path}: FM repair_status.status {status!r} should include repaired_by when a patch or successor record exists")
    if status == "repaired" and not repair_status.get("date_repaired"):
        warnings.append(f"{path}: FM repair_status.date_repaired should be populated for repaired records")
    if status == "repaired" and not (repaired_by or related_patch_notes(record)):
        errors.append(
            f"{path}: FM repair_status.status is 'repaired' but no linked patch record appears in "
            "repair_status.repaired_by or linked_records.related_patch_notes"
        )
    if status == "repaired" and str(record.get("record_state", "")).lower() == "active":
        warnings.append(f"{path}: FM record_state is active while repair_status.status is repaired; prefer monitoring")


def validate_triage_model(
    path: Path,
    record: dict[str, Any],
    errors: list[str],
) -> None:
    """Enforce severity/triage model 2.0 without silently reinterpreting legacy records."""
    triage = record.get("triage")
    classification = record.get("failure_classification")
    if not isinstance(triage, dict) or triage.get("model_version") != TRIAGE_MODEL_VERSION:
        return
    if not isinstance(classification, dict):
        errors.append(f"{path}: model 2.0 FM requires failure_classification")
        return

    severity = classification.get("severity")
    if severity not in ALLOWED_SEVERITIES:
        errors.append(
            f"{path}: model 2.0 severity {severity!r} is invalid; expected one of "
            f"{', '.join(sorted(ALLOWED_SEVERITIES))}"
        )
    if is_blank(classification.get("severity_assessment_basis")):
        errors.append(f"{path}: model 2.0 severity requires severity_assessment_basis")
    if severity == "SU" and is_blank(classification.get("severity_assessment_gap")):
        errors.append(f"{path}: SU severity requires severity_assessment_gap")

    required = {
        "triage_priority",
        "triage_owner",
        "triage_status",
        "triage_action_basis",
        "triage_review_date",
        "escalation_required",
        "recommended_next_step",
    }
    add_missing(errors, path, triage, required)
    priority = triage.get("triage_priority")
    status = triage.get("triage_status")
    if priority not in ALLOWED_TRIAGE_PRIORITIES:
        errors.append(
            f"{path}: model 2.0 triage_priority {priority!r} is invalid; expected one of "
            f"{', '.join(sorted(ALLOWED_TRIAGE_PRIORITIES))}"
        )
    if status not in ALLOWED_TRIAGE_STATUSES:
        errors.append(
            f"{path}: model 2.0 triage_status {status!r} is invalid; expected one of "
            f"{', '.join(sorted(ALLOWED_TRIAGE_STATUSES))}"
        )
    if priority in ACTIVE_TRIAGE_PRIORITIES and is_blank(triage.get("recommended_next_step")):
        errors.append(f"{path}: {priority} requires recommended_next_step")
    if priority in {"P0", "P1"}:
        for field in ("triage_owner", "triage_action_basis", "triage_review_date"):
            if is_blank(triage.get(field)):
                errors.append(f"{path}: {priority} requires {field}")
    if priority == "P0" and is_blank(triage.get("escalation_required")):
        errors.append(f"{path}: P0 requires escalation_required or a documented escalation trigger")
    if priority == "PU":
        if is_blank(triage.get("triage_assessment_gap")):
            errors.append(f"{path}: PU requires triage_assessment_gap")
        if is_blank(triage.get("recommended_next_step")):
            errors.append(f"{path}: PU requires a triage next step")
    if priority == "PN" and status in PN_FORBIDDEN_STATUSES:
        errors.append(f"{path}: PN is incompatible with triage_status {status!r}")
    if status in CLOSED_TRIAGE_STATUSES and priority != "PN":
        errors.append(f"{path}: triage_status {status!r} requires PN")
    if str(record.get("record_state", "")).lower() in CLOSED_RECORD_STATES and priority != "PN":
        errors.append(f"{path}: closed record_state requires PN")
    if status == "monitoring" and priority in {"P0", "P1"}:
        for field in ("active_escalation_trigger", "intervention_pathway"):
            if is_blank(triage.get(field)):
                errors.append(f"{path}: monitoring with {priority} requires {field}")

    repair = record.get("repair_status")
    if isinstance(repair, dict) and repair.get("status") == "repaired" and priority in {"P0", "P1"}:
        if is_blank(triage.get("urgent_condition")):
            errors.append(f"{path}: repaired record retaining {priority} requires urgent_condition")

    history = record.get("triage_history")
    if history is not None:
        if not isinstance(history, list):
            errors.append(f"{path}: triage_history must be an append-only array")
        else:
            for index, entry in enumerate(history):
                label = f"{path}: triage_history[{index}]"
                if not isinstance(entry, dict):
                    errors.append(f"{label} must be an object")
                    continue
                add_missing(errors, path, entry, TRIAGE_HISTORY_REQUIRED)
                if entry.get("from") not in ALLOWED_TRIAGE_PRIORITIES:
                    errors.append(f"{label}.from is not a model 2.0 priority")
                if entry.get("to") not in ALLOWED_TRIAGE_PRIORITIES:
                    errors.append(f"{label}.to is not a model 2.0 priority")
                for field in TRIAGE_HISTORY_REQUIRED - {"from", "to"}:
                    if is_blank(entry.get(field)):
                        errors.append(f"{label}.{field} must not be blank")


def validate_resolution_status(path: Path, record: dict[str, Any], errors: list[str], warnings: list[str]) -> None:
    resolution_status = record.get("resolution_status")
    if resolution_status is None:
        return
    if not isinstance(resolution_status, dict):
        errors.append(f"{path}: PROP resolution_status must be an object")
        return
    missing = sorted(field for field in RESOLUTION_STATUS_REQUIRED if field not in resolution_status)
    if missing:
        errors.append(f"{path}: PROP resolution_status missing required keys: {', '.join(missing)}")
    status = resolution_status.get("status")
    if status not in RESOLUTION_STATUS_ALLOWED:
        allowed = ", ".join(sorted(RESOLUTION_STATUS_ALLOWED))
        errors.append(f"{path}: PROP resolution_status.status {status!r} is not allowed; allowed values: {allowed}")
    resolved_by = resolution_status.get("resolved_by")
    if not isinstance(resolved_by, list):
        errors.append(f"{path}: PROP resolution_status.resolved_by must be an array")
        resolved_by = []
    elif any(not isinstance(item, str) or not item for item in resolved_by):
        errors.append(f"{path}: PROP resolution_status.resolved_by must contain only non-empty strings")
    if status == "resolved-by-patch" and not (resolved_by or related_patch_notes(record)):
        warnings.append(f"{path}: PROP resolution_status is resolved-by-patch but no linked patch record is present")



def _validate_non_negative_count(path: Path, label: str, value: Any, errors: list[str]) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        errors.append(f"{path}: {label} must be a non-negative integer")
        return False
    return True


def _validate_string_list(path: Path, label: str, value: Any, errors: list[str]) -> None:
    if not isinstance(value, list):
        errors.append(f"{path}: {label} must be an array")
        return
    if any(not isinstance(item, str) or not item.strip() for item in value):
        errors.append(f"{path}: {label} must contain only non-empty strings")


def _validate_runtime_entries(
    path: Path,
    block_name: str,
    block: dict[str, Any],
    array_name: str,
    count_name: str,
    required_extra_fields: set[str],
    errors: list[str],
) -> None:
    entries = block.get(array_name)
    if entries is None:
        return
    if not isinstance(entries, list):
        errors.append(f"{path}: {block_name}.{array_name} must be an array")
        return
    count = block.get(count_name)
    if isinstance(count, int) and not isinstance(count, bool) and count >= 0 and count != len(entries):
        errors.append(
            f"{path}: {block_name}.{count_name}={count} does not match "
            f"{block_name}.{array_name} length {len(entries)}"
        )
    required = {"vendor", "platform", "runtime", "date_observed"} | required_extra_fields
    for index, entry in enumerate(entries):
        label = f"{block_name}.{array_name}[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{path}: {label} must be an object")
            continue
        list_fields = {"evidence_urls", "related_patch_ids"}
        missing = sorted(
            field
            for field in required
            if field not in entry or (field not in list_fields and is_blank(entry.get(field)))
        )
        if missing:
            errors.append(f"{path}: {label} missing required fields: {', '.join(missing)}")
        for field in ("vendor", "platform", "runtime", "date_observed"):
            value = entry.get(field)
            if value is not None and (not isinstance(value, str) or not value.strip()):
                errors.append(f"{path}: {label}.{field} must be a non-empty string")
        for field in ("evidence_urls", "related_patch_ids"):
            if field in entry:
                _validate_string_list(path, f"{label}.{field}", entry.get(field), errors)



def _unique_non_empty_strings(
    path: Path,
    label: str,
    value: Any,
    errors: list[str],
) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{path}: {label} must be an array")
        return []
    if any(not isinstance(item, str) or not item.strip() for item in value):
        errors.append(f"{path}: {label} must contain only non-empty strings")
        return []
    if len(value) != len(set(value)):
        errors.append(f"{path}: {label} must not contain duplicates")
    return value


def validate_fm_evidence_system_context(
    path: Path,
    context: dict[str, Any],
    errors: list[str],
) -> None:
    missing = sorted(field for field in FM_EVIDENCE_CONTEXT_REQUIRED if field not in context)
    if missing:
        errors.append(
            f"{path}: FM system_context missing evidence-backed fields: {', '.join(missing)}"
        )
        return

    scope = context.get("evidence_scope")
    if scope not in FM_EVIDENCE_SCOPE_VALUES:
        errors.append(
            f"{path}: system_context.evidence_scope {scope!r} is invalid; expected one of "
            f"{', '.join(sorted(FM_EVIDENCE_SCOPE_VALUES))}"
        )

    vendors = _unique_non_empty_strings(
        path, "system_context.evidenced_vendors", context.get("evidenced_vendors"), errors
    )
    products = _unique_non_empty_strings(
        path,
        "system_context.evidenced_products_or_services",
        context.get("evidenced_products_or_services"),
        errors,
    )
    models = _unique_non_empty_strings(
        path,
        "system_context.evidenced_models_or_runtimes",
        context.get("evidenced_models_or_runtimes"),
        errors,
    )

    systems = context.get("evidenced_systems")
    union_vendors: list[str] = []
    union_products: list[str] = []
    union_models: list[str] = []
    if not isinstance(systems, list):
        errors.append(f"{path}: system_context.evidenced_systems must be an array")
        systems = []
    else:
        for index, system in enumerate(systems):
            label = f"system_context.evidenced_systems[{index}]"
            if not isinstance(system, dict):
                errors.append(f"{path}: {label} must be an object")
                continue
            source_title = system.get("source_title")
            if not isinstance(source_title, str) or not source_title.strip():
                errors.append(f"{path}: {label}.source_title must be a non-empty string")
            for optional_field in ("source_url", "deployment_context"):
                value = system.get(optional_field)
                if value is not None and (not isinstance(value, str) or not value.strip()):
                    errors.append(f"{path}: {label}.{optional_field} must be a non-empty string when present")
            entry_vendors = _unique_non_empty_strings(
                path, f"{label}.providers_or_vendors", system.get("providers_or_vendors"), errors
            )
            entry_products = _unique_non_empty_strings(
                path, f"{label}.products_or_services", system.get("products_or_services"), errors
            )
            entry_models = _unique_non_empty_strings(
                path, f"{label}.models_or_runtimes", system.get("models_or_runtimes"), errors
            )
            if not (entry_vendors or entry_products or entry_models):
                errors.append(f"{path}: {label} must identify at least one provider, product, model, or runtime")
            for item in entry_vendors:
                if item not in union_vendors:
                    union_vendors.append(item)
            for item in entry_products:
                if item not in union_products:
                    union_products.append(item)
            for item in entry_models:
                if item not in union_models:
                    union_models.append(item)

    if vendors != union_vendors:
        errors.append(
            f"{path}: system_context.evidenced_vendors must equal the ordered union of evidenced_systems providers"
        )
    if products != union_products:
        errors.append(
            f"{path}: system_context.evidenced_products_or_services must equal the ordered union of "
            "evidenced_systems products"
        )
    if models != union_models:
        errors.append(
            f"{path}: system_context.evidenced_models_or_runtimes must equal the ordered union of "
            "evidenced_systems models/runtimes"
        )

    if scope == "multi-provider" and len(vendors) < 2:
        errors.append(f"{path}: multi-provider evidence_scope requires at least two evidenced_vendors")
    if scope == "single-provider" and len(vendors) != 1:
        errors.append(f"{path}: single-provider evidence_scope requires exactly one evidenced_vendor")
    if scope in {"provider-unresolved", "system-unresolved", "not-applicable"} and vendors:
        errors.append(f"{path}: {scope} evidence_scope must not contain evidenced_vendors")
    if scope in {"system-unresolved", "not-applicable"} and (products or models or systems):
        errors.append(f"{path}: {scope} evidence_scope must not contain concrete evidenced systems")
    if scope == "provider-unresolved" and not (products or models):
        errors.append(
            f"{path}: provider-unresolved evidence_scope requires an evidenced product/model with unresolved provider"
        )

    platform = context.get("platform_or_vendor")
    if platform == "Multi Vendor" and scope != "multi-provider":
        errors.append(f"{path}: platform_or_vendor 'Multi Vendor' requires evidence_scope 'multi-provider'")
    if scope == "multi-provider" and platform != "Multi Vendor":
        errors.append(f"{path}: multi-provider evidence_scope requires platform_or_vendor 'Multi Vendor'")

    if vendors:
        for compatibility_field in ("vendor_cluster", "primary_evidenced_vendors"):
            value = context.get(compatibility_field)
            if value != vendors:
                errors.append(
                    f"{path}: system_context.{compatibility_field} must equal evidenced_vendors for reconciled FMs"
                )

    projection = context.get("evidence_projection")
    if not isinstance(projection, dict):
        errors.append(f"{path}: system_context.evidence_projection must be an object")
    else:
        missing_projection = sorted(
            field for field in FM_EVIDENCE_PROJECTION_REQUIRED if is_blank(projection.get(field))
        )
        if missing_projection:
            errors.append(
                f"{path}: system_context.evidence_projection missing required fields: "
                f"{', '.join(missing_projection)}"
            )
        reconciled_on = projection.get("reconciled_on")
        if isinstance(reconciled_on, str) and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", reconciled_on):
            errors.append(
                f"{path}: system_context.evidence_projection.reconciled_on must use YYYY-MM-DD"
            )


def validate_runtime_conformance(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    block = record.get("runtime_conformance")
    if block is None:
        return
    if record.get("record_type") not in {"patch", "patch_note"}:
        errors.append(f"{path}: runtime_conformance is permitted only on PATCH records")
    if not isinstance(block, dict):
        errors.append(f"{path}: runtime_conformance must be an object")
        return
    required = {"overall_status", "confirming_count", "non_confirming_count", "unknown_count", "notes"}
    missing = sorted(field for field in required if is_blank(block.get(field)))
    if missing:
        errors.append(f"{path}: runtime_conformance missing required fields: {', '.join(missing)}")
    status = block.get("overall_status")
    if status not in RUNTIME_CONFORMANCE_STATUS_ALLOWED:
        allowed = ", ".join(sorted(RUNTIME_CONFORMANCE_STATUS_ALLOWED))
        errors.append(f"{path}: runtime_conformance.overall_status {status!r} is not allowed; allowed values: {allowed}")
    for count_name in ("confirming_count", "non_confirming_count", "unknown_count"):
        _validate_non_negative_count(path, f"runtime_conformance.{count_name}", block.get(count_name), errors)
    notes = block.get("notes")
    if not isinstance(notes, str) or not notes.strip():
        errors.append(f"{path}: runtime_conformance.notes must be a non-empty string")
    _validate_runtime_entries(
        path, "runtime_conformance", block, "confirming_runtimes", "confirming_count", {"evidence_basis"}, errors
    )
    _validate_runtime_entries(
        path,
        "runtime_conformance",
        block,
        "non_confirming_runtimes",
        "non_confirming_count",
        {"failure_expression", "evidence_urls", "related_patch_ids"},
        errors,
    )
    _validate_runtime_entries(
        path, "runtime_conformance", block, "unknown_runtimes", "unknown_count", {"evidence_basis"}, errors
    )


def validate_runtime_non_conformance(path: Path, record: dict[str, Any], errors: list[str]) -> None:
    block = record.get("runtime_non_conformance")
    if block is None:
        return
    if record.get("record_type") != "failure_mode":
        errors.append(f"{path}: runtime_non_conformance is permitted only on FM records")
    if not isinstance(block, dict):
        errors.append(f"{path}: runtime_non_conformance must be an object")
        return
    required = {"non_confirming_count", "unknown_count", "non_confirming_runtimes", "notes"}
    missing = sorted(field for field in required if is_blank(block.get(field)))
    if missing:
        errors.append(f"{path}: runtime_non_conformance missing required fields: {', '.join(missing)}")
    for count_name in ("non_confirming_count", "unknown_count"):
        _validate_non_negative_count(path, f"runtime_non_conformance.{count_name}", block.get(count_name), errors)
    notes = block.get("notes")
    if not isinstance(notes, str) or not notes.strip():
        errors.append(f"{path}: runtime_non_conformance.notes must be a non-empty string")
    _validate_runtime_entries(
        path,
        "runtime_non_conformance",
        block,
        "non_confirming_runtimes",
        "non_confirming_count",
        {"failure_expression", "evidence_urls", "related_patch_ids"},
        errors,
    )
    _validate_runtime_entries(
        path, "runtime_non_conformance", block, "unknown_runtimes", "unknown_count", {"evidence_basis"}, errors
    )


def standards_reference_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        for key in ("standard_id", "id", "title"):
            text = value.get(key)
            if isinstance(text, str) and text:
                return text
    return ""


def is_cam_instrument_reference(value: Any) -> bool:
    return standards_reference_text(value).startswith(CAM_INTERNAL_REFERENCE_PREFIXES)


def linked_record_identifier(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        candidate = value.get("id", value.get("record_id"))
        return candidate if isinstance(candidate, str) else None
    return None


def validate_canonical_path(path: Path, record_id: Any, record_type: Any, errors: list[str]) -> None:
    """Validate canonical repository paths while allowing standalone fixture files."""
    try:
        relative = path.resolve().relative_to(RECORDS_ROOT.resolve())
    except ValueError:
        return
    if not isinstance(record_id, str) or record_type not in TYPE_DIR:
        return
    parts = record_id.split("-")
    if len(parts) < 4:
        return
    expected = Path(TYPE_DIR[record_type]) / parts[1] / f"{record_id}.json"
    if relative != expected:
        errors.append(f"{path}: record path must be vigil/records/{expected.as_posix()} for id/type")


def validate_record(
    path: Path,
    record: dict[str, Any],
    known_ids: set[str],
    errors: list[str],
    warnings: list[str],
    allowed_platform_or_vendor_values: set[str],
    allowed_product_or_service_values: set[str],
) -> None:
    record_id = record.get("id")
    record_type = record.get("record_type")

    common_required = set(REQUIRED_COMMON)
    # Temporary patch scaffolds may intentionally carry an empty source_records array;
    # source_records still must be present and typed as an array below.
    if record_type in {"patch", "patch_note"} and str(record.get("record_state", "")).lower() == "scaffolding":
        common_required.discard("source_records")
    add_missing(errors, path, record, common_required)

    if contains_key(record, "source_data"):
        errors.append(f"{path}: source_data is forbidden anywhere in individual records; use source_records only")
        if isinstance(record.get("source_data"), dict) and "sources" in record["source_data"]:
            errors.append(f"{path}: source_data.sources is forbidden in individual records; use source_records only")

    if not record_id:
        errors.append(f"{path}: missing required id")
    elif path.stem != record_id:
        errors.append(f"{path}: filename stem does not match id {record_id!r}")
    validate_canonical_path(path, record_id, record_type, errors)

    if record_type not in RECORD_TYPES:
        errors.append(f"{path}: invalid record_type {record_type!r}")
    elif record_id:
        expected = f"VIGIL-"
        prefix = ID_PREFIX[record_type]
        parts = str(record_id).split("-")
        if len(parts) < 3 or not str(record_id).startswith(expected) or parts[2] != prefix:
            errors.append(f"{path}: ID prefix must be {prefix!r} for record_type {record_type!r}")

    identity = record.get("record_identity")
    if not isinstance(identity, dict):
        errors.append(f"{path}: record_identity must be an object")
    else:
        if identity.get("record_id") != record_id:
            errors.append(f"{path}: record_identity.record_id does not match id")
        if identity.get("record_type") != record_type:
            errors.append(f"{path}: record_identity.record_type does not match record_type")
        if "status" in identity:
            errors.append(f"{path}: record_identity.status is deprecated; use top-level record_state only")

    sources = record.get("source_records")
    if not isinstance(sources, list):
        errors.append(f"{path}: source_records must be an array")
    else:
        for index, source in enumerate(sources):
            if not isinstance(source, dict):
                errors.append(f"{path}: source_records[{index}] must be an object")
                continue
            legacy_keys = sorted({key for key in ("title", "url", "platform") if key in source})
            if legacy_keys:
                mapping = {"title": "source_title", "url": "source_url", "platform": "source_platform"}
                replacements = ", ".join(f"{key}->{mapping[key]}" for key in legacy_keys)
                errors.append(f"{path}: source_records[{index}] uses legacy source key(s): {replacements}")
            if not source.get("source_url") and source.get("archive_url"):
                warnings.append(f"{path}: source_records[{index}] source_url is blank but archive_url is present")

    linked = record.get("linked_records")
    if not isinstance(linked, dict):
        errors.append(f"{path}: linked_records must be an object")
    else:
        primary_urls = source_urls(record)
        for index, ref in enumerate(linked.get("external_references", [])):
            if isinstance(ref, dict) and (ref.get("url") in primary_urls or ref.get("source_url") in primary_urls):
                errors.append(f"{path}: linked_records.external_references[{index}] duplicates a primary source_records URL")
        for field in (
            "related_observations",
            "related_failure_modes",
            "related_proposals",
            "related_patch_notes",
            "research",
        ):
            value = linked.get(field, [])
            if not isinstance(value, list):
                errors.append(f"{path}: linked_records.{field} must be an array")
                continue
            for linked_id in value:
                identifier = linked_record_identifier(linked_id)
                requires_vigil_record_id = field != "research" or (isinstance(identifier, str) and identifier.startswith("VIGIL-"))
                if requires_vigil_record_id and (not isinstance(identifier, str) or not VIGIL_RECORD_ID_PATTERN.fullmatch(identifier)):
                    errors.append(f"{path}: linked_records.{field} contains malformed VIGIL record id {linked_id!r}")
                    continue
                if (
                    isinstance(identifier, str)
                    and identifier
                    and identifier not in known_ids
                    and requires_vigil_record_id
                ):
                    warnings.append(f"{path}: linked record id {identifier!r} in {field} cannot be resolved; it may be a future record")
        standards = linked.get("standards", [])
        if isinstance(standards, list):
            for index, standard in enumerate(standards):
                if is_cam_instrument_reference(standard):
                    errors.append(
                        f"{path}: linked_records.standards[{index}] contains a CAM/VIGIL internal reference; "
                        "CAM and VIGIL internal IDs belong in cam_internal routing fields, not linked_records.standards."
                    )
        elif standards:
            errors.append(f"{path}: linked_records.standards must be an array when present")
        if record_type == "proposal" and record.get("external_standards_required") is True and not linked.get("standards"):
            warnings.append(f"{path}: external standards are marked required but absent from proposal linked_records.standards")

    validate_relationship_scope(path, record, known_ids, errors, warnings)

    system_context = record.get("system_context")
    if not isinstance(system_context, dict):
        errors.append(f"{path}: system_context must be an object")
    else:
        add_missing(errors, path, system_context, SYSTEM_CONTEXT_REQUIRED)
        if "product_family" in system_context:
            errors.append(f"{path}: system_context.product_family is deprecated; use platform_or_vendor")
        if "specific_model" in system_context:
            errors.append(f"{path}: system_context.specific_model is deprecated; use specific_model_or_runtime")
        platform_or_vendor = system_context.get("platform_or_vendor")
        if (
            isinstance(platform_or_vendor, str)
            and platform_or_vendor
            and platform_or_vendor not in allowed_platform_or_vendor_values
        ):
            allowed = ", ".join(sorted(allowed_platform_or_vendor_values))
            errors.append(
                f"{path}: system_context.platform_or_vendor {platform_or_vendor!r} is not canonical; "
                f"allowed values: {allowed}"
            )
        # Multi Vendor is an evidentiary routing value, not a product-list escape hatch.
        # Authors must provide separated vendor evidence arrays and keep product_or_service
        # to one canonical value (usually "Other" for genuinely multi-product records).
        if platform_or_vendor == "Multi Vendor":
            vendor_cluster = system_context.get("vendor_cluster")
            if not isinstance(vendor_cluster, list) or not vendor_cluster or any(
                not isinstance(item, str) or not item.strip() for item in vendor_cluster
            ):
                errors.append(
                    f"{path}: system_context.vendor_cluster must be a non-empty array of non-empty strings "
                    "when platform_or_vendor is 'Multi Vendor'"
                )
            primary_evidenced_vendors = system_context.get("primary_evidenced_vendors")
            if not isinstance(primary_evidenced_vendors, list) or not primary_evidenced_vendors or any(
                not isinstance(item, str) or not item.strip() for item in primary_evidenced_vendors
            ):
                errors.append(
                    f"{path}: system_context.primary_evidenced_vendors must be a non-empty array of "
                    "non-empty strings when platform_or_vendor is 'Multi Vendor'"
                )
            comparative_vendor_notes = system_context.get("comparative_vendor_notes")
            if comparative_vendor_notes is not None:
                if not isinstance(comparative_vendor_notes, dict) or any(
                    not isinstance(item, str) for item in comparative_vendor_notes.values()
                ):
                    errors.append(
                        f"{path}: system_context.comparative_vendor_notes must be an object with string values"
                    )
        product_or_service = system_context.get("product_or_service")
        if (
            isinstance(product_or_service, str)
            and product_or_service
            and product_or_service not in allowed_product_or_service_values
        ):
            allowed = ", ".join(sorted(allowed_product_or_service_values))
            errors.append(
                f"{path}: system_context.product_or_service {product_or_service!r} is not canonical; "
                f"allowed values: {allowed}"
            )
        runtime = system_context.get("specific_model_or_runtime")
        if not isinstance(runtime, str) or not runtime.strip():
            errors.append(f"{path}: system_context.specific_model_or_runtime must be a non-empty string")
        interface = system_context.get("interface_surface")
        if isinstance(interface, list):
            if not interface or any(not isinstance(item, str) or not item.strip() for item in interface):
                errors.append(f"{path}: system_context.interface_surface array must contain non-empty strings")
        elif not isinstance(interface, str) or not interface.strip():
            errors.append(f"{path}: system_context.interface_surface must be a non-empty string or array of non-empty strings")

    validate_runtime_conformance(path, record, errors)
    validate_runtime_non_conformance(path, record, errors)

    jurisdiction = record.get("jurisdictional_context")
    if isinstance(jurisdiction, dict):
        if str(jurisdiction.get("primary_jurisdiction", "")).lower() in {"unknown", "to be assessed"}:
            warnings.append(f"{path}: jurisdictional_context.primary_jurisdiction uses unknown/to be assessed")
    cam = record.get("cam_internal")
    if isinstance(cam, dict):
        preferred_route = {
            "observation": "related_or_similar_instruments",
            "failure_mode": "affected_instruments",
            "proposal": "target_instruments",
            "patch": "changed_instruments",
            "patch_note": "changed_instruments",
        }.get(record_type)
        if preferred_route is not None and preferred_route in cam and not isinstance(cam.get(preferred_route), list):
            errors.append(f"{path}: cam_internal.{preferred_route} must be an array when present")
        deprecated_routes = {
            "observation": ("affected_instruments", "target_instruments", "changed_instruments"),
            "failure_mode": ("target_instruments", "changed_instruments"),
            "proposal": ("affected_instruments", "changed_instruments"),
            "patch": ("affected_instruments", "target_instruments"),
            "patch_note": ("affected_instruments", "target_instruments"),
        }.get(record_type, ())
        for route in deprecated_routes:
            if route in cam:
                warnings.append(
                    f"{path}: cam_internal.{route} is non-preferred for record_type {record_type!r}; "
                    f"prefer cam_internal.{preferred_route}"
                )

    if record_type == "observation":
        present = sorted(field for field in OBS_FORBIDDEN if field in record)
        if present:
            errors.append(f"{path}: OBS contains forbidden record-class fields: {', '.join(present)}")
        if contains_key(record, "patch_status"):
            errors.append(f"{path}: OBS contains forbidden patch_status; patch state belongs in PATCH records")
    elif record_type == "failure_mode":
        add_missing(errors, path, record, FM_REQUIRED)
        validate_fm_evidence_system_context(path, system_context, errors)
        validate_repair_status(path, record, errors, warnings)
        validate_triage_model(path, record, errors)
        classification = record.get("failure_classification")
        if isinstance(classification, dict):
            retired = sorted(RETIRED_FM_TAXONOMY_FIELDS.intersection(classification))
            if retired:
                errors.append(
                    f"{path}: FM failure_classification contains retired taxonomy fields: {', '.join(retired)}"
                )
            facets = classification.get("faceted_analysis")
            if isinstance(facets, dict) and "external_taxonomy_refs" in facets:
                errors.append(
                    f"{path}: FM failure_classification.faceted_analysis.external_taxonomy_refs is retired "
                    "during the taxonomy-free transition"
                )
            add_missing(
                errors,
                path,
                classification,
                {"persistence", "reproducibility", "visibility"},
            )
        linked = record.get("linked_records")
        if isinstance(linked, dict) and "related_failure_modes" in linked:
            errors.append(
                f"{path}: FM linked_records.related_failure_modes is retired; peer failure similarity belongs "
                "to taxonomy membership"
            )
        cam = record.get("cam_internal")
        if isinstance(cam, dict):
            retired_cam = sorted(
                {"cam_taxonomy_primary_group", "cam_taxonomy_secondary_groups", "cam_taxonomy_candidate_labels"}
                .intersection(cam)
            )
            if retired_cam:
                errors.append(f"{path}: FM cam_internal contains retired taxonomy fields: {', '.join(retired_cam)}")
        if "proposed_taxonomy_patch" in record:
            errors.append(f"{path}: FM proposed_taxonomy_patch is retired")
    elif record_type == "proposal":
        add_missing(errors, path, record, PROP_REQUIRED)
        state = str(record.get("record_state", "")).lower()
        forbidden_patch_fields = sorted(field for field in PROPOSAL_PATCH_IMPLEMENTATION_FIELDS if contains_key(record, field))
        if forbidden_patch_fields:
            errors.append(
                f"{path}: PROP contains forbidden patch implementation field(s): "
                f"{', '.join(forbidden_patch_fields)}; implemented work belongs in PATCH records"
            )
        if is_blank(record.get("proposal_scope")):
            errors.append(f"{path}: PROP proposal_scope must not be empty")
        validate_resolution_status(path, record, errors, warnings)
        if state in {"implemented", "completed"}:
            errors.append(f"{path}: PROP record_state {state!r} is an implementation claim; use PATCH records for implementation")
        if state == "closed-actioned":
            resolution_status = record.get("resolution_status")
            resolution_state = resolution_status.get("status") if isinstance(resolution_status, dict) else None
            if resolution_state != "resolved-by-patch":
                errors.append(
                    f"{path}: PROP record_state 'closed-actioned' requires resolution_status.status "
                    "'resolved-by-patch'"
                )
            if not related_patch_notes(record) and not (
                isinstance(resolution_status, dict) and resolution_status.get("resolved_by")
            ):
                errors.append(f"{path}: PROP record_state 'closed-actioned' requires a linked patch record")
    elif record_type in {"patch", "patch_note"}:
        add_missing(errors, path, record, PATCH_REQUIRED)
        validate_patch_trace_structure(path, record, errors)
        if is_blank(record.get("date_implemented")):
            errors.append(f"{path}: PATCH date_implemented is required")
        if is_blank(record.get("change_details")) or is_blank(record.get("implementation_verification")):
            errors.append(f"{path}: PATCH changed/implementation fields are required")
        verification = record.get("implementation_verification")
        evidence = verification.get("evidence") if isinstance(verification, dict) else ""
        if not record.get("source_records") and not evidence:
            errors.append(f"{path}: PATCH lacks implemented-change evidence")


def validate_research_record(
    path: Path,
    record: dict[str, Any],
    known_ids: set[str],
    errors: list[str],
    body: str = "",
) -> None:
    required = {
        "id",
        "record_type",
        "record_state",
        "date_recorded",
        "title",
        "summary",
        "status",
        "research_method",
        "governance_purpose",
        "evidence_confidence",
        "domains",
        "linked_records",
        "publication_status",
        "research_scope",
        "limitations",
        "source_corpus",
    }
    add_missing(errors, path, record, required)
    record_id = record.get("id")
    if record.get("record_type") != "research":
        errors.append(f"{path}: research front matter record_type must be 'research'")
    if not isinstance(record_id, str) or not record_id.startswith("VIGIL-") or "-RESEARCH-" not in record_id:
        errors.append(f"{path}: research id must use VIGIL-YYYY-RESEARCH-NNNN")
    elif path.stem != record_id:
        errors.append(f"{path}: filename stem does not match research id {record_id!r}")
    for field in ("title", "summary", "status", "research_method", "governance_purpose"):
        if not isinstance(record.get(field), str) or not record[field].strip():
            errors.append(f"{path}: {field} must be a non-empty string")
    for field in ("research_scope", "limitations"):
        if not isinstance(record.get(field), str) or not record[field].strip():
            errors.append(f"{path}: {field} must be a non-empty string")
    if record.get("publication_status") not in {"draft", "published", "superseded"}:
        errors.append(f"{path}: publication_status must be draft, published, or superseded")
    domains = record.get("domains")
    if not isinstance(domains, list) or not domains or any(
        not isinstance(domain, str) or not domain.strip() for domain in domains
    ):
        errors.append(f"{path}: domains must be a non-empty array of non-empty strings")
    linked = record.get("linked_records")
    if not isinstance(linked, dict):
        errors.append(f"{path}: linked_records must be an object")
        return
    for field in ("related_observations", "related_failure_modes", "related_proposals", "related_patch_notes"):
        values = linked.get(field)
        if not isinstance(values, list):
            errors.append(f"{path}: linked_records.{field} must be an array")
            continue
        for linked_id in values:
            if not isinstance(linked_id, str) or not linked_id:
                errors.append(f"{path}: linked_records.{field} must contain only non-empty strings")
            elif linked_id not in known_ids:
                errors.append(f"{path}: linked research target {linked_id!r} cannot be resolved")

    source_corpus = record.get("source_corpus")
    if not isinstance(source_corpus, list):
        errors.append(f"{path}: source_corpus must be an array")
        source_corpus = []
    source_domains: set[str] = set()
    source_urls: set[str] = set()
    for index, source in enumerate(source_corpus):
        if not isinstance(source, dict):
            errors.append(f"{path}: source_corpus[{index}] must be an object")
            continue
        for field in ("title", "publisher", "url", "source_kind", "relevance"):
            if not is_non_empty_string(source.get(field)):
                errors.append(f"{path}: source_corpus[{index}].{field} must be a non-empty string")
        url = source.get("url")
        if is_non_empty_string(url):
            parsed = urlparse(url)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                errors.append(f"{path}: source_corpus[{index}].url must be an external HTTP(S) URL")
            else:
                source_urls.add(url)
                source_domains.add(parsed.netloc.lower().removeprefix("www."))

    if record.get("publication_status") == "published":
        word_count = len(re.findall(r"\b[\w’'-]+\b", body))
        if word_count < RESEARCH_MINIMUM_PUBLISHED_WORDS:
            errors.append(
                f"{path}: published research body has {word_count} words; "
                f"minimum is {RESEARCH_MINIMUM_PUBLISHED_WORDS}"
            )
        for section in RESEARCH_REQUIRED_SECTIONS:
            if not re.search(rf"^##\s+{re.escape(section)}\s*$", body, flags=re.MULTILINE | re.IGNORECASE):
                errors.append(f"{path}: published research missing required section '## {section}'")
        if len(source_corpus) < RESEARCH_MINIMUM_SOURCE_CORPUS_ENTRIES:
            errors.append(
                f"{path}: published research requires at least "
                f"{RESEARCH_MINIMUM_SOURCE_CORPUS_ENTRIES} source_corpus entries"
            )
        bibliography_match = re.search(
            r"^##\s+Bibliography and Primary Sources\s*$([\s\S]*)",
            body,
            flags=re.MULTILINE | re.IGNORECASE,
        )
        bibliography = bibliography_match.group(1) if bibliography_match else ""
        bibliography_urls = set(re.findall(r"https?://[^\s)>]+", bibliography))
        if len(bibliography_urls) < RESEARCH_MINIMUM_SOURCE_CORPUS_ENTRIES:
            errors.append(
                f"{path}: published research bibliography requires at least "
                f"{RESEARCH_MINIMUM_SOURCE_CORPUS_ENTRIES} distinct external URLs"
            )
        body_before_bibliography = body[: bibliography_match.start()] if bibliography_match else body
        claim_level_links = set(re.findall(r"\[[^\]]+\]\((https?://[^)]+)\)", body_before_bibliography))
        if len(claim_level_links) < 3:
            errors.append(f"{path}: published research requires at least 3 claim-level source links")
        if record.get("evidence_confidence") in {"corroborated", "externally corroborated"}:
            if len(source_domains) < 2 and not is_non_empty_string(record.get("corroboration_scope")):
                errors.append(
                    f"{path}: corroborated research from one publisher domain requires "
                    "a non-empty corroboration_scope qualification"
                )


def validate(root: Path | None = None, schema_path: Path | None = None) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if root is None:
        for deprecated_path in DEPRECATED_OUTPUT_PATHS:
            if deprecated_path.exists():
                errors.append(f"{deprecated_path}: deprecated generated file must not exist")

    allowed_platform_or_vendor_values = load_allowed_platform_or_vendor_values(schema_path)
    allowed_product_or_service_values = load_allowed_product_or_service_values(schema_path)

    files = record_files(root)
    records_by_path: dict[Path, dict[str, Any]] = {}
    research_by_path: dict[Path, dict[str, Any]] = {}
    research_body_by_path: dict[Path, str] = {}
    ids: set[str] = set()
    for path in files:
        try:
            record = load_json(path)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path}: unable to read JSON: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"{path}: individual record file must contain one JSON object")
            continue
        if "records" in record or "generated_notice" in record:
            errors.append(f"{path}: individual record file must not contain a generated aggregate wrapper")
        records_by_path[path] = record
        if isinstance(record.get("id"), str):
            if record["id"] in ids:
                errors.append(f"{path}: duplicate id {record['id']!r}")
            ids.add(record["id"])

    if root is None and RECORD_TYPE_DIRS == DEFAULT_RECORD_TYPE_DIRS and RESEARCH_ROOT.exists():
        for path in sorted(RESEARCH_ROOT.rglob("*.md"), key=lambda item: item.as_posix()):
            try:
                record, body = load_research_document(path)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"{path}: unable to read research metadata: {exc}")
                continue
            research_by_path[path] = record
            research_body_by_path[path] = body
            record_id = record.get("id")
            if isinstance(record_id, str):
                if record_id in ids:
                    errors.append(f"{path}: duplicate id {record_id!r}")
                ids.add(record_id)

    for path, record in records_by_path.items():
        validate_record(
            path,
            record,
            ids,
            errors,
            warnings,
            allowed_platform_or_vendor_values,
            allowed_product_or_service_values,
        )

    for path, record in research_by_path.items():
        validate_research_record(path, record, ids, errors, research_body_by_path.get(path, ""))

    records_by_id = {
        record["id"]: record
        for record in records_by_path.values()
        if isinstance(record.get("id"), str)
    }
    for path, research in research_by_path.items():
        research_id = research.get("id")
        linked = research.get("linked_records", {})
        if not isinstance(research_id, str) or not isinstance(linked, dict):
            continue
        for field in ("related_observations", "related_failure_modes", "related_proposals", "related_patch_notes"):
            for linked_id in linked.get(field, []):
                target = records_by_id.get(linked_id)
                target_research = target.get("linked_records", {}).get("research", []) if target else []
                if research_id not in target_research:
                    errors.append(
                        f"{path}: {linked_id} must reciprocally include {research_id} in linked_records.research"
                    )

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)

    if errors:
        print("VIGIL record validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "VIGIL record validation passed: "
        f"{len(records_by_path)} JSON files, {len(research_by_path)} research files, "
        f"{len(ids)} unique records."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", help="Optional record or fixture directory to validate.")
    args = parser.parse_args()
    return validate(Path(args.path) if args.path else None)


if __name__ == "__main__":
    raise SystemExit(main())
