#!/usr/bin/env python3
"""Validate optional faceted analysis on VIGIL Failure Mode records.

Legacy Failure Mode records remain valid without a faceted_analysis block. When the
block is present, this validator enforces the controlled reporting dimensions used
for event state, manifestation/cause separation, failure locus, repair side,
observability, propagation, completion/verification state, and execution pattern.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
FAILURES_ROOT = ROOT / "vigil" / "records" / "failures"

ALLOWED_FIELDS = {
    "schema_version",
    "event_state",
    "manifestation",
    "mechanism_or_cause",
    "cause_status",
    "failure_locus",
    "repair_side",
    "execution_phase",
    "observability",
    "evidence_state",
    "effect_or_harm",
    "propagation",
    "completion_state",
    "verification_state",
    "execution_pattern",
    "reporting_notes",
}

REQUIRED_FIELDS = {
    "schema_version",
    "event_state",
    "failure_locus",
    "observability",
    "evidence_state",
    "propagation",
}

SCALAR_ENUMS = {
    "schema_version": {"1.0"},
    "event_state": {"anomaly", "hazard", "near-miss", "incident", "confirmed-failure", "unknown"},
    "cause_status": {
        "unknown",
        "hypothesised",
        "corroborated",
        "reproduced",
        "root-cause-confirmed",
        "not-applicable",
    },
    "observability": {
        "overt",
        "latent",
        "silent",
        "differentially-observable",
        "externally-detected",
        "user-reported",
        "unknown",
    },
    "evidence_state": {
        "reported",
        "observed",
        "corroborated",
        "reproduced",
        "root-cause-confirmed",
        "provisional",
        "unknown",
    },
    "propagation": {"local", "downstream", "cascading", "cross-provider", "systemic", "unknown"},
    "completion_state": {
        "completed",
        "premature-termination",
        "non-termination",
        "false-completion",
        "unknown",
        "not-applicable",
    },
    "verification_state": {
        "not-attempted",
        "incomplete",
        "incorrect",
        "passed",
        "failed",
        "unknown",
        "not-applicable",
    },
    "execution_pattern": {
        "single-pass",
        "repeated-step",
        "looping",
        "retry-amplification",
        "degraded-but-functional",
        "unknown",
        "not-applicable",
    },
}

FAILURE_LOCUS_VALUES = {
    "model",
    "harness",
    "orchestration",
    "agent-agent-interface",
    "model-harness-interface",
    "memory",
    "retrieval",
    "tool",
    "tool-environment-interface",
    "data-pipeline",
    "provider-service",
    "cross-provider-interface",
    "user-interface",
    "evaluator",
    "human-workflow",
    "external-environment",
    "other",
    "unknown",
}

REPAIR_SIDE_VALUES = FAILURE_LOCUS_VALUES | {"governance", "multi-party"}

EXECUTION_PHASE_VALUES = {
    "intake",
    "planning",
    "reasoning",
    "delegation",
    "retrieval",
    "tool-selection",
    "tool-execution",
    "inter-agent-handoff",
    "verification",
    "completion-assessment",
    "output-generation",
    "post-processing",
    "monitoring",
    "change-management",
    "unknown",
    "not-applicable",
}

STRING_ARRAY_FIELDS = {
    "manifestation",
    "mechanism_or_cause",
    "effect_or_harm",
}


def is_blank(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def _validate_controlled_array(
    path: Path,
    field: str,
    value: Any,
    allowed: set[str],
    errors: list[str],
    *,
    require_nonempty: bool = False,
) -> None:
    label = f"failure_classification.faceted_analysis.{field}"
    if not isinstance(value, list):
        errors.append(f"{path}: {label} must be an array")
        return
    if require_nonempty and not value:
        errors.append(f"{path}: {label} must not be empty")
    if any(not isinstance(item, str) for item in value):
        errors.append(f"{path}: {label} must contain only strings")
        return
    if len(value) != len(set(value)):
        errors.append(f"{path}: {label} must contain unique values")
    for item in value:
        if item not in allowed:
            errors.append(f"{path}: {label} contains unsupported value {item!r}")


def validate_record(path: Path, record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if record.get("record_type") != "failure_mode":
        return errors

    classification = record.get("failure_classification")
    if not isinstance(classification, dict):
        return errors  # Existing record validator owns the required classification contract.

    block = classification.get("faceted_analysis")
    if block is None:
        return errors  # Intentional legacy compatibility.
    if not isinstance(block, dict):
        return [f"{path}: failure_classification.faceted_analysis must be an object"]

    unknown_fields = sorted(set(block) - ALLOWED_FIELDS)
    if unknown_fields:
        errors.append(
            f"{path}: failure_classification.faceted_analysis contains unsupported field(s): "
            f"{', '.join(unknown_fields)}"
        )

    missing = sorted(field for field in REQUIRED_FIELDS if field not in block or is_blank(block.get(field)))
    if missing:
        errors.append(
            f"{path}: failure_classification.faceted_analysis missing required fields: {', '.join(missing)}"
        )

    for field, allowed in SCALAR_ENUMS.items():
        if field in block and block.get(field) not in allowed:
            errors.append(
                f"{path}: failure_classification.faceted_analysis.{field} {block.get(field)!r} is not allowed"
            )

    if "failure_locus" in block:
        _validate_controlled_array(
            path,
            "failure_locus",
            block.get("failure_locus"),
            FAILURE_LOCUS_VALUES,
            errors,
            require_nonempty=True,
        )
    if "repair_side" in block:
        _validate_controlled_array(path, "repair_side", block.get("repair_side"), REPAIR_SIDE_VALUES, errors)
    if "execution_phase" in block:
        _validate_controlled_array(
            path,
            "execution_phase",
            block.get("execution_phase"),
            EXECUTION_PHASE_VALUES,
            errors,
        )

    for field in STRING_ARRAY_FIELDS:
        if field not in block:
            continue
        values = block.get(field)
        label = f"failure_classification.faceted_analysis.{field}"
        if not isinstance(values, list):
            errors.append(f"{path}: {label} must be an array")
            continue
        if any(not isinstance(value, str) or not value.strip() for value in values):
            errors.append(f"{path}: {label} must contain only non-empty strings")
        elif len(values) != len(set(values)):
            errors.append(f"{path}: {label} must contain unique values")

    notes = block.get("reporting_notes")
    if notes is not None and (not isinstance(notes, str) or not notes.strip()):
        errors.append(
            f"{path}: failure_classification.faceted_analysis.reporting_notes must be a non-empty string when present"
        )

    return errors


def _files(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    return sorted(root.rglob("*.json"), key=lambda item: item.as_posix())


def validate(root: Path | None = None) -> int:
    target = root or FAILURES_ROOT
    errors: list[str] = []
    reviewed = 0
    faceted = 0

    for path in _files(target):
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path}: unable to read JSON: {exc}")
            continue
        if not isinstance(record, dict) or record.get("record_type") != "failure_mode":
            continue
        reviewed += 1
        if isinstance(record.get("failure_classification"), dict) and "faceted_analysis" in record["failure_classification"]:
            faceted += 1
        errors.extend(validate_record(path, record))

    if errors:
        print("VIGIL Failure Mode facet validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"VIGIL Failure Mode facet validation passed: {reviewed} FM records, {faceted} faceted records.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", help="Optional FM record or directory to validate.")
    args = parser.parse_args()
    return validate(Path(args.path) if args.path else None)


if __name__ == "__main__":
    raise SystemExit(main())
