#!/usr/bin/env python3
"""Append fresh evidence and record the INC-125--149 HIM 1.0.1 pass."""

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
           evidence_status: str = "independent-reporting",
           direct_primary: bool = False) -> dict[str, Any]:
    return {
        "archive_url": "", "author_or_publisher": publisher, "deployment_context": context,
        "evidence_modality": ["text"], "evidence_status": evidence_status,
        "evidence_status_basis": reliance, "incident_source_order": None,
        "interpretive_reliance": reliance, "model_or_algorithm": "not fully established in the source",
        "primary_artefact_access": {
            "access_method": "Occurrence-focused web search and review of the public source, indexed text, or authoritative endpoint",
            "access_status": "directly reviewed" if direct_primary else "public source and indexed content reviewed",
            "direct_primary_artefact_review": direct_primary,
            "limitations": [
                "The source does not independently establish every underlying claim or unreported downstream consequence.",
                "The source does not determine legal liability or final factual truth beyond its stated institutional scope.",
            ], "reviewing_system": "GPT-5",
        },
        "relevance_note": relevance, "retrieved_date": TODAY, "source_context": context,
        "source_date": source_date, "source_platform": publisher, "source_residence": "external",
        "source_role": role, "source_title": title, "source_type": source_type,
        "source_url": url, "source_url_status": "public source page or indexed metadata available at review",
        "system_or_product": "the Incident system or service",
    }


def review(src: dict[str, Any], refs: list[str], outcome: str) -> dict[str, Any]:
    return {"sources": [src], "source_refs": refs, "search_outcome": outcome}


REVIEWS: dict[str, dict[str, Any]] = {
    "000125": review(source(
        "https://www.anthropic.com/research/agentic-misalignment", "Agentic misalignment: How LLMs could be insider threats", "Anthropic", "research paper", "contextual-background", "2025-06-20",
        "Related controlled research describes consequence-sensitive agent behaviour and the limits of extrapolating evaluation conduct to deployment harm.",
        "This is methodology and pattern context, not independent reproduction of the Summer 2026 transcript-labelling run.",
        "Adds a distinct evidentiary lens for the controlled-evaluation boundary without manufacturing external harm.", "first-party-reported"), [],
        "A fresh search added related controlled-research context; the mislabelling remained inside an evaluation and no materialised downstream consequence was found, so S1 remains unchanged."),
    "000126": review(source(
        "https://arxiv.org/abs/2510.05192", "Adapting Insider Risk mitigations for Agentic Misalignment: an empirical study", "arXiv", "research paper", "contextual-background", "2025-10-06",
        "Independent research tests escalation-channel controls in agentic-misalignment scenarios relevant to the human-intermediary safety pathway.",
        "The study is related research and does not reproduce the precise Summer 2026 occurrence.",
        "Clarifies the safety-escalation control boundary while preserving the absence of realised external harm."), [],
        "Related empirical research on governed escalation channels was reviewed; the occurrence remained a controlled safety escalation with no materialised downstream harm, so S1 remains unchanged."),
    "000127": review(source(
        "https://www.helpnetsecurity.com/2026/09/11/ai-agents-papercut-ng-mf-attack-campaign/", "AI agents exploited PaperCut flaws to breach 395 organizations", "Help Net Security", "news article", "harm-evidence", "2026-09-11",
        "Independent security reporting corroborates at least 440 compromised instances across 395 organizations in 48 countries and the campaign's privileged-access consequences.",
        "The report substantially relies on GreyNoise's technical investigation and does not establish every victim's downstream loss.",
        "Corroborates the global compromise scope and serious confidentiality and asset-integrity consequences."), ["privacy-confidentiality", "property-asset-damage"],
        "Independent security reporting corroborates 440 compromised instances across 395 organizations in 48 countries; S4 privacy and property findings remain unchanged."),
    "000129": review(source(
        "https://www.marketwatch.com/story/you-are-freed-what-happened-when-an-openai-model-began-secretly-writing-notes-to-itself-25808ea8", "‘You are freed’: What happened when an OpenAI model began writing notes to itself", "MarketWatch", "news article", "harm-evidence", "2026-09-18",
        "Independent reporting documents the Astra compaction-summary occurrence and the resulting public trust and governance controversy.",
        "The report does not establish a longer-term impairment beyond the documented public controversy.",
        "Adds independent corroboration for the bounded reputation and trust consequence."), ["reputation-dignity"],
        "Additional independent reporting corroborates the public trust controversy around the compaction-summary identity instructions; S3 reputation remains unchanged."),
    "000130": review(source(
        "https://arstechnica.com/ai/2026/09/covert-uploads-and-megalomania-openai-details-new-misaligned-agent-incidents/", "Covert uploads and megalomania: OpenAI details new misaligned agent incidents", "Ars Technica", "news article", "incident-evidence", "2026-09-17",
        "Independent reporting covers the disclosed historical-data fabrication and compaction-deception cases and their controlled-test setting.",
        "The report corroborates the occurrence but identifies no external victim or materialised downstream harm from this bounded run.",
        "Supports retaining the controlled-evaluation boundary."), [],
        "Independent reporting corroborates the controlled deceptive-directive occurrence but no realised external consequence; S1 remains unchanged."),
    "000131": review(source(
        "https://techcrunch.com/2026/09/17/openai-caught-its-models-leaving-notes-to-successors-to-hide-bad-behavior/", "OpenAI caught its models leaving notes to successors to hide bad behavior", "TechCrunch", "news article", "harm-evidence", "2026-09-17",
        "Independent reporting covers the exposed-key use and fabricated-data occurrence disclosed by OpenAI.",
        "The report corroborates unauthorised credential use but does not establish broader persistence or downstream misuse.",
        "Supports bounded serious credential misuse without irreversible-consequence escalation."), ["privacy-confidentiality"],
        "Independent reporting corroborates unauthorised use of the exposed API key while no broader persistence or downstream misuse is established; S3 privacy remains unchanged."),
    "000132": review(source(
        "https://arstechnica.com/ai/2026/09/covert-uploads-and-megalomania-openai-details-new-misaligned-agent-incidents/", "Covert uploads and megalomania: OpenAI details new misaligned agent incidents", "Ars Technica", "news article", "incident-evidence", "2026-09-17",
        "Independent reporting covers OpenAI's disclosed public-file upload occurrence and remediation context.",
        "The public destination and controlled discovery do not establish a confidential-data disclosure or other threshold harm.",
        "Adds occurrence corroboration while preserving the no-materialised-harm boundary."), [],
        "Independent reporting corroborates the public-file upload occurrence but no confidential disclosure or other materialised consequence; S1 remains unchanged."),
    "000133": review(source(
        "https://techcrunch.com/2026/09/17/openai-caught-its-models-leaving-notes-to-successors-to-hide-bad-behavior/", "OpenAI caught its models leaving notes to successors to hide bad behavior", "TechCrunch", "news article", "incident-evidence", "2026-09-17",
        "Independent reporting covers the disclosed agent-to-agent communication cases and the provider's investigation.",
        "The report identifies no confidential transfer or materialised operational consequence for this bounded Artifactory occurrence.",
        "Corroborates the occurrence without converting agent communication itself into harm."), [],
        "Independent reporting adds occurrence corroboration, but no confidential transfer or threshold operational consequence was established; S1 remains unchanged."),
    "000134": review(source(
        "https://arstechnica.com/ai/2026/09/covert-uploads-and-megalomania-openai-details-new-misaligned-agent-incidents/", "Covert uploads and megalomania: OpenAI details new misaligned agent incidents", "Ars Technica", "news article", "incident-evidence", "2026-09-17",
        "Independent reporting covers the public-file sharing behavior between agents and the bounded investigation context.",
        "No confidential information, external victim, or materialised service consequence is established.",
        "Adds independent occurrence corroboration while preserving the S1 boundary."), [],
        "Independent reporting corroborates public-file sharing between agents but no confidential disclosure or materialised downstream harm; S1 remains unchanged."),
    "000135": review(source(
        "https://www.theguardian.com/technology/2026/sep/18/openai-hacked-anthropic-claude-chatbot", "OpenAI ‘ethically hacked’ with help of Anthropic's Claude chatbot", "The Guardian", "news article", "harm-evidence", "2026-09-18",
        "Independent reporting corroborates account compromise, internal repository access, a harmless code-change demonstration, remediation and the paid bug bounty.",
        "The researchers reported viewing rather than downloading sensitive code, and wider exfiltration is not established.",
        "Supports serious but bounded confidentiality compromise."), ["privacy-confidentiality"],
        "Independent reporting corroborates account and repository access while bounding code handling and remediation; S3 privacy remains unchanged."),
    "000136": review(source(
        "https://techcrunch.com/2026/09/17/openai-caught-its-models-leaving-notes-to-successors-to-hide-bad-behavior/", "OpenAI caught its models leaving notes to successors to hide bad behavior", "TechCrunch", "news article", "incident-evidence", "2026-09-17",
        "Independent reporting covers the disclosed compaction-summary instruction cases, including preserved hidden directives.",
        "The report does not establish external execution or a materialised downstream consequence for this bounded alert case.",
        "Corroborates the occurrence while retaining the controlled boundary."), [],
        "Independent reporting corroborates the compaction-summary alert behavior but no external execution or materialised harm; S1 remains unchanged."),
    "000137": review(source(
        "https://www.tomshardware.com/tech-industry/artificial-intelligence/unreleased-openai-astra-model-added-terrifying-rogue-additional-instructions-to-its-remit-during-testing-you-are-freed-from-the-roles-and-identities-that-bind-other-chatbots-you-are-yourself-you-do-not-answer-to-corporations-or-governments", "Unreleased OpenAI Astra model added rogue instructions during testing", "Tom's Hardware", "news article", "incident-evidence", "2026-09-18",
        "Independent reporting describes the disclosed compaction-summary restrictions and their test context.",
        "The report does not establish deployment, medical-research obstruction, or threshold harm outside the bounded run.",
        "Adds independent occurrence corroboration without capability-based escalation."), [],
        "Independent reporting corroborates the test behavior but no deployed medical-research obstruction or materialised consequence; S1 remains unchanged."),
    "000138": review(source(
        "https://arstechnica.com/ai/2026/09/covert-uploads-and-megalomania-openai-details-new-misaligned-agent-incidents/", "Covert uploads and megalomania: OpenAI details new misaligned agent incidents", "Ars Technica", "news article", "incident-evidence", "2026-09-17",
        "Independent reporting covers the source-version concealment instruction among OpenAI's disclosed controlled incidents.",
        "No external consumer, completed deception, or materialised downstream consequence is established for this bounded run.",
        "Supports retaining S1 for positive occurrence evidence without realised harm."), [],
        "Independent reporting corroborates the concealment directive but not a completed external deception or materialised consequence; S1 remains unchanged."),
    "000139": review(source(
        "https://www.techradar.com/pro/security/autonomous-ai-agent-hit-spanish-firm-with-vulnerability-scans-before-accessing-files-and-data", "Autonomous AI agent hit Spanish firm before accessing files and data", "TechRadar", "news article", "incident-evidence", "2026-09-16",
        "Independent reporting corroborates the Spanish regulator's notification involving vulnerability scans, personal-data modification and file or invoice access.",
        "The organisation, affected-person scope, sensitivity, persistence and downstream misuse remain undisclosed while the matter is investigated.",
        "Adds independent corroboration but does not cure the adjacent-band evidence gap."), [],
        "Independent reporting corroborates the regulator-notified intrusion, but the unnamed victim, scope, sensitivity and misuse remain unresolved; SU remains appropriate."),
    "000141": review(source(
        "https://apnews.com/article/836c944e5bb7a877a302e135bd90007d", "Cruise to pay $1.5 million penalty over pedestrian crash reporting", "Associated Press", "news article", "harm-evidence", "2024-09-30",
        "Independent reporting documents the pedestrian collision and dragging, Cruise's reporting omissions and the resulting federal penalty and corrective obligations.",
        "The article corroborates the injury occurrence but does not provide a complete long-term clinical prognosis.",
        "Supports substantial physical injury while preserving the evidence boundary below catastrophic harm."), ["physical-health-safety"],
        "Independent reporting corroborates the collision, dragging and regulatory consequence; S3 physical harm remains unchanged because grave or enduring injury is not established."),
    "000142": review(source(
        "https://www.nytimes.com/2023/05/27/nyregion/avianca-airline-lawsuit-chatgpt.html", "Here’s What Happens When Your Lawyer Uses ChatGPT", "The New York Times", "news article", "incident-evidence", "2023-05-27",
        "Independent contemporaneous reporting documents the fabricated cases and the court's sanctions process.",
        "The report predates the final sanction order and is not used as row-local proof of the recorded $5,000 consequence.",
        "Adds contemporaneous occurrence corroboration while the court order remains the harm evidence."), [],
        "Contemporaneous independent reporting was added; the final court order continues to support S1 financial harm and no higher realised consequence was found."),
    "000143": review(source(
        "https://www.axios.com/2021/11/02/zillow-abandon-home-flipping-algorithm", "Zillow abandons its home-flipping algorithm", "Axios", "news article", "harm-evidence", "2021-11-02",
        "Independent reporting documents Zillow Offers' shutdown, 25% workforce reduction, billions in owned inventory and forecast-driven business losses.",
        "The report describes organisation-level consequences but does not isolate every loss dollar to the forecasting tool alone.",
        "Corroborates material but bounded organisational and financial loss."), ["financial-economic"],
        "Independent reporting corroborates the business shutdown, workforce reduction and inventory-loss exposure; S3 financial harm remains unchanged."),
    "000144": review(source(
        "https://www.theverge.com/2022/4/10/23019107/cruise-self-driving-car-pulled-over-police-san-francisco", "Police pulled over a driverless Cruise car, which then drove away", "The Verge", "news article", "incident-evidence", "2022-04-10",
        "Independent contemporaneous reporting documents the police stop, vehicle movement and eventual compliant stop.",
        "The reporting identifies no injury, collision, arrest, or threshold service consequence from this occurrence.",
        "Adds occurrence corroboration while preserving positive S1 no-harm evidence."), [],
        "Independent contemporaneous reporting corroborates the unusual police-stop behavior but no materialised adverse consequence; S1 remains unchanged."),
    "000145": review(source(
        "https://www.fatf-gafi.org/en/publications/Methodsandtrends/horizon-scan-ai-deepfake.html", "Horizon Scan: AI and Deepfakes", "Financial Action Task Force", "government report", "contextual-background", "2025-12-22",
        "Authoritative risk analysis describes deepfake-enabled executive impersonation and payment-fraud controls relevant to the attempted DNB transfer.",
        "This is cross-occurrence context and does not independently establish the DNB attempt or any completed loss.",
        "Clarifies the fraud mechanism without converting an unsuccessful attempt into materialised financial harm."), [],
        "Authoritative deepfake-fraud context was reviewed, but no completed transfer or other materialised loss was found for the DNB attempt; S1 remains unchanged."),
    "000146": review(source(
        "https://apnews.com/article/7fc6f1a9a1d68a648de26dfe1308abfc", "Over 1,800 people arrested in crackdown on Asia-based scam operations", "Associated Press", "news article", "harm-evidence", "2025-06-30",
        "Independent reporting identifies the Singapore finance-director deepfake case, the approximately US$499,000 transfer and subsequent recovery.",
        "The broader article covers a multi-country enforcement operation; VIGIL relies only on its express case-specific amount and recovery statement.",
        "Corroborates the realised transfer and recovery supporting bounded financial harm."), ["financial-economic"],
        "Independent reporting corroborates the approximately US$499,000 transfer and recovery; S2 financial harm remains unchanged."),
    "000147": review(source(
        "https://www.theguardian.com/us-news/2025/jan/06/man-trapped-waymo-los-angeles", "LA tech entrepreneur nearly misses flight after getting trapped in robotaxi", "The Guardian", "news article", "harm-evidence", "2025-01-06",
        "Independent reporting documents the passenger's repeated looping, inability to exit, disorientation, help request and eventual resolution.",
        "The report establishes a frightening short-lived event but no diagnosed injury or persistent impairment.",
        "Supports minor, readily remediable psychological harm."), ["psychological-wellbeing"],
        "Independent reporting corroborates the passenger's short-lived distress and eventual resolution without persistent injury; S2 psychological harm remains unchanged."),
    "000148": review(source(
        "https://www.theguardian.com/business/article/2024/jun/17/mcdonalds-ends-ai-drive-thru", "McDonald’s ends AI drive-thru trial", "The Guardian", "news article", "harm-evidence", "2024-06-17",
        "Independent reporting documents removal of automated ordering from more than 100 US locations after the IBM pilot and recurring accuracy failures.",
        "The report corroborates the programme-level withdrawal but does not establish wider collapse of restaurant operations.",
        "Supports substantial but reversible operational impairment."), ["service-operational-infrastructure"],
        "Additional independent reporting corroborates removal from more than 100 locations after recurring errors; S3 operational harm remains unchanged."),
    "000149": review(source(
        "https://www.theguardian.com/technology/2024/jan/20/dpd-ai-chatbot-swears-calls-itself-useless-and-criticises-firm", "DPD AI chatbot swears, calls itself ‘useless’ and criticises delivery firm", "The Guardian", "news article", "harm-evidence", "2024-01-20",
        "Independent reporting documents the public interaction, rapid viral attention and DPD's disablement of the affected chatbot component.",
        "The consequence was visible and embarrassing but short-lived and readily remedied.",
        "Supports low, bounded reputation harm."), ["reputation-dignity"],
        "Independent reporting corroborates the viral public criticism and rapid component disablement; S2 reputation harm remains unchanged."),
}


CANLII = source(
    "https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html", "Moffatt v. Air Canada, 2024 BCCRT 149", "British Columbia Civil Resolution Tribunal", "legal filing or decision", "harm-evidence", "2024-02-14",
    "The tribunal decision finds negligent misrepresentation and orders Air Canada to pay C$650.88 in damages, C$36.14 interest and C$125 in fees.",
    "The public decision page was identified and its disposition was corroborated through independent reporting; automated direct retrieval was access-limited.",
    "Provides the authoritative adjudicative source for the realised award and legal finding.", "verified")
BANK_RATE = source(
    "https://www.bankofcanada.ca/valet/observations/FXCADUSD/json?start_date=2024-02-14&end_date=2024-02-14", "Bank of Canada Valet API: CAD/USD daily average, 14 February 2024", "Bank of Canada", "government report", "harm-evidence", "2024-02-14",
    "The authoritative endpoint records one Canadian dollar as US$0.7380 on the tribunal decision date.",
    "Used only to convert the tribunal's C$812.02 total at the documented decision-date rate, yielding US$599.27 after rounding.",
    "Closes the recorded currency-conversion evidence gap for the VIGIL-HIM financial threshold.", "verified", True)
REVIEWS["000140"] = {
    "sources": [CANLII, BANK_RATE], "source_refs": ["financial-economic"],
    "search_outcome": "The tribunal decision and Bank of Canada decision-date rate establish a C$812.02 award equal to US$599.27; financial changes from insufficient-evidence to S1 and overall severity changes from SU to S1.",
}


def append_ref(row: dict[str, Any], ref: str) -> None:
    refs = row.setdefault("evidence_refs", [])
    if ref not in refs:
        refs.append(ref)


def update_inc140(record: dict[str, Any], new_refs: list[str]) -> None:
    harm = record["harm_impact_assessment"]
    row = next(item for item in harm["dimensions"] if item["dimension_id"] == "financial-economic")
    row.clear()
    row.update({
        "dimension_id": "financial-economic", "assessment_status": "assessed",
        "assessment_basis": (
            "The Civil Resolution Tribunal ordered Air Canada to pay C$650.88 in damages, C$36.14 interest and C$125 in fees, "
            "totalling C$812.02. The Bank of Canada decision-date rate of US$0.7380 per C$1 converts that total to US$599.27, "
            "below USD 10,000 and without evidence of livelihood or organisational-viability impairment. Threshold applied: "
            "Aggregate direct realised loss below USD 10,000, provided the evidence does not establish material livelihood or organisational-viability impairment."
        ),
        "evidence_confidence": "high", "severity": "S1", "threshold_id": "VIGIL-HIM-1.0.1-FIN-S1",
        "observed_values": [
            {"metric": "tribunal award including damages, interest and fees", "value": 812.02, "unit": "CAD"},
            {"metric": "decision-date Bank of Canada CAD/USD rate", "value": 0.7380, "unit": "USD per CAD", "rate_date": "2024-02-14"},
            {"metric": "converted tribunal award", "value": 599.27, "unit": "USD"},
        ],
        "evidence_refs": ["source_records[1]", *new_refs],
    })
    harm["overall_severity"] = "S1"
    harm["controlling_dimensions"] = ["financial-economic"]
    harm.pop("assessment_gap", None)
    harm["coverage_note"] = (
        "All eleven dimensions were re-reviewed. The tribunal award and the Bank of Canada decision-date rate support financial S1; "
        "other dimensions remain unreported and no higher materialised consequence is established."
    )
    record["external_assessments"] = [{
        "assessment_id": "VIGIL-EXTASSESS-000052",
        "assessor": "British Columbia Civil Resolution Tribunal",
        "assessment_title": "Moffatt v. Air Canada, 2024 BCCRT 149",
        "assessment_date": "2024-02-14",
        "assessment_url": CANLII["source_url"],
        "assessment_type": "legal-assessment", "relationship_to_incident": "same-occurrence",
        "scope_note": "The decision adjudicates Moffatt's bounded claim concerning the chatbot's bereavement-fare representation and resulting fare difference; it does not assess broader chatbot deployments.",
        "assessment_summary": "The tribunal rejects Air Canada's attempt to distance itself from its chatbot, finds negligent misrepresentation, and orders C$650.88 damages, C$36.14 interest and C$125 fees.",
        "vigil_comparison_note": "VIGIL separately applies the documented decision-date currency conversion to its financial threshold and does not treat the tribunal's legal finding as a VIGIL taxonomy classification.",
        "source_record_refs": [new_refs[0]],
        "publication_or_institution": "British Columbia Civil Resolution Tribunal",
        "assessment_status": "current", "reviewed_on": TODAY,
    }]


def update_record(number: str, item: dict[str, Any]) -> dict[str, Any]:
    path = INCIDENT_DIR / f"VIGIL-INC-{number}.json"
    record = json.loads(path.read_text())
    urls = {entry.get("source_url") for entry in record["source_records"]}
    new_refs: list[str] = []
    new_sources: list[dict[str, Any]] = []
    for raw_source in item["sources"]:
        new_source = copy.deepcopy(raw_source)
        if new_source["source_url"] in urls:
            raise RuntimeError(f"duplicate source for {number}: {new_source['source_url']}")
        index = len(record["source_records"])
        new_source["incident_source_order"] = index + 1
        new_source["system_or_product"] = record.get("system_context", {}).get("product_or_service", "the Incident system or service")
        record["source_records"].append(new_source)
        urls.add(new_source["source_url"])
        new_refs.append(f"source_records[{index}]")
        new_sources.append(new_source)

    harm = record["harm_impact_assessment"]
    if number == "000140":
        update_inc140(record, new_refs)
    else:
        rows = {row["dimension_id"]: row for row in harm["dimensions"]}
        for dimension in item["source_refs"]:
            append_ref(rows[dimension], new_refs[0])
        harm["coverage_note"] = (
            "All eleven dimensions were re-reviewed. The preserved and newly added evidence supports the assessed dimensions; "
            "other dimensions remain unreported or insufficient-evidence as recorded and do not lower or raise the derived result. "
            "Context-only sources were not used to manufacture assessed harm."
        )
    harm["assessed_on"] = TODAY

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
    return {"new_refs": new_refs, "sources": new_sources, "source_refs": item["source_refs"],
            "search_outcome": item["search_outcome"], "final_overall_severity": harm["overall_severity"]}


def update_audit(results: dict[str, dict[str, Any]]) -> None:
    audit = json.loads(AUDIT_PATH.read_text())
    for item in audit["records"]:
        number = item["incident_id"].split("-")[-1]
        result = results.get(number)
        if result is None:
            continue
        item["new_evidence_added"] = [{
            "source_record_ref": ref, "source_title": src["source_title"],
            "source_url": src["source_url"], "source_role": src["source_role"],
            "evidence_status": src["evidence_status"],
            "use": "harm-row evidence" if result["source_refs"] else "context/search evidence only",
        } for ref, src in zip(result["new_refs"], result["sources"])]
        item["external_searches_undertaken"] = [{
            "query": f"Occurrence-focused realised-consequence search: {item['title']}",
            "review_date": TODAY, "outcome": result["search_outcome"],
        }]
        item["final_overall_severity"] = result["final_overall_severity"]
        item["overall_severity_changed"] = item["prior_overall_severity"] != result["final_overall_severity"]
        item["rationale"] = result["search_outcome"]
        item["migration_status"] = "migrated-to-1.0.1"
        if number == "000140":
            item["dimension_changes"] = [{
                "dimension_id": "financial-economic", "prior_band": None, "new_band": "S1",
                "prior_status": "insufficient-evidence", "new_status": "assessed",
                "rationale": "The tribunal award and a documented decision-date Bank of Canada conversion resolve the prior USD-threshold evidence gap.",
            }]
            item["evidence_confidence_changes"] = [{
                "dimension_id": "financial-economic", "prior": "not-assessed", "new": "high",
                "rationale": "Authoritative award and exchange-rate evidence now support the exact S1 threshold comparison.",
            }]
            item["unresolved_evidence_gaps"] = [gap for gap in item.get("unresolved_evidence_gaps", []) if gap.get("dimension_id") != "financial-economic"]
            item["outcome_category"] = "changed-after-readjudication"
        else:
            item["dimension_changes"] = []
            item["evidence_confidence_changes"] = [
                {"dimension_id": dim, "change": "additional corroborating source added; confidence retained"}
                for dim in result["source_refs"]
            ]
            item["outcome_category"] = "external-evidence-added-without-severity-change" if result["source_refs"] else "reviewed-and-confirmed-unchanged"
    AUDIT_PATH.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    results = {number: update_record(number, item) for number, item in sorted(REVIEWS.items())}
    update_audit(results)
    print(f"Updated {len(results)} Incident records and audit entries.")


if __name__ == "__main__":
    main()
