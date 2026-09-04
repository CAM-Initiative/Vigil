#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_governance" / "requirements"
SHARD = REQ / "requirements" / "IEEE-7009" / "2024.json"
LEDGER = REQ / "metadata-review.json"
BACKLOG = REQ / "reextraction-backlog.json"
FIDELITY = REQ / "source-fidelity.json"
DATE = "2026-09-04"

TARGETS = {
    "EXTREQ-528978BC3EB32446": {
        "timing_or_frequency": [
            "Capabilities are required when the conforming ASOI is in operation."
        ],
        "required_artefacts": [
            "Specification of design constraints, prerequisites and characteristics enabling operational monitoring, anomaly detection and risk-relevant anomaly identification."
        ],
        "evidence_expectation": [
            "Evidence that the ASOI can monitor its behavior, detect anomalous-behavior incidents and identify anomalies with potential to cause unacceptable risk during operation."
        ],
        "verification_method": [
            "Demonstrate the three source-defined operational capabilities under the specified operational and regulatory context and trace them to the supporting design-constraint, prerequisite and characteristic specification."
        ],
        "exceptions_or_qualifications": [
            "This legacy aggregate record groups three source-native capabilities; linked atomic records remain the preferred unit for independent assessment.",
            "The source requires the capabilities to a specified extent during operation in a specified regulatory context."
        ],
    },
    "EXTREQ-BBE358DBC3A6FD24": {
        "timing_or_frequency": [
            "Capabilities are required when the conforming ASOI is in operation."
        ],
        "required_artefacts": [
            "Specification of design constraints, prerequisites and characteristics enabling behavior moderation and modification for preservation of freedom from unacceptable risk."
        ],
        "evidence_expectation": [
            "Evidence that the ASOI can moderate and modify behavior to preserve freedom from unacceptable risk during operation."
        ],
        "verification_method": [
            "Demonstrate moderation and modification capabilities under the specified operational and regulatory context and trace them to the supporting Clause 6 specification."
        ],
        "exceptions_or_qualifications": [
            "This legacy aggregate record groups two source-native capabilities; linked atomic records remain the preferred unit for independent assessment.",
            "The source requires the capabilities to a specified extent during operation in a specified regulatory context."
        ],
    },
    "EXTREQ-C2FC30A1E260F4C1": {
        "timing_or_frequency": [
            "Execute monitoring during operation; issue periodic or continuation requests at the source-defined DIOP points and perform diagnosis when behavioral anomalies are detected."
        ],
        "required_artefacts": [
            "Operational monitoring and anomaly records plus diagnostic reports covering detected anomalies, labelled deviations, criticality, confidence and target recovery threshold."
        ],
        "evidence_expectation": [
            "Operational traces showing monitoring, anomaly detection or behavior verification, diagnosis, root-cause confidence, deviation criticality, target recovery threshold and required reporting or continuation requests."
        ],
        "verification_method": [
            "Exercise DIOP1 through DIOP3 in accordance with the fail-safe design-in-operation process and confirm the specified monitoring, detection, diagnosis, calculations, reporting and continuation-request behavior."
        ],
        "exceptions_or_qualifications": [
            "This legacy aggregate record spans DIOP1 through DIOP3; linked atomic records remain the preferred independent assessment units.",
            "DIOP tasks are implemented in accordance with the fail-safe design-in-operation process and the Clause 6 design constraints, prerequisites and characteristics."
        ],
    },
    "EXTREQ-4041B6E279EF30CC": {
        "timing_or_frequency": [
            "Perform moderation or modification in response to the operational state as applicable; evaluate freedom from unacceptable risk after moderation or modification and at DIOP6, with optional continuation requests issued only when the preceding decision task determines they are needed."
        ],
        "required_artefacts": [
            "Operational records of selected and initiated moderating responses or behavioral modifications, evaluation results, deviation reporting and continuation-request decisions."
        ],
        "evidence_expectation": [
            "Operational traces showing identification, selection and initiation of risk-preserving responses or modifications, subsequent safety-state evaluation and continuation-request decisions."
        ],
        "verification_method": [
            "Exercise DIOP4 through DIOP6 and confirm response or modification selection and initiation, evaluation of freedom from unacceptable risk, deviation reporting and conditional continuation-request behavior."
        ],
        "exceptions_or_qualifications": [
            "This legacy aggregate record spans DIOP4 through DIOP6; linked atomic records remain the preferred independent assessment units.",
            "Optional continuation requests in DIOP4 through DIOP6 are conditional on the immediately preceding decision task.",
            "DIOP tasks are implemented in accordance with the fail-safe design-in-operation process and Clause 6 constraints, prerequisites and characteristics."
        ],
    },
}

FIELDS = (
    "applicable_actor", "governed_object", "timing_or_frequency", "required_artefacts",
    "evidence_expectation", "verification_method", "applicability_conditions",
    "exceptions_or_qualifications",
)

def dump(path: Path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

records = json.loads(SHARD.read_text(encoding="utf-8"))
by_id = {r["requirement_id"]: r for r in records}
assert set(TARGETS) <= set(by_id)

identity_snapshot = {
    rid: {
        "identity_key": by_id[rid]["identity_key"],
        "clause_or_control": by_id[rid]["clause_or_control"],
        "requirement_posture": by_id[rid]["requirement_posture"],
        "requirement_summary": by_id[rid]["requirement_summary"],
        "related_external_requirements": list(by_id[rid]["related_external_requirements"]),
    }
    for rid in TARGETS
}

for rid, spec in TARGETS.items():
    r = by_id[rid]
    for field, value in spec.items():
        r[field] = list(value)
    limitations = list(r.get("review_limitations", []))
    note = "Legacy aggregate identity remains active for stability; field-level metadata is now complete, while semantic decomposition remains represented by linked atomic successor records and the explicit re-extraction backlog."
    if note not in limitations:
        limitations.append(note)
    r["review_limitations"] = limitations

for rid, snap in identity_snapshot.items():
    r = by_id[rid]
    assert r["identity_key"] == snap["identity_key"]
    assert r["clause_or_control"] == snap["clause_or_control"]
    assert r["requirement_posture"] == snap["requirement_posture"]
    assert r["requirement_summary"] == snap["requirement_summary"]
    assert r["related_external_requirements"] == snap["related_external_requirements"]

dump(SHARD, records)

ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
ledger["updated_at"] = DATE
review_by = {e["requirement_id"]: e for e in ledger["entries"]}
for rid in TARGETS:
    r = by_id[rid]
    e = review_by[rid]
    e["reviewed_at"] = DATE
    e["review_basis"] = "licensed-primary-text"
    e["review_notes"] = [
        "Direct IEEE 7009-2024 primary-text review completed field-level metadata for this preserved legacy compound identity.",
        "The identity-level re-extraction finding remains open because linked source-native atomic records are the preferred independent assessment units."
    ]
    affected = {
        "timing_or_frequency", "required_artefacts", "evidence_expectation",
        "verification_method", "exceptions_or_qualifications",
    }
    e["field_status"] = {
        f: (
            "review-required"
            if f in affected
            else ("populated-reviewed" if r[f] else "not-specified-by-source")
        )
        for f in FIELDS
    }
    assert all(e["field_status"][f] == "review-required" for f in affected)
ledger["entries"] = sorted(review_by.values(), key=lambda e: e["requirement_id"])
dump(LEDGER, ledger)

backlog = json.loads(BACKLOG.read_text(encoding="utf-8"))
entries = [e for e in backlog["entries"] if e["external_source_id"] == "IEEE-7009"]
assert {e["current_requirement_id"] for e in entries} == set(TARGETS)
for e in entries:
    assert e["review_status"] == "in-review"
    assert e["recommended_repair"] == "semantic-decomposition-with-identity-migration"
# Backlog intentionally remains unchanged.
dump(BACKLOG, backlog)

fidelity = json.loads(FIDELITY.read_text(encoding="utf-8"))
for e in fidelity["entries"]:
    if e["external_source_id"] == "IEEE-7009" and e["source_version"] == "2024":
        assert e["fidelity_status"] == "requires-reextraction"
        assert e["effective_extraction_status"] == "partial"
        e["assessment_basis"] = (
            "Direct review against the complete lawfully accessed IEEE 7009-2024 licensed primary PDF confirms that all 67 canonical records now have complete field-level metadata decisions. "
            "Four established legacy records still compress distinct Clause 6.1 or Clause 8.3 activities. Their source-native atomic complements are present and linked, but the aggregate identities remain active for stability. "
            "The residual defect is therefore identity-level semantic decomposition rather than metadata incompleteness."
        )
        e["known_fidelity_gaps"] = [
            "Four legacy compound identities remain active for stability: 6.1(a-c), 6.1(d-e), DIOP1-3 and DIOP4-6.",
            "All four legacy compounds are now metadata-complete, but the source remains not fidelity-assured while those aggregate identities remain canonical alongside their linked atomic constituents."
        ]
        e["next_action"] = (
            "Retain all established IDs unless an explicit identity-retirement decision is made. "
            "If approved, retire only the four flagged aggregate identities to their linked source-native successors and re-run the fidelity gate."
        )
        break
else:
    raise AssertionError("IEEE-7009 fidelity entry missing")
dump(FIDELITY, fidelity)

print("IEEE 7009 legacy metadata enrichment valid: four stable aggregate IDs preserved; 20 source-supported provisional values added; affected field decisions remain review-required while four re-extraction flags remain open.")
