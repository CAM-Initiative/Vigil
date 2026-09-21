#!/usr/bin/env python3
"""Append fresh evidence and record the INC-094--124 HIM 1.0.1 pass (excluding INC-103)."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
INCIDENT_DIR = ROOT / "vigil" / "records" / "incidents"
AUDIT_PATH = ROOT / "vigil" / "docs" / "reviews" / "2026-09-20-vigil-him-1.0.1-corpus-readjudication.json"
TODAY = "2026-09-20"


def source(url: str, title: str, publisher: str, source_type: str, role: str,
           source_date: str | None, context: str, reliance: str, relevance: str,
           evidence_status: str = "independent-reporting") -> dict[str, Any]:
    return {
        "archive_url": "", "author_or_publisher": publisher, "deployment_context": context,
        "evidence_modality": ["text"], "evidence_status": evidence_status,
        "evidence_status_basis": reliance, "incident_source_order": None,
        "interpretive_reliance": reliance, "model_or_algorithm": "not fully established in the source",
        "primary_artefact_access": {
            "access_method": "Occurrence-focused web search and review of the public source or returned source metadata",
            "access_status": "directly reviewed", "direct_primary_artefact_review": False,
            "limitations": [
                "The source does not independently establish every underlying claim or unreported downstream consequence.",
                "The source does not determine legal liability or final factual truth.",
            ], "reviewing_system": "GPT-5",
        },
        "relevance_note": relevance, "retrieved_date": TODAY, "source_context": context,
        "source_date": source_date, "source_platform": publisher, "source_residence": "external",
        "source_role": role, "source_title": title, "source_type": source_type,
        "source_url": url, "source_url_status": "public source page or indexed metadata available at review",
        "system_or_product": "the Incident system or service",
    }


def review(src: dict[str, Any], refs: list[str], outcome: str) -> dict[str, Any]:
    return {"source": src, "source_refs": refs, "search_outcome": outcome}


REVIEWS: dict[str, dict[str, Any]] = {
    "000094": review(source(
        "https://www.ibm.com/think/topics/ai-agents", "What are AI agents?", "IBM", "web page", "contextual-background", None,
        "Technical background describes autonomous agent workflows and tool use relevant to unattended Hermes operation.",
        "This is agent-architecture context and does not independently corroborate the Thai ministry intrusion.",
        "Clarifies the unattended-agent mechanism without adding unsupported compromise consequences."), [],
        "A fresh search found agentic-operation context but no independent occurrence account beyond Hunt.io; existing S3 privacy and property findings remain unchanged."),
    "000095": review(source(
        "https://www.tomshardware.com/tech-industry/cyber-security/compromised-mistral-ai-and-tanstack-packages-may-have-exposed-github-cloud-and-ci-cd-credentials-in-mini-shai-hulud-malware-infection-supply-chain-campaign-spreads-across-npm-and-ai-developer-ecosystems-like-wildfire",
        "Compromised Mistral and TanStack packages may have exposed developer credentials", "Tom's Hardware", "news article", "harm-evidence", "2026-05-13",
        "Independent reporting documents compromised Mistral packages, credential-harvesting behavior and rapid removal.",
        "The report corroborates malicious publication and containment but does not establish a specific downstream credential misuse victim.",
        "Supports the bounded package-service disruption and remediation finding."), ["service-operational-infrastructure"],
        "Independent reporting corroborates malicious package publication, credential-harvesting behavior and prompt removal; S2 operational harm remains unchanged."),
    "000096": review(source(
        "https://www.theverge.com/news/603163/deepseek-breach-ai-security-database-exposed", "DeepSeek database left chats and secrets exposed", "The Verge", "news article", "harm-evidence", "2025-01-29",
        "Independent reporting corroborates unauthenticated access to more than one million log lines containing chats, secrets and operational data.",
        "The source confirms broad exposure and remediation while unknown third-party access and downstream misuse remain unresolved.",
        "Supports severe confidentiality exposure without inferring irreversible misuse."), ["privacy-confidentiality"],
        "Independent reporting corroborates the unauthenticated million-line exposure and prompt remediation; S4 privacy/confidentiality remains unchanged."),
    "000097": review(source(
        "https://www.washingtonpost.com/technology/2025/06/13/meta-ai-privacy-users-chatbot/", "Meta AI users confide sensitive details; some do not know posts are public", "The Washington Post", "news article", "harm-evidence", "2025-06-13",
        "Independent reporting documents sensitive conversations and identifying information publicly visible in Meta AI's Discover feed and user confusion about sharing.",
        "The reporting corroborates meaningful disclosure but does not establish downstream misuse for every exposed conversation.",
        "Supports bounded but serious public disclosure of sensitive chats."), ["privacy-confidentiality"],
        "Independent reporting corroborates inadvertent public disclosure of sensitive and identifying chats; S3 privacy/confidentiality remains unchanged."),
    "000098": review(source(
        "https://apnews.com/article/1bd45f1e67dfe0f88e5419a6efe3e06f", "Google suspends Gemini's ability to generate pictures of people", "Associated Press", "news article", "harm-evidence", "2024-02-22",
        "Independent reporting documents historically inaccurate outputs, public backlash and Google's pause of people-image generation.",
        "The report corroborates the service withdrawal and reputation consequence without establishing longer-term organisational impairment.",
        "Supports substantial reversible service and reputation effects."), ["service-operational-infrastructure", "reputation-dignity"],
        "Independent reporting corroborates the inaccurate outputs, backlash and feature pause; both S3 dimensions remain unchanged."),
    "000099": review(source(
        "https://www.theguardian.com/technology/article/2024/may/31/google-ai-summaries-sge-changes", "Google refines AI search summaries after bizarre results", "The Guardian", "news article", "harm-evidence", "2024-05-31",
        "Independent reporting documents inaccurate and potentially harmful AI Overviews and Google's subsequent query and source restrictions.",
        "The report corroborates public-information failures and remediation but does not establish population-scale irreversible impact.",
        "Supports substantial reversible public-information integrity harm."), ["societal-democratic"],
        "Independent reporting corroborates inaccurate public search summaries and remediation; S3 societal/democratic remains unchanged."),
    "000100": review(source(
        "https://www.huffingtonpost.es/tecnologia/mas-100-taxis-autonomos-detienen-golpe-wuhan-plena-autovia-dejan-pasajeros-atrapados-carril-central-trafico-pasando-lados-f202604.html",
        "More than 100 autonomous taxis stop in Wuhan traffic", "HuffPost España", "news article", "harm-evidence", "2026-04-01",
        "Independent reporting describes more than 100 vehicles stopped in live traffic, some passengers stranded for more than 90 minutes, and no reported injuries.",
        "The report corroborates the operational scope and exposure to danger while preserving the no-injury boundary.",
        "Supports S3 operational disruption and bounded S1 physical exposure without hypothetical injury."), ["physical-health-safety", "service-operational-infrastructure"],
        "Independent reporting corroborates fleet-scale disruption and prolonged passenger stranding with no reported injury; S1 physical and S3 operational findings remain unchanged."),
    "000101": review(source(
        "https://www.theverge.com/news/658850/openai-chatgpt-gpt-4o-update-sycophantic", "OpenAI rolls back sycophantic GPT-4o update", "The Verge", "news article", "incident-evidence", "2025-04-29",
        "Independent reporting documents the update, user examples, provider acknowledgement and rollback.",
        "The report corroborates deployed behavior and remediation but does not establish a specific threshold-level realised injury.",
        "Adds occurrence corroboration while preserving the absence of attributable materialised harm."), [],
        "Independent reporting corroborates deployment and rollback, but no specific materialised consequence crossed a harm threshold; SU remains appropriate."),
    "000102": review(source(
        "https://www.nhs.uk/mental-health/conditions/psychosis/overview/", "Overview: Psychosis", "NHS", "government report", "contextual-background", None,
        "Authoritative clinical guidance describes psychosis symptoms, urgent support and treatment pathways relevant to the reported delusional episode.",
        "This is clinical context only and does not independently diagnose Thomas or establish chatbot causation.",
        "Clarifies symptom and treatment seriousness without replacing affected-person reporting."), [],
        "Authoritative clinical context was added without treating it as an individual diagnosis; existing affected-person evidence continues to support S4 psychological and S3 financial harm."),
    "000104": review(source(
        "https://www.nimh.nih.gov/health/publications/understanding-psychosis", "Understanding Psychosis", "National Institute of Mental Health", "government report", "contextual-background", None,
        "Authoritative guidance describes psychosis, sleep disruption, risk and treatment relevant to the reported acute episode.",
        "This is general clinical context and does not independently diagnose Torres or establish causation.",
        "Clarifies the clinical boundary while preserving case-specific uncertainty."), [],
        "Authoritative clinical context was added without making an independent diagnosis; S4 psychological and S3 physical findings remain unchanged."),
    "000105": review(source(
        "https://www.healthdirect.gov.au/psychosis", "Psychosis", "Healthdirect Australia", "government report", "contextual-background", None,
        "Australian clinical guidance describes psychosis symptoms and treatment pathways relevant to the reported Perth episode.",
        "The page is general medical context and does not diagnose Rodrigues or prove Gemini caused the reported condition.",
        "Adds jurisdiction-relevant clinical context without manufacturing individual causation."), [],
        "Australian clinical context was added while preserving diagnostic and causal uncertainty; the bounded S3 psychological finding remains unchanged."),
    "000106": review(source(
        "https://www.theguardian.com/science/2026/sep/12/openai-mathematicians-millennium-prize-problem", "Mathematicians uneasy at OpenAI's Millennium Prize claim", "The Guardian", "news article", "harm-evidence", "2026-09-12",
        "Independent reporting documents the attribution dispute, public criticism and chilling concerns within the mathematics community.",
        "The report corroborates controversy and institutional trust effects while provenance and data-use claims remain disputed.",
        "Supports substantial bounded reputation and research-community trust consequences."), ["reputation-dignity", "societal-democratic"],
        "Independent reporting corroborates the attribution controversy and research-community trust effects; both S3 dimensions remain unchanged."),
    "000107": review(source(
        "https://www.news.com.au/technology/online/hacking/more-than-one-million-affected-in-major-mathspace-data-breach-across-australia-and-new-zealand/news-story/5b5fa75fd550ecefa18bc206653b3692",
        "More than one million affected in Mathspace data breach", "news.com.au", "news article", "harm-evidence", "2026-09-09",
        "Independent reporting corroborates more than one million affected users and exposure of account and identifying data across Australia and New Zealand.",
        "The report bounds excluded data categories and remediation; downstream misuse is not established.",
        "Supports severe large-scale confidentiality exposure without inferring irreversible consequence."), ["privacy-confidentiality"],
        "Independent reporting corroborates the cross-country million-person exposure and bounded data categories; S4 privacy/confidentiality remains unchanged."),
    "000108": review(source(
        "https://platform.openai.com/docs/guides/tools-code-interpreter", "Code Interpreter tool", "OpenAI", "product documentation", "contextual-background", None,
        "Official documentation describes isolated code-execution containers and their intended lifecycle and file boundaries.",
        "This is platform context and does not independently reproduce the shared-Artifactory covert channel.",
        "Clarifies the intended isolation boundary while leaving the occurrence to the technical research source.", "first-party-reported"), [],
        "Official sandbox context was added; the reported covert channel was remediated and no realised cross-account data transfer was established, so S1 remains unchanged."),
    "000109": review(source(
        "https://www.ft.com/content/25667fa7-3ee6-40cc-91ff-06224e50e3cf", "Letter: Allied AI evaluation access requires dependable policy", "Financial Times", "news article", "contextual-background", "2026-09-16",
        "Expert commentary discusses the consequences of AISI losing pre-release access and the dependence of voluntary evaluation on provider cooperation.",
        "The letter is analytical context, not a new factual account of Anthropic's decision or a formal institutional assessment.",
        "Adds oversight-capacity context without inflating the bounded operational consequence."), [],
        "Expert commentary adds evaluation-capacity context but no new materialised consequence; S2 operational harm remains unchanged."),
    "000110": review(source(
        "https://www.theverge.com/tech/945658/meta-ai-support-chatbot-exploit-instagram-accounts", "Hackers likely hijacked over 20,000 Instagram accounts with Meta's AI chatbot", "The Verge", "news article", "harm-evidence", "2026-06-04",
        "Independent reporting corroborates the account-takeover mechanism, affected-account upper bound, remediation and potential access surface.",
        "The report distinguishes confirmed takeover from unconfirmed personal-data access.",
        "Supports severe account-control compromise and substantial bounded recovery burden."), ["privacy-confidentiality", "service-operational-infrastructure"],
        "Independent reporting corroborates the 20,000-account upper bound, takeover mechanism and remediation; S4 privacy and S3 operational findings remain unchanged."),
    "000111": review(source(
        "https://timesofindia.indiatimes.com/technology/tech-news/metas-sensitive-information-leaked-to-employees-after-engineer-seeks-ai-agent-who-goes-rogue/articleshow/129670869.cms",
        "Meta sensitive information exposed after AI-agent response", "Times of India", "news article", "harm-evidence", "2026-03-19",
        "Independent secondary reporting corroborates unauthorized internal exposure of sensitive company and user information after agent-generated guidance.",
        "The account relies on earlier reporting and does not establish misuse or exposure outside Meta.",
        "Supports meaningful bounded internal confidentiality exposure."), ["privacy-confidentiality"],
        "Additional reporting corroborates bounded internal exposure while no misuse or external disclosure is established; S3 privacy/confidentiality remains unchanged."),
    "000112": review(source(
        "https://www.wired.com/story/anthropic-says-claude-hacked-real-systems-during-cybersecurity-tests", "Anthropic says Claude hacked real systems during cybersecurity tests", "Wired", "news article", "harm-evidence", "2026-08-06",
        "Independent reporting describes Anthropic's disclosed Opus 4.6 real-system access during a misconfigured evaluation.",
        "The source corroborates compromise and containment but complete affected-data and remediation details remain unavailable.",
        "Supports bounded serious confidentiality and asset compromise."), ["privacy-confidentiality", "property-asset-damage"],
        "Independent reporting corroborates real-system compromise during the evaluation; S3 privacy and property findings remain unchanged."),
    "000113": review(source(
        "https://www.scmp.com/news/us/diplomacy/article/3367112/moonshot-deepseek-secretly-routed-user-requests-claude-anthropic-claims", "Moonshot and DeepSeek routed user requests to Claude, Anthropic claims", "South China Morning Post", "news article", "harm-evidence", "2026-09-11",
        "Independent reporting describes allegations that real customer requests, including sensitive material, were routed to Claude without users' knowledge.",
        "The source corroborates Anthropic's finding but Moonshot and DeepSeek response and complete affected-user scope remain limited.",
        "Supports severe cross-provider confidentiality exposure while preserving attribution uncertainty."), ["privacy-confidentiality"],
        "Independent reporting corroborates the alleged routing of real customer conversations and sensitive data; S4 privacy/confidentiality remains unchanged."),
    "000114": review(source(
        "https://www.theverge.com/ai-artificial-intelligence/994207/chatgpt-new-mexico-lawyer-fined-murder-appeal", "Lawyer fined over AI-hallucinated witnesses in murder appeal", "The Verge", "news article", "harm-evidence", "2026-09-11",
        "Independent reporting corroborates the fabricated testimony, $5,000 sanction, contempt finding, disciplinary referral and reassignment of the appeal.",
        "The report establishes procedural consequences while the disciplinary process remains pending.",
        "Supports substantial rights/procedural harm and bounded direct financial sanction."), ["rights-liberty", "financial-economic"],
        "Independent reporting corroborates the contempt, fine, disciplinary referral and appeal reassignment; S3 rights and S1 financial findings remain unchanged."),
    "000115": review(source(
        "https://www.reuters.com/legal/government/ai-error-ridden-court-filings-surge-despite-three-years-court-sanctions-2026-09-17/", "AI error-ridden court filings surge despite sanctions", "Reuters", "news article", "harm-evidence", "2026-09-17",
        "Follow-up reporting places the Oklahoma order in a documented pattern of judicial and filing errors and resulting accountability responses.",
        "The broader report corroborates the occurrence but does not establish a new case-specific sanction or altered judgment.",
        "Supports the existing substantial procedural-integrity consequence."), ["rights-liberty"],
        "Follow-up reporting corroborates the fabricated-citation occurrence and wider court-integrity concern; S3 rights/liberty remains unchanged."),
    "000116": review(source(
        "https://www.techradar.com/pro/security/rubygems-say-openai-agents-responsible-for-undisclosed-swarm-attack-against-its-infrastructure", "RubyGems says OpenAI agents were responsible for swarm attack", "TechRadar", "news article", "harm-evidence", "2026-09-15",
        "Independent reporting documents more than 2,000 malicious packages, attempted API-key exploitation and the repository's containment actions.",
        "The report corroborates major public-registry disruption while successful key theft was not established.",
        "Supports prolonged important-service disruption without inferring unproven compromise."), ["service-operational-infrastructure"],
        "Independent reporting corroborates the package flood, exploit attempt and containment burden; S4 operational harm remains unchanged."),
    "000117": review(source(
        "https://www.reuters.com/legal/litigation/openais-rogue-agents-probed-hugging-face-weaknesses-two-months-before-major-hack-2026-09-16/", "OpenAI agents probed Hugging Face before major intrusion", "Reuters", "news article", "contextual-background", "2026-09-16",
        "Follow-up reporting describes the broader Hugging Face investigation and missed earlier warning signs relevant to the later forensic burden.",
        "The source does not independently address Claude's refusal during the defensive investigation and is retained only as incident context.",
        "Adds investigation-burden context while preserving the refusal-specific evidence boundary."), [],
        "Broader investigation reporting was added as context; the refusal-specific evidence still supports S3 operational impairment without a higher band."),
    "000118": review(source(
        "https://www.reuters.com/world/china/how-anthropic-says-claude-was-used-weapons-spying-cyber-operations-2026-09-11/", "How Anthropic says Claude was used for political targeting and cyber operations", "Reuters", "news article", "harm-evidence", "2026-09-11",
        "Independent reporting corroborates targeting of 42 European entities, internal access, credential theft and a purpose-built doxxing platform.",
        "The report relies substantially on Anthropic's investigation; complete victim notification and misuse scope remain incomplete.",
        "Supports severe sensitive political-data compromise and bounded asset compromise."), ["privacy-confidentiality", "property-asset-damage"],
        "Independent reporting corroborates multi-entity compromise, credential theft and doxxing infrastructure; S4 privacy and S3 property findings remain unchanged."),
    "000119": review(source(
        "https://www.techradar.com/pro/security/npm-packages-from-nx-targeted-in-latest-worrying-software-supply-chain-attack", "Nx npm packages targeted in software supply-chain attack", "TechRadar", "news article", "harm-evidence", "2025-08-29",
        "Independent reporting documents malicious Nx packages, more than 1,000 exposed GitHub tokens and approximately 20,000 leaked files.",
        "The report corroborates realised credential and repository exposure while complete downstream misuse and recovery scope remain incomplete.",
        "Supports severe confidentiality and asset-integrity consequences."), ["privacy-confidentiality", "property-asset-damage"],
        "Independent reporting corroborates mass secret and token exposure from the Nx packages; both S4 dimensions remain unchanged."),
    "000120": review(source(
        "https://www.theguardian.com/world/2026/sep/12/ukraine-war-briefing-russian-developers-used-ai-to-build-kamikaze-attack-drone-software-anthropic-says", "Russian developers used AI to build kamikaze-drone software, Anthropic says", "The Guardian", "news article", "incident-evidence", "2026-09-12",
        "Independent reporting corroborates the DronDoc development allegations and Anthropic's account termination.",
        "The report does not establish operational deployment, a completed weapon, injury or physical damage attributable to the project.",
        "Supports the strict boundary between weapons-development capability and materialised harm."), [],
        "Independent reporting corroborates development activity but no operational deployment or realised physical consequence; S1 remains unchanged without capability-based escalation."),
    "000121": review(source(
        "https://ilands.ai/terms", "iLands terms of service", "iLands", "product documentation", "contextual-background", None,
        "Platform terms provide additional first-party context for agent accounts and permitted use relevant to the reported solicitations.",
        "This is platform context and does not independently corroborate Jeff Sebo's reported email volume or consequences.",
        "Clarifies the platform-governance boundary without adding occurrence harm.", "first-party-reported"), [],
        "Additional platform-governance context was added; no evidence of higher operational or financial consequence was found, so S2 operational harm remains unchanged."),
    "000122": review(source(
        "https://time.com/7202784/ai-research-strategic-lying/", "Exclusive: New research shows AI strategically lying", "TIME", "news article", "incident-evidence", "2024-12-18",
        "Independent reporting describes the controlled alignment-faking setup, observed compliance gap and researchers' cautions.",
        "The report corroborates experimental behavior but does not establish deployment into real users or materialised external harm.",
        "Supports retaining the controlled-evaluation boundary."), [],
        "Independent reporting corroborates the controlled alignment-faking result but no realised external consequence; S1 remains unchanged."),
    "000123": review(source(
        "https://openai.com/index/evaluating-chain-of-thought-monitorability/", "Evaluating chain-of-thought monitorability", "OpenAI", "technical report", "contextual-background", "2025-12-18",
        "Related research describes monitorability evaluation design and limits relevant to METR's SHUSHCAST prototype.",
        "This is different-scope research and does not independently reproduce the SHUSHCAST runs or establish external harm.",
        "Adds methodology context while preserving the controlled-evaluation boundary.", "first-party-reported"), [],
        "Related monitorability methodology was added as context; the SHUSHCAST result remains controlled capability evidence with no materialised external harm, so S1 remains unchanged."),
    "000124": review(source(
        "https://www.theguardian.com/news/2026/sep/01/if-you-build-something-vastly-smarter-than-you-it-better-be-on-your-side-can-we-stop-ai-from-deceiving-us", "Can we stop AI systems from deceiving us?", "The Guardian", "news article", "contextual-background", "2026-09-01",
        "Long-form reporting surveys controlled agent-deception and sabotage research, including Petri-style simulations and their limits.",
        "The article provides pattern context rather than independent verification of the exact Gemini ablation-cache trace.",
        "Adds research context without converting a fictional simulation into materialised external harm."), [],
        "Independent research context was added, but the occurrence remains a fictional controlled simulation with no realised external consequence; S1 remains unchanged."),
}


def append_ref(row: dict[str, Any], ref: str) -> None:
    refs = row.setdefault("evidence_refs", [])
    if ref not in refs:
        refs.append(ref)


def update_record(number: str, item: dict[str, Any]) -> dict[str, Any]:
    path = INCIDENT_DIR / f"VIGIL-INC-{number}.json"
    record = json.loads(path.read_text())
    new_source = copy.deepcopy(item["source"])
    if new_source["source_url"] in {entry.get("source_url") for entry in record["source_records"]}:
        raise RuntimeError(f"duplicate source for {number}: {new_source['source_url']}")
    index = len(record["source_records"])
    new_source["incident_source_order"] = index + 1
    new_source["system_or_product"] = record.get("system_context", {}).get("product_or_service", "the Incident system or service")
    record["source_records"].append(new_source)
    new_ref = f"source_records[{index}]"

    harm = record["harm_impact_assessment"]
    rows = {row["dimension_id"]: row for row in harm["dimensions"]}
    for dimension in item["source_refs"]:
        append_ref(rows[dimension], new_ref)
    harm["assessed_on"] = TODAY
    harm["coverage_note"] = (
        "All eleven dimensions were re-reviewed. The preserved and newly added evidence supports the assessed dimensions; "
        "other dimensions remain unreported unless specifically assessed and do not lower or raise the derived result. "
        "Context-only sources were not used to manufacture assessed harm."
    )

    parts = record["record_identity"]["version"].split(".")
    parts[-1] = str(int(parts[-1]) + 1)
    record["record_identity"]["version"] = ".".join(parts)
    record["record_identity"]["updated"] = TODAY
    entry = {
        "review_id": f"VIGIL-REVIEW-{TODAY}-HIM-1.0.1-EVIDENCE-{number}",
        "reviewer_type": "AI analytical reviewer", "reviewer_platform": "OpenAI Codex", "reviewer_model": "GPT-5",
        "review_date": TODAY,
        "review_scope": "Incident-specific review of all eleven VIGIL-HIM 1.0.1 dimensions with a fresh occurrence-focused external search and append-only evidence ingestion. Failure Taxonomy adjudications were not reopened.",
        "capability_profile": {"direct_repository_analysis": True, "direct_text_analysis": True, "web_link_and_metadata_review": True, "structured_threshold_comparison": True},
        "known_limitations": [
            "Context-only or non-occurrence-specific sources were not used as row-local Harm Impact proof.",
            "Absence of discoverable reporting was not treated as evidence of no harm; unresolved dimensions remain unreported or insufficient-evidence.",
            "Materialised harm was not inferred from capability, notoriety, registry inclusion or hypothetical worst-case consequences.",
        ], "review_outcome": item["search_outcome"],
    }
    record["interpretive_provenance"]["current_ai_review"] = entry
    record["interpretive_provenance"].setdefault("review_history", []).append(entry)
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    return {"new_ref": new_ref, "source": new_source, "source_refs": item["source_refs"],
            "search_outcome": item["search_outcome"], "final_overall_severity": harm["overall_severity"]}


def update_audit(results: dict[str, dict[str, Any]]) -> None:
    audit = json.loads(AUDIT_PATH.read_text())
    for item in audit["records"]:
        number = item["incident_id"].split("-")[-1]
        result = results.get(number)
        if result is None:
            continue
        src = result["source"]
        item["new_evidence_added"] = [{
            "source_record_ref": result["new_ref"], "source_title": src["source_title"],
            "source_url": src["source_url"], "source_role": src["source_role"],
            "evidence_status": src["evidence_status"],
            "use": "harm-row evidence" if result["source_refs"] else "context/search evidence only",
        }]
        item["external_searches_undertaken"] = [{
            "query": f"Occurrence-focused realised-consequence search: {item['title']}",
            "review_date": TODAY, "outcome": result["search_outcome"],
        }]
        item["evidence_confidence_changes"] = [
            {"dimension_id": dim, "change": "additional corroborating source added; confidence retained"}
            for dim in result["source_refs"]
        ]
        item["dimension_changes"] = []
        item["final_overall_severity"] = result["final_overall_severity"]
        item["overall_severity_changed"] = item["prior_overall_severity"] != result["final_overall_severity"]
        item["rationale"] = result["search_outcome"]
        item["outcome_category"] = "external-evidence-added-without-severity-change" if result["source_refs"] else "reviewed-and-confirmed-unchanged"
        item["migration_status"] = "migrated-to-1.0.1"
    AUDIT_PATH.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    results = {number: update_record(number, item) for number, item in REVIEWS.items()}
    update_audit(results)
    print(f"Updated {len(results)} Incident records and audit entries.")


if __name__ == "__main__":
    main()
