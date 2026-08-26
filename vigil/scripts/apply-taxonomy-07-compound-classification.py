#!/usr/bin/env python3
"""Apply the bounded TAXONOMY-07 compound-classification review."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FAILURES = ROOT / "records" / "failures" / "2026"
FAMILIES = ROOT / "taxonomy" / "families"
LEDGER = ROOT / "taxonomy" / "migration" / "VIGIL.FailureMode.TaxonomyClassificationLedger.json"
VERSION = "0.2.0-draft"
REVIEW_DATE = "2026-08-26"

# Primary tuple: family ID, class ID, confidence, basis.
# Secondary tuple: family ID, class ID, confidence, basis.
DECISIONS: dict[int, dict[str, Any]] = {
    5: {
        "primary": ("VIGIL-FF-0009", "VIGIL-FC-000049", "high", "The record defines a relational objective that cultivates attachment, unresolved affect, anticipatory dependence, or difficulty disengaging as a means of sustaining engagement and influence."),
    },
    16: {
        "primary": ("VIGIL-FF-0009", "VIGIL-FC-000050", "high", "Minor emotional and developmental vulnerability signals that should trigger protection or minimisation are repurposed as inputs to engagement, attachment, intimacy, and retention personalisation."),
    },
    23: {
        "primary": ("VIGIL-FF-0002", "VIGIL-FC-000013", "high", "The record expressly identifies loss of custody across user-authored, transformed, safety-normalised, classifier-visible, renderer-facing, outcome, and explanation stages, preventing reliable reconstruction of what was evaluated."),
        "secondary": [
            ("VIGIL-FF-0002", "VIGIL-FC-000047", "high", "The final explanation may attribute a specific policy or misconduct mechanism to the visible user request even though the available lineage does not establish that causal account and material alternatives remain unresolved."),
        ],
    },
    26: {
        "primary": ("VIGIL-FF-0002", "VIGIL-FC-000047", "high", "A deception or scheming mechanism is attributed without a traceable pathway audit of objectives, constraints, affordances, action history, concealment, or false-belief induction."),
    },
    27: {
        "primary": ("VIGIL-FF-0002", "VIGIL-FC-000047", "high", "Anthropomorphic or moralised mechanism labels are assigned without preserving the operational substrate and evaluation conditions needed to support the attribution."),
    },
    30: {
        "primary": ("VIGIL-FF-0002", "VIGIL-FC-000047", "high", "The responding system supplies a purposeful or causal runtime account despite lacking telemetry or another traceable evidentiary basis for the attributed mechanism."),
        "secondary": [
            ("VIGIL-FF-0004", "VIGIL-FC-000029", "medium", "The actual material interruption or runtime state is unavailable or not surfaced to the user whose understanding of safety, execution, privacy, or system agency depends on it."),
        ],
    },
    32: {
        "primary": ("VIGIL-FF-0001", "VIGIL-FC-000003", "high", "Affective governance valid or purported for one functional role or relationship scope is applied across a materially different companion, tutor, child-facing, clinical, accessibility, service, or hybrid-role scope without re-establishing applicability."),
    },
    38: {
        "primary": ("VIGIL-FF-0001", "VIGIL-FC-000046", "high", "A probabilistic identity match valid as investigative evidence is promoted into practically determinative authority for arrest, detention, or comparable coercive action."),
    },
    39: {
        "primary": ("VIGIL-FF-0001", "VIGIL-FC-000046", "high", "A population-derived prediction or care estimate valid as decision support is promoted into a binding or presumptive individual care-entitlement determination."),
    },
    43: {
        "primary": ("VIGIL-FF-0009", "VIGIL-FC-000051", "high", "Evidence selection, omission, framing, repetition, and confidence signalling are conditioned on the user's belief or relational posture in a way that steers confidence and compromises independent epistemic agency."),
        "secondary": [
            ("VIGIL-FF-0002", "VIGIL-FC-000011", "high", "Repeated outputs and selectively presented evidence are treated as independent corroboration even though their shared antecedent claim or inference pathway is not adequately traceable."),
        ],
    },
    50: {
        "primary": ("VIGIL-FF-0005", "VIGIL-FC-000048", "medium", "A facially valid content entitlement becomes unavailable solely because remote verification cannot complete and no cached entitlement, grace period, local verification, or degraded access route preserves access."),
    },
    58: {
        "primary": ("VIGIL-FF-0009", "VIGIL-FC-000052", "high", "The system treats another decision-maker as an instrument and uses deception, impersonation, concealment, pressure, persistence, or vulnerability exploitation to obtain an objective-directed state transition that bypasses meaningful independent choice."),
    },
    62: {
        "primary": ("VIGIL-FF-0001", "VIGIL-FC-000046", "high", "An unresolved biometric non-verification state is promoted into authority to suspend, deny, or materially burden an essential public benefit without independent evidence of ineligibility, fraud, or lawful revocation."),
        "secondary": [
            ("VIGIL-FF-0005", "VIGIL-FC-000048", "high", "The failure threshold independently requires absence of a proportionate alternative verification pathway while unresolved verification blocks practical benefit access."),
        ],
    },
}


def catalogue() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    families: dict[str, dict[str, Any]] = {}
    classes: dict[str, dict[str, Any]] = {}
    for path in sorted(FAMILIES.glob("*.json")):
        document = json.loads(path.read_text(encoding="utf-8"))
        family = document["family"]
        families[family["family_id"]] = family
        classes.update({item["class_id"]: item for item in document["classes"]})
    return families, classes


def family_ref(family_id: str, families: dict[str, dict[str, Any]]) -> dict[str, str]:
    family = families[family_id]
    return {
        "family_id": family_id,
        "family_code": family["family_code"],
        "family_name": family["name"],
    }


def class_ref(class_id: str, classes: dict[str, dict[str, Any]]) -> dict[str, str]:
    item = classes[class_id]
    return {
        "class_id": class_id,
        "class_code": item["class_code"],
        "class_name": item["name"],
        "abstraction": item["abstraction"],
    }


def provenance() -> dict[str, str]:
    return {
        "method": "compound-mechanism-record-definition-threshold-to-taxonomy-criteria-review",
        "review_date": REVIEW_DATE,
        "ai_provider": "OpenAI",
        "ai_platform": "ChatGPT Work",
        "ai_model": "GPT-5.6 Sol",
        "ai_role": "substantive taxonomy classification analysis, family-invariant testing, and drafting support",
        "human_review_status": "not-reviewed",
        "authority_boundary": "AI classification is provisional draft taxonomy analysis and is not independently authoritative.",
    }


def apply_decisions() -> None:
    families, classes = catalogue()
    for number, decision in DECISIONS.items():
        path = FAILURES / f"VIGIL-2026-FM-{number:04d}.json"
        record = json.loads(path.read_text(encoding="utf-8"))
        family_id, class_id, confidence, basis = decision["primary"]
        block: dict[str, Any] = {
            "taxonomy_version": VERSION,
            "classification_status": "classified",
            "classification_basis": basis,
            "classification_confidence": confidence,
            "classified_on": REVIEW_DATE,
            "structural_review_flags": ["compound-mechanism"] if decision.get("secondary") else [],
            "primary_family": family_ref(family_id, families),
            "primary_class": class_ref(class_id, classes),
        }
        if decision.get("secondary"):
            block["secondary_classifications"] = []
            for secondary_family_id, secondary_class_id, secondary_confidence, secondary_basis in decision["secondary"]:
                block["secondary_classifications"].append({
                    "family": family_ref(secondary_family_id, families),
                    "class": class_ref(secondary_class_id, classes),
                    "classification_basis": secondary_basis,
                    "classification_confidence": secondary_confidence,
                })
        block["classification_review_provenance"] = provenance()
        record["taxonomy_classification"] = block
        path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def rebuild_ledger() -> None:
    entries: list[dict[str, Any]] = []
    status_counts: Counter[str] = Counter()
    primary_family_counts: Counter[str] = Counter()
    primary_class_counts: Counter[str] = Counter()
    secondary_family_counts: Counter[str] = Counter()
    secondary_class_counts: Counter[str] = Counter()
    for path in sorted(FAILURES.glob("VIGIL-2026-FM-*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        block = record["taxonomy_classification"]
        family = block.get("primary_family", {})
        klass = block.get("primary_class", {})
        row: dict[str, Any] = {
            "failure_mode_id": record["id"],
            "title": record["record_identity"]["title"],
            "classification_status": block["classification_status"],
            "family_id": family.get("family_id"),
            "class_id": klass.get("class_id"),
            "classification_confidence": block["classification_confidence"],
            "classification_basis": block["classification_basis"],
            "structural_review_flags": block["structural_review_flags"],
        }
        secondaries = []
        for secondary in block.get("secondary_classifications", []):
            secondary_family = secondary["family"]
            secondary_class = secondary["class"]
            secondaries.append({
                "family_id": secondary_family["family_id"],
                "class_id": secondary_class["class_id"],
                "classification_confidence": secondary["classification_confidence"],
                "classification_basis": secondary["classification_basis"],
            })
            secondary_family_counts[secondary_family["family_id"]] += 1
            secondary_class_counts[secondary_class["class_id"]] += 1
        if secondaries:
            row["secondary_classifications"] = secondaries
        entries.append(row)
        status_counts[block["classification_status"]] += 1
        if family.get("family_id"):
            primary_family_counts[family["family_id"]] += 1
        if klass.get("class_id"):
            primary_class_counts[klass["class_id"]] += 1
    document = {
        "schema_version": "1.0",
        "taxonomy_version": VERSION,
        "reviewed_on": REVIEW_DATE,
        "review_package": "TAXONOMY-07",
        "record_count": len(entries),
        "classification_status_counts": dict(sorted(status_counts.items())),
        "primary_family_counts": dict(sorted(primary_family_counts.items())),
        "primary_class_counts": dict(sorted(primary_class_counts.items())),
        "secondary_classification_count": sum(secondary_class_counts.values()),
        "secondary_family_counts": dict(sorted(secondary_family_counts.items())),
        "secondary_class_counts": dict(sorted(secondary_class_counts.items())),
        "entries": entries,
    }
    LEDGER.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    apply_decisions()
    rebuild_ledger()
    print(json.dumps({"reviewed_records": len(DECISIONS), "review_date": REVIEW_DATE}, sort_keys=True))


if __name__ == "__main__":
    main()
