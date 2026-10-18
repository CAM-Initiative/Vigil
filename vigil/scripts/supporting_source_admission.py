"""Structural traceability for reviewed supporting-authority extraction.

These checks resolve retained substantive decisions. They cannot establish the
truth of an external proposition, material class fit, or occurrence alignment.
Existing primary-source requirements are outside this additive admission gate.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

METADATA_FIELDS = (
    "applicable_actor", "governed_object", "timing_or_frequency", "required_artefacts",
    "evidence_expectation", "verification_method", "applicability_conditions",
    "exceptions_or_qualifications",
)
CLASS_FIELDS = (
    "class_id", "definition", "invariant", "failure_condition",
    "failure_recognition", "success_condition", "success_recognition", "exclusions",
)


def digest(value: dict) -> str:
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, ensure_ascii=False, separators=(",", ":"),
    ).encode("utf-8")).hexdigest()


def class_digest(value: dict) -> str:
    return digest({field: value.get(field) for field in CLASS_FIELDS})


def source_key(value: dict) -> tuple[str, str]:
    return value.get("vigil_source_id", ""), value.get("source_version", "")


def fidelity_errors(requirements: list[dict], scopes: dict, entries: list[dict]) -> list[str]:
    errors = []
    by_source = {source_key(entry): entry for entry in entries}
    for req in requirements:
        if req.get("source_role") != "supporting-external-authority":
            continue
        rid = req.get("requirement_id")
        review = by_source.get(source_key(req), {})
        if review.get("fidelity_status") not in {"assured", "provisional"}:
            errors.append(f"{rid}: extracted supporting source requires a substantive fidelity review")
        if rid not in review.get("audited_requirement_ids", []):
            errors.append(f"{rid}: supporting fidelity review must include this requirement")
        scope = scopes.get(source_key(req), {})
        if scope.get("extraction_status") == "complete" and review.get("fidelity_status") != "assured":
            errors.append(f"{rid}: complete supporting extraction requires assured bounded fidelity")
    return errors


def admission_errors(requirements: list[dict], scopes: dict, fidelity: list[dict],
                     metadata: list[dict], relationships: list[dict], classes: dict,
                     repository_root: Path) -> list[str]:
    errors = fidelity_errors(requirements, scopes, fidelity)
    metadata_by_id = {entry.get("requirement_id"): entry for entry in metadata}
    root = repository_root.resolve()
    for req in requirements:
        if req.get("source_role") != "supporting-external-authority":
            continue
        rid = req.get("requirement_id")
        scope = scopes.get(source_key(req), {})
        if scope.get("extraction_status") not in {"in-progress", "partial", "complete"}:
            errors.append(f"{rid}: supporting requirements need an explicit bounded extraction state")
        if req.get("source_access_status") not in {
            "direct-public-primary", "direct-licensed-primary", "official-public-extract",
        }:
            errors.append(f"{rid}: supporting admission requires access to the actual provision")
        if req.get("requirement_posture") not in {
            "mandatory-normative", "recommended-practice", "permitted-optional",
            "conformity-evidence-expectation",
        } or req.get("alignment_relationship") == "reference-only":
            errors.append(f"{rid}: commentary, definitions and examples are reference-only, not supporting normative admission")
        review = metadata_by_id.get(rid, {})
        states = review.get("field_status", {})
        if review.get("review_basis") not in {
            "direct-primary-text", "licensed-primary-text", "official-public-extract",
        } or not review.get("reviewed_at"):
            errors.append(f"{rid}: supporting admission needs dated primary-text metadata review")
        for field in METADATA_FIELDS:
            expected = "populated-reviewed" if req.get(field) else "not-specified-by-source"
            if states.get(field) not in ({expected} if req.get(field) else {expected, "not-applicable"}):
                errors.append(f"{rid}: supporting metadata dimension {field} lacks a compatible reviewed disposition")
        retained = False
        for relation in relationships:
            if relation.get("requirement_id") != rid or relation.get("review_status") != "supported" or relation.get("strength") not in {"direct", "strong-supporting"}:
                continue
            cls = classes.get(relation.get("class_id"))
            if not cls or relation.get("requirement_sha256") != digest(req) or relation.get("class_semantic_sha256") != class_digest(cls):
                continue
            if any(relation.get(field) != req.get(field) for field in (
                "vigil_source_id", "external_source_id", "source_version", "clause_or_control",
            )):
                continue
            if relation.get("invariant") != cls.get("invariant") or not relation.get("supported_component") or not relation.get("scope_correspondence") or not relation.get("limitation"):
                continue
            ref = relation.get("review_artifact")
            if not isinstance(ref, str) or Path(ref).is_absolute():
                continue
            path = (root / ref).resolve()
            if not path.is_relative_to(root):
                continue
            try:
                artifact = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            identity = artifact.get("source_identity", {})
            if identity.get("external_source_id") != req.get("external_source_id") or identity.get("source_version") != req.get("source_version"):
                continue
            if not artifact.get("reviewed_on") or not artifact.get("review_basis"):
                continue
            # Resolve the exact retained decision, not a rationale-only assertion.
            for entry in artifact.get("entries", []):
                if entry.get("requirement_id") == rid and entry.get("requirement_sha256") == digest(req) and relation in entry.get("relationships", []):
                    retained = True
        if not retained:
            errors.append(f"{rid}: supporting admission needs a resolving reviewed direct/strong-supporting invariant relationship")
    return errors
