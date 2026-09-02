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
TAXONOMY_INDEX_PATH = VIGIL_DIR / "taxonomy" / "VIGIL.FailureTaxonomy.Index.json"
RECORDS_ROOT = VIGIL_DIR / "records"
SCHEMA_PATH = VIGIL_DIR / "VIGIL.Schema.json"
DEPRECATED_OUTPUT_PATHS = [
    VIGIL_DIR / "VIGIL.ActiveRecords.json",
    VIGIL_DIR / "VIGIL.ClosedRecords.json",
    VIGIL_DIR / "VIGIL.Records.Index.json",
    VIGIL_DIR / "VIGIL.Records.json",
]
DEFAULT_RECORD_TYPE_DIRS = [
    RECORDS_ROOT / "incidents",
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
DIAGNOSTIC_METHOD = "human-ai-collaborative-analysis"
DIAGNOSTIC_PLATFORM = "OpenAI ChatGPT"
DIAGNOSTIC_REVIEW_STATUS = "human-reviewed-and-approved"
DIAGNOSTIC_REQUIRED_FIELDS = {
    "method", "diagnostic_date", "human_role", "ai_role", "ai_platform", "ai_model",
    "model_attribution_basis", "review_status", "authority_boundary", "date_attribution_status",
}
TAXONOMY_CLASSIFICATION_STATUSES = {"classified", "family-only", "candidate-new-class", "unmapped", "deferred"}
TAXONOMY_CLASSIFICATION_REQUIRED = {
    "taxonomy_version", "classification_status", "classification_basis", "classification_confidence",
    "classified_on", "classification_review_provenance",
}
TAXONOMY_REVIEW_REQUIRED = {
    "method", "review_date", "ai_provider", "ai_platform", "ai_model", "ai_role",
    "human_review_status", "authority_boundary",
}
TAXONOMY_SECONDARY_REQUIRED = {
    "family", "class", "classification_basis", "classification_confidence",
}
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
INCIDENT_ALLOWED_SEVERITIES = {"S1", "S2", "S3", "S4", "SU"}
INCIDENT_SEVERITY_STATUSES = {"provisionally-migrated", "incident-assessed", "requires-incident-review"}
INCIDENT_ADJACENT_SEVERITIES = {
    "S1": {"S2"},
    "S2": {"S1", "S3"},
    "S3": {"S2", "S4"},
    "S4": {"S3"},
}
INCIDENT_GENERIC_SEVERITY_BASES = (
    "reflects high impact or risk",
    "reflects material but bounded harm",
    "reflects limited or low-impact harm",
    "reflects severe, widespread, or enduring harm",
    "explain the incident-level severity determination",
)
CANONICAL_INCIDENT_SOURCE_TYPES = {
    "incident database entry", "news article", "official announcement", "incident report",
    "technical report", "technical analysis", "platform status report", "product documentation",
    "product changelog", "research paper", "investigation report", "government report",
    "legal filing or decision", "press release", "social media post", "first-person account",
    "interaction record", "repository record", "governance record", "standards document",
    "observation record", "web page",
}
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

RECORD_TYPES = {"incident", "observation", "failure_mode", "proposal", "patch", "patch_note"}
CAM_INTERNAL_REFERENCE_PREFIXES = ("CAM-BS", "CAM-EQ", "VIGIL-")
VIGIL_RECORD_ID_PATTERN = re.compile(
    r"^(?:VIGIL-INC-\d{6}|VIGIL-\d{4}-(?:OBS|FM|PROP|PATCH|LEARN|RESEARCH)-\d{4})$"
)
WITHDRAWN_REFERENCE_ID_PATTERN = re.compile(r"^VIGIL-\d{4}-(?:PROP|PATCH|LEARN)-\d{4}$")
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
    "incident": "INC",
    "observation": "OBS",
    "failure_mode": "FM",
    "proposal": "PROP",
    "patch": "PATCH",
    "patch_note": "PATCH",
}
TYPE_DIR = {
    "incident": "incidents",
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
FM_REQUIRED = {
    "failure_mode_definition", "failure_threshold", "failure_classification", "taxonomy_classification",
    "triage", "repair_status",
}
INCIDENT_REQUIRED = {
    "incident_identity", "vigil_assessment", "severity_assessment", "taxonomy_classification", "preferred_evidence",
    "diagnostic_provenance",
    "interpretive_provenance",
}
INCIDENT_FORBIDDEN = {
    "corpus_coverage",
    "repair_status",
    "remaining_gaps",
    "proposal_needed",
    "patch_note_needed",
}
INCIDENT_CAM_INTERNAL_ALLOWED = {
    "governance_layer",
    "routing_note",
    "cam_relevance",
    "cam_failure_type",
    "cam_observed_failure",
    "cam_internal_failure_statement",
    "cam_expected_control",
    "cam_compliance_status",
}
INCIDENT_CLASSIFICATION_STATUSES = {
    "unclassified", "provisionally-classified", "classified", "classification-disputed",
    "requires-human-review",
}
INCIDENT_EVIDENCE_STATUSES = {
    "verified",
    "independently-corroborated",
    "independent-reporting",
    "registry-reported",
    "first-party-reported",
    "allegation-on-record",
    "internal-observation",
    "user-reported",
    "disputed",
    "unverified",
    "not-assessed",
}
INCIDENT_DATE_PRECISIONS = {"exact-day", "date-range", "month", "year", "reported-date", "unknown"}
INCIDENT_EXTERNAL_RELATIONSHIPS = {
    "same-incident", "related-incident", "broader-event", "narrower-event",
    "supporting-registry-entry",
}
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
      