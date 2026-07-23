#!/usr/bin/env python3
"""Validate AI reviewer provenance and source artefact-access metadata."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
RECORDS = ROOT / "vigil" / "records"
REVIEW_REQUIRED = {
    "review_id", "reviewer_type", "reviewer_platform", "reviewer_model",
    "review_date", "review_scope", "capability_profile", "known_limitations",
    "review_outcome",
}
SOURCE_REQUIRED = {"evidence_modality", "primary_artefact_access", "interpretive_reliance"}
ACCESS_REQUIRED = {"access_status", "reviewing_system", "access_method", "direct_primary_artefact_review", "limitations"}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("record must be one JSON object")
    return value


def parse_iso_date(value: Any) -> date | None:
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


def main() -> int:
    errors: list[str] = []
    count = 0
    for path in sorted(RECORDS.rglob("*.json")):
        count += 1
        try:
            record = load(path)
        except Exception as exc:
            errors.append(f"{path}: unable to load: {exc}")
            continue

        provenance = record.get("interpretive_provenance")
        if not isinstance(provenance, dict):
            errors.append(f"{path}: missing interpretive_provenance")
            continue
        identity = record.get("record_identity")
        created_value = identity.get("created") if isinstance(identity, dict) else None
        if not created_value:
            created_value = record.get("date_recorded")
        created_date = parse_iso_date(created_value)
        if created_date is None:
            errors.append(f"{path}: record creation date must begin with an ISO YYYY-MM-DD date")

        history = provenance.get("review_history")
        current = provenance.get("current_ai_review")
        editor = provenance.get("human_governance_editor")
        if not isinstance(history, list) or not history:
            errors.append(f"{path}: review_history must be a non-empty list")
        else:
            seen_review_ids: set[str] = set()
            for index, review in enumerate(history):
                if not isinstance(review, dict):
                    errors.append(f"{path}: review_history[{index}] must be an object")
                    continue
                missing = sorted(REVIEW_REQUIRED - set(review))
                if missing:
                    errors.append(f"{path}: review_history[{index}] missing {missing}")
                review_id = review.get("review_id")
                if not isinstance(review_id, str) or not review_id:
                    errors.append(f"{path}: review_history[{index}].review_id must be non-empty")
                elif review_id in seen_review_ids:
                    errors.append(f"{path}: duplicate review_id {review_id!r}")
                else:
                    seen_review_ids.add(review_id)
                review_date = parse_iso_date(review.get("review_date"))
                if review_date is None:
                    errors.append(
                        f"{path}: review_history[{index}].review_date must be an ISO YYYY-MM-DD date"
                    )
                elif created_date is not None and review_date < created_date:
                    errors.append(
                        f"{path}: review {review_id!r} dated {review_date} predates record creation "
                        f"{created_date}"
                    )
        if not isinstance(current, dict):
            errors.append(f"{path}: current_ai_review must be an object")
        else:
            missing = sorted(REVIEW_REQUIRED - set(current))
            if missing:
                errors.append(f"{path}: current_ai_review missing {missing}")
            if current.get("reviewer_type") != "AI analytical reviewer":
                errors.append(f"{path}: current reviewer must be identified as AI analytical reviewer")
            current_id = current.get("review_id")
            if isinstance(history, list) and not any(
                isinstance(item, dict) and item.get("review_id") == current_id
                for item in history
            ):
                errors.append(f"{path}: current_ai_review must also be preserved in append-only review_history")
        if not isinstance(editor, dict) or not editor.get("name") or not editor.get("authority_boundary"):
            errors.append(f"{path}: human_governance_editor must identify name and authority boundary")

        sources = record.get("source_records")
        if not isinstance(sources, list):
            errors.append(f"{path}: source_records must be a list")
            continue
        for index, source in enumerate(sources):
            if not isinstance(source, dict):
                errors.append(f"{path}: source_records[{index}] must be an object")
                continue
            missing = sorted(SOURCE_REQUIRED - set(source))
            if missing:
                errors.append(f"{path}: source_records[{index}] missing {missing}")
                continue
            modalities = source.get("evidence_modality")
            if not isinstance(modalities, list) or not modalities:
                errors.append(f"{path}: source_records[{index}].evidence_modality must be non-empty list")
            access = source.get("primary_artefact_access")
            if not isinstance(access, dict):
                errors.append(f"{path}: source_records[{index}].primary_artefact_access must be object")
            else:
                missing_access = sorted(ACCESS_REQUIRED - set(access))
                if missing_access:
                    errors.append(f"{path}: source_records[{index}].primary_artefact_access missing {missing_access}")

    fm = RECORDS / "failures" / "2026" / "VIGIL-2026-FM-0033.json"
    if not fm.exists():
        errors.append(f"{fm}: primary behavioural evidence accessibility failure record is required")

    if errors:
        print("Interpretive provenance validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Interpretive provenance validation passed for {count} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
