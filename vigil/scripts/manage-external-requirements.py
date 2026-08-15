#!/usr/bin/env python3
"""Validate and build VIGIL Layer 1 external-governance requirements.

This machinery is deliberately independent of VIGIL evidentiary record classes and
of Caelestis. It validates source/version provenance, access posture, requirement
identity, extraction completeness and generated review projections.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "external_sources"
REQ = ROOT / "external_requirements"
LEDGER_PATH = SOURCES / "ledger.json"
SCOPE_PATH = REQ / "source-scope.json"
REQUIREMENTS_PATH = REQ / "requirements.json"
INDEX_PATH = REQ / "requirements-index.json"
COMPLETENESS_PATH = REQ / "completeness-report.json"
CATALOGUE_PATH = REQ / "EXTERNAL-AI-GOVERNANCE-REQUIREMENTS.md"
ACCESS_PATH = REQ / "SOURCE-ACCESS-LIMITATIONS.md"
PRIORITY_PATH = REQ / "BLOCKED-SOURCE-PRIORITIES.md"

SOURCE_ROLES = {
    "primary-ai-governance",
    "supporting-external-authority",
    "context-or-discovery",
    "excluded-from-current-scope",
}
ACCESS_STATES = {
    "direct-public-primary",
    "direct-licensed-primary",
    "official-public-extract",
    "official-metadata-only",
    "secondary-source-only",
    "source-unavailable",
}
INSUFFICIENT_FULL_REVIEW_ACCESS = {
    "official-public-extract",
    "official-metadata-only",
    "secondary-source-only",
    "source-unavailable",
}
EXTRACTION_STATES = {
    "not-started",
    "in-progress",
    "partial",
    "complete",
    "blocked-access",
    "supporting-only",
    "context-only",
    "excluded",
    "superseded-version",
}
POSTURES = {
    "mandatory-normative",
    "recommended-practice",
    "permitted-optional",
    "definitional",
    "informative-guidance",
    "implementation-example",
    "conformity-evidence-expectation",
}
EXPECTATION_TYPES = {
    "positive-duty", "prohibition", "permission", "definition", "guidance",
    "implementation-example", "conformity-criterion", "right-or-protection",
}
ALIGNMENT_PRIORITIES = {
    "critical-alignment-source", "high-value-alignment-source",
    "supporting-specialist-source", "low-immediate-priority",
}
INTERPRETATION_STATES = {
    "authoritative-direct",
    "reviewed-analytical-summary",
    "provisional-interpretation",
    "needs-specialist-review",
}
LIFECYCLE_STAGES = {
    "governance",
    "design",
    "development",
    "data-acquisition",
    "training",
    "testing-evaluation",
    "conformity-assessment",
    "placing-on-market",
    "deployment",
    "operation-use",
    "monitoring",
    "incident-response",
    "change-management",
    "retirement",
    "supply-chain",
    "cross-lifecycle",
    "not-specified",
}
GOVERNANCE_CONCEPTS = {
    "accountability",
    "ai-literacy",
    "assurance",
    "change-management",
    "conformity",
    "data-governance",
    "documentation",
    "environmental-impact",
    "fairness-bias",
    "human-oversight",
    "impact-assessment",
    "incident-governance",
    "inventory",
    "lifecycle-governance",
    "monitoring",
    "privacy",
    "provenance",
    "risk-management",
    "robustness",
    "safety",
    "security",
    "supply-chain",
    "testing-evaluation",
    "traceability",
    "transparency",
    "worker-affected-person-rights",
}
REQ_ID_RE = re.compile(r"^EXTREQ-[A-F0-9]{16}$")
IDENTITY_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PROVENANCE_BASES = {
    "direct-primary-text",
    "licensed-primary-text",
    "official-public-extract",
    "official-metadata-only",
    "secondary-source",
}

REQUIRED_REQUIREMENT_FIELDS = {
    "requirement_id",
    "identity_key",
    "vigil_source_id",
    "external_source_id",
    "source_version",
    "canonical_source_identifier",
    "issuer",
    "jurisdiction",
    "source_class",
    "source_lifecycle_state",
    "source_role",
    "authoritative_locator",
    "clause_or_control",
    "parent_section_or_group",
    "source_access_status",
    "source_review_date",
    "source_access_notes",
    "requirement_summary",
    "requirement_posture",
    "expectation_type",
    "applicable_actor",
    "governed_object",
    "lifecycle_stage",
    "governance_expectation",
    "evidence_expectation",
    "timing_or_frequency",
    "required_artefacts",
    "verification_method",
    "applicability_conditions",
    "exceptions_or_qualifications",
    "governance_concepts",
    "source_defined_tags",
    "related_external_requirements",
    "interpretation_status",
    "interpretation_provenance",
    "review_limitations",
}
REQUIRED_SCOPE_FIELDS = {
    "vigil_source_id",
    "external_source_id",
    "source_version",
    "canonical_source_identifier",
    "source_role",
    "source_access_status",
    "access_checked_at",
    "access_locator",
    "source_access_notes",
    "extraction_status",
    "extraction_scope_notes",
    "inaccessible_sections",
    "known_unreviewed_sections",
    "next_action",
    "alignment_priority",
    "alignment_priority_rationale",
    "maintainer_action_required",
    "maintainer_action",
}
FORBIDDEN_INTERNAL_FIELDS = {
    "caelestis_instrument",
    "caelestis_canonical_code",
    "caelestis_coverage",
    "internal_alignment_status",
    "patch_requirement",
    "corpus_gap",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def json_text(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False, sort_keys=False) + "\n"


def source_key(value: dict[str, Any]) -> tuple[str, str]:
    return str(value.get("vigil_source_id", "")), str(value.get("source_version", ""))


def requirement_id(vigil_source_id: str, source_version: str, clause: str, identity_key: str) -> str:
    seed = "|".join((vigil_source_id, source_version, clause.strip(), identity_key.strip()))
    return "EXTREQ-" + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16].upper()


def non_empty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def string_array(value: Any, *, nonempty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (not nonempty or bool(value))
        and all(non_empty(item) for item in value)
        and len(value) == len(set(value))
    )


def validate_scope(
    ledger_by_key: dict[tuple[str, str], dict[str, Any]],
    scope_entries: list[dict[str, Any]],
    errors: list[str],
) -> dict[tuple[str, str], dict[str, Any]]:
    scope_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for entry in scope_entries:
        key = source_key(entry)
        missing_fields = sorted(REQUIRED_SCOPE_FIELDS - set(entry))
        unexpected_fields = sorted(set(entry) - REQUIRED_SCOPE_FIELDS)
        if missing_fields:
            errors.append(f"source-scope {key} missing required fields {missing_fields}")
        if unexpected_fields:
            errors.append(f"source-scope {key} contains fields not permitted by schema {unexpected_fields}")
        if key in scope_by_key:
            errors.append(f"duplicate source-scope key {key}")
            continue
        scope_by_key[key] = entry
        ledger = ledger_by_key.get(key)
        if ledger is None:
            errors.append(f"source-scope entry {key} does not resolve to ledger source/version")
            continue
        if entry.get("external_source_id") != ledger.get("external_source_id"):
            errors.append(f"source-scope {key} external_source_id differs from ledger")
        if entry.get("canonical_source_identifier") != ledger.get("canonical_identifier"):
            errors.append(f"source-scope {key} canonical_source_identifier differs from ledger")
        role = entry.get("source_role")
        access = entry.get("source_access_status")
        extraction = entry.get("extraction_status")
        if role not in SOURCE_ROLES:
            errors.append(f"source-scope {key} has invalid source_role {role!r}")
        if access not in ACCESS_STATES:
            errors.append(f"source-scope {key} has invalid source_access_status {access!r}")
        if extraction not in EXTRACTION_STATES:
            errors.append(f"source-scope {key} has invalid extraction_status {extraction!r}")
        for field in ("access_checked_at", "access_locator", "source_access_notes", "extraction_scope_notes"):
            if not non_empty(entry.get(field)):
                errors.append(f"source-scope {key} requires non-empty {field}")
        if not isinstance(entry.get("access_checked_at"), str) or not DATE_RE.fullmatch(entry["access_checked_at"]):
            errors.append(f"source-scope {key} access_checked_at must use YYYY-MM-DD")
        if not string_array(entry.get("inaccessible_sections", [])):
            errors.append(f"source-scope {key} inaccessible_sections must be a unique string array")
        if not string_array(entry.get("known_unreviewed_sections", [])):
            errors.append(f"source-scope {key} known_unreviewed_sections must be a unique string array")
        if not non_empty(entry.get("next_action")):
            errors.append(f"source-scope {key} next_action must be non-empty")
        if entry.get("alignment_priority") not in ALIGNMENT_PRIORITIES:
            errors.append(f"source-scope {key} has invalid alignment_priority")
        if not non_empty(entry.get("alignment_priority_rationale")):
            errors.append(f"source-scope {key} alignment_priority_rationale must be non-empty")
        action_required = entry.get("maintainer_action_required")
        if not isinstance(action_required, bool):
            errors.append(f"source-scope {key} maintainer_action_required must be boolean")
        if action_required and not non_empty(entry.get("maintainer_action")):
            errors.append(f"source-scope {key} requires maintainer_action")
        if extraction == "complete" and access in INSUFFICIENT_FULL_REVIEW_ACCESS:
            errors.append(f"source-scope {key} cannot be complete with access {access}")
        if extraction == "complete" and entry.get("inaccessible_sections"):
            errors.append(f"source-scope {key} complete extraction cannot list inaccessible sections")
        if extraction == "complete" and entry.get("known_unreviewed_sections"):
            errors.append(f"source-scope {key} complete extraction cannot retain known unreviewed sections")
        if extraction == "blocked-access" and access not in INSUFFICIENT_FULL_REVIEW_ACCESS:
            errors.append(f"source-scope {key} blocked-access conflicts with access {access}")
        if extraction in {"blocked-access", "partial", "in-progress", "not-started"} and not action_required:
            errors.append(f"source-scope {key} incomplete primary extraction requires a maintainer action")
        expected = {
            "supporting-external-authority": "supporting-only",
            "context-or-discovery": "context-only",
            "excluded-from-current-scope": "excluded",
        }.get(role)
        if expected and extraction != expected:
            errors.append(f"source-scope {key} role {role} requires extraction_status {expected}")
        if role == "primary-ai-governance" and extraction in {"supporting-only", "context-only", "excluded"}:
            errors.append(f"source-scope {key} primary role conflicts with extraction_status {extraction}")

    missing = sorted(set(ledger_by_key) - set(scope_by_key))
    extra = sorted(set(scope_by_key) - set(ledger_by_key))
    if missing:
        errors.append(f"source-scope omits {len(missing)} ledger source version(s): {missing[:5]}")
    if extra:
        errors.append(f"source-scope includes {len(extra)} unknown source version(s): {extra[:5]}")
    return scope_by_key


def validate_requirements(
    requirements: list[dict[str, Any]],
    ledger_by_key: dict[tuple[str, str], dict[str, Any]],
    scope_by_key: dict[tuple[str, str], dict[str, Any]],
    errors: list[str],
) -> None:
    ids: set[str] = set()
    counts: Counter[tuple[str, str]] = Counter()
    for index, req in enumerate(requirements):
        label = req.get("requirement_id") or f"requirements[{index}]"
        missing = sorted(REQUIRED_REQUIREMENT_FIELDS - set(req))
        if missing:
            errors.append(f"{label}: missing required fields {missing}")
            continue
        forbidden = sorted(FORBIDDEN_INTERNAL_FIELDS & set(req))
        if forbidden:
            errors.append(f"{label}: contains forbidden Caelestis-alignment fields {forbidden}")
        unexpected = sorted(set(req) - REQUIRED_REQUIREMENT_FIELDS)
        if unexpected:
            errors.append(f"{label}: contains fields not permitted by schema {unexpected}")
        req_id = req["requirement_id"]
        if not isinstance(req_id, str) or not REQ_ID_RE.fullmatch(req_id):
            errors.append(f"{label}: invalid requirement_id")
        if req_id in ids:
            errors.append(f"duplicate requirement_id {req_id}")
        ids.add(req_id)
        identity_key = req.get("identity_key")
        if not isinstance(identity_key, str) or not IDENTITY_RE.fullmatch(identity_key):
            errors.append(f"{label}: invalid identity_key")
        expected_id = requirement_id(
            str(req.get("vigil_source_id")),
            str(req.get("source_version")),
            str(req.get("clause_or_control")),
            str(identity_key),
        )
        if req_id != expected_id:
            errors.append(f"{label}: identifier is not deterministic; expected {expected_id}")

        key = source_key(req)
        counts[key] += 1
        ledger = ledger_by_key.get(key)
        scope = scope_by_key.get(key)
        if ledger is None or scope is None:
            errors.append(f"{label}: references unknown source/version {key}")
            continue
        metadata_pairs = {
            "external_source_id": ledger.get("external_source_id"),
            "canonical_source_identifier": ledger.get("canonical_identifier"),
            "issuer": ledger.get("issuer"),
            "jurisdiction": ledger.get("jurisdiction"),
            "source_class": ledger.get("source_class"),
            "source_lifecycle_state": ledger.get("source_lifecycle_state"),
            "authoritative_locator": ledger.get("official_locator"),
            "source_role": scope.get("source_role"),
            "source_access_status": scope.get("source_access_status"),
        }
        for field, expected in metadata_pairs.items():
            if req.get(field) != expected:
                errors.append(f"{label}: {field} differs from registered source metadata")
        if scope.get("extraction_status") == "superseded-version":
            errors.append(f"{label}: silently points at a superseded source version")
        if scope.get("source_role") != "primary-ai-governance":
            errors.append(f"{label}: requirement extraction is limited to primary AI-governance sources")
        if not non_empty(req.get("clause_or_control")):
            errors.append(f"{label}: clause_or_control is required")
        parent = req.get("parent_section_or_group")
        if parent is not None and not non_empty(parent):
            errors.append(f"{label}: parent_section_or_group must be null or non-empty")
        if not non_empty(req.get("source_access_notes")):
            errors.append(f"{label}: source_access_notes must be non-empty")
        if not isinstance(req.get("source_review_date"), str) or not DATE_RE.fullmatch(req["source_review_date"]):
            errors.append(f"{label}: source_review_date must use YYYY-MM-DD")
        if not non_empty(req.get("requirement_summary")) or not non_empty(req.get("governance_expectation")):
            errors.append(f"{label}: requirement summary and governance expectation must be non-empty")
        if req.get("requirement_posture") not in POSTURES:
            errors.append(f"{label}: invalid requirement_posture")
        if req.get("expectation_type") not in EXPECTATION_TYPES:
            errors.append(f"{label}: invalid expectation_type")
        if req.get("interpretation_status") not in INTERPRETATION_STATES:
            errors.append(f"{label}: invalid interpretation_status")
        for field in ("applicable_actor", "governed_object", "lifecycle_stage", "governance_concepts"):
            if not string_array(req.get(field), nonempty=True):
                errors.append(f"{label}: {field} must be a non-empty unique string array")
        for value in req.get("lifecycle_stage", []):
            if value not in LIFECYCLE_STAGES:
                errors.append(f"{label}: invalid lifecycle_stage {value!r}")
        for value in req.get("governance_concepts", []):
            if value not in GOVERNANCE_CONCEPTS:
                errors.append(f"{label}: invalid governance_concept {value!r}")
        for field in ("evidence_expectation", "timing_or_frequency", "required_artefacts", "verification_method", "applicability_conditions", "exceptions_or_qualifications", "related_external_requirements", "review_limitations"):
            if not string_array(req.get(field)):
                errors.append(f"{label}: {field} must be a unique string array")
        tags = req.get("source_defined_tags")
        if not isinstance(tags, list):
            errors.append(f"{label}: source_defined_tags must be an array")
        else:
            schemes: set[str] = set()
            for tag in tags:
                if not isinstance(tag, dict) or set(tag) != {"scheme", "values"}:
                    errors.append(f"{label}: each source_defined_tag requires only scheme and values")
                    continue
                if not non_empty(tag.get("scheme")) or not string_array(tag.get("values"), nonempty=True):
                    errors.append(f"{label}: source_defined_tag requires a scheme and non-empty unique values")
                if tag.get("scheme") in schemes:
                    errors.append(f"{label}: source_defined_tag schemes must be unique")
                schemes.add(tag.get("scheme"))
        if req.get("expectation_type") == "prohibition" and req.get("requirement_posture") != "mandatory-normative":
            errors.append(f"{label}: prohibition must have mandatory-normative posture")
        if req.get("requirement_posture") == "mandatory-normative" and req.get("interpretation_status") in {"provisional-interpretation", "needs-specialist-review"}:
            errors.append(f"{label}: mandatory posture requires reviewed authoritative source interpretation")

        status = req.get("interpretation_status")
        access = req.get("source_access_status")
        provenance = req.get("interpretation_provenance")
        if not isinstance(provenance, dict):
            errors.append(f"{label}: interpretation_provenance must be an object")
        else:
            for field in ("basis", "reviewed_by", "review_method", "source_locator", "source_fingerprint"):
                if not non_empty(provenance.get(field)):
                    errors.append(f"{label}: interpretation_provenance.{field} must be non-empty")
            if set(provenance) != {"basis", "reviewed_by", "review_method", "source_locator", "source_fingerprint"}:
                errors.append(f"{label}: interpretation_provenance has missing or unexpected fields")
            if provenance.get("basis") not in PROVENANCE_BASES:
                errors.append(f"{label}: invalid interpretation_provenance.basis")
            if provenance.get("source_fingerprint") != ledger.get("fingerprint"):
                errors.append(f"{label}: interpretation provenance fingerprint differs from ledger")
            expected_basis = {
                "direct-public-primary": "direct-primary-text",
                "direct-licensed-primary": "licensed-primary-text",
                "official-public-extract": "official-public-extract",
                "official-metadata-only": "official-metadata-only",
                "secondary-source-only": "secondary-source",
            }.get(access)
            if expected_basis and provenance.get("basis") != expected_basis:
                errors.append(f"{label}: provenance basis conflicts with source access {access}")
        if status == "authoritative-direct" and access not in {"direct-public-primary", "direct-licensed-primary"}:
            errors.append(f"{label}: authoritative-direct claim conflicts with access {access}")
        if access == "official-public-extract" and status in {"authoritative-direct", "reviewed-analytical-summary"}:
            errors.append(f"{label}: public-extract access requires a provisional or specialist interpretation state")
        if status in {"authoritative-direct", "reviewed-analytical-summary"} and access in {
            "official-metadata-only", "secondary-source-only", "source-unavailable"
        }:
            errors.append(f"{label}: direct review claim conflicts with access {access}")
        if access in {"official-metadata-only", "secondary-source-only", "source-unavailable"}:
            errors.append(f"{label}: requirement cannot be established from access {access}")

    for req in requirements:
        for related in req.get("related_external_requirements", []):
            if related == req.get("requirement_id"):
                errors.append(f"{related}: requirement cannot relate to itself")
            elif related not in ids:
                errors.append(f"{req.get('requirement_id')}: related requirement {related} does not resolve")

    for key, scope in scope_by_key.items():
        count = counts[key]
        status = scope.get("extraction_status")
        role = scope.get("source_role")
        if status == "complete" and count == 0:
            errors.append(f"source-scope {key} claims complete extraction but has no requirements")
        if role == "primary-ai-governance" and count == 0 and status not in {
            "not-started", "in-progress", "blocked-access", "superseded-version"
        }:
            errors.append(f"primary source {key} is omitted without explicit incomplete/access state")
        if status in {"supporting-only", "context-only", "excluded", "blocked-access", "superseded-version"} and count:
            errors.append(f"source-scope {key} status {status} conflicts with {count} requirement record(s)")


def build_outputs(
    ledger_by_key: dict[tuple[str, str], dict[str, Any]],
    scope_entries: list[dict[str, Any]],
    requirements: list[dict[str, Any]],
    reviewed_at: str,
) -> dict[Path, str]:
    sorted_requirements = sorted(requirements, key=lambda item: item["requirement_id"])
    index = {
        "schema_version": "1.1",
        "generated_from": "requirements.json",
        "generated_at": reviewed_at,
        "requirement_count": len(sorted_requirements),
        "requirements": [
            {
                "requirement_id": req["requirement_id"],
                "vigil_source_id": req["vigil_source_id"],
                "external_source_id": req["external_source_id"],
                "source_version": req["source_version"],
                "clause_or_control": req["clause_or_control"],
                "requirement_summary": req["requirement_summary"],
                "requirement_posture": req["requirement_posture"],
                "expectation_type": req["expectation_type"],
                "applicable_actor": req["applicable_actor"],
                "governance_concepts": req["governance_concepts"],
                "interpretation_status": req["interpretation_status"],
            }
            for req in sorted_requirements
        ],
    }

    by_source: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for req in sorted_requirements:
        by_source[source_key(req)].append(req)

    source_rows = []
    for scope in sorted(scope_entries, key=lambda item: (item["external_source_id"], item["source_version"])):
        key = source_key(scope)
        ledger = ledger_by_key[key]
        items = by_source[key]
        source_rows.append({
            "vigil_source_id": scope["vigil_source_id"],
            "external_source_id": scope["external_source_id"],
            "title": ledger.get("title"),
            "source_version": scope["source_version"],
            "source_role": scope["source_role"],
            "source_access_status": scope["source_access_status"],
            "source_access_notes": scope["source_access_notes"],
            "extraction_status": scope["extraction_status"],
            "extraction_scope_notes": scope["extraction_scope_notes"],
            "requirement_count": len(items),
            "reviewed_requirement_count": sum(item["interpretation_status"] in {"authoritative-direct", "reviewed-analytical-summary"} for item in items),
            "unresolved_interpretation_count": sum(item["interpretation_status"] in {"provisional-interpretation", "needs-specialist-review"} for item in items),
            "inaccessible_sections": scope["inaccessible_sections"],
            "known_unreviewed_sections": scope["known_unreviewed_sections"],
            "next_action": scope["next_action"],
            "alignment_priority": scope["alignment_priority"],
            "alignment_priority_rationale": scope["alignment_priority_rationale"],
            "maintainer_action_required": scope["maintainer_action_required"],
            "maintainer_action": scope["maintainer_action"],
        })
    completeness = {
        "schema_version": "1.1",
        "generated_at": reviewed_at,
        "source_version_count": len(source_rows),
        "primary_source_version_count": sum(row["source_role"] == "primary-ai-governance" for row in source_rows),
        "requirement_count": len(sorted_requirements),
        "sources": source_rows,
    }

    catalogue = [
        "# External AI-Governance Requirements",
        "",
        "Generated from the maintained Layer 0 source ledger, Layer 1 source-scope decisions and requirement records. This catalogue does not state Caelestis coverage or conformance.",
        "",
        f"- Registered source versions: {len(source_rows)}",
        f"- Primary AI-governance source versions: {completeness['primary_source_version_count']}",
        f"- Requirement records: {len(sorted_requirements)}",
        "",
    ]
    for row in source_rows:
        catalogue += [
            f"## {row['title']} — {row['source_version']}",
            "",
            f"- Source: `{row['vigil_source_id']}` / `{row['external_source_id']}`",
            f"- Role: `{row['source_role']}`",
            f"- Access: `{row['source_access_status']}`",
            f"- Extraction: `{row['extraction_status']}`",
            f"- Requirements: {row['requirement_count']} ({row['reviewed_requirement_count']} reviewed; {row['unresolved_interpretation_count']} unresolved)",
            f"- Next action: {row['next_action']}",
            "",
        ]
        items = by_source[(row["vigil_source_id"], row["source_version"])]
        if items:
            catalogue += [
                "| Requirement | Clause/control | Summary | Posture / type | Actor | Object | Governance expectation | Evidence expectation | Timing / artefact / verification | Applicability / qualification | Review / access |",
                "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            ]
            for req in sorted(items, key=lambda item: (item["clause_or_control"], item["requirement_id"])):
                actor = ", ".join(req["applicable_actor"])
                evidence = "; ".join(req["evidence_expectation"]) or "Not expressly stated"
                applicability = "; ".join(req["applicability_conditions"] + req["exceptions_or_qualifications"]) or "Generally applicable within the cited provision"
                governed_object = ", ".join(req["governed_object"])
                operational_detail = "; ".join(req["timing_or_frequency"] + req["required_artefacts"] + req["verification_method"]) or "Not expressly stated"
                safe = lambda value: str(value).replace("|", "\\|").replace("\n", " ")
                catalogue.append(
                    f"| `{req['requirement_id']}` | {safe(req['clause_or_control'])} | {safe(req['requirement_summary'])} | `{req['requirement_posture']}` / `{req['expectation_type']}` | "
                    f"{safe(actor)} | {safe(governed_object)} | {safe(req['governance_expectation'])} | {safe(evidence)} | {safe(operational_detail)} | {safe(applicability)} | `{req['interpretation_status']}` / `{req['source_access_status']}` |"
                )
            catalogue.append("")
        else:
            catalogue += [f"No requirement records are asserted. {scope_note(row, scope_entries)}", ""]

    limited_rows = [
        row for row in source_rows
        if row["maintainer_action_required"] or row["source_access_status"] in INSUFFICIENT_FULL_REVIEW_ACCESS
    ]
    access = [
        "# Source Access Limitations and Maintainer Access List",
        "",
        "A source listed here has not been represented as fully reviewed. Titles, abstracts, metadata or secondary summaries are not treated as substitutes for normative source text.",
        "",
        "| Source | Version | Role | Access | Extraction | Inaccessible material | Maintainer action |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in limited_rows:
        inaccessible = "; ".join(row["inaccessible_sections"]) or "Full or sufficient source text"
        action_text = row["maintainer_action"] or "No action currently required"
        access.append(
            f"| {row['title']} | `{row['source_version']}` | `{row['source_role']}` | `{row['source_access_status']}` | "
            f"`{row['extraction_status']}` | {inaccessible.replace('|', '\\|')} | {action_text.replace('|', '\\|')} |"
        )
    access.append("")

    blocked_primary = [row for row in source_rows if row["source_role"] == "primary-ai-governance" and row["extraction_status"] == "blocked-access"]
    priority = [
        "# Blocked Primary-Source Priorities",
        "",
        "This is an access-planning projection. Priority does not imply that inaccessible normative requirements were reviewed.",
        "",
        "| Priority | Source | Version | Governance value | Access limitation | Next action |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    priority_order = {"critical-alignment-source": 0, "high-value-alignment-source": 1, "supporting-specialist-source": 2, "low-immediate-priority": 3}
    for row in sorted(blocked_primary, key=lambda item: (priority_order[item["alignment_priority"]], item["title"], item["source_version"])):
        priority.append(
            f"| `{row['alignment_priority']}` | {row['title']} | `{row['source_version']}` | "
            f"{row['alignment_priority_rationale'].replace('|', '\\|')} | {row['source_access_status']} | {row['next_action'].replace('|', '\\|')} |"
        )
    priority.append("")

    return {
        INDEX_PATH: json_text(index),
        COMPLETENESS_PATH: json_text(completeness),
        CATALOGUE_PATH: "\n".join(catalogue).rstrip() + "\n",
        ACCESS_PATH: "\n".join(access).rstrip() + "\n",
        PRIORITY_PATH: "\n".join(priority).rstrip() + "\n",
    }


def scope_note(row: dict[str, Any], scope_entries: list[dict[str, Any]]) -> str:
    for scope in scope_entries:
        if source_key(scope) == (row["vigil_source_id"], row["source_version"]):
            return scope["extraction_scope_notes"]
    return "No extraction note is available."


def load_and_validate() -> tuple[dict[Path, str], list[str]]:
    errors: list[str] = []
    ledger = load_json(LEDGER_PATH)
    scope_doc = load_json(SCOPE_PATH)
    req_doc = load_json(REQUIREMENTS_PATH)
    ledger_entries = ledger.get("entries", [])
    scope_entries = scope_doc.get("entries", [])
    requirements = req_doc.get("requirements", [])
    if scope_doc.get("schema_version") != "1.1" or req_doc.get("schema_version") != "1.1":
        errors.append("source-scope and requirements documents must use schema_version 1.1")
    if not isinstance(scope_doc.get("reviewed_at"), str) or not DATE_RE.fullmatch(scope_doc["reviewed_at"]):
        errors.append("source-scope reviewed_at must use YYYY-MM-DD")
    if not isinstance(req_doc.get("updated_at"), str) or not DATE_RE.fullmatch(req_doc["updated_at"]):
        errors.append("requirements updated_at must use YYYY-MM-DD")
    if not isinstance(ledger_entries, list) or not isinstance(scope_entries, list) or not isinstance(requirements, list):
        raise ValueError("ledger, source-scope and requirements collections must be arrays")
    ledger_by_key = {source_key(item): item for item in ledger_entries}
    if len(ledger_by_key) != len(ledger_entries):
        errors.append("external source ledger contains duplicate source/version keys")
    scope_by_key = validate_scope(ledger_by_key, scope_entries, errors)
    validate_requirements(requirements, ledger_by_key, scope_by_key, errors)
    outputs = build_outputs(ledger_by_key, scope_entries, requirements, str(scope_doc.get("reviewed_at", "")))
    return outputs, errors


def build() -> None:
    outputs, errors = load_and_validate()
    if errors:
        raise ValueError("\n".join(errors))
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path}")


def validate(check_generated: bool) -> None:
    outputs, errors = load_and_validate()
    if check_generated:
        for path, expected in outputs.items():
            actual = path.read_text(encoding="utf-8") if path.exists() else ""
            if actual != expected:
                errors.append(f"generated output is stale: {path}")
    if errors:
        raise ValueError("\n".join(errors))
    req_count = len(load_json(REQUIREMENTS_PATH)["requirements"])
    source_count = len(load_json(SCOPE_PATH)["entries"])
    print(f"External requirements valid: {source_count} source versions, {req_count} requirements")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build")
    validate_parser = sub.add_parser("validate")
    validate_parser.add_argument("--check-generated", action="store_true")
    args = parser.parse_args()
    if args.command == "build":
        build()
    else:
        validate(args.check_generated)


if __name__ == "__main__":
    main()
