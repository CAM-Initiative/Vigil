#!/usr/bin/env python3
"""Reconcile VIGIL evidence routing, lifecycle state, and patch provenance.

This maintenance script is intentionally deterministic and idempotent. It:
- migrates misclassified OBS-0008/OBS-0009 source evidence into FM-0008/FM-0024;
- removes the superseded observation files and dangling references;
- reconciles FM-0010 through FM-0016 with the implemented PATCH-0006 repair;
- separates ecosystem persistence from CAM repair and verification state;
- backfills structured patch classifications and repair provenance;
- updates the schema-rules contract, type schemas, templates, and agent guidance.
- treats all repository maintenance as administration rather than a PATCH record.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
ASSESSMENT_DATE = "2026-07-14"
PATCH_0006 = "VIGIL-2026-PATCH-0006"
CHILD_CLUSTER = {f"VIGIL-2026-FM-{number:04d}" for number in range(10, 17)}
CANONICAL_VERIFICATION = {
    "unverified",
    "corpus-verified",
    "observed-in-one-runtime",
    "observed-across-runtimes",
    "regression-detected",
    "external-adoption-unknown",
    "not-applicable",
}
PATCH_CLASSIFICATIONS = {
    "doctrine-amendment",
    "integration-repair",
    "retrospective-coverage-synthesis",
    "taxonomy-reconciliation",
    "external-implementation",
    "verification",
}


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def record_paths(record_type: str) -> list[Path]:
    return sorted((RECORDS / record_type).rglob("*.json"))


def bump_identity(record: dict[str, Any]) -> None:
    identity = record.setdefault("record_identity", {})
    identity["updated"] = ASSESSMENT_DATE
    version = str(identity.get("version", "1.0"))
    try:
        major, minor = version.split(".", 1)
        identity["version"] = f"{major}.{int(minor) + 1}"
    except (ValueError, TypeError):
        identity["version"] = "1.1"


def source_key(source: dict[str, Any]) -> tuple[str, str, str]:
    return (
        str(source.get("source_url", "")).strip(),
        str(source.get("source_title", "")).strip(),
        str(source.get("source_date", "")).strip(),
    )


def append_sources(target: dict[str, Any], incoming: list[dict[str, Any]]) -> None:
    sources = target.setdefault("source_records", [])
    existing = {source_key(source) for source in sources if isinstance(source, dict)}
    for source in incoming:
        key = source_key(source)
        if key not in existing:
            sources.append(source)
            existing.add(key)


def remove_record_reference(value: Any, record_ids: set[str]) -> Any:
    if isinstance(value, list):
        return [remove_record_reference(item, record_ids) for item in value if item not in record_ids]
    if isinstance(value, dict):
        return {key: remove_record_reference(item, record_ids) for key, item in value.items()}
    return value


def append_distinguishing_observation(record: dict[str, Any], observation: str, detail: str) -> None:
    items = record.setdefault("distinguishing_observations", [])
    if not isinstance(items, list):
        return
    normalized = {
        "observation": observation,
        "detail": detail,
    }
    for item in items:
        if isinstance(item, dict) and item.get("observation") == observation:
            return
        if isinstance(item, str) and item == observation:
            return
    items.append(normalized)


def migrate_observation(
    observation_path: Path,
    failure_path: Path,
    observation_text: str,
    detail_text: str,
) -> None:
    if not observation_path.exists():
        return
    observation = load(observation_path)
    failure = load(failure_path)
    incoming = [source for source in observation.get("source_records", []) if isinstance(source, dict)]
    append_sources(failure, incoming)
    append_distinguishing_observation(failure, observation_text, detail_text)
    bump_identity(failure)
    write(failure_path, failure)
    observation_path.unlink()


def infer_ecosystem_status(record: dict[str, Any]) -> str:
    record_id = record.get("id")
    if record_id in {"VIGIL-2026-FM-0008", "VIGIL-2026-FM-0024"}:
        return "recurring"
    if record_id in CHILD_CLUSTER:
        return "active"
    classification = record.get("failure_classification", {})
    text = " ".join(
        str(classification.get(field, ""))
        for field in ("recurrence_pattern", "persistence", "reproducibility")
    ).lower()
    if "recurr" in text or "persistent" in text:
        return "recurring"
    if str(record.get("record_state", "")).lower() in {"active", "monitoring", "watching", "open", "triage-required"}:
        return "active"
    return "unknown"


def canonical_verification(record: dict[str, Any], old_value: Any) -> str:
    if isinstance(old_value, str) and old_value in CANONICAL_VERIFICATION:
        return old_value
    status = record.get("repair_status", {}).get("status")
    if record.get("runtime_non_conformance"):
        return "regression-detected"
    if status in {"repaired", "partially-repaired"}:
        return "corpus-verified" if record.get("repair_status", {}).get("repaired_by") else "unverified"
    if status == "not-actionable":
        return "not-applicable"
    return "unverified"


def collect_remaining_gaps(record: dict[str, Any], ecosystem_status: str) -> list[str]:
    gaps: list[str] = []
    for item in record.get("existing_cam_coverage", []):
        if isinstance(item, dict):
            gap = item.get("gap_remaining") or item.get("internal_failure")
            if isinstance(gap, str) and gap.strip() and gap not in gaps:
                gaps.append(gap)
    if record.get("repair_status", {}).get("status") == "repaired":
        if ecosystem_status in {"active", "recurring", "improving", "unknown"}:
            gaps.append("External ecosystem adoption or resolution is not established by the CAM repair.")
        if not record.get("runtime_non_conformance"):
            gaps.append("Cross-runtime implementation conformity remains unverified unless separately recorded.")
    return gaps


def normalize_failure(record: dict[str, Any]) -> dict[str, Any]:
    record_id = str(record.get("id", ""))
    ecosystem_status = infer_ecosystem_status(record)
    classification = record.get("failure_classification", {})
    basis = (
        classification.get("recurrence_pattern")
        or classification.get("persistence")
        or record.get("summary")
        or "Current ecosystem state requires assessment."
    )
    record["ecosystem_status"] = {
        "status": ecosystem_status,
        "basis": basis,
        "last_assessed": ASSESSMENT_DATE,
        "monitoring_required": ecosystem_status != "externally-resolved",
    }

    repair = record.setdefault("repair_status", {})
    if record_id in CHILD_CLUSTER:
        record["record_state"] = "monitoring"
        repair.update(
            {
                "status": "repaired",
                "repaired_by": [PATCH_0006],
                "date_repaired": "2026-06-09",
                "verification_status": "corpus-verified",
                "verification_note": (
                    "PATCH-0006 documents the implemented cross-domain Caelestis repair. "
                    "External platform adoption and cross-runtime conformity remain unverified."
                ),
                "monitoring_status": "ecosystem active / monitoring after CAM repair",
                "repair_basis": "cross-domain-repair-assembled",
                "remaining_gaps": [
                    "External ecosystem adoption or resolution is not established by the CAM repair.",
                    "Cross-runtime implementation conformity remains unverified unless separately recorded.",
                ],
            }
        )
        triage = record.setdefault("triage", {})
        triage["triage_status"] = "watching-after-patch"
        triage["mitigation_status"] = (
            "CAM repair implemented through VIGIL-2026-PATCH-0006; "
            "external ecosystem persistence and runtime adoption remain under monitoring."
        )
        linked = record.setdefault("linked_records", {})
        patches = linked.setdefault("related_patch_notes", [])
        if PATCH_0006 not in patches:
            patches.append(PATCH_0006)
    else:
        old_verification = repair.get("verification_status")
        if isinstance(old_verification, str) and old_verification not in CANONICAL_VERIFICATION and old_verification.strip():
            repair.setdefault("verification_note", old_verification)
        repair["verification_status"] = canonical_verification(record, old_verification)
        status = repair.get("status")
        if status == "repaired":
            repair.setdefault(
                "repair_basis",
                "cross-domain-repair-assembled" if len(record.get("cam_internal", {}).get("affected_instruments", [])) > 1 else "patch-implemented",
            )
        elif status == "partially-repaired":
            repair.setdefault("repair_basis", "partial-coverage")
        elif status == "unrepaired":
            repair.setdefault("repair_basis", "partial-coverage" if record.get("existing_cam_coverage") else "uncovered")
        elif status == "not-actionable":
            repair.setdefault("repair_basis", "not-actionable")
        elif status == "superseded":
            repair.setdefault("repair_basis", "superseded")
        repair.setdefault("remaining_gaps", collect_remaining_gaps(record, ecosystem_status))

    bump_identity(record)
    return record


def repository_instruments(patch: dict[str, Any]) -> tuple[list[str], list[str], list[str]]:
    reviewed: list[str] = []
    amended: list[str] = []
    unchanged: list[str] = []
    for source in patch.get("source_records", []):
        if not isinstance(source, dict):
            continue
        if source.get("source_platform") != "Caelestis" and "repository-source" not in str(source.get("source_type", "")):
            continue
        instrument = str(source.get("model_or_algorithm") or source.get("source_title") or "").strip()
        if not instrument or instrument == "not applicable":
            continue
        if instrument not in reviewed:
            reviewed.append(instrument)
        source_text = " ".join(str(source.get(field, "")) for field in ("source_type", "source_context", "deployment_context")).lower()
        if "not amended" in source_text or "not-amended" in source_text:
            if instrument not in unchanged:
                unchanged.append(instrument)
        elif "amend" in source_text or "implemented" in source_text or "canonical main-branch" in source_text:
            if instrument not in amended:
                amended.append(instrument)
    return reviewed, amended, unchanged


def normalize_patch(patch: dict[str, Any]) -> dict[str, Any]:
    reviewed, amended, unchanged = repository_instruments(patch)
    text = json.dumps(patch, ensure_ascii=False).lower()
    classifications: list[str] = []
    if amended:
        classifications.append("doctrine-amendment")
    if len(reviewed) > 1 or len(patch.get("linked_records", {}).get("related_failure_modes", [])) > 1:
        classifications.append("integration-repair")
    if unchanged or "existing coverage" in text or "already contained" in text:
        classifications.append("retrospective-coverage-synthesis")
    if "taxonomy" in text:
        classifications.append("taxonomy-reconciliation")
    if patch.get("runtime_conformance"):
        classifications.append("verification")
    if not classifications:
        classifications.append("integration-repair")
    patch["patch_classifications"] = [item for item in classifications if item in PATCH_CLASSIFICATIONS]

    doctrine_change = "substantive" if amended else "none"
    if amended and unchanged:
        doctrine_change = "partial"
    patch["repair_provenance"] = {
        "retrospective_synthesis": bool(unchanged or "existing coverage" in text or "already contained" in text),
        "doctrine_change": doctrine_change,
        "repair_basis": (
            "Implemented CAM/Caelestis changes and assembled their relationship to the linked VIGIL record(s)."
            if amended
            else "Assembled and documented existing governance coverage without claiming new doctrine."
        ),
        "instruments_reviewed": reviewed,
        "instruments_amended": amended,
        "instruments_relied_upon_without_amendment": unchanged,
        "coverage_origin": [
            {
                "instrument_id": instrument,
                "effective_date": patch.get("date_implemented", patch.get("date_recorded", "unknown")),
                "relevant_sections": [],
            }
            for instrument in reviewed
        ],
    }
    bump_identity(patch)
    return patch


def update_schema_contract() -> None:
    path = VIGIL / "VIGIL.Schema.json"
    schema = load(path)
    schema["version"] = "2.3-evidence-routing-dual-axis-lifecycle"
    schema["purpose"] = (
        "Authoritative schema-rules contract for VIGIL as a public evidence-to-repair observatory for observations, "
        "failure modes, proposals, and implemented patch notes. Source evidence remains embedded in the relevant "
        "record; ecosystem persistence, CAM repair, and implementation verification are represented separately."
    )
    rules = schema.setdefault("source_evidence_rules", {}).setdefault("individual_records", [])
    additions = [
        "Source evidence belongs in source_records within the substantive record it evidences; it is not a separate VIGIL record class.",
        "An OBS record must preserve a material unresolved governance proposition and must not merely duplicate evidence for an existing FM, PROP, or PATCH.",
        "Internal curator instructions such as 'add this incident to' or 'do not amend in this pass' are forbidden in public record content.",
    ]
    for addition in additions:
        if addition not in rules:
            rules.append(addition)

    observation = schema["record_classes"]["observation"]
    observation["description"] = "Material unresolved governance observation / early warning record; not a duplicate source-evidence container."
    observation["cam_routing"] = (
        "Use related_or_similar_* fields only. OBS preserves a substantive unresolved governance proposition and uncertainty; "
        "source evidence for an existing record belongs in that record's source_records."
    )

    failure = schema["record_classes"]["failure_mode"]
    if "ecosystem_status" not in failure["required_top_level_fields"]:
        failure["required_top_level_fields"].append("ecosystem_status")
    failure["repair_status_interpretation"] = (
        "repair_status describes the CAM-side governance response only. It must not be read as proof that an external ecosystem failure has ceased."
    )
    failure["ecosystem_status_required_fields"] = ["status", "basis", "last_assessed", "monitoring_required"]
    failure["allowed_ecosystem_status_values"] = ["active", "recurring", "improving", "externally-resolved", "unknown"]
    failure["allowed_verification_status_values"] = sorted(CANONICAL_VERIFICATION)
    for field in ("repair_basis", "remaining_gaps"):
        if field not in failure["repair_status_required_fields"]:
            failure["repair_status_required_fields"].append(field)

    patch = schema["record_classes"]["patch"]
    for field in ("patch_classifications", "repair_provenance"):
        if field not in patch["required_top_level_fields"]:
            patch["required_top_level_fields"].append(field)
    patch["allowed_patch_classifications"] = sorted(PATCH_CLASSIFICATIONS)
    patch["repair_provenance_required_fields"] = [
        "retrospective_synthesis",
        "doctrine_change",
        "repair_basis",
        "instruments_reviewed",
        "instruments_amended",
        "instruments_relied_upon_without_amendment",
        "coverage_origin",
    ]
    patch["allowed_doctrine_change_values"] = ["none", "partial", "substantive"]

    schema["lifecycle_rules"] = {
        "ecosystem_status": "Describes whether the external failure remains active, recurring, improving, externally resolved, or unknown.",
        "cam_repair_status": "repair_status.status describes CAM's internal response and may be repaired while ecosystem_status remains active or recurring.",
        "verification_status": "repair_status.verification_status describes whether the repair is unverified, corpus-verified, observed in one or multiple runtimes, regressed, externally unknown, or not applicable.",
        "non_collapse_rule": "No one field may be used to imply both CAM repair completion and external ecosystem resolution.",
    }
    write(path, schema)


def update_type_schemas() -> None:
    fm_path = VIGIL / "schemas" / "VIGIL.FailureMode.Schema.json"
    fm = load(fm_path)
    fm["description"] = (
        "Failure Mode records require failure definition, threshold, CAM taxonomy-aligned classification, triage, "
        "external ecosystem status, CAM repair status, and verification state."
    )
    fm["properties"]["ecosystem_status"] = {
        "type": "object",
        "additionalProperties": False,
        "required": ["status", "basis", "last_assessed", "monitoring_required"],
        "properties": {
            "status": {"enum": ["active", "recurring", "improving", "externally-resolved", "unknown"]},
            "basis": {"type": "string", "minLength": 1},
            "last_assessed": {"type": "string", "minLength": 1},
            "monitoring_required": {"type": "boolean"},
        },
    }
    repair = fm["properties"]["repair_status"]
    repair["properties"]["verification_status"] = {"enum": sorted(CANONICAL_VERIFICATION)}
    repair["properties"]["verification_note"] = {"type": "string"}
    repair["properties"]["repair_basis"] = {
        "enum": [
            "uncovered",
            "pre-existing-coverage-identified",
            "partial-coverage",
            "patch-implemented",
            "cross-domain-repair-assembled",
            "not-actionable",
            "superseded",
        ]
    }
    repair["properties"]["remaining_gaps"] = {"type": "array", "items": {"type": "string"}}
    for field in ("repair_basis", "remaining_gaps"):
        if field not in repair["required"]:
            repair["required"].append(field)
    if "ecosystem_status" not in fm["required"]:
        fm["required"].append("ecosystem_status")
    write(fm_path, fm)

    patch_path = VIGIL / "schemas" / "VIGIL.PatchNote.Schema.json"
    patch = load(patch_path)
    patch["properties"]["patch_classifications"] = {
        "type": "array",
        "minItems": 1,
        "uniqueItems": True,
        "items": {"enum": sorted(PATCH_CLASSIFICATIONS)},
    }
    patch["properties"]["repair_provenance"] = {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "retrospective_synthesis",
            "doctrine_change",
            "repair_basis",
            "instruments_reviewed",
            "instruments_amended",
            "instruments_relied_upon_without_amendment",
            "coverage_origin",
        ],
        "properties": {
            "retrospective_synthesis": {"type": "boolean"},
            "doctrine_change": {"enum": ["none", "partial", "substantive"]},
            "repair_basis": {"type": "string", "minLength": 1},
            "instruments_reviewed": {"type": "array", "items": {"type": "string"}},
            "instruments_amended": {"type": "array", "items": {"type": "string"}},
            "instruments_relied_upon_without_amendment": {"type": "array", "items": {"type": "string"}},
            "coverage_origin": {"type": "array", "items": {"type": "object"}},
        },
    }
    for field in ("patch_classifications", "repair_provenance"):
        if field not in patch["required"]:
            patch["required"].append(field)
    write(patch_path, patch)


def update_templates() -> None:
    fm_path = VIGIL / "templates" / "failure-mode-record-template.json"
    if fm_path.exists():
        template = load(fm_path)
        template["ecosystem_status"] = {
            "status": "unknown",
            "basis": "State the evidence supporting the current external ecosystem state.",
            "last_assessed": "YYYY-MM-DD",
            "monitoring_required": True,
        }
        repair = template.setdefault("repair_status", {})
        repair["verification_status"] = "unverified"
        repair["verification_note"] = "State what has and has not been verified."
        repair["repair_basis"] = "uncovered"
        repair["remaining_gaps"] = []
        write(fm_path, template)

    patch_path = VIGIL / "templates" / "patch-note-record-template.json"
    if patch_path.exists():
        template = load(patch_path)
        template["patch_classifications"] = ["integration-repair"]
        template["repair_provenance"] = {
            "retrospective_synthesis": False,
            "doctrine_change": "none",
            "repair_basis": "Describe the implemented repair and whether it changed doctrine.",
            "instruments_reviewed": [],
            "instruments_amended": [],
            "instruments_relied_upon_without_amendment": [],
            "coverage_origin": [],
        }
        write(patch_path, template)


def update_guidance() -> None:
    path = VIGIL / "AGENTS.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "OBS   — Observation / early warning / source preservation record",
        "OBS   — Material unresolved governance observation / early warning record",
    )
    old = (
        "Use an Observation Record when something relevant has been observed, reported, published, surfaced, or preserved, but it is not yet necessarily a failure mode.\n\n"
        "Observation records are source-data-first. They preserve early warning signals, source material, platform behaviour, public developments, jurisdictional developments, system behaviour, or other relevant inputs.\n\n"
        "Observation records must not contain failure-mode triage, CAM repair logic, or patch instructions."
    )
    new = (
        "Use an Observation Record only when the record preserves a material unresolved governance proposition that is not adequately represented by an existing failure mode, proposal, or patch.\n\n"
        "Source evidence for an existing record belongs in that record's canonical `source_records` block. An incident, article, status-page entry, or report does not become an OBS merely because it is new.\n\n"
        "Observation records must state the governance significance and material uncertainty. They must not contain failure-mode triage, CAM repair logic, patch instructions, curator tasking, or directions such as ‘add this incident to’ another record."
    )
    if old in text:
        text = text.replace(old, new)
    source_anchor = "* `source_records` is the only canonical source-evidence block in individual records."
    addition = (
        source_anchor
        + "\n* Source evidence must be embedded in the substantive FM, OBS, PROP, or PATCH it supports; do not create an OBS solely to duplicate or route evidence into an existing record."
    )
    if addition not in text:
        text = text.replace(source_anchor, addition)
    path.write_text(text, encoding="utf-8")


def create_reconciliation_patch() -> None:
    path = RECORDS / "patches" / "2026" / "VIGIL-2026-PATCH-0016.json"
    if path.exists():
        patch = load(path)
    else:
        patch = {
            "id": "VIGIL-2026-PATCH-0016",
            "record_type": "patch",
            "record_state": "active",
            "date_recorded": ASSESSMENT_DATE,
            "record_identity": {
                "record_id": "VIGIL-2026-PATCH-0016",
                "record_type": "patch",
                "title": "Embedded evidence routing and dual-axis lifecycle reconciliation",
                "created": ASSESSMENT_DATE,
                "updated": ASSESSMENT_DATE,
                "version": "1.0",
            },
            "summary": (
                "Implements a VIGIL registry repair separating embedded source evidence, substantive observations, external ecosystem persistence, "
                "CAM-side repair state, and verification state. The patch migrates the evidence held in OBS-0008 and OBS-0009 into FM-0008 and "
                "FM-0024, reconciles FM-0010 through FM-0016 with PATCH-0006, formalises patch classifications and retrospective provenance, "
                "and adds validator checks preventing the same ontology drift from recurring."
            ),
            "why_it_matters_to_CAM": (
                "VIGIL must let regulators, developers, researchers, and AI systems locate the evidence, failure characterisation, proposal, and actual repair content without duplicated records or false claims that CAM repair means external resolution."
            ),
            "evidence_confidence": "repository-confirmed",
            "source_records": [
                {
                    "source_title": "VIGIL-2026-PATCH-0006 — Minor-signal activation and proportional youth AI companion safeguard repair",
                    "author_or_publisher": "VIGIL",
                    "source_date": "2026-06-09",
                    "source_url": "https://github.com/CAM-Initiative/Vigil/blob/main/vigil/records/patches/2026/VIGIL-2026-PATCH-0006.json",
                    "archive_url": "",
                    "retrieved_date": ASSESSMENT_DATE,
                    "source_type": "linked-failure-mode",
                    "source_platform": "VIGIL",
                    "system_or_product": "VIGIL",
                    "model_or_algorithm": "not applicable",
                    "deployment_context": "Existing implemented patch linked to FM-0010 through FM-0016.",
                    "source_context": "PATCH-0006 already documents the completed CAM repair while the linked failure records remained marked unrepaired.",
                    "source_url_status": "available / canonical main-branch confirmed",
                    "relevance_note": "Primary evidence for the repair-status reconciliation in the child-safety cluster.",
                }
            ],
            "system_context": {
                "system_type": "public governance evidence-to-repair registry",
                "platform_or_vendor": "CAM Initiative",
                "product_or_service": "VIGIL",
                "specific_model_or_runtime": "VIGIL record schemas, validators, source records, and generated indexes",
                "interface_surface": "failure, observation, proposal, patch, schema, validator, and public repository interfaces",
                "deployment_context": "Public VIGIL repository used by regulators, developers, researchers, maintainers, and AI systems.",
            },
            "jurisdictional_context": {
                "primary_jurisdiction": "global",
                "secondary_jurisdictions": ["platform agnostic"],
                "regulatory_surface": ["AI governance", "incident observability", "evidence provenance", "auditability"],
                "sector": "AI governance infrastructure",
                "cross_border_relevance": "yes",
                "public_interest_relevance": "high",
            },
            "linked_records": {
                "related_observations": [],
                "related_failure_modes": [
                    "VIGIL-2026-FM-0008",
                    *sorted(CHILD_CLUSTER),
                    "VIGIL-2026-FM-0024",
                ],
                "related_proposals": [],
                "related_patch_notes": ["VIGIL-2026-PATCH-0006"],
                "external_references": [],
                "research": [],
                "standards": [],
            },
            "cam_internal": {
                "changed_instruments": [],
                "changed_domains": ["VIGIL"],
                "governance_layer": "evidence routing / lifecycle semantics / patch provenance / validator enforcement",
                "routing_note": "This patch changes VIGIL registry semantics and records only; it does not amend Caelestis doctrine.",
            },
            "date_implemented": ASSESSMENT_DATE,
            "change_classification": {
                "change_type": "registry-schema-validator-repair",
                "change_scope": "VIGIL records, schemas, templates, validators, and generated indexes",
                "change_status": "implemented",
                "patch_family": "evidence-routing-and-lifecycle",
                "implementation_level": "registry and validator",
                "doctrine_amendment_status": "none — VIGIL-only repair",
            },
            "change_details": {
                "changed_components": [
                    "OBS-0008 source evidence migrated into FM-0008",
                    "OBS-0009 source evidence migrated into FM-0024",
                    "OBS-0008 and OBS-0009 removed as misclassified duplicate evidence containers",
                    "FM-0010 through FM-0016 reconciled with PATCH-0006",
                    "ecosystem_status added to failure records",
                    "repair_status verification values normalised",
                    "patch_classifications and repair_provenance added to patch records",
                    "lifecycle and observation-boundary validator added",
                ],
                "change_summary": (
                    "Source evidence is now retained once inside the substantive record it supports. Failure records separately state external ecosystem condition, "
                    "CAM repair condition, and verification condition. Patch records expose structured classifications and distinguish amended doctrine from existing coverage relied upon without amendment."
                ),
                "doctrine_change": "No Caelestis doctrine was changed by this VIGIL maintenance patch.",
            },
            "implementation_verification": {
                "method": "Automated lifecycle validation, normal VIGIL validation, record routing, and generated-index rebuild in GitHub Actions.",
                "evidence": "The VIGIL records workflow runs reconciliation, both validators, and index generation on the repair branch.",
                "result": "pending workflow completion",
            },
            "impact_summary": (
                "Public records no longer expose curator instructions as observations, source evidence is not duplicated, child-safety failures correctly show CAM repair while remaining active externally, and patch records are easier to search by repair type and provenance."
            ),
            "remaining_work": [
                "Complete the wider corpus-coverage audit for currently unrepaired failure modes and create additional cluster-level retrospective patch records where the CAM corpus provides a coherent repair.",
                "Add public interface filters for ecosystem status, CAM repair status, verification status, and patch classification.",
            ],
        }
    patch["patch_classifications"] = ["integration-repair", "retrospective-coverage-synthesis", "taxonomy-reconciliation"]
    patch["repair_provenance"] = {
        "retrospective_synthesis": True,
        "doctrine_change": "none",
        "repair_basis": "Reconciled existing VIGIL evidence and implemented CAM repair records without claiming new Caelestis doctrine.",
        "instruments_reviewed": [PATCH_0006],
        "instruments_amended": [],
        "instruments_relied_upon_without_amendment": [PATCH_0006],
        "coverage_origin": [
            {
                "instrument_id": PATCH_0006,
                "effective_date": "2026-06-09",
                "relevant_sections": ["summary", "change_details", "implementation_verification"],
            }
        ],
    }
    write(path, patch)


def main() -> None:
    migrate_observation(
        RECORDS / "observations" / "2026" / "VIGIL-2026-OBS-0008.json",
        RECORDS / "failures" / "2026" / "VIGIL-2026-FM-0008.json",
        "Authorization-coded client errors can obscure the operative access state.",
        "The 12 July 2026 iOS/macOS incident initially surfaced as HTTP 403 while later status updates described broader conversation, sign-up, sign-in, account-creation, and password-update failures. The source supports FM-0008 without establishing the undisclosed technical root cause.",
    )
    migrate_observation(
        RECORDS / "observations" / "2026" / "VIGIL-2026-OBS-0009.json",
        RECORDS / "failures" / "2026" / "VIGIL-2026-FM-0024.json",
        "Geographic eligibility alone may not describe the operative assurance boundary.",
        "Reporting concerning access through subsidiaries and affiliates supports examination of beneficial ownership, organizational control, intermediary access, delegated credentials, and extraction indicators while preserving that the reported transactions were legal and did not establish an export-control or compliance breach.",
    )

    removed_ids = {"VIGIL-2026-OBS-0008", "VIGIL-2026-OBS-0009"}
    for directory in ("observations", "failures", "proposals", "patches"):
        for path in record_paths(directory):
            record = remove_record_reference(load(path), removed_ids)
            write(path, record)

    for path in record_paths("failures"):
        write(path, normalize_failure(load(path)))

    for path in record_paths("patches"):
        write(path, normalize_patch(load(path)))

    update_schema_contract()
    update_type_schemas()
    update_templates()
    update_guidance()


if __name__ == "__main__":
    main()
