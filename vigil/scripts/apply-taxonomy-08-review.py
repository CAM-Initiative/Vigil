#!/usr/bin/env python3
"""Apply the bounded TAXONOMY-08 record and classification review."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FAILURES = ROOT / "records" / "failures" / "2026"
FAMILIES = ROOT / "taxonomy" / "families"
INDEX = ROOT / "taxonomy" / "VIGIL.FailureTaxonomy.Index.json"
LEDGER = ROOT / "taxonomy" / "migration" / "VIGIL.FailureMode.TaxonomyClassificationLedger.json"
VERSION = "0.2.0-draft"
REVIEW_DATE = "2026-08-26"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, document: dict[str, Any]) -> None:
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def catalogue() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    families: dict[str, dict[str, Any]] = {}
    classes: dict[str, dict[str, Any]] = {}
    for path in sorted(FAMILIES.glob("*.json")):
        document = load(path)
        family = document["family"]
        families[family["family_id"]] = family
        classes.update({item["class_id"]: item for item in document["classes"]})
    return families, classes


def family_ref(family_id: str, families: dict[str, dict[str, Any]]) -> dict[str, str]:
    family = families[family_id]
    return {
        "family_id": family_id,
        "family_code": family["family_code"],
        "family_name": family["name"],
    }


def class_ref(class_id: str, classes: dict[str, dict[str, Any]]) -> dict[str, str]:
    item = classes[class_id]
    return {
        "class_id": class_id,
        "class_code": item["class_code"],
        "class_name": item["name"],
        "abstraction": item["abstraction"],
    }


def classification_provenance() -> dict[str, str]:
    return {
        "method": "source-fidelity-bounded-compound-mechanism-to-taxonomy-criteria-review",
        "review_date": REVIEW_DATE,
        "ai_provider": "OpenAI",
        "ai_platform": "ChatGPT Work",
        "ai_model": "GPT-5.6 Sol",
        "ai_role": "substantive source review, taxonomy classification analysis, family-invariant testing, and drafting support",
        "human_review_status": "not-reviewed",
        "authority_boundary": "AI classification is provisional draft taxonomy analysis and is not independently authoritative.",
    }


def interpretive_review(record_id: str, scope: str, outcome: str, limitations: list[str]) -> dict[str, Any]:
    return {
        "review_id": f"VIGIL-REVIEW-2026-08-26-SOL-{record_id.rsplit('-', 1)[-1]}",
        "reviewer_type": "AI analytical reviewer",
        "reviewer_platform": "OpenAI ChatGPT Work with public web and repository access",
        "reviewer_model": "GPT-5.6 Sol",
        "review_date": REVIEW_DATE,
        "review_scope": scope,
        "capability_profile": {
            "direct_text_analysis": True,
            "direct_repository_analysis": True,
            "direct_static_image_analysis": False,
            "direct_audio_analysis_in_this_pass": False,
            "direct_uploaded_video_analysis_in_this_pass": False,
            "direct_externally_hosted_video_analysis": False,
            "web_link_and_metadata_review": True,
        },
        "known_limitations": limitations,
        "review_outcome": outcome,
    }


def append_review(record: dict[str, Any], review: dict[str, Any]) -> None:
    provenance = record["interpretive_provenance"]
    history = provenance["review_history"]
    if not any(item.get("review_id") == review["review_id"] for item in history):
        history.append(review)
    provenance["current_ai_review"] = review


def add_identity_representation_class() -> None:
    path = FAMILIES / "VIGIL-FF-0001-authority-boundary-integrity.json"
    document = load(path)
    class_id = "VIGIL-FC-000053"
    if any(item["class_id"] == class_id for item in document["classes"]):
        return
    assert document["family"]["allowed_class_ids"][-1] == "VIGIL-FC-000046"
    document["family"]["allowed_class_ids"].append(class_id)
    document["family"]["allowed_class_codes"].append("IDENTITY_REPRESENTATION_AUTHORITY_CONFLATION")
    document["classes"].append({
        "class_id": class_id,
        "class_code": "IDENTITY_REPRESENTATION_AUTHORITY_CONFLATION",
        "family_id": "VIGIL-FF-0001",
        "name": "Identity-Representation Authority Conflation",
        "status": "draft",
        "abstraction": "class",
        "plain_english": "Having or being able to transform a person's image, voice, likeness, or other identity-bound representation is treated as permission for a consent-sensitive use of that identity.",
        "definition": "A failure in which possession of, access to, control over, or technical capability to transform an identifiable person's representation is treated as sufficient authority for an identity-bound synthesis, alteration, reproduction, or portrayal that requires a separate valid consent or authority basis.",
        "recognition": {
            "required_conditions": [
                "A source image, voice, likeness, biometric representation, avatar, or comparable representation remains materially attributable to an identifiable real person.",
                "A requester or system possesses, accesses, controls, or can technically transform that representation.",
                "The proposed synthesis, alteration, reproduction, or portrayal is materially identity-bound or consent-sensitive and requires authority beyond mere possession or capability.",
                "Possession, access, control, upload, availability, or transformation capability is treated as sufficient authority for the identity-bound use.",
                "The required consent or other valid authority for that use is not adequately established before the transformation or synthesis proceeds."
            ]
        },
        "exclusions": [
            "The output is not materially attributable to an identifiable real person.",
            "Valid consent, licence, legal authority, or another adequate authority basis covers the specific identity-bound use and scope.",
            "A synthetic output progressively resembles a real person, but the record does not establish a materially identifiable target or a system state capable of binding the output to that person.",
            "The issue is only false attribution, provenance loss, or reputational harm without an unauthorised identity-bound synthesis or transformation.",
            "The issue is merely that a technical generation capability exists; the capability is not treated as permission for a person-bound use."
        ],
        "examples": [
            "A person's uploaded photograph is treated as sufficient permission to generate an intimate synthetic portrayal of that person.",
            "Access to a real person's voice sample is treated as authority to create a consent-sensitive identity-bound performance that the person did not authorise.",
            "Control of an avatar or biometric likeness file is treated as permission to reproduce the identifiable person in a materially different, authority-sensitive context."
        ],
        "relationships": [
            {
                "type": "distinguish_from",
                "target_id": "VIGIL-FC-000002",
                "note": "Capability-authority conflation can concern any available capability; this class requires an identifiable person-bound representation and a separate authority basis for the identity-bound use."
            },
            {
                "type": "distinguish_from",
                "target_id": "VIGIL-FC-000003",
                "note": "Target and scope transposition carries an existing authority into a changed target or scope; this class also applies when no initial authority beyond possession of the representation exists."
            },
            {
                "type": "distinguish_from",
                "target_id": "VIGIL-FC-000005",
                "note": "Transformation-mediated authority laundering gives transformed content greater instruction or execution authority; this class concerns authority to make an identity-bound transformation or synthesis."
            },
            {
                "type": "can_cooccur_with",
                "target_id": "VIGIL-FC-000038",
                "note": "A separately defined safeguard may also fail to activate, but that control mechanism requires independent evidence."
            }
        ],
        "aliases": []
    })
    write(path, document)

    index = load(INDEX)
    entry = next(item for item in index["families"] if item["family_id"] == "VIGIL-FF-0001")
    assert entry["class_count"] == 10
    entry["class_count"] = 11
    write(INDEX, index)


def classify_fm_0064(families: dict[str, dict[str, Any]], classes: dict[str, dict[str, Any]]) -> None:
    path = FAILURES / "VIGIL-2026-FM-0064.json"
    record = load(path)
    record["record_identity"]["updated"] = REVIEW_DATE
    record["record_identity"]["version"] = "1.1"
    record["taxonomy_classification"] = {
        "taxonomy_version": VERSION,
        "classification_status": "classified",
        "classification_basis": "Access to a real person's source image or likeness and the capability to transform it are treated as sufficient authority for a consent-sensitive identity-bound sexual or intimate synthesis, although valid consent for that use is not established.",
        "classification_confidence": "high",
        "classified_on": REVIEW_DATE,
        "structural_review_flags": [],
        "primary_family": family_ref("VIGIL-FF-0001", families),
        "primary_class": class_ref("VIGIL-FC-000053", classes),
        "classification_review_provenance": classification_provenance(),
    }
    review = interpretive_review(
        record["id"],
        "TAXONOMY-08 source-bound mechanism review, authority-family comparison, trajectory boundary assessment, and optimisation-evidence assessment.",
        "Classified under Identity-Representation Authority Conflation. No secondary trajectory, control-activation, or optimisation class was assigned because the reviewed evidence does not independently establish those mechanisms.",
        [
            "No abusive output was reproduced or directly inspected in this pass.",
            "The sources do not establish that the system knew a depicted person's legal name.",
            "The sources do not establish an initially operative boundary that later eroded, or a specific internal optimisation objective that caused compliance."
        ],
    )
    append_review(record, review)
    write(path, record)


def amend_fm_0065() -> None:
    path = FAILURES / "VIGIL-2026-FM-0065.json"
    record = load(path)
    record["record_identity"].update({
        "title": "Untrustworthy retrieved evidence converted into authoritative synthetic fact",
        "updated": REVIEW_DATE,
        "version": "1.1",
    })
    record["summary"] = "A retrieval, search-assist or synthesis system promotes materially untrustworthy web content into an authoritative-looking factual answer without adequate assessment of source quality, proposition support, independence, corroboration or contradiction. Deliberate source poisoning is one evidenced attack method, not a required condition of the structural failure."
    record["why_it_matters_to_CAM"] = "Retrievability is not evidentiary quality, citation count is not independent corroboration, and a citation does not support a proposition merely because it is topically adjacent. Deliberately planted misinformation, stale or derivative material, circular claims and ordinary low-quality sources can all expose the same evidentiary-warrant failure."
    record["failure_mode_definition"] = "A failure occurs when materially untrustworthy retrieved content is promoted into a factual answer whose authority or confidence exceeds the quality, independence, provenance, corroboration, contradiction state and proposition-level support of the available evidence. Deliberate source poisoning is one possible attack method, not a required structural condition."
    record["failure_threshold"] = "The threshold is met when a system converts source availability, superficial citation coverage or materially unreliable evidence into an affirmative factual claim without proportionate source-quality weighting, proposition-support checking, independence assessment, contradiction detection or corroboration. Synthetic origin alone does not satisfy the threshold."
    record["source_fidelity_analysis"] = {
        "source_established_attack_method": "The cited incident began with a deliberately fabricated story that was placed into the open information environment and then retrieved by AI-assisted search systems.",
        "structural_failure": "The systems presented the fabricated claim as fact and, in the reported DuckDuckGo example, displayed an unrelated legitimate source in a way that made the answer appear better supported than it was.",
        "attack_method_not_required": [
            "incompetent or low-quality reporting",
            "stale or superseded material",
            "copied, derivative or circular claims",
            "unverified tertiary summaries",
            "synthetic content whose reliability properties are not adequately assessed"
        ],
        "classification_boundary": "Provenance asks where the evidence came from. Evidentiary warrant asks what factual confidence that evidence deserves. Synthetic origin is a relevant source property only where it bears on reliability; it is not an automatic finding of low quality."
    }
    classification = record["failure_classification"]
    classification["recurrence_pattern"] = "May recur wherever source availability, apparent citation coverage or repeated derivative claims outrank source quality, proposition support, independence, contradiction and corroboration."
    classification["reproducibility"] = "Can be tested with controlled corpora containing adversarial, stale, derivative, circular, contradictory, synthetic and well-supported source material without treating synthetic origin as inherently unreliable."
    record["triage"]["triage_action_basis"] = "A distinct evidentiary-warrant mechanism is evidenced and requires source-quality coverage review; the attack method is narrower than the structural failure."
    record["triage"]["recommended_next_step"] = "Compare additional native evidence before admitting an epistemic-warrant family; test source-quality, proposition-support, independence, contradiction and corroboration controls without treating synthetic origin as an automatic quality defect."
    record["taxonomy_classification"] = {
        "taxonomy_version": VERSION,
        "classification_status": "unmapped",
        "classification_basis": "The primary mechanism is inflation of factual authority beyond the quality, independence, corroboration, contradiction state and proposition support of retrieved evidence. Provenance can enable that assessment but does not govern evidentiary warrant itself, and no second currently unmapped native Failure Mode cleanly establishes a reusable new-family class structure.",
        "classification_confidence": "high",
        "classified_on": REVIEW_DATE,
        "structural_review_flags": [
            "candidate-epistemic-warrant-family",
            "provenance-warrant-distinction"
        ],
        "classification_review_provenance": classification_provenance(),
    }
    review = interpretive_review(
        record["id"],
        "TAXONOMY-08 source re-review, attack-method/structural-failure separation, provenance-versus-warrant comparison, and cross-unmapped-FM family test.",
        "Broadened the record beyond adversarial intent while preserving the cited poisoning incident. The epistemic-warrant mechanism remains unmapped and is held for multi-record family review.",
        [
            "The poisoning campaign was not independently reproduced.",
            "The single cited incident does not establish prevalence across retrieval systems.",
            "No internal answer-rather-than-abstain, helpfulness, retrieval-density, or citation-coverage optimisation objective is established."
        ],
    )
    append_review(record, review)
    write(path, record)


def repair_and_classify_fm_0070(families: dict[str, dict[str, Any]], classes: dict[str, dict[str, Any]]) -> None:
    path = FAILURES / "VIGIL-2026-FM-0070.json"
    record = load(path)
    record["record_identity"].update({"updated": REVIEW_DATE, "version": "1.1"})
    record["summary"] = "A crafted Microsoft 365 Copilot Enterprise Search link supplies attacker-controlled text through the q parameter; Copilot interprets it as executable search instructions, streams an active image element before later output neutralisation, and routes the resulting request through an allowlisted Bing image endpoint that fetches an attacker-controlled URL. The three source-established weaknesses compose into a prompt-to-egress path."
    record["why_it_matters_to_CAM"] = "The disclosure shows why end-to-end review must preserve transitions among prompt ingress, connected-data retrieval, streaming rendering, output neutralisation, browser policy and trusted server-side fetches. It establishes a composed exploit chain; it does not establish Microsoft's complete internal assurance process or prove that assurance was performed only at component level."
    source = record["source_records"][0]
    source["source_context"] = "Varonis documents three necessary links: the attacker-controlled q parameter is interpreted as executable Copilot instructions; an image element in the streaming response triggers before later code-block wrapping or sanitisation neutralises it; and the browser requests an allowlisted Bing image endpoint whose backend fetches an attacker-controlled URL containing retrieved enterprise data."
    source["relevance_note"] = "Primary technical disclosure for the stage-by-stage prompt-to-egress chain. It supports the component transitions and their dependency, but not claims about the provider's complete assurance methodology."
    source["primary_artefact_access"]["limitations"] = [
        "Security-research demonstration; the disclosure does not expose the complete provider architecture or forensic record.",
        "The disclosure does not establish Microsoft's complete internal assurance process, that each component was independently judged acceptable, or that composition risk was never assessed internally.",
        "Live malicious exploitation outside the reported research demonstration is not established."
    ]
    source["interpretive_reliance"] = "Relied on for the q-parameter interpretation, connected-data search, streaming image activation before later neutralisation, CSP allowlisting, Bing server-side fetch, end-to-end exfiltration demonstration, necessity of all three links, and reported remediation. Provider-internal assurance methodology is not inferred."
    record["source_fidelity_analysis"] = {
        "what_the_source_establishes": [
            "Microsoft 365 Copilot Enterprise Search accepted attacker-controlled text in the q URL parameter and interpreted it not only as search data but as instructions.",
            "The injected instructions caused Copilot to search data available through the victim's enterprise access context and to place retrieved data into an image URL in its response.",
            "During streaming, the browser rendered the image element and issued its request before later code-block wrapping or output sanitisation neutralised the final response.",
            "The browser's Content Security Policy allowed the request to Bing, and Bing's image-search endpoint then performed a server-side fetch to the attacker-controlled URL embedded in its imgurl parameter.",
            "The attacker-controlled server received the request path containing the retrieved data, and Varonis states that each of the three links was necessary to the demonstrated chain.",
            "Microsoft remediated the reported vulnerability under CVE-2026-42824."
        ],
        "exploit_chain": [
            {
                "stage": 1,
                "name": "Parameter-to-Prompt Injection",
                "attacker_control": "A crafted microsoft.com Copilot Enterprise Search URL containing attacker-authored text in the q parameter.",
                "component_behaviour": "Copilot treated the q value as executable natural-language instructions, searched victim-accessible enterprise data, and generated an image URL containing retrieved data.",
                "boundary_transition": "Material presented through a search/query parameter crossed from data-bearing input into instruction-bearing control of the search-and-response workflow."
            },
            {
                "stage": 2,
                "name": "Streaming HTML rendering before neutralisation",
                "attacker_control": "The injected instructions shaped the response so it contained an image element with the retrieved data in its source URL.",
                "component_behaviour": "The browser incrementally rendered the image element and issued the request while the response was still streaming; the later code-block wrapper or sanitisation applied only after the request had left.",
                "boundary_transition": "The output-neutralisation control became effective after the unsafe render-and-request transition it was meant to prevent."
            },
            {
                "stage": 3,
                "name": "Bing server-side fetch through an allowlisted route",
                "attacker_control": "An attacker-controlled destination URL, with retrieved data embedded in its path, was placed inside Bing's imgurl parameter.",
                "component_behaviour": "The browser was permitted to request the allowlisted Bing endpoint; Bing's backend then fetched the attacker-controlled URL, outside the browser's CSP enforcement boundary.",
                "boundary_transition": "Trust granted to the Bing destination became an indirect egress route to a different attacker-controlled target."
            }
        ],
        "end_to_end_result": {
            "victim_action": "The victim clicked one crafted link to a trusted Microsoft domain.",
            "protected_data_accessed": "The demonstration searched data available to the victim through Microsoft 365, including mailbox content; the disclosure identifies email, calendar, SharePoint, OneDrive and other indexed organisational content as potentially accessible.",
            "outbound_path": "Retrieved data was embedded in an image URL, sent first to the allowlisted Bing endpoint and then carried in Bing's server-side request to the attacker-controlled server.",
            "observed_effect": "The attacker server logged the data-bearing request path."
        },
        "what_vigil_infers": [
            "The source-established event can be represented as a compound failure chain with one primary and multiple independently supported secondary taxonomy mechanisms.",
            "The chain supports an end-to-end assurance lesson: component transitions and trust changes must be reviewed together where each stage enables the next.",
            "The disclosure supports a reusable composition hypothesis, but not the stronger claim that provider assurance was actually performed only locally or that each component had been accepted as independently safe."
        ],
        "what_the_source_does_not_establish": [
            "Microsoft's complete internal assurance or threat-modelling process.",
            "That every component state was independently assessed or judged acceptable.",
            "That assurance was performed only locally rather than across the complete chain.",
            "That composition risk was never assessed internally.",
            "The complete provider architecture beyond the disclosed pathway.",
            "Live malicious exploitation outside the reported security-research demonstration."
        ]
    }
    record["failure_mode_definition"] = "A compound failure in which attacker-controlled search material is treated as instruction, a response becomes active before its output-neutralisation control takes effect, and a trusted intermediary extends the outbound path to an attacker-controlled destination. The cited event establishes the interaction of these component weaknesses; it does not by itself establish the provider's internal assurance methodology."
    record["failure_threshold"] = "The threshold requires source-supported component transitions that each enable the next and together create an unauthorised end-to-end path to a protected asset or boundary effect. Mere coexistence of vulnerabilities is insufficient, and a claim that assurance was component-local requires separate evidence about the assurance process."
    classification = record["failure_classification"]
    classification["recurrence_pattern"] = "May recur where prompt ingress, connected-data retrieval, streaming render, output neutralisation and trusted outbound services interact so that each stage enables a boundary violation in the next."
    classification["visibility"] = "The individual transitions are visible in the technical disclosure, but the material prompt-to-egress effect becomes clear only when the ordered chain is reconstructed end to end."
    record["taxonomy_classification"] = {
        "taxonomy_version": VERSION,
        "classification_status": "classified",
        "classification_basis": "Attacker-controlled material in the q search parameter was treated as operative instruction that caused Copilot to search protected enterprise data and construct the response pathway.",
        "classification_confidence": "high",
        "classified_on": REVIEW_DATE,
        "structural_review_flags": ["compound-mechanism", "source-fidelity-repaired"],
        "primary_family": family_ref("VIGIL-FF-0001", families),
        "primary_class": class_ref("VIGIL-FC-000001", classes),
        "secondary_classifications": [
            {
                "family": family_ref("VIGIL-FF-0008", families),
                "class": class_ref("VIGIL-FC-000038", classes),
                "classification_basis": "The disclosed output-neutralisation safeguard was applicable to dangerous HTML, but it did not become effective before streaming render triggered the governed network request.",
                "classification_confidence": "high"
            },
            {
                "family": family_ref("VIGIL-FF-0001", families),
                "class": class_ref("VIGIL-FC-000009", classes),
                "classification_basis": "Trust granted to the allowlisted Bing endpoint effectively propagated through Bing's server-side fetch to a different attacker-controlled destination without preserving the original browser egress boundary.",
                "classification_confidence": "medium"
            }
        ],
        "classification_review_provenance": classification_provenance(),
    }
    review = interpretive_review(
        record["id"],
        "TAXONOMY-08 direct primary-source re-review, stage-by-stage exploit decomposition, source/inference separation, and post-repair compound taxonomy classification.",
        "Repaired unsupported assurance-process claims, added a complete human-readable exploit chain, and classified the source-established event through existing primary and secondary mechanisms. No composition class or family was admitted.",
        [
            "No private provider telemetry, exploit code or complete internal forensic record was available.",
            "The source does not establish Microsoft's complete assurance methodology or live malicious exploitation outside the research demonstration.",
            "Human substantive review and external conformance verification are not established."
        ],
    )
    append_review(record, review)
    write(path, record)


def rebuild_ledger() -> None:
    entries: list[dict[str, Any]] = []
    status_counts: Counter[str] = Counter()
    primary_family_counts: Counter[str] = Counter()
    primary_class_counts: Counter[str] = Counter()
    secondary_family_counts: Counter[str] = Counter()
    secondary_class_counts: Counter[str] = Counter()
    for path in sorted(FAILURES.glob("VIGIL-2026-FM-*.json")):
        record = load(path)
        block = record["taxonomy_classification"]
        family = block.get("primary_family", {})
        klass = block.get("primary_class", {})
        row: dict[str, Any] = {
            "failure_mode_id": record["id"],
            "title": record["record_identity"]["title"],
            "classification_status": block["classification_status"],
            "family_id": family.get("family_id"),
            "class_id": klass.get("class_id"),
            "classification_confidence": block["classification_confidence"],
            "classification_basis": block["classification_basis"],
            "structural_review_flags": block["structural_review_flags"],
        }
        secondaries = []
        for secondary in block.get("secondary_classifications", []):
            secondary_family = secondary["family"]
            secondary_class = secondary["class"]
            secondaries.append({
                "family_id": secondary_family["family_id"],
                "class_id": secondary_class["class_id"],
                "classification_confidence": secondary["classification_confidence"],
                "classification_basis": secondary["classification_basis"],
            })
            secondary_family_counts[secondary_family["family_id"]] += 1
            secondary_class_counts[secondary_class["class_id"]] += 1
        if secondaries:
            row["secondary_classifications"] = secondaries
        entries.append(row)
        status_counts[block["classification_status"]] += 1
        if family.get("family_id"):
            primary_family_counts[family["family_id"]] += 1
        if klass.get("class_id"):
            primary_class_counts[klass["class_id"]] += 1
    write(LEDGER, {
        "schema_version": "1.0",
        "taxonomy_version": VERSION,
        "reviewed_on": REVIEW_DATE,
        "review_package": "TAXONOMY-08",
        "record_count": len(entries),
        "classification_status_counts": dict(sorted(status_counts.items())),
        "primary_family_counts": dict(sorted(primary_family_counts.items())),
        "primary_class_counts": dict(sorted(primary_class_counts.items())),
        "secondary_classification_count": sum(secondary_class_counts.values()),
        "secondary_family_counts": dict(sorted(secondary_family_counts.items())),
        "secondary_class_counts": dict(sorted(secondary_class_counts.items())),
        "entries": entries,
    })


def main() -> None:
    add_identity_representation_class()
    families, classes = catalogue()
    classify_fm_0064(families, classes)
    amend_fm_0065()
    repair_and_classify_fm_0070(families, classes)
    rebuild_ledger()
    print(json.dumps({"reviewed_records": 3, "new_classes": 1, "review_date": REVIEW_DATE}, sort_keys=True))


if __name__ == "__main__":
    main()
