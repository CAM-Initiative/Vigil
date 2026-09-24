#!/usr/bin/env python3
"""Synchronise the Incident × Failure Class taxonomy-role matrix.

Mechanical only: adds MISSING cells for current selectable classes, migrates
the legacy failure-only matrix without discarding its decisions, and preserves
existing semantic decisions. It never chooses a taxonomy relationship.
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

SCHEMA_VERSION = "0.2.0"
SEMANTIC_DECISIONS = {
    "failure-occurrence",
    "successful-invariant",
    "ambiguous-boundary",
    "no-mapping",
    "unresolved",
}


def load(path):
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
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


def clean_prior_failure(value):
    if not isinstance(value, dict):
        return None
    decision = value.get("decision")
    reason = value.get("reason")
    if decision != "NO" or not isinstance(reason, str) or not reason.strip():
        return None
    return {"decision": "NO", "reason": reason.strip()}


def migrate_row(row):
    """Return one v0.2 role-aware row without inventing a relationship."""
    if not isinstance(row, dict):
        return {"decision": "MISSING", "reason": ""}

    decision = row.get("decision")
    reason = row.get("reason")
    reason = reason.strip() if isinstance(reason, str) else ""
    prior = clean_prior_failure(row.get("prior_failure_adjudication"))

    if decision in SEMANTIC_DECISIONS and reason:
        migrated = {"decision": decision, "reason": reason}
    elif decision == "YES" and reason:
        migrated = {"decision": "failure-occurrence", "reason": reason}
    elif decision == "UNRESOLVED" and reason:
        migrated = {"decision": "unresolved", "reason": reason}
    elif decision == "NO" and reason:
        # NO established only that failure occurrence was rejected. The two
        # exemplar roles remain unreviewed, so no-mapping cannot be inferred.
        migrated = {
            "decision": "MISSING",
            "reason": "",
            "prior_failure_adjudication": {"decision": "NO", "reason": reason},
        }
    else:
        migrated = {"decision": "MISSING", "reason": ""}

    if prior is not None:
        migrated["prior_failure_adjudication"] = prior
    return migrated


def sync(matrix, add):
    version, ids = current_classes()
    incidents = matrix.get("incidents", {})
    if not isinstance(incidents, dict):
        incidents = {}
    for incident_id in add:
        if not (INC / f"{incident_id}.json").exists():
            raise ValueError(f"{incident_id}: canonical Incident missing")
        incidents.setdefault(incident_id, {})

    output = {}
    for incident_id in sorted(incidents):
        if not (INC / f"{incident_id}.json").exists():
            raise ValueError(f"{incident_id}: canonical Incident missing")
        old_rows = incidents[incident_id] if isinstance(incidents[incident_id], dict) else {}
        output[incident_id] = {
            class_id: migrate_row(old_rows.get(class_id)) for class_id in ids
        }
    return {
        "schema_version": SCHEMA_VERSION,
        "taxonomy_version": version,
        "incidents": output,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--add-incident", action="append", default=[])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    old = load(MATRIX) if MATRIX.exists() else {"incidents": {}}
    new = sync(old, args.add_incident)
    text = json.dumps(new, indent=2, ensure_ascii=False) + "\n"
    existing = MATRIX.read_text(encoding="utf-8") if MATRIX.exists() else ""
    if args.check:
        if existing != text:
            print(
                "Adjudication matrix is out of sync; run "
                "sync-vigil-taxonomy-adjudications.py.",
                file=sys.stderr,
            )
            raise SystemExit(1)
        print("Adjudication matrix is synchronised.")
    else:
        MATRIX.write_text(text, encoding="utf-8")
        print(
            f"Synchronised {len(new['incidents'])} Incident(s) against "
            f"{len(current_classes()[1])} classes."
        )
