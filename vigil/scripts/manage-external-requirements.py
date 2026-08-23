#!/usr/bin/env python3
"""Validate and build VIGIL's canonical external governance requirements corpus.

The maintained corpus records authoritative external-source abstractions and source
review state. CAM applicability and coverage are assessed separately under
`vigil/cam_assessment/`.
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
REGISTRY_PATH = SOURCES / "source-registry.json"
SCOPE_PATH = REQ / "source-scope.json"
REQUIREMENTS_PATH = REQ / "requirements.json"
INDEX_PATH = REQ / "requirements-index.json"
COMPLETENESS_PATH = REQ / "completeness-report.json"
CATALOGUE_PATH = REQ / "EXTERNAL-AI-GOVERNANCE-REQUIREMENTS.md"
ACCESS_PATH = REQ / "SOURCE-ACCESS-LIMITATIONS.md"
PRIORITY_PATH = REQ / "BLOCKED-SOURCE-PRIORITIES.md"
REVIEW_ASSURANCE_PATH = REQ / "source-review-assurance.json"
COVERAGE_PATH = REQ / "source-coverage-manifests.json"
CROSSWALKS_PATH = REQ / "derivative-crosswalks.json"
CROSSWALK_INDEX_PATH = REQ / "derivative-crosswalk-index.json"
CROSSWALK_VIEW_PATH = REQ / "DERIVATIVE-CROSSWALKS.md"
PROVENANCE_REF = "vigil/provenance/AUTHORSHIP-PROVENANCE.json"

DEFAULT_PROVENANCE = {
    "content_origin": "ai-authored",
    "generation_mode": "semi-autonomous",
    "human_role": "contract-approver",
    "human_authorship": False,
    "human_review_status": "not-reviewed",
    "human_verification_status": "not-verified",
    "declaration": PROVENANCE_REF,
}
GENERATED_BASE = {
    "content_origin": "deterministically-generated",
    "generation_mode": "deterministic-generation",
    "human_role": "contract-approver",
    "human_authorship": False,
    "human_review_status": "not-reviewed",
    "human_verification_status": "not-verified",
    "declaration": PROVENANCE_REF,
}

SOURCE_ROLES = {
    "primary-ai-governance", "supporting-external-authority",
    "context-or-discovery", "excluded-from-current-scope",
}
ACCESS_STATES = {
    "direct-public-primary", "direct-licensed-primary", "official-public-extract",
    "official-metadata-only", "secondary-source-only", "source-unavailable",
}
INSUFFICIENT_FULL_REVIEW_ACCESS = {
    "official-public-extract", "official-metadata-only", "secondary-source-only", "source-unavailable",
}
EXTRACTION_STATES = {
    "not-started", "in-progress", "partial", "complete", "blocked-access",
    "supporting-only", "context-only", "excluded", "superseded-version",
}
POSTURES = {
    "mandatory-normative", "recommended-practice", "permitted-optional", "definitional",
    "informative-guidance", "implementation-example", "conformity-evidence-expectation",
}
EXPECTATION_TYPES = {
    "positive-duty", "prohibition", "permission", "definition", "guidance",
    "implementation-example", "conformity-criterion", "right-or-protection",
}
REVIEW_PRIORITIES = {
    "critical-governance-source", "high-value-governance-source",
    "supporting-specialist-source", "low-immediate-priority",
}
INTERPRETATION_STATES = {
    "authoritative-direct", "reviewed-analytical-summary",
    "provisional-interpretation", "needs-specialist-review",
}
NORMATIVE_FORCE = {
    "binding-law", "regulatory-requirement", "contractual-or-incorporated-standard",
    "voluntary-consensus-standard", "voluntary-technical-specification", "informative-technical-report",
    "government-voluntary-framework", "industry-framework",
}
ALIGNMENT_RELATIONSHIP = {"compliance", "conformance", "alignment", "reference-only"}
LIFECYCLE_STAGES = {
    "governance", "design", "development", "data-acquisition", "training",
    "testing-evaluation", "conformity-assessment", "placing-on-market", "deployment",
    "operation-use", "monitoring", "incident-response", "change-management", "retirement",
    "supply-chain", "cross-lifecycle", "not-specified",
}
GOVERNANCE_CONCEPTS = {
    "accountability", "ai-literacy", "assurance", "change-management", "conformity",
    "data-governance", "documentation", "environmental-impact", "fairness-bias", "human-oversight",
    "impact-assessment", "incident-governance", "inventory", "lifecycle-governance", "monitoring",
    "privacy", "provenance", "risk-management", "robustness", "safety", "security", "supply-chain",
    "testing-evaluation", "traceability", "transparency", "worker-affected-person-rights",
}
REQ_ID_RE = re.compile(r"^EXTREQ-[A-F0-9]{16}$")
IDENTITY_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PROVENANCE_BASES = {
    "direct-primary-text", "licensed-primary-text", "official-public-extract",
    "official-metadata-only", "secondary-source",
}

REQUIRED_REQUIREMENT_FIELDS = {
    "requirement_id", "identity_key", "vigil_source_id", "external_source_id", "source_version",
    "canonical_source_identifier", "issuer", "jurisdiction", "source_class", "source_lifecycle_state",
    "source_role", "authoritative_locator", "clause_or_control", "parent_section_or_group",
    "source_access_status", "source_review_date", "source_access_notes", "requirement_summary",
    "requirement_posture", "expectation_type", "normative_force", "alignment_relationship",
    "applicable_actor", "governed_object", "lifecycle_stage", "governance_expectation",
    "evidence_expectation", "timing_or_frequency", "required_artefacts", "verification_method",
    "applicability_conditions", "exceptions_or_qualifications", "governance_concepts",
    "source_defined_tags", "related_external_requirements", "interpretation_status",
    "interpretation_provenance", "assurance_provenance", "review_limitations",
}
REQUIRED_SCOPE_FIELDS = {
    "vigil_source_id", "external_source_id", "source_version", "canonical_source_identifier",
    "source_role", "source_access_status", "access_checked_at", "access_locator", "source_access_notes",
    "extraction_status", "extraction_scope_notes", "inaccessible_sections", "known_unreviewed_sections",
    "next_action", "review_priority", "review_priority_rationale", "maintainer_action_required",
    "maintainer_action",
}
FORBIDDEN_INTERNAL_FIELDS = {
    "cam_applicability", "cam_coverage", "cam_" + "conformance", "cam_instrument_refs",
    "caelestis_coverage", "caelestis_conformance", "caelestis_crosswalk_refs",
    "internal_alignment_status", "patch_requirement", "corpus_gap",
}


def generated(upstream: list[str]) -> dict[str, Any]:
    return {**GENERATED_BASE, "upstream_provenance": upstream}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def json_text(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


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
    registry_by_key: dict[tuple[str, str], dict[str, Any]],
    scope_entries: list[dict[str, Any]],
    errors: list[str],
) -> dict[tuple[str, str], dict[str, Any]]:
    scope_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for entry in scope_entries:
        key = source_key(entry)
        missing = sorted(REQUIRED_SCOPE_FIELDS - set(entry))
        unexpected = sorted(set(entry) - REQUIRED_SCOPE_FIELDS)
        if missing:
            errors.append(f"source-scope {key} missing required fields {missing}")
        if unexpected:
            errors.append(f"source-scope {key} contains unsupported fields {unexpected}")
        if key in scope_by_key:
            errors.append(f"duplicate source-scope key {key}")
            continue
        scope_by_key[key] = entry
        source = registry_by_key.get(key)
        if source is None:
            errors.append(f"source-scope {key} does not resolve to source registry")
            continue
        if entry.get("external_source_id") != source.get("external_source_id"):
            errors.append(f"source-scope {key} external_source_id differs from source registry")
        if entry.get("canonical_source_identifier") != source.get("canonical_identifier"):
            errors.append(f"source-scope {key} canonical identifier differs from source registry")
        role = entry.get("source_role")
        access = entry.get("source_access_status")
        extraction = entry.get("extraction_status")
        if role not in SOURCE_ROLES:
            errors.append(f"source-scope {key} invalid source_role {role!r}")
        if access not in ACCESS_STATES:
            errors.append(f"source-scope {key} invalid source_access_status {access!r}")
        if extraction not in EXTRACTION_STATES:
            errors.append(f"source-scope {key} invalid extraction_status {extraction!r}")
        if entry.get("review_priority") not in REVIEW_PRIORITIES:
            errors.append(f"source-scope {key} invalid review_priority")
        if not non_empty(entry.get("review_priority_rationale")):
            errors.append(f"source-scope {key} review_priority_rationale must be non-empty")
        for field in ("access_checked_at", "access_locator", "source_access_notes", "extraction_scope_notes", "next_action"):
            if not non_empty(entry.get(field)):
                errors.append(f"source-scope {key} requires non-empty {field}")
        if not isinstance(entry.get("access_checked_at"), str) or not DATE_RE.fullmatch(entry["access_checked_at"]):
            errors.append(f"source-scope {key} access_checked_at must use YYYY-MM-DD")
        if not string_array(entry.get("inaccessible_sections", [])):
            errors.append(f"source-scope {key} inaccessible_sections must be a unique string array")
        if not string_array(entry.get("known_unreviewed_sections", [])):
            errors.append(f"source-scope {key} known_unreviewed_sections must be a unique string array")
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
    missing = sorted(set(registry_by_key) - set(scope_by_key))
    extra = sorted(set(scope_by_key) - set(registry_by_key))
    if missing:
        errors.append(f"source-scope omits {len(missing)} registered source version(s): {missing[:5]}")
    if extra:
        errors.append(f"source-scope includes {len(extra)} unknown source version(s): {extra[:5]}")
    return scope_by_key


def load_assurance(
    registry_by_key: dict[tuple[str, str], dict[str, Any]],
    requirements: list[dict[str, Any]],
    errors: list[str],
) -> dict[tuple[str, str], dict[str, Any]]:
    document = load_json(REVIEW_ASSURANCE_PATH)
    if document.get("schema_version") != "1.0":
        errors.append("source-review-assurance.json schema_version must be 1.0")
    requirement_sources = {r["requirement_id"]: source_key(r) for r in requirements}
    reviews: dict[tuple[str, str], dict[str, Any]] = {}
    assurance_ids: set[str] = set()
    for review in document.get("source_reviews", []):
        key = source_key(review)
        source = registry_by_key.get(key)
        if key in reviews:
            errors.append(f"source-review-assurance duplicate source/version {key}")
            continue
        if source is None:
            errors.append(f"source-review-assurance references absent source {key}")
            continue
        if review.get("external_source_id") != source.get("external_source_id"):
            errors.append(f"source-review-assurance external source mismatch {key}")
        if review.get("source_metadata_fingerprint") != source.get("source_metadata_fingerprint"):
            errors.append(f"source-review-assurance metadata fingerprint mismatch {key}")
        digest = review.get("reviewed_source_digest")
        if digest is not None:
            value = digest.get("digest") if isinstance(digest, dict) else None
            if not isinstance(digest, dict) or digest.get("algorithm") != "sha256" or not isinstance(value, str) or not re.fullmatch(r"[a-f0-9]{64}", value):
                errors.append(f"source-review-assurance invalid reviewed source digest {key}")
        for assurance in review.get("assurance_provenance", []):
            aid = assurance.get("assurance_id")
            if aid in assurance_ids:
                errors.append(f"duplicate assurance_id {aid}")
            assurance_ids.add(aid)
            if assurance.get("human_role") not in {"reviewer", "verifier"}:
                errors.append(f"invalid human assurance role {aid}")
            target = assurance.get("target_scope")
            ids = assurance.get("target_requirement_ids", [])
            if target == "source-version" and ids:
                errors.append(f"{aid}: source-version assurance cannot enumerate requirements")
            elif target == "explicit-requirements":
                if not ids:
                    errors.append(f"{aid}: explicit assurance requires requirement IDs")
                for rid in ids:
                    if requirement_sources.get(rid) != key:
                        errors.append(f"{aid}: assurance target absent or belongs to another source")
            elif target not in {"source-version", "explicit-requirements"}:
                errors.append(f"{aid}: invalid assurance target_scope")
        reviews[key] = review
    return reviews


def expected_assurance(review: dict[str, Any] | None, requirement_id_value: str) -> list[dict[str, Any]]:
    if not review:
        return []
    digest = review.get("reviewed_source_digest")
    result = []
    for item in review.get("assurance_provenance", []):
        applies = item.get("target_scope") == "source-version" or requirement_id_value in item.get("target_requirement_ids", [])
        if not applies:
            continue
        value = json.loads(json.dumps(item))
        value.pop("target_scope", None)
        value.pop("target_requirement_ids", None)
        value["reviewed_source_digest"] = digest["digest"] if digest else None
        result.append(value)
    return result


def validate_requirements(
    requirements: list[dict[str, Any]],
    registry_by_key: dict[tuple[str, str], dict[str, Any]],
    scope_by_key: dict[tuple[str, str], dict[str, Any]],
    reviews: dict[tuple[str, str], dict[str, Any]],
    errors: list[str],
) -> None:
    ids: set[str] = set()
    counts: Counter[tuple[str, str]] = Counter()
    expected_provenance_fields = {
        "basis", "content_origin", "generated_by", "generation_mode", "human_role", "human_authorship",
        "human_review_status", "human_verification_status", "source_analysis_method", "source_locator",
        "source_metadata_fingerprint", "reviewed_source_digest", "reviewed_source_digest_algorithm",
        "reviewed_source_digest_status",
    }
    for index, req in enumerate(requirements):
        label = req.get("requirement_id") or f"requirements[{index}]"
        missing = sorted(REQUIRED_REQUIREMENT_FIELDS - set(req))
        if missing:
            errors.append(f"{label}: missing required fields {missing}")
            continue
        forbidden = sorted(FORBIDDEN_INTERNAL_FIELDS & set(req))
        if forbidden:
            errors.append(f"{label}: contains forbidden CAM-assessment fields {forbidden}")
        unexpected = sorted(set(req) - REQUIRED_REQUIREMENT_FIELDS)
        if unexpected:
            errors.append(f"{label}: contains unsupported fields {unexpected}")
        rid = req["requirement_id"]
        if not isinstance(rid, str) or not REQ_ID_RE.fullmatch(rid):
            errors.append(f"{label}: invalid requirement_id")
        if rid in ids:
            errors.append(f"duplicate requirement_id {rid}")
        ids.add(rid)
        ikey = req.get("identity_key")
        if not isinstance(ikey, str) or not IDENTITY_RE.fullmatch(ikey):
            errors.append(f"{label}: invalid identity_key")
        expected_id = requirement_id(str(req.get("vigil_source_id")), str(req.get("source_version")), str(req.get("clause_or_control")), str(ikey))
        if rid != expected_id:
            errors.append(f"{label}: identifier is not deterministic; expected {expected_id}")
        key = source_key(req)
        counts[key] += 1
        source = registry_by_key.get(key)
        scope = scope_by_key.get(key)
        if source is None or scope is None:
            errors.append(f"{label}: references unknown source/version {key}")
            continue
        metadata_pairs = {
            "external_source_id": source.get("external_source_id"),
            "canonical_source_identifier": source.get("canonical_identifier"),
            "issuer": source.get("issuer"),
            "jurisdiction": source.get("jurisdiction"),
            "source_class": source.get("source_class"),
            "source_lifecycle_state": source.get("source_lifecycle_state"),
            "authoritative_locator": source.get("official_locator"),
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
        if not isinstance(req.get("source_review_date"), str) or not DATE_RE.fullmatch(req["source_review_date"]):
            errors.append(f"{label}: source_review_date must use YYYY-MM-DD")
        if req.get("requirement_posture") not in POSTURES:
            errors.append(f"{label}: invalid requirement_posture")
        if req.get("expectation_type") not in EXPECTATION_TYPES:
            errors.append(f"{label}: invalid expectation_type")
        if req.get("normative_force") not in NORMATIVE_FORCE:
            errors.append(f"{label}: invalid normative_force")
        if req.get("alignment_relationship") not in ALIGNMENT_RELATIONSHIP:
            errors.append(f"{label}: invalid alignment_relationship")
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
        for field in (
            "evidence_expectation", "timing_or_frequency", "required_artefacts", "verification_method",
            "applicability_conditions", "exceptions_or_qualifications", "related_external_requirements",
            "review_limitations",
        ):
            if not string_array(req.get(field)):
                errors.append(f"{label}: {field} must be a unique string array")
        tags = req.get("source_defined_tags")
        if not isinstance(tags, list):
            errors.append(f"{label}: source_defined_tags must be an array")
        else:
            schemes = set()
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
        provenance = req.get("interpretation_provenance")
        if not isinstance(provenance, dict) or set(provenance) != expected_provenance_fields:
            errors.append(f"{label}: interpretation_provenance has missing or unexpected fields")
        else:
            expected_default = {
                "content_origin": "ai-authored", "generated_by": "ai", "generation_mode": "semi-autonomous",
                "human_role": "contract-approver", "human_authorship": False,
                "human_review_status": "not-reviewed", "human_verification_status": "not-verified",
            }
            for field, expected in expected_default.items():
                if provenance.get(field) != expected:
                    errors.append(f"{label}: interpretation_provenance.{field} must be {expected!r}")
            if provenance.get("basis") not in PROVENANCE_BASES:
                errors.append(f"{label}: invalid interpretation_provenance.basis")
            if provenance.get("source_metadata_fingerprint") != source.get("source_metadata_fingerprint"):
                errors.append(f"{label}: source metadata fingerprint differs from source registry")
            review = reviews.get(key)
            digest = (review or {}).get("reviewed_source_digest")
            expected_status = "recorded" if digest else "not-recorded"
            if provenance.get("reviewed_source_digest_status") != expected_status:
                errors.append(f"{label}: reviewed source digest status differs from assurance sidecar")
            if digest:
                if provenance.get("reviewed_source_digest") != digest.get("digest") or provenance.get("reviewed_source_digest_algorithm") != "sha256":
                    errors.append(f"{label}: reviewed source digest differs from assurance sidecar")
            elif provenance.get("reviewed_source_digest") is not None or provenance.get("reviewed_source_digest_algorithm") is not None:
                errors.append(f"{label}: unrecorded reviewed source digest must remain null")
            expected_basis = {
                "direct-public-primary": "direct-primary-text",
                "direct-licensed-primary": "licensed-primary-text",
                "official-public-extract": "official-public-extract",
                "official-metadata-only": "official-metadata-only",
                "secondary-source-only": "secondary-source",
            }.get(req.get("source_access_status"))
            if expected_basis and provenance.get("basis") != expected_basis:
                errors.append(f"{label}: provenance basis conflicts with source access")
        if req.get("assurance_provenance") != expected_assurance(reviews.get(key), rid):
            errors.append(f"{label}: assurance_provenance differs from source-review-assurance sidecar")
        access = req.get("source_access_status")
        status = req.get("interpretation_status")
        if status == "authoritative-direct" and access not in {"direct-public-primary", "direct-licensed-primary"}:
            errors.append(f"{label}: authoritative-direct claim conflicts with access {access}")
        if access == "official-public-extract" and status in {"authoritative-direct", "reviewed-analytical-summary"}:
            errors.append(f"{label}: public-extract access requires a provisional or specialist interpretation state")
        if status in {"authoritative-direct", "reviewed-analytical-summary"} and access in {"official-metadata-only", "secondary-source-only", "source-unavailable"}:
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
        if role == "primary-ai-governance" and count == 0 and status not in {"not-started", "in-progress", "blocked-access", "superseded-version"}:
            errors.append(f"primary source {key} is omitted without explicit incomplete/access state")
        if status in {"supporting-only", "context-only", "excluded", "blocked-access", "superseded-version"} and count:
            errors.append(f"source-scope {key} status {status} conflicts with {count} requirement record(s)")


def coverage_manifest(scope: dict[str, Any], reqs: list[dict[str, Any]], review: dict[str, Any] | None) -> dict[str, Any]:
    status = scope["extraction_status"]
    state = {
        "complete": "bounded-complete", "partial": "partial", "in-progress": "partial",
        "not-started": "not-started", "blocked-access": "blocked", "supporting-only": "supporting-only",
        "context-only": "context-only", "excluded": "excluded", "superseded-version": "superseded",
    }[status]
    direct = scope["source_access_status"] in {"direct-public-primary", "direct-licensed-primary"}
    digest = (review or {}).get("reviewed_source_digest")
    return {
        "vigil_source_id": scope["vigil_source_id"],
        "external_source_id": scope["external_source_id"],
        "source_version": scope["source_version"],
        "coverage_state": state,
        "source_access_status": scope["source_access_status"],
        "source_retrieval_state": "retrieved" if direct and reqs else ("not-established" if direct else "not-retrieved"),
        "analysis_state": status,
        "reviewed_sections": [],
        "reviewed_sections_status": "not-enumerated",
        "represented_requirement_count": len(reqs),
        "represented_clause_or_control_count": len({r["clause_or_control"] for r in reqs}),
        "expected_requirement_population": None,
        "known_unreviewed_sections": scope["known_unreviewed_sections"],
        "inaccessible_sections": scope["inaccessible_sections"],
        "completeness_criterion": scope["extraction_scope_notes"],
        "completeness_claim": (
            "Bounded-complete means governance-significant material identified by the recorded criterion is represented; it is not exhaustive atomisation."
            if status == "complete" else "No bounded-complete claim is made."
        ),
        "informative_material_treatment": "Informative material is atomised only when it has independent governance meaning.",
        "reviewed_source_digest_status": "recorded" if digest else ("not-recorded" if direct and reqs else "not-applicable"),
        "reviewed_source_digests": [digest["digest"]] if digest else [],
        "human_assurance_count": len((review or {}).get("assurance_provenance", [])),
        "assurance_limitations": [] if digest or not (direct and reqs) else ["Exact reviewed source artefact digest was not recorded for this historical extraction."],
    }


def validate_crosswalks(document: dict[str, Any], errors: list[str]) -> list[dict[str, Any]]:
    crosswalks = document.get("crosswalks", [])
    seen = set()
    for item in crosswalks:
        xid = item.get("crosswalk_id")
        if xid in seen:
            errors.append(f"duplicate crosswalk {xid}")
        seen.add(xid)
        if item.get("derivative_not_source_authority") is not True:
            errors.append(f"{xid}: derivative source-authority boundary is invalid")
        if item.get("may_assert_target_requirement_text_from_crosswalk") is not False:
            errors.append(f"{xid}: crosswalk cannot assert unseen target requirement text")
        if item.get("may_assert_conformance") is not False:
            errors.append(f"{xid}: crosswalk cannot assert conformance")
        if item.get("completeness", {}).get("ingested_row_count") != len(item.get("mappings", [])):
            errors.append(f"{xid}: crosswalk row count mismatch")
    return sorted(crosswalks, key=lambda x: x["crosswalk_id"])


def build_outputs(
    registry_by_key: dict[tuple[str, str], dict[str, Any]],
    scopes: list[dict[str, Any]],
    requirements: list[dict[str, Any]],
    reviews: dict[tuple[str, str], dict[str, Any]],
    crosswalks: list[dict[str, Any]],
    reviewed_at: str,
) -> dict[Path, str]:
    upstream = [
        "vigil/external_sources/source-registry.json", "vigil/external_requirements/source-scope.json",
        "vigil/external_requirements/requirements.json", "vigil/external_requirements/source-review-assurance.json",
    ]
    sorted_requirements = sorted(requirements, key=lambda x: x["requirement_id"])
    by_source: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for req in sorted_requirements:
        by_source[source_key(req)].append(req)
    index = {
        "schema_version": "1.2",
        "generated_from": "requirements.json",
        "generated_at": reviewed_at,
        "authorship_provenance": generated(upstream),
        "requirement_count": len(sorted_requirements),
        "requirements": [
            {
                "requirement_id": r["requirement_id"], "vigil_source_id": r["vigil_source_id"],
                "external_source_id": r["external_source_id"], "source_version": r["source_version"],
                "clause_or_control": r["clause_or_control"], "requirement_summary": r["requirement_summary"],
                "requirement_posture": r["requirement_posture"], "expectation_type": r["expectation_type"],
                "normative_force": r["normative_force"], "alignment_relationship": r["alignment_relationship"],
                "applicable_actor": r["applicable_actor"], "governance_concepts": r["governance_concepts"],
                "interpretation_status": r["interpretation_status"],
            }
            for r in sorted_requirements
        ],
    }
    source_rows = []
    for scope in sorted(scopes, key=lambda x: (x["external_source_id"], x["source_version"])):
        key = source_key(scope)
        source = registry_by_key[key]
        items = by_source[key]
        source_rows.append({
            "vigil_source_id": scope["vigil_source_id"], "external_source_id": scope["external_source_id"],
            "title": source.get("title"), "source_version": scope["source_version"],
            "source_role": scope["source_role"], "source_access_status": scope["source_access_status"],
            "source_access_notes": scope["source_access_notes"], "extraction_status": scope["extraction_status"],
            "extraction_scope_notes": scope["extraction_scope_notes"], "requirement_count": len(items),
            "reviewed_requirement_count": sum(i["interpretation_status"] in {"authoritative-direct", "reviewed-analytical-summary"} for i in items),
            "unresolved_interpretation_count": sum(i["interpretation_status"] in {"provisional-interpretation", "needs-specialist-review"} for i in items),
            "inaccessible_sections": scope["inaccessible_sections"], "known_unreviewed_sections": scope["known_unreviewed_sections"],
            "next_action": scope["next_action"], "review_priority": scope["review_priority"],
            "review_priority_rationale": scope["review_priority_rationale"],
            "maintainer_action_required": scope["maintainer_action_required"], "maintainer_action": scope["maintainer_action"],
        })
    completeness = {
        "schema_version": "1.2", "generated_at": reviewed_at, "authorship_provenance": generated(upstream),
        "source_version_count": len(source_rows),
        "primary_source_version_count": sum(r["source_role"] == "primary-ai-governance" for r in source_rows),
        "requirement_count": len(sorted_requirements), "sources": source_rows,
    }
    manifests = [coverage_manifest(scope, by_source[source_key(scope)], reviews.get(source_key(scope))) for scope in sorted(scopes, key=lambda x: (x["external_source_id"], x["source_version"]))]
    coverage = {
        "schema_version": "1.0", "generated_at": reviewed_at, "authorship_provenance": generated(upstream),
        "source_version_count": len(manifests), "manifests": manifests,
    }
    catalogue = [
        "# External AI-Governance Requirements", "",
        "Canonical analytical catalogue derived from registered external governance sources. Inclusion does not establish CAM applicability, adoption, coverage, compliance, conformance or alignment.", "",
        f"- Registered source versions: {len(source_rows)}",
        f"- Primary AI-governance source versions: {sum(r['source_role'] == 'primary-ai-governance' for r in source_rows)}",
        f"- Requirement records: {len(sorted_requirements)}", "",
    ]
    scope_map = {source_key(s): s for s in scopes}
    for row in source_rows:
        key = (row["vigil_source_id"], row["source_version"])
        catalogue += [
            f"## {row['title']} — {row['source_version']}", "",
            f"- Source: `{row['vigil_source_id']}` / `{row['external_source_id']}`",
            f"- Role: `{row['source_role']}`",
            f"- Access: `{row['source_access_status']}`",
            f"- Extraction: `{row['extraction_status']}`",
            f"- Requirements: {row['requirement_count']}",
            f"- Review priority: `{row['review_priority']}`",
            f"- Next action: {row['next_action']}", "",
        ]
        items = by_source[key]
        if items:
            catalogue += [
                "| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |",
                "| --- | --- | --- | --- | --- | --- | --- |",
            ]
            for r in items:
                safe_summary = r["requirement_summary"].replace("|", "\\|")
                safe_clause = r["clause_or_control"].replace("|", "\\|")
                catalogue.append(
                    f"| `{r['requirement_id']}` | {safe_clause} | {safe_summary} | `{r['requirement_posture']}` / `{r['expectation_type']}` | "
                    f"`{r['normative_force']}` | `{r['alignment_relationship']}` | `{r['interpretation_status']}` / `{r['source_access_status']}` |"
                )
            catalogue.append("")
        else:
            catalogue += [f"No requirement records are asserted. {scope_map[key]['extraction_scope_notes']}", ""]
    limited = [r for r in source_rows if r["maintainer_action_required"] or r["source_access_status"] in INSUFFICIENT_FULL_REVIEW_ACCESS]
    access_lines = [
        "# Source Access Limitations and Maintainer Access List", "",
        "Sources listed here are not represented as fully reviewed. Metadata, abstracts, previews and secondary summaries are not substitutes for authoritative normative text.", "",
        "| Source | Version | Role | Access | Extraction | Inaccessible material | Maintainer action |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in limited:
        inaccessible = "; ".join(row["inaccessible_sections"]) or "Full or sufficient source text"
        action = row["maintainer_action"] or "No action currently required"
        access_lines.append(f"| {row['title']} | `{row['source_version']}` | `{row['source_role']}` | `{row['source_access_status']}` | `{row['extraction_status']}` | {inaccessible.replace('|', chr(92) + '|')} | {action.replace('|', chr(92) + '|')} |")
    access_lines.append("")
    blocked = [r for r in source_rows if r["source_role"] == "primary-ai-governance" and r["extraction_status"] == "blocked-access"]
    priority_order = {"critical-governance-source": 0, "high-value-governance-source": 1, "supporting-specialist-source": 2, "low-immediate-priority": 3}
    priority_lines = [
        "# Blocked Primary-Source Priorities", "",
        "This is an access-planning projection. Priority does not imply that inaccessible normative requirements were reviewed.", "",
        "| Priority | Source | Version | Governance value | Access limitation | Next action |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in sorted(blocked, key=lambda x: (priority_order[x["review_priority"]], x["title"], x["source_version"])):
        priority_lines.append(f"| `{row['review_priority']}` | {row['title']} | `{row['source_version']}` | {row['review_priority_rationale'].replace('|', chr(92) + '|')} | {row['source_access_status']} | {row['next_action'].replace('|', chr(92) + '|')} |")
    priority_lines.append("")
    crosswalk_upstream = ["vigil/external_requirements/derivative-crosswalks.json"]
    xindex = {
        "schema_version": "1.0", "generated_at": reviewed_at, "authorship_provenance": generated(crosswalk_upstream),
        "crosswalk_count": len(crosswalks), "mapping_row_count": sum(len(x.get("mappings", [])) for x in crosswalks),
        "crosswalks": [
            {
                "crosswalk_id": x["crosswalk_id"], "mapping_name": x["mapping_name"], "mapping_version": x["mapping_version"],
                "mapping_status": x["mapping_status"], "relationship_type": x["relationship_type"],
                "reference_document": x["reference_document"], "focal_document": x["focal_document"],
                "mapping_locator": x["mapping_locator"], "ingested_row_count": len(x.get("mappings", [])),
                "row_ingestion_status": x["completeness"]["row_ingestion_status"], "may_assert_conformance": False,
            }
            for x in crosswalks
        ],
    }
    xview = [
        "# Derivative External-Governance Crosswalks", "",
        "Crosswalks record published or developer-asserted relationships. They do not supply unseen target normative text, determine CAM applicability, or establish conformance.", "",
        f"- Crosswalk records: {len(crosswalks)}",
        f"- Ingested mapping rows: {sum(len(x.get('mappings', [])) for x in crosswalks)}", "",
    ]
    for x in crosswalks:
        xview += [
            f"## {x['mapping_name']}", "", f"- ID: `{x['crosswalk_id']}`",
            f"- Version/status: `{x['mapping_version']}` / `{x['mapping_status']}`",
            f"- Relationship: `{x['relationship_type']}`", f"- Rows represented: {len(x.get('mappings', []))}",
            "- Conformance assertion permitted: `false`", "",
        ]
    return {
        INDEX_PATH: json_text(index), COMPLETENESS_PATH: json_text(completeness), COVERAGE_PATH: json_text(coverage),
        CATALOGUE_PATH: "\n".join(catalogue).rstrip() + "\n",
        ACCESS_PATH: "\n".join(access_lines).rstrip() + "\n",
        PRIORITY_PATH: "\n".join(priority_lines).rstrip() + "\n",
        CROSSWALK_INDEX_PATH: json_text(xindex), CROSSWALK_VIEW_PATH: "\n".join(xview).rstrip() + "\n",
    }


def load_and_validate() -> tuple[dict[Path, str], list[str]]:
    errors: list[str] = []
    registry = load_json(REGISTRY_PATH)
    scope_doc = load_json(SCOPE_PATH)
    req_doc = load_json(REQUIREMENTS_PATH)
    crosswalk_doc = load_json(CROSSWALKS_PATH)
    if registry.get("schema_version") != "1.0":
        errors.append("source-registry schema_version must be 1.0")
    if scope_doc.get("schema_version") != "1.2":
        errors.append("source-scope schema_version must be 1.2")
    if req_doc.get("schema_version") != "1.2":
        errors.append("requirements schema_version must be 1.2")
    reviewed_at = scope_doc.get("reviewed_at")
    if not isinstance(reviewed_at, str) or not DATE_RE.fullmatch(reviewed_at):
        errors.append("source-scope reviewed_at must use YYYY-MM-DD")
        reviewed_at = ""
    registry_entries = registry.get("entries", [])
    scopes = scope_doc.get("entries", [])
    requirements = req_doc.get("requirements", [])
    if not isinstance(registry_entries, list) or not isinstance(scopes, list) or not isinstance(requirements, list):
        raise ValueError("source registry, source scope and requirements collections must be arrays")
    registry_by_key = {source_key(item): item for item in registry_entries}
    if len(registry_by_key) != len(registry_entries):
        errors.append("source registry contains duplicate source/version keys")
    scope_by_key = validate_scope(registry_by_key, scopes, errors)
    reviews = load_assurance(registry_by_key, requirements, errors)
    validate_requirements(requirements, registry_by_key, scope_by_key, reviews, errors)
    crosswalks = validate_crosswalks(crosswalk_doc, errors)
    outputs = build_outputs(registry_by_key, scopes, requirements, reviews, crosswalks, reviewed_at)
    return outputs, errors


def build() -> None:
    outputs, errors = load_and_validate()
    if errors:
        raise ValueError("\n".join(errors))
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path}")


def validate(check_generated: bool = False) -> None:
    outputs, errors = load_and_validate()
    if check_generated:
        for path, expected in outputs.items():
            actual = path.read_text(encoding="utf-8") if path.exists() else ""
            if actual != expected:
                errors.append(f"generated output is stale: {path}")
    if errors:
        raise ValueError("\n".join(errors))
    requirements = load_json(REQUIREMENTS_PATH)["requirements"]
    sources = load_json(REGISTRY_PATH)["entries"]
    print(f"External requirements valid: {len(sources)} source versions, {len(requirements)} requirements")


def main() -> None:
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(dest="command", required=True)
    subs.add_parser("build")
    validate_parser = subs.add_parser("validate")
    validate_parser.add_argument("--check-generated", action="store_true")
    args = parser.parse_args()
    if args.command == "build":
        build()
    else:
        validate(args.check_generated)


if __name__ == "__main__":
    main()
