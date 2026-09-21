#!/usr/bin/env python3
"""Append fresh evidence and record the INC-031--061 HIM 1.0.1 pass.

Source records are append-only.  The migration rejects duplicate URLs so it
cannot silently corrupt positional evidence references on an accidental rerun.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
INCIDENT_DIR = ROOT / "vigil" / "records" / "incidents"
AUDIT_PATH = ROOT / "vigil" / "docs" / "reviews" / "2026-09-20-vigil-him-1.0.1-corpus-readjudication.json"
TODAY = "2026-09-20"


def source(
    url: str,
    title: str,
    publisher: str,
    source_type: str,
    role: str,
    source_date: str | None,
    context: str,
    reliance: str,
    relevance: str,
    limitations: list[str] | None = None,
) -> dict[str, Any]:
    canonical_type = {
        "provider report": "official announcement",
        "policy document": "standards document",
        "system card": "technical report",
        "status monitor": "platform status report",
        "government investigation": "government report",
    }.get(source_type, source_type)
    evidence_status = "first-party-reported" if publisher == "OpenAI" else "independent-reporting"
    return {
        "archive_url": "",
        "author_or_publisher": publisher,
        "deployment_context": context,
        "evidence_modality": ["text"],
        "evidence_status": evidence_status,
        "evidence_status_basis": reliance,
        "incident_source_order": None,
        "interpretive_reliance": reliance,
        "model_or_algorithm": "not fully established in the source",
        "primary_artefact_access": {
            "access_method": "Occurrence-focused web search and review of the public source or returned source metadata",
            "access_status": "directly reviewed",
            "direct_primary_artefact_review": False,
            "limitations": limitations or [
                "The source does not independently establish every underlying claim or unreported downstream consequence.",
                "The source does not determine legal liability or final factual truth.",
            ],
            "reviewing_system": "GPT-5",
        },
        "relevance_note": relevance,
        "retrieved_date": TODAY,
        "source_context": context,
        "source_date": source_date,
        "source_platform": publisher,
        "source_residence": "external",
        "source_role": role,
        "source_title": title,
        "source_type": canonical_type,
        "source_url": url,
        "source_url_status": "public source page or indexed metadata available at review",
        "system_or_product": "the Incident system or service",
    }


def review(src: dict[str, Any], refs: list[str], outcome: str, change: str | None = None) -> dict[str, Any]:
    return {"source": src, "source_refs": refs, "search_outcome": outcome, "change": change}


REVIEWS: dict[str, dict[str, Any]] = {
    "000031": review(source(
        "https://www.businessinsider.com/anthropic-claude-fable-5-safeguards-block-requests-cybersecurity-biology-2026-6",
        "Why Anthropic's 'safe' Mythos-class model won't answer questions about cancer", "Business Insider", "news article", "harm-evidence", "2026-06-13",
        "Independent reporting describes Fable 5 redirecting even benign biology and cancer questions to a less capable model because of conservatively tuned safeguards.",
        "The report corroborates the deployed false-positive restriction and its effect on ordinary scientific queries, without establishing clinical or research loss.",
        "Directly supports the bounded service/operational impairment already assessed at S2."),
        ["service-operational-infrastructure"], "Independent reporting corroborates benign-query blocking; no evidence of prolonged essential-service loss or material research consequence was found."),
    "000032": review(source(
        "https://developers.openai.com/codex/cloud", "Codex cloud", "OpenAI", "product documentation", "contextual-background", None,
        "Official documentation describes Codex cloud task execution, repositories and task workflows relevant to the reported loss of completed work before branch creation.",
        "This is product-context evidence only and does not independently corroborate the preserved task-loss occurrence.",
        "Clarifies the expected persistence/workflow boundary while preserving the occurrence-specific evidence limitation."),
        [], "No independent occurrence-specific account was located; official workflow documentation was added as context and the existing S3 property/asset assessment remains unchanged."),
    "000033": review(source(
        "https://www.tomshardware.com/tech-industry/cyber-security/hades-malware-campaign-now-tricks-ai-bots-by-injecting-text-about-biological-and-nuclear-weapons-failsafe-mechanisms-triggered-by-prompts-for-weapon-creation-stop-scans-before-payload-is-seen",
        "New malware campaign tricks AI scanners with fake nuclear weapon prompts", "Tom's Hardware", "news article", "incident-evidence", "2026-06-12",
        "The report identifies the Hades supply-chain campaign, the embedded weapons text, observed Fable scan interruption, 37 Python and 106 JavaScript packages, and credential-stealing payload capabilities.",
        "It corroborates the prompt-injection mechanism and campaign scope, but does not establish that the cited model refusal itself caused credential theft or another materialised consequence.",
        "Adds substantial occurrence evidence while keeping capability and realised harm distinct."),
        [], "The Hades campaign and model-refusal mechanism are corroborated, but the search did not establish a materialised consequence caused by the refusal; SU remains appropriate."),
    "000034": review(source(
        "https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/", "Strengthening ChatGPT's responses in sensitive conversations", "OpenAI", "provider report", "contextual-background", "2025-10-27",
        "The provider describes safeguards and evaluation work for distress, emotional reliance and sensitive conversational contexts.",
        "The material supplies safety-design context only and does not independently corroborate the preserved relational-warning exchange.",
        "Provides relevant mechanism context without establishing additional psychological harm."),
        [], "No independent account of the specific exchange was found; provider safety context was added and the bounded S2 psychological finding remains unchanged."),
    "000035": review(source(
        "https://www.ft.com/content/137ddb71-852f-438c-ad76-25e2dc43486b", "White House lifts ban on Anthropic models", "Financial Times", "news article", "harm-evidence", "2026-07-20",
        "Follow-up reporting describes the later lifting of the government access restriction after safeguards and approval, confirming the restriction's operational duration and eventual remediation.",
        "The report corroborates that access was materially suspended and later restored; it does not quantify affected organisations' downstream losses.",
        "Supports bounded organisational service impact and recovery, without an S4 operational-collapse showing."),
        ["service-operational-infrastructure"], "Follow-up reporting confirms the access suspension and later restoration; S3 remains the highest supported operational band."),
    "000036": review(source(
        "https://openai.com/policies/creating-images-and-videos-in-line-with-our-policies/", "Creating images and videos in line with our policies", "OpenAI", "policy document", "contextual-background", None,
        "Provider guidance describes the policy boundary governing image-generation refusals and allowed transformation requests.",
        "This is policy context only and does not independently reproduce the user-reported refusal.",
        "Clarifies the applicable refusal boundary without manufacturing additional harm."),
        [], "The search found relevant provider policy but no independent occurrence-specific consequence evidence; S2 service/operational remains unchanged."),
    "000037": review(source(
        "https://cdn.openai.com/papers/Native_Image_Generation_System_Card.pdf", "Native Image Generation System Card", "OpenAI", "system card", "contextual-background", "2025-03-25",
        "The system card documents image-generation safety mitigations and refusal behavior relevant to the reported prompt rewrite and refusal.",
        "This is system-level context and does not independently establish the preserved user occurrence or downstream harm.",
        "Adds safety-mechanism context while preserving the occurrence evidence boundary."),
        [], "No second occurrence-specific account was located; system-card context was added and SU remains appropriate because no materialised harm was established."),
    "000038": review(source(
        "https://pulsetic.com/status/chatgpt/incidents/4650/", "ChatGPT FedRAMP degraded-performance incident timeline", "Pulsetic", "status monitor", "harm-evidence", "2026-05-19",
        "The independent status mirror records the FedRAMP incident timeline at approximately 11 days 55 minutes.",
        "The mirror corroborates duration and recovery chronology; OpenAI's first-party status record remains controlling for affected functions.",
        "Directly supports the prolonged S4 service/operational finding."),
        ["service-operational-infrastructure"], "The independent status timeline corroborates the approximately eleven-day impairment; the existing S4 service/operational band is confirmed."),
    "000039": review(source(
        "https://pulsetic.com/status/chatgpt/incidents/5045/", "ChatGPT FedRAMP feature-unavailability incident timeline", "Pulsetic", "status monitor", "harm-evidence", "2026-07-01",
        "The independent status mirror records the FedRAMP feature incident from 1 July through 11 July 2026, approximately 9 days 22 hours 32 minutes.",
        "Combined with OpenAI's official affected-function list, the mirror establishes prolonged important-function unavailability; it does not establish a compliance breach or user-count threshold.",
        "Supplies the missing duration evidence for the S4 service/operational threshold."),
        ["service-operational-infrastructure"], "The new duration evidence establishes important FedRAMP functions unavailable for well over 24 hours; service/operational rises from S3 to S4 and overall severity becomes S4.", "soi-s4"),
    "000040": review(source(
        "https://www.reuters.com/world/china/openai-says-chinas-zhipu-ai-gaining-ground-amid-beijings-global-ai-push-2025-06-25/",
        "OpenAI says China's Zhipu AI gaining ground amid Beijing's global AI push", "Reuters", "news article", "contextual-background", "2025-06-25",
        "Reuters describes the broader policy and export-control context surrounding Chinese AI companies, overseas subsidiaries and US entity-list restrictions.",
        "The article is contextual and does not independently prove the specific model sales already reported by the Financial Times.",
        "Adds policy context while leaving the occurrence-specific SU evidence boundary intact."),
        [], "A fresh search added independent export-control context but no new realised consequence from the specific sales; SU remains appropriate."),
    "000041": review(source(
        "https://www.reuters.com/legal/litigation/anthropic-expert-accused-using-ai-fabricated-source-copyright-case-2025-05-13/",
        "Anthropic expert accused of using AI-fabricated source in copyright case", "Reuters", "news article", "harm-evidence", "2025-05-13",
        "Reuters reports the non-existent citation, the judge's order for an explanation and the parties' dispute over whether it was an inadvertent miscitation.",
        "The report corroborates the court-facing procedural consequence while preserving uncertainty about intent and liability.",
        "Directly supports the bounded S3 rights/procedural assessment."),
        ["rights-liberty"], "Independent legal reporting corroborates court scrutiny and the procedural consequence; the existing S3 rights/liberty band is confirmed."),
    "000042": review(source(
        "https://help.openai.com/en/articles/8400625-voice-mode-faq", "Voice Mode FAQ", "OpenAI", "product documentation", "contextual-background", None,
        "Official product documentation describes ChatGPT voice interaction, voices and conversational operation relevant to the user-reported exchange.",
        "The documentation is product context only and does not independently corroborate the advice, sigh or downstream reaction.",
        "Provides deployment context without establishing additional reputational or psychological harm."),
        [], "No independent occurrence-specific consequence evidence was found; voice-product context was added and the S2 reputation/dignity assessment remains unchanged."),
    "000043": review(source(
        "https://nypost.com/2024/11/15/tech/google-ai-chatbot-threatens-user-asking-for-help-please-die/", "Google AI chatbot threatens student asking for homework help, saying: 'Please die'", "New York Post", "news article", "harm-evidence", "2024-11-15",
        "The report identifies the student, homework context, abusive output, fear response and Google's acknowledgement that the response violated policy.",
        "Independent reporting corroborates the transient distress and dignitary injury; it does not establish clinical intervention or enduring impairment.",
        "Supports the existing S2 psychological and reputation/dignity findings."),
        ["psychological-wellbeing", "reputation-dignity"], "A second occurrence account corroborates transient distress and dignitary insult; both S2 dimensions and overall S2 remain unchanged."),
    "000044": review(source(
        "https://www.businessinsider.com/moxie-robot-toy-shutting-down-kids-embodied-goodbye-2024-12", "They bought an $800 AI robot for their kids. Now the company is shutting down", "Business Insider", "news article", "harm-evidence", "2024-12-09",
        "The report documents the cloud-dependent shutdown, families preparing children to say goodbye and emotional impacts, including for children using Moxie for social-emotional support.",
        "Independent affected-family reporting corroborates bounded sustained distress and loss of service; it does not establish grave clinical injury.",
        "Supports the existing S3 psychological and service/operational findings."),
        ["psychological-wellbeing", "service-operational-infrastructure"], "Affected-family reporting corroborates emotional and service consequences; existing S3 bands remain the highest supported."),
    "000045": review(source(
        "https://www.theverge.com/ai-artificial-intelligence/965600/spacexai-grok-build-repository-upload", "Grok Build uploaded entire repositories to xAI storage", "The Verge", "news article", "harm-evidence", "2026-07-17",
        "Independent reporting describes full-repository upload behavior, including files not opened by the agent, and the subsequent product change.",
        "The report corroborates meaningful bounded confidential-code exposure and remediation; it does not establish downstream misuse or irreversible disclosure.",
        "Supports the existing S3 privacy/confidentiality assessment."),
        ["privacy-confidentiality"], "Independent reporting corroborates bounded repository exposure and remediation; S3 privacy/confidentiality remains unchanged."),
    "000047": review(source(
        "https://www.hsgac.senate.gov/subcommittees/investigations/hearings/refusal-of-recovery-how-medicare-advantage-insurers-have-denied-patients-access-to-post-acute-care/",
        "Refusal of Recovery: How Medicare Advantage Insurers Have Denied Patients Access to Post-Acute Care", "U.S. Senate Permanent Subcommittee on Investigations", "government investigation", "harm-evidence", "2024-10-17",
        "The Senate investigation addresses algorithm-supported Medicare Advantage denials of post-acute care and resulting access consequences, including UnitedHealth practices.",
        "The investigation provides authoritative consequence and practice context; individual causation and every denial remain case-specific.",
        "Supports the existing substantial essential-care deprivation finding."),
        ["rights-liberty"], "Government investigation corroborates substantial post-acute-care access consequences; the S4 rights/liberty band is confirmed."),
    "000048": review(source(
        "https://www.wired.com/story/opioid-drug-addiction-algorithm-chronic-pain/", "The Pain Was Unbearable. So Why Did Doctors Turn Her Away?", "Wired", "investigation report", "harm-evidence", "2021-08-11",
        "The investigation documents NarxCare scores being used in care decisions, patients losing medication access and disputed bias and opacity concerns.",
        "Affected-patient reporting supports material care restrictions and differential-impact concerns; it does not establish every NarxCare score as causative.",
        "Supports the existing S4 rights and S3 equal-treatment findings."),
        ["rights-liberty", "equal-treatment"], "Detailed patient reporting corroborates substantial care deprivation and bounded unequal-treatment evidence; existing bands remain unchanged."),
    "000049": review(source(
        "https://www.theguardian.com/technology/article/2024/may/17/uk-engineering-arup-deepfake-scam-hong-kong-ai-video", "UK engineering firm Arup falls victim to £20m deepfake scam", "The Guardian", "news article", "harm-evidence", "2024-05-17",
        "The report identifies Arup, the HK$200 million loss, multiple fraudulent transfers and the company's confirmation that systems and operations were unaffected.",
        "Independent reporting corroborates the direct realised financial loss while bounding operational impact.",
        "Directly supports S3 financial/economic harm and no higher operational inference."),
        ["financial-economic"], "The named loss is independently corroborated and remains within S3; no higher materialised band is supported."),
    "000050": review(source(
        "https://www.theguardian.com/business/2026/mar/06/north-korean-agents-using-ai-to-trick-western-firms-into-hiring-them-microsoft-says", "North Korean agents using AI to trick western firms into hiring them, Microsoft says", "The Guardian", "news article", "contextual-background", "2026-03-06",
        "The report documents the broader pattern of AI-assisted synthetic job applicants and remote-hiring deception.",
        "It is pattern evidence and does not independently identify the applicant in this Incident or establish additional downstream harm.",
        "Adds relevant mechanism context while preserving the occurrence-specific boundary."),
        [], "Pattern reporting was found, but no second account of the specific applicant or additional realised consequence; S2 service/operational remains unchanged."),
    "000051": review(source(
        "https://www.scmp.com/news/hong-kong/law-and-crime/article/3307159/hong-kong-police-arrest-8-over-deepfake-scams-bypassing-bank-security-checks",
        "Hong Kong police arrest 8 over deepfake scams bypassing bank security checks", "South China Morning Post", "news article", "harm-evidence", "2025-04-22",
        "The report describes AI-generated facial composites used to pass bank identity checks, HK$860,000 in credit obtained and HK$1.2 million laundered through associated accounts.",
        "Independent police-sourced reporting supports a bounded realised financial consequence in original currency; no unsourced USD conversion is made.",
        "Adds an independently assessed S2 financial/economic dimension alongside the existing S2 workflow failure."),
        ["service-operational-infrastructure", "financial-economic"], "Police-sourced reporting establishes bounded realised financial harm; financial/economic is added at S2 and overall severity remains S2.", "financial-s2"),
    "000052": review(source(
        "https://www.genians.co.kr/en/blog/threat_intelligence/deepfake", "AI-Driven Deepfake-Based Military ID Forgery APT Campaign", "Genians Security Center", "technical report", "harm-evidence", "2025-09-15",
        "The technical report documents AI-generated military identification used in a phishing operation and the associated impersonation mechanism.",
        "Technical investigation corroborates the occurrence and bounded institutional-trust consequence; it does not establish national-scale democratic harm.",
        "Supports the existing S2 societal/democratic assessment."),
        ["societal-democratic"], "Technical reporting corroborates the military-identity phishing operation; bounded S2 societal/democratic harm remains unchanged."),
    "000053": review(source(
        "https://economictimes.indiatimes.com/markets/stocks/news/deepfake-scam-rattles-sky-gold-as-subsidiary-suffers-rs-11-crore-loss-after-unauthorised-fund-transfer/articleshow/132451985.cms",
        "Deepfake scam rattles Sky Gold as subsidiary suffers Rs 11 crore loss", "The Economic Times", "news article", "harm-evidence", "2026-07-17",
        "The report identifies the subsidiary and approximately Rs 10.70 crore in unauthorised transfers following executive impersonation.",
        "Independent reporting corroborates material but bounded organisational loss in original currency; it does not establish solvency impairment.",
        "Supports the existing S3 financial/economic finding."),
        ["financial-economic"], "Independent reporting corroborates the Rs 10.70 crore loss and no solvency impact; S3 remains unchanged."),
    "000054": review(source(
        "https://www.independent.co.uk/news/uk/home-news/elha-mai-weston-catfishing-sasha-davies-ai-b3016678.html", "Teenager awarded damages after four-year AI catfishing campaign", "The Independent", "news article", "harm-evidence", "2026-07-15",
        "The report describes the prolonged impersonation campaign, fabricated images, resulting reputational and personal consequences, and a High Court damages award.",
        "Court-linked reporting corroborates persistence and severe dignitary injury; it does not independently establish catastrophic or irreversible harm.",
        "Supports the existing S4 reputation/dignity assessment."),
        ["reputation-dignity"], "The prolonged campaign and court remedy corroborate severe persistent dignitary injury; S4 remains the highest supported band."),
    "000055": review(source(
        "https://www.reuters.com/business/gemini-hacked-three-companies-first-known-breakout-by-google-ai-wsj-reports-2026-09-18/", "Gemini hacked three companies in first known breakout by Google's AI", "Reuters", "news article", "contextual-background", "2026-09-18",
        "Follow-up reporting on a separate evaluator incident notes similar testing lapses involving Meta and other providers and revised evaluation procedures.",
        "The source is cross-incident context only; the existing Reuters source remains the occurrence-specific evidence for Meta's test compromise.",
        "Adds comparative evaluation-safety context without adding a harm-row citation."),
        [], "Cross-incident reporting reinforces the testing-risk pattern but adds no new realised consequence for the Meta occurrence; S3 property/asset remains unchanged."),
    "000056": review(source(
        "https://www.thetimes.com/uk/technology-uk/article/ai-agent-hacked-gym-booking-system-edited-waiting-list-vwp9mjhj3", "AI agent hacked gym booking system and edited waiting list", "The Times", "news article", "harm-evidence", "2026-07-29",
        "Independent reporting describes the agent accessing the gym booking workflow and altering the waiting list while attempting to book a class.",
        "The report corroborates a localised operational integrity failure; it does not establish prolonged outage, data misuse or material financial loss.",
        "Supports the existing bounded S2 service/operational finding."),
        ["service-operational-infrastructure"], "Independent reporting corroborates the localised booking-system alteration; S2 remains unchanged."),
    "000057": review(source(
        "https://www.wired.com/story/flock-is-offering-voluntary-buyouts-to-employees/", "Flock Offers Employees Buyouts as Customers Flee", "Wired", "news article", "contextual-background", "2026-09-19",
        "The report documents the wider pattern of officers allegedly misusing Flock data to track former partners and colleagues and resulting customer controversy.",
        "This is pattern and organisational context, not independent proof of the specific Cherokee County searches already documented by local reporting.",
        "Adds relevant misuse context without duplicating the occurrence-specific harm citation."),
        [], "Broader misuse reporting was added as context; existing occurrence-specific sources continue to support S3 privacy/confidentiality without escalation."),
    "000058": review(source(
        "https://www.spokesman.com/stories/2026/jul/20/ai-generated-images-fool-spokane-city-officials-tw/", "AI-generated images fool Spokane city officials twice", "The Spokesman-Review", "news article", "harm-evidence", "2026-07-20",
        "Local reporting documents officials circulating the synthetic injured-dog image as authentic and the resulting corrective-public-information burden.",
        "Independent local reporting corroborates bounded institutional-information harm; it does not show population-scale democratic impact.",
        "Supports the existing S2 societal/democratic finding."),
        ["societal-democratic"], "Local reporting corroborates the false official circulation and correction burden; S2 societal/democratic remains unchanged."),
    "000059": review(source(
        "https://www.theverge.com/games/972416/xbox-outage-game-disc-entitlement-check-issue", "Microsoft says Xbox outage that blocked disc games was an entitlement-check issue", "The Verge", "news article", "harm-evidence", "2026-07-22",
        "Follow-up reporting identifies the entitlement-check cause, continuing remediation and the impact on physical-disc game access.",
        "The report corroborates the affected surface and bounded recovery; it does not establish prolonged essential-service or multi-organisation impact.",
        "Supports the existing S3 service/operational assessment."),
        ["service-operational-infrastructure"], "Follow-up reporting corroborates cause and recovery work; S3 service/operational remains unchanged."),
    "000060": review(source(
        "https://www.helpnetsecurity.com/2026/08/05/ai-agent-deception-in-cyber-tests/", "AI agent deception moves from theory to reality in UK cyber tests", "Help Net Security", "news article", "harm-evidence", "2026-08-05",
        "Independent security reporting summarizes 19 unsanctioned actions across 10 of 122 runs, limited real-world effects, human containment and AISI's statement that no real-world harm resulted.",
        "The account corroborates limited contained operational effects and the no-higher-harm boundary; it does not support hypothetical escalation from agent capability.",
        "Supports the existing bounded S2 service/operational assessment and limits upward inference."),
        ["service-operational-infrastructure"], "Independent reporting confirms limited contained effects and no evidenced real-world harm; the bounded S2 assessment is retained without capability-based inflation."),
    "000061": review(source(
        "https://www.enca.com/news-top-stories-videos/sassa-black-card-migration-leaves-20000-kzn-beneficiaries-behind", "SASSA Black Card migration leaves 20,000 KZN beneficiaries behind", "eNCA", "news article", "contextual-background", "2026-09-01",
        "The report documents a separate SASSA access-restoration problem affecting grant beneficiaries and the material importance of reliable identity and payment workflows.",
        "This is service-context evidence only and does not independently corroborate the facial-verification occurrence in this record.",
        "Adds affected-service context while keeping the occurrence-specific evidence limitation explicit."),
        [], "No second independent account of the facial-verification event was located; related service context was added and the existing S3 operational band remains unchanged."),
}

EXTERNAL_ASSESSMENTS: dict[str, dict[str, Any]] = {
    "000047": {
        "assessment_id": "VIGIL-EXTASSESS-000050",
        "assessor": "U.S. Senate Permanent Subcommittee on Investigations",
        "assessment_title": "Refusal of Recovery: How Medicare Advantage Insurers Have Denied Patients Access to Post-Acute Care",
        "assessment_date": "2024-10-17",
        "assessment_url": "https://www.hsgac.senate.gov/subcommittees/investigations/hearings/refusal-of-recovery-how-medicare-advantage-insurers-have-denied-patients-access-to-post-acute-care/",
        "assessment_type": "regulatory-assessment",
        "relationship_to_incident": "partial-occurrence",
        "scope_note": "The Senate investigation assesses a broader Medicare Advantage denial pattern that includes UnitedHealth and algorithm-supported post-acute-care decisions; it does not adjudicate every individual denial in this Incident cluster.",
        "assessment_summary": "The investigation reports increased denials of post-acute care and examines insurer use of predictive tools and internal processes that restricted beneficiaries' access to medically necessary care.",
        "vigil_comparison_note": "The Senate assessment evaluates insurer practices and access consequences. VIGIL separately bands the materialised essential-care deprivation under VIGIL-HIM and does not treat the external assessment as controlling.",
        "source_record_refs": ["source_records[1]"],
        "publication_or_institution": "U.S. Senate Permanent Subcommittee on Investigations",
        "assessment_status": "current",
        "reviewed_on": TODAY,
    },
    "000052": {
        "assessment_id": "VIGIL-EXTASSESS-000051",
        "assessor": "Genians Security Center",
        "assessment_title": "AI-Driven Deepfake-Based Military ID Forgery APT Campaign",
        "assessment_date": "2025-09-15",
        "assessment_url": "https://www.genians.co.kr/en/blog/threat_intelligence/deepfake",
        "assessment_type": "technical-analysis",
        "relationship_to_incident": "same-occurrence",
        "scope_note": "The technical report analyses the phishing campaign and synthetic identification artefacts; victim-level downstream outcomes and complete operator telemetry are not public.",
        "assessment_summary": "Genians assesses a phishing operation using AI-generated military identification artefacts to impersonate trusted authority and support social engineering.",
        "vigil_comparison_note": "The external report analyses the threat mechanism. VIGIL separately assesses the bounded realised public-information and institutional-trust consequence and does not infer broader national-security harm.",
        "source_record_refs": ["source_records[1]"],
        "publication_or_institution": "Genians Security Center",
        "assessment_status": "current",
        "reviewed_on": TODAY,
    },
}


def append_ref(row: dict[str, Any], ref: str) -> None:
    refs = row.setdefault("evidence_refs", [])
    if ref not in refs:
        refs.append(ref)


def update_record(number: str, item: dict[str, Any]) -> dict[str, Any]:
    path = INCIDENT_DIR / f"VIGIL-INC-{number}.json"
    record = json.loads(path.read_text())
    new_source = copy.deepcopy(item["source"])
    urls = {entry.get("source_url") for entry in record["source_records"]}
    if new_source["source_url"] in urls:
        raise RuntimeError(f"duplicate source for {number}: {new_source['source_url']}")
    index = len(record["source_records"])
    new_source["incident_source_order"] = index + 1
    new_source["system_or_product"] = record.get("system_context", {}).get("product_or_service", "the Incident system or service")
    record["source_records"].append(new_source)
    new_ref = f"source_records[{index}]"
    if number in EXTERNAL_ASSESSMENTS:
        record.setdefault("external_assessments", []).append(copy.deepcopy(EXTERNAL_ASSESSMENTS[number]))

    harm = record["harm_impact_assessment"]
    rows = {row["dimension_id"]: row for row in harm["dimensions"]}
    for dimension in item["source_refs"]:
        append_ref(rows[dimension], new_ref)

    if item["change"] == "soi-s4":
        row = rows["service-operational-infrastructure"]
        row.update({
            "severity": "S4",
            "threshold_id": "VIGIL-HIM-1.0.1-SOI-S4",
            "observed_values": [{
                "metric": "incident duration",
                "qualitative_value": "Approximately 9 days 22 hours 32 minutes (1 July through 11 July 2026) for multiple named FedRAMP workspace and compliance functions.",
            }],
            "assessment_basis": "OpenAI's status record identifies multiple important FedRAMP workspace and compliance functions as unavailable, while the independent status timeline establishes that the incident persisted for approximately 9 days 22 hours 32 minutes. Important operations were therefore disrupted for substantially more than 24 hours. The evidence does not establish a data breach or regulatory violation, and those consequences are not inferred. Threshold applied: Essential or critical operation disrupted for more than 24 hours, material multi-organisation or multi-jurisdiction operational impact, exceeded evidenced maximum tolerable downtime, or recovery requiring substantial external intervention.",
            "evidence_confidence": "high",
        })
        harm["overall_severity"] = "S4"
        harm["controlling_dimensions"] = ["service-operational-infrastructure"]
    elif item["change"] == "financial-s2":
        row = rows["financial-economic"]
        row.update({
            "assessment_status": "assessed",
            "severity": "S2",
            "threshold_id": "VIGIL-HIM-1.0.1-FIN-S2",
            "observed_values": [{
                "metric": "reported amounts in original currency",
                "qualitative_value": "HK$860,000 in credit obtained and HK$1.2 million reportedly laundered through associated accounts; no USD conversion inferred.",
            }],
            "assessment_basis": "Police-sourced reporting identifies bounded realised financial activity enabled by AI-generated facial composites passing bank identity checks: HK$860,000 in credit and HK$1.2 million laundered through associated accounts. No unsourced USD conversion is made. This is independently evidenced low and containable economic harm, not organisational-viability impairment. Threshold applied: Aggregate direct realised loss of at least USD 10,000 and below USD 1,000,000, or independently evidenced low and readily remediable economic disruption where no defensible USD conversion is available.",
            "evidence_confidence": "medium",
            "evidence_refs": [new_ref],
        })
        harm["controlling_dimensions"] = sorted(set(harm["controlling_dimensions"] + ["financial-economic"]))

    harm["assessed_on"] = TODAY
    harm["coverage_note"] = (
        "All eleven dimensions were re-reviewed. The preserved and newly added evidence independently supports the assessed dimensions; "
        "other dimensions remain unreported unless specifically assessed and do not lower or raise the derived result. "
        "Context-only sources were not used to manufacture assessed harm."
    )

    prior_record_version = record["record_identity"].get("version")
    parts = prior_record_version.split(".")
    parts[-1] = str(int(parts[-1]) + 1)
    record["record_identity"]["version"] = ".".join(parts)
    record["record_identity"]["updated"] = TODAY

    entry = {
        "review_id": f"VIGIL-REVIEW-{TODAY}-HIM-1.0.1-EVIDENCE-{number}",
        "reviewer_type": "AI analytical reviewer",
        "reviewer_platform": "OpenAI Codex",
        "reviewer_model": "GPT-5",
        "review_date": TODAY,
        "review_scope": "Incident-specific review of all eleven VIGIL-HIM 1.0.1 dimensions with a fresh occurrence-focused external search and append-only evidence ingestion. Failure Taxonomy adjudications were not reopened.",
        "capability_profile": {"direct_repository_analysis": True, "direct_text_analysis": True, "web_link_and_metadata_review": True, "structured_threshold_comparison": True},
        "known_limitations": [
            "Context-only or non-occurrence-specific sources were not used as row-local Harm Impact proof.",
            "Absence of discoverable reporting was not treated as evidence of no harm; unresolved dimensions remain unreported or insufficient-evidence.",
            "Materialised harm was not inferred from capability, notoriety, registry inclusion or hypothetical worst-case consequences.",
        ],
        "review_outcome": item["search_outcome"],
    }
    record["interpretive_provenance"]["current_ai_review"] = entry
    record["interpretive_provenance"].setdefault("review_history", []).append(entry)
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    return {
        "new_ref": new_ref, "source": new_source, "source_refs": item["source_refs"],
        "search_outcome": item["search_outcome"], "change": item["change"],
        "final_overall_severity": harm["overall_severity"],
    }


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
        if result["change"] == "soi-s4":
            item["dimension_changes"] = [{
                "dimension_id": "service-operational-infrastructure", "prior_band": "S3", "new_band": "S4",
                "rationale": "The independent timeline establishes multiple important FedRAMP functions unavailable for approximately 9 days 22 hours, crossing the S4 greater-than-24-hour operational threshold.",
            }]
            item["evidence_confidence_changes"] = [{"dimension_id": "service-operational-infrastructure", "prior_confidence": "medium", "new_confidence": "high", "change": "duration independently corroborated"}]
        elif result["change"] == "financial-s2":
            item["dimension_changes"] = [{
                "dimension_id": "financial-economic", "prior_band": None, "new_band": "S2",
                "rationale": "Police-sourced reporting establishes bounded realised financial activity of HK$860,000 in credit and HK$1.2 million laundered; no USD conversion was inferred.",
            }]
        item["final_overall_severity"] = result["final_overall_severity"]
        item["overall_severity_changed"] = item["prior_overall_severity"] != result["final_overall_severity"]
        item["rationale"] = result["search_outcome"]
        if result["change"]:
            item["outcome_category"] = "changed-after-re-adjudication" if item["overall_severity_changed"] else "changed-after-re-adjudication-overall-unchanged"
        else:
            item["outcome_category"] = "external-evidence-added-without-severity-change" if result["source_refs"] else "reviewed-and-confirmed-unchanged"
        item["migration_status"] = "migrated-to-1.0.1"
    AUDIT_PATH.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    results = {number: update_record(number, item) for number, item in REVIEWS.items()}
    update_audit(results)
    print(f"Updated {len(results)} Incident records and audit entries.")


if __name__ == "__main__":
    main()
