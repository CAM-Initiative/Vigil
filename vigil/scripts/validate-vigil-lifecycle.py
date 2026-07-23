#!/usr/bin/env python3
"""Validate VIGIL evidence routing, lifecycle separation, corpus coverage, and patch provenance."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
RECORDS = ROOT / "vigil" / "records"

ECOSYSTEM_STATES = {"active", "recurring", "improving", "externally-resolved", "unknown"}
VERIFICATION_STATES = {
    "unverified",
    "corpus-verified",
    "observed-in-one-runtime",
    "observed-across-runtimes",
    "regression-detected",
    "external-adoption-unknown",
    "not-applicable",
}
VERIFIED_REPAIR_STATES = {
    "corpus-verified",
    "observed-in-one-runtime",
    "observed-across-runtimes",
    "regression-detected",
}
REPAIR_BASES = {
    "not-yet-established",
    "pre-existing-coverage-identified",
    "patch-implemented",
    "cross-domain-repair-assembled",
    "not-actionable",
    "superseded",
}
CORPUS_COVERAGE_STATES = {
    "implemented-repair",
    "retrospective-coverage",
    "partial-coverage",
    "no-confirmed-coverage",
    "verification-pending",
    "not-applicable",
}
PATCH_CLASSIFICATIONS = {
    "doctrine-amendment",
    "integration-repair",
    "retrospective-coverage-synthesis",
    "taxonomy-reconciliation",
    "external-implementation",
    "verification",
}
DOCTRINE_CHANGE = {"none", "partial", "substantive"}
CURATOR_DIRECTIVES = (
    "add this incident to",
    "add this observation to",
    "do not amend caelestis",
    "do not amend in this vigil pass",
)
MISCLASSIFIED_OBSERVATIONS = {"VIGIL-2026-OBS-0008", "VIGIL-2026-OBS-0009"}


def load_records() -> tuple[dict[str, dict[str, Any]], dict[str, Path], list[str]]:
    records: dict[str, dict[str, Any]] = {}
    paths: dict[str, Path] = {}
    errors: list[str] = []
    for path in sorted(RECORDS.rglob("*.json")):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: unable to load JSON: {exc}")
            continue
        if not isinstance(value, dict):
            errors.append(f"{path}: expected one JSON object")
            continue
        record_id = value.get("id")
        if not isinstance(record_id, str) or not record_id:
            errors.append(f"{path}: missing non-empty id")
            continue
        records[record_id] = value
        paths[record_id] = path
    return records, paths, errors


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_corpus_coverage(
    record: dict[str, Any],
    path: Path,
    repair: dict[str, Any],
    errors: list[str],
) -> None:
    coverage = record.get("corpus_coverage")
    if not isinstance(coverage, dict):
        errors.append(f"{path}: failure mode requires corpus_coverage object")
        return

    classification = coverage.get("classification")
    if classification not in CORPUS_COVERAGE_STATES:
        errors.append(f"{path}: corpus_coverage.classification {classification!r} is not canonical")

    for field in (
        "corpus_repository",
        "corpus_ref",
        "corpus_commit",
        "assessed_date",
        "coverage_summary",
    ):
        if not non_empty_string(coverage.get(field)):
            errors.append(f"{path}: corpus_coverage.{field} must be a non-empty string")

    covered_by = coverage.get("covered_by")
    if not isinstance(covered_by, list):
        errors.append(f"{path}: corpus_coverage.covered_by must be an array")
        covered_by = []
    for index, item in enumerate(covered_by):
        if not isinstance(item, dict):
            errors.append(f"{path}: corpus_coverage.covered_by[{index}] must be an object")
            continue
        if not non_empty_string(item.get("instrument_id")):
            errors.append(f"{path}: corpus_coverage.covered_by[{index}].instrument_id must be non-empty")
        if not isinstance(item.get("path"), str):
            errors.append(f"{path}: corpus_coverage.covered_by[{index}].path must be a string")
        sections = item.get("sections")
        if not isinstance(sections, list) or any(not isinstance(section, str) for section in sections):
            errors.append(f"{path}: corpus_coverage.covered_by[{index}].sections must be an array of strings")
        if not non_empty_string(item.get("coverage_type")):
            errors.append(f"{path}: corpus_coverage.covered_by[{index}].coverage_type must be non-empty")

    gaps = coverage.get("remaining_gaps")
    if not isinstance(gaps, list) or any(not isinstance(item, str) for item in gaps):
        errors.append(f"{path}: corpus_coverage.remaining_gaps must be an array of strings")
        gaps = []

    if classification in {"implemented-repair", "retrospective-coverage"}:
        if repair.get("status") != "repaired":
            errors.append(f"{path}: {classification} requires repair_status.status 'repaired'")
        if repair.get("verification_status") not in VERIFIED_REPAIR_STATES:
            errors.append(
                f"{path}: {classification} requires a verified repair status "
                "(corpus-verified, observed-in-one-runtime, observed-across-runtimes, or regression-detected)"
            )
        if not repair.get("repaired_by"):
            errors.append(f"{path}: {classification} requires at least one linked patch")
        if not covered_by:
            errors.append(f"{path}: {classification} requires at least one covered_by instrument")

    if classification == "retrospective-coverage" and repair.get("repair_basis") != "pre-existing-coverage-identified":
        errors.append(
            f"{path}: retrospective-coverage requires repair_basis 'pre-existing-coverage-identified'"
        )

    if classification == "implemented-repair" and repair.get("repair_basis") not in {
        "patch-implemented",
        "cross-domain-repair-assembled",
        "pre-existing-coverage-identified",
    }:
        errors.append(f"{path}: implemented-repair conflicts with repair_basis {repair.get('repair_basis')!r}")

    if classification in {"partial-coverage", "no-confirmed-coverage", "verification-pending"} and not gaps:
        errors.append(f"{path}: {classification} must preserve concrete remaining_gaps")


def validate_failure(
    record_id: str,
    record: dict[str, Any],
    path: Path,
    records: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    ecosystem = record.get("ecosystem_status")
    if not isinstance(ecosystem, dict):
        errors.append(f"{path}: failure mode requires ecosystem_status object")
    else:
        status = ecosystem.get("status")
        if status not in ECOSYSTEM_STATES:
            errors.append(f"{path}: ecosystem_status.status {status!r} is not canonical")
        if not non_empty_string(ecosystem.get("basis")):
            errors.append(f"{path}: ecosystem_status.basis must be a non-empty string")
        if not non_empty_string(ecosystem.get("last_assessed")):
            errors.append(f"{path}: ecosystem_status.last_assessed must be a non-empty date string")
        if not isinstance(ecosystem.get("monitoring_required"), bool):
            errors.append(f"{path}: ecosystem_status.monitoring_required must be boolean")
        if status == "externally-resolved" and ecosystem.get("monitoring_required") is True:
            errors.append(f"{path}: externally-resolved ecosystem_status cannot require active monitoring")

    repair = record.get("repair_status")
    if not isinstance(repair, dict):
        errors.append(f"{path}: failure mode requires repair_status object")
        return

    verification = repair.get("verification_status")
    if verification not in VERIFICATION_STATES:
        errors.append(f"{path}: repair_status.verification_status {verification!r} is not canonical")
    basis = repair.get("repair_basis")
    if basis not in REPAIR_BASES:
        errors.append(f"{path}: repair_status.repair_basis {basis!r} is not canonical")
    gaps = repair.get("remaining_gaps")
    if not isinstance(gaps, list) or any(not isinstance(item, str) for item in gaps):
        errors.append(f"{path}: repair_status.remaining_gaps must be an array of strings")

    repaired_by = repair.get("repaired_by", [])
    linked_patches = record.get("linked_records", {}).get("related_patch_notes", [])
    if not isinstance(repaired_by, list):
        errors.append(f"{path}: repair_status.repaired_by must be an array")
        repaired_by = []
    if not isinstance(linked_patches, list):
        errors.append(f"{path}: linked_records.related_patch_notes must be an array")
        linked_patches = []

    status = repair.get("status")
    if status == "unrepaired":
        if basis != "not-yet-established":
            errors.append(f"{path}: unrepaired CAM status requires repair_basis 'not-yet-established'")
        if repaired_by:
            errors.append(f"{path}: unrepaired CAM status cannot name a repairing patch")
        if non_empty_string(repair.get("date_repaired")):
            errors.append(f"{path}: unrepaired CAM status cannot have date_repaired")
    elif status in {"partially-repaired", "repaired"}:
        if not repaired_by:
            errors.append(f"{path}: {status} CAM status requires at least one repairing patch")
        if basis == "not-yet-established":
            errors.append(f"{path}: {status} CAM status cannot use repair_basis 'not-yet-established'")
    elif status == "not-actionable" and basis != "not-actionable":
        errors.append(f"{path}: not-actionable CAM status requires repair_basis 'not-actionable'")
    elif status == "superseded" and basis != "superseded":
        errors.append(f"{path}: superseded CAM status requires repair_basis 'superseded'")

    if basis in {
        "pre-existing-coverage-identified",
        "patch-implemented",
        "cross-domain-repair-assembled",
    } and not repaired_by:
        errors.append(f"{path}: repair_basis {basis!r} requires at least one linked repairing patch")

    for patch_id in repaired_by:
        if patch_id not in records:
            errors.append(f"{path}: repairing patch {patch_id!r} does not resolve")
            continue
        patch = records[patch_id]
        if patch.get("record_type") not in {"patch", "patch_note"}:
            errors.append(f"{path}: repairing record {patch_id!r} is not a patch")
        if patch_id not in linked_patches:
            errors.append(f"{path}: repairing patch {patch_id!r} is absent from linked_records.related_patch_notes")
        related_failures = patch.get("linked_records", {}).get("related_failure_modes", [])
        if isinstance(related_failures, list) and record_id not in related_failures:
            errors.append(f"{path}: patch {patch_id!r} does not reciprocally link to {record_id}")

    ecosystem_state = ecosystem.get("status") if isinstance(ecosystem, dict) else None
    if repair.get("status") == "repaired" and ecosystem_state in {"active", "recurring", "improving", "unknown"}:
        if not gaps:
            errors.append(
                f"{path}: repaired CAM status with non-resolved ecosystem state must preserve external or verification gaps"
            )

    validate_corpus_coverage(record, path, repair, errors)


def validate_patch(record: dict[str, Any], path: Path, errors: list[str]) -> None:
    classifications = record.get("patch_classifications")
    if not isinstance(classifications, list) or not classifications:
        errors.append(f"{path}: patch_classifications must be a non-empty array")
    else:
        unknown = sorted(set(classifications) - PATCH_CLASSIFICATIONS)
        if unknown:
            errors.append(f"{path}: unknown patch classification(s): {', '.join(unknown)}")
        if len(classifications) != len(set(classifications)):
            errors.append(f"{path}: patch_classifications must not contain duplicates")

    provenance = record.get("repair_provenance")
    if not isinstance(provenance, dict):
        errors.append(f"{path}: repair_provenance must be an object")
        return
    required = {
        "retrospective_synthesis",
        "doctrine_change",
        "repair_basis",
        "instruments_reviewed",
        "instruments_amended",
        "instruments_relied_upon_without_amendment",
        "coverage_origin",
    }
    missing = sorted(required - provenance.keys())
    if missing:
        errors.append(f"{path}: repair_provenance missing: {', '.join(missing)}")
    if not isinstance(provenance.get("retrospective_synthesis"), bool):
        errors.append(f"{path}: repair_provenance.retrospective_synthesis must be boolean")
    if provenance.get("doctrine_change") not in DOCTRINE_CHANGE:
        errors.append(f"{path}: repair_provenance.doctrine_change is not canonical")
    if not non_empty_string(provenance.get("repair_basis")):
        errors.append(f"{path}: repair_provenance.repair_basis must be a non-empty string")
    for field in (
        "instruments_reviewed",
        "instruments_amended",
        "instruments_relied_upon_without_amendment",
        "coverage_origin",
    ):
        if not isinstance(provenance.get(field), list):
            errors.append(f"{path}: repair_provenance.{field} must be an array")

    amended = provenance.get("instruments_amended", [])
    unchanged = provenance.get("instruments_relied_upon_without_amendment", [])
    doctrine = provenance.get("doctrine_change")
    if doctrine == "none" and amended:
        errors.append(f"{path}: doctrine_change 'none' conflicts with non-empty instruments_amended")
    if doctrine == "substantive" and not amended:
        errors.append(f"{path}: doctrine_change 'substantive' requires an amended instrument")
    if provenance.get("retrospective_synthesis") and not unchanged and "retrospective-coverage-synthesis" in (
        classifications or []
    ):
        if "existing" not in str(provenance.get("repair_basis", "")).lower():
            errors.append(
                f"{path}: retrospective synthesis requires unchanged coverage or an explicit existing-coverage basis"
            )

    origins = provenance.get("coverage_origin", [])
    if isinstance(origins, list):
        for index, origin in enumerate(origins):
            if not isinstance(origin, dict):
                errors.append(f"{path}: repair_provenance.coverage_origin[{index}] must be an object")
                continue
            if not non_empty_string(origin.get("instrument_id")):
                errors.append(f"{path}: repair_provenance.coverage_origin[{index}].instrument_id must be non-empty")
            sections = origin.get("relevant_sections")
            if not isinstance(sections, list) or any(not isinstance(section, str) for section in sections):
                errors.append(
                    f"{path}: repair_provenance.coverage_origin[{index}].relevant_sections must be an array of strings"
                )


def validate_proposal(record: dict[str, Any], path: Path, records: dict[str, dict[str, Any]], errors: list[str]) -> None:
    reconciliation = record.get("coverage_reconciliation")
    if reconciliation is not None:
        if not isinstance(reconciliation, dict):
            errors.append(f"{path}: coverage_reconciliation must be an object")
        else:
            for field in ("status", "assessed_date", "corpus_commit"):
                if not non_empty_string(reconciliation.get(field)):
                    errors.append(f"{path}: coverage_reconciliation.{field} must be non-empty")
            resolved_by = reconciliation.get("resolved_by", [])
            remaining_scope = reconciliation.get("remaining_scope", [])
            if not isinstance(resolved_by, list):
                errors.append(f"{path}: coverage_reconciliation.resolved_by must be an array")
                resolved_by = []
            if not isinstance(remaining_scope, list) or any(not isinstance(item, str) for item in remaining_scope):
                errors.append(f"{path}: coverage_reconciliation.remaining_scope must be an array of strings")
            for patch_id in resolved_by:
                if patch_id not in records:
                    errors.append(f"{path}: coverage reconciliation patch {patch_id!r} does not resolve")

    resolution = record.get("resolution_status")
    if isinstance(resolution, dict) and resolution.get("status") == "resolved":
        resolved_by = resolution.get("resolved_by", [])
        if not isinstance(resolved_by, list) or not resolved_by:
            errors.append(f"{path}: resolved proposal requires at least one resolving patch")


def validate_observation(record_id: str, record: dict[str, Any], path: Path, errors: list[str]) -> None:
    if record_id in MISCLASSIFIED_OBSERVATIONS:
        errors.append(f"{path}: {record_id} must be decomposed into embedded source evidence and removed")
    public_text = " ".join(
        str(record.get(field, ""))
        for field in ("summary", "why_it_matters_to_CAM", "next_action")
    ).lower()
    for phrase in CURATOR_DIRECTIVES:
        if phrase in public_text:
            errors.append(f"{path}: public OBS contains internal curator directive {phrase!r}")


def main() -> int:
    records, paths, errors = load_records()
    for record_id, record in records.items():
        path = paths[record_id]
        record_type = record.get("record_type")
        if record_type == "failure_mode":
            validate_failure(record_id, record, path, records, errors)
        elif record_type in {"patch", "patch_note"}:
            validate_patch(record, path, errors)
        elif record_type == "proposal":
            validate_proposal(record, path, records, errors)
        elif record_type == "observation":
            validate_observation(record_id, record, path, errors)

    if errors:
        print("VIGIL lifecycle and corpus coverage validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"VIGIL lifecycle and corpus coverage validation passed for {len(records)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
