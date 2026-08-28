#!/usr/bin/env python3
"""Validate VIGIL CAM applicability and coverage assessments."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

from external_requirements_io import load_requirements_document

ROOT = Path(__file__).resolve().parents[1]
CAM_ASSESSMENT = ROOT / "cam_assessment"
ASSESSMENTS = CAM_ASSESSMENT / "assessments.json"
PROVENANCE_REF = "vigil/provenance/AUTHORSHIP-PROVENANCE.json"

FORCE = {
    "binding-law",
    "regulatory-requirement",
    "contractual-or-incorporated-standard",
    "voluntary-consensus-standard",
    "voluntary-technical-specification",
    "informative-technical-report",
    "government-voluntary-framework",
    "industry-framework",
}
RELATIONSHIP = {"compliance", "conformance", "alignment", "reference-only"}
APPLICABILITY = {"applicable", "conditionally-applicable", "reference-only", "not-applicable", "unresolved"}
COVERAGE = {"full", "partial", "absent", "conflicting", "indeterminate", "not-applicable"}
ROUTING = {"none", "needs-review", "ready-for-routing", "routed"}
REVIEW = {"not-reviewed", "spot-checked", "substantively-reviewed", "line-by-line-reviewed"}
VERIFY = {"not-verified", "sample-verified", "source-verified", "fully-verified"}
DEFAULT_PROVENANCE = {
    "content_origin": "ai-authored",
    "generation_mode": "semi-autonomous",
    "human_role": "contract-approver",
    "human_authorship": False,
    "human_review_status": "not-reviewed",
    "human_verification_status": "not-verified",
    "declaration": PROVENANCE_REF,
}

def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value

def assessment_id(extreq_id: str, cam_corpus_commit: str) -> str:
    payload = f"CAMALIGN|{extreq_id}|{cam_corpus_commit}".encode("utf-8")
    return "CAMALIGN-" + hashlib.sha256(payload).hexdigest()[:16].upper()

def nonempty_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) and item.strip() for item in value)
        and len(value) == len(set(value))
    )

def validate_assurance(items: object, label: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(items, list):
        return [f"{label}: assurance_provenance must be an array"]
    seen: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            errors.append(f"{label}: assurance item must be an object")
            continue
        aid = item.get("assurance_id")
        if not isinstance(aid, str) or not re.fullmatch(r"ASSURE-[A-F0-9]{16}", aid):
            errors.append(f"{label}: invalid assurance_id")
        elif aid in seen:
            errors.append(f"{label}: duplicate assurance_id {aid}")
        else:
            seen.add(aid)
        if item.get("human_role") not in {"reviewer", "verifier"}:
            errors.append(f"{label}: assurance human_role must be reviewer or verifier")
        if item.get("human_review_status") not in REVIEW:
            errors.append(f"{label}: invalid assurance human_review_status")
        if item.get("human_verification_status") not in VERIFY:
            errors.append(f"{label}: invalid assurance human_verification_status")
        for field in ("performed_by", "performed_at", "scope", "method"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{label}: assurance {field} must be non-empty")
        for field in ("evidence_refs", "limitations"):
            if not nonempty_strings(item.get(field)):
                errors.append(f"{label}: assurance {field} must be a unique string array")
    return errors

def validate_assessment(item: dict[str, Any], extreq: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    label = str(item.get("assessment_id", "unknown assessment"))
    required = {
        "assessment_id", "extreq_id", "external_source_id", "source_version",
        "normative_force", "alignment_relationship", "applicability_state",
        "applicability_rationale", "coverage_state", "cam_corpus_commit",
        "cam_instrument_refs", "coverage_evidence_refs", "assessment_provenance",
        "assurance_provenance", "remediation_required", "remediation_refs",
        "vigil_routing_state", "limitations",
    }
    missing = sorted(required - set(item))
    if missing:
        errors.append(f"{label}: missing fields {missing}")
        return errors

    commit = item["cam_corpus_commit"]
    if not isinstance(commit, str) or not re.fullmatch(r"[a-f0-9]{40}", commit):
        errors.append(f"{label}: cam_corpus_commit must be a 40-character lowercase commit SHA")
    elif item["assessment_id"] != assessment_id(item["extreq_id"], commit):
        errors.append(f"{label}: assessment_id does not match EXTREQ + CAM commit identity")

    for field in ("external_source_id", "source_version", "normative_force", "alignment_relationship"):
        if item.get(field) != extreq.get(field):
            errors.append(f"{label}: {field} differs from canonical EXTREQ")
    if item["normative_force"] not in FORCE:
        errors.append(f"{label}: invalid normative_force")
    if item["alignment_relationship"] not in RELATIONSHIP:
        errors.append(f"{label}: invalid alignment_relationship")
    if item["applicability_state"] not in APPLICABILITY:
        errors.append(f"{label}: invalid applicability_state")
    if item["coverage_state"] not in COVERAGE:
        errors.append(f"{label}: invalid coverage_state")
    if item["vigil_routing_state"] not in ROUTING:
        errors.append(f"{label}: invalid vigil_routing_state")
    if not isinstance(item["applicability_rationale"], str) or not item["applicability_rationale"].strip():
        errors.append(f"{label}: applicability_rationale must be non-empty")
    for field in ("cam_instrument_refs", "coverage_evidence_refs", "remediation_refs", "limitations"):
        if not nonempty_strings(item[field]):
            errors.append(f"{label}: {field} must be a unique string array")
    if not isinstance(item["remediation_required"], bool):
        errors.append(f"{label}: remediation_required must be boolean")

    provenance = item["assessment_provenance"]
    if not isinstance(provenance, dict):
        errors.append(f"{label}: assessment_provenance must be an object")
    else:
        if provenance.get("declaration") != PROVENANCE_REF:
            errors.append(f"{label}: assessment provenance must reference {PROVENANCE_REF}")
        if provenance.get("human_role") == "contract-approver":
            if provenance.get("human_authorship") is not False:
                errors.append(f"{label}: contract approval cannot assert human authorship")
            if provenance.get("human_review_status") != "not-reviewed":
                errors.append(f"{label}: contract approval cannot assert substantive human review")
            if provenance.get("human_verification_status") != "not-verified":
                errors.append(f"{label}: contract approval cannot assert human verification")
    errors.extend(validate_assurance(item["assurance_provenance"], label))

    applicability = item["applicability_state"]
    coverage = item["coverage_state"]
    if applicability == "not-applicable":
        if coverage != "not-applicable":
            errors.append(f"{label}: not-applicable applicability requires not-applicable coverage")
        if item["remediation_required"]:
            errors.append(f"{label}: not-applicable assessment cannot require remediation")
    elif coverage == "not-applicable":
        errors.append(f"{label}: not-applicable coverage requires not-applicable applicability")
    if applicability == "unresolved" and coverage != "indeterminate":
        errors.append(f"{label}: unresolved applicability requires indeterminate coverage")
    if applicability == "reference-only" and coverage not in {"indeterminate", "not-applicable"}:
        errors.append(f"{label}: reference-only applicability cannot assert substantive CAM coverage")
    if coverage == "full":
        if not item["cam_instrument_refs"] or not item["coverage_evidence_refs"]:
            errors.append(f"{label}: full coverage requires CAM instrument references and coverage evidence")
        if applicability not in {"applicable", "conditionally-applicable"}:
            errors.append(f"{label}: full coverage requires applicable or conditionally-applicable state")
    if coverage in {"partial", "absent", "conflicting"} and not item["remediation_required"]:
        errors.append(f"{label}: material coverage gap requires remediation_required true")
    if item["remediation_required"] and item["vigil_routing_state"] == "none":
        errors.append(f"{label}: remediation-required assessment must enter VIGIL routing workflow")
    return errors

def validate_repository(
    assessments_document: dict[str, Any] | None = None,
    requirements_document: dict[str, Any] | None = None,
) -> list[str]:
    assessments_document = assessments_document or load(ASSESSMENTS)
    requirements_document = requirements_document or load_requirements_document()
    errors: list[str] = []
    if assessments_document.get("schema_version") != "1.0":
        errors.append("CAM assessments schema_version must be 1.0")
    if assessments_document.get("authorship_provenance") != DEFAULT_PROVENANCE:
        errors.append("CAM assessment dataset authorship provenance differs from VIGIL default")
    extreqs = {item["requirement_id"]: item for item in requirements_document.get("requirements", [])}
    seen: set[str] = set()
    for item in assessments_document.get("assessments", []):
        if not isinstance(item, dict):
            errors.append("CAM assessment must be an object")
            continue
        aid = item.get("assessment_id")
        if aid in seen:
            errors.append(f"duplicate CAM assessment_id {aid}")
        seen.add(aid)
        rid = item.get("extreq_id")
        extreq = extreqs.get(rid)
        if extreq is None:
            errors.append(f"{aid or 'unknown assessment'}: references absent effective EXTREQ {rid}")
            continue
        errors.extend(validate_assessment(item, extreq))
    return errors

def main() -> int:
    errors = validate_repository()
    if errors:
        print("VIGIL CAM assessment validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("VIGIL CAM assessment validation passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
