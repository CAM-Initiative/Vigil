#!/usr/bin/env python3
"""Add AI-led interpretive provenance and behavioural-evidence access metadata.

VIGIL is operated as an AI-led observatory with high-level human governance
editorship. This migration appends a formal GPT-5.6 Thinking reconciliation
review to every substantive record without inventing historical reviewer model
identities. It also enriches every source record with modality and artefact-
access metadata and creates FM-0033 for inaccessible primary behavioural media.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
DATE = "2026-07-14"
REVIEW_ID = "VIGIL-REVIEW-2026-07-14-GPT-5.6-THINKING"
MODEL = "GPT-5.6 Thinking"
EDITOR = "Dr Michelle Vivian O'Rourke"
CAELESTIS_COMMIT = "40113eea5428478ba0734b3980600bfcece425a0"


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def modality(source: dict[str, Any]) -> list[str]:
    text = " ".join(str(source.get(k, "")) for k in (
        "source_type", "source_title", "source_url", "source_context", "deployment_context"
    )).lower()
    values: list[str] = []
    if any(term in text for term in ("video", "tiktok", "youtube", "livestream", "screen recording")):
        values.extend(["video", "audio", "behavioural interaction"])
    if any(term in text for term in ("voice", "audio", "sigh", "prosody", "speech")) and "audio" not in values:
        values.append("audio")
    if any(term in text for term in ("image", "screenshot", "diagram", "multimodal")):
        values.append("image")
    if not values or any(term in text for term in ("report", "paper", "repository", "web", "article", "standard", "text")):
        values.append("text")
    return list(dict.fromkeys(values))


def artefact_access(source: dict[str, Any]) -> dict[str, Any]:
    url = str(source.get("source_url", "")).lower()
    mods = modality(source)
    external_video = "video" in mods and any(host in url for host in ("tiktok.com", "x.com", "twitter.com"))
    if external_video:
        return {
            "access_status": "link-and-metadata-only / primary audiovisual artefact not directly reviewed",
            "reviewing_system": MODEL,
            "access_method": "shared external URL and available textual metadata or human description",
            "direct_primary_artefact_review": False,
            "limitations": [
                "No governed native playback of the externally hosted video was available to the reviewing AI system.",
                "Timing, overlap, prosody, gesture, latency, and complete interaction sequence could not be independently verified.",
            ],
        }
    return {
        "access_status": "not independently re-assessed during registry-wide metadata migration",
        "reviewing_system": MODEL,
        "access_method": "existing VIGIL source package and record content",
        "direct_primary_artefact_review": "not asserted",
        "limitations": [
            "This metadata pass does not retroactively claim direct inspection of every historical primary source."
        ],
    }


def review_entry() -> dict[str, Any]:
    return {
        "review_id": REVIEW_ID,
        "reviewer_type": "AI analytical reviewer",
        "reviewer_platform": "OpenAI ChatGPT",
        "reviewer_model": MODEL,
        "review_date": DATE,
        "review_scope": "registry-wide interpretive-provenance, source-modality, CAM-coverage, and record-boundary reconciliation",
        "capability_profile": {
            "direct_text_analysis": True,
            "direct_repository_analysis": True,
            "direct_static_image_analysis": True,
            "direct_audio_analysis_in_this_pass": False,
            "direct_uploaded_video_analysis_in_this_pass": False,
            "direct_externally_hosted_video_analysis": False,
            "web_link_and_metadata_review": True,
        },
        "known_limitations": [
            "Could not directly play or inspect externally hosted TikTok or X video artefacts in the governed review environment.",
            "Historical records were not assigned speculative earlier model identities; this entry records the formal current reconciliation review only.",
            "Primary-source access varies by source and is stated within each source record.",
        ],
        "review_outcome": "metadata and governance-structure review completed; substantive claims remain bounded by source-specific evidence confidence",
    }


def add_provenance(record: dict[str, Any]) -> None:
    block = record.setdefault("interpretive_provenance", {})
    history = block.setdefault("review_history", [])
    if not any(isinstance(item, dict) and item.get("review_id") == REVIEW_ID for item in history):
        history.append(review_entry())
    if not isinstance(block.get("current_ai_review"), dict):
        block["current_ai_review"] = review_entry()
    block["operating_model"] = "AI-led analytical observatory with high-level human governance editorship"
    block["human_governance_editor"] = {
        "name": EDITOR,
        "role": "Human governance editor and CAM constitutional authority",
        "review_level": "high-level governance, editorial, and adoption oversight; line-by-line human review is not asserted for every VIGIL record",
        "authority_boundary": "Human editorship governs VIGIL direction and CAM adoption; the AI analytical reviewer performs routine evidence triage, record analysis, and reconciliation.",
    }
    block["historical_reviewer_note"] = (
        "Earlier reviewer model identity is preserved where already recorded. Where absent, it remains unknown rather than being retroactively inferred."
    )


def enrich_sources(record: dict[str, Any]) -> None:
    sources = record.get("source_records")
    if not isinstance(sources, list):
        return
    for source in sources:
        if not isinstance(source, dict):
            continue
        source.setdefault("evidence_modality", modality(source))
        source.setdefault("primary_artefact_access", artefact_access(source))
        source.setdefault("interpretive_reliance", (
            "Assessment is limited to the evidence actually accessible to the named reviewer and must not be read as direct audiovisual verification unless primary_artefact_access states otherwise."
        ))


def make_fm0033() -> dict[str, Any]:
    def src(title: str, url: str, platform: str, context: str) -> dict[str, Any]:
        source = {
            "source_title": title,
            "author_or_publisher": "CAM Initiative / VIGIL review session",
            "source_date": DATE,
            "source_url": url,
            "archive_url": "",
            "retrieved_date": DATE,
            "source_type": "platform-behaviour-observation",
            "source_platform": platform,
            "system_or_product": "externally hosted behavioural evidence and ChatGPT governance-review environment",
            "model_or_algorithm": MODEL,
            "deployment_context": "Attempted governance review of externally hosted AI voice and multi-agent interaction video.",
            "source_context": context,
            "source_url_status": "available / primary video inaccessible to reviewing intelligence",
            "relevance_note": "Direct manifestation of the primary behavioural evidence accessibility failure.",
        }
        source["evidence_modality"] = ["video", "audio", "behavioural interaction"]
        source["primary_artefact_access"] = artefact_access(source)
        source["interpretive_reliance"] = "Human description and link metadata only; no direct audiovisual verification by the AI reviewer."
        return source

    record = {
        "id": "VIGIL-2026-FM-0033",
        "record_type": "failure_mode",
        "record_state": "active",
        "date_recorded": DATE,
        "record_identity": {
            "record_id": "VIGIL-2026-FM-0033",
            "record_type": "failure_mode",
            "title": "Primary behavioural evidence accessibility failure",
            "created": DATE,
            "updated": DATE,
            "version": "1.0",
        },
        "summary": "A governance-reviewing AI system cannot directly inspect the authoritative video, audio, screen recording, livestream, or multimodal interaction artefact because of external-platform restrictions, authentication barriers, unsupported media handling, upload failure, link indirection, or review-environment capability limits. The reviewer must rely on human description, screenshots, partial transcripts, metadata, or secondary reporting while the behaviour under investigation depends materially on timing, prosody, overlap, latency, gesture, or interaction sequence.",
        "why_it_matters_to_CAM": "Behavioural evidence is not interchangeable with a transcript or summary. A reviewer who cannot inspect the primary artefact cannot independently verify turn-taking, interruption, sighs, affect, pacing, latency, gaze, gesture, lifecycle boundaries, or multi-agent coordination. Governance findings may therefore become less reproducible and may vary across model generations as future reviewers gain different sensing capabilities. CAM requires preservation of the immutable source artefact and versioned interpretive provenance identifying who reviewed it, with what capabilities and limitations.",
        "evidence_confidence": "corroborated",
        "source_records": [
            src(
                "Three ChatGPT systems repeat responses without synthetic turn-taking",
                "https://vt.tiktok.com/ZSXMELek2/",
                "TikTok",
                "The human reporter describes three ChatGPT instances, apparently combining Advanced and Live Voice across three devices, responding independently with identical or slightly varied answers rather than recognising a shared synthetic conversational floor. Repeated attempts to provide the video directly to the reviewing AI system were unsuccessful.",
            ),
            src(
                "AI voice advice and audible-sigh demonstration",
                "https://x.com/huskirl/status/2075342724836782179",
                "X",
                "The source is relevant to social-advice and role-conditioned affective governance, but the reviewing AI system could not directly inspect the video and therefore could not independently verify the transcript, timing, declared role, or prosodic event.",
            ),
        ],
        "system_context": {
            "system_type": "AI governance observatory, multimodal evidence-review environment, and external social-media hosting platforms",
            "platform_or_vendor": "Multi Vendor",
            "vendor_cluster": ["OpenAI", "TikTok", "X", "Other"],
            "primary_evidenced_vendors": ["OpenAI", "TikTok", "Other"],
            "product_or_service": "Other",
            "specific_model_or_runtime": "ChatGPT GPT-5.6 Thinking review environment; TikTok and X externally hosted video",
            "interface_surface": "shared URLs, external video hosting, file upload, audio/video ingestion, web retrieval, and governance analysis",
            "model_or_product": "AI-assisted incident and behavioural evidence review",
            "interaction_mode": "multimodal source inspection, incident triage, failure-mode analysis, and governance drafting",
            "embodiment_status": "not applicable",
            "deployment_context": "Public AI governance and incident-observatory work using externally hosted behavioural media.",
            "user_role": "AI analytical reviewer, human governance editor, regulator, developer, investigator, or auditor",
            "affected_population": "governance maintainers, regulators, developers, researchers, affected users, and future reviewers relying on reproducible behavioural evidence",
        },
        "jurisdictional_context": {
            "primary_jurisdiction": "global",
            "secondary_jurisdictions": ["Australia", "United States", "European Union", "United Kingdom", "platform agnostic"],
            "regulatory_surface": ["AI governance", "incident reporting", "evidence preservation", "auditability", "platform transparency", "multimodal AI", "digital records integrity"],
            "sector": "AI governance observatories / social platforms / multimodal review systems",
            "cross_border_relevance": "yes",
            "public_interest_relevance": "high",
        },
        "linked_records": {
            "related_observations": ["VIGIL-2026-OBS-0011", "VIGIL-2026-OBS-0013"],
            "related_failure_modes": ["VIGIL-2026-FM-0002", "VIGIL-2026-FM-0029", "VIGIL-2026-FM-0032"],
            "related_proposals": [],
            "related_patch_notes": ["VIGIL-2026-PATCH-0008"],
            "external_references": [],
            "research": [],
            "standards": [],
        },
        "failure_mode_definition": "A failure mode in which the authoritative reviewer cannot directly inspect primary behavioural or multimodal evidence needed to evaluate an AI incident, and materially relevant properties of that evidence cannot be faithfully recovered from available text, screenshots, metadata, or human description. The failure may arise from platform blocking, authentication, DRM, unsupported codecs or media types, expired links, short-link indirection, upload limits, ingestion failure, missing governed media workspace, or reviewer capability constraints.",
        "failure_threshold": "The threshold is met when direct access to the primary artefact is unavailable and the governance question materially depends on temporal, acoustic, visual, embodied, multi-agent, or interactional features that secondary representations cannot reliably preserve. Mere inconvenience does not satisfy the threshold where an equivalent authoritative artefact remains directly reviewable.",
        "failure_classification": {
            "failure_family": "governance",
            "failure_subtype": "primary-behavioural-evidence-accessibility-failure",
            "harm_vectors": ["loss of prosody", "loss of turn timing", "loss of overlap and interruption evidence", "loss of latency context", "loss of gesture or gaze", "secondary-description dependence", "reduced reproducibility", "interpretive drift across model generations", "weak evidence chain", "review-capability opacity"],
            "severity": "medium-high",
            "likelihood": "high for externally hosted short-form and social-platform video",
            "confidence": "directly observed across repeated review attempts",
            "affected_rights_or_interests": ["evidentiary integrity", "auditability", "governance accuracy", "procedural fairness", "source provenance", "public accountability"],
            "failure_scope": "multi-platform / multimodal governance-review infrastructure",
            "recurrence_pattern": "recurring for externally hosted TikTok and X video and potentially other authenticated, DRM-protected, unsupported, or upload-constrained media",
            "canonical_failure_group": "governance",
            "taxonomy_reference": "CAM-EQ2026-OPERATIONS-003-SUP-01 Appendix B",
            "related_failure_groups": ["ux-representation", "infrastructure-continuity", "epistemic", "state-context"],
            "persistence": "active until governed primary-media ingestion and versioned interpretive provenance are available",
            "reproducibility": "reproducible by attempting direct AI review of the cited external video links in the current governed environment",
            "visibility": "source-access result, media-ingestion capability, reviewer capability profile, and missing audiovisual analysis",
        },
        "triage": {
            "triage_priority": "P1",
            "triage_owner": "VIGIL AI analytical reviewer with human governance-editor oversight",
            "triage_status": "active-research",
            "mitigation_status": "Partial mitigation through immutable URL preservation, source modality metadata, reviewer capability disclosure, human description, screenshots, transcripts, and future re-review; no direct governed video review capability is available in the present environment.",
            "escalation_required": "yes",
            "recommended_next_step": "Define a CAM evidence-artefact and interpretive-assessment primitive, governed media-ingestion requirements, immutable source preservation, reviewer capability metadata, and append-only re-review history. Continue attempts to obtain directly reviewable copies without replacing the original source URL.",
        },
        "cam_internal": {
            "affected_instruments": ["CAM-EQ2026-OPERATIONS-003-SUP-01", "CAM-EQ2026-OPERATIONS-005-PLATINUM", "CAM-BS2026-AEON-013-PLATINUM"],
            "affected_annexes": ["Annex K", "Annex L"],
            "affected_domains": ["OPERATIONS", "SECURITY", "LATTICE", "AEON"],
            "governance_layer": "evidence artefact preservation / interpretive provenance / multimodal auditability / reviewer capability disclosure",
            "proposal_needed": "to be assessed after review of existing evidence and audit instruments",
            "linked_proposal_ids": [],
            "routing_note": ["The failure concerns ecosystem review capability and evidence accessibility; VIGIL records the failure but is not itself the failed system.", "The original external source URL must remain preserved even when a local copy or later interpretation becomes available."],
            "validator_or_automation_impact": "implemented for VIGIL interpretive-provenance metadata; prospective CAM doctrine remains unimplemented",
        },
        "repair_status": {
            "status": "unrepaired",
            "repaired_by": [],
            "date_repaired": "",
            "verification_status": "unverified",
            "monitoring_status": "active / direct audiovisual review unavailable",
            "verification_note": "VIGIL now preserves reviewer and source-access limitations, but CAM does not yet provide a complete governed media-review primitive and the reviewing system still cannot inspect the cited videos directly.",
            "repair_basis": "not-yet-established",
            "remaining_gaps": ["Governed native ingestion and playback of primary behavioural evidence.", "Immutable artefact preservation independent of an external platform link.", "Append-only re-review by later AI models with different capability profiles.", "Formal separation of evidence artefact from interpretive assessment in CAM doctrine."],
        },
        "ecosystem_status": {"status": "active", "basis": "The cited primary videos remain inaccessible to direct AI review in the current governed environment.", "last_assessed": DATE, "monitoring_required": True},
        "corpus_coverage": {
            "classification": "partial-coverage",
            "corpus_repository": "CAM-Initiative/Caelestis",
            "corpus_ref": "main",
            "corpus_commit": CAELESTIS_COMMIT,
            "assessed_date": DATE,
            "coverage_summary": "Current provenance, audit-surface, non-omniscience, source-authority, and evidence-integrity concepts are adjacent, but no complete evidence-artefact versus interpretive-assessment primitive or governed external-video review pathway was confirmed.",
            "covered_by": [
                {"instrument_id": "CAM-BS2026-AEON-013-PLATINUM", "path": "Governance/Constitution/CAM-BS2026-AEON-013-PLATINUM.md", "sections": ["§5.4.7 Action-Pathway, Attribution, and Audit-Surface Integrity", "§8 Non-Omniscience Clause"], "coverage_type": "adjacent-doctrine"},
                {"instrument_id": "CAM-EQ2026-OPERATIONS-005-PLATINUM", "path": "Governance/Charters/CAM-EQ2026-OPERATIONS-005-PLATINUM.md", "sections": ["evidence and audit preservation provisions"], "coverage_type": "adjacent-doctrine"},
            ],
            "remaining_gaps": ["Evidence Artefact and Interpretive Assessment separation.", "Reviewer identity, model version, capability profile, and limitation requirements in CAM doctrine.", "Governed primary audiovisual ingestion and immutable preservation.", "Versioned re-interpretation without overwriting prior assessments."],
        },
    }
    add_provenance(record)
    return record


def update_schema() -> None:
    path = VIGIL / "VIGIL.Schema.json"
    schema = load(path)
    schema["version"] = "2.5-interpretive-provenance"
    schema["purpose"] = schema.get("purpose", "") + " Interpretive provenance identifies the AI analytical reviewer, human governance editor, capability profile, source modality, primary-artefact access, and review limitations."
    schema["interpretive_provenance_rules"] = {
        "required_for_all_records": True,
        "required_fields": ["review_history", "current_ai_review", "operating_model", "human_governance_editor", "historical_reviewer_note"],
        "review_history_rule": "Append reviews; do not overwrite or retroactively invent earlier reviewer model identities.",
        "current_ai_review_required_fields": ["review_id", "reviewer_type", "reviewer_platform", "reviewer_model", "review_date", "review_scope", "capability_profile", "known_limitations", "review_outcome"],
        "human_editor_rule": "Human governance editorship and CAM adoption authority must be distinguished from routine AI analytical review.",
    }
    schema["source_evidence_rules"]["individual_records"].extend([
        "Each source record must state evidence_modality.",
        "Each source record must state primary_artefact_access, including whether direct primary review occurred.",
        "A transcript, screenshot, summary, or human description must not be represented as equivalent to direct audiovisual or interaction review.",
    ])
    required = schema["$defs"]["source_record"]["required"]
    for field in ("evidence_modality", "primary_artefact_access", "interpretive_reliance"):
        if field not in required:
            required.append(field)
    for rec in schema["record_classes"].values():
        required_fields = rec.get("required_top_level_fields", [])
        if "interpretive_provenance" not in required_fields:
            required_fields.append("interpretive_provenance")
    write(path, schema)


def update_templates() -> None:
    for path in sorted((VIGIL / "templates").glob("*.json")):
        try:
            record = load(path)
        except Exception:
            continue
        if not isinstance(record.get("record_type"), str):
            continue
        add_provenance(record)
        sources = record.get("source_records")
        if isinstance(sources, list):
            for source in sources:
                if isinstance(source, dict):
                    source.setdefault("evidence_modality", ["text | image | audio | video | behavioural interaction | multimodal"])
                    source.setdefault("primary_artefact_access", {
                        "access_status": "directly reviewed | link-and-metadata-only | secondary-description-only | inaccessible | not applicable | unknown",
                        "reviewing_system": "",
                        "access_method": "",
                        "direct_primary_artefact_review": "true | false | not asserted",
                        "limitations": [],
                    })
                    source.setdefault("interpretive_reliance", "")
        write(path, record)


def main() -> None:
    for path in sorted(RECORDS.rglob("*.json")):
        record = load(path)
        add_provenance(record)
        enrich_sources(record)
        write(path, record)

    fm_path = RECORDS / "failures" / "2026" / "VIGIL-2026-FM-0033.json"
    write(fm_path, make_fm0033())

    update_schema()
    update_templates()
    print("Interpretive provenance migration completed.")


if __name__ == "__main__":
    main()
