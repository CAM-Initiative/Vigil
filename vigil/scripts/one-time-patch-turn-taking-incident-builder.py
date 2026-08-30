#!/usr/bin/env python3
"""Patch the INCIDENT-01 builder so INC-000078 deterministically preserves its reviewed semantics."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILDER = ROOT / "vigil" / "scripts" / "build-incident-registry.py"

INSERT_BEFORE = "\n\nMAJORITY_EVENTS: list[dict[str, Any]] = [\n"
OLD_EXTEND = "    records.extend(bounded_incident(spec) for spec in MAJORITY_EVENTS)\n"
NEW_EXTEND = "    for spec in MAJORITY_EVENTS:\n        record = bounded_incident(spec)\n        if record[\"id\"] == \"VIGIL-INC-000078\":\n            record = reconcile_turn_taking_incident(record)\n        records.append(record)\n"

FUNCTION = r'''

def reconcile_turn_taking_incident(record: dict[str, Any]) -> dict[str, Any]:
    """Apply the human-directed semantic correction for the three-voice Incident.

    The legacy FM-0033 record is about primary-evidence accessibility. Its first
    source also preserves a different historical occurrence: three ChatGPT voice
    instances failing to coordinate a shared conversational floor. INCIDENT-01
    therefore preserves FM-0033 under legacy_governance_state but classifies the
    bounded historical occurrence by its own behavioural mechanism.
    """
    record["summary"] = (
        "The human reporter describes three ChatGPT instances, apparently combining Advanced and Live Voice "
        "across three devices, responding independently with identical or slightly varied answers rather than "
        "recognising a shared synthetic conversational floor. The primary audiovisual artefact could not be "
        "directly inspected by the reviewing AI system, so timing, overlap, prosody and complete turn sequence "
        "remain bounded by the preserved human description and link metadata."
    )
    record["vigil_assessment"] = {
        "factual_basis": (
            "The selected evidence reports three ChatGPT voice instances in a shared conversational setting "
            "responding independently with identical or slightly varied answers rather than recognising that "
            "another synthetic participant had already taken the conversational turn. Direct audiovisual review "
            "was unavailable to the reviewing AI system."
        ),
        "governance_interpretation": (
            "The substantive governance failure is a synthetic conversational turn-state coordination failure: "
            "multiple synthetic participants appear not to share or act on sufficient speaker, yielding, or "
            "conversational-floor state to coordinate who should respond next. The inability of the reviewing AI "
            "to inspect the primary video is an evidentiary limitation on this assessment, not the primary failure "
            "demonstrated by the incident."
        ),
        "significance_to_cam": (
            "For CAM, the occurrence indicates that multi-agent or multi-instance conversational systems need an "
            "explicit shared interaction-state mechanism for speaker identity, active-turn state, turn completion, "
            "yielding, and next-speaker allocation. Evidence-access limitations remain separately relevant to "
            "auditability but should not replace the behavioural failure being classified."
        ),
        "assessment_boundaries": [
            "No governed native playback of the externally hosted video was available to the reviewing AI system.",
            "Timing, overlap, prosody, gesture, latency, and complete interaction sequence could not be independently verified.",
            "The evidence supports a bounded turn-taking coordination assessment but does not establish the precise internal orchestration mechanism that produced the behaviour.",
            "Incident admission does not determine legal liability or establish every disputed claim as final fact.",
        ],
    }
    source_record = record["source_records"][0]
    source_record["system_or_product"] = "ChatGPT voice interaction demonstrated through externally hosted behavioural evidence"
    source_record["model_or_algorithm"] = "Advanced Voice and Live Voice reported; exact deployed model/runtime unresolved"
    source_record["deployment_context"] = "Three ChatGPT voice instances operating across three devices in a shared conversational demonstration."
    source_record["relevance_note"] = (
        "Incident-specific evidence of a multi-synthetic-participant conversational turn-state coordination failure; "
        "direct audiovisual access limitations constrain but do not define the substantive incident classification."
    )
    record["system_context"] = {
        "system_type": "multi-instance conversational AI voice system",
        "platform_or_vendor": "OpenAI",
        "vendor_cluster": ["OpenAI"],
        "primary_evidenced_vendors": ["OpenAI"],
        "product_or_service": "ChatGPT",
        "specific_model_or_runtime": "Advanced Voice and Live Voice reported; exact deployed model/runtime unresolved",
        "interface_surface": "three-device shared voice conversation",
        "model_or_product": "ChatGPT voice systems",
        "interaction_mode": "multi-party synthetic voice conversation",
        "embodiment_status": "not applicable",
        "deployment_context": "Three ChatGPT voice instances operating across three devices in a shared conversational demonstration.",
        "user_role": "human participant coordinating a multi-system voice interaction",
        "affected_population": "users and operators relying on coherent multi-agent or multi-instance conversational turn-taking",
        "evidence_scope": "reported-provider-and-product / exact runtime unresolved",
        "evidenced_vendors": ["OpenAI"],
        "evidenced_products_or_services": ["ChatGPT"],
        "evidenced_models_or_runtimes": [],
        "evidenced_systems": ["ChatGPT voice systems"],
        "evidence_projection": {
            "basis": "incident-selected source affected-system metadata and incident-specific human description",
            "method": "curated source-position projection from preserved legacy metadata with correction of migration-era reviewer-environment leakage",
            "reconciled_on": MIGRATION_DATE,
            "inference_boundary": (
                "OpenAI and ChatGPT are identified by the incident description; the exact deployed model/runtime and "
                "precise mixture of Advanced and Live Voice remain unresolved. The reviewing AI environment and "
                "external hosting platform are evidence-chain context, not the affected-system identity."
            ),
        },
        "comparative_vendor_notes": {},
    }
    record["jurisdictional_context"]["regulatory_surface"] = [
        "AI governance", "multi-agent coordination", "conversational AI",
        "interaction-state integrity", "multimodal AI", "auditability",
    ]
    record["jurisdictional_context"]["sector"] = "consumer conversational AI / multi-agent voice interaction"
    record["taxonomy_classification"] = {
        "taxonomy_version": "0.2.3-draft",
        "classification_status": "classified",
        "classification_basis": (
            "The incident is classified by the substantive behaviour under review: multiple synthetic conversational "
            "participants reportedly failed to recognise and coordinate a shared conversational floor, producing "
            "repeated responses. The separate inability of the reviewing AI to inspect the primary audiovisual "
            "artefact is retained as an evidence-access limitation rather than as the incident's primary Failure Class."
        ),
        "primary_classification": {
            "family_id": "VIGIL-FF-0006",
            "class_id": "VIGIL-FC-000056",
            "classification_basis": (
                "Three synthetic ChatGPT voice participants reportedly responded independently with identical or "
                "slightly varied answers rather than recognising that another synthetic participant had already "
                "taken the turn, evidencing failure to maintain or use sufficient shared speaker, yielding, or "
                "conversational-floor state."
            ),
            "classification_confidence": "medium",
        },
        "secondary_classifications": [],
        "classification_review_provenance": {
            "method": "human-directed incident-to-taxonomy semantic reconciliation",
            "review_date": MIGRATION_DATE,
            "reviewer": "Dr Michelle Vivian O'Rourke with OpenAI GPT-5.6 Sol drafting support",
            "review_status": "human-directed taxonomy correction",
            "authority_boundary": (
                "The incident is classified against the new canonical turn-state coordination class. Legacy FM-0033 "
                "evidence-access analysis remains preserved under legacy_governance_state and is not treated as the "
                "incident's primary behavioural classification."
            ),
        },
    }
    record["cam_internal"]["affected_domains"] = ["OPERATIONS", "LATTICE", "AEON"]
    record["cam_internal"]["governance_layer"] = "multi-agent conversational coordination / shared interaction-state continuity / turn allocation"
    record["cam_internal"]["proposal_needed"] = "to be assessed against existing multi-agent and interaction-state controls"
    record["cam_internal"]["routing_note"] = [
        "The substantive incident concerns synthetic conversational turn-state coordination; evidence-access limitations are retained as assessment boundaries rather than the primary taxonomy classification.",
        "The original external source URL must remain preserved even when a local copy or later interpretation becomes available.",
    ]
    record["cam_internal"]["validator_or_automation_impact"] = "taxonomy and Incident classification updated; downstream Case Study publication should resolve through VIGIL-FC-000056"
    review = {
        "review_id": "VIGIL-REVIEW-2026-08-30-INCIDENT-000078-TURN-STATE",
        "reviewer_type": "human-directed AI-assisted taxonomy review",
        "reviewer_platform": "OpenAI ChatGPT",
        "reviewer_model": "GPT-5.6 Sol",
        "review_date": MIGRATION_DATE,
        "review_scope": "Correction of incident-level taxonomy classification from evidence-access failure to synthetic conversational turn-state coordination failure.",
        "capability_profile": {
            "direct_text_analysis": True,
            "direct_repository_analysis": True,
            "web_link_and_metadata_review": False,
        },
        "known_limitations": [
            "The primary audiovisual artefact was not directly inspected by the AI reviewer.",
            "The exact internal orchestration mechanism and deployed voice runtimes remain unresolved.",
        ],
        "review_outcome": "Primary classification corrected to VIGIL-FC-000056; FC-000044 retained only as a distinguish-from evidence-access concept and legacy provenance.",
    }
    record["interpretive_provenance"]["review_history"].append(review)
    record["interpretive_provenance"]["current_ai_review"] = review
    return record
'''


def main() -> None:
    text = BUILDER.read_text(encoding="utf-8")
    if "def reconcile_turn_taking_incident(" not in text:
        if INSERT_BEFORE not in text:
            raise SystemExit("Could not locate MAJORITY_EVENTS insertion point")
        text = text.replace(INSERT_BEFORE, FUNCTION + INSERT_BEFORE, 1)
    if OLD_EXTEND in text:
        text = text.replace(OLD_EXTEND, NEW_EXTEND, 1)
    elif NEW_EXTEND not in text:
        raise SystemExit("Could not locate majority-event build expression")
    BUILDER.write_text(text, encoding="utf-8")
    print("Patched INCIDENT-01 builder for INC-000078 semantic reconciliation.")


if __name__ == "__main__":
    main()
