#!/usr/bin/env python3
"""Remove evidence types that are not eligible for taxonomy textbook case studies."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
CASE_EXAMPLES = ROOT / "generated" / "VIGIL.FailureTaxonomy.CaseFileExamples.json"
INCIDENT_RECORDS = ROOT.parent / "records" / "incidents"
EXCLUDED_SOURCE_TYPES = {"interaction record"}


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise TypeError(f"{path} must contain one JSON object")
    return data


def canonical_sources(record: dict[str, Any]) -> list[dict[str, Any]]:
    sources = record.get("source_records", [])
    if not isinstance(sources, list):
        return []
    return [source for source in sources if isinstance(source, dict)]


def preferred_source(record: dict[str, Any]) -> dict[str, Any]:
    sources = canonical_sources(record)
    preferred = record.get("preferred_evidence")
    preferred = preferred if isinstance(preferred, dict) else {}
    preferred_url = str(preferred.get("source_url") or "").strip()
    if preferred_url:
        selected = next(
            (source for source in sources if str(source.get("source_url") or "").strip() == preferred_url),
            None,
        )
        if selected is not None:
            return selected
    return sources[0] if sources else {}


def publication_eligible(record: dict[str, Any]) -> bool:
    source_type = str(preferred_source(record).get("source_type") or "").strip().lower()
    return source_type not in EXCLUDED_SOURCE_TYPES


def incident_record(incident_id: str, cache: dict[str, dict[str, Any]]) -> dict[str, Any]:
    if incident_id in cache:
        return cache[incident_id]
    path = INCIDENT_RECORDS / f"{incident_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"Taxonomy case-study projection references missing Incident {incident_id}")
    cache[incident_id] = load_json(path)
    return cache[incident_id]


def filter_examples(data: dict[str, Any]) -> tuple[dict[str, Any], set[str]]:
    cache: dict[str, dict[str, Any]] = {}
    excluded_incidents: set[str] = set()

    for collection_name in ("families", "classes"):
        collection = data.get(collection_name)
        if not isinstance(collection, dict):
            continue
        for key, examples in list(collection.items()):
            if not isinstance(examples, list):
                continue
            retained: list[dict[str, Any]] = []
            for example in examples:
                if not isinstance(example, dict):
                    continue
                incident_id = str(example.get("incident_id") or "").strip()
                if not incident_id:
                    continue
                record = incident_record(incident_id, cache)
                if not publication_eligible(record):
                    excluded_incidents.add(incident_id)
                    continue
                retained.append(example)
            collection[key] = retained

    return data, excluded_incidents


def assert_no_excluded_examples(data: dict[str, Any]) -> None:
    cache: dict[str, dict[str, Any]] = {}
    for collection_name in ("families", "classes"):
        collection = data.get(collection_name)
        if not isinstance(collection, dict):
            continue
        for examples in collection.values():
            if not isinstance(examples, list):
                continue
            for example in examples:
                if not isinstance(example, dict):
                    continue
                incident_id = str(example.get("incident_id") or "").strip()
                if not incident_id:
                    continue
                record = incident_record(incident_id, cache)
                if not publication_eligible(record):
                    source_type = str(preferred_source(record).get("source_type") or "").strip()
                    raise ValueError(
                        f"{incident_id} remains in the textbook case-study projection with excluded "
                        f"source_type {source_type!r}"
                    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the current textbook case-study projection still contains an excluded evidence type.",
    )
    args = parser.parse_args()

    data = load_json(CASE_EXAMPLES)
    if args.check:
        assert_no_excluded_examples(data)
        print("Textbook case-study evidence-type exclusions verified.")
        return

    filtered, excluded_incidents = filter_examples(data)
    CASE_EXAMPLES.write_text(
        json.dumps(filtered, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    assert_no_excluded_examples(filtered)
    if excluded_incidents:
        print(
            "Excluded textbook case-study Incidents whose preferred evidence is an interaction record: "
            + ", ".join(sorted(excluded_incidents))
        )
    else:
        print("No textbook case-study Incidents used excluded evidence types.")


if __name__ == "__main__":
    main()
