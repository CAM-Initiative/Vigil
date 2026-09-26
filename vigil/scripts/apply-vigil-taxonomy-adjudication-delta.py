#!/usr/bin/env python3
"""Apply an explicit semantic adjudication delta to the VIGIL Incident × Fidelity Class matrix.

Unlike sync-vigil-taxonomy-adjudications.py, this tool never invents or migrates
semantic decisions. The supplied delta must contain one complete decision row
for every current selectable Fidelity Class for each named canonical Incident.
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V = ROOT / "vigil"
T = V / "taxonomy"
INDEX = T / "VIGIL.FailureTaxonomy.Index.json"
MATRIX = T / "VIGIL.FailureTaxonomy.Adjudications.json"
INC = V / "records" / "incidents"

SEMANTIC_DECISIONS = {
    "failure-occurrence",
    "successful-invariant",
    "ambiguous-boundary",
    "no-mapping",
    "unresolved",
}


def load(path: Path):
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def current_classes():
    index = load(INDEX)
    ids = []
    for family in index.get("families", []):
        data = load(T / family["file"])
        ids.extend(
            item["class_id"]
            for item in data.get("classes", [])
            if isinstance(item, dict) and isinstance(item.get("class_id"), str)
        )
    return index["standard"]["version"], sorted(set(ids))


def validate_row(incident_id, row, expected_ids):
    if not isinstance(row, dict):
        raise ValueError(f"{incident_id}: adjudication row must be an object")
    actual_ids = sorted(row)
    if actual_ids != expected_ids:
        missing = sorted(set(expected_ids) - set(actual_ids))
        extra = sorted(set(actual_ids) - set(expected_ids))
        raise ValueError(
            f"{incident_id}: row does not match current selectable class set; "
            f"missing={missing}, extra={extra}"
        )
    for class_id in expected_ids:
        cell = row[class_id]
        if not isinstance(cell, dict):
            raise ValueError(f"{incident_id} {class_id}: cell must be an object")
        decision = cell.get("decision")
        reason = cell.get("reason")
        if decision not in SEMANTIC_DECISIONS:
            raise ValueError(
                f"{incident_id} {class_id}: invalid semantic decision {decision!r}"
            )
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError(f"{incident_id} {class_id}: non-empty reason required")


def apply_delta(matrix, delta):
    version, class_ids = current_classes()
    if delta.get("taxonomy_version") != version:
        raise ValueError(
            f"delta taxonomy_version {delta.get('taxonomy_version')!r} "
            f"does not match current taxonomy {version!r}"
        )
    if matrix.get("taxonomy_version") != version:
        raise ValueError(
            f"matrix taxonomy_version {matrix.get('taxonomy_version')!r} "
            f"does not match current taxonomy {version!r}"
        )

    incidents = matrix.get("incidents")
    if not isinstance(incidents, dict):
        raise ValueError("matrix incidents must be an object")

    rows = delta.get("incidents")
    if not isinstance(rows, dict) or not rows:
        raise ValueError("delta incidents must be a non-empty object")

    for incident_id, row in rows.items():
        if not (INC / f"{incident_id}.json").exists():
            raise ValueError(f"{incident_id}: canonical Incident missing")
        validate_row(incident_id, row, class_ids)
        incidents[incident_id] = {
            class_id: row[class_id] for class_id in class_ids
        }

    matrix["incidents"] = dict(
        sorted(
            incidents.items(),
            key=lambda item: int(item[0].rsplit("-", 1)[-1]),
        )
    )
    return matrix, sorted(rows), len(class_ids)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("delta", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    matrix = load(MATRIX)
    delta = load(args.delta)
    updated, incident_ids, class_count = apply_delta(matrix, delta)
    text = json.dumps(updated, indent=2, ensure_ascii=False) + "\n"

    if args.check:
        current = MATRIX.read_text(encoding="utf-8")
        if current != text:
            print(
                "Adjudication delta is not fully applied to the canonical matrix.",
                file=sys.stderr,
            )
            raise SystemExit(1)
        print(
            f"Adjudication delta already applied for {len(incident_ids)} "
            f"Incident(s) × {class_count} classes."
        )
        return

    MATRIX.write_text(text, encoding="utf-8")
    print(
        f"Applied adjudication delta for {len(incident_ids)} Incident(s) × "
        f"{class_count} classes: {', '.join(incident_ids)}"
    )


if __name__ == "__main__":
    main()
