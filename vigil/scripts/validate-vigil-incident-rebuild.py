#!/usr/bin/env python3
"""Guard against destructive VIGIL Incident rebuilds.

This is a maintainer workflow validator. It compares a candidate Incident with an
explicit baseline and requires an adjudication manifest to account for taxonomy
and source changes. It does not decide whether a taxonomy mapping is substantively
correct; it ensures that a rebuild cannot silently erase prior governed state.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ALLOWED_MODES = {"full-rebuild", "bounded-edit"}
ALLOWED_DISPOSITIONS = {
    "retained",
    "role-changed",
    "confidence-changed",
    "role-confidence-changed",
    "superseded",
    "removed-unsupported",
}
REMOVAL_DISPOSITIONS = {"superseded", "removed-unsupported"}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def load_git_json(ref: str, repo_path: str) -> dict[str, Any]:
    completed = subprocess.run(
        ["git", "show", f"{ref}:{repo_path}"],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise ValueError(
            f"unable to load baseline {ref}:{repo_path}: {completed.stderr.strip()}"
        )
    value = json.loads(completed.stdout)
    if not isinstance(value, dict):
        raise ValueError(f"{ref}:{repo_path} must contain a JSON object")
    return value


def mapping_list(record: dict[str, Any]) -> list[dict[str, Any]]:
    block = record.get("taxonomy_classification")
    if not isinstance(block, dict):
        return []
    items: list[dict[str, Any]] = []
    primary = block.get("primary_classification")
    if isinstance(primary, dict):
        items.append(primary)
    secondary = block.get("secondary_classifications")
    if isinstance(secondary, list):
        items.extend(item for item in secondary if isinstance(item, dict))
    return [item for item in items if isinstance(item.get("class_id"), str)]


def mapping_map(record: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["class_id"]: item for item in mapping_list(record)}


def source_key(source: dict[str, Any]) -> str:
    for field in ("source_url", "canonical_url", "source_title"):
        value = source.get(field)
        if isinstance(value, str) and value.strip():
            return f"{field}:{value.strip()}"
    return json.dumps(source, sort_keys=True, ensure_ascii=False)


def sources(record: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw = record.get("source_records")
    if not isinstance(raw, list):
        return {}
    return {
        source_key(item): item
        for item in raw
        if isinstance(item, dict)
    }


def word_count(value: Any) -> int:
    return len(value.split()) if isinstance(value, str) else 0


def non_empty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def disposition_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw = manifest.get("taxonomy_mapping_dispositions")
    if not isinstance(raw, list):
        return {}
    result: dict[str, dict[str, Any]] = {}
    for item in raw:
        if isinstance(item, dict) and isinstance(item.get("class_id"), str):
            result[item["class_id"]] = item
    return result


def new_mapping_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw = manifest.get("new_taxonomy_mappings")
    if not isinstance(raw, list):
        return {}
    result: dict[str, dict[str, Any]] = {}
    for item in raw:
        if isinstance(item, dict) and isinstance(item.get("class_id"), str):
            result[item["class_id"]] = item
    return result


def source_disposition_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw = manifest.get("source_dispositions")
    if not isinstance(raw, list):
        return {}
    result: dict[str, dict[str, Any]] = {}
    for item in raw:
        if not isinstance(item, dict):
            continue
        key = item.get("source_key") or item.get("source_url") or item.get("source_title")
        if isinstance(key, str) and key.strip():
            result[key.strip()] = item
    return result


def expected_disposition(old: dict[str, Any], new: dict[str, Any] | None) -> str:
    if new is None:
        return "removed"
    role_old = old.get("classification_role")
    role_new = new.get("classification_role")
    conf_old = old.get("classification_confidence")
    conf_new = new.get("classification_confidence")
    role_changed = role_old != role_new
    conf_changed = conf_old != conf_new
    if role_changed and conf_changed:
        return "role-confidence-changed"
    if role_changed:
        return "role-changed"
    if conf_changed:
        return "confidence-changed"
    return "retained"


def validate(
    baseline: dict[str, Any],
    candidate: dict[str, Any],
    manifest: dict[str, Any],
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    baseline_id = baseline.get("id")
    candidate_id = candidate.get("id")
    manifest_id = manifest.get("incident_id")
    if not (baseline_id == candidate_id == manifest_id):
        errors.append(
            f"incident identity mismatch: baseline={baseline_id!r}, "
            f"candidate={candidate_id!r}, manifest={manifest_id!r}"
        )

    mode = manifest.get("review_mode")
    if mode not in ALLOWED_MODES:
        errors.append(f"review_mode must be one of {sorted(ALLOWED_MODES)}")

    for field in ("summary",):
        if not non_empty(candidate.get(field)):
            errors.append(f"candidate {field} must be non-empty")

    assessment = candidate.get("vigil_assessment")
    if not isinstance(assessment, dict) or not non_empty(assessment.get("factual_basis")):
        errors.append("candidate vigil_assessment.factual_basis must be non-empty")

    taxonomy = candidate.get("taxonomy_classification")
    if not isinstance(taxonomy, dict):
        errors.append("candidate taxonomy_classification must be an object")
    elif not isinstance(taxonomy.get("classification_review_provenance"), dict):
        errors.append(
            "candidate taxonomy_classification.classification_review_provenance must be an object"
        )

    if mode == "full-rebuild":
        evidence = manifest.get("evidence_search")
        if not isinstance(evidence, dict) or evidence.get("status") != "performed":
            errors.append("full-rebuild requires evidence_search.status = performed")
        elif not isinstance(evidence.get("queries"), list) or not any(
            non_empty(item) for item in evidence.get("queries", [])
        ):
            errors.append("full-rebuild requires at least one recorded evidence-search query")

        review = manifest.get("taxonomy_review")
        if not isinstance(review, dict):
            errors.append("full-rebuild requires taxonomy_review")
        else:
            if review.get("current_taxonomy_loaded") is not True:
                errors.append("full-rebuild requires current_taxonomy_loaded = true")
            if review.get("complete_class_set_review") is not True:
                errors.append("full-rebuild requires complete_class_set_review = true")
            candidate_version = (
                taxonomy.get("taxonomy_version") if isinstance(taxonomy, dict) else None
            )
            if review.get("taxonomy_version") != candidate_version:
                errors.append(
                    "taxonomy_review.taxonomy_version must match candidate taxonomy_version"
                )
            tested = review.get("candidate_classes_tested")
            if not isinstance(tested, list) or not tested:
                errors.append("full-rebuild requires candidate_classes_tested")

        harm = manifest.get("harm_review")
        if not isinstance(harm, dict) or harm.get("status") not in {
            "reviewed",
            "preserved-not-reopened",
        }:
            errors.append(
                "full-rebuild requires harm_review.status = reviewed or preserved-not-reopened"
            )

        interpretation = manifest.get("governance_interpretation_review")
        if not isinstance(interpretation, dict) or interpretation.get("status") != "reviewed":
            errors.append(
                "full-rebuild requires governance_interpretation_review.status = reviewed"
            )

    old_mappings = mapping_map(baseline)
    new_mappings = mapping_map(candidate)
    dispositions = disposition_map(manifest)

    duplicate_dispositions = manifest.get("taxonomy_mapping_dispositions")
    if isinstance(duplicate_dispositions, list):
        ids = [
            item.get("class_id")
            for item in duplicate_dispositions
            if isinstance(item, dict) and isinstance(item.get("class_id"), str)
        ]
        if len(ids) != len(set(ids)):
            errors.append("taxonomy_mapping_dispositions contains duplicate class_id entries")

    for class_id, old in old_mappings.items():
        entry = dispositions.get(class_id)
        if entry is None:
            errors.append(f"baseline taxonomy mapping {class_id} has no disposition")
            continue
        disposition = entry.get("disposition")
        if disposition not in ALLOWED_DISPOSITIONS:
            errors.append(
                f"{class_id} disposition must be one of {sorted(ALLOWED_DISPOSITIONS)}"
            )
            continue

        new = new_mappings.get(class_id)
        expected = expected_disposition(old, new)
        if expected == "removed":
            if disposition not in REMOVAL_DISPOSITIONS:
                errors.append(
                    f"{class_id} is absent from candidate and must be superseded or removed-unsupported"
                )
            if not non_empty(entry.get("reason")):
                errors.append(f"{class_id} removal/supersession requires a substantive reason")
            if disposition == "superseded":
                replacements = entry.get("replacement_class_ids")
                if not isinstance(replacements, list) or not replacements:
                    errors.append(f"{class_id} superseded disposition requires replacement_class_ids")
                else:
                    missing = [
                        value
                        for value in replacements
                        if not isinstance(value, str) or value not in new_mappings
                    ]
                    if missing:
                        errors.append(
                            f"{class_id} replacement_class_ids must exist in candidate: {missing}"
                        )
        elif disposition != expected:
            errors.append(
                f"{class_id} disposition {disposition!r} does not match observed change {expected!r}"
            )

    unexplained = set(dispositions) - set(old_mappings)
    if unexplained:
        errors.append(
            "taxonomy_mapping_dispositions may describe only baseline mappings; "
            f"unexpected: {sorted(unexplained)}"
        )

    additions = set(new_mappings) - set(old_mappings)
    new_entries = new_mapping_map(manifest)
    for class_id in sorted(additions):
        entry = new_entries.get(class_id)
        if entry is None or not non_empty(entry.get("reason")):
            errors.append(f"new taxonomy mapping {class_id} requires a reason in new_taxonomy_mappings")
    stale_new = set(new_entries) - additions
    if stale_new:
        errors.append(
            f"new_taxonomy_mappings contains classes not newly added: {sorted(stale_new)}"
        )

    old_sources = sources(baseline)
    new_sources = sources(candidate)
    removed_source_keys = set(old_sources) - set(new_sources)
    source_dispositions = source_disposition_map(manifest)
    for key in sorted(removed_source_keys):
        source = old_sources[key]
        candidates = [
            key,
            source.get("source_url"),
            source.get("source_title"),
        ]
        entry = next(
            (
                source_dispositions[value]
                for value in candidates
                if isinstance(value, str) and value in source_dispositions
            ),
            None,
        )
        if entry is None or not non_empty(entry.get("reason")):
            errors.append(f"removed baseline source {key} requires source_dispositions reason")

    prose = manifest.get("prose_changes")
    if not isinstance(prose, dict):
        prose = {}
    for field, reason_key in (
        ("summary", "summary_reduction_reason"),
        ("factual_basis", "factual_basis_reduction_reason"),
    ):
        if field == "summary":
            old_text = baseline.get("summary")
            new_text = candidate.get("summary")
        else:
            old_assessment = baseline.get("vigil_assessment")
            new_assessment = candidate.get("vigil_assessment")
            old_text = old_assessment.get("factual_basis") if isinstance(old_assessment, dict) else None
            new_text = new_assessment.get("factual_basis") if isinstance(new_assessment, dict) else None
        old_words = word_count(old_text)
        new_words = word_count(new_text)
        if old_words >= 20 and new_words < old_words * 0.70:
            if not non_empty(prose.get(reason_key)):
                errors.append(
                    f"{field} shrank from {old_words} to {new_words} words; "
                    f"{reason_key} is required"
                )
            else:
                warnings.append(
                    f"{field} materially shortened ({old_words} -> {new_words} words) "
                    "with an explicit reduction reason"
                )

    return errors, warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    baseline = parser.add_mutually_exclusive_group(required=True)
    baseline.add_argument("--baseline-file", type=Path)
    baseline.add_argument("--baseline-ref")
    parser.add_argument("--candidate-file", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument(
        "--repo-path",
        help="Repository-relative Incident path for --baseline-ref. Defaults to candidate path.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        candidate = load_json(args.candidate_file)
        manifest = load_json(args.manifest)
        if args.baseline_file:
            baseline = load_json(args.baseline_file)
        else:
            repo_path = args.repo_path or args.candidate_file.as_posix()
            baseline = load_git_json(args.baseline_ref, repo_path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    errors, warnings = validate(baseline, candidate, manifest)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"Incident rebuild validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        f"Incident rebuild validation passed for {candidate.get('id')} "
        f"({len(mapping_list(baseline))} baseline taxonomy mapping(s) accounted for)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
