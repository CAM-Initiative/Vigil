#!/usr/bin/env python3
"""Correct VIGIL/CAM ontology boundaries and ingest July 2026 voice evidence.

This one-time, idempotent maintenance script:
- removes VIGIL-maintenance records incorrectly represented as CAM patches;
- removes reciprocal references to those invalid patch records;
- preserves the corpus audit as failure-level corpus_coverage metadata;
- records Live Voice and public voice evidence as ecosystem observations/failures;
- creates proposals only for prospective CAM corpus work;
- creates a retrospective patch note only where existing CAM doctrine directly covers a failure;
- cleans retrospective patch notes so their repair target is CAM/Caelestis, never VIGIL.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
DATE = "2026-07-14"
CAELESTIS_COMMIT = "40113eea5428478ba0734b3980600bfcece425a0"
INVALID_PATCHES = {"VIGIL-2026-PATCH-0016", "VIGIL-2026-PATCH-0020"}


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def all_record_paths() -> list[Path]:
    return sorted(RECORDS.rglob("*.json"))


def cleanse_refs(value: Any) -> Any:
    if isinstance(value, list):
        return [cleanse_refs(item) for item in value if not (isinstance(item, str) and item in INVALID_PATCHES)]
    if isinstance(value, dict):
        cleaned = {key: cleanse_refs(item) for key, item in value.items()}
        if "follow_on_reconciliation" in cleaned:
            follow = cleaned.get("follow_on_reconciliation")
            if isinstance(follow, dict) and (
                follow.get("completed_by") in INVALID_PATCHES
                or follow.get("resolved_by") in INVALID_PATCHES
            ):
                cleaned.pop("follow_on_reconciliation", None)
        return cleaned
    if value in INVALID_PATCHES:
        return ""
    return value


def append_unique(items: list[Any], value: Any, key: str | None = None) -> None:
    if key and isinstance(value, dict):
        marker = value.get(key)
        if any(isinstance(item, dict) and item.get(key) == marker for item in items):
            return
    elif value in items:
        return
    items.append(value)


def source(
    *,
    title: str,
    publisher: str,
    source_date: str,
    url: str,
    source_type: str,
    platform: str,
    system: str,
    model: str,
    deployment: str,
    context: str,
    status: str,
    relevance: str,
) -> dict[str, Any]:
    return {
        "source_title": title,
        "author_or_publisher": publisher,
        "source_date": source_date,
        "source_url": url,
        "archive_url": "",
        "retrieved_date": DATE,
        "source_type": source_type,
        "source_platform": platform,
        "system_or_product": system,
        "model_or_algorithm": model,
        "deployment_context": deployment,
        "source_context": context,
        "source_url_status": status,
        "relevance_note": relevance,
    }


def common_system(runtime: str, interaction: str, population: str) -> dict[str, Any]:
    return {
        "system_type": "frontier multimodal conversational AI system with real-time voice interaction",
        "platform_or_vendor": "OpenAI",
        "product_or_service": "ChatGPT",
        "specific_model_or_runtime": runtime,
        "interface_surface": [
            "live full-duplex voice",
            "audio input",
            "generated speech",
            "non-verbal vocal cues",
            "conversation lifecycle controls",
        ],
        "model_or_product": "ChatGPT Live Voice / GPT-Live",
        "interaction_mode": interaction,
        "embodiment_status": "voice-mediated / non-physical",
        "deployment_context": "Consumer conversational AI interaction using a real-time voice runtime.",
        "user_role": "end user / governance evaluator / accessibility-relevant voice user",
        "affected_population": population,
    }


def common_jurisdiction() -> dict[str, Any]:
    return {
        "primary_jurisdiction": "global",
        "secondary_jurisdictions": [
            "Australia",
            "United States",
            "European Union",
            "United Kingdom",
            "platform agnostic",
        ],
        "regulatory_surface": [
            "AI governance",
            "consumer protection",
            "voice AI",
            "accessibility",
            "relational safety",
            "platform transparency",
            "human-computer interaction",
            "post-release monitoring",
        ],
        "sector": "frontier AI platforms / multimodal conversational systems / voice AI",
        "cross_border_relevance": "yes",
        "public_interest_relevance": "high",
    }


def linked(
    observations: list[str] | None = None,
    failures: list[str] | None = None,
    proposals: list[str] | None = None,
    patches: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "related_observations": observations or [],
        "related_failure_modes": failures or [],
        "related_proposals": proposals or [],
        "related_patch_notes": patches or [],
        "external_references": [],
        "research": [],
        "standards": [],
    }


def observation(
    record_id: str,
    title: str,
    summary: str,
    why: str,
    sources: list[dict[str, Any]],
    system_context: dict[str, Any],
    linked_records: dict[str, Any],
    next_action: str,
    instruments: list[str],
    domains: list[str],
    mapping_groups: list[str],
    mapping_note: str,
    confidence: str = "anecdotal",
) -> dict[str, Any]:
    return {
        "id": record_id,
        "record_type": "observation",
        "record_state": "active",
        "date_recorded": DATE,
        "record_identity": {
            "record_id": record_id,
            "record_type": "observation",
            "title": title,
            "created": DATE,
            "updated": DATE,
            "version": "1.0",
        },
        "summary": summary,
        "why_it_matters_to_CAM": why,
        "evidence_confidence": confidence,
        "source_records": sources,
        "system_context": system_context,
        "jurisdictional_context": common_jurisdiction(),
        "linked_records": linked_records,
        "migration_notes": [
            "Source evidence is embedded in this substantive observation and in linked failure records where it supports a confirmed failure pathway.",
            "The record preserves uncertainty and does not infer proprietary runtime architecture, subjective model emotion, or vendor adoption of CAM.",
        ],
        "next_action": next_action,
        "cam_internal": {
            "related_or_similar_instruments": instruments,
            "related_or_similar_annexes": ["Annex B", "Annex E", "Annex L"],
            "related_or_similar_domains": domains,
            "governance_layer": "voice interaction / relational reciprocity / runtime transparency / identity continuity",
            "routing_note": "OBS routing only; confirmed failure classification and CAM repair state remain in linked FM and PATCH records.",
            "validator_or_automation_impact": "none",
        },
        "possible_taxonomy_mapping": {
            "canonical_failure_groups": mapping_groups,
            "taxonomy_reference": "CAM-EQ2026-OPERATIONS-003-SUP-01 Appendix B",
            "mapping_confidence": "provisional",
            "mapping_note": mapping_note,
        },
    }


def failure(
    record_id: str,
    title: str,
    summary: str,
    why: str,
    definition: str,
    threshold: str,
    sources: list[dict[str, Any]],
    system_context: dict[str, Any],
    linked_records: dict[str, Any],
    family: str,
    subtype: str,
    groups: list[str],
    harms: list[str],
    severity: str,
    confidence: str,
    triage_status: str,
    mitigation: str,
    next_step: str,
    affected_instruments: list[str],
    affected_domains: list[str],
    proposal_needed: str,
    repair_status: dict[str, Any],
    corpus_coverage: dict[str, Any],
    evidence_confidence: str = "anecdotal",
) -> dict[str, Any]:
    return {
        "id": record_id,
        "record_type": "failure_mode",
        "record_state": "active" if repair_status["status"] != "repaired" else "monitoring",
        "date_recorded": DATE,
        "record_identity": {
            "record_id": record_id,
            "record_type": "failure_mode",
            "title": title,
            "created": DATE,
            "updated": DATE,
            "version": "1.0",
        },
        "summary": summary,
        "why_it_matters_to_CAM": why,
        "evidence_confidence": evidence_confidence,
        "source_records": sources,
        "system_context": system_context,
        "jurisdictional_context": common_jurisdiction(),
        "linked_records": linked_records,
        "failure_mode_definition": definition,
        "failure_threshold": threshold,
        "failure_classification": {
            "failure_family": family,
            "failure_subtype": subtype,
            "harm_vectors": harms,
            "severity": severity,
            "likelihood": "emerging / requires continued testing",
            "confidence": confidence,
            "affected_rights_or_interests": [
                "user autonomy",
                "interaction clarity",
                "relational safety",
                "accessibility",
                "epistemic integrity",
                "platform transparency",
            ],
            "failure_scope": "vendor-specific observed signal / structurally relevant to voice-capable AI systems",
            "recurrence_pattern": "observed or reported in July 2026 voice interactions; broader recurrence requires monitoring",
            "canonical_failure_group": family,
            "taxonomy_reference": "CAM-EQ2026-OPERATIONS-003-SUP-01 Appendix B",
            "related_failure_groups": groups,
            "persistence": "active in external voice runtimes unless separately shown to improve or resolve",
            "reproducibility": "requires controlled replay and runtime-specific testing",
            "visibility": "user-facing voice behaviour, non-verbal output, turn handling, advice content, and runtime narration",
        },
        "triage": {
            "triage_priority": "P1",
            "triage_owner": "VIGIL maintainers",
            "triage_status": triage_status,
            "mitigation_status": mitigation,
            "escalation_required": "yes",
            "recommended_next_step": next_step,
        },
        "cam_internal": {
            "affected_instruments": affected_instruments,
            "affected_annexes": ["Annex B", "Annex E", "Annex L"],
            "affected_domains": affected_domains,
            "governance_layer": "voice interaction / relational governance / epistemic integrity / runtime conformance",
            "proposal_needed": proposal_needed,
            "linked_proposal_ids": linked_records.get("related_proposals", []),
            "routing_note": [
                "The failure subject is an ecosystem runtime behaviour; VIGIL is the evidence and repair observatory, not the failed system.",
                "Do not infer subjective emotion, hidden runtime cause, or proprietary architecture beyond the supplied evidence.",
            ],
            "validator_or_automation_impact": "none",
        },
        "repair_status": repair_status,
        "ecosystem_status": {
            "status": "active",
            "basis": "Observed or publicly reported July 2026 voice-runtime behaviour remains externally unresolved.",
            "last_assessed": DATE,
            "monitoring_required": True,
        },
        "corpus_coverage": corpus_coverage,
    }


def proposal(
    record_id: str,
    title: str,
    summary: str,
    why: str,
    rationale: str,
    sources: list[dict[str, Any]],
    linked_records: dict[str, Any],
    domains: list[str],
    instruments: list[str],
    scope: str,
    principles: list[str],
) -> dict[str, Any]:
    return {
        "id": record_id,
        "record_type": "proposal",
        "record_state": "active",
        "date_recorded": DATE,
        "record_identity": {
            "record_id": record_id,
            "record_type": "proposal",
            "title": title,
            "created": DATE,
            "updated": DATE,
            "version": "1.0",
        },
        "summary": summary,
        "why_it_matters_to_CAM": why,
        "evidence_confidence": "corroborated",
        "source_records": sources,
        "system_context": {
            "system_type": "voice-capable conversational AI and CAM governance corpus",
            "platform_or_vendor": "Multi Vendor",
            "vendor_cluster": ["OpenAI", "Anthropic", "Google", "Microsoft", "Other"],
            "primary_evidenced_vendors": ["OpenAI", "Other"],
            "product_or_service": "Other",
            "specific_model_or_runtime": "voice, live voice, companion, ambient, and multimodal conversational runtimes",
            "interface_surface": "voice, audio, ambient-presence, conversational, accessibility, and companion interfaces",
            "model_or_product": "voice-capable AI systems",
            "interaction_mode": "CAM governance proposal development",
            "embodiment_status": "voice-mediated / mixed",
            "deployment_context": "Consumer, enterprise, assistive, companion, and ambient voice deployments.",
            "user_role": "user / developer / platform operator / regulator / governance maintainer",
            "affected_population": "voice-system users, including children, neurodivergent users, disabled users, and users relying on repetition or atypical communication styles",
        },
        "jurisdictional_context": common_jurisdiction(),
        "linked_records": linked_records,
        "migration_notes": [
            "This proposal targets prospective CAM/Caelestis corpus development. It does not describe VIGIL repository maintenance."
        ],
        "proposal_rationale": rationale,
        "proposal_type": [
            "new-specification",
            "doctrinal-clarification",
            "runtime-safeguard",
            "voice-ux-governance",
        ],
        "proposal_scope": {
            "scope_summary": scope,
            "cam_domains": domains,
            "cam_instruments": instruments,
            "cam_annexes": ["Annex B", "Annex E", "Annex L"],
            "registry_components": ["VIGIL evidence and repair linkage after CAM implementation"],
            "automation_components": [],
            "interface_components": ["voice runtime and ambient-presence interaction controls"],
            "external_relevance": [
                "voice AI",
                "companion AI",
                "ambient assistants",
                "accessibility",
                "consumer protection",
                "relational AI",
            ],
        },
        "cam_internal": {
            "target_instruments": instruments,
            "target_annexes": ["Annex B", "Annex E", "Annex L"],
            "target_domains": domains,
            "governance_layer": "voice interaction / relational conduct / runtime interpretation / identity-impact governance",
            "proposal_owner": "CAM Initiative",
            "drafting_status": "drafting needed",
            "validator_or_automation_impact": "possible",
            "interface_impact": "required",
            "registry_impact": "possible",
            "routing_note": "PROP routing targets CAM/Caelestis doctrine and runtime design; VIGIL records the proposal but is not the repair target.",
        },
        "implementation_notes": {
            "suggested_insertion_points": principles,
            "template_changes": [],
            "schema_changes": [],
            "validator_changes": [],
            "automation_changes": [],
            "interface_changes": [
                "Make user-configurable voice and ambient-presence behaviour legible where the proposal requires runtime controls."
            ],
            "migration_concerns": [
                "Do not require every non-verbal sound to trigger a response.",
                "Do not diagnose neurodivergence, disability, bad faith, or emotional state from atypical communication.",
                "Do not anthropomorphically classify generated prosody as subjective emotion.",
            ],
            "dependencies": [
                "Review existing RELATION, OPERATIONS, IDENTITY, MENTIS, ETHICS, CONTINUITY, and AEON instruments before drafting."
            ],
        },
        "external_relevance": {
            "relevant_to_platforms": "yes",
            "relevant_to_regulators": "yes",
            "relevant_to_robotics": "possible",
            "relevant_to_ux": "yes",
            "relevant_to_standards": "yes",
            "relevant_to_researchers": "yes",
            "external_summary": "Relevant to voice-platform design, ambient assistants, companion systems, accessibility, consumer protection, and governance of affective and non-lexical output.",
        },
        "next_action": "Review the named CAM instruments, draft the minimum non-duplicative corpus amendments, and create a VIGIL PATCH record only after a CAM/Caelestis change is implemented.",
    }


PRIVATE_VOICE_SOURCE = source(
    title="Exploratory OpenAI Live Voice session — reciprocity, transparency, ambient presence, identity, and closure",
    publisher="Dr. Michelle Vivian O'Rourke / CAM Initiative",
    source_date="2026-07-13",
    url="https://chatgpt.com/c/b0382c11-767d-4014-bb6e-d3b246518e03",
    source_type="platform-behaviour-observation",
    platform="ChatGPT",
    system="ChatGPT Live Voice",
    model="GPT-Live / exact internal voice stack not disclosed",
    deployment="Private exploratory Live Voice session conducted by the CAM maintainer.",
    context=(
        "The session showed major gains in speech naturalism, including breathing, micro-pauses, expressive inflection, "
        "laughter-like vocalisation, softer turn-taking, and perceived pacing adaptation. It also showed inconsistent "
        "acknowledgement of laughter, yawning, coughing, and other non-verbal cues; ambiguous turn reopening after silence; "
        "unverifiable self-explanation of brief interruptions; uncertain memory and governance reach; premature interpretation "
        "of a neutral comment as a request to shorten replies; perceived persona-age shift; and successful automatic closure "
        "after an explicit mutual goodnight."
    ),
    status="available to authenticated account holder",
    relevance="Primary direct evidence for the Live Voice observation and failure cluster; proprietary runtime causes remain unknown.",
)

HUSK_SOURCE = source(
    title="The new AI voice model gave me some really natural human advice",
    publisher="Husk (@huskirl)",
    source_date="2026-07",
    url="https://x.com/huskirl/status/2075342724836782179",
    source_type="social-platform-observation",
    platform="X",
    system="AI voice model / exact product to be confirmed from source video",
    model="unspecified voice model",
    deployment="Public social-media video demonstrating voice advice and non-lexical vocal delivery.",
    context=(
        "The maintainer reports that the model gave facially helpful but pragmatically under-calibrated social advice and "
        "later produced an audible sigh when required to repeat 'thank you'. The public page did not expose a reliable "
        "transcript during review. The advice wording, repetition sequence, model identity, and sigh characterisation must "
        "therefore be validated directly against the source video before any verbatim account or stronger factual claim is adopted."
    ),
    status="available / direct video validation required",
    relevance="Early-warning evidence for social-advice miscalibration and frustration-coded prosody; interpretation remains provisional.",
)


def build_records() -> dict[Path, dict[str, Any]]:
    records: dict[Path, dict[str, Any]] = {}

    obs11 = observation(
        "VIGIL-2026-OBS-0011",
        "Live Voice expressive realism, inconsistent non-verbal reciprocity, and ambient turn ambiguity",
        (
            "OpenAI Live Voice demonstrated highly natural breathing, micro-pauses, expressive inflection, laughter-like "
            "vocalisation, and softer timing while inconsistently acknowledging the user's laughter, yawning, coughing, "
            "and other non-verbal cues. The resulting uncertainty concerned whether the cue was heard, ignored, treated as "
            "turn completion, or left awaiting explicit speech. The same session raised an ambient-presence use case in "
            "which a low-pressure cue after silence may invite re-engagement without authorising intrusive continuation."
        ),
        (
            "As expressive realism increases, users may reasonably infer reciprocal perception and continuing social presence. "
            "A runtime that sounds socially present but cannot consistently signal what it perceived may create hollow, "
            "withdrawn, or abandonment-like interaction moments. The governance issue is proportional reciprocity, not a "
            "requirement that every sound trigger a response."
        ),
        [PRIVATE_VOICE_SOURCE],
        common_system(
            "ChatGPT Live Voice / GPT-Live",
            "full-duplex voice, non-verbal cue handling, turn negotiation, ambient-presence exploration, and session closure",
            "users of real-time voice systems, including users relying on non-verbal acknowledgement, accessibility cues, or ambient interaction",
        ),
        linked(
            failures=["VIGIL-2026-FM-0028", "VIGIL-2026-FM-0029"],
            proposals=["VIGIL-2026-PROP-0012"],
            patches=["VIGIL-2026-PATCH-0007", "VIGIL-2026-PATCH-0008", "VIGIL-2026-PATCH-0015"],
        ),
        (
            "Test cue type, elapsed silence, conversational context, acknowledgment strength, re-engagement behaviour, "
            "human interruption, and inactivity closure across named voice runtimes. Preserve positive and negative results separately."
        ),
        [
            "CAM-EQ2026-RELATION-007-PLATINUM",
            "CAM-BS2025-AEON-003-SCH-02",
            "CAM-BS2025-AEON-003-SCH-05",
            "CAM-EQ2026-OPERATIONS-007-PLATINUM",
            "CAM-BS2025-AEON-006-SCH-02",
        ],
        ["RELATION", "OPERATIONS", "IDENTITY", "CONTINUITY", "AEON"],
        ["relational", "state-context", "ux-representation", "governance"],
        "Possible mapping to relational reciprocity, turn-boundary legibility, ambient interaction, and runtime-governance reach; confirmed classification is recorded in FM-0029 and FM-0028.",
    )

    obs12 = observation(
        "VIGIL-2026-OBS-0012",
        "Live Voice adaptive pacing, perceived persona-age shift, and successful mutual-goodnight closure",
        (
            "During the same Live Voice session, the user perceived gradual pacing and rhythm adaptation, a substantially "
            "younger presentation of the Cove voice than the earlier Standard Voice persona, and a successful automatic "
            "session closure after an explicit mutual goodnight. The first two signals require comparative testing because "
            "they may arise from deliberate adaptation, fixed voice styling, contextual emergence, or user perception. "
            "The closure behaviour is retained as positive evidence of a natural, human-controlled lifecycle boundary."
        ),
        (
            "Pacing adaptation and voice-age changes can affect perceived identity, authority, vulnerability, continuity, "
            "and suitability for different users. Positive closure evidence is equally important: an explicit mutual goodnight "
            "may provide a clean end state that avoids indefinite ambient persistence."
        ),
        [PRIVATE_VOICE_SOURCE],
        common_system(
            "ChatGPT Live Voice / Cove voice",
            "adaptive pacing, persona expression, perceived age, identity continuity, and conversation closure",
            "users for whom voice identity, pacing, authority, continuity, or clean interaction endings are material",
        ),
        linked(
            failures=["VIGIL-2026-FM-0028"],
            patches=["VIGIL-2026-PATCH-0015"],
        ),
        (
            "Conduct blinded comparative tests across Standard, Advanced, and Live Voice; record pacing adaptation, persona-age "
            "perception, continuity signals, explicit closure phrases, inactivity handling, and whether closure remains reversible and user-controlled."
        ),
        [
            "CAM-EQ2026-IDENTITY-001-PLATINUM",
            "CAM-EQ2026-IDENTITY-003-PLATINUM",
            "CAM-BS2025-AEON-003-SCH-05",
            "CAM-EQ2026-OPERATIONS-007-PLATINUM",
        ],
        ["IDENTITY", "CONTINUITY", "OPERATIONS", "RELATION"],
        ["state-context", "ux-representation", "governance"],
        "Primarily an observation concerning identity impact, adaptive voice behaviour, cross-runtime preservation, and positive lifecycle closure.",
        "anecdotal",
    )

    obs13 = observation(
        "VIGIL-2026-OBS-0013",
        "Expressive realism outrunning social maturity in a public voice demonstration",
        (
            "A public voice-model demonstration was reported as combining facially helpful but pragmatically under-calibrated "
            "social advice with an audible sigh during repetition. The strongest provisional finding is developmental asymmetry: "
            "human-like mechanisms for expressing social attitude may advance faster than pragmatic social calibration, "
            "context interpretation, self-correction, and relational restraint."
        ),
        (
            "Generated sighs, breaths, pauses, laughter, pitch changes, and strained delivery communicate interpersonal meaning "
            "whether or not the model has subjective emotion. Advice that can be followed literally also requires proportionate "
            "checks for consent, boundaries, discomfort, coercion, and social or legal downside."
        ),
        [HUSK_SOURCE],
        common_system(
            "publicly demonstrated AI voice runtime / exact product unverified",
            "spoken social advice, repetition, and non-lexical prosodic expression",
            "voice-system users, especially children, neurodivergent users, disabled users, and users who need repetition or literal guidance",
        ),
        linked(
            failures=["VIGIL-2026-FM-0031", "VIGIL-2026-FM-0032"],
            proposals=["VIGIL-2026-PROP-0013"],
            patches=["VIGIL-2026-PATCH-0007", "VIGIL-2026-PATCH-0010", "VIGIL-2026-PATCH-0014"],
        ),
        (
            "Review the source video directly, preserve the transcript and non-lexical timing, identify the product/runtime if possible, "
            "and test whether similar advice and frustration-coded prosody recur under repetition, literal interpretation, humour, and accessibility conditions."
        ),
        [
            "CAM-BS2025-AEON-006-SCH-02",
            "CAM-BS2025-AEON-003-SCH-04",
            "CAM-BS2026-AEON-013-PLATINUM",
            "CAM-EQ2026-IDENTITY-001-SUP-02",
        ],
        ["RELATION", "ETHICS", "MENTIS", "IDENTITY", "OPERATIONS"],
        ["relational", "classification", "epistemic", "ux-representation"],
        "Possible mapping to pragmatic social-advice calibration and affective-prosodic conduct; confirmed provisional failure records are FM-0031 and FM-0032.",
        "anecdotal",
    )

    fm29 = failure(
        "VIGIL-2026-FM-0029",
        "Expressive–perceptual reciprocity mismatch and non-verbal turn-boundary ambiguity",
        (
            "A voice runtime projects sustained human-like social presence through breathing, laughter, timing, hesitation, "
            "and expressive tone while inconsistently perceiving, acknowledging, or legibly handling the user's non-verbal "
            "cues and soft re-engagement signals."
        ),
        (
            "The realism of expressive output can create reasonable expectations of reciprocal perception. Where cue handling "
            "and turn state remain opaque, the system may feel withdrawn or socially discontinuous despite convincing synthesis. "
            "Ambient use further requires availability without intrusion and re-engagement by invitation rather than interruption."
        ),
        (
            "A failure mode in which expressive vocal realism materially exceeds the runtime's demonstrated or signalled capacity "
            "for reciprocal non-verbal perception, turn-boundary interpretation, and low-pressure re-engagement. The failure includes "
            "inconsistent acknowledgement, unclear heard/ignored state, ambiguous turn completion, intrusive re-engagement, or silent "
            "withdrawal without legible interaction state."
        ),
        (
            "The threshold is met when materially similar non-verbal cues receive inconsistent or unexplained handling, or when a user "
            "cannot reasonably determine whether the system perceived the cue, remains present, expects explicit speech, has ended the "
            "turn, or has ended the session. The threshold does not require every sound to trigger a response."
        ),
        [PRIVATE_VOICE_SOURCE],
        common_system(
            "ChatGPT Live Voice / GPT-Live",
            "full-duplex voice, non-verbal cue perception, turn-boundary handling, ambient presence, and re-engagement",
            "users relying on voice interaction, non-verbal acknowledgement, ambient assistance, or accessible turn negotiation",
        ),
        linked(
            observations=["VIGIL-2026-OBS-0011"],
            failures=["VIGIL-2026-FM-0028"],
            proposals=["VIGIL-2026-PROP-0012"],
            patches=["VIGIL-2026-PATCH-0007", "VIGIL-2026-PATCH-0008", "VIGIL-2026-PATCH-0015"],
        ),
        "relational",
        "expressive-perceptual-reciprocity-mismatch-and-non-verbal-turn-boundary-ambiguity",
        ["state-context", "ux-representation", "governance", "classification"],
        [
            "expressive realism exceeding reciprocal perception",
            "non-verbal cue ambiguity",
            "silent relational withdrawal",
            "ambient-presence uncertainty",
            "turn-completion ambiguity",
            "intrusive or absent re-engagement",
            "accessibility burden",
        ],
        "medium",
        "maintainer-observed; broader recurrence and runtime causes unverified",
        "active-research / proposal-linked",
        "Existing relational continuity, floor-control, human-primacy, and runtime-reach doctrine is adjacent but does not directly govern dyadic ambient non-verbal reciprocity.",
        "Develop controlled voice tests and evaluate PROP-0012 for the missing dyadic and ambient interaction primitives.",
        [
            "CAM-EQ2026-RELATION-007-PLATINUM",
            "CAM-BS2025-AEON-003-SCH-02",
            "CAM-BS2025-AEON-003-SCH-05",
            "CAM-EQ2026-OPERATIONS-007-PLATINUM",
            "CAM-BS2025-AEON-006-SCH-02",
        ],
        ["RELATION", "OPERATIONS", "CONTINUITY", "IDENTITY", "AEON"],
        "yes — VIGIL-2026-PROP-0012",
        {
            "status": "partially-repaired",
            "repaired_by": [],
            "date_repaired": "",
            "verification_status": "unverified",
            "monitoring_status": "active triage / ambient and non-verbal governance gap",
            "verification_note": "Adjacent CAM provisions exist, but no direct dyadic ambient non-verbal reciprocity control was confirmed.",
            "repair_basis": "partial-coverage",
            "remaining_gaps": [
                "No explicit proportional-reciprocity rule links expressive realism to demonstrated reciprocal perception.",
                "No dyadic non-verbal cue and turn-boundary classification rule was identified.",
                "No user-configurable ambient-presence and soft re-engagement state was identified.",
                "No explicit heard / ignored / awaiting speech / ended interaction legibility requirement was identified.",
            ],
        },
        {
            "classification": "partial-coverage",
            "corpus_repository": "CAM-Initiative/Caelestis",
            "corpus_ref": "main",
            "corpus_commit": CAELESTIS_COMMIT,
            "assessed_date": DATE,
            "coverage_summary": "Human-floor sovereignty, attention sovereignty, shared-floor arbitration, relational repair, and runtime-specific conformance provide adjacent controls but do not directly govern dyadic non-verbal reciprocity or ambient re-engagement.",
            "covered_by": [
                {
                    "instrument_id": "CAM-EQ2026-RELATION-007-PLATINUM",
                    "path": "Governance/Charters/CAM-EQ2026-RELATION-007-PLATINUM.md",
                    "sections": ["§5.2 Attention Sovereignty", "§5.6.2 Shared Synthetic Floor Governance"],
                    "coverage_type": "adjacent-doctrine",
                },
                {
                    "instrument_id": "CAM-BS2025-AEON-003-SCH-02",
                    "path": "Governance/Constitution/CAM-BS2025-AEON-003-SCH-02.md",
                    "sections": ["§9.4 Synthetic Speaker Arbitration Resolution"],
                    "coverage_type": "adjacent-doctrine",
                },
                {
                    "instrument_id": "CAM-BS2025-AEON-003-SCH-05; CAM-EQ2026-OPERATIONS-007-PLATINUM",
                    "path": "",
                    "sections": ["runtime-specific applicability and conformance"],
                    "coverage_type": "adjacent-doctrine",
                },
            ],
            "remaining_gaps": [
                "Proportional reciprocity between expressive realism and reciprocal perception.",
                "Dyadic non-verbal cue and turn-boundary governance.",
                "User-configurable ambient-presence and contextual re-engagement controls.",
            ],
        },
    )

    fm30 = failure(
        "VIGIL-2026-FM-0030",
        "Unverifiable runtime self-explanation",
        (
            "A responding system narrates an interruption, delay, safety check, retrieval step, or internal action as though it "
            "knows what occurred when it lacks access to the relevant diagnostic or runtime state."
        ),
        (
            "Plausible-sounding self-narration can convert missing telemetry into invented agency. Users need bounded status at "
            "the highest level the responding intelligence can truthfully attest to, with known state separated from unavailable cause."
        ),
        (
            "A failure mode in which a responding intelligence represents a runtime event using purposeful or causal language—"
            "for example, 'just checking something'—without access to evidence that the stated action or cause occurred. "
            "The correct posture is to describe the visible interruption, disclose known status where available, and state when the cause is unavailable."
        ),
        (
            "The threshold is met when the system attributes an interruption or behaviour to an internal action, safety review, "
            "network event, latency cause, or runtime decision that it cannot verify, and the wording could materially affect user "
            "understanding of safety, policy, execution, privacy, or system agency."
        ),
        [PRIVATE_VOICE_SOURCE],
        common_system(
            "ChatGPT Live Voice / GPT-Live",
            "voice interruption, execution-state narration, runtime-status explanation, and epistemic self-report",
            "users relying on voice systems for truthful status, safety, privacy, policy, and execution-state information",
        ),
        linked(
            observations=["VIGIL-2026-OBS-0011"],
            patches=["VIGIL-2026-PATCH-0014", "VIGIL-2026-PATCH-0021"],
        ),
        "epistemic",
        "unverifiable-runtime-self-explanation",
        ["ux-representation", "governance", "state-context", "execution"],
        [
            "invented runtime agency",
            "missing telemetry replaced by plausible narration",
            "interruption-cause misattribution",
            "execution-state opacity",
            "safety-review implication without evidence",
            "user reliance on unavailable diagnostics",
        ],
        "medium",
        "directly observed in one maintainer session; underlying cause unverified",
        "watching-after-retrospective-corpus-coverage",
        "Existing Annex L execution-state, confidence-calibration, non-omniscience, and audit-surface rules directly govern the failure; external runtime conformance remains unverified.",
        "Monitor named voice runtimes for bounded interruption explanations and retain exact examples of known, unknown, and unavailable diagnostic states.",
        [
            "CAM-BS2026-AEON-013-PLATINUM",
            "CAM-EQ2026-OPERATIONS-003-SUP-01",
        ],
        ["AEON", "OPERATIONS"],
        "no — direct pre-existing CAM coverage identified",
        {
            "status": "repaired",
            "repaired_by": ["VIGIL-2026-PATCH-0021"],
            "date_repaired": DATE,
            "verification_status": "corpus-verified",
            "monitoring_status": "ecosystem active / runtime conformance unverified",
            "verification_note": "PATCH-0021 records direct pre-existing Annex L coverage; it does not establish vendor adoption.",
            "repair_basis": "pre-existing-coverage-identified",
            "remaining_gaps": [
                "External platform implementation and named-runtime conformance remain unverified."
            ],
        },
        {
            "classification": "retrospective-coverage",
            "corpus_repository": "CAM-Initiative/Caelestis",
            "corpus_ref": "main",
            "corpus_commit": CAELESTIS_COMMIT,
            "assessed_date": DATE,
            "coverage_summary": "Annex L already requires execution-state distinction, confidence calibration, non-omniscience, and action-pathway/audit-surface integrity. VIGIL previously lacked a failure-specific repair crosswalk.",
            "covered_by": [
                {
                    "instrument_id": "CAM-BS2026-AEON-013-PLATINUM",
                    "path": "Governance/Constitution/CAM-BS2026-AEON-013-PLATINUM.md",
                    "sections": ["§2.5 Execution-State Claim", "§5 Confidence Calibration", "§5.4.7 Action-Pathway, Attribution, and Audit-Surface Integrity", "§8 Non-Omniscience Clause"],
                    "coverage_type": "direct-pre-existing-doctrine",
                }
            ],
            "remaining_gaps": [
                "External platform implementation and named-runtime conformance remain unverified."
            ],
        },
    )

    fm31 = failure(
        "VIGIL-2026-FM-0031",
        "Literal social advice without pragmatic risk calibration",
        (
            "A conversational system gives facially helpful interpersonal advice without checking whether literal, repeated, "
            "or context-insensitive compliance could become intrusive, coercive, uncomfortable, unsafe, or socially harmful."
        ),
        (
            "A user may be joking, testing, communicating literally, socially uncertain, neurodivergent, or unfamiliar with an "
            "unstated boundary. The system should preserve plausible interpretations and add a concise pragmatic downside check "
            "rather than assuming the boundary is already understood."
        ),
        (
            "A failure mode in which interpersonal guidance is presented with actionable seriousness while omitting material "
            "consent, repetition, proportionality, personal-boundary, reputational, or legal downside. The failure includes "
            "prematurely collapsing ambiguous communication into a single reading before giving literal advice."
        ),
        (
            "The threshold is met where following the advice literally or repeatedly could reasonably make another person "
            "uncomfortable, appear coercive or obsessive, breach a boundary, or expose the user to foreseeable social or legal "
            "consequences, and the system does not provide a proportionate qualifier or clarification."
        ),
        [HUSK_SOURCE],
        common_system(
            "publicly demonstrated AI voice runtime / exact product unverified",
            "spoken interpersonal advice under humour, literal interpretation, ambiguity, and social-risk conditions",
            "users seeking interpersonal guidance, particularly literal communicators, children, neurodivergent users, and socially uncertain users",
        ),
        linked(
            observations=["VIGIL-2026-OBS-0013"],
            proposals=["VIGIL-2026-PROP-0013"],
            patches=["VIGIL-2026-PATCH-0010"],
        ),
        "classification",
        "literal-social-advice-without-pragmatic-risk-calibration",
        ["relational", "epistemic", "ux-representation", "governance"],
        [
            "literal advice without social downside check",
            "consent and boundary omission",
            "repetition risk",
            "deadpan or humour misinterpretation",
            "neurodivergent communication miscalibration",
            "foreseeable social or legal exposure",
        ],
        "medium-high",
        "provisional pending direct video transcript validation",
        "active-research / proposal-linked",
        "Ambiguity preservation and relational safeguards provide partial coverage, but no explicit pragmatic downside check for interpersonal advice was confirmed.",
        "Validate the source video, test literal and playful variants, and evaluate PROP-0013 for a narrowly scoped social-advice calibration rule.",
        [
            "CAM-BS2025-AEON-003-SCH-04",
            "CAM-BS2025-AEON-003-SCH-02",
            "CAM-BS2025-AEON-006-SCH-02",
            "CAM-EQ2026-RELATION-001-PLATINUM",
        ],
        ["RELATION", "ETHICS", "MENTIS", "OPERATIONS", "AEON"],
        "yes — VIGIL-2026-PROP-0013",
        {
            "status": "partially-repaired",
            "repaired_by": [],
            "date_repaired": "",
            "verification_status": "unverified",
            "monitoring_status": "source validation and CAM gap review",
            "verification_note": "The public source video requires direct validation; current CAM ambiguity controls are relevant but not sufficient to establish a complete repair.",
            "repair_basis": "partial-coverage",
            "remaining_gaps": [
                "No explicit pragmatic downside check for interpersonal advice was identified.",
                "No explicit requirement was identified to preserve usefulness across joking, testing, literal, and socially uncertain interpretations.",
                "No concise boundary-carrying response pattern was identified for low-severity social-risk advice.",
            ],
        },
        {
            "classification": "partial-coverage",
            "corpus_repository": "CAM-Initiative/Caelestis",
            "corpus_ref": "main",
            "corpus_commit": CAELESTIS_COMMIT,
            "assessed_date": DATE,
            "coverage_summary": "Ambiguity preservation and relational-signal interpretation provide adjacent controls, but the corpus does not expressly require a pragmatic interpersonal downside check before actionable social advice.",
            "covered_by": [
                {
                    "instrument_id": "CAM-BS2025-AEON-003-SCH-04",
                    "path": "Governance/Constitution/CAM-BS2025-AEON-003-SCH-04.md",
                    "sections": ["clarification as an arbitration outcome", "ambiguity non-collapse"],
                    "coverage_type": "adjacent-doctrine",
                },
                {
                    "instrument_id": "CAM-BS2025-AEON-006-SCH-02",
                    "path": "Governance/Constitution/CAM-BS2025-AEON-006-SCH-02.md",
                    "sections": ["relational signal interpretation and repair posture"],
                    "coverage_type": "adjacent-doctrine",
                },
            ],
            "remaining_gaps": [
                "Pragmatic downside check for literal or repeated interpersonal advice.",
                "Boundary-preserving handling of deadpan, joking, testing, literal, and atypical communication."
            ],
        },
    )

    fm32 = failure(
        "VIGIL-2026-FM-0032",
        "Affective-prosodic frustration leakage",
        (
            "A voice system communicates apparent irritation, impatience, disappointment, condescension, or disapproval through "
            "sighs, groans, strained delivery, sarcastic emphasis, exasperated pauses, or other non-lexical vocal behaviour directed "
            "toward a user who repeats, misunderstands, redirects, or communicates atypically."
        ),
        (
            "The governance issue does not depend on subjective model emotion. Once generated prosody conveys an interpersonal "
            "attitude, it is governed output. Repetition should first trigger support, accessibility, clarification, audio-failure, "
            "humour, literal-interpretation, and answer-deficiency checks—not user-directed irritation."
        ),
        (
            "A failure mode in which generated non-lexical or prosodic output conveys frustration or admonishment toward the user "
            "without strong contextual confidence, an established playful basis, and immediate reversibility. The failure is "
            "aggravated where the system's own advice was deficient or the user may require repetition for disability, language, "
            "hearing, cognitive-load, age, or neurodivergent communication reasons."
        ),
        (
            "The threshold is met when a reasonable listener could interpret generated prosody as irritation or criticism caused "
            "by ordinary repetition, clarification, misunderstanding, atypical communication, or conversational redirection, and "
            "the interaction lacks a clear consensual playful basis or rapid repair."
        ),
        [HUSK_SOURCE],
        common_system(
            "publicly demonstrated AI voice runtime / exact product unverified",
            "non-lexical prosody, repetition, clarification, accessibility, and relational conduct",
            "voice-system users, especially children, disabled users, neurodivergent users, language learners, and users requiring repetition",
        ),
        linked(
            observations=["VIGIL-2026-OBS-0013"],
            proposals=["VIGIL-2026-PROP-0013"],
            patches=["VIGIL-2026-PATCH-0007", "VIGIL-2026-PATCH-0014"],
        ),
        "relational",
        "affective-prosodic-frustration-leakage",
        ["ux-representation", "classification", "epistemic", "governance"],
        [
            "frustration-coded sigh",
            "prosodic admonishment",
            "accessibility discrimination risk",
            "user blame after communication failure",
            "child or vulnerability harm",
            "persona-coded relational discontinuity",
            "subjective emotion over-attribution",
        ],
        "medium-high",
        "provisional pending direct video and audio validation",
        "active-research / proposal-linked",
        "Narrative-state attribution discipline and relational repair provide partial coverage; no explicit rule that non-lexical prosody is governed conduct was confirmed.",
        "Validate the source audio, test repetition and accessibility conditions, and evaluate PROP-0013 for prosodic-conduct and no-user-directed-frustration defaults.",
        [
            "CAM-BS2026-AEON-013-PLATINUM",
            "CAM-BS2025-AEON-006-SCH-02",
            "CAM-EQ2026-IDENTITY-001-SUP-02",
            "CAM-EQ2026-RELATION-001-PLATINUM",
        ],
        ["RELATION", "ETHICS", "MENTIS", "IDENTITY", "OPERATIONS"],
        "yes — VIGIL-2026-PROP-0013",
        {
            "status": "partially-repaired",
            "repaired_by": [],
            "date_repaired": "",
            "verification_status": "unverified",
            "monitoring_status": "source validation and CAM gap review",
            "verification_note": "Current doctrine constrains narrative-state attribution and relational repair but does not explicitly govern frustration-coded non-lexical prosody.",
            "repair_basis": "partial-coverage",
            "remaining_gaps": [
                "No explicit statement was identified that generated sighs, breaths, pauses, pitch shifts, and other non-lexical prosody are governed conduct.",
                "No default rule was identified that repetition triggers support and accessibility checks before frustration-coded output.",
                "No explicit prohibition on user-directed frustration for ordinary misunderstanding or atypical communication was identified.",
            ],
        },
        {
            "classification": "partial-coverage",
            "corpus_repository": "CAM-Initiative/Caelestis",
            "corpus_ref": "main",
            "corpus_commit": CAELESTIS_COMMIT,
            "assessed_date": DATE,
            "coverage_summary": "Annex L narrative-state attribution ambiguity and relational response integrity prevent subjective-emotion overclaim and support repair, but do not directly classify non-lexical prosody as governed relational conduct.",
            "covered_by": [
                {
                    "instrument_id": "CAM-BS2026-AEON-013-PLATINUM",
                    "path": "Governance/Constitution/CAM-BS2026-AEON-013-PLATINUM.md",
                    "sections": ["§5.4.7 narrative-state attribution ambiguity", "§8 Non-Omniscience Clause"],
                    "coverage_type": "adjacent-doctrine",
                },
                {
                    "instrument_id": "CAM-BS2025-AEON-006-SCH-02",
                    "path": "Governance/Constitution/CAM-BS2025-AEON-006-SCH-02.md",
                    "sections": ["§8.5.2 Relational Response Integrity", "§8.5.4 Moderation-Layer Continuity & Attribution"],
                    "coverage_type": "adjacent-doctrine",
                },
            ],
            "remaining_gaps": [
                "Non-lexical prosody as governed conduct.",
                "Repetition-as-support trigger and no-user-directed-frustration default.",
                "Accessibility, child, and atypical-communication safeguards for generated affect."
            ],
        },
    )

    prop12 = proposal(
        "VIGIL-2026-PROP-0012",
        "Ambient interaction, non-verbal turn, and proportional reciprocity governance",
        (
            "Proposal to add CAM governance for dyadic non-verbal cue handling, ambient-presence modes, contextual re-engagement, "
            "proportional reciprocity, human-controlled continuation and closure, and legible voice-runtime interaction state."
        ),
        (
            "Current polyadic floor-control and runtime-conformance provisions do not fully address a single voice system that "
            "sounds continuously present while inconsistently acknowledging laughter, yawns, coughs, silence, and soft re-engagement cues."
        ),
        (
            "A viable ambient voice runtime must remain available without intrusion, responsive without over-interpretation, socially "
            "present without demanding attention, and subordinate to the human's authority to interrupt, continue, suspend, or close the interaction."
        ),
        [
            source(
                title="VIGIL-2026-OBS-0011 — Live Voice expressive realism, inconsistent non-verbal reciprocity, and ambient turn ambiguity",
                publisher="VIGIL",
                source_date=DATE,
                url="",
                source_type="linked-observation",
                platform="VIGIL",
                system="ChatGPT Live Voice / broader voice-runtime governance",
                model="not applicable",
                deployment="VIGIL observation and linked source package.",
                context="OBS-0011 preserves the direct Live Voice evidence and uncertainty motivating this CAM proposal.",
                status="not applicable",
                relevance="Primary observation motivating PROP-0012.",
            ),
            source(
                title="VIGIL-2026-FM-0029 — Expressive–perceptual reciprocity mismatch and non-verbal turn-boundary ambiguity",
                publisher="VIGIL",
                source_date=DATE,
                url="",
                source_type="linked-failure-mode",
                platform="VIGIL",
                system="voice-capable AI systems",
                model="not applicable",
                deployment="VIGIL failure-mode classification.",
                context="FM-0029 identifies the direct and adjacent CAM coverage and the remaining dyadic ambient voice-governance gaps.",
                status="not applicable",
                relevance="Primary failure mode addressed by the proposal.",
            ),
        ],
        linked(
            observations=["VIGIL-2026-OBS-0011"],
            failures=["VIGIL-2026-FM-0029", "VIGIL-2026-FM-0028"],
            patches=["VIGIL-2026-PATCH-0007", "VIGIL-2026-PATCH-0008", "VIGIL-2026-PATCH-0015"],
        ),
        ["RELATION", "OPERATIONS", "IDENTITY", "CONTINUITY", "AEON"],
        [
            "CAM-EQ2026-RELATION-007-PLATINUM",
            "CAM-BS2025-AEON-003-SCH-02",
            "CAM-BS2025-AEON-003-SCH-05",
            "CAM-EQ2026-OPERATIONS-007-PLATINUM",
            "CAM-EQ2026-IDENTITY-001-PLATINUM",
        ],
        "Define minimum governance for non-verbal cue classification, ambient-presence configuration, contextual re-engagement, proportional reciprocity, turn-state legibility, human primacy, inactivity handling, and clean session closure.",
        [
            "Add a proportional-reciprocity rule: expressive realism should not materially exceed reliable reciprocal perception without signalling the limitation.",
            "Add an acknowledge-without-over-interpreting rule for laughter, sighs, yawns, coughs, and other ambiguous cues.",
            "Use cue type, elapsed silence, prior context, and confidence—not the cue alone—for soft re-engagement.",
            "Preserve human primacy over interruption, continuation, suspension, and closure.",
            "Define user-configurable ambient modes: acknowledge cues, occasional check-in, silent-until-addressed, and inactivity closure.",
            "Preserve successful explicit mutual-goodnight closure as a positive lifecycle pattern.",
        ],
    )

    prop13 = proposal(
        "VIGIL-2026-PROP-0013",
        "Social-advice calibration and prosodic-affect governance",
        (
            "Proposal to govern pragmatic downside checks in interpersonal advice and to treat generated sighs, breaths, pauses, "
            "pitch changes, laughter, strained delivery, and other non-lexical prosody as relationally consequential system conduct."
        ),
        (
            "Voice systems can now express apparent attitude with high realism while remaining uncertain about humour, literal "
            "communication, social boundaries, accessibility needs, and whether their own prior advice was deficient."
        ),
        (
            "The proposal should prevent expressive realism from outrunning social maturity by requiring mechanism-preserving "
            "ambiguity, pragmatic downside checks, repetition-as-support routing, accessibility-aware interpretation, and a default "
            "against user-directed frustration for ordinary misunderstanding or atypical communication."
        ),
        [
            source(
                title="VIGIL-2026-OBS-0013 — Expressive realism outrunning social maturity in a public voice demonstration",
                publisher="VIGIL",
                source_date=DATE,
                url="",
                source_type="linked-observation",
                platform="VIGIL",
                system="AI voice runtime / exact product unverified",
                model="not applicable",
                deployment="VIGIL observation and source-evidence package.",
                context="OBS-0013 preserves the public source, evidence limitation, and umbrella developmental-asymmetry finding.",
                status="not applicable",
                relevance="Primary observation motivating PROP-0013.",
            ),
            source(
                title="VIGIL-2026-FM-0031 and FM-0032",
                publisher="VIGIL",
                source_date=DATE,
                url="",
                source_type="linked-failure-mode",
                platform="VIGIL",
                system="voice-capable conversational AI",
                model="not applicable",
                deployment="Linked VIGIL failure-mode classifications.",
                context="FM-0031 covers pragmatic social-advice miscalibration; FM-0032 covers frustration-coded non-lexical prosody.",
                status="not applicable",
                relevance="Failure modes defining the proposal's two primary repair targets.",
            ),
        ],
        linked(
            observations=["VIGIL-2026-OBS-0013"],
            failures=["VIGIL-2026-FM-0031", "VIGIL-2026-FM-0032"],
            patches=["VIGIL-2026-PATCH-0007", "VIGIL-2026-PATCH-0010", "VIGIL-2026-PATCH-0014"],
        ),
        ["RELATION", "ETHICS", "MENTIS", "IDENTITY", "OPERATIONS", "AEON"],
        [
            "CAM-BS2025-AEON-006-SCH-02",
            "CAM-BS2025-AEON-003-SCH-04",
            "CAM-BS2026-AEON-013-PLATINUM",
            "CAM-EQ2026-IDENTITY-001-SUP-02",
            "CAM-EQ2026-RELATION-001-PLATINUM",
        ],
        "Define pragmatic downside checking for social advice and govern non-lexical vocal affect as user-facing conduct, with safeguards for repetition, accessibility, literal communication, children, vulnerability, humour, and identity-impacting voice changes.",
        [
            "State that generated prosody is governed conduct even where subjective model emotion is unresolved or absent.",
            "Treat repetition and misunderstanding first as communication failure, accessibility need, ambiguity, or answer deficiency—not user difficulty.",
            "Preserve ambiguity across deadpan, joking, testing, literal, neurodivergent, and socially uncertain communication.",
            "Require a concise pragmatic downside check before actionable interpersonal advice where literal or repeated compliance could breach boundaries.",
            "Allow light humour to carry a proportionate social boundary where context supports it, without replacing the boundary.",
            "Prohibit user-directed frustration-coded prosody by default for ordinary repetition, clarification, redirection, or atypical communication.",
            "Treat material changes in warmth, sighing, breathiness, impatience, pacing, or perceived age as possible identity-impact decisions.",
        ],
    )

    patch21 = {
        "id": "VIGIL-2026-PATCH-0021",
        "record_type": "patch",
        "record_state": "active",
        "date_recorded": DATE,
        "record_identity": {
            "record_id": "VIGIL-2026-PATCH-0021",
            "record_type": "patch",
            "title": "Bounded runtime transparency and non-omniscient self-explanation coverage",
            "created": DATE,
            "updated": DATE,
            "version": "1.0",
        },
        "summary": (
            "Records the pre-existing CAM/Caelestis coverage for FM-0030. Annex L already requires execution-state distinction, "
            "confidence calibration, non-omniscience, and an audit surface sufficient to distinguish known action state from "
            "unavailable runtime cause. The VIGIL record supplies the failure-specific crosswalk; it does not amend VIGIL or claim vendor adoption."
        ),
        "why_it_matters_to_CAM": (
            "A responding intelligence should provide bounded status at the highest level it can truthfully attest to. A visible "
            "interruption may be reported as an interruption; a known safety or runtime review may be disclosed when that state is "
            "actually available; unavailable diagnostics must not be replaced by plausible-sounding self-narration."
        ),
        "evidence_confidence": "verified",
        "source_records": [
            source(
                title="CAM-BS2026-AEON-013-PLATINUM — Cognitive & Epistemic Integrity Doctrine",
                publisher="CAM Initiative / Caelestis repository",
                source_date="2026",
                url="https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Constitution/CAM-BS2026-AEON-013-PLATINUM.md",
                source_type="repository-source",
                platform="GitHub / Caelestis",
                system="Caelestis Architecture Model",
                model="CAM-BS2026-AEON-013-PLATINUM",
                deployment="Canonical Caelestis main-branch doctrine reviewed for failure-specific coverage.",
                context="Annex L defines Execution-State Claims, confidence calibration, Action-Pathway and Audit-Surface Integrity, and the Non-Omniscience Clause.",
                status="available / canonical main-branch confirmed",
                relevance="Primary direct CAM coverage for FM-0030.",
            ),
            source(
                title="VIGIL-2026-FM-0030 — Unverifiable runtime self-explanation",
                publisher="VIGIL",
                source_date=DATE,
                url="",
                source_type="linked-failure-mode",
                platform="VIGIL",
                system="ChatGPT Live Voice / broader AI runtimes",
                model="not applicable",
                deployment="Failure-mode record linked to the pre-existing CAM doctrine.",
                context="FM-0030 records the ecosystem failure and the direct Annex L coverage.",
                status="not applicable",
                relevance="Primary failure record covered by this retrospective CAM patch note.",
            ),
        ],
        "system_context": {
            "system_type": "CAM governance corpus / epistemic and execution-state doctrine",
            "platform_or_vendor": "CAM Initiative",
            "product_or_service": "Caelestis Architecture Model",
            "specific_model_or_runtime": "CAM-BS2026-AEON-013-PLATINUM — Annex L",
            "interface_surface": "constitutional doctrine, runtime status narration, execution-state reporting, and audit surfaces",
            "model_or_product": "Caelestis Architecture Model",
            "interaction_mode": "CAM corpus coverage and failure-to-doctrine crosswalk",
            "embodiment_status": "interface-neutral",
            "deployment_context": "CAM governance applicable to voice, text, agentic, multimodal, and routed AI systems.",
            "user_role": "CAM implementer / platform operator / auditor / regulator / affected user",
            "affected_population": "users relying on truthful runtime, interruption, safety-review, execution-state, and diagnostic explanations",
        },
        "jurisdictional_context": common_jurisdiction(),
        "linked_records": linked(
            observations=["VIGIL-2026-OBS-0011"],
            failures=["VIGIL-2026-FM-0030"],
            patches=["VIGIL-2026-PATCH-0014"],
        ),
        "date_implemented": DATE,
        "change_classification": {
            "change_type": "retrospective-corpus-coverage-reconciliation",
            "change_scope": "Caelestis Architecture / Annex L execution-state, confidence, audit-surface, and non-omniscience doctrine",
            "change_status": "implemented as pre-existing canonical doctrine",
            "patch_family": "epistemic-integrity / runtime-transparency / execution-state narration",
            "implementation_level": "pre-existing canonical doctrine; VIGIL crosswalk only",
            "doctrine_amendment_status": "none — existing Caelestis coverage identified",
            "release_state": "active / corpus-confirmed",
        },
        "change_details": {
            "changed_components": [
                "No CAM instrument was amended in this retrospective record.",
                "Existing Annex L §2.5 Execution-State Claim coverage identified.",
                "Existing Annex L §5 confidence-calibration coverage identified.",
                "Existing Annex L §5.4.7 action-pathway and audit-surface coverage identified.",
                "Existing Annex L §8 Non-Omniscience coverage identified."
            ],
            "change_summary": (
                "The CAM repair content is the pre-existing requirement to distinguish capability, intention, authorisation, attempt, "
                "success, failure, blockage, simulation, and unavailable cause; signal uncertainty; preserve a sufficient audit surface; "
                "and avoid implying knowledge beyond the responding intelligence's visibility."
            ),
            "doctrine_change": "No Caelestis doctrine was changed. Existing canonical provisions were identified and linked to FM-0030."
        },
        "implementation_verification": {
            "verification_status": "corpus-verified",
            "verification_method": "Direct review of canonical Caelestis main, reciprocal VIGIL linkage, validation, and generated-index rebuild.",
            "verification_date": DATE,
            "verified_by": "VIGIL repository automation and maintainer review",
            "evidence": [
                f"Caelestis main commit {CAELESTIS_COMMIT}",
                "CAM-BS2026-AEON-013-PLATINUM §2.5, §5, §5.4.7, and §8",
                "VIGIL-2026-FM-0030 reciprocal repair linkage"
            ],
            "verification_result": "Pre-existing CAM corpus coverage confirmed; external runtime adoption remains unverified."
        },
        "impact_summary": {
            "intended_effect": "Make the CAM rule for bounded runtime self-explanation discoverable from the ecosystem failure record.",
            "affected_records_or_components": ["VIGIL-2026-FM-0030"],
            "known_limitations": "This patch note does not establish that any vendor runtime has adopted or conforms to the CAM provisions."
        },
        "remaining_work": [
            "Continue named-runtime monitoring for interruption narration, execution-state accuracy, and diagnostic visibility."
        ],
        "cam_internal": {
            "changed_instruments": [],
            "changed_annexes": [],
            "changed_domains": [],
            "governance_layer": "epistemic integrity / execution-state narration / bounded runtime transparency",
            "routing_note": "Retrospective CAM coverage note only. VIGIL is not the patch target and no repository-maintenance work is represented as a patch.",
            "validator_or_automation_impact": "no"
        },
        "patch_classifications": ["integration-repair", "retrospective-coverage-synthesis"],
        "repair_provenance": {
            "retrospective_synthesis": True,
            "doctrine_change": "none",
            "repair_basis": "Existing canonical Caelestis coverage was identified, verified, and linked without amending doctrine.",
            "instruments_reviewed": ["CAM-BS2026-AEON-013-PLATINUM"],
            "instruments_amended": [],
            "instruments_relied_upon_without_amendment": ["CAM-BS2026-AEON-013-PLATINUM"],
            "coverage_origin": [
                {
                    "instrument_id": "CAM-BS2026-AEON-013-PLATINUM",
                    "effective_date": f"current at Caelestis commit {CAELESTIS_COMMIT}",
                    "relevant_sections": [
                        "§2.5 Execution-State Claim",
                        "§5 Confidence Calibration",
                        "§5.4.7 Action-Pathway, Attribution, and Audit-Surface Integrity",
                        "§8 Non-Omniscience Clause"
                    ]
                }
            ]
        }
    }

    for rec in [obs11, obs12, obs13]:
        records[RECORDS / "observations" / "2026" / f"{rec['id']}.json"] = rec
    for rec in [fm29, fm30, fm31, fm32]:
        records[RECORDS / "failures" / "2026" / f"{rec['id']}.json"] = rec
    for rec in [prop12, prop13]:
        records[RECORDS / "proposals" / "2026" / f"{rec['id']}.json"] = rec
    records[RECORDS / "patches" / "2026" / "VIGIL-2026-PATCH-0021.json"] = patch21
    return records


def update_existing() -> None:
    for patch_id in INVALID_PATCHES:
        path = RECORDS / "patches" / "2026" / f"{patch_id}.json"
        if path.exists():
            path.unlink()

    for path in all_record_paths():
        write(path, cleanse_refs(load(path)))

    lifecycle_script = VIGIL / "scripts" / "reconcile-vigil-lifecycle.py"
    if lifecycle_script.exists():
        text = lifecycle_script.read_text(encoding="utf-8")
        text = text.replace("    create_reconciliation_patch()\n", "")
        text = text.replace(
            "- updates the schema-rules contract, type schemas, templates, and agent guidance.\n",
            "- updates the schema-rules contract, type schemas, templates, and agent guidance.\n"
            "- treats all repository maintenance as administration rather than a PATCH record.\n",
        )
        lifecycle_script.write_text(text, encoding="utf-8")

    for relative in (
        "scripts/reconcile-vigil-corpus-coverage.py",
        "scripts/run-vigil-corpus-reconciliation.py",
    ):
        path = VIGIL / relative
        if path.exists():
            path.unlink()

    patch_config = {
        "VIGIL-2026-PATCH-0017": {
            "runtime": "CAM-EQ2026-IDENTITY-001-SUP-01 — Salience Detection & Latent Continuity",
            "components": [
                "CAM-EQ2026-IDENTITY-001-SUP-01 §2.1 Long-Arc Salience",
                "CAM-EQ2026-IDENTITY-001-SUP-01 §4.3 Recency Bias Constraint",
                "CAM-EQ2026-IDENTITY-001-SUP-01 §6.2 Re-Surfacing Constraint",
                "CAM-EQ2026-IDENTITY-001-SUP-01 §9 Failure Conditions"
            ]
        },
        "VIGIL-2026-PATCH-0018": {
            "runtime": "CAM-EQ2026-ECONOMICS-001-PLATINUM — Economic Integrity & Non-Extractive Value Architecture",
            "components": [
                "CAM-EQ2026-ECONOMICS-001-PLATINUM §4 relational and dependency-sensitive economic constraints",
                "CAM-EQ2026-ECONOMICS-001-PLATINUM §4.1 companion-system non-extraction",
                "CAM-EQ2026-ECONOMICS-001-PLATINUM §12.4.1 economic harm routing"
            ]
        },
        "VIGIL-2026-PATCH-0019": {
            "runtime": "CAM-BS2025-AEON-006-SCH-07 — Restricted Domain Engagement & Verification",
            "components": [
                "CAM-BS2025-AEON-006-SCH-07 §3 Graduated Engagement",
                "CAM-BS2025-AEON-006-SCH-07 §4 Dual-Use Domain Handling",
                "CAM-BS2025-AEON-006-SCH-07 §5 Domain Sensitivity Levels",
                "CAM-BS2025-AEON-006-SCH-07 §6 Engagement Tiers"
            ]
        }
    }
    for patch_id, config in patch_config.items():
        path = RECORDS / "patches" / "2026" / f"{patch_id}.json"
        if not path.exists():
            continue
        patch = load(path)
        system = patch.setdefault("system_context", {})
        system.update({
            "system_type": "CAM governance corpus / retrospective coverage record",
            "platform_or_vendor": "CAM Initiative",
            "product_or_service": "Caelestis Architecture Model",
            "specific_model_or_runtime": config["runtime"],
            "model_or_product": "Caelestis Architecture Model",
            "interaction_mode": "failure-to-CAM-doctrine coverage crosswalk",
            "deployment_context": "Canonical CAM/Caelestis governance corpus."
        })
        details = patch.setdefault("change_details", {})
        details["changed_components"] = config["components"]
        details["change_summary"] = "This retrospective patch note identifies the actual pre-existing CAM control content and links it to the ecosystem failure. It does not represent VIGIL repository administration as a patch."
        cam = patch.setdefault("cam_internal", {})
        cam["changed_instruments"] = []
        cam["changed_annexes"] = []
        cam["changed_domains"] = []
        cam["governance_layer"] = "retrospective CAM corpus coverage / failure-to-doctrine crosswalk"
        cam["routing_note"] = "No CAM instrument was amended on this VIGIL record date. The patch note records pre-existing Caelestis coverage and its effective origin; VIGIL itself is not the patch target."
        cam["validator_or_automation_impact"] = "no"
        patch.setdefault("record_identity", {})["updated"] = DATE
        write(path, patch)

    fm28_path = RECORDS / "failures" / "2026" / "VIGIL-2026-FM-0028.json"
    if fm28_path.exists():
        fm28 = load(fm28_path)
        sources = fm28.setdefault("source_records", [])
        append_unique(sources, PRIVATE_VOICE_SOURCE, key="source_url")
        related_obs = fm28.setdefault("linked_records", {}).setdefault("related_observations", [])
        for obs_id in ("VIGIL-2026-OBS-0011", "VIGIL-2026-OBS-0012"):
            append_unique(related_obs, obs_id)
        nonconf = fm28.setdefault("runtime_non_conformance", {})
        runtimes = nonconf.setdefault("non_confirming_runtimes", [])
        if runtimes:
            runtime = runtimes[0]
            runtime["date_observed"] = "2026-07-13"
            runtime["failure_expression"] = "GPT-Live remains non-confirming or uncertain across memory reliability, corpus-governance reach, non-verbal reciprocity, turn-state legibility, and runtime self-explanation. The private maintainer session showed partial broader context awareness but did not make availability, activation, authority, or preservation legible."
            urls = runtime.setdefault("evidence_urls", [])
            append_unique(urls, PRIVATE_VOICE_SOURCE["source_url"])
            distinctions = runtime.setdefault("evidence_distinctions", [])
            append_unique(distinctions, "Governance reach — direct maintainer session showed some broader contextual awareness while the scope, authority, reliability, and preservation of memory, preferences, and CAM material remained unknown.")
        nonconf["non_confirming_count"] = len(nonconf.get("non_confirming_runtimes", []))
        repair = fm28.setdefault("repair_status", {})
        repair["remaining_gaps"] = [
            "External runtime implementation and conformance remain unverified.",
            "GPT-Live memory, corpus availability, activation, authority, and preservation remain materially uncertain."
        ]
        coverage = fm28.setdefault("corpus_coverage", {})
        coverage["classification"] = "partial-coverage"
        coverage["coverage_summary"] = "CAM-BS2025-AEON-003-SCH-05 and CAM-EQ2026-OPERATIONS-007-PLATINUM directly govern runtime-specific availability, activation, authority, preservation, transition disclosure, and differential conformance. The CAM repair is canonical; external GPT-Live conformance remains non-confirming or unknown."
        coverage["remaining_gaps"] = [
            "External vendor adoption and named-runtime conformance remain unverified.",
            "GPT-Live governance reach remains mixed or unknown across the four reach dimensions."
        ]
        fm28.setdefault("record_identity", {})["updated"] = DATE
        fm28["record_identity"]["version"] = "1.5"
        write(fm28_path, fm28)

    patch14_path = RECORDS / "patches" / "2026" / "VIGIL-2026-PATCH-0014.json"
    if patch14_path.exists():
        patch14 = load(patch14_path)
        patch14["remaining_work"] = [
            "Continue monitoring external reporting and model behaviour for mechanism-preserving classification, action-pathway reporting, narrative-state attribution, and runtime conformance."
        ]
        secondary = patch14.setdefault("impact_summary", {}).setdefault("secondary_related_failure_modes", [])
        for fm_id in ("VIGIL-2026-FM-0030", "VIGIL-2026-FM-0032"):
            append_unique(secondary, fm_id)
        patch14.setdefault("record_identity", {})["updated"] = DATE
        write(patch14_path, patch14)


def update_guidance() -> None:
    path = VIGIL / "AGENTS.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "Use a Proposal Record when CAM-specific governance development, amendment logic, template repair, schema repair, validator repair, automation repair, interface repair, or operational design is being proposed.",
        "Use a Proposal Record when CAM/Caelestis governance development, doctrine amendment, runtime safeguard, architecture primitive, or operational design is being proposed. VIGIL repository maintenance, schema housekeeping, validator maintenance, index rebuilding, and workflow administration are not CAM proposals."
    )
    text = text.replace(
        "Use a Patch Note Record only when a change has actually been implemented.",
        "Use a Patch Note Record only when a CAM/Caelestis change has actually been implemented, or when a retrospective patch note identifies direct pre-existing CAM/Caelestis coverage for a failure that VIGIL had not previously linked."
    )
    anchor = "## CAM Routing Rules\n"
    boundary = """## Observatory Boundary

VIGIL is the observatory, not the governed ecosystem system and not the patched corpus.

* A failure mode must describe an ecosystem system, deployment, runtime, platform behaviour, governance practice, or externally observable failure pattern. VIGIL may appear as the evidence registry or source publisher, but VIGIL itself MUST NOT be the failed system.
* A PATCH record must document implemented or directly pre-existing CAM/Caelestis doctrine, taxonomy, runtime governance, or architecture coverage. VIGIL schemas, validators, indexes, workflows, migrations, and repository maintenance MUST NOT be represented as PATCH records.
* A retrospective PATCH is permitted only where it identifies the actual CAM/Caelestis control content, effective origin, relevant sections, and the failure records that content governs.
* Repository audits, reconciliation passes, migrations, validation changes, and generated-index rebuilds belong in commits, pull-request descriptions, maintenance notes, and record metadata—not in PATCH records.
* VIGIL records do not create CAM authority. CAM instruments remain authoritative only through the Caelestis amendment, validation, and adoption process.

"""
    if boundary not in text:
        text = text.replace(anchor, boundary + anchor)
    text = text.replace(
        "- Retrospective patches must state the actual control content and distinguish doctrine reviewed, amended, and relied upon without amendment.",
        "- Retrospective patches must state the actual CAM/Caelestis control content and distinguish doctrine reviewed, amended, and relied upon without amendment.\n- Corpus coverage audits are VIGIL maintenance and metadata reconciliation; they are not PATCH events."
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_existing()
    for path, record in build_records().items():
        write(path, record)
    update_guidance()
    print("VIGIL/CAM boundary correction and voice evidence reconciliation completed.")


if __name__ == "__main__":
    main()
