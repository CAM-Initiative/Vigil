#!/usr/bin/env python3
"""Validate VIGIL authorship, human-review, and human-verification provenance."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from external_requirements_io import load_requirements_document


ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"

VOCABULARY = {
    "content_origin": {
        "human-authored",
        "ai-authored",
        "human-ai-coauthored",
        "deterministically-generated",
    },
    "generation_mode": {
        "manual",
        "ai-assisted",
        "semi-autonomous",
        "deterministic-generation",
    },
    "human_role": {
        "none",
        "contract-approver",
        "substantive-contributor",
        "co-author",
        "reviewer",
        "verifier",
    },
    "human_review_status": {
        "not-reviewed",
        "spot-checked",
        "substantively-reviewed",
        "line-by-line-reviewed",
    },
    "human_verification_status": {
        "not-verified",
        "sample-verified",
        "source-verified",
        "fully-verified",
    },
}

DEFAULT = {
    "content_origin": "ai-authored",
    "generation_mode": "semi-autonomous",
    "human_role": "contract-approver",
    "human_authorship": False,
    "human_review_status": "not-reviewed",
    "human_verification_status": "not-verified",
}

GENERATED = {
    "content_origin": "deterministically-generated",
    "generation_mode": "deterministic-generation",
    "human_role": "contract-approver",
    "human_authorship": False,
    "human_review_status": "not-reviewed",
    "human_verification_status": "not-verified",
}

INHERITANCE_RULES = {
    "default_applies_when_override_absent": True,
    "explicit_artefact_override_precedence": True,
    "explicit_artefact_override_field": "authorship_provenance",
    "absence_of_override_means_human_review": False,
    "repository_acceptance_means_human_review": False,
    "repository_publication_means_human_review": False,
    "repository_acceptance_means_human_verification": False,
    "legacy_interpretive_provenance_is_authorship_override": False,
}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def validate_provenance(
    provenance: object,
    label: str,
    *,
    require_upstream: bool = False,
) -> list[str]:
    errors: list[str] = []
    if not isinstance(provenance, dict):
        return [f"{label}: provenance must be an object"]

    required = {*VOCABULARY, "human_authorship"}
    for field in sorted(required):
        if field not in provenance:
            errors.append(f"{label}: missing {field}")
    for field, allowed in VOCABULARY.items():
        value = provenance.get(field)
        if value not in allowed:
            errors.append(f"{label}: invalid {field} {value!r}")
    if not isinstance(provenance.get("human_authorship"), bool):
        errors.append(f"{label}: human_authorship must be boolean")

    if provenance.get("human_role") == "contract-approver":
        if provenance.get("human_authorship") is not False:
            errors.append(f"{label}: contract-approver cannot assert human authorship")
        if provenance.get("human_review_status") != "not-reviewed":
            errors.append(f"{label}: contract-approver cannot assert human review")
        if provenance.get("human_verification_status") != "not-verified":
            errors.append(f"{label}: contract-approver cannot assert human verification")

    origin = provenance.get("content_origin")
    if origin in {"human-authored", "human-ai-coauthored"} and provenance.get("human_authorship") is not True:
        errors.append(f"{label}: {origin} requires human_authorship true")
    if origin in {"ai-authored", "deterministically-generated"} and provenance.get("human_authorship") is not False:
        errors.append(f"{label}: {origin} requires human_authorship false")
    if origin == "deterministically-generated" and provenance.get("generation_mode") != "deterministic-generation":
        errors.append(f"{label}: deterministically-generated requires deterministic-generation")
    if provenance.get("generation_mode") == "deterministic-generation" and origin != "deterministically-generated":
        errors.append(f"{label}: deterministic-generation requires deterministically-generated origin")

    upstream = provenance.get("upstream_provenance")
    if require_upstream and (
        not isinstance(upstream, list)
        or not upstream
        or any(not isinstance(item, str) or not item.strip() for item in upstream)
    ):
        errors.append(f"{label}: generated artefact must identify upstream_provenance")
    return errors


def validate_repository() -> list[str]:
    errors: list[str] = []

    requirements = load_requirements_document()
    for record in requirements.get("requirements", []):
        provenance = record.get("interpretation_provenance")
        label = f"{record.get('requirement_id', 'unknown requirement')}.interpretation_provenance"
        errors.extend(validate_provenance(provenance, label))
        if isinstance(provenance, dict):
            expected = {
                **DEFAULT,
                "generated_by": "ai",
            }
            for field, value in expected.items():
                if provenance.get(field) != value:
                    errors.append(f"{label}: {field} must be {value!r}")
            if "reviewed_by" in provenance or "review_method" in provenance:
                errors.append(f"{label}: deprecated review wording is forbidden")
            if not isinstance(provenance.get("source_analysis_method"), str) or not provenance["source_analysis_method"].strip():
                errors.append(f"{label}: source_analysis_method must be non-empty")

    for relative in (
        "external_governance/sources/source-registry.json",
        "external_governance/requirements/requirements/manifest.json",
        "external_governance/requirements/requirements.json",
        "external_governance/requirements/derivative-crosswalks.json",
    ):
        document = load(VIGIL / relative)
        provenance = document.get("authorship_provenance")
        errors.extend(validate_provenance(provenance, relative))
        if isinstance(provenance, dict):
            for field, value in DEFAULT.items():
                if provenance.get(field) != value:
                    errors.append(f"{relative}: {field} must be {value!r}")

    for relative in (
        "external_governance/sources/source-review-queue.json",
        "external_governance/requirements/requirements-index.json",
        "external_governance/requirements/completeness-report.json",
        "external_governance/requirements/source-coverage-manifests.json",
        "external_governance/requirements/derivative-crosswalk-index.json",
    ):
        document = load(VIGIL / relative)
        provenance = document.get("authorship_provenance")
        errors.extend(validate_provenance(provenance, relative, require_upstream=True))
        if isinstance(provenance, dict):
            for field, value in GENERATED.items():
                if provenance.get(field) != value:
                    errors.append(f"{relative}: {field} must be {value!r}")

    for relative in (
        "VIGIL.Incidents.Index.json",
        "VIGIL.Registry.Index.json",
    ):
        document = load(VIGIL / relative)
        provenance = document.get("authorship_provenance")
        errors.extend(validate_provenance(provenance, relative, require_upstream=True))
        if isinstance(provenance, dict):
            for field, value in GENERATED.items():
                if provenance.get(field) != value:
                    errors.append(f"{relative}: {field} must be {value!r}")
    return errors


def main() -> int:
    errors = validate_repository()
    if errors:
        print("VIGIL authorship provenance validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("VIGIL authorship provenance validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
