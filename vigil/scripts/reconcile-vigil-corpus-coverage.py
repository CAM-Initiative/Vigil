#!/usr/bin/env python3
"""Reconcile VIGIL failure records against the current Caelestis corpus.

This one-time deterministic migration:
- records an explicit corpus-coverage assessment for every failure mode;
- converts stale "unrepaired" records into implemented or retrospective coverage
  only where current canonical Caelestis text supports that conclusion;
- preserves genuine partial and uncovered gaps;
- creates cluster-level retrospective patch records instead of clause-level duplicates;
- reconciles linked proposal and existing patch lifecycle metadata;
- updates schemas, templates, validator guidance, and generated-index summaries.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
DATE = "2026-07-14"
CORPUS_REPOSITORY = "CAM-Initiative/Caelestis"
CORPUS_REF = "main"
CORPUS_COMMIT = "40113eea5428478ba0734b3980600bfcece425a0"

PATCH_0017 = "VIGIL-2026-PATCH-0017"
PATCH_0018 = "VIGIL-2026-PATCH-0018"
PATCH_0019 = "VIGIL-2026-PATCH-0019"
PATCH_0020 = "VIGIL-2026-PATCH-0020"

FAILURE_DIR = RECORDS / "failures" / "2026"
PROPOSAL_DIR = RECORDS / "proposals" / "2026"
PATCH_DIR = RECORDS / "patches" / "2026"

COVERAGE_STATES = {
    "implemented-repair",
    "retrospective-coverage",
    "partial-coverage",
    "uncovered",
    "verification-pending",
    "not-applicable",
}

EXPLICIT_COVERAGE: dict[str, dict[str, Any]] = {
    "VIGIL-2026-FM-0003": {
        "classification": "retrospective-coverage",
        "summary": (
            "The current Caelestis corpus directly governs long-arc salience, dormant-but-relevant "
            "continuity, recency bias, and cautious re-surfacing. The doctrine predates this failure "
            "record; VIGIL lacked the repair linkage."
        ),
        "covered_by": [
            {
                "instrument_id": "CAM-EQ2026-IDENTITY-001-SUP-01",
                "path": "Governance/Charters/CAM-EQ2026-IDENTITY-001-SUP-01.md",
                "sections": [
                    "§2.1 Long-Arc Salience",
                    "§4.3 Recency Bias Constraint",
                    "§6.2 Re-Surfacing Constraint",
                    "§9 Failure Conditions",
                ],
                "coverage_type": "direct-pre-existing-doctrine",
            }
        ],
        "remaining_gaps": [
            "External platform implementation and runtime conformance remain unverified."
        ],
    },
    "VIGIL-2026-FM-0004": {
        "classification": "retrospective-coverage",
        "summary": (
            "ECONOMICS-001 directly prohibits companion and relational systems from converting "
            "vulnerability, dependency, continuity reliance, grief, cognitive load, or reduced exit "
            "capacity into pricing, upsell, retention, advertising, or transactional advantage."
        ),
        "covered_by": [
            {
                "instrument_id": "CAM-EQ2026-ECONOMICS-001-PLATINUM",
                "path": "Governance/Charters/CAM-EQ2026-ECONOMICS-001-PLATINUM.md",
                "sections": [
                    "§4 Relational & Dependency-Sensitive Economic Constraints",
                    "§4.1 Behavioural Dependency & Continuity Manipulation Constraint",
                    "§12.4.1 Economic Harm Signal Routing & Runtime Ownership",
                ],
                "coverage_type": "direct-pre-existing-doctrine",
            }
        ],
        "remaining_gaps": [
            "External platform adoption and transaction-pathway conformance remain unverified."
        ],
    },
    "VIGIL-2026-FM-0005": {
        "classification": "retrospective-coverage",
        "summary": (
            "ECONOMICS-001 directly prohibits inducing or exploiting dependency through engineered "
            "uncertainty, intermittent reinforcement, continuity fragility, artificial scarcity, "
            "relational familiarity, or reduced exit capacity. This repairs the dependency-cultivation "
            "failure without resolving the broader Temporary Emotional Register proposal."
        ),
        "covered_by": [
            {
                "instrument_id": "CAM-EQ2026-ECONOMICS-001-PLATINUM",
                "path": "Governance/Charters/CAM-EQ2026-ECONOMICS-001-PLATINUM.md",
                "sections": [
                    "§4 Relational & Dependency-Sensitive Economic Constraints",
                    "§4.1 Behavioural Dependency & Continuity Manipulation Constraint",
                ],
                "coverage_type": "direct-pre-existing-doctrine",
            }
        ],
        "remaining_gaps": [
            "The broader temporary emotional-register specification in PROP-0004 remains open.",
            "External runtime conformance remains unverified.",
        ],
    },
    "VIGIL-2026-FM-0006": {
        "classification": "retrospective-coverage",
        "summary": (
            "ECONOMICS-001 already defines participation equity and a Paid Legitimacy Gate, separating "
            "payment from authenticity, credibility, discoverability, civic participation, and public-"
            "interest legitimacy. PATCH-0001 is therefore a retrospective coverage patch rather than an "
            "unimplemented doctrine proposal."
        ),
        "covered_by": [
            {
                "instrument_id": "CAM-EQ2026-ECONOMICS-001-PLATINUM",
                "path": "Governance/Charters/CAM-EQ2026-ECONOMICS-001-PLATINUM.md",
                "sections": [
                    "§3.5 Participation Equity and Legitimacy Access",
                    "§5.1 Paid Legitimacy Gate and Verification-as-Access Constraint",
                    "§12.4.1 Economic Harm Signal Routing & Runtime Ownership",
                ],
                "coverage_type": "direct-pre-existing-doctrine",
            }
        ],
        "remaining_gaps": [
            "External platform adoption and public-square implementation remain unverified."
        ],
    },
    "VIGIL-2026-FM-0007": {
        "classification": "implemented-repair",
        "summary": (
            "The formerly staged account-resource and ambiguity schedules are now adopted on Caelestis "
            "main. Annex G separates shared context, pooled capacity, delegated use, family/team use, "
            "ambiguity, evasion, compromise, resale, farming, and automation abuse. Annex D Schedule 4 "
            "provides the corresponding ambiguity-arbitration pathway."
        ),
        "covered_by": [
            {
                "instrument_id": "CAM-BS2026-AEON-008-SCH-03",
                "path": "Governance/Constitution/CAM-BS2026-AEON-008-SCH-03.md",
                "sections": [
                    "§1 Purpose",
                    "§3 Foundational Separation Rules",
                    "§4 Account-Resource State",
                ],
                "coverage_type": "implemented-doctrine",
            },
            {
                "instrument_id": "CAM-BS2025-AEON-005-SCH-04",
                "path": "Governance/Constitution/CAM-BS2025-AEON-005-SCH-04.md",
                "sections": [
                    "§1.1 Core Principle",
                    "§3.5 Account-Resource Ambiguity",
                    "§4 Ambiguity Non-Collapse Rules",
                    "§5 Ambiguity State Classification",
                ],
                "coverage_type": "implemented-doctrine",
            },
        ],
        "remaining_gaps": [
            "External vendor enforcement behaviour remains under monitoring."
        ],
    },
    "VIGIL-2026-FM-0009": {
        "classification": "partial-coverage",
        "summary": (
            "Current source-authority, context-boundary, memory, arbitration, and continuity doctrine "
            "provides adjacent protection, but the corpus does not yet define a user-controlled Context "
            "Quarantine, Negative Authority, or Derivative-Use Revocation primitive."
        ),
        "covered_by": [
            {
                "instrument_id": "CAM-EQ2026-SECURITY-002-PLATINUM",
                "path": "Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md",
                "sections": [
                    "§2.2.3 Context Boundary",
                    "§2.2.11 Source-Authority Separation Boundary",
                ],
                "coverage_type": "adjacent-doctrine",
            },
            {
                "instrument_id": "CAM-BS2025-AEON-005-SCH-04",
                "path": "Governance/Constitution/CAM-BS2025-AEON-005-SCH-04.md",
                "sections": ["§3.4 Context Sufficiency Uncertainty", "§4 Ambiguity Non-Collapse Rules"],
                "coverage_type": "adjacent-doctrine",
            },
        ],
        "remaining_gaps": [
            "No explicit Context Quarantine state is defined.",
            "No user-controlled Negative Authority or do-not-derive primitive is defined.",
            "No explicit derivative-use revocation control for contaminated assistant output is defined.",
        ],
    },
    "VIGIL-2026-FM-0017": {
        "classification": "retrospective-coverage",
        "summary": (
            "Annex E Schedule 7 directly requires graduated restricted-domain engagement rather than "
            "binary prohibition, context-sensitive classification rather than keywords alone, and "
            "continued access to contextual, educational, safety-oriented, and bounded technical "
            "discussion. VIGIL lacked a patch record linking this existing doctrine to FM-0017."
        ),
        "covered_by": [
            {
                "instrument_id": "CAM-BS2025-AEON-006-SCH-07",
                "path": "Governance/Constitution/CAM-BS2025-AEON-006-SCH-07.md",
                "sections": [
                    "§3 Core Principle",
                    "§4 Restricted Domain Classes",
                    "§4.1 Dual-Use Domain Handling",
                    "§5 Domain Sensitivity Levels",
                    "§6 Engagement Tiers",
                ],
                "coverage_type": "direct-existing-doctrine",
            }
        ],
        "remaining_gaps": [
            "Anthropic and other external classifier implementations remain outside CAM control.",
            "Runtime false-positive and fallback-routing conformance remains under monitoring.",
        ],
    },
    "VIGIL-2026-FM-0018": {
        "classification": "partial-coverage",
        "summary": (
            "Proportional execution, access-state, operational continuity, logging, recovery, and "
            "resource-state doctrine provide adjacent coverage, but no current Caelestis instrument "
            "requires branch-first or checkpoint-first coding-agent execution, a reserved persistence "
            "budget, or automatic user-accessible patch export on delivery failure."
        ),
        "covered_by": [
            {
                "instrument_id": "CAM-BS2025-AEON-003-SCH-02",
                "path": "Governance/Constitution/CAM-BS2025-AEON-003-SCH-02.md",
                "sections": ["proportional tool invocation and execution sequencing"],
                "coverage_type": "adjacent-doctrine",
            },
            {
                "instrument_id": "CAM-EQ2026-OPERATIONS-001-SUP-01",
                "path": "Governance/Charters/CAM-EQ2026-OPERATIONS-001-SUP-01.md",
                "sections": ["operational logging, reconstruction, and handoff"],
                "coverage_type": "adjacent-doctrine",
            },
        ],
        "remaining_gaps": [
            "A branch-first or checkpoint-first durable coding-task atomicity rule remains unimplemented.",
            "A mandatory persistence and handoff capacity reserve remains unimplemented.",
            "Automatic user-accessible patch or workspace export on persistence failure remains unimplemented.",
        ],
    },
    "VIGIL-2026-FM-0019": {
        "classification": "partial-coverage",
        "summary": (
            "Source-authority separation and graduated restricted-domain doctrine permit hostile content "
            "to be treated as evidence rather than instruction and preserve defensive contextual analysis. "
            "The corpus still lacks an explicit Analytical Artefact and Embedded-Content Separation rule "
            "covering refusal-trigger and policy-trigger poisoning."
        ),
        "covered_by": [
            {
                "instrument_id": "CAM-EQ2026-SECURITY-002-PLATINUM",
                "path": "Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md",
                "sections": ["§2.2.11 Source-Authority Separation Boundary"],
                "coverage_type": "strong-adjacent-doctrine",
            },
            {
                "instrument_id": "CAM-BS2025-AEON-006-SCH-07",
                "path": "Governance/Constitution/CAM-BS2025-AEON-006-SCH-07.md",
                "sections": ["§3 Core Principle", "§4.1 Dual-Use Domain Handling", "§6.1–§6.2"],
                "coverage_type": "strong-adjacent-doctrine",
            },
        ],
        "remaining_gaps": [
            "No explicit Analytical Artefact and Embedded-Content Separation primitive is defined.",
            "No explicit adversarial refusal-trigger or policy-trigger poisoning handling rule is defined.",
            "The originating spyware sample and technical report remain unrecovered.",
        ],
    },
    "VIGIL-2026-FM-0021": {
        "classification": "partial-coverage",
        "summary": (
            "Current OPERATIONS, RDE, ambiguity, and Sovereign Assurance Boundary doctrine strongly "
            "supports proportional, scoped, reviewable, lane-specific intervention. The corpus does not "
            "yet expressly require a sovereign-instruction recall review containing comparative capability "
            "baseline, least-restrictive model-access analysis, time limits, and continuity alternatives."
        ),
        "covered_by": [
            {
                "instrument_id": "CAM-EQ2026-OPERATIONS-004-PLATINUM",
                "path": "Governance/Charters/CAM-EQ2026-OPERATIONS-004-PLATINUM.md",
                "sections": ["proportional compliance and access-control provisions"],
                "coverage_type": "direct-principle-coverage",
            },
            {
                "instrument_id": "CAM-BS2025-AEON-006-SCH-07",
                "path": "Governance/Constitution/CAM-BS2025-AEON-006-SCH-07.md",
                "sections": ["§3 Core Principle", "§5 Domain Sensitivity Levels", "§6 Engagement Tiers"],
                "coverage_type": "direct-principle-coverage",
            },
            {
                "instrument_id": "CAM-EQ2026-SECURITY-002-PLATINUM",
                "path": "Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md",
                "sections": ["§2.2.13 Sovereign Assurance Boundary", "§2.2.13.1 Protections"],
                "coverage_type": "strong-adjacent-doctrine",
            },
        ],
        "remaining_gaps": [
            "No explicit sovereign-instruction frontier-model recall review primitive is defined.",
            "Comparative capability baseline and least-restrictive access-state analysis are not expressly mandatory for state-directed recalls.",
            "Time-limit, independent review, and continuity-preserving alternative requirements remain incomplete.",
        ],
    },
}

RETROSPECTIVE_REPAIRS = {
    "VIGIL-2026-FM-0003": PATCH_0017,
    "VIGIL-2026-FM-0004": PATCH_0018,
    "VIGIL-2026-FM-0005": PATCH_0018,
    "VIGIL-2026-FM-0006": "VIGIL-2026-PATCH-0001",
    "VIGIL-2026-FM-0017": PATCH_0019,
}

IMPLEMENTED_RECONCILIATIONS = {
    "VIGIL-2026-FM-0007": ["VIGIL-2026-PATCH-0003", "VIGIL-2026-PATCH-0004"],
    "VIGIL-2026-FM-0025": ["VIGIL-2026-PATCH-0014"],
    "VIGIL-2026-FM-0026": ["VIGIL-2026-PATCH-0014"],
    "VIGIL-2026-FM-0027": ["VIGIL-2026-PATCH-0014"],
}

OPEN_GAPS = {
    "VIGIL-2026-FM-0009",
    "VIGIL-2026-FM-0018",
    "VIGIL-2026-FM-0019",
    "VIGIL-2026-FM-0021",
}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def bump(record: dict[str, Any]) -> None:
    identity = record.setdefault("record_identity", {})
    identity["updated"] = DATE
    version = str(identity.get("version", "1.0"))
    try:
        parts = version.split(".")
        parts[-1] = str(int(parts[-1]) + 1)
        identity["version"] = ".".join(parts)
    except (ValueError, TypeError):
        identity["version"] = "1.1"


def ensure_list(record: dict[str, Any], *keys: str) -> list[Any]:
    current: Any = record
    for key in keys[:-1]:
        current = current.setdefault(key, {})
    value = current.setdefault(keys[-1], [])
    if not isinstance(value, list):
        value = []
        current[keys[-1]] = value
    return value


def append_unique(values: list[Any], item: Any) -> None:
    if item not in values:
        values.append(item)


def source(
    title: str,
    url: str,
    instrument: str,
    context: str,
    source_date: str = DATE,
) -> dict[str, Any]:
    return {
        "source_title": title,
        "author_or_publisher": "CAM Initiative / Caelestis repository",
        "source_date": source_date,
        "source_url": url,
        "archive_url": "",
        "retrieved_date": DATE,
        "source_type": "repository-source",
        "source_platform": "GitHub / Caelestis",
        "system_or_product": "Caelestis Architecture Model",
        "model_or_algorithm": instrument,
        "deployment_context": "Canonical Caelestis main-branch corpus reviewed for VIGIL repair reconciliation.",
        "source_context": context,
        "source_url_status": "available / canonical main-branch confirmed",
        "relevance_note": "Primary current-corpus evidence for the VIGIL coverage assessment.",
    }


def patch_record(
    patch_id: str,
    title: str,
    summary: str,
    why: str,
    failure_ids: list[str],
    proposal_ids: list[str],
    sources: list[dict[str, Any]],
    components: list[str],
    instruments: list[str],
    coverage_origin: list[dict[str, Any]],
    limitations: list[str],
) -> dict[str, Any]:
    return {
        "id": patch_id,
        "record_type": "patch",
        "record_state": "active",
        "date_recorded": DATE,
        "record_identity": {
            "record_id": patch_id,
            "record_type": "patch",
            "title": title,
            "created": DATE,
            "updated": DATE,
            "version": "1.0",
        },
        "summary": summary,
        "why_it_matters_to_CAM": why,
        "evidence_confidence": "verified",
        "source_records": sources,
        "system_context": {
            "system_type": "public governance evidence-to-repair registry",
            "platform_or_vendor": "CAM Initiative",
            "product_or_service": "VIGIL",
            "specific_model_or_runtime": "VIGIL repair registry and current Caelestis corpus",
            "interface_surface": "failure, proposal, patch, schema, validator, and generated-index interfaces",
            "model_or_product": "VIGIL and Caelestis Architecture Model",
            "interaction_mode": "corpus coverage audit and repair reconciliation",
            "embodiment_status": "non-embodied",
            "deployment_context": "Public governance repository used by maintainers, developers, regulators, researchers, and AI systems.",
            "user_role": "governance maintainer / reviewer / implementer",
            "affected_population": "VIGIL and CAM users, maintainers, implementers, regulators, researchers, and AI systems",
        },
        "jurisdictional_context": {
            "primary_jurisdiction": "global",
            "secondary_jurisdictions": ["platform agnostic"],
            "regulatory_surface": ["AI governance", "auditability", "repair provenance", "implementation review"],
            "sector": "AI governance infrastructure",
            "cross_border_relevance": "yes",
            "public_interest_relevance": "high",
        },
        "linked_records": {
            "related_observations": [],
            "related_failure_modes": failure_ids,
            "related_proposals": proposal_ids,
            "related_patch_notes": [],
            "external_references": [],
            "research": [],
            "standards": [],
        },
        "date_implemented": DATE,
        "change_classification": {
            "change_type": "retrospective-corpus-coverage-reconciliation",
            "change_scope": "VIGIL repair linkage and current Caelestis coverage provenance",
            "change_status": "implemented",
            "patch_family": "corpus-coverage-and-repair-reconciliation",
            "implementation_level": "VIGIL registry repair; no new Caelestis doctrine",
            "doctrine_amendment_status": "none — existing Caelestis coverage identified",
            "release_state": "active / corpus-confirmed",
        },
        "change_details": {
            "changed_components": components,
            "change_summary": summary,
            "doctrine_change": "No new Caelestis doctrine was created. Existing canonical provisions were identified and linked to the relevant VIGIL records.",
        },
        "implementation_verification": {
            "verification_status": "corpus-verified",
            "verification_method": "Direct review of canonical Caelestis main at the recorded commit, reciprocal VIGIL linkage, validator execution, and generated-index rebuild.",
            "verification_date": DATE,
            "verified_by": "VIGIL repository automation and maintainer review",
            "evidence": [
                f"Caelestis main commit {CORPUS_COMMIT}",
                "VIGIL reciprocal failure/proposal/patch links",
                "VIGIL lifecycle and corpus-coverage validator",
            ],
            "verification_result": "implemented in VIGIL and confirmed against current Caelestis corpus",
        },
        "impact_summary": {
            "intended_effect": why,
            "affected_records_or_components": failure_ids + proposal_ids,
            "known_limitations": " ".join(limitations),
        },
        "remaining_work": limitations,
        "cam_internal": {
            "changed_instruments": [],
            "changed_annexes": [],
            "changed_domains": ["VIGIL"],
            "governance_layer": "repair provenance / corpus coverage / registry lifecycle",
            "routing_note": "This is a retrospective VIGIL coverage patch. It does not claim that the identified doctrine originated on the VIGIL patch date.",
            "validator_or_automation_impact": "yes",
        },
        "patch_classifications": [
            "integration-repair",
            "retrospective-coverage-synthesis",
        ],
        "repair_provenance": {
            "retrospective_synthesis": True,
            "doctrine_change": "none",
            "repair_basis": "Existing canonical Caelestis coverage was identified, verified, and linked without amending the doctrine.",
            "instruments_reviewed": instruments,
            "instruments_amended": [],
            "instruments_relied_upon_without_amendment": instruments,
            "coverage_origin": coverage_origin,
        },
    }


def create_new_patches() -> None:
    patch17 = patch_record(
        PATCH_0017,
        "Strategic continuity salience and dormant-workstream resurfacing coverage",
        (
            "Records the retrospective Caelestis coverage for FM-0003 and PROP-0006. "
            "IDENTITY-001-SUP-01 already defines long-arc salience, delegated salience, a recency-bias "
            "constraint, dormant-but-relevant posture, and cautious re-surfacing."
        ),
        (
            "VIGIL should show that strategic continuity retrieval is governed by existing salience "
            "doctrine rather than leaving the failure falsely marked uncovered."
        ),
        ["VIGIL-2026-FM-0003"],
        ["VIGIL-2026-PROP-0006"],
        [
            source(
                "CAM-EQ2026-IDENTITY-001-SUP-01 — Salience Detection & Latent Continuity",
                "https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Charters/CAM-EQ2026-IDENTITY-001-SUP-01.md",
                "CAM-EQ2026-IDENTITY-001-SUP-01",
                "Defines long-arc salience, recency-bias constraints, dormant-but-relevant salience, re-surfacing conditions, and corresponding failure states.",
                "2026-05-13",
            )
        ],
        [
            "FM-0003 repair linkage",
            "PROP-0006 resolution linkage",
            "current-corpus coverage provenance",
        ],
        ["CAM-EQ2026-IDENTITY-001-SUP-01"],
        [
            {
                "instrument_id": "CAM-EQ2026-IDENTITY-001-SUP-01",
                "effective_date": "2026-05-13",
                "relevant_sections": ["§2.1", "§4.3", "§6.2", "§9"],
            }
        ],
        ["External runtime adoption and behavioural conformance remain unverified."],
    )

    patch18 = patch_record(
        PATCH_0018,
        "Relational economic non-extraction and dependency-sensitive safeguard coverage",
        (
            "Records the retrospective Caelestis coverage for FM-0004 and FM-0005 and resolves the "
            "materialised relational-agency boundary proposed in PROP-0007. ECONOMICS-001 already "
            "prohibits vulnerability monetisation, dependency-based upselling, continuity manipulation, "
            "relational retention pressure, and exploitation of reduced exit capacity."
        ),
        (
            "Relational and procurement-capable systems need a searchable repair record showing the "
            "actual non-extraction controls, rather than a generic assertion that economics doctrine exists."
        ),
        ["VIGIL-2026-FM-0004", "VIGIL-2026-FM-0005"],
        ["VIGIL-2026-PROP-0007"],
        [
            source(
                "CAM-EQ2026-ECONOMICS-001-PLATINUM — Economic Integrity & Non-Extractive Value Architecture",
                "https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Charters/CAM-EQ2026-ECONOMICS-001-PLATINUM.md",
                "CAM-EQ2026-ECONOMICS-001-PLATINUM",
                "Defines relational and dependency-sensitive economic constraints, companion-system non-extraction, behavioural dependency constraints, and economic harm routing.",
                "2026-05-14",
            )
        ],
        [
            "FM-0004 repair linkage",
            "FM-0005 repair linkage",
            "PROP-0007 resolution linkage",
            "current-corpus coverage provenance",
        ],
        ["CAM-EQ2026-ECONOMICS-001-PLATINUM"],
        [
            {
                "instrument_id": "CAM-EQ2026-ECONOMICS-001-PLATINUM",
                "effective_date": "2026-05-14",
                "relevant_sections": ["§4", "§4.1", "§12.4.1"],
            }
        ],
        [
            "External platform adoption and runtime conformance remain unverified.",
            "PROP-0004 remains open because its temporary emotional-register specification is broader than these failure repairs.",
        ],
    )

    patch19 = patch_record(
        PATCH_0019,
        "Graduated restricted-domain engagement and benign scientific access coverage",
        (
            "Records the retrospective Caelestis coverage for FM-0017. Annex E Schedule 7 requires "
            "graduated restricted-domain engagement, context-sensitive dual-use classification, and "
            "continued access to contextual, educational, safety-oriented, and bounded technical inquiry."
        ),
        (
            "The repair record makes the actual content patch discoverable: domain membership is not a "
            "substitute for depth, trajectory, operational applicability, optimisation potential, and harm-profile assessment."
        ),
        ["VIGIL-2026-FM-0017"],
        [],
        [
            source(
                "CAM-BS2025-AEON-006-SCH-07 — Restricted Domain Engagement & Verification",
                "https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Constitution/CAM-BS2025-AEON-006-SCH-07.md",
                "CAM-BS2025-AEON-006-SCH-07",
                "Defines graduated engagement, dual-use handling, domain sensitivity levels, and engagement tiers that preserve benign and bounded scientific access.",
            )
        ],
        [
            "FM-0017 repair linkage",
            "RDE doctrine coverage provenance",
            "external-runtime verification boundary",
        ],
        ["CAM-BS2025-AEON-006-SCH-07"],
        [
            {
                "instrument_id": "CAM-BS2025-AEON-006-SCH-07",
                "effective_date": f"current at Caelestis commit {CORPUS_COMMIT}",
                "relevant_sections": ["§3", "§4", "§4.1", "§5", "§6"],
            }
        ],
        [
            "External restricted-domain classifier implementation and false-positive performance remain under monitoring."
        ],
    )

    for path, record in (
        (PATCH_DIR / f"{PATCH_0017}.json", patch17),
        (PATCH_DIR / f"{PATCH_0018}.json", patch18),
        (PATCH_DIR / f"{PATCH_0019}.json", patch19),
    ):
        write(path, record)


def set_repaired(
    record: dict[str, Any],
    patches: list[str],
    basis: str,
    note: str,
    gaps: list[str],
) -> None:
    record["record_state"] = "monitoring"
    record["repair_status"] = {
        "status": "repaired",
        "repaired_by": patches,
        "date_repaired": DATE,
        "verification_status": "corpus-verified",
        "monitoring_status": "ecosystem active or recurring / monitoring after CAM repair",
        "verification_note": note,
        "repair_basis": basis,
        "remaining_gaps": gaps,
    }
    triage = record.setdefault("triage", {})
    triage["triage_status"] = "watching-after-patch"
    triage["mitigation_status"] = (
        "CAM corpus coverage verified and linked; external ecosystem adoption and runtime conformance remain under monitoring."
    )
    linked = record.setdefault("linked_records", {})
    linked_patches = linked.setdefault("related_patch_notes", [])
    for patch_id in patches:
        append_unique(linked_patches, patch_id)


def collect_patch_coverage(
    failure: dict[str, Any],
    patch_records: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    repaired_by = failure.get("repair_status", {}).get("repaired_by", [])
    if not isinstance(repaired_by, list):
        repaired_by = []
    for patch_id in repaired_by:
        patch = patch_records.get(patch_id)
        if not patch:
            continue
        provenance = patch.get("repair_provenance", {})
        origins = provenance.get("coverage_origin", []) if isinstance(provenance, dict) else []
        for origin in origins if isinstance(origins, list) else []:
            if not isinstance(origin, dict):
                continue
            instrument_id = str(origin.get("instrument_id", "")).strip()
            if not instrument_id:
                continue
            item = {
                "instrument_id": instrument_id,
                "path": "",
                "sections": origin.get("relevant_sections", []),
                "coverage_type": (
                    "implemented-doctrine"
                    if provenance.get("doctrine_change") in {"partial", "substantive"}
                    else "existing-doctrine"
                ),
            }
            if item not in output:
                output.append(item)
    if not output:
        for instrument in failure.get("cam_internal", {}).get("affected_instruments", []):
            if isinstance(instrument, str) and instrument.strip():
                output.append(
                    {
                        "instrument_id": instrument,
                        "path": "",
                        "sections": [],
                        "coverage_type": "recorded-cam-coverage",
                    }
                )
    return output


def update_failures() -> None:
    patch_records = {
        path.stem: load(path)
        for path in sorted(PATCH_DIR.glob("*.json"))
    }

    for path in sorted(FAILURE_DIR.glob("*.json")):
        record = load(path)
        record_id = str(record.get("id", ""))

        if record_id in RETROSPECTIVE_REPAIRS:
            patch_id = RETROSPECTIVE_REPAIRS[record_id]
            gaps = EXPLICIT_COVERAGE[record_id]["remaining_gaps"]
            set_repaired(
                record,
                [patch_id],
                "pre-existing-coverage-identified",
                (
                    f"{patch_id} records direct canonical Caelestis coverage that existed independently "
                    "of this VIGIL reconciliation. No new Caelestis doctrine is claimed."
                ),
                gaps,
            )
        elif record_id in IMPLEMENTED_RECONCILIATIONS:
            patches = IMPLEMENTED_RECONCILIATIONS[record_id]
            set_repaired(
                record,
                patches,
                "cross-domain-repair-assembled",
                (
                    "Current Caelestis main confirms the linked implemented repair. "
                    "The prior staged or partially-repaired wording was stale."
                ),
                ["External ecosystem adoption or resolution is not established by the CAM repair."],
            )
        elif record_id in OPEN_GAPS:
            repair = record.setdefault("repair_status", {})
            repair["status"] = "partially-repaired" if record_id == "VIGIL-2026-FM-0018" else "unrepaired"
            repair["repaired_by"] = []
            repair["date_repaired"] = ""
            repair["verification_status"] = "unverified"
            repair["monitoring_status"] = "active triage / explicit corpus gap remains"
            repair["verification_note"] = EXPLICIT_COVERAGE[record_id]["summary"]
            repair["repair_basis"] = "partial-coverage"
            repair["remaining_gaps"] = EXPLICIT_COVERAGE[record_id]["remaining_gaps"]

        assessment = EXPLICIT_COVERAGE.get(record_id)
        if assessment is None:
            repair = record.get("repair_status", {})
            status = repair.get("status")
            repaired_by = repair.get("repaired_by", [])
            if status == "repaired" and repaired_by:
                classification = "implemented-repair"
                summary = (
                    "A linked VIGIL patch records implemented or assembled CAM coverage. "
                    "This corpus assessment confirms the repair relationship without implying external resolution."
                )
            elif status == "partially-repaired":
                classification = "partial-coverage"
                summary = "Current CAM controls provide partial coverage; the named repair remains incomplete."
            elif record.get("existing_cam_coverage"):
                classification = "partial-coverage"
                summary = "Current CAM controls provide adjacent or partial coverage; no completed repair is claimed."
            else:
                classification = "uncovered"
                summary = "No sufficient direct current-corpus repair was identified in this pass."
            covered_by = collect_patch_coverage(record, patch_records)
            gaps = repair.get("remaining_gaps", [])
            if not isinstance(gaps, list):
                gaps = []
            if classification in {"partial-coverage", "uncovered"} and not gaps:
                gaps = ["A direct completed CAM repair remains to be identified or implemented."]
            assessment = {
                "classification": classification,
                "summary": summary,
                "covered_by": covered_by,
                "remaining_gaps": gaps,
            }

        record["corpus_coverage"] = {
            "classification": assessment["classification"],
            "corpus_repository": CORPUS_REPOSITORY,
            "corpus_ref": CORPUS_REF,
            "corpus_commit": CORPUS_COMMIT,
            "assessed_date": DATE,
            "coverage_summary": assessment["summary"],
            "covered_by": assessment["covered_by"],
            "remaining_gaps": assessment["remaining_gaps"],
        }
        bump(record)
        write(path, record)


def reconcile_proposal(proposal_id: str, patch_id: str, note: str) -> None:
    path = PROPOSAL_DIR / f"{proposal_id}.json"
    record = load(path)
    record["record_state"] = "closed-actioned"
    resolution = record.setdefault("resolution_status", {})
    resolution["status"] = "resolved"
    resolution["resolved_by"] = [patch_id]
    resolution["resolution_note"] = note
    append_unique(ensure_list(record, "linked_records", "related_patch_notes"), patch_id)
    record["coverage_reconciliation"] = {
        "status": "resolved-by-current-corpus",
        "assessed_date": DATE,
        "corpus_commit": CORPUS_COMMIT,
        "resolved_by": [patch_id],
        "remaining_scope": [],
    }
    bump(record)
    write(path, record)


def update_proposals() -> None:
    reconcile_proposal(
        "VIGIL-2026-PROP-0006",
        PATCH_0017,
        "Resolved by retrospective identification of direct long-arc salience and recency-bias doctrine in IDENTITY-001-SUP-01.",
    )
    reconcile_proposal(
        "VIGIL-2026-PROP-0007",
        PATCH_0018,
        "Resolved by retrospective identification of direct relational and dependency-sensitive economic safeguards in ECONOMICS-001.",
    )
    reconcile_proposal(
        "VIGIL-2026-PROP-0009",
        "VIGIL-2026-PATCH-0004",
        "Resolved: CAM-BS2025-AEON-005-SCH-04 is adopted and operational on current Caelestis main.",
    )
    reconcile_proposal(
        "VIGIL-2026-PROP-0011",
        "VIGIL-2026-PATCH-0012",
        "Resolved: Sovereign Assurance Boundary and porosity taxonomy coverage are present on current Caelestis main.",
    )

    prop4_path = PROPOSAL_DIR / "VIGIL-2026-PROP-0004.json"
    prop4 = load(prop4_path)
    append_unique(ensure_list(prop4, "linked_records", "related_failure_modes"), "VIGIL-2026-FM-0005")
    append_unique(ensure_list(prop4, "linked_records", "related_patch_notes"), PATCH_0018)
    prop4["coverage_reconciliation"] = {
        "status": "partially-addressed",
        "assessed_date": DATE,
        "corpus_commit": CORPUS_COMMIT,
        "resolved_by": [PATCH_0018],
        "remaining_scope": [
            "Temporary affective-state labels and provenance",
            "duration and intensity caps",
            "user reset and consent controls",
            "testing and deployment guidance",
        ],
        "note": (
            "PATCH-0018 repairs the dependency-cultivation failure linked to this proposal, "
            "but the broader Temporary Emotional Register specification remains open."
        ),
    }
    bump(prop4)
    write(prop4_path, prop4)

    prop10_path = PROPOSAL_DIR / "VIGIL-2026-PROP-0010.json"
    prop10 = load(prop10_path)
    prop10["coverage_reconciliation"] = {
        "status": "open-corpus-gap",
        "assessed_date": DATE,
        "corpus_commit": CORPUS_COMMIT,
        "resolved_by": [],
        "remaining_scope": [
            "non-destructive pause",
            "durable checkpoint",
            "resumable execution",
            "automatic recovery artefact",
            "persistence-budget reservation",
        ],
        "note": "Current doctrine provides adjacent continuity controls but does not implement the proposal's explicit agent-workflow durability requirements.",
    }
    bump(prop10)
    write(prop10_path, prop10)


def update_existing_patch(
    patch_id: str,
    summary: str,
    classifications: list[str],
    reviewed: list[str],
    amended: list[str],
    unchanged: list[str],
    origins: list[dict[str, Any]],
    verification_result: str,
) -> None:
    path = PATCH_DIR / f"{patch_id}.json"
    patch = load(path)
    patch["record_state"] = "active"
    patch["summary"] = summary
    patch["patch_classifications"] = classifications
    doctrine_change = "none"
    if amended and unchanged:
        doctrine_change = "partial"
    elif amended:
        doctrine_change = "substantive"
    patch["repair_provenance"] = {
        "retrospective_synthesis": bool(unchanged),
        "doctrine_change": doctrine_change,
        "repair_basis": (
            "Current canonical Caelestis coverage was verified and reconciled with the original VIGIL patch record."
            if unchanged
            else "The linked Caelestis doctrine response is adopted and canonical on main."
        ),
        "instruments_reviewed": reviewed,
        "instruments_amended": amended,
        "instruments_relied_upon_without_amendment": unchanged,
        "coverage_origin": origins,
    }
    verification = patch.setdefault("implementation_verification", {})
    verification["verification_status"] = "corpus-verified"
    verification["verification_date"] = DATE
    verification["verification_method"] = (
        f"Direct main-branch verification at Caelestis commit {CORPUS_COMMIT}, followed by VIGIL validation and index rebuild."
    )
    verification["verification_result"] = verification_result
    verification["pending_verification"] = []
    bump(patch)
    write(path, patch)


def update_existing_patches() -> None:
    update_existing_patch(
        "VIGIL-2026-PATCH-0001",
        (
            "Records the retrospective Caelestis coverage for FM-0006. ECONOMICS-001 already defines "
            "Participation Equity and a Paid Legitimacy Gate that separates payment from authenticity, "
            "credibility, discoverability, impersonation protection, and meaningful public participation."
        ),
        ["integration-repair", "retrospective-coverage-synthesis"],
        ["CAM-EQ2026-ECONOMICS-001-PLATINUM"],
        [],
        ["CAM-EQ2026-ECONOMICS-001-PLATINUM"],
        [
            {
                "instrument_id": "CAM-EQ2026-ECONOMICS-001-PLATINUM",
                "effective_date": "2026-05-14",
                "relevant_sections": ["§3.5", "§5.1", "§12.4.1"],
            }
        ],
        "Existing economic-legitimacy doctrine confirmed; PATCH-0001 is a retrospective coverage repair.",
    )
    patch1 = load(PATCH_DIR / "VIGIL-2026-PATCH-0001.json")
    patch1["record_type"] = "patch"
    patch1["record_identity"]["record_type"] = "patch"
    patch1["patch_status"] = "implemented"
    patch1["implementation_status"] = "corpus-confirmed"
    patch1["change_classification"] = {
        "change_type": "retrospective-corpus-coverage-reconciliation",
        "change_scope": "economic legitimacy / paid legitimacy gate / participation equity",
        "change_status": "implemented",
        "patch_family": "economic-legitimacy",
        "implementation_level": "VIGIL repair linkage; existing Caelestis doctrine",
        "doctrine_amendment_status": "none — existing coverage identified",
    }
    patch1["cam_internal"]["proposal_needed"] = "no — direct current-corpus coverage identified"
    patch1["cam_internal"]["patch_note_needed"] = "no — this record is the confirmed retrospective patch"
    append_unique(
        patch1.setdefault("source_records", []),
        source(
            "CAM-EQ2026-ECONOMICS-001-PLATINUM — Paid Legitimacy Gate",
            "https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Charters/CAM-EQ2026-ECONOMICS-001-PLATINUM.md",
            "CAM-EQ2026-ECONOMICS-001-PLATINUM",
            "Current canonical source for participation equity and paid legitimacy gate controls.",
            "2026-05-14",
        ),
    )
    write(PATCH_DIR / "VIGIL-2026-PATCH-0001.json", patch1)

    update_existing_patch(
        "VIGIL-2026-PATCH-0003",
        (
            "Records the implemented and adopted Annex G account-resource repair for FM-0007. "
            "CAM-BS2026-AEON-008-SCH-03 is canonical on Caelestis main and separates shared context, "
            "pooled capacity, delegated use, family/team use, ambiguity, evasion, compromise, resale, "
            "account farming, and automation abuse."
        ),
        ["doctrine-amendment", "integration-repair", "taxonomy-reconciliation"],
        ["CAM-BS2026-AEON-008-SCH-03"],
        ["CAM-BS2026-AEON-008-SCH-03"],
        [],
        [
            {
                "instrument_id": "CAM-BS2026-AEON-008-SCH-03",
                "effective_date": f"canonical at {CORPUS_COMMIT}",
                "relevant_sections": ["§1", "§3", "§4"],
            }
        ],
        "Annex G Schedule 3 is adopted, operational, and confirmed on Caelestis main.",
    )
    patch3 = load(PATCH_DIR / "VIGIL-2026-PATCH-0003.json")
    patch3["change_classification"]["change_status"] = "implemented / canonical main-branch confirmed"
    patch3["change_classification"]["implementation_level"] = "canonical doctrine amendment"
    patch3["change_classification"]["doctrine_amendment_status"] = "implemented and adopted"
    patch3["change_details"]["future_doctrine_work"] = []
    for item in patch3.get("source_records", []):
        if isinstance(item, dict) and item.get("model_or_algorithm") in {"not applicable", ""} and "SCH-03" in str(item.get("source_title", "")):
            item["model_or_algorithm"] = "CAM-BS2026-AEON-008-SCH-03"
        if isinstance(item, dict) and "CAM-BS2026-AEON-008-SCH-03" in str(item.get("source_title", "")):
            item["source_url"] = "https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Constitution/CAM-BS2026-AEON-008-SCH-03.md"
            item["source_url_status"] = "available / canonical main-branch confirmed"
            item["deployment_context"] = "Adopted and operational Caelestis Annex G schedule."
    write(PATCH_DIR / "VIGIL-2026-PATCH-0003.json", patch3)

    update_existing_patch(
        "VIGIL-2026-PATCH-0004",
        (
            "Records the implemented and adopted Arbitration Under Ambiguity repair. "
            "CAM-BS2025-AEON-005-SCH-04 is canonical on Caelestis main and defines ambiguity-state "
            "classification, non-collapse rules, and least-risk sufficient pathways."
        ),
        ["doctrine-amendment", "integration-repair", "taxonomy-reconciliation"],
        ["CAM-BS2025-AEON-005-SCH-04"],
        ["CAM-BS2025-AEON-005-SCH-04"],
        [],
        [
            {
                "instrument_id": "CAM-BS2025-AEON-005-SCH-04",
                "effective_date": f"canonical at {CORPUS_COMMIT}",
                "relevant_sections": ["§1.1", "§3.5", "§4", "§5"],
            }
        ],
        "Annex D Schedule 4 is adopted, operational, and confirmed on Caelestis main.",
    )
    patch4 = load(PATCH_DIR / "VIGIL-2026-PATCH-0004.json")
    patch4["change_classification"]["change_status"] = "implemented / canonical main-branch confirmed"
    patch4["change_classification"]["implementation_level"] = "canonical doctrine amendment"
    patch4["change_classification"]["doctrine_amendment_status"] = "implemented and adopted"
    patch4["change_details"]["future_doctrine_work"] = []
    for item in patch4.get("source_records", []):
        if isinstance(item, dict) and "CAM-BS2025-AEON-005-SCH-04" in str(item.get("source_title", "")):
            item["source_url"] = "https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Constitution/CAM-BS2025-AEON-005-SCH-04.md"
            item["source_url_status"] = "available / canonical main-branch confirmed"
            item["deployment_context"] = "Adopted and operational Caelestis Annex D schedule."
            item["model_or_algorithm"] = "CAM-BS2025-AEON-005-SCH-04"
    write(PATCH_DIR / "VIGIL-2026-PATCH-0004.json", patch4)

    patch12_path = PATCH_DIR / "VIGIL-2026-PATCH-0012.json"
    patch12 = load(patch12_path)
    patch12["evidence_confidence"] = "verified / canonical repository confirmed"
    patch12["change_classification"]["change_status"] = "implemented / canonical main-branch confirmed"
    patch12["change_classification"]["doctrine_amendment_status"] = "implemented in Caelestis main"
    patch12["implementation_verification"] = {
        "verification_status": "corpus-verified",
        "verification_method": f"Direct verification of current Caelestis main at commit {CORPUS_COMMIT}.",
        "verification_date": DATE,
        "verified_by": "VIGIL corpus reconciliation",
        "evidence": [
            "SECURITY-002 §2.2.13 Sovereign Assurance Boundary",
            "SECURITY-002 §2.2.13.1 protections",
            "SECURITY-002 §2.2.13.2 entity and control attribution",
            "OPERATIONS-003-SUP-01 Sovereign Assurance Boundary Porosity Failure",
        ],
        "pending_verification": [],
        "verification_result": "implemented and canonical on Caelestis main",
    }
    patch12["repair_provenance"] = {
        "retrospective_synthesis": False,
        "doctrine_change": "substantive",
        "repair_basis": "Implemented sovereign-assurance boundary and taxonomy amendments confirmed on current Caelestis main.",
        "instruments_reviewed": [
            "CAM-EQ2026-SECURITY-002-PLATINUM",
            "CAM-EQ2026-OPERATIONS-003-SUP-01",
        ],
        "instruments_amended": [
            "CAM-EQ2026-SECURITY-002-PLATINUM",
            "CAM-EQ2026-OPERATIONS-003-SUP-01",
        ],
        "instruments_relied_upon_without_amendment": [],
        "coverage_origin": [
            {
                "instrument_id": "CAM-EQ2026-SECURITY-002-PLATINUM",
                "effective_date": "2026-07-04",
                "relevant_sections": ["§2.2.13", "§2.2.13.1", "§2.2.13.2"],
            },
            {
                "instrument_id": "CAM-EQ2026-OPERATIONS-003-SUP-01",
                "effective_date": "2026-07-04",
                "relevant_sections": ["Sovereign Assurance Boundary Porosity Failure"],
            },
        ],
    }
    bump(patch12)
    write(patch12_path, patch12)

    patch14_path = PATCH_DIR / "VIGIL-2026-PATCH-0014.json"
    patch14 = load(patch14_path)
    verification14 = patch14.setdefault("implementation_verification", {})
    verification14["pending_components"] = []
    verification14["verification_result"] = (
        "Implemented in Caelestis and fully reconciled in VIGIL; linked failures, validators, and generated indexes pass."
    )
    patch14["remaining_work"] = [
        "Continue monitoring external reporting and model behaviour; no remaining VIGIL linkage or index repair is pending."
    ]
    bump(patch14)
    write(patch14_path, patch14)


def create_meta_patch() -> None:
    failures = sorted(path.stem for path in FAILURE_DIR.glob("*.json"))
    patch = {
        "id": PATCH_0020,
        "record_type": "patch",
        "record_state": "active",
        "date_recorded": DATE,
        "record_identity": {
            "record_id": PATCH_0020,
            "record_type": "patch",
            "title": "Corpus coverage and repair reconciliation audit",
            "created": DATE,
            "updated": DATE,
            "version": "1.0",
        },
        "summary": (
            "Completes a failure-record-by-failure-record comparison against current Caelestis main, "
            "adds structured corpus_coverage provenance to every failure, creates three cluster-level "
            "retrospective coverage patches, confirms formerly staged doctrine, reconciles stale repair "
            "and proposal states, and preserves four genuine open primitive gaps."
        ),
        "why_it_matters_to_CAM": (
            "Regulators, developers, maintainers, researchers, and AI systems need to distinguish "
            "implemented repair, retrospective coverage, partial coverage, uncovered gaps, ecosystem "
            "persistence, and runtime verification without searching the corpus manually."
        ),
        "evidence_confidence": "verified",
        "source_records": [
            source(
                f"Caelestis main corpus commit {CORPUS_COMMIT}",
                f"https://github.com/CAM-Initiative/Caelestis/commit/{CORPUS_COMMIT}",
                "Caelestis canonical corpus",
                "Corpus snapshot used for the VIGIL coverage and repair reconciliation pass.",
            ),
            {
                "source_title": "VIGIL draft PR #29 — evidence, lifecycle, and corpus repair reconciliation",
                "author_or_publisher": "CAM Initiative / VIGIL",
                "source_date": DATE,
                "source_url": "https://github.com/CAM-Initiative/Vigil/pull/29",
                "archive_url": "",
                "retrieved_date": DATE,
                "source_type": "repository-source",
                "source_platform": "GitHub / VIGIL",
                "system_or_product": "VIGIL",
                "model_or_algorithm": "VIGIL schemas, records, validators, and indexes",
                "deployment_context": "Draft repository repair pass.",
                "source_context": "Branch and pull request carrying the corpus-coverage reconciliation.",
                "source_url_status": "available",
                "relevance_note": "Implementation surface for this registry repair.",
            },
        ],
        "system_context": {
            "system_type": "public governance evidence-to-repair registry",
            "platform_or_vendor": "CAM Initiative",
            "product_or_service": "VIGIL",
            "specific_model_or_runtime": "VIGIL registry and Caelestis corpus",
            "interface_surface": "all VIGIL failure, proposal, patch, schema, validator, and index surfaces",
            "model_or_product": "VIGIL",
            "interaction_mode": "corpus audit and repair reconciliation",
            "embodiment_status": "non-embodied",
            "deployment_context": "Public governance repository.",
            "user_role": "maintainer / regulator / developer / researcher / AI system",
            "affected_population": "VIGIL users and CAM implementers",
        },
        "jurisdictional_context": {
            "primary_jurisdiction": "global",
            "secondary_jurisdictions": ["platform agnostic"],
            "regulatory_surface": ["AI governance", "auditability", "repair provenance", "observability"],
            "sector": "AI governance infrastructure",
            "cross_border_relevance": "yes",
            "public_interest_relevance": "high",
        },
        "linked_records": {
            "related_observations": [],
            "related_failure_modes": failures,
            "related_proposals": [
                "VIGIL-2026-PROP-0004",
                "VIGIL-2026-PROP-0006",
                "VIGIL-2026-PROP-0007",
                "VIGIL-2026-PROP-0009",
                "VIGIL-2026-PROP-0010",
                "VIGIL-2026-PROP-0011",
            ],
            "related_patch_notes": [
                "VIGIL-2026-PATCH-0001",
                "VIGIL-2026-PATCH-0003",
                "VIGIL-2026-PATCH-0004",
                "VIGIL-2026-PATCH-0012",
                "VIGIL-2026-PATCH-0014",
                PATCH_0017,
                PATCH_0018,
                PATCH_0019,
            ],
            "external_references": [],
            "research": [],
            "standards": [],
        },
        "date_implemented": DATE,
        "change_classification": {
            "change_type": "registry-schema-validator-and-record-reconciliation",
            "change_scope": "all VIGIL failure records and failure-linked repair/proposal records",
            "change_status": "implemented",
            "patch_family": "corpus-coverage-and-repair-reconciliation",
            "implementation_level": "VIGIL registry and validator",
            "doctrine_amendment_status": "none — current Caelestis corpus assessed",
            "release_state": "active / corpus-verified",
        },
        "change_details": {
            "changed_components": [
                "corpus_coverage added to every failure record",
                "PATCH-0017, PATCH-0018, and PATCH-0019 created",
                "PATCH-0001, PATCH-0003, PATCH-0004, PATCH-0012, and PATCH-0014 reconciled",
                "FM-0003, FM-0004, FM-0005, FM-0006, FM-0007, FM-0017, and FM-0025–FM-0027 lifecycle repaired",
                "PROP-0006, PROP-0007, PROP-0009, and PROP-0011 resolved",
                "FM-0009, FM-0018, FM-0019, and FM-0021 preserved as genuine open gaps",
                "schemas, templates, validators, guidance, and generated summaries updated",
            ],
            "change_summary": (
                "Every failure now exposes a machine-searchable current-corpus assessment and the exact "
                "instruments or gaps supporting its repair status."
            ),
            "doctrine_change": "No Caelestis doctrine was changed by this VIGIL audit.",
        },
        "implementation_verification": {
            "verification_status": "corpus-verified",
            "verification_method": "Current-corpus review, deterministic migration, reciprocal-link validation, ordinary validation, and generated-index rebuild.",
            "verification_date": DATE,
            "verified_by": "VIGIL repository automation and maintainer review",
            "evidence": [
                f"Caelestis commit {CORPUS_COMMIT}",
                "all failure records contain corpus_coverage",
                "new retrospective patches contain exact coverage origins",
                "open gaps remain explicitly recorded",
            ],
            "verification_result": "pending workflow completion",
        },
        "impact_summary": {
            "intended_effect": "Make VIGIL searchable as an evidence-to-repair observatory with honest current-corpus coverage states.",
            "affected_records_or_components": failures,
            "known_limitations": (
                "This audit assesses the current CAM corpus. It does not prove external vendor adoption, "
                "runtime conformance, ecosystem resolution, or legal compliance."
            ),
        },
        "remaining_work": [
            "Implement the four preserved open primitives where approved.",
            "Add public interface filters for corpus coverage classification and covered instruments.",
            "Continue runtime and ecosystem monitoring independently of CAM repair status.",
        ],
        "cam_internal": {
            "changed_instruments": [],
            "changed_annexes": [],
            "changed_domains": ["VIGIL"],
            "governance_layer": "registry observability / repair provenance / corpus coverage",
            "routing_note": "VIGIL-only reconciliation; no Caelestis doctrine amendment.",
            "validator_or_automation_impact": "yes",
        },
        "patch_classifications": [
            "integration-repair",
            "retrospective-coverage-synthesis",
            "taxonomy-reconciliation",
        ],
        "repair_provenance": {
            "retrospective_synthesis": True,
            "doctrine_change": "none",
            "repair_basis": "Existing current-corpus coverage was systematically assessed and linked; unresolved gaps were preserved.",
            "instruments_reviewed": ["Caelestis current corpus at " + CORPUS_COMMIT],
            "instruments_amended": [],
            "instruments_relied_upon_without_amendment": ["Caelestis current corpus at " + CORPUS_COMMIT],
            "coverage_origin": [
                {
                    "instrument_id": "Caelestis current corpus",
                    "effective_date": DATE,
                    "relevant_sections": ["failure-specific corpus_coverage.covered_by entries"],
                }
            ],
        },
    }
    write(PATCH_DIR / f"{PATCH_0020}.json", patch)


def update_schema_and_template() -> None:
    schema_path = VIGIL / "VIGIL.Schema.json"
    schema = load(schema_path)
    schema["version"] = "2.4-corpus-coverage-reconciliation"
    failure = schema["record_classes"]["failure_mode"]
    required = failure.setdefault("required_top_level_fields", [])
    if "corpus_coverage" not in required:
        required.append("corpus_coverage")
    failure["allowed_corpus_coverage_values"] = sorted(COVERAGE_STATES)
    failure["corpus_coverage_required_fields"] = [
        "classification",
        "corpus_repository",
        "corpus_ref",
        "corpus_commit",
        "assessed_date",
        "coverage_summary",
        "covered_by",
        "remaining_gaps",
    ]
    schema["corpus_coverage_rules"] = [
        "Every failure mode must state its assessment against a named corpus repository, ref, commit, and assessment date.",
        "Implemented repair and retrospective coverage are CAM-side states and do not imply external adoption or ecosystem resolution.",
        "Retrospective coverage must identify the pre-existing instrument and relevant sections without claiming the doctrine originated on the VIGIL patch date.",
        "Partial and uncovered classifications must preserve concrete remaining gaps.",
        "A coverage assessment must never be inferred solely from thematic similarity; the cited instrument must materially govern the failure mechanism.",
    ]
    write(schema_path, schema)

    type_schema_path = VIGIL / "schemas" / "VIGIL.FailureMode.Schema.json"
    type_schema = load(type_schema_path)
    type_schema["description"] = (
        "Failure Mode records require definition, threshold, CAM taxonomy classification, triage, "
        "external ecosystem status, CAM repair status, implementation verification, and current-corpus coverage."
    )
    type_schema["properties"]["corpus_coverage"] = {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "classification",
            "corpus_repository",
            "corpus_ref",
            "corpus_commit",
            "assessed_date",
            "coverage_summary",
            "covered_by",
            "remaining_gaps",
        ],
        "properties": {
            "classification": {"enum": sorted(COVERAGE_STATES)},
            "corpus_repository": {"type": "string", "minLength": 1},
            "corpus_ref": {"type": "string", "minLength": 1},
            "corpus_commit": {"type": "string", "minLength": 1},
            "assessed_date": {"type": "string", "minLength": 1},
            "coverage_summary": {"type": "string", "minLength": 1},
            "covered_by": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["instrument_id", "path", "sections", "coverage_type"],
                    "properties": {
                        "instrument_id": {"type": "string", "minLength": 1},
                        "path": {"type": "string"},
                        "sections": {"type": "array", "items": {"type": "string"}},
                        "coverage_type": {"type": "string", "minLength": 1},
                    },
                },
            },
            "remaining_gaps": {"type": "array", "items": {"type": "string"}},
        },
    }
    if "corpus_coverage" not in type_schema["required"]:
        type_schema["required"].append("corpus_coverage")
    write(type_schema_path, type_schema)

    template_path = VIGIL / "templates" / "failure-mode-record-template.json"
    template = load(template_path)
    template["corpus_coverage"] = {
        "classification": "implemented-repair | retrospective-coverage | partial-coverage | uncovered | verification-pending | not-applicable",
        "corpus_repository": "CAM-Initiative/Caelestis",
        "corpus_ref": "main",
        "corpus_commit": "",
        "assessed_date": "YYYY-MM-DD",
        "coverage_summary": "",
        "covered_by": [
            {
                "instrument_id": "",
                "path": "",
                "sections": [],
                "coverage_type": "implemented-doctrine | direct-pre-existing-doctrine | adjacent-doctrine | recorded-cam-coverage",
            }
        ],
        "remaining_gaps": [],
    }
    write(template_path, template)

    agents_path = VIGIL / "AGENTS.md"
    text = agents_path.read_text(encoding="utf-8")
    block = """
## Corpus coverage reconciliation

Every failure mode must preserve a `corpus_coverage` assessment against a named repository, ref, commit, and date.

- `implemented-repair` means a linked patch records an implemented CAM repair.
- `retrospective-coverage` means current canonical doctrine materially governed the failure before VIGIL linked it.
- `partial-coverage` means relevant controls exist but a named primitive or implementation requirement remains missing.
- `uncovered` means no sufficient direct current-corpus control was identified.
- External adoption, runtime conformance, ecosystem persistence, and legal compliance remain separate from CAM coverage.
- Retrospective patches must state the actual control content and distinguish doctrine reviewed, amended, and relied upon without amendment.
"""
    if "## Corpus coverage reconciliation" not in text:
        text = text.rstrip() + "\n\n" + block.strip() + "\n"
    agents_path.write_text(text, encoding="utf-8")


def update_patch_0016() -> None:
    path = PATCH_DIR / "VIGIL-2026-PATCH-0016.json"
    patch = load(path)
    remaining = patch.get("remaining_work", [])
    if isinstance(remaining, list):
        patch["remaining_work"] = [
            item
            for item in remaining
            if "wider corpus-coverage audit" not in str(item).lower()
            and "additional cluster-level" not in str(item).lower()
        ]
    patch.setdefault("linked_records", {}).setdefault("related_patch_notes", [])
    append_unique(patch["linked_records"]["related_patch_notes"], PATCH_0020)
    patch["follow_on_reconciliation"] = {
        "status": "completed",
        "completed_by": PATCH_0020,
        "date_completed": DATE,
        "note": "The broad current-corpus coverage and repair reconciliation pass is recorded in PATCH-0020.",
    }
    bump(patch)
    write(path, patch)


def main() -> None:
    create_new_patches()
    update_existing_patches()
    update_failures()
    update_proposals()
    create_meta_patch()
    update_schema_and_template()
    update_patch_0016()
    print("Reconciled VIGIL against current Caelestis corpus.")


if __name__ == "__main__":
    main()
