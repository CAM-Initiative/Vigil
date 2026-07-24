#!/usr/bin/env python3
"""Validate individual VIGIL record JSON files for the clean record design."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

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

RECORD_TYPES = {"observation", "failure_mode", "proposal", "patch", "patch_note"}
CAM_INTERNAL_REFERENCE_PREFIXES = ("CAM-BS", "CAM-EQ", "VIGIL-")
FALLBACK_ALLOWED_CANONICAL_FAILURE_GROUPS = {
    # Fallback only. The primary VIGIL taxonomy source is
    # VIGIL.Schema.json / cam_failure_taxonomy.allowed_canonical_failure_group_values,
    # derived from CAM-EQ2026-OPERATIONS-003-SUP-01 Appendix B.
    "execution",
    "arbitration",
    "epistemic",
    "relational",
    "security-integrity",
    "state-context",
    "ux-representation",
    "governance",
    "infrastructure-continuity",
    "classification",
    "economic-legitimacy",
    "provisional",
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


def load_research_metadata(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("research record must begin with JSON front matter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("research record has unterminated JSON front matter")
    metadata = json.loads(text[4:end])
    if not isinstance(metadata, dict):
        raise TypeError("research front matter must contain one JSON object")
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


def load_allowed_canonical_failure_groups(schema_path: Path | None = None) -> set[str]:
    """Load canonical failure groups from the VIGIL schema-derived CAM taxonomy registry."""
    try:
        schema = load_json(schema_path or SCHEMA_PATH)
        values = schema.get("cam_failure_taxonomy", {}).get("allowed_canonical_failure_group_values", [])
        loaded = {value for value in values if isinstance(value, str) and value}
        return loaded or set(FALLBACK_ALLOWED_CANONICAL_FAILURE_GROUPS)
    except Exception:  # noqa: BLE001 - validator must retain a labelled offline fallback
        return set(FALLBACK_ALLOWED_CANONICAL_FAILURE_GROUPS)


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
    allowed_canonical_failure_groups: set[str],
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
                if (
                    isinstance(linked_id, str)
                    and linked_id
                    and linked_id not in known_ids
                    and (field != "research" or linked_id.startswith("VIGIL-"))
                ):
                    warnings.append(f"{path}: linked record id {linked_id!r} in {field} cannot be resolved; it may be a future record")
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
        validate_repair_status(path, record, errors, warnings)
        classification = record.get("failure_classification")
        if isinstance(classification, dict):
            if is_blank(classification.get("failure_family")):
                errors.append(f"{path}: FM failure_classification.failure_family is required")
            canonical_group = classification.get("canonical_failure_group")
            if is_blank(canonical_group):
                errors.append(f"{path}: FM failure_classification.canonical_failure_group is required")
            elif canonical_group not in allowed_canonical_failure_groups:
                allowed = ", ".join(sorted(allowed_canonical_failure_groups))
                errors.append(
                    f"{path}: FM failure_classification.canonical_failure_group {canonical_group!r} "
                    f"is not in allowed CAM taxonomy groups: {allowed}"
                )
            failure_family = classification.get("failure_family")
            if (
                isinstance(failure_family, str)
                and failure_family
                and canonical_group in allowed_canonical_failure_groups
                and failure_family not in allowed_canonical_failure_groups
            ):
                warnings.append(
                    f"{path}: FM failure_classification.failure_family {failure_family!r} is not a canonical "
                    "group; treating it as a local family/subtype routed through canonical_failure_group"
                )
            related_groups = classification.get("related_failure_groups")
            if isinstance(related_groups, list):
                for related_group in related_groups:
                    if isinstance(related_group, str) and related_group and related_group not in allowed_canonical_failure_groups:
                        warnings.append(
                            f"{path}: FM failure_classification.related_failure_groups contains "
                            f"non-canonical value {related_group!r}; move local concepts to harm_vectors, "
                            "routing_note, or subtype fields"
                        )
            add_missing(
                errors,
                path,
                classification,
                {"taxonomy_reference", "related_failure_groups", "persistence", "reproducibility", "visibility"},
            )
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


def validate(root: Path | None = None, schema_path: Path | None = None) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if root is None:
        for deprecated_path in DEPRECATED_OUTPUT_PATHS:
            if deprecated_path.exists():
                errors.append(f"{deprecated_path}: deprecated generated file must not exist")

    allowed_canonical_failure_groups = load_allowed_canonical_failure_groups(schema_path)
    allowed_platform_or_vendor_values = load_allowed_platform_or_vendor_values(schema_path)
    allowed_product_or_service_values = load_allowed_product_or_service_values(schema_path)

    files = record_files(root)
    records_by_path: dict[Path, dict[str, Any]] = {}
    research_by_path: dict[Path, dict[str, Any]] = {}
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
                record = load_research_metadata(path)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"{path}: unable to read research metadata: {exc}")
                continue
            research_by_path[path] = record
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
            allowed_canonical_failure_groups,
            allowed_platform_or_vendor_values,
            allowed_product_or_service_values,
        )

    for path, record in research_by_path.items():
        validate_research_record(path, record, ids, errors)

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
