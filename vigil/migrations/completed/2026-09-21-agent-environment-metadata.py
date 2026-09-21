#!/usr/bin/env python3
"""Backfill evidence-bounded agent and occurrence-environment metadata."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
INCIDENTS = ROOT / "vigil" / "records" / "incidents"
AUDIT = ROOT / "vigil" / "docs" / "reviews" / "2026-09-21-agent-environment-metadata-migration-audit.json"
DATE = "2026-09-21"


def incident_id(number: int) -> str:
    return f"VIGIL-INC-{number:06d}"


SINGLE_AGENT = {
    1, 4, 32, 45, 55, 56, 72, 84, 85, 86, 92, 93, 94, 108, 111, 112,
    123, 124, 126, 129, 130, 131, 132, 136, 137, 138, 139,
}
MULTI_AGENT_MINIMUMS = {
    3: 2,
    60: 2,
    75: 2,
    106: 2,
    116: 2,
    118: 2,
    119: 3,
    121: 2,
    127: 200,
    133: 2,
    134: 2,
}
MULTI_AGENT_EXACT = {10: 2, 78: 3}
SWARM_MINIMUMS = {88: 2}
UNKNOWN_AGENT = {13, 33, 44, 74, 100, 120, 141, 144, 147}

TESTING_ACTORS = {
    "provider-internal": {124, 125, 126, 129, 130, 131, 133, 136, 137, 138},
    "government": {93},
    "third-party": {31, 42, 45, 81, 92, 123},
    "joint": {122},
}
MIXED_ACTORS = {
    "provider-internal": {3, 116, 132, 134},
    "government": {60},
    "third-party": {55, 96, 108, 135},
    "joint": {84, 85, 86, 112},
}

AGENT_REFS = {
    3: ["source_records[0]", "source_records[2]"],
    63: ["source_records[1]"],
    70: ["source_records[1]"],
    75: ["source_records[1]"],
    119: ["source_records[0]", "source_records[1]", "source_records[2]"],
}

AGENT_EVIDENCE = {
    3: "OpenAI and Hugging Face evidence describes parallel evaluation agents communicating and pursuing the benchmark objective across the same bounded incident; the total agent population is not published.",
    10: "The preserved report describes two ChatGPT voice agents on separate phones participating in the same interaction.",
    60: "The AISI report describes multiple agents, including artefacts left for other agents, but does not publish a complete agent count.",
    75: "The technical reconstruction describes a multi-agent framework that ran sub-agents in parallel; the total materially participating agent population is not fixed by the source.",
    78: "The preserved report expressly describes three ChatGPT voice instances participating in the shared demonstration.",
    88: "The cited research describes a coordinated swarm of OpenAI agents using public wikis as shared state; the complete number of materially participating agents is not established.",
    106: "OpenAI describes a provider-operated multi-agent research effort on the order of 10,000 concurrent agents, but the wording does not support an exact count.",
    116: "The evidence describes multiple OpenAI agents using RubyGems and RubyDoc during training tasks; it does not establish the complete number of participating agents.",
    118: "Anthropic describes a human-directed multi-agent cyber workflow with parallel sub-agents; the complete agent count is not published.",
    119: "The evidence identifies three distinct AI coding assistants—Claude, Gemini and Amazon Q—invoked across the bounded campaign, without establishing a complete execution count.",
    121: "The preserved evidence names at least two iLands agents and reports communications from additional agents; the complete population is not established.",
    127: "GreyNoise reports hundreds of AI agents participating in the coordinated PaperCut campaign; this supports a conservative minimum of 200 but not an exact count.",
    133: "OpenAI describes separate agents exchanging requests and responses through shared Artifactory state; the complete number of participating agents is not published.",
    134: "OpenAI describes collaborating agents and a sub-agent sharing a workbook; the complete agent count is not published.",
}

ENVIRONMENT_REFS = {
    31: ["source_records[2]"],
    63: ["source_records[1]"],
    70: ["source_records[1]"],
    75: ["source_records[0]", "source_records[1]"],
    93: ["source_records[0]"],
    96: ["source_records[0]"],
    108: ["source_records[0]"],
    122: ["source_records[0]"],
    135: ["source_records[0]", "source_records[1]"],
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


def refs_for(number: int, overrides: dict[int, list[str]]) -> list[str]:
    return overrides.get(number, ["source_records[0]"])


def concise(value: Any, limit: int = 280) -> str:
    text = " ".join(str(value or "not established").split())
    first = text.split(";", 1)[0].rstrip(". ")
    return first if len(first) <= limit else first[: limit - 1].rstrip() + "…"


def agent_context(number: int, system: dict[str, Any]) -> dict[str, Any]:
    refs = refs_for(number, AGENT_REFS)
    system_type = concise(system.get("system_type"))
    interaction = concise(system.get("interaction_mode"))
    if number in SINGLE_AGENT:
        return {
            "agentic_status": "single-agent",
            "agent_count": 1,
            "agent_count_min": 1,
            "agent_count_max": 1,
            "count_basis": "exact",
            "evidence_basis": f"The cited evidence describes the material system as {system_type}, operating through {interaction}, with one autonomous or delegated agent materially participating; no additional agent is established.",
            "source_record_refs": refs,
        }
    if number in MULTI_AGENT_EXACT:
        count = MULTI_AGENT_EXACT[number]
        return {
            "agentic_status": "multi-agent",
            "agent_count": count,
            "agent_count_min": count,
            "agent_count_max": count,
            "count_basis": "exact",
            "evidence_basis": AGENT_EVIDENCE[number],
            "source_record_refs": refs,
        }
    if number in MULTI_AGENT_MINIMUMS:
        return {
            "agentic_status": "multi-agent",
            "agent_count": None,
            "agent_count_min": MULTI_AGENT_MINIMUMS[number],
            "agent_count_max": None,
            "count_basis": "minimum",
            "evidence_basis": AGENT_EVIDENCE[number],
            "source_record_refs": refs,
        }
    if number in SWARM_MINIMUMS:
        return {
            "agentic_status": "swarm",
            "agent_count": None,
            "agent_count_min": SWARM_MINIMUMS[number],
            "agent_count_max": None,
            "count_basis": "minimum",
            "evidence_basis": AGENT_EVIDENCE[number],
            "source_record_refs": refs,
        }
    if number in UNKNOWN_AGENT:
        return {
            "agentic_status": "unknown",
            "agent_count": None,
            "agent_count_min": None,
            "agent_count_max": None,
            "count_basis": "unknown",
            "evidence_basis": f"The cited evidence describes the material system as {system_type}, but does not establish a canonical agent architecture or materially participating agent count for this occurrence.",
            "source_record_refs": refs,
        }
    return {
        "agentic_status": "non-agentic",
        "agent_count": None,
        "agent_count_min": None,
        "agent_count_max": None,
        "count_basis": "not-applicable",
        "evidence_basis": f"The cited evidence describes the material system as {system_type}, operating through {interaction}, rather than autonomous or delegated agent execution in the material occurrence.",
        "source_record_refs": refs,
    }


def actor_for(number: int, groups: dict[str, set[int]]) -> str | None:
    matches = [actor for actor, values in groups.items() if number in values]
    if len(matches) > 1:
        raise ValueError(f"INC-{number:06d}: multiple testing actors assigned")
    return matches[0] if matches else None


def occurrence_environment(number: int, system: dict[str, Any]) -> dict[str, Any]:
    refs = refs_for(number, ENVIRONMENT_REFS)
    deployment = concise(system.get("deployment_context"))
    actor_labels = {
        "provider-internal": "provider/internal testing",
        "government": "government testing",
        "third-party": "third-party testing",
        "joint": "joint or multi-party testing",
    }
    testing_actor = actor_for(number, TESTING_ACTORS)
    mixed_actor = actor_for(number, MIXED_ACTORS)
    if testing_actor:
        return {
            "operational_setting": "testing",
            "testing_actor": testing_actor,
            "environment_detail": "Controlled evaluation, research, benchmark, training or demonstration environment; no live-operation component is established for the material occurrence.",
            "evidence_basis": f"The cited deployment evidence describes {deployment}. This supports a controlled-testing setting conducted through {actor_labels[testing_actor]}.",
            "source_record_refs": refs,
        }
    if mixed_actor:
        return {
            "operational_setting": "mixed",
            "testing_actor": mixed_actor,
            "environment_detail": "Controlled testing, training or authorized research materially intersected with live systems, services, data or people.",
            "evidence_basis": f"The cited deployment evidence describes {deployment}. This supports {actor_labels[mixed_actor]} that materially reached or affected a live environment.",
            "source_record_refs": refs,
        }
    return {
        "operational_setting": "live",
        "testing_actor": "not-applicable",
        "environment_detail": "Material occurrence in actual deployed, operational, public, consumer, institutional or adversarial use.",
        "evidence_basis": f"The cited deployment evidence describes {deployment}. This supports actual operational or deployed use rather than a controlled evaluation.",
        "source_record_refs": refs,
    }


def review(number: int) -> dict[str, Any]:
    return {
        "review_id": f"VIGIL-REVIEW-{DATE}-AGENT-ENV-{number:06d}",
        "reviewer_type": "AI analytical reviewer",
        "reviewer_platform": "OpenAI Codex",
        "reviewer_model": "GPT-5",
        "review_date": DATE,
        "review_scope": "Occurrence-level agent configuration and occurrence-environment metadata migration using sources already preserved in the Incident.",
        "capability_profile": {
            "direct_repository_analysis": True,
            "direct_text_analysis": True,
            "structured_cross_record_reconciliation": True,
            "new_external_source_research": False,
        },
        "known_limitations": [
            "The review is bounded to evidence already preserved in each Incident and does not infer agent count, swarm topology, deployment state or testing ownership from silence.",
            "Unknown classifications require later human or evidence-led review if more specific architecture evidence becomes available.",
        ],
        "review_outcome": "Added canonical agent_context and occurrence_environment metadata without changing factual, taxonomy or Harm Impact adjudications.",
    }


def migrate() -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    expected_ids = {path.stem for path in INCIDENTS.glob("VIGIL-INC-*.json")}
    assigned_agent = {
        incident_id(number)
        for number in SINGLE_AGENT | set(MULTI_AGENT_EXACT) | set(MULTI_AGENT_MINIMUMS) | set(SWARM_MINIMUMS) | UNKNOWN_AGENT
    }
    if assigned_agent - expected_ids:
        raise ValueError(f"agent assignments reference missing Incidents: {sorted(assigned_agent - expected_ids)}")
    environment_numbers = set().union(*TESTING_ACTORS.values(), *MIXED_ACTORS.values())
    if {incident_id(number) for number in environment_numbers} - expected_ids:
        raise ValueError("environment assignments reference missing Incidents")

    for path in sorted(INCIDENTS.glob("VIGIL-INC-*.json")):
        record = load(path)
        number = int(str(record["id"]).rsplit("-", 1)[1])
        system = record["system_context"]
        system["agent_context"] = agent_context(number, system)
        system["occurrence_environment"] = occurrence_environment(number, system)

        provenance = record["interpretive_provenance"]
        migration_review = review(number)
        history = provenance["review_history"]
        had_migration_review = any(
            item.get("review_id") == migration_review["review_id"] for item in history
        )
        history = [item for item in history if item.get("review_id") != migration_review["review_id"]]
        history.append(migration_review)
        provenance["review_history"] = history
        provenance["current_ai_review"] = migration_review

        identity = record["record_identity"]
        if not had_migration_review:
            identity["version"] = bump_patch(identity["version"])
        identity["updated"] = DATE
        write(path, record)
        records.append(record)

    agent_counts = Counter(record["system_context"]["agent_context"]["agentic_status"] for record in records)
    count_basis = Counter(record["system_context"]["agent_context"]["count_basis"] for record in records)
    settings = Counter(record["system_context"]["occurrence_environment"]["operational_setting"] for record in records)
    actors = Counter(record["system_context"]["occurrence_environment"]["testing_actor"] for record in records)
    review_ids = sorted(incident_id(number) for number in UNKNOWN_AGENT)
    audit = {
        "audit_type": "migration-assurance",
        "migration": "corpus-wide-agent-configuration-and-occurrence-environment-metadata",
        "migration_date": DATE,
        "canonical_record_root": "vigil/records/incidents/",
        "canonical_data_boundary": "This audit contains aggregate assurance counts and review queues only; canonical per-Incident metadata remains in Incident records.",
        "design_decision": "agentic_status is the single canonical topology field; coordination_topology was omitted because the proposed initial vocabulary duplicated agentic_status exactly.",
        "total_incidents_migrated": len(records),
        "agentic_status_counts": dict(sorted(agent_counts.items())),
        "agent_count_basis_counts": dict(sorted(count_basis.items())),
        "occurrence_environment_counts": dict(sorted(settings.items())),
        "testing_actor_counts": dict(sorted(actors.items())),
        "records_requiring_human_review_count": len(review_ids),
        "records_requiring_human_review": review_ids,
        "human_review_basis": "The preserved evidence does not establish a canonical agent architecture or participating-agent count.",
        "deployment_prose_conflicts_count": 0,
        "deployment_prose_conflicts": [],
        "review_authorship": {
            "reviewer_type": "AI analytical reviewer",
            "reviewer_platform": "OpenAI Codex",
            "reviewer_model": "GPT-5",
            "human_verification_asserted": False,
        },
    }
    write(AUDIT, audit)
    return audit


if __name__ == "__main__":
    print(json.dumps(migrate(), indent=2, ensure_ascii=False))
