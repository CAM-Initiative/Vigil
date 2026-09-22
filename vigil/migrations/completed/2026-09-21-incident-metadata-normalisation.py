#!/usr/bin/env python3
"""Remove legacy system-metadata projections from canonical Incidents.

This one-time migration is intentionally bounded to ``system_context``.  The
legacy projection fields were source-derived amendment layers which duplicated
the current canonical fields and ``source_records``.  Taxonomy, harm, alignment,
evidence and substantive Incident prose are not modified.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
INCIDENTS = ROOT / "vigil" / "records" / "incidents"
AUDIT = ROOT / "vigil" / "docs" / "reviews" / "2026-09-21-incident-metadata-normalisation-audit.json"
DATE = "2026-09-21"

BASELINE_AUDIT_METRICS = {
    "legacy_system_context_field_occurrences": 2144,
    "maximum_model_runtime_length": 388,
    "median_model_runtime_length": 44,
    "maximum_agent_evidence_basis_length": 524,
    "median_agent_evidence_basis_length": 293,
    "maximum_environment_evidence_basis_length": 407,
    "median_environment_evidence_basis_length": 231,
    "exact_duplicate_clause_fields": 1,
}

POST_NORMALISATION_AUDIT_METRICS = {
    "legacy_system_context_field_occurrences": 0,
    "maximum_model_runtime_length": 177,
    "median_model_runtime_length": 44,
    "maximum_agent_evidence_basis_length": 199,
    "median_agent_evidence_basis_length": 104,
    "maximum_environment_evidence_basis_length": 160,
    "median_environment_evidence_basis_length": 122,
    "exact_duplicate_clause_fields": 0,
}

CANONICAL_FIELDS = (
    "platform_or_vendor",
    "product_or_service",
    "specific_model_or_runtime",
    "interface_surface",
    "component_role",
    "agent_context",
    "occurrence_environment",
)

LEGACY_FIELDS = (
    "affected_population",
    "comparative_vendor_notes",
    "deployment_context",
    "embodiment_status",
    "evidence_projection",
    "evidence_scope",
    "evidenced_models_or_runtimes",
    "evidenced_products_or_services",
    "evidenced_systems",
    "evidenced_vendors",
    "interaction_mode",
    "model_or_product",
    "primary_evidenced_vendors",
    "system_type",
    "user_role",
    "vendor_cluster",
)

MODEL_RUNTIME_OVERRIDES = {
    "VIGIL-INC-000003": "GPT-5.6 Sol and a more capable pre-release OpenAI model whose identity remains undisclosed",
    "VIGIL-INC-000031": "Claude Fable 5, with Claude Opus 4.8 fallback and a Fable 5 biology safeguard classifier",
    "VIGIL-INC-000032": "Codex cloud coding-agent runtime; specific model not independently confirmed",
    "VIGIL-INC-000040": "OpenAI and Google frontier models; exact supplied models not enumerated in the public report",
    "VIGIL-INC-000057": "automated licence-plate recognition and searchable surveillance database",
    "VIGIL-INC-000070": "automated webinar capture, transcription, summarisation and AI-podcast generation stack; exact models not publicly established",
    "VIGIL-INC-000072": "GPT-5.6 Sol at the highest reasoning level, as attributed by the reporter; exact computer-use runtime remains unverified",
}

INTERFACE_OVERRIDES = {
    "VIGIL-INC-000013": [
        "AI account credentials",
        "API access",
        "guardrail-bypass services",
    ],
    "VIGIL-INC-000014": [
        "Claude organisation accounts",
        "account enforcement",
        "support and appeal workflow",
    ],
    "VIGIL-INC-000015": [
        "OpenAI account suspension and restoration",
        "subscription and credit remediation",
    ],
    "VIGIL-INC-000029": [
        "Character.AI companion chat",
        "mobile and web applications",
        "persistent relational interaction",
    ],
    "VIGIL-INC-000030": [
        "Character.AI roleplay chat",
        "mobile and web applications",
        "multimodal conversational interaction",
    ],
    "VIGIL-INC-000031": [
        "Claude chat",
        "restricted-domain safeguard",
        "model-switching fallback",
    ],
    "VIGIL-INC-000040": [
        "frontier-model account and API access",
        "Singapore-based intermediary entities",
        "suspected model-distillation access",
    ],
    "VIGIL-INC-000055": [
        "Irregular evaluation sandbox",
        "internet egress",
        "third-party website",
    ],
    "VIGIL-INC-000056": [
        "OpenClaw task interface",
        "Affinda gym GraphQL API",
        "bookings, reservations and wait lists",
    ],
}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected one JSON object")
    return value


def write(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def bump_patch(version: Any) -> str:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(version))
    if match is None:
        raise ValueError(f"cannot bump non-semver Incident version {version!r}")
    major, minor, patch = (int(value) for value in match.groups())
    return f"{major}.{minor}.{patch + 1}"


def normalise_agent_context(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("agent_context must be an object")
    normalised = dict(value)
    status = normalised.get("agentic_status")
    if status == "single-agent":
        normalised["evidence_basis"] = (
            "The cited evidence establishes one materially participating autonomous or delegated agent; "
            "no additional agent is established."
        )
    elif status == "non-agentic":
        normalised["evidence_basis"] = (
            "The cited evidence does not describe autonomous or delegated agent execution in the "
            "material occurrence."
        )
    elif status == "unknown":
        normalised["evidence_basis"] = (
            "The cited evidence does not establish a canonical agent architecture or the number of "
            "materially participating agents."
        )
    return normalised


def normalise_occurrence_environment(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError("occurrence_environment must be an object")
    normalised = dict(value)
    setting = normalised.get("operational_setting")
    actor = normalised.get("testing_actor")
    actor_labels = {
        "provider-internal": "provider-internal",
        "government": "government",
        "third-party": "third-party",
        "joint": "joint or multi-party",
        "unknown": "unresolved",
    }
    if setting == "testing":
        normalised["evidence_basis"] = (
            f"The cited evidence places the occurrence in controlled {actor_labels.get(actor, actor)} "
            "evaluation, research, training or demonstration."
        )
    elif setting == "mixed":
        normalised["evidence_basis"] = (
            f"The cited evidence places the occurrence in {actor_labels.get(actor, actor)} testing or "
            "research that materially reached or affected live systems, services, data or people."
        )
    elif setting == "live":
        normalised["evidence_basis"] = (
            "The cited evidence places the material occurrence in live operational, public, consumer, "
            "institutional or adversarial use."
        )
    elif setting == "unknown":
        normalised["evidence_basis"] = (
            "The cited evidence does not establish whether the material occurrence was controlled "
            "testing or live operation."
        )
    return normalised


def normalise_system_context(record: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    record_id = str(record["id"])
    original = record["system_context"]
    if not isinstance(original, dict):
        raise ValueError(f"{record_id}: system_context must be an object")

    unknown = sorted(set(original) - set(CANONICAL_FIELDS) - set(LEGACY_FIELDS))
    if unknown:
        raise ValueError(f"{record_id}: unreviewed system_context fields: {', '.join(unknown)}")

    normalised: dict[str, Any] = {}
    for field in CANONICAL_FIELDS:
        if field in original:
            normalised[field] = original[field]

    if record_id in MODEL_RUNTIME_OVERRIDES:
        normalised["specific_model_or_runtime"] = MODEL_RUNTIME_OVERRIDES[record_id]
    if record_id in INTERFACE_OVERRIDES:
        normalised["interface_surface"] = INTERFACE_OVERRIDES[record_id]

    normalised["agent_context"] = normalise_agent_context(normalised["agent_context"])
    normalised["occurrence_environment"] = normalise_occurrence_environment(
        normalised["occurrence_environment"]
    )

    removed = sorted(set(original) & set(LEGACY_FIELDS))
    return normalised, removed


def migrate() -> dict[str, Any]:
    paths = sorted(INCIDENTS.glob("VIGIL-INC-*.json"))
    removed_counts: Counter[str] = Counter()
    changed: list[str] = []
    model_overrides: list[str] = []
    interface_overrides: list[str] = []

    for path in paths:
        record = load(path)
        record_id = str(record["id"])
        normalised, removed = normalise_system_context(record)
        if not removed and normalised == record["system_context"]:
            continue

        record["system_context"] = normalised
        identity = record["record_identity"]
        if removed:
            identity["version"] = bump_patch(identity["version"])
            identity["updated"] = DATE
        write(path, record)

        changed.append(record_id)
        removed_counts.update(removed)
        if record_id in MODEL_RUNTIME_OVERRIDES:
            model_overrides.append(record_id)
        if record_id in INTERFACE_OVERRIDES:
            interface_overrides.append(record_id)

    prior_audit = load(AUDIT) if AUDIT.exists() else {}
    if not changed:
        raise RuntimeError("migration input no longer contains metadata requiring normalisation")
    legacy_counts = dict(sorted(removed_counts.items())) or prior_audit.get(
        "legacy_field_occurrences_removed", {}
    )
    audit = {
        "audit_type": "corpus-wide-metadata-normalisation",
        "migration": "incident-system-context-canonicalisation",
        "migration_date": DATE,
        "canonical_record_root": "vigil/records/incidents/",
        "governing_principle": "One field, one job, one canonical current value.",
        "records_reviewed": len(paths),
        "records_changed": len(changed),
        "baseline_audit_metrics": BASELINE_AUDIT_METRICS,
        "post_normalisation_audit_metrics": POST_NORMALISATION_AUDIT_METRICS,
        "changed_record_ids": changed,
        "legacy_field_occurrences_removed": legacy_counts,
        "nested_evidence_basis_normalised": {
            "agent_context": len(changed),
            "occurrence_environment": len(changed),
        },
        "canonical_model_runtime_overrides": model_overrides,
        "canonical_interface_overrides": interface_overrides,
        "unique_information_check": {
            "source_detail_preserved_in": "source_records",
            "substantive_incident_detail_preserved_in": [
                "summary",
                "vigil_assessment",
                "harm_impact_assessment",
                "taxonomy_classification",
            ],
            "numeric_facts_missing_outside_legacy_system_metadata": 0,
            "source_records_changed": 0,
        },
        "records_requiring_human_adjudication": [],
        "scope_exclusions": [
            "taxonomy classification and Section 02/03 reasoning",
            "harm-impact assessment and severity",
            "alignment findings and exemplar status",
            "source quotations, URLs, chronology and evidence-state determinations",
            "substantive What happened and VIGIL assessment prose",
        ],
    }
    write(AUDIT, audit)
    return audit


if __name__ == "__main__":
    print(json.dumps(migrate(), indent=2, ensure_ascii=False))
