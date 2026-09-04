#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_governance" / "requirements"
SHARD = REQ / "requirements" / "IEEE-7001" / "2021.json"
LEDGER = REQ / "metadata-review.json"
ASSURANCE = REQ / "source-review-assurance.json"
FIDELITY = REQ / "source-fidelity.json"
SCOPE = REQ / "source-scope.json"

DATE = "2026-09-04"
SOURCE_ID = "EXT-338E4D8BD259"
EXTERNAL_ID = "IEEE-7001"
VERSION = "2021"
LOCATOR = "https://standards.ieee.org/ieee/7001/6929/"
FINGERPRINT = "9a7c443a8adc44faf2654c5386e2034ebe871fc56e8d72845911e641abaae707"
DIGEST = "2bf1a21360236fffa7d87a71d544cd47153dae2bbcdf7e48dffe19bda289006b"

FIELDS = (
    "applicable_actor", "governed_object", "timing_or_frequency", "required_artefacts",
    "evidence_expectation", "verification_method", "applicability_conditions",
    "exceptions_or_qualifications",
)

ESTABLISHED_IDS = {
    "EXTREQ-05800E1D5E774996","EXTREQ-0644CA6F6AA495DE","EXTREQ-0C5664070D141929",
    "EXTREQ-0FC8A0CA89BD2FB2","EXTREQ-10591B52C510BE45","EXTREQ-13E71F1E78D8FA2D",
    "EXTREQ-1909D633DD153925","EXTREQ-1F0BCB344AEA2690","EXTREQ-3F3FE69853DA2FE6",
    "EXTREQ-4A3A98EDC233BFD4","EXTREQ-4DCFB5BB26E9B218","EXTREQ-70BB4ECD22E7DC60",
    "EXTREQ-7417A4E295C50432","EXTREQ-7675F4F8753B09FB","EXTREQ-770BD65BD9B3CA90",
    "EXTREQ-7B0BD423DE335511","EXTREQ-80B95118891500CC","EXTREQ-86020155B4C4312E",
    "EXTREQ-8D3D5329349F21FE","EXTREQ-8DCC70AF4AB7136E","EXTREQ-8F7D774F70387DA7",
    "EXTREQ-9EA13A62F93E8434","EXTREQ-A85A860E9017EA52","EXTREQ-B283FB077323F944",
    "EXTREQ-CB76B4C437492E66","EXTREQ-D0403321A5F45CC7","EXTREQ-DE76405345E5C624",
    "EXTREQ-DF16873D107C059C","EXTREQ-EAFAB33E1DFA6E7B","EXTREQ-F34E10E503F4CEC8",
    "EXTREQ-F5BFD7C2FB8700EE","EXTREQ-F8F11DA0D9D14DD0","EXTREQ-F9D5AD96B52ECC93",
}

def dump(path: Path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def m(**kwargs):
    return kwargs

SOURCE_QUAL = [
    "IEEE 7001-2021 is a voluntary consensus standard; applicable laws and regulations remain controlling.",
]
LEVEL_SELECTION = "Applies where the adopter selects the identified stakeholder transparency level for the autonomous system."

META = {
"7001-user-understanding": m(
    required_artefacts=["User-facing transparency information explaining system activity and operational basis."],
    evidence_expectation=["Information sufficient for the intended user class to understand what the system is doing and why/how it is doing it."],
    verification_method=["Assess whether the transparency presented is understandable and appropriate to the relevant user class."],
    applicability_conditions=["Applies to users of autonomous systems, with the level of detail adapted to non-expert, domain-expert or superuser needs."],
),
"7001-user-scenarios-and-principles": m(
    required_artefacts=["Accessible user documentation with example scenarios, degraded-mode expectations and general operating principles."],
    evidence_expectation=["Documentation covers anticipated system behaviour, degraded modes and general operating principles; for machine-learning systems it also identifies learning sources and possible bias sources."],
    verification_method=["Inspect the user documentation for the required scenarios, degraded-mode information and operating-principle explanation."],
    applicability_conditions=["Table 1 user transparency Level 1; user levels are non-progressive."],
),
"7001-user-role-documentation": m(
    required_artefacts=["Role-appropriate user documentation covering safe operation and supervision, and for superusers fault diagnosis, repair, maintenance, upgrade and decommissioning."],
    evidence_expectation=["Documentation appropriate to domain-expert and superuser responsibilities."],
    verification_method=["Review documentation against the responsibilities of the intended expert-user class."],
    applicability_conditions=["Applies to domain-expert users and superusers at Table 1 Level 1."],
),
"7001-interactive-user-training": m(
    required_artefacts=["Interactive presentation, video or simulation for rehearsing relevant system interactions."],
    evidence_expectation=["Interactive material enables users to rehearse system interactions in specific relevant situations."],
    verification_method=["Demonstrate that the training material permits rehearsal of relevant interactions."],
    applicability_conditions=["Table 1 user transparency Level 2; user levels are non-progressive."],
),
"7001-expert-lifecycle-training": m(
    required_artefacts=["Interactive training material for safe operation and supervision; for superusers, additional training for fault diagnosis, repair, maintenance, upgrade and decommissioning."],
    evidence_expectation=["Training content appropriate to domain-expert and superuser lifecycle responsibilities."],
    verification_method=["Review or demonstrate the interactive training coverage for the intended expert-user class."],
    applicability_conditions=["Applies to domain-expert users and superusers at Table 1 Level 2."],
),
"7001-recent-action-explanation": m(
    timing_or_frequency=["Provide the explanation immediately when initiated by the user for the system's most recent activity."],
    required_artefacts=["User-initiated explanation functionality."],
    evidence_expectation=["A brief, immediate and commonly understandable explanation of the system's most recent activity."],
    verification_method=["Trigger the explanation function after system activity and assess immediacy and understandability."],
    applicability_conditions=["Applies to non-expert users at Table 1 Level 3."],
),
"7001-domain-decision-explanation": m(
    timing_or_frequency=["Provide explanations on request for recent system decisions."],
    required_artefacts=["Explanation-request functionality and documentation describing how domain experts request and interpret explanations."],
    evidence_expectation=["Domain-appropriate explanations and supporting request/interpretation documentation."],
    verification_method=["Request explanations for recent decisions and review the supporting documentation."],
    applicability_conditions=["Applies to systems designed for domain-expert users at Table 1 Level 3."],
    exceptions_or_qualifications=["Documentation should cover natural-language-processing subsystems where present."],
),
"7001-counterfactual-explanation": m(
    timing_or_frequency=["Provide a brief and immediate response when the user initiates a prospective or counterfactual query."],
    required_artefacts=["User-initiated prospective or counterfactual explanation functionality."],
    evidence_expectation=["The system can explain what it would do in a stated situation within its scope of work."],
    verification_method=["Exercise applicable hypothetical scenarios and assess whether the system returns an understandable prospective explanation."],
    applicability_conditions=["Table 1 user transparency Level 4; applies where counterfactual exploration is relevant to the system's scope."],
    exceptions_or_qualifications=["Non-expert users need not undergo special training, although familiarity with user documentation is required."],
),
"7001-continuous-adaptive-explanation": m(
    timing_or_frequency=["Provide explanations continuously during operation and adapt them to user information needs and context."],
    required_artefacts=["Continuous explanation interface and, where non-sensitive, access to relevant log files and training data."],
    evidence_expectation=["Explanations adapt to the user's context and interaction history."],
    verification_method=["Observe explanations over operation and assess adaptation to user needs and context."],
    applicability_conditions=["Table 1 user transparency Level 5; user levels are non-progressive."],
    exceptions_or_qualifications=["Access to logs and training data excludes sensitive information such as personal data."],
),
"7001-explanation-access-and-detail": m(
    timing_or_frequency=["Make relevant explanations available without additional effort to non-expert users and additional detail available on demand to expert users."],
    required_artefacts=["User-facing explanation interface with on-demand deeper detail for domain experts and superusers."],
    evidence_expectation=["Non-experts can access relevant explanations with low effort and experts can interactively obtain additional detail."],
    verification_method=["Test explanation access separately for non-expert and expert user roles."],
    applicability_conditions=["Table 1 user transparency Level 5."],
),
"7001-autonomous-identity-disclosure": m(
    timing_or_frequency=["Identify the system as autonomous at the start of an interaction where applicable."],
    required_artefacts=["Autonomous-system identification such as a message, watermark, insignia or equivalent design cue."],
    evidence_expectation=["Users or bystanders can clearly identify the system as autonomous."],
    verification_method=["Inspect representative interactions or outputs for clear autonomous-system identification."],
    applicability_conditions=["Table 2 public/bystander transparency Level 1; public/bystander levels are non-progressive except Level 3 depends on Level 2."],
),
"7001-sensor-data-warning": m(
    required_artefacts=["Public or environmental warnings about relevant external sensor-data collection or recording."],
    evidence_expectation=["Warnings identify that relevant sensor data concerning public or bystanders is being collected or recorded."],
    verification_method=["Inspect the system and deployment environment for appropriate warnings or notifications."],
    applicability_conditions=["Applies where external sensor data related to the general public or bystanders is collected or recorded at Table 2 Level 2."],
),
"7001-public-sensor-documentation": m(
    required_artefacts=["Publicly available documentation or identification graphics describing sensor-data types and how they are used."],
    evidence_expectation=["Public information identifies the types of collected data and their use."],
    verification_method=["Review the publicly available sensor-data documentation or linked information."],
    applicability_conditions=["Table 2 public/bystander transparency Level 2."],
    exceptions_or_qualifications=["Level 2 concerns information about data types rather than disclosure of sensor-data content."],
),
"7001-public-purpose-operator-contact": m(
    required_artefacts=["Public documentation describing system purpose, nominal operator and responsible contact details."],
    evidence_expectation=["The Level 2 documentation additionally identifies intended purpose, nominal operator and a responsible owner, supervisor or other authority."],
    verification_method=["Review the public documentation for the additional Level 3 information."],
    applicability_conditions=["Table 2 Level 3; all Level 2 requirements shall also be met."],
),
"7001-data-governance-policy-requests": m(
    timing_or_frequency=["Accept and respond to data-governance requests when they are made."],
    required_artefacts=["Clear data-governance policy and a means for submitting data-governance requests."],
    evidence_expectation=["Evidence that data-governance enquiries can be received, processed and answered."],
    verification_method=["Review the policy and exercise or inspect the request-handling process."],
    applicability_conditions=["Table 2 public/bystander transparency Level 4; Level 5 is defined as the same transparency as Level 4."],
),
"7001-validation-specification": m(
    required_artefacts=["System specification, identification of validated properties, and description of the validation process and standards applied."],
    evidence_expectation=["Documentation identifies system decisions, validated properties, validation process and applied standards."],
    verification_method=["Review the submitted validation documentation against Table 3 Level 1."],
    applicability_conditions=["Table 3 validation/certification transparency Level 1; this stakeholder scale is progressive."],
    exceptions_or_qualifications=["The standard requires evidence of validation undertaken, if any; it does not itself require that the system has been validated."],
),
"7001-detailed-validation-process": m(
    required_artefacts=["System specification and detailed validation-process documentation, including ongoing validation and system-level testing where relevant."],
    evidence_expectation=["Evidence that internal validation has occurred and that decision implementation and relevant testing are described."],
    verification_method=["Review the detailed validation process, internal validation evidence and relevant system-level tests."],
    applicability_conditions=["Table 3 Level 2; Level 1 shall also be met because validation/certification levels are progressive."],
),
"7001-high-level-design-model": m(
    required_artefacts=["High-level system design or preferably executable model; a simulation may be used."],
    evidence_expectation=["A design or model sufficient to expose the high-level system structure to validators."],
    verification_method=["Inspect the supplied design/model and, where executable, exercise it as part of validation review."],
    applicability_conditions=["Table 3 Level 3; lower validation/certification levels shall also be met."],
),
"7001-validation-issues-and-conditions": m(
    required_artefacts=["Account of important issues uncovered and resolved and any analysis of anticipated or actual operating conditions."],
    evidence_expectation=["Development/deployment issues and operating-condition analyses are disclosed, including affected communities or environments where analyzed."],
    verification_method=["Review issue history and operating-condition analysis; confirm explicit disclosure where analyses were not performed."],
    applicability_conditions=["Table 3 Level 3; lower validation/certification levels shall also be met."],
    exceptions_or_qualifications=["If operating-condition analysis has not taken place, this shall be stated."],
),
"7001-statistical-model-bias-validation": m(
    required_artefacts=["Documentation of statistical models and their validation, including bias, unfairness or inequity assessment and mitigation."],
    evidence_expectation=["Validation outcomes and assessment of unwanted bias, unfairness or inequity are documented."],
    verification_method=["Review statistical-model validation and bias/fairness assessment outcomes."],
    applicability_conditions=["Applies at Table 3 Level 3 where statistical models are used; lower validation/certification levels shall also be met."],
    exceptions_or_qualifications=["If no statistical models are used or no model assessment was made, that fact shall be stated as applicable."],
),
"7001-reproducible-final-validation": m(
    required_artefacts=["All material necessary to reproduce final-system validation, including relevant tools, working system versions, training data and operational validation data where applicable."],
    evidence_expectation=["A validator can reproduce the final validation process using the supplied material."],
    verification_method=["Attempt or assess reproducibility of the final validation process using the supplied assets."],
    applicability_conditions=["Table 3 Level 4; lower validation/certification levels shall also be met."],
    exceptions_or_qualifications=["Data-protection agreements or user notice may be necessary when personal data is used or shared for validation."],
),
"7001-full-system-validation-assets": m(
    required_artefacts=["Full source code, relevant statistical models, training data with composition/provenance descriptions, validation tools and working system versions."],
    evidence_expectation=["The complete source and validation assets required by Table 3 Level 5 are available to the validation/certification agency."],
    verification_method=["Review the completeness of the supplied source, model, data and validation assets and assess reproducibility."],
    applicability_conditions=["Table 3 Level 5; all lower validation/certification levels shall also be met."],
),
"7001-incident-traceability": m(
    timing_or_frequency=["Retain sufficient trace information over the period leading to an incident."],
    required_artefacts=["Secure time-stamped event data sufficient to trace relevant internal system processes."],
    evidence_expectation=["Investigators can reconstruct the internal processes that led to an incident over the relevant time period."],
    verification_method=["Use recorded event data with system documentation to trace the sequence leading to an incident."],
    applicability_conditions=["Applies to incident-investigator transparency under Clause 5.2.2."],
),
"7001-independent-physical-incident-recording": m(
    timing_or_frequency=["Record relevant external context around the time of an incident."],
    required_artefacts=["Independent audiovisual recording device for a physical autonomous system."],
    evidence_expectation=["Unmodified, correctly time-stamped and non-modifiable external-context data relevant to the system purpose and domain."],
    verification_method=["Inspect recorder independence, placement, time-stamping, data integrity and playback capability."],
    applicability_conditions=["Recommended practice for physical autonomous systems at Table 4 Level 1; incident-investigator levels are progressive."],
    exceptions_or_qualifications=["The recorder should be independent of the system sensing/control systems and have an independent power source except for charging."],
),
"7001-software-incident-input-output-log": m(
    timing_or_frequency=["Log system inputs and outputs during operation so incident-relevant data is available."],
    required_artefacts=["Event-data-recorder module for a software-only autonomous system."],
    evidence_expectation=["Recorded system inputs and outputs."],
    verification_method=["Inspect the event recorder and verify that relevant inputs and outputs are logged."],
    applicability_conditions=["Mandatory Table 4 Level 1 requirement for software-only autonomous systems; incident-investigator levels are progressive."],
),
"7001-edr-key-input-output-log": m(
    timing_or_frequency=["Continuously retain the most recent relevant time window of time-stamped data for physical systems."],
    required_artefacts=["Event data recorder capable of securely recording time-stamped key system inputs and outputs."],
    evidence_expectation=["Secure time-stamped key input/output records, including relevant sensor data and actuator demands for physical systems."],
    verification_method=["Inspect EDR logging, time-stamping and secure retention; for physical systems assess survivability against foreseeable incident environments."],
    applicability_conditions=["Table 4 Level 2; Level 1 shall also be met because incident-investigator levels are progressive."],
),
"7001-standardized-edr-decisions": m(
    timing_or_frequency=["Continuously retain the most recent relevant time window and continue recording after an incident where a physical system remains functional."],
    required_artefacts=["Standard or open-standard EDR, where feasible standards exist, recording key inputs, outputs and high-level decisions in a secure standard format."],
    evidence_expectation=["Secure standard-format event records include key inputs, outputs and high-level decisions."],
    verification_method=["Review EDR conformance to the selected standard/open standard and inspect recorded decision data."],
    applicability_conditions=["Table 4 Level 3; Levels 1 and 2 shall also be met."],
    exceptions_or_qualifications=["Use of a standard or open standard applies where feasible standards exist."],
),
"7001-edr-decision-reasons": m(
    timing_or_frequency=["Record the decision basis when high-level decisions occur; for neural-network systems, connection-state snapshots are recommended periodically."],
    required_artefacts=["EDR records identifying the reason, decision-making logic or mechanism behind high-level decisions."],
    evidence_expectation=["Investigators can determine how and why high-level decisions were made."],
    verification_method=["Reconstruct decision logic from EDR traces together with code or model information."],
    applicability_conditions=["Table 4 Level 4; Levels 1–3 shall also be met."],
),
"7001-investigator-audit-tools": m(
    required_artefacts=["Tools for reviewing and auditing Level 4 event data."],
    evidence_expectation=["Investigators can review and audit recorded event data, including decision sequences."],
    verification_method=["Exercise the supplied review/audit tools against representative recorded event data."],
    applicability_conditions=["Table 4 Level 5; Levels 1–4 shall also be met."],
),
"7001-quality-assurance-evidence": m(
    required_artefacts=["Documentary evidence of transparent reporting of system quality-assurance activities."],
    evidence_expectation=["Quality-assurance reporting evidence is available for expert advisors."],
    verification_method=["Review quality-assurance documentary evidence."],
    applicability_conditions=["Table 5 expert-advisor transparency Level 1; this stakeholder scale is generally non-progressive."],
    exceptions_or_qualifications=["Certification to ISO 9001:2015 or equivalent is an example of evidence, not the only permitted evidence."],
),
"7001-ethical-risk-assessment-reports": m(
    required_artefacts=["Ethical-risk assessment and control/mitigation reports."],
    evidence_expectation=["Reports identify ethical risks, likely impacts and mitigation steps."],
    verification_method=["Review the ethical-risk assessment process and resulting risk/mitigation reports."],
    applicability_conditions=["Table 5 expert-advisor transparency Level 2."],
    exceptions_or_qualifications=["Published standards such as BS 8611:2016 or IEEE 7000-2021 are examples of assessment approaches; equivalent approaches may be used."],
),
"7001-ethical-governance-framework": m(
    timing_or_frequency=["Apply and document the ethical-governance framework through the product life cycle."],
    required_artefacts=["Documented ethical-governance framework."],
    evidence_expectation=["Evidence that the system developer/manufacturer applies an ethical-governance framework within the product lifecycle."],
    verification_method=["Review the documented framework and evidence of its lifecycle application."],
    applicability_conditions=["Table 5 Level 3; despite the stakeholder scale being described as non-progressive, the Level 3 definition explicitly includes Level 2."],
),
"7001-process-audit-trail": m(
    timing_or_frequency=["Maintain the audit trail across the relevant quality, risk-control and ethical-governance processes."],
    required_artefacts=["Full chronological audit trail for quality, risk assessment/control/mitigation and ethical-governance processes."],
    evidence_expectation=["Documentary evidence supports reconstruction of the relevant organizational processes."],
    verification_method=["Audit the process records for completeness and traceability across Levels 1–3 process areas."],
    applicability_conditions=["Table 5 Level 4; Level 5 is defined as the same transparency as Level 4."],
),
}

records = json.loads(SHARD.read_text(encoding="utf-8"))
assert len(records) == 33
assert {r["requirement_id"] for r in records} == ESTABLISHED_IDS
by_key = {r["identity_key"]: r for r in records}
assert set(by_key) == set(META), (set(by_key)-set(META), set(META)-set(by_key))

for r in records:
    spec = META[r["identity_key"]]
    r["source_review_date"] = DATE
    # Preserve established actor/object values: direct source review supports them.
    r["timing_or_frequency"] = list(spec.get("timing_or_frequency", []))
    r["required_artefacts"] = list(spec.get("required_artefacts", []))
    r["evidence_expectation"] = list(spec.get("evidence_expectation", []))
    r["verification_method"] = list(spec.get("verification_method", []))
    r["applicability_conditions"] = list(spec.get("applicability_conditions", [LEVEL_SELECTION]))
    r["exceptions_or_qualifications"] = list(spec.get("exceptions_or_qualifications", [])) + SOURCE_QUAL
    p = r["interpretation_provenance"]
    p["basis"] = "licensed-primary-text"
    p["source_analysis_method"] = "Direct clause-level fidelity review of IEEE Std 7001-2021 licensed primary text, including Clause 5 stakeholder rules and Tables 1–5; analytical paraphrase only."
    p["source_locator"] = LOCATOR
    p["source_metadata_fingerprint"] = FINGERPRINT
    p["reviewed_source_digest"] = DIGEST
    p["reviewed_source_digest_algorithm"] = "sha256"
    p["reviewed_source_digest_status"] = "recorded"
    r["review_limitations"] = [
        "Transparency levels apply under the source's stakeholder-specific progressive or non-progressive rules; a higher number does not universally mean a duty for every system.",
        "Repeated highest levels that add no new transparency requirement are not duplicated as separate analytical records.",
        "Licensed IEEE text is not stored in VIGIL.",
    ]
    r["assurance_provenance"] = []

dump(SHARD, records)

ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
ledger["updated_at"] = DATE
review_by = {e["requirement_id"]: e for e in ledger["entries"]}
for r in records:
    review_by[r["requirement_id"]] = {
        "requirement_id": r["requirement_id"],
        "reviewed_at": DATE,
        "review_basis": "licensed-primary-text",
        "review_notes": [
            "Direct review of the lawfully accessed IEEE 7001-2021 primary text; all 33 established identities preserved and field-level source silence recorded without inference."
        ],
        "field_status": {
            f: ("populated-reviewed" if r[f] else "not-specified-by-source")
            for f in FIELDS
        },
    }
ledger["entries"] = sorted(review_by.values(), key=lambda e: e["requirement_id"])
dump(LEDGER, ledger)

assurance = json.loads(ASSURANCE.read_text(encoding="utf-8"))
assurance["updated_at"] = DATE
review_entry = {
    "vigil_source_id": SOURCE_ID,
    "external_source_id": EXTERNAL_ID,
    "source_version": VERSION,
    "source_metadata_fingerprint": FINGERPRINT,
    "reviewed_source_digest": {
        "algorithm": "sha256",
        "digest": DIGEST,
        "recorded_at": DATE,
        "artefact_role": "reviewed-primary-source",
        "access_basis": "licensed-primary",
        "evidence_ref": LOCATOR,
    },
    "assurance_provenance": [],
}
for i,e in enumerate(assurance["source_reviews"]):
    if e["external_source_id"] == EXTERNAL_ID and e["source_version"] == VERSION:
        assurance["source_reviews"][i] = review_entry
        break
else:
    assurance["source_reviews"].append(review_entry)
dump(ASSURANCE, assurance)

fidelity = json.loads(FIDELITY.read_text(encoding="utf-8"))
fidelity["reviewed_at"] = DATE
fentry = {
    "vigil_source_id": SOURCE_ID,
    "external_source_id": EXTERNAL_ID,
    "source_version": VERSION,
    "fidelity_status": "assured",
    "effective_extraction_status": "complete",
    "assessment_basis": "Direct review against the complete lawfully accessed IEEE 7001-2021 licensed primary PDF confirmed that the 33 established analytical records provide bounded coverage of the operative Clause 5 stakeholder transparency requirements. All established EXTREQ identities and source postures were preserved. The review also confirmed the stakeholder-specific progressive/non-progressive level rules and that repeated highest levels adding no new requirement should not be duplicated. Field-level metadata has been reconciled to source-explicit artefacts, evidence, verification cues, timing, applicability and qualifications without reproducing licensed text.",
    "known_fidelity_gaps": [],
    "audited_requirement_ids": sorted(ESTABLISHED_IDS),
    "next_action": "Retain the 33 reviewed identities and repeat fidelity review on material revision of IEEE 7001.",
}
for i,e in enumerate(fidelity["entries"]):
    if e["external_source_id"] == EXTERNAL_ID and e["source_version"] == VERSION:
        fidelity["entries"][i] = fentry
        break
else:
    fidelity["entries"].append(fentry)
dump(FIDELITY, fidelity)

scope = json.loads(SCOPE.read_text(encoding="utf-8"))
for e in scope["entries"]:
    if e["external_source_id"] == EXTERNAL_ID and e["source_version"] == VERSION:
        e["extraction_status"] = "complete"
        e["extraction_scope_notes"] = "Direct licensed-primary fidelity review confirmed bounded coverage of the operative Clause 5 stakeholder transparency requirements in 33 stable analytical records, including the source's stakeholder-specific progressive/non-progressive level rules."
        e["known_unreviewed_sections"] = []
        e["next_action"] = "Monitor for material source revision."
        e["maintainer_action_required"] = False
        e["maintainer_action"] = None
        break
else:
    raise AssertionError("IEEE-7001 scope entry missing")
dump(SCOPE, scope)

print("IEEE 7001 fidelity enrichment valid: 33 established IDs preserved; no new requirement identities added.")
print("Digest", DIGEST)
