#!/usr/bin/env python3
"""Authoritative effective Layer 1 builder for VIGIL external governance requirements.

The frozen v1.1 baseline and historical extension packs remain reproducible. This
builder removes source-family assumptions from the active extension path, makes
extension state transitions explicit, distinguishes metadata fingerprints from
reviewed-source artefact digests, and emits normalized effective Layer 1 v1.2.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "external_sources"
REQ = ROOT / "external_requirements"
EXT = REQ / "extensions"
TRANSITIONS = REQ / "extension-transitions.json"
REVIEW_ASSURANCE = REQ / "source-review-assurance.json"
COVERAGE = REQ / "source-coverage-manifests.json"
PROVENANCE_REF = "vigil/provenance/AUTHORSHIP-PROVENANCE.json"
DATASET_PROVENANCE = {
    "content_origin": "ai-authored",
    "generation_mode": "semi-autonomous",
    "human_role": "contract-approver",
    "human_authorship": False,
    "human_review_status": "not-reviewed",
    "human_verification_status": "not-verified",
    "declaration": PROVENANCE_REF,
}
GENERATED = {
    "content_origin": "deterministically-generated",
    "generation_mode": "deterministic-generation",
    "human_role": "contract-approver",
    "human_authorship": False,
    "human_review_status": "not-reviewed",
    "human_verification_status": "not-verified",
    "declaration": PROVENANCE_REF,
}

def imod(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module

legacy = imod(ROOT / "scripts/manage-external-requirements-extended.py", "legacy_extended")
base = legacy.base
led = legacy.led
ELED = legacy.ELED
EVIEW = legacy.EVIEW
EREQ = legacy.EREQ
XDATA = legacy.XDATA
XIDX = legacy.XIDX
XVIEW = legacy.XVIEW
CURRENT_REVIEWED_AT = ""
SOURCE_MAP: dict[tuple[str, str], dict[str, Any]] = {}

def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def jtxt(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"

def sk(value: dict[str, Any]) -> tuple[str, str]:
    return str(value.get("vigil_source_id", "")), str(value.get("source_version", ""))

def generated(upstream: list[str]) -> dict[str, Any]:
    return {**GENERATED, "upstream_provenance": upstream}

def metadata_fingerprint(source: dict[str, Any]) -> str:
    return str(source.get("source_metadata_fingerprint") or source.get("fingerprint") or led.fingerprint(source))

def normalise_source(source: dict[str, Any]) -> dict[str, Any]:
    out = json.loads(json.dumps(source))
    legacy_fp = out.pop("fingerprint", None)
    out["source_metadata_fingerprint"] = str(legacy_fp or led.fingerprint(out))
    out["source_metadata_fingerprint_semantics"] = (
        "SHA-256 of VIGIL's material source-metadata projection; not a digest of a reviewed source artefact."
    )
    return out

def access_note(access: str) -> str:
    return {
        "direct-public-primary": "Authoritative public primary text access recorded.",
        "direct-licensed-primary": "Lawful licensed primary text access recorded; copyrighted source text is not stored in VIGIL.",
        "official-public-extract": "Official publisher extract available; it is not treated as complete primary text.",
        "official-metadata-only": "Official metadata available; unseen normative text is not inferred.",
        "secondary-source-only": "Secondary material only; it cannot establish authoritative normative requirements.",
        "source-unavailable": "Authoritative source not available for direct review.",
    }[access]

def scope_defaults(status: str) -> tuple[str, list[str], str]:
    if status == "complete":
        return ("Bounded governance-significant extraction completed under the stated criterion.", [], "Monitor for material source revision.")
    if status == "partial":
        return ("Bounded direct-source extraction is represented; remaining material is not claimed complete.", ["Governance-significant content outside represented extraction scope"], "Continue bounded source review.")
    if status == "in-progress":
        return ("Primary-source review has begun; no completeness claim is made.", ["Full bounded primary-source review remains incomplete"], "Complete bounded source review.")
    if status == "not-started":
        return ("Primary-source access may exist, but analytical extraction has not started.", ["Full bounded primary-source review"], "Begin bounded primary-source review.")
    if status == "blocked-access":
        return ("Primary-source review is blocked by access; requirements are not inferred.", ["Normative or governance-significant content beyond available source access"], "Obtain lawful primary-source access.")
    if status == "supporting-only":
        return ("Supporting authority only; exhaustive first-class decomposition is outside current scope.", [], "Monitor source lifecycle.")
    if status == "context-only":
        return ("Context/discovery source only.", [], "Monitor source lifecycle as context.")
    if status == "excluded":
        return ("Explicitly excluded from current Layer 1 decomposition.", [], "No extraction action required.")
    return ("Superseded historical source version.", [], "Preserve historical provenance only.")

def generic_scope(update: dict[str, Any], source: dict[str, Any], reviewed_at: str) -> dict[str, Any]:
    status = update["extraction_status"]
    detail, default_unreviewed, next_action = scope_defaults(status)
    unreviewed = update.get("known_unreviewed_sections", default_unreviewed)
    inaccessible = update.get("inaccessible_sections", unreviewed if status == "blocked-access" else [])
    priority = update["alignment_priority"]
    rationale = update.get("alignment_priority_rationale") or {
        "critical-alignment-source": "Foundational external AI governance, assurance, risk, lifecycle, audit or controllability source.",
        "high-value-alignment-source": "Material external governance source with significant design, safety, transparency, impact or runtime relevance.",
        "supporting-specialist-source": "Specialist semantic, domain or implementation guidance.",
        "low-immediate-priority": "Supporting authority or lower-immediacy source rather than a first-order control baseline.",
    }[priority]
    action = status in {"blocked-access", "partial", "in-progress", "not-started"}
    return {
        "vigil_source_id": update["vigil_source_id"],
        "external_source_id": update["external_source_id"],
        "source_version": update["source_version"],
        "canonical_source_identifier": source["canonical_identifier"],
        "source_role": update["source_role"],
        "source_access_status": update["source_access_status"],
        "access_checked_at": update.get("access_checked_at", reviewed_at),
        "access_locator": update.get("access_locator", source["official_locator"]),
        "source_access_notes": update.get("source_access_notes", access_note(update["source_access_status"])),
        "extraction_status": status,
        "extraction_scope_notes": update.get("extraction_scope_notes", detail),
        "inaccessible_sections": inaccessible,
        "known_unreviewed_sections": unreviewed,
        "next_action": update.get("next_action", next_action),
        "alignment_priority": priority,
        "alignment_priority_rationale": rationale,
        "maintainer_action_required": update.get("maintainer_action_required", action),
        "maintainer_action": update.get("maintainer_action", next_action if action else None),
    }

def patched_scope(update: dict[str, Any]) -> dict[str, Any]:
    source = SOURCE_MAP[(update["vigil_source_id"], update["source_version"])]
    return generic_scope(update, source, CURRENT_REVIEWED_AT)

def patched_req_common(src, ver, clause, ikey, summary, posture, etype, actors, objects, stages, concepts, access, basis, method, limits):
    return {
        "requirement_id": base.requirement_id(src["vigil_source_id"], ver, clause, ikey),
        "identity_key": ikey,
        "vigil_source_id": src["vigil_source_id"],
        "external_source_id": src["external_source_id"],
        "source_version": ver,
        "canonical_source_identifier": src["canonical_identifier"],
        "issuer": src["issuer"],
        "jurisdiction": src["jurisdiction"],
        "source_class": src["source_class"],
        "source_lifecycle_state": src["source_lifecycle_state"],
        "source_role": "primary-ai-governance",
        "authoritative_locator": src["official_locator"],
        "clause_or_control": clause,
        "parent_section_or_group": None,
        "source_access_status": access,
        "source_review_date": CURRENT_REVIEWED_AT,
        "source_access_notes": access_note(access),
        "requirement_summary": summary,
        "requirement_posture": posture,
        "expectation_type": etype,
        "applicable_actor": actors,
        "governed_object": objects,
        "lifecycle_stage": stages,
        "governance_expectation": summary,
        "evidence_expectation": [],
        "timing_or_frequency": [],
        "required_artefacts": [],
        "verification_method": [],
        "applicability_conditions": [],
        "exceptions_or_qualifications": [],
        "governance_concepts": concepts,
        "source_defined_tags": [],
        "related_external_requirements": [],
        "interpretation_status": "reviewed-analytical-summary",
        "interpretation_provenance": {
            "basis": basis,
            "content_origin": "ai-authored",
            "generated_by": "ai",
            "generation_mode": "semi-autonomous",
            "human_role": "contract-approver",
            "human_authorship": False,
            "human_review_status": "not-reviewed",
            "human_verification_status": "not-verified",
            "source_analysis_method": method,
            "source_locator": src["official_locator"],
            "source_fingerprint": metadata_fingerprint(src),
        },
        "review_limitations": limits,
    }

def patched_direct_req(item: Any, src: dict[str, Any], defaults: dict[str, Any]) -> dict[str, Any]:
    c = {"clause": item[0], "identity_key": item[1], "summary": item[2]} if isinstance(item, list) else item
    access = defaults.get("source_access_status", "direct-licensed-primary")
    basis = "licensed-primary-text" if access == "direct-licensed-primary" else "direct-primary-text"
    r = patched_req_common(
        src, defaults["version"], c["clause"], c["identity_key"], c["summary"],
        c.get("posture", defaults["posture"]), c.get("expectation_type", defaults["expectation_type"]),
        c.get("actors", defaults["actors"]), c.get("objects", defaults["objects"]),
        c.get("stages", defaults["stages"]), c.get("concepts", defaults["concepts"]),
        access, basis,
        defaults.get("source_analysis_method", "Direct clause-level analysis of lawfully accessed primary text; analytical paraphrase only."),
        c.get("review_limitations", defaults["review_limitations"]),
    )
    r["parent_section_or_group"] = c.get("parent", defaults.get("parent"))
    r["governance_expectation"] = c.get("governance_expectation", c["summary"])
    r["evidence_expectation"] = c.get("evidence", [])
    r["timing_or_frequency"] = c.get("timing", [])
    r["required_artefacts"] = c.get("artefacts", [])
    r["verification_method"] = c.get("verification", [])
    r["applicability_conditions"] = c.get("conditions", defaults.get("conditions", []))
    r["exceptions_or_qualifications"] = c.get("qualifications", defaults.get("qualifications", []))
    r["source_defined_tags"] = [{"scheme": f"{defaults['source_tag']}-clause", "values": [c["clause"]]}]
    p = r["interpretation_provenance"]
    p["source_locator"] = defaults.get("source_locator", src["official_locator"])
    if defaults.get("source_metadata_fingerprint") or defaults.get("source_fingerprint"):
        p["source_fingerprint"] = defaults.get("source_metadata_fingerprint") or defaults["source_fingerprint"]
    return r

def source_semantics(source: dict[str, Any]) -> tuple[str, str]:
    external_id = str(source.get("external_source_id", "")).upper()
    issuer = str(source.get("issuer", "")).lower()
    source_class = str(source.get("source_class", "")).lower()
    canonical = str((source.get("canonical_identifier") or {}).get("value", "")).upper()
    if external_id.startswith("EU-AI-ACT") or any(t in source_class for t in ("law", "regulation", "directive", "legislation", "statute")):
        return "binding-law", "compliance"
    if "nist" in issuer or "national institute of standards and technology" in issuer or "imda" in issuer or "infocomm media development authority" in issuer:
        return "government-voluntary-framework", "alignment"
    if "ISO/IEC TR " in canonical or "ISO TR " in canonical or "IEC TR " in canonical:
        return "informative-technical-report", "reference-only"
    if "ISO/IEC TS " in canonical or "ISO TS " in canonical or "IEC TS " in canonical:
        return "voluntary-technical-specification", "conformance"
    if external_id.startswith("SPDX") or external_id.startswith("CYCLONEDX") or "technical-specification" in source_class:
        return "voluntary-technical-specification", "conformance"
    if "iso" in issuer or "iec" in issuer or "ieee" in issuer or "standard" in source_class:
        return "voluntary-consensus-standard", "conformance"
    if "framework" in source_class or "guidance" in source_class or external_id.startswith("AAM-SDOS"):
        return "industry-framework", "alignment"
    return "industry-framework", "reference-only"

def transition_key(item: dict[str, Any]) -> tuple[str, str, str, str]:
    return item["vigil_source_id"], item["source_version"], item["from_pack"], item["to_pack"]

def extension_context() -> tuple[dict[tuple[str, str], dict[str, Any]], dict[tuple[str, str], dict[str, Any]], str, list[str]]:
    errors: list[str] = []
    sources = {sk(x): x for x in load(base.LEDGER_PATH)["entries"]}
    scopes = {sk(x): x for x in load(base.SCOPE_PATH)["entries"]}
    origin = {key: "baseline" for key in scopes}
    reviewed_at = load(base.SCOPE_PATH)["reviewed_at"]
    transition_items = load(TRANSITIONS).get("transitions", []) if TRANSITIONS.exists() else []
    transitions = {transition_key(x): x for x in transition_items}
    if len(transitions) != len(transition_items):
        errors.append("duplicate source-scope transition registry key")
    used: set[tuple[str, str, str, str]] = set()
    for path in sorted(EXT.glob("*.json")):
        pack = load(path)
        date = pack.get("reviewed_at", reviewed_at)
        reviewed_at = max(reviewed_at, date)
        for seed in pack.get("sources", []):
            source = legacy.new_source(seed, date)
            key = sk(source)
            if key in sources:
                errors.append(f"{path.name}: duplicate extension source {key}")
            else:
                sources[key] = source
        for update in pack.get("source_scope_updates", []):
            key = update["vigil_source_id"], update["source_version"]
            source = sources.get(key)
            if source is None:
                errors.append(f"{path.name}: scope update references absent source {key}")
                continue
            previous = scopes.get(key)
            previous_origin = origin.get(key, "baseline")
            if previous_origin != "baseline":
                tkey = key[0], key[1], previous_origin, path.name
                transition = transitions.get(tkey)
                if transition is None:
                    errors.append(f"{path.name}: repeated scope update {key} lacks explicit transition")
                else:
                    if transition.get("external_source_id") != source.get("external_source_id"):
                        errors.append(f"{path.name}: transition source identity mismatch for {key}")
                    if transition.get("from_extraction_status") != (previous or {}).get("extraction_status"):
                        errors.append(f"{path.name}: transition prior state mismatch for {key}")
                    if transition.get("to_extraction_status") != update.get("extraction_status"):
                        errors.append(f"{path.name}: transition target state mismatch for {key}")
                    used.add(tkey)
            scopes[key] = generic_scope(update, source, date)
            origin[key] = path.name
    unused = sorted(set(transitions) - used)
    if unused:
        errors.append(f"registered source-scope transitions were not exercised: {unused}")
    return sources, scopes, reviewed_at, errors

def packs_with_context():
    global CURRENT_REVIEWED_AT
    for path in sorted(EXT.glob("*.json")):
        pack = load(path)
        CURRENT_REVIEWED_AT = pack.get("reviewed_at", CURRENT_REVIEWED_AT)
        yield pack

def load_assurance(sources: dict[tuple[str, str], dict[str, Any]], requirements: list[dict[str, Any]], errors: list[str]):
    if not REVIEW_ASSURANCE.exists():
        return {}
    doc = load(REVIEW_ASSURANCE)
    if doc.get("schema_version") != "1.0" or doc.get("authorship_provenance") != DATASET_PROVENANCE:
        errors.append("source-review-assurance.json: invalid schema/provenance contract")
    requirement_sources = {r["requirement_id"]: sk(r) for r in requirements}
    reviews = {}
    assurance_ids = set()
    for review in doc.get("source_reviews", []):
        key = sk(review)
        if key in reviews:
            errors.append(f"source-review-assurance.json: duplicate source/version {key}")
            continue
        source = sources.get(key)
        if source is None:
            errors.append(f"source-review-assurance.json: absent source {key}")
            continue
        if review.get("external_source_id") != source.get("external_source_id"):
            errors.append(f"source-review-assurance.json: external source mismatch {key}")
        if review.get("source_metadata_fingerprint") != metadata_fingerprint(source):
            errors.append(f"source-review-assurance.json: metadata fingerprint mismatch {key}")
        digest = review.get("reviewed_source_digest")
        if digest is not None:
            value = digest.get("digest") if isinstance(digest, dict) else None
            if not isinstance(digest, dict) or digest.get("algorithm") != "sha256" or not isinstance(value, str) or len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
                errors.append(f"source-review-assurance.json: invalid reviewed-source digest {key}")
        for assurance in review.get("assurance_provenance", []):
            aid = assurance.get("assurance_id")
            if aid in assurance_ids:
                errors.append(f"source-review-assurance.json: duplicate assurance_id {aid}")
            assurance_ids.add(aid)
            if assurance.get("human_role") not in {"reviewer", "verifier"}:
                errors.append(f"source-review-assurance.json: invalid human assurance role {aid}")
            target = assurance.get("target_scope")
            ids = assurance.get("target_requirement_ids", [])
            if target == "source-version" and ids:
                errors.append(f"{aid}: source-version assurance cannot enumerate requirements")
            elif target == "explicit-requirements":
                if not ids:
                    errors.append(f"{aid}: explicit assurance requires requirement IDs")
                for rid in ids:
                    if requirement_sources.get(rid) != key:
                        errors.append(f"{aid}: assurance target absent or belongs to another source")
            elif target not in {"source-version", "explicit-requirements"}:
                errors.append(f"{aid}: invalid assurance target_scope")
        reviews[key] = review
    return reviews

def assurance_applies(item: dict[str, Any], requirement_id: str) -> bool:
    return item.get("target_scope") == "source-version" or requirement_id in item.get("target_requirement_ids", [])

def normalise_requirement(record: dict[str, Any], source: dict[str, Any], review: dict[str, Any] | None) -> dict[str, Any]:
    req = json.loads(json.dumps(record))
    p = dict(req["interpretation_provenance"])
    legacy_fp = p.pop("source_fingerprint", None)
    p["source_metadata_fingerprint"] = str(legacy_fp or metadata_fingerprint(source))
    digest = (review or {}).get("reviewed_source_digest")
    p["reviewed_source_digest"] = digest["digest"] if digest else None
    p["reviewed_source_digest_algorithm"] = digest["algorithm"] if digest else None
    p["reviewed_source_digest_status"] = "recorded" if digest else "not-recorded"
    req["interpretation_provenance"] = p
    assurance = []
    for item in (review or {}).get("assurance_provenance", []):
        if assurance_applies(item, req["requirement_id"]):
            value = json.loads(json.dumps(item))
            value.pop("target_scope", None)
            value.pop("target_requirement_ids", None)
            value["reviewed_source_digest"] = digest["digest"] if digest else None
            assurance.append(value)
    req["assurance_provenance"] = assurance
    req["normative_force"], req["alignment_relationship"] = source_semantics(source)
    return req

def validate_effective_requirement(req: dict[str, Any], source: dict[str, Any], errors: list[str]) -> None:
    force = {
        "binding-law", "regulatory-requirement", "contractual-or-incorporated-standard",
        "voluntary-consensus-standard", "voluntary-technical-specification", "informative-technical-report",
        "government-voluntary-framework", "industry-framework",
    }
    if req.get("normative_force") not in force:
        errors.append(f"{req['requirement_id']}: invalid normative_force")
    if req.get("alignment_relationship") not in {"compliance", "conformance", "alignment", "reference-only"}:
        errors.append(f"{req['requirement_id']}: invalid alignment_relationship")
    p = req["interpretation_provenance"]
    if "source_fingerprint" in p or p.get("source_metadata_fingerprint") != metadata_fingerprint(source):
        errors.append(f"{req['requirement_id']}: invalid effective source metadata provenance")
    if p.get("reviewed_source_digest_status") == "recorded":
        if p.get("reviewed_source_digest_algorithm") != "sha256" or not p.get("reviewed_source_digest"):
            errors.append(f"{req['requirement_id']}: invalid reviewed-source digest provenance")
    elif p.get("reviewed_source_digest") is not None or p.get("reviewed_source_digest_algorithm") is not None:
        errors.append(f"{req['requirement_id']}: absent reviewed-source digest must remain null")

def coverage_manifest(scope: dict[str, Any], reqs: list[dict[str, Any]], review: dict[str, Any] | None) -> dict[str, Any]:
    status = scope["extraction_status"]
    state = {
        "complete": "bounded-complete", "partial": "partial", "in-progress": "partial",
        "not-started": "not-started", "blocked-access": "blocked", "supporting-only": "supporting-only",
        "context-only": "context-only", "excluded": "excluded", "superseded-version": "superseded",
    }[status]
    direct = scope["source_access_status"] in {"direct-public-primary", "direct-licensed-primary"}
    digest = (review or {}).get("reviewed_source_digest")
    digest_values = [digest["digest"]] if digest else []
    return {
        "vigil_source_id": scope["vigil_source_id"],
        "external_source_id": scope["external_source_id"],
        "source_version": scope["source_version"],
        "coverage_state": state,
        "source_access_status": scope["source_access_status"],
        "source_retrieval_state": "retrieved" if direct and reqs else ("not-established" if direct else "not-retrieved"),
        "analysis_state": status,
        "reviewed_sections": [],
        "reviewed_sections_status": "not-enumerated",
        "represented_requirement_count": len(reqs),
        "represented_clause_or_control_count": len({r["clause_or_control"] for r in reqs}),
        "expected_requirement_population": None,
        "known_unreviewed_sections": scope["known_unreviewed_sections"],
        "inaccessible_sections": scope["inaccessible_sections"],
        "completeness_criterion": scope["extraction_scope_notes"],
        "completeness_claim": (
            "Bounded-complete means governance-significant material identified by the recorded criterion is represented; it is not exhaustive atomisation."
            if status == "complete" else "No bounded-complete claim is made."
        ),
        "informative_material_treatment": "Informative material is atomised only when it has independent governance meaning.",
        "reviewed_source_digest_status": "recorded" if digest else ("not-recorded" if direct and reqs else "not-applicable"),
        "reviewed_source_digests": digest_values,
        "human_assurance_count": len((review or {}).get("assurance_provenance", [])),
        "assurance_limitations": [] if digest or not (direct and reqs) else ["Exact reviewed source artefact digest was not recorded for this historical extraction."],
    }

def effective() -> tuple[dict[Path, str], list[str]]:
    global SOURCE_MAP, CURRENT_REVIEWED_AT
    sources, scopes, reviewed_at, errors = extension_context()
    SOURCE_MAP = sources
    CURRENT_REVIEWED_AT = reviewed_at
    legacy.packs = packs_with_context
    legacy.scope = patched_scope
    legacy.req_common = patched_req_common
    legacy.direct_req = patched_direct_req
    out, legacy_errors = legacy.effective()
    errors.extend(legacy_errors)

    legacy_ledger = json.loads(out[ELED])
    legacy_requirements = json.loads(out[EREQ])
    source_map = {sk(x): x for x in legacy_ledger["entries"]}
    reviews = load_assurance(source_map, legacy_requirements["requirements"], errors)
    requirements = [normalise_requirement(r, source_map[sk(r)], reviews.get(sk(r))) for r in legacy_requirements["requirements"]]
    for req in requirements:
        validate_effective_requirement(req, source_map[sk(req)], errors)

    upstream = [
        "vigil/external_requirements/requirements.json",
        "vigil/external_requirements/extensions/*.json",
        "vigil/external_requirements/extension-transitions.json",
        "vigil/external_requirements/source-review-assurance.json",
    ]
    source_upstream = [
        "vigil/external_sources/ledger.json",
        "vigil/external_requirements/extensions/*.json",
        "vigil/external_requirements/extension-transitions.json",
    ]
    normalized_sources = [normalise_source(x) for x in legacy_ledger["entries"]]
    out[ELED] = jtxt({
        "schema_version": "1.1",
        "updated_at": reviewed_at,
        "generated_from": ["external_sources/ledger.json", "external_requirements/extensions/*.json", "external_requirements/extension-transitions.json"],
        "authorship_provenance": DATASET_PROVENANCE,
        "generation_provenance": generated(source_upstream),
        "entries": normalized_sources,
    })
    out[EREQ] = jtxt({
        "schema_version": "1.2",
        "updated_at": reviewed_at,
        "generated_from": [x.removeprefix("vigil/") for x in upstream],
        "authorship_provenance": DATASET_PROVENANCE,
        "generation_provenance": generated(upstream),
        "requirement_count": len(requirements),
        "requirements": sorted(requirements, key=lambda x: x["requirement_id"]),
    })

    by_source: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for req in requirements:
        by_source.setdefault(sk(req), []).append(req)
    manifests = [
        coverage_manifest(scope, by_source.get(sk(scope), []), reviews.get(sk(scope)))
        for scope in sorted(scopes.values(), key=lambda x: (x["external_source_id"], x["source_version"]))
    ]
    out[COVERAGE] = jtxt({
        "schema_version": "1.0",
        "generated_at": reviewed_at,
        "authorship_provenance": generated(upstream),
        "source_version_count": len(manifests),
        "manifests": manifests,
    })

    idx = json.loads(out[base.INDEX_PATH])
    for item in idx["requirements"]:
        source = source_map[(item["vigil_source_id"], item["source_version"])]
        item["normative_force"], item["alignment_relationship"] = source_semantics(source)
    idx["authorship_provenance"] = generated(upstream)
    out[base.INDEX_PATH] = jtxt(idx)

    lines = [
        "# Effective External Governance Sources", "",
        "Frozen Layer 0 plus reviewed extension sources. Inventory only; no CAM applicability or conformity is asserted.", "",
        f"- Effective source versions: {len(normalized_sources)}",
        f"- Reviewed through: {reviewed_at}", "",
        "| VIGIL Source | External Source | Version | Issuer | Lifecycle | Canonical identifier | Metadata fingerprint |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for src in normalized_sources:
        lines.append(
            f"| `{src['vigil_source_id']}` | {src.get('title') or ''} | `{src['source_version']}` | {src['issuer']} | "
            f"`{src['source_lifecycle_state']}` | `{src['canonical_identifier']['value']}` | `{src['source_metadata_fingerprint'][:12]}…` |"
        )
    lines += [
        "",
        "The metadata fingerprint identifies registered source/version metadata only; it is not a reviewed-document digest.",
        "Private-sector frameworks retain their actual publisher authority; inclusion does not elevate them to standards or regulatory authority.",
        "",
        "## Authorship provenance",
        "",
        f"This is a deterministically generated projection. No human review or verification is implied. See `{PROVENANCE_REF}`.",
        "",
    ]
    out[EVIEW] = "\n".join(lines)

    return out, errors

def run(build: bool = False, check: bool = False) -> None:
    out, errors = effective()
    if build and not errors:
        for path, content in out.items():
            path.write_text(content, encoding="utf-8")
            print("Wrote", path)
    if check:
        for path, content in out.items():
            if (path.read_text(encoding="utf-8") if path.exists() else "") != content:
                errors.append(f"generated output is stale: {path}")
    if errors:
        raise ValueError("\n".join(errors))
    ledger = json.loads(out[ELED])
    requirements = json.loads(out[EREQ])
    crosswalks = json.loads(out[XDATA])
    print(
        f"Effective external requirements valid: {len(ledger['entries'])} source versions, "
        f"{requirements['requirement_count']} requirements, {crosswalks['crosswalk_count']} derivative crosswalks"
    )

def main() -> None:
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(dest="cmd", required=True)
    subs.add_parser("build")
    validate = subs.add_parser("validate")
    validate.add_argument("--check-generated", action="store_true")
    args = parser.parse_args()
    run(build=args.cmd == "build", check=getattr(args, "check_generated", False))

if __name__ == "__main__":
    main()
