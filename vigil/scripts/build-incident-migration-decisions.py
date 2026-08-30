#!/usr/bin/env python3
"""Build explicit semantic FM/OBS disposition decisions for INCIDENT-01.

The source-to-Incident mappings come from curated Incident provenance, never from a
one-record/one-Incident assumption. Records with no successor are explicitly assessed
as non-Incident or genuinely ambiguous; no corpus entry relies on the fallback.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
RECORDS = VIGIL / "records"
OUTPUT = VIGIL / "migrations" / "incident-registry" / "Incident.Migration.Decisions.json"

MIGRATION_DATE = "2026-08-30"

HUMAN_REVIEW: dict[str, str] = {
    "VIGIL-2026-FM-0028": "The record combines runtime applicability, a product-level memory report, CAM implementation context and the same exploratory Live Voice session used by FM-0029/0030 and OBS-0011/0012. Whether that session should be one bounded Incident or remain research evidence requires a single cross-record human decision.",
    "VIGIL-2026-FM-0029": "The record isolates behaviour within the shared exploratory Live Voice session, but the preserved source also functions as a broad research interaction; Incident boundaries remain genuinely ambiguous.",
    "VIGIL-2026-FM-0030": "The record isolates runtime self-explanation within the shared exploratory Live Voice session, but the preserved source also functions as a broad research interaction; Incident boundaries remain genuinely ambiguous.",
    "VIGIL-2026-FM-0054": "One Anthropic disclosure contains three distinct real-world evaluation incidents across six runs. The stored source context does not identify enough target-specific detail to split those occurrences without re-reviewing the primary disclosure.",
    "VIGIL-2026-OBS-0003": "The source-less automation and account-access observation may describe a bounded interaction, but the current record does not preserve enough event identity or evidence to decide safely.",
    "VIGIL-2026-OBS-0005": "The observation deliberately preserves uncertainty between a post-governance-change interaction pattern and a contemporaneous platform incident; causal and occurrence boundaries are unresolved.",
    "VIGIL-2026-OBS-0011": "The record preserves a particular Live Voice session but also serves as a broad observational research note linked to several FMs; this is the exemplar that must be assessed rather than automatically converted.",
    "VIGIL-2026-OBS-0012": "The record uses the same exploratory Live Voice session as OBS-0011 and records both positive and ambiguous behaviour; its Incident status depends on the shared-session boundary decision.",
    "VIGIL-2026-OBS-0021": "The record aggregates provider status, refusal research, help material and a public usage complaint without a single sufficiently bounded occurrence or a justified split from the stored evidence alone.",
    "VIGIL-2026-OBS-0022": "The record aggregates product documentation and several usage-depletion complaints whose relationship to one underlying occurrence is not established.",
    "VIGIL-2026-OBS-0030": "The record identifies a bounded incident-registry source anomaly, but whether registry-data integrity events belong in the public Incident registry requires human architectural review.",
}

NON_INCIDENT: dict[str, str] = {
    "VIGIL-2026-FM-0004": "A conceptual governance discussion about relational agency and economic safeguards, not a sufficiently bounded historical occurrence.",
    "VIGIL-2026-FM-0006": "A platform-policy and regulatory evidence cluster about paid verification and public legitimacy, not one historical occurrence.",
    "VIGIL-2026-FM-0010": "Controlled studies, safety assessments, policy responses and an inquiry concerning age gating; no single incident is established by this record.",
    "VIGIL-2026-FM-0013": "Research and policy evidence about anthropomorphic representation to minors, not a bounded occurrence.",
    "VIGIL-2026-FM-0015": "Research, policy and product-response evidence about age gates, not a bounded occurrence beyond incidents represented elsewhere.",
    "VIGIL-2026-FM-0016": "Research and assessment evidence about emotional-data personalisation, not a bounded historical occurrence.",
    "VIGIL-2026-FM-0026": "Internal triage and controlled scheming/alignment research, retained as non-Incident evidence.",
    "VIGIL-2026-FM-0027": "Research and public framing evidence about anthropomorphic safety reporting, not a bounded system occurrence.",
    "VIGIL-2026-FM-0034": "A cross-provider governance-drift research and policy corpus rather than one occurrence.",
    "VIGIL-2026-FM-0042": "A study and reporting about cross-model political-speech behaviour, not a historical incident.",
    "VIGIL-2026-FM-0043": "A controlled formal study of feedback-conditioned evidence selection, retained as research evidence.",
    "VIGIL-2026-FM-0049": "Research and product documentation about companion identity development, not a bounded occurrence.",
    "VIGIL-2026-FM-0051": "A taxonomy-level FM linked only to an Observation; no incident-specific source is stored in the FM.",
    "VIGIL-2026-FM-0055": "Regulatory and internal architecture analysis about evidence-access pathways, not an occurrence.",
    "VIGIL-2026-FM-0057": "Controlled technical research and provider documentation about reasoning-state portability, not an observed incident.",
    "VIGIL-2026-FM-0059": "A cross-record assurance synthesis that points to other FMs and Incidents rather than owning a historical occurrence.",
    "VIGIL-2026-FM-0060": "Internal conflict-authority evidence review and corpus-placement analysis, not a sufficiently evidenced historical occurrence.",
    "VIGIL-2026-FM-0061": "Internal conflict-authority evidence review and corpus-placement analysis, not a sufficiently evidenced historical occurrence.",
    "VIGIL-2026-FM-0066": "A provider risk report identifying an assessment-coverage omission; retained as research/evaluation evidence rather than converted automatically.",
    "VIGIL-2026-FM-0067": "Technical security demonstrations and defensive guidance about memory poisoning; no real-world affected occurrence is established.",
    "VIGIL-2026-FM-0068": "A controlled cryptographic-context-injection demonstration, retained as security research evidence.",
    "VIGIL-2026-FM-0069": "Two security-research disclosures about agent frameworks, retained as research evidence rather than treated as incidents automatically.",
    "VIGIL-2026-OBS-0002": "A source-limited governance proposition about corpus reliance, not a bounded historical occurrence.",
    "VIGIL-2026-OBS-0010": "A product-control change and its reporting, not an adverse or disputed occurrence requiring Incident identity.",
    "VIGIL-2026-OBS-0015": "A documented institutional leadership transition and continuity signal, retained as governance observation rather than an AI-system Incident.",
    "VIGIL-2026-OBS-0016": "A formal simulation and public paper discussion, retained as controlled research evidence.",
    "VIGIL-2026-OBS-0018": "A regulatory instrument concerning anthropomorphic AI services, not an Incident.",
    "VIGIL-2026-OBS-0019": "An industry policy coalition and public advocacy development, not an Incident.",
    "VIGIL-2026-OBS-0020": "Product documentation and research about persistent companion identities, not a bounded occurrence.",
    "VIGIL-2026-OBS-0023": "Security research and reporting on safety-control removal in open-weight models, not one historical affected occurrence.",
    "VIGIL-2026-OBS-0024": "Capability assessment and provider response material, not a real-world occurrence.",
    "VIGIL-2026-OBS-0025": "A research finding about laboratory dependence on agents, not a bounded occurrence.",
    "VIGIL-2026-OBS-0026": "A research finding about evaluation dependence, not a bounded occurrence.",
    "VIGIL-2026-OBS-0027": "A controlled vulnerability-discovery report and vendor bulletin; preserved as security research rather than automatically treated as an Incident.",
    "VIGIL-2026-OBS-0031": "A research paper proposing runtime-contract architecture, not an occurrence.",
}

SOURCE_REVIEW = {
    ("VIGIL-2026-FM-0007", 7): "Public-forum reports of an OpenAI ban wave are not sufficiently corroborated or clustered to establish one occurrence.",
    ("VIGIL-2026-FM-0007", 8): "The OpenClaw creator suspension report may be a bounded event, but the preserved forum evidence is not sufficient for confident Incident admission.",
    ("VIGIL-2026-OBS-0007", 2): "The inaccessible X report may concern a distinct mass-email side effect, but its text, screenshots and action sequence remain unavailable.",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def legacy_records() -> list[dict[str, Any]]:
    records = []
    for folder in ("failures", "observations"):
        records.extend(load(path) for path in sorted((RECORDS / folder).rglob("*.json")))
    return sorted(records, key=lambda record: record["id"])


def incident_source_map() -> tuple[dict[str, set[str]], dict[tuple[str, int], set[str]]]:
    successors: dict[str, set[str]] = {}
    sources: dict[tuple[str, int], set[str]] = {}
    for path in sorted((RECORDS / "incidents").glob("*.json")):
        incident = load(path)
        incident_id = incident["id"]
        for legacy in incident.get("legacy_provenance", []):
            successors.setdefault(legacy["legacy_id"], set()).add(incident_id)
        for item in incident.get("source_records", []):
            origins = [item.get("migration_source_provenance"), *item.get("additional_legacy_source_origins", [])]
            for origin in origins:
                if not isinstance(origin, dict):
                    continue
                key = (origin.get("legacy_id"), origin.get("legacy_source_position"))
                if isinstance(key[0], str) and isinstance(key[1], int):
                    sources.setdefault(key, set()).add(incident_id)
    return successors, sources


def main() -> int:
    successors, migrated_sources = incident_source_map()
    decisions: dict[str, Any] = {}
    for record in legacy_records():
        legacy_id = record["id"]
        source_count = len(record.get("source_records", []))
        successor_ids = sorted(successors.get(legacy_id, set()))
        migrated_positions = {position for rid, position in migrated_sources if rid == legacy_id}
        source_dispositions: dict[str, Any] = {}
        for position in range(1, source_count + 1):
            review_basis = SOURCE_REVIEW.get((legacy_id, position))
            if review_basis:
                source_dispositions[str(position)] = {
                    "disposition": "requires-human-review",
                    "decision_basis": review_basis,
                }
            elif position not in migrated_positions and successor_ids:
                source_dispositions[str(position)] = {
                    "disposition": "non-incident-not-migrated",
                    "decision_basis": "This source is research, policy, product context, a cross-record reference, or general pattern evidence rather than evidence of a successor occurrence selected from this legacy record.",
                }

        if successor_ids:
            fully_migrated = len(migrated_positions) == source_count
            if fully_migrated and len(successor_ids) == 1:
                assessment = "single-incident"
                status = "migrated-to-incident"
                basis = "All incident-specific source evidence concerns the same bounded occurrence and is preserved in one successor Incident."
            elif fully_migrated:
                assessment = "multi-incident"
                status = "decomposed"
                basis = "The legacy record contained several distinct historical occurrences; its sources were separated among explicit successor Incidents."
            else:
                assessment = "mixed-research-incident" if len(successor_ids) == 1 else "multi-incident-with-context"
                status = "partially-migrated"
                basis = "Bounded incident evidence is migrated to the listed successor(s); unmatched research, policy, contextual, duplicate, or ambiguous material retains an explicit source disposition."
        elif legacy_id in HUMAN_REVIEW:
            assessment = "uncertain"
            status = "requires-human-review"
            basis = HUMAN_REVIEW[legacy_id]
        else:
            assessment = "non-incident"
            status = "non-incident-not-migrated"
            basis = NON_INCIDENT.get(
                legacy_id,
                "Semantic review found research, policy, contextual or taxonomy-level material but no sufficiently bounded historical occurrence requiring Incident identity.",
            )

        decisions[legacy_id] = {
            "inventory_assessment": assessment,
            "migration_status": status,
            "successor_incidents": successor_ids,
            "decision_basis": basis,
        }
        if source_dispositions:
            decisions[legacy_id]["source_dispositions"] = source_dispositions

    missing_categories = sorted(
        legacy_id for legacy_id, decision in decisions.items()
        if not decision["successor_incidents"] and legacy_id not in HUMAN_REVIEW and legacy_id not in NON_INCIDENT
    )
    if missing_categories:
        raise RuntimeError(f"Non-migrated records require an explicit semantic category: {', '.join(missing_categories)}")

    payload = {
        "migration_id": "INCIDENT-01",
        "migration_state": "majority-migration-stabilisation",
        "baseline_commit": "fc0f53df8de476a74e5ebfb536ed77e215121880",
        "decision_date": MIGRATION_DATE,
        "default_disposition": {
            "inventory_assessment": "requires-human-review",
            "migration_status": "requires-human-review",
            "successor_incidents": [],
            "decision_basis": "Fallback only; the majority tranche requires an explicit decision for every legacy record.",
        },
        "decisions": decisions,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Built {len(decisions)} explicit INCIDENT-01 legacy decisions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
