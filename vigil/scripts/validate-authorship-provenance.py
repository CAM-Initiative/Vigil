#!/usr/bin/env python3
"""Validate VIGIL authorship, human-review, and human-verification provenance."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
DECLARATION_PATH = VIGIL / "provenance" / "AUTHORSHIP-PROVENANCE.json"
DECLARATION_REF = "vigil/provenance/AUTHORSHIP-PROVENANCE.json"

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


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def validate_provenance(
    provenance: object,
    label: str,
    *,
    require_declaration: bool = False,
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

    if require_declaration and provenance.get("declaration") != DECLARATION_REF:
        errors.append(f"{label}: declaration must reference {DECLARATION_REF}")
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
    declaration = load(DECLARATION_PATH)
    if declaration.get("default_provenance") != DEFAULT:
        errors.append(f"{DECLARATION_PATH}: default_provenance differs from the VIGIL default")

    declared_vocab = declaration.get("controlled_vocabulary")
    if not isinstance(declared_vocab, dict):
        errors.append(f"{DECLARATION_PATH}: controlled_vocabulary must be an object")
    else:
        for field, expected in VOCABULARY.items():
            actual = declared_vocab.get(field)
            if not isinstance(actual, dict) or set(actual) != expected:
                errors.append(f"{DECLARATION_PATH}: controlled vocabulary mismatch for {field}")

    inheritance = declaration.get("inheritance_rules", {})
    expected_false = {
        "absence_of_override_means_human_review",
        "repository_acceptance_means_human_review",
        "repository_publication_means_human_review",
        "repository_acceptance_means_human_verification",
    }
    for field in expected_false:
        if inheritance.get(field) is not False:
            errors.append(f"{DECLARATION_PATH}: {field} must be false")
    for field in ("default_applies_when_override_absent", "explicit_artefact_override_precedence"):
        if inheritance.get(field) is not True:
            errors.append(f"{DECLARATION_PATH}: {field} must be true")
    if inheritance.get("explicit_artefact_override_field") != "authorship_provenance":
        errors.append(f"{DECLARATION_PATH}: explicit override field must be authorship_provenance")
    if inheritance.get("legacy_interpretive_provenance_is_authorship_override") is not False:
        errors.append(f"{DECLARATION_PATH}: legacy interpretive provenance must not override authorship provenance")

    dataset = declaration.get("dataset_declarations", {}).get(
        "external-governance-sources-and-requirements", {}
    )
    if dataset.get("provenance") != DEFAULT:
        errors.append(f"{DECLARATION_PATH}: external governance source/requirement provenance differs from the VIGIL default")
    if dataset.get("external_source_authorship_unchanged") is not True:
        errors.append(f"{DECLARATION_PATH}: external-source authorship boundary must be preserved")
    generated = declaration.get("generated_artefact_rule", {})
    if generated.get("provenance") != GENERATED:
        errors.append(f"{DECLARATION_PATH}: generated artefact provenance is invalid")
    if generated.get("upstream_provenance_reference_required") is not True:
        errors.append(f"{DECLARATION_PATH}: generated artefacts must reference upstream provenance")

    requirements = load(VIGIL / "external_requirements" / "requirements.json")
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
        "external_sources/source-registry.json",
        "external_requirements/requirements.json",
        "external_requirements/derivative-crosswalks.json",
    ):
        document = load(VIGIL / relative)
        provenance = document.get("authorship_provenance")
        errors.extend(validate_provenance(provenance, relative, require_declaration=True))
        if isinstance(provenance, dict):
            for field, value in DEFAULT.items():
                if provenance.get(field) != value:
                    errors.append(f"{relative}: {field} must be {value!r}")

    for relative in (
        "external_sources/source-review-queue.json",
        "external_requirements/requirements-index.json",
        "external_requirements/completeness-report.json",
        "external_requirements/source-coverage-manifests.json",
        "external_requirements/derivative-crosswalk-index.json",
    ):
        document = load(VIGIL / relative)
        provenance = document.get("authorship_provenance")
        errors.extend(
            validate_provenance(
                provenance,
                relative,
                require_declaration=True,
                require_upstream=True,
            )
        )
        if isinstance(provenance, dict):
            for field, value in GENERATED.items():
                if provenance.get(field) != value:
                    errors.append(f"{relative}: {field} must be {value!r}")

    for relative in (
        "VIGIL.Failures.Index.json",
        "VIGIL.Observations.Index.json",
        "VIGIL.Proposals.Index.json",
        "VIGIL.PatchNotes.Index.json",
        "VIGIL.Research.Index.json",
        "VIGIL.Learn.Index.json",
        "VIGIL.Registry.Index.json",
    ):
        document = load(VIGIL / relative)
        provenance = document.get("authorship_provenance")
        errors.extend(
            validate_provenance(
                provenance,
                relative,
                require_declaration=True,
                require_upstream=True,
            )
        )
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
