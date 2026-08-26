#!/usr/bin/env python3
"""Apply staged semantic-atomicity replacements for the consolidated EU AI Act."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_requirements"
SOURCES = ROOT / "external_sources"
REQUIREMENTS = REQ / "requirements.json"
REGISTRY = SOURCES / "source-registry.json"
SCOPE = REQ / "source-scope.json"
REEXTRACTIONS = REQ / "reextractions"
METADATA_NORMALIZATION = REEXTRACTIONS / "EU-AI-ACT-2026-07-27-metadata-normalization.json"


def load(path): return json.loads(Path(path).read_text(encoding="utf-8"))
def source_key(value): return value["vigil_source_id"], value["source_version"]
def requirement_id(source_id, version, clause, identity):
    seed = "|".join((source_id, version, clause.strip(), identity.strip()))
    return "EXTREQ-" + hashlib.sha256(seed.encode()).hexdigest()[:16].upper()

def parent_for(clause):
    if clause.startswith("Article 4a"): return "Article 4a — Processing of special categories of personal data for bias detection and correction"
    if clause.startswith("Article 9"): return "Article 9 — Risk management system"
    if clause.startswith("Article 10"): return "Article 10 — Data and data governance"
    if clause.startswith("Article 11"): return "Article 11 — Technical documentation"
    if clause.startswith("Article 12"): return "Article 12 — Record-keeping"
    if clause.startswith("Article 13"): return "Article 13 — Transparency and provision of information to deployers"
    if clause.startswith("Article 14"): return "Article 14 — Human oversight"
    if clause.startswith("Article 15"): return "Article 15 — Accuracy, robustness and cybersecurity"
    raise ValueError(f"unsupported staged EU AI Act clause: {clause}")

def apply_metadata_overlay(candidate, overrides):
    normalized = dict(candidate)
    override = overrides.get(candidate["requirement_id"], {})
    allowed = {
        "applicable_actor", "governed_object", "lifecycle_stage", "evidence_expectation",
        "timing_or_frequency", "required_artefacts", "verification_method",
        "applicability_conditions", "exceptions_or_qualifications"
    }
    unexpected = set(override) - allowed
    if unexpected:
        raise ValueError(f"unsupported metadata override fields for {candidate['requirement_id']}: {sorted(unexpected)}")
    for key, value in override.items():
        normalized[key] = value
    return normalized

def expand(candidate, source, scope, package, overrides):
    candidate = apply_metadata_overlay(candidate, overrides)
    clause, identity = candidate["clause_or_control"], candidate["identity_key"]
    expected = requirement_id(source["vigil_source_id"], source["source_version"], clause, identity)
    if candidate["requirement_id"] != expected:
        raise ValueError(f"non-deterministic candidate {candidate['requirement_id']}; expected {expected}")
    summary = candidate["requirement_summary"]
    return {
        "requirement_id": candidate["requirement_id"], "identity_key": identity,
        "vigil_source_id": source["vigil_source_id"], "external_source_id": source["external_source_id"],
        "source_version": source["source_version"], "canonical_source_identifier": source["canonical_identifier"],
        "issuer": source["issuer"], "jurisdiction": source["jurisdiction"], "source_class": source["source_class"],
        "source_lifecycle_state": source["source_lifecycle_state"], "source_role": scope["source_role"],
        "authoritative_locator": source["official_locator"], "clause_or_control": clause,
        "parent_section_or_group": parent_for(clause), "source_access_status": scope["source_access_status"],
        "source_review_date": package["reviewed_at"],
        "source_access_notes": "Authoritative consolidated public text directly reviewed on EUR-Lex for semantic re-extraction.",
        "requirement_summary": summary,
        "requirement_posture": candidate.get("requirement_posture", "mandatory-normative"),
        "expectation_type": candidate.get("expectation_type", "positive-duty"), "normative_force": "binding-law",
        "alignment_relationship": "compliance", "applicable_actor": candidate["applicable_actor"],
        "governed_object": candidate["governed_object"], "lifecycle_stage": candidate["lifecycle_stage"],
        "governance_expectation": candidate.get("governance_expectation", summary),
        "evidence_expectation": candidate.get("evidence_expectation", []),
        "timing_or_frequency": candidate.get("timing_or_frequency", []),
        "required_artefacts": candidate.get("required_artefacts", []),
        "verification_method": candidate.get("verification_method", []),
        "applicability_conditions": candidate.get("applicability_conditions", ["Applies to high-risk AI systems subject to the cited provision."]),
        "exceptions_or_qualifications": candidate.get("exceptions_or_qualifications", []),
        "governance_concepts": candidate["governance_concepts"],
        "source_defined_tags": [], "related_external_requirements": [], "interpretation_status": "reviewed-analytical-summary",
        "interpretation_provenance": {
            "basis":"direct-primary-text","content_origin":"ai-authored","generated_by":"ai","generation_mode":"semi-autonomous",
            "human_role":"contract-approver","human_authorship":False,"human_review_status":"not-reviewed","human_verification_status":"not-verified",
            "source_analysis_method":"Semantic-atomicity re-extraction from the authoritative consolidated EUR-Lex text under SOURCE-FIDELITY-METHODOLOGY.md, with source-explicit metadata normalization.",
            "source_locator":source["official_locator"],"source_metadata_fingerprint":source["source_metadata_fingerprint"],
            "reviewed_source_digest":None,"reviewed_source_digest_algorithm":None,"reviewed_source_digest_status":"not-recorded"},
        "assurance_provenance": [],
        "review_limitations": ["Consolidated EUR-Lex text is a documentation tool; authentic amending acts remain the legal source of record."]}

def migrate(check_only):
    package_paths = sorted(
        path for path in REEXTRACTIONS.glob("EU-AI-ACT-2026-07-27-*.json")
        if path.name != METADATA_NORMALIZATION.name
    )
    if not package_paths: raise ValueError("no staged EU AI Act re-extraction packages found")
    packages = [load(path) for path in package_paths]
    normalization = load(METADATA_NORMALIZATION)
    overrides = normalization.get("overrides", {})
    req_doc, registry, scopes = load(REQUIREMENTS), load(REGISTRY)["entries"], load(SCOPE)["entries"]
    requirements = req_doc["requirements"]; by_id = {x["requirement_id"]: x for x in requirements}
    all_retired, replacements, staged_ids = set(), [], set()
    for package in packages:
        key = source_key(package["source"])
        source = next((x for x in registry if source_key(x) == key), None)
        scope = next((x for x in scopes if source_key(x) == key), None)
        if source is None or scope is None: raise ValueError(f"unregistered source/version {key}")
        if source["external_source_id"] != package["source"]["external_source_id"]: raise ValueError("external_source_id mismatch")
        if source["source_metadata_fingerprint"] != package["source"]["source_metadata_fingerprint"]: raise ValueError("source fingerprint mismatch")
        retired = {x["requirement_id"] for x in package["retired_requirements"]}
        if all_retired & retired: raise ValueError("retired requirement appears in multiple packages")
        for item in package["retired_requirements"]:
            current = by_id.get(item["requirement_id"])
            if current is None: raise ValueError(f"retired requirement absent: {item['requirement_id']}")
            if source_key(current) != key: raise ValueError(f"retired requirement belongs to another source: {item['requirement_id']}")
        all_retired.update(retired)
        staged_ids.update(x["requirement_id"] for x in package["requirements"])
        replacements.extend(expand(x, source, scope, package, overrides) for x in package["requirements"])
    orphan_overrides = sorted(set(overrides) - staged_ids)
    if orphan_overrides:
        raise ValueError(f"metadata normalization references non-staged requirement IDs: {orphan_overrides}")
    replacement_ids = [x["requirement_id"] for x in replacements]
    if len(replacement_ids) != len(set(replacement_ids)): raise ValueError("duplicate replacement IDs")
    collisions = sorted((set(replacement_ids) & set(by_id)) - all_retired)
    if collisions: raise ValueError(f"replacement identity collisions: {collisions}")
    migrated = [x for x in requirements if x["requirement_id"] not in all_retired] + replacements
    migrated.sort(key=lambda x: x["requirement_id"])
    req_doc["requirements"], req_doc["requirement_count"] = migrated, len(migrated)
    req_doc["updated_at"] = max(x["reviewed_at"] for x in packages)
    print(f"EU AI Act staged migration valid: retire {len(all_retired)}, add {len(replacements)}, apply {len(overrides)} metadata normalizations, resulting count {len(migrated)}")
    if check_only: return
    REQUIREMENTS.write_text(json.dumps(req_doc, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(f"Wrote {REQUIREMENTS}")
    print("Next: manage-external-requirements.py build; validate --check-generated; validate-external-requirement-fidelity.py")

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--check-only",action="store_true"); args=parser.parse_args(); migrate(args.check_only)
if __name__ == "__main__": main()
