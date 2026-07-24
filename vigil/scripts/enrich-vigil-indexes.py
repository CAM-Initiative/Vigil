#!/usr/bin/env python3
"""Enrich generated VIGIL indexes with lifecycle, corpus, and review provenance."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"

INDEXES = {
    "observations": VIGIL / "VIGIL.Observations.Index.json",
    "failures": VIGIL / "VIGIL.Failures.Index.json",
    "proposals": VIGIL / "VIGIL.Proposals.Index.json",
    "patches": VIGIL / "VIGIL.PatchNotes.Index.json",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def records_by_id(directory: str) -> dict[str, dict[str, Any]]:
    output: dict[str, dict[str, Any]] = {}
    for path in sorted((RECORDS / directory).rglob("*.json")):
        record = load(path)
        if isinstance(record, dict) and isinstance(record.get("id"), str):
            output[record["id"]] = record
    return output


def review_summary(source: dict[str, Any]) -> dict[str, Any]:
    provenance = source.get("interpretive_provenance")
    if not isinstance(provenance, dict):
        return {}
    current = provenance.get("current_ai_review")
    editor = provenance.get("human_governance_editor")
    output: dict[str, Any] = {
        "operating_model": provenance.get("operating_model"),
        "review_count": len(provenance.get("review_history", [])) if isinstance(provenance.get("review_history"), list) else 0,
    }
    if isinstance(current, dict):
        output["ai_reviewer"] = {
            "platform": current.get("reviewer_platform"),
            "model": current.get("reviewer_model"),
            "review_date": current.get("review_date"),
            "review_scope": current.get("review_scope"),
            "capability_profile": current.get("capability_profile"),
            "known_limitations": current.get("known_limitations"),
        }
    if isinstance(editor, dict):
        output["human_governance_editor"] = {
            "name": editor.get("name"),
            "role": editor.get("role"),
            "review_level": editor.get("review_level"),
        }
    return {key: value for key, value in output.items() if value not in (None, "", [], {})}


def evidence_access_summary(source: dict[str, Any]) -> dict[str, Any]:
    modalities: list[str] = []
    access_states: list[str] = []
    direct_review = 0
    indirect_review = 0
    for item in source.get("source_records", []):
        if not isinstance(item, dict):
            continue
        values = item.get("evidence_modality")
        if isinstance(values, list):
            modalities.extend(str(value) for value in values)
        access = item.get("primary_artefact_access")
        if isinstance(access, dict):
            status = access.get("access_status")
            if status:
                access_states.append(str(status))
            if access.get("direct_primary_artefact_review") is True:
                direct_review += 1
            elif access.get("direct_primary_artefact_review") is False:
                indirect_review += 1
    return {
        "evidence_modalities": sorted(set(modalities)),
        "primary_artefact_access_states": sorted(set(access_states)),
        "direct_primary_artefact_reviews": direct_review,
        "indirect_or_unavailable_primary_artefact_reviews": indirect_review,
    }


def enrich_index(path: Path, source_records: dict[str, dict[str, Any]], fields: dict[str, str]) -> None:
    index = load(path)
    if not isinstance(index, dict) or not isinstance(index.get("records"), list):
        raise ValueError(f"{path} is not a generated VIGIL index")
    for item in index["records"]:
        if not isinstance(item, dict):
            continue
        source = source_records.get(str(item.get("id", "")))
        if source is None:
            continue
        for output_field, source_field in fields.items():
            value = source.get(source_field)
            if value not in (None, "", [], {}):
                item[output_field] = value
        review = review_summary(source)
        if review:
            item["interpretive_provenance_summary"] = review
        access = evidence_access_summary(source)
        if access["evidence_modalities"] or access["primary_artefact_access_states"]:
            item["evidence_access_summary"] = access
    write(path, index)


def main() -> None:
    enrich_index(INDEXES["observations"], records_by_id("observations"), {})
    enrich_index(
        INDEXES["failures"],
        records_by_id("failures"),
        {
            "ecosystem_status_summary": "ecosystem_status",
            "repair_status_summary": "repair_status",
            "corpus_coverage_summary": "corpus_coverage",
        },
    )
    enrich_index(
        INDEXES["proposals"],
        records_by_id("proposals"),
        {
            "resolution_status_summary": "resolution_status",
            "coverage_reconciliation_summary": "coverage_reconciliation",
        },
    )
    enrich_index(
        INDEXES["patches"],
        records_by_id("patches"),
        {
            "decision_trace": "decision_trace",
            "corpus_implementation": "corpus_implementation",
            "record_reconstruction": "record_reconstruction",
            "patch_classifications": "patch_classifications",
            "repair_provenance_summary": "repair_provenance",
        },
    )
    print("Enriched VIGIL indexes with decision traces, literal corpus implementation, lifecycle, reviewer, and evidence-access summaries.")


if __name__ == "__main__":
    main()
