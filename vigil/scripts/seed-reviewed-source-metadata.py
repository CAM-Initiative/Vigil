#!/usr/bin/env python3
"""Apply and seed the directly reviewed non-EU metadata slices.

The decisions in this script are intentionally limited to NIST AI RMF 1.0,
CycloneDX 1.7, NIST AI 600-1, IMDA Agentic AI MGF 1.5 and NIST SP 800-218A.
They were made from the cited public primary sources on 2026-08-26, with the
NIST AI 600-1 constituent-fidelity tranche completed on 2026-08-28. This is
not a generic empty-field classifier.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from external_requirements_io import (
    REQUIREMENTS_ROOT,
    load_requirements_document,
    write_requirements_document,
)

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_requirements"
LEDGER = REQ / "metadata-review.json"
BACKLOG = REQ / "reextraction-backlog.json"

FIELDS = (
    "applicable_actor",
    "governed_object",
    "timing_or_frequency",
    "required_artefacts",
    "evidence_expectation",
    "verification_method",
    "applicability_conditions",
    "exceptions_or_qualifications",
)

NIST_RMF = "EXT-6442C7954667"
CYCLONEDX = "EXT-13FB945E8A06"
NIST_GAI = "EXT-DE4FDB52698E"
IMDA_AGENTIC = "EXT-3CCBC407EAC8"
NIST_218A = "EXT-65F7658B8B04"
CYCLONEDX_MODALITY_DEFECT = "EXTREQ-FA1B882FFAD54D93"

IMDA_SCOPE = (
    "The framework applies to organizations looking to deploy agentic AI, "
    "whether they develop agents in-house or use third-party agentic solutions."
)

# Direct review of IMDA MGF 1.5 found eight semantically over-compressed 2.1
# records and twelve records whose section-level locator masks the actual
# subsection proposition. Affected fields stay unresolved; the canonical
# records are not silently repaired in this metadata pass.
IMDA_BACKLOG = {
    "EXTREQ-14B4DA1E7646754E": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse"],
        ["governed_object", "timing_or_frequency", "required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary adds number, value and duration limits that are not the cited section's general agent-limits proposition and combines them with scope-of-impact controls.",
    ),
    "EXTREQ-3B91F9DF01838676": (
        ["constituent-semantics-loss", "condition-loss"],
        ["timing_or_frequency", "applicability_conditions", "exceptions_or_qualifications"],
        "The source requires evaluation of whether residual risk is tolerable and can be accepted; the summary adds further-treatment and avoidance alternatives not stated in that proposition.",
    ),
    "EXTREQ-3E386D665B98BDEA": (
        ["compound-normative-propositions", "constituent-semantics-loss"],
        ["governed_object", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary recombines distinct impact factors for sensitive data and external-system access and adds tool criticality without preserving the source-defined factor boundaries.",
    ),
    "EXTREQ-7B1019B56EF6F868": (
        ["constituent-semantics-loss", "condition-loss"],
        ["governed_object", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary adds consequences for affected parties while compressing the source's distinct domain, error-tolerance and business-process criticality considerations.",
    ),
    "EXTREQ-5513796D63BEB71E": (
        ["constituent-semantics-loss", "output-or-artefact-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The source calls for centrally issuing and tracking agent identities and attendant permissions; the summary adds owners, purposes and operating status.",
    ),
    "EXTREQ-844AFD2FC9FB59FD": (
        ["compound-normative-propositions", "constituent-semantics-loss", "output-or-artefact-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "applicability_conditions", "exceptions_or_qualifications"],
        "The source requires recording the capacities in which an agent acts for auditability; the summary adds distinguishability in interactions and does not preserve the record's content boundary.",
    ),
    "EXTREQ-F3EBD6E34FEFE18E": (
        ["constituent-semantics-loss", "output-or-artefact-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "applicability_conditions", "exceptions_or_qualifications"],
        "The source requires delegations of authority to be clearly recorded; the summary adds sub-delegation chains and a separate attribution outcome.",
    ),
    "EXTREQ-F477502DEE0603FE": (
        ["actor-loss", "condition-loss", "constituent-semantics-loss"],
        ["applicable_actor", "governed_object", "applicability_conditions", "exceptions_or_qualifications"],
        "The source limits what an authorising human user may set for an agent; the summary changes the actor and extends the rule to organisational authority generally.",
    ),
    "EXTREQ-2DC8F2B745E464D5": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse", "condition-loss"],
        ["required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The section-level summary combines responsibility allocation with several separate external-party transparency and information-sharing practices from subsection 2.2.1.",
    ),
    "EXTREQ-82D791A7B54305B0": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse"],
        ["applicability_conditions", "exceptions_or_qualifications"],
        "The section-level locator compresses multiple source-defined internal roles and lifecycle responsibilities in subsection 2.2.1.",
    ),
    "EXTREQ-90553A3F265B9C63": (
        ["constituent-semantics-loss", "locator-too-coarse", "output-or-artefact-loss", "condition-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The source addresses security arrangements, performance guarantees and data protection in terms or contracts; the summary substitutes access and response obligations.",
    ),
    "EXTREQ-DB1BC74DC84D4718": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse", "timing-loss"],
        ["timing_or_frequency", "required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary compresses subsection 2.2.2's separate approval-boundary, approval-quality, oversight-audit, training and automated-monitoring propositions.",
    ),
    "EXTREQ-1F35B4A263EF7055": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse", "output-or-artefact-loss"],
        ["required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary omits subsection 2.3.3's express logging, reporting, failsafe, intervention, debugging and periodic-audit outputs while using a whole-section locator.",
    ),
    "EXTREQ-99712BA8308E32FF": (
        ["locator-too-coarse"], [],
        "The proposition is supported by subsection 2.3.2, but the current locator identifies only section 2.3.",
    ),
    "EXTREQ-DCFA4FF526B6439C": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse"],
        ["governed_object", "applicability_conditions", "exceptions_or_qualifications"],
        "The generic whole-section summary does not preserve subsection 2.3.1's distinct control-selection propositions for agent components, security surfaces and multi-agent interactions.",
    ),
    "EXTREQ-DFAE10B7FA4CAEEF": (
        ["timing-loss", "constituent-semantics-loss", "locator-too-coarse"],
        ["timing_or_frequency", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The source separately requires continuous post-deployment testing and change reviews triggered by technical, environmental, performance or regulatory changes; the summary conflates those propositions.",
    ),
    "EXTREQ-FE078DDB1FABA3AF": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse", "condition-loss"],
        ["governed_object", "timing_or_frequency", "required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary combines distinct runtime intervention, human-approval, termination and fallback practices and adds revocation without a precise subsection locator.",
    ),
    "EXTREQ-24F5ABCB4CAFC499": (
        ["compound-normative-propositions", "constituent-semantics-loss", "locator-too-coarse", "condition-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary combines information for interacting users and training for integrating users, which have different source-defined applicability in subsections 2.4.2 and 2.4.3.",
    ),
    "EXTREQ-4253F163EB11C1C9": (
        ["constituent-semantics-loss", "locator-too-coarse", "condition-loss"],
        ["governed_object", "applicability_conditions", "exceptions_or_qualifications"],
        "The source requires point-of-interaction disclosure to users who interact with agents; the summary adds people materially affected by a system.",
    ),
    "EXTREQ-47EE577CC52EF131": (
        ["constituent-semantics-loss", "locator-too-coarse", "output-or-artefact-loss", "condition-loss"],
        ["required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The source calls for responsible human contact points for malfunction or dissatisfaction; the summary adds help, reporting and challenge channels and the metadata invents a required report.",
    ),
}

NIST_218A_ACTOR = (
    "Organization applying NIST SP 800-218A as an AI model producer, AI system "
    "producer, or AI system acquirer, as relevant to its role"
)
NIST_218A_SCOPE = (
    "Applies to AI model development, including data sourcing, design, training, "
    "fine-tuning, evaluation, and incorporation or integration into other software."
)
NIST_218A_GLOBAL_QUALIFICATIONS = [
    "The Profile supplements NIST SP 800-218 SSDF 1.1 and is not intended for standalone use.",
    "Organizations are expected to adapt, customize, and omit items as necessary through a risk-based approach because not all practices and tasks apply to every use case.",
    "Deployment and operation of AI systems and most of the data governance and management life cycle are outside the Profile's scope.",
]

NIST_218A_BACKLOG = {
    "EXTREQ-0D340334BF013176": (
        ["constituent-semantics-loss", "condition-loss"],
        ["required_artefacts", "evidence_expectation", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary truncates the source's statement that model-development security requirements may arise from laws, regulations, contracts, and standards.",
        "constituent-enrichment-preserve-identity",
    ),
    "EXTREQ-494632407D193E4D": (
        ["constituent-semantics-loss"],
        ["governed_object", "verification_method", "exceptions_or_qualifications"],
        "The summary truncates the source-defined vulnerability and threat examples used to bound the risk-modeling proposition.",
        "constituent-enrichment-preserve-identity",
    ),
    "EXTREQ-597D56E05968BAA7": (
        ["constituent-semantics-loss", "condition-loss", "output-or-artefact-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary truncates the access-restriction condition for models trained on sensitive data and the relationship to existing access rights for that data.",
        "constituent-enrichment-preserve-identity",
    ),
    "EXTREQ-924ED328626DF5C8": (
        ["constituent-semantics-loss"],
        ["verification_method", "exceptions_or_qualifications"],
        "The summary truncates the source's non-exhaustive methods for analyzing and altering model-development data.",
        "constituent-enrichment-preserve-identity",
    ),
    "EXTREQ-B7D6A74ED85415CF": (
        ["constituent-semantics-loss", "exception-loss"],
        ["governed_object", "applicability_conditions", "exceptions_or_qualifications"],
        "The summary truncates the qualification that protected AI model elements need not share the same storage location or mechanism.",
        "constituent-enrichment-preserve-identity",
    ),
    "EXTREQ-CFC9864F6289630A": (
        ["compound-normative-propositions", "modality-loss", "locator-too-coarse", "output-or-artefact-loss"],
        ["governed_object", "required_artefacts", "evidence_expectation", "verification_method", "applicability_conditions", "exceptions_or_qualifications"],
        "The record combines PW.7.1 R1 (include AI code in review policies) with the distinct PW.7.1 C1 consideration (consider scanning model code) and represents both under the R1 recommended-practice modality.",
        "semantic-decomposition-with-identity-migration",
    ),
}

NIST_218A_TIMING = {
    "PO.2.1 R1": ["Throughout the software development life cycle."],
    "PO.3.2 R2": ["At a frequency commensurate with risk."],
    "PO.4.1 R1": ["Throughout the AI development life cycle."],
    "PO.5.1 R4": ["Continuously during model development."],
    "PO.5.1 R6": ["Continuously in each development environment."],
    "PO.5.3 R1": ["Continuously in development environments hosting AI models or related resources."],
    "PO.5.3 R2": ["Continuously as part of monitoring and analysis."],
    "PS.1.2 R1": ["Continuously during model development."],
    "PS.1.3 R2": ["Continuously during model development."],
    "PS.2.1 R2": ["For AI model changes."],
    "PW.1.1 C1": ["Periodically after release for future model versions and derivatives."],
    "PW.3.1 R1": ["Before using the data."],
    "PW.4.4 R1": ["Before using an acquired AI model or component."],
    "PW.4.4 R2": ["Before using an acquired AI model or component."],
    "PW.8.2 R2": ["When an AI model is retrained or new data sources are added."],
    "RV.1.2 R1": ["Frequently on an ongoing basis."],
    "RV.1.2 R2": ["On an ongoing basis."],
    "RV.1.2 R3": ["Periodically."],
}

NIST_218A_ARTEFACTS = {
    "PO.1.2 R1": ["Organizational policies supporting current AI model development security requirements."],
    "PO.1.2 C1": ["Reused or expanded organizational data-classification policy and processes."],
    "PO.3.1 R1": ["Plan for automated AI model development security toolchains."],
    "PS.2.1 R1": ["Cryptographic hashes or digital signatures for the AI model, components, artifacts, and documentation."],
    "PS.2.1 R2": ["Digital signatures for AI model changes."],
    "PS.3.1 R1": ["Version and tracking records for infrastructure tools supporting dataset creation and model training."],
    "PS.3.1 R2": ["Documented justification for AI model selection retained with release information."],
    "PS.3.1 R3": ["Documentation of the training process, including data preprocessing and model architecture."],
    "PS.3.2 R1": ["Provenance records for the AI model, its components and derivatives, and the libraries, frameworks, and pipelines used to build it."],
    "PS.3.2 C1": ["Disclosure of the provenance of training, testing, fine-tuning, and aligning data."],
    "PW.1.1 R1": ["AI model security risk model incorporating relevant vulnerability and threat types."],
    "PW.1.1 C1": ["Updated risk model for future model versions and derivatives."],
    "PW.7.1 R1": ["Code review and analysis policies or guidelines covering AI model code and related components."],
    "PW.8.1 R1": ["Code testing policies and guidelines covering AI models."],
    "PW.8.2 R1": ["AI model vulnerability test results and triaged issue records."],
    "PW.8.2 R2": ["AI model retest results and triaged issue records."],
    "RV.1.1 R1": ["Logs and analysis of AI model inputs and outputs."],
    "RV.1.1 R2": ["Information for users describing mechanisms for reporting potential security and performance issues."],
    "RV.1.2 R1": ["AI model vulnerability scan and test results."],
    "RV.1.2 R2": ["Ongoing automated scan and test results."],
    "RV.1.2 R3": ["AI model audit results."],
    "RV.1.3 R1": ["Vulnerability disclosure and remediation policies covering AI model vulnerabilities."],
    "RV.1.3 R2": ["Information for users describing model limitations and cybersecurity reporting mechanisms."],
    "RV.2.2 R2": ["Criteria and processes for stopping model use and rolling back to a previous version and its components."],
}
NIST_218A_EVIDENCE = dict(NIST_218A_ARTEFACTS)

NIST_218A_VERIFICATION = {
    "PO.3.2 R2": ["Security verification of toolchains at a risk-commensurate frequency."],
    "PO.4.1 C1": ["Human review and approval of software security checks beyond risk-based thresholds."],
    "PS.2.1 R1": ["Cryptographic hash or digital-signature verification."],
    "PS.2.1 R2": ["Digital-signature verification."],
    "PW.3.1 R1": ["Verification of known provenance and data integrity before use."],
    "PW.4.4 R1": ["Integrity, provenance, and security verification before use."],
    "PW.4.4 R2": ["Vulnerability and malicious-content scanning and testing before use."],
    "PW.7.2 R1": ["Scanning for malware, vulnerabilities, backdoors, and other security issues under organizational review policies."],
    "PW.8.1 R1": ["Unit, integration, penetration, red-team, use-case, or adversarial testing, as selected by the organization."],
    "PW.8.1 C1": ["Automated regression testing in the development pipeline where possible."],
    "PW.8.2 R1": ["Vulnerability testing under organizational code-testing policies or guidelines."],
    "PW.8.2 R2": ["Retesting following model retraining or addition of data sources."],
    "RV.1.2 R1": ["Frequent scanning and testing for previously undetected vulnerabilities."],
    "RV.1.2 R2": ["Primarily automated ongoing scanning and testing, with human involvement as needed."],
    "RV.1.2 R3": ["Periodic AI model audits."],
}

NIST_218A_SPECIFIC_QUALIFICATIONS = {
    "PO.1.2 R1": ["Requirements may arise from laws, regulations, contracts, and standards."],
    "PO.4.1 C1": ["Human review and approval is considered for checks beyond risk-based thresholds."],
    "PO.5.1 C1": ["Environment separation is considered only to the extent feasible."],
    "PS.1.1 R1": ["Protected model elements need not be stored together or through the same mechanism."],
    "PS.1.2 R1": ["The confidentiality monitoring recommendation applies only to non-public data."],
    "PS.1.2 C1": ["Future storage is considered only if feasible."],
    "PS.1.3 R2": ["The confidentiality monitoring recommendation applies only to closed models."],
    "PW.1.1 C1": ["The consideration applies after release to future model versions and derivatives."],
    "PW.1.1 C2": ["The consideration concerns critical paths for significant security decisions without a human in the loop."],
    "PW.3.1 R1": ["Provenance is verified when known."],
    "PW.8.1 C1": ["Pipeline automation is considered where possible."],
    "RV.1.1 R2": ["For this recommendation, users are AI system producers and acquirers using an AI model."],
    "RV.1.2 R2": ["A human is involved as needed rather than by default for every scan or test."],
    "RV.2.2 C1": ["Alternative operations continue until the model's risks are sufficiently addressed."],
}

# Curated after action-by-action comparison with NIST AI 600-1. These 60
# source-defined action identities were retained while their complete action
# text and field-level constituent semantics were restored on 2026-08-28.
NIST_GAI_CONSTITUENT_REPAIRS = {
    "EXTREQ-007D7BAAE8A25C9D", "EXTREQ-036F8B9FBBE33437",
    "EXTREQ-09A4C260900D6A83", "EXTREQ-0E404DEFECDA5FE0",
    "EXTREQ-11A6E84345FB4301", "EXTREQ-1269988FF25A00FD",
    "EXTREQ-13DCE314CA72D587", "EXTREQ-1AAAF9F63C4B77A8",
    "EXTREQ-210E95EA572DB5FC", "EXTREQ-25BDC1BF6A486355",
    "EXTREQ-3209D60A503A7B46", "EXTREQ-3287D5CADAAE2D71",
    "EXTREQ-383E0AAF594EFF28", "EXTREQ-38A00DC3A54A582F",
    "EXTREQ-3CF6BE0334DEC565", "EXTREQ-3DE000C1C7E37071",
    "EXTREQ-3F827BC2D6FB855C", "EXTREQ-4277B23509413079",
    "EXTREQ-42E00BFFFB610685", "EXTREQ-4935F57986DF9317",
    "EXTREQ-4972B48203D4A92C", "EXTREQ-4D5BF8BEA4A413B0",
    "EXTREQ-4FA48F69E0D84D76", "EXTREQ-56049F64C61351DF",
    "EXTREQ-572E8F9A8CA166B2", "EXTREQ-5CEC8E71C7C1373F",
    "EXTREQ-606A32149AB41BA4", "EXTREQ-62AE400907DF1A92",
    "EXTREQ-684FDF9FC22A253D", "EXTREQ-696F45AAD993A382",
    "EXTREQ-6C9AF8BEB0C00E2C", "EXTREQ-6F77B758D19B752C",
    "EXTREQ-6FB32C15D60F5ECA", "EXTREQ-7BC3EDE0976A4F5B",
    "EXTREQ-7E4ACD956465C7ED", "EXTREQ-7E7500D622B64943",
    "EXTREQ-7F3E164A4F5EB23A", "EXTREQ-80C57DEB7282DF1E",
    "EXTREQ-84B3A244B2A9DDD1", "EXTREQ-864ED9C1B56018A2",
    "EXTREQ-8943536BE57E678B", "EXTREQ-89EDF6573EDE84D8",
    "EXTREQ-A67E54A283E42597", "EXTREQ-AC5BA019342AFFE9",
    "EXTREQ-B0737DEC2D388821", "EXTREQ-B609E1D64C88DC3D",
    "EXTREQ-BA19F5BDCF5FA962", "EXTREQ-BA7B79BDE2DC32FB",
    "EXTREQ-C37E171E0EA8E0CA", "EXTREQ-C395266FE4929644",
    "EXTREQ-CDA0F3004234AF9C", "EXTREQ-D01548E276DC81C7",
    "EXTREQ-D038CD035E17057F", "EXTREQ-D81F0D37C92F766F",
    "EXTREQ-E6335E9335C8D367", "EXTREQ-E7CB2246EA0311DC",
    "EXTREQ-F0686AA575DC32B9", "EXTREQ-F5EE679C987F9F08",
    "EXTREQ-F7D150323DFB3260", "EXTREQ-FCDE17D3F0843F55",
}

GAI_ACTOR = "Organization or relevant AI actor applying NIST AI 600-1"
GAI_APPLICABILITY = (
    "Applicability is determined from organizational considerations and the "
    "organization's unique use of GAI systems."
)
ACTOR_TAG_SCHEME = "NIST AI 600-1 AI Actor Tasks (subcategory-level)"
NIST_GAI_REVIEW_DIGEST = "6e73620ab6b64e90ef2c04bf0e0d6246185a2f4b1b13cab0df494496cff89b6a"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_nist_gai_actor_metadata(record: dict) -> None:
    provenance = record["interpretation_provenance"]
    provenance["reviewed_source_digest"] = NIST_GAI_REVIEW_DIGEST
    provenance["reviewed_source_digest_algorithm"] = "sha256"
    provenance["reviewed_source_digest_status"] = "recorded"
    if not re.fullmatch(r"(?:GV|MP|MS|MG)-\d+\.\d+-\d{3}", record["clause_or_control"]):
        return
    current = record.get("applicable_actor", [])
    tags = record.setdefault("source_defined_tags", [])
    actor_tag = next((tag for tag in tags if tag.get("scheme") == ACTOR_TAG_SCHEME), None)
    if current != [GAI_ACTOR]:
        if len(current) != 1 or not current[0]:
            raise ValueError(f"unexpected NIST AI 600-1 actor metadata for {record['requirement_id']}")
        values = [value.strip() for value in current[0].split(",") if value.strip()]
        expected_tag = {"scheme": ACTOR_TAG_SCHEME, "values": values}
        if actor_tag is not None and actor_tag != expected_tag:
            raise ValueError(f"conflicting NIST AI 600-1 actor-task tag for {record['requirement_id']}")
        if actor_tag is None:
            tags.append(expected_tag)
        record["applicable_actor"] = [GAI_ACTOR]
    elif actor_tag is None:
        raise ValueError(f"normalized actor lacks preserved source actor-task tag for {record['requirement_id']}")

    conditions = record.get("applicability_conditions", [])
    if not conditions:
        record["applicability_conditions"] = [GAI_APPLICABILITY]
    elif conditions[0] != GAI_APPLICABILITY:
        raise ValueError(f"unexpected NIST AI 600-1 applicability metadata for {record['requirement_id']}")


def _contains(action: str, *needles: str) -> bool:
    lower = action.lower()
    return any(needle in lower for needle in needles)


def normalize_nist_gai_constituent_metadata(record: dict) -> None:
    """Resolve the reviewed field dimensions without changing action identity."""
    if record["requirement_id"] not in NIST_GAI_CONSTITUENT_REPAIRS:
        return
    action = record["governance_expectation"].strip()
    if not action or "…" in action:
        raise ValueError(f"incomplete NIST AI 600-1 action text for {record['requirement_id']}")
    record["requirement_summary"] = action

    objects = []
    object_rules = (
        (("incident",), "GAI incident response, recovery, disclosure, and communication processes"),
        (("content provenance", "content authentication"), "GAI content-provenance data, methods, and controls"),
        (("training data", "tevv data", "evaluation data"), "GAI training and testing, evaluation, verification, and validation data"),
        (("generated content", "gai output", "gai system output"), "GAI system outputs and generated content"),
        (("third-party", "vendor", "supplier", "acquisition", "procurement"), "Third-party GAI resources, suppliers, and service relationships"),
        (("end-user", "end user", "human reviewer", "affected communit"), "Human interactions with and impacts from GAI systems"),
        (("risk", "bias", "fairness", "security", "privacy"), "GAI risks, tolerances, assessments, and controls"),
        (("gai model", "gai system"), "GAI models, systems, and lifecycle processes"),
    )
    for needles, label in object_rules:
        if _contains(action, *needles) and label not in objects:
            objects.append(label)
    record["governed_object"] = objects or ["The GAI practice expressly addressed by the cited suggested action"]

    timing = []
    timing_rules = (
        (("at a regular cadence", "regular cadences"), "At the regular cadence specified by the action."),
        (("periodic monitoring",), "Periodically."),
        (("continuous monitoring", "continual improvement", "continuous improvement"), "Continuously or as part of continual improvement."),
        (("real-time monitoring", "real-time reporting"), "In real time."),
        (("after-action", "post-mortem", "retrospective learning"), "After relevant incidents."),
        (("deployment approval", "pre-deployment"), "Before or as part of deployment approval."),
        (("when decommissioning", "deactivation or disengagement"), "When decommissioning, deactivating, or disengaging the GAI system."),
        (("when adapting", "new domain"), "When adapting or detecting use of a GAI model in a new domain."),
        (("over time",), "Over time."),
    )
    for needles, label in timing_rules:
        if _contains(action, *needles) and label not in timing:
            timing.append(label)
    record["timing_or_frequency"] = timing

    artefacts = []
    artefact_rules = (
        (("policies", "procedures"), "Policies and procedures specified by the action."),
        (("plans",), "Plans specified by the action."),
        (("document", "documentation"), "Action-specific documentation specified by the source."),
        (("record", "tracked"), "Records specified by the action."),
        (("inventory entries",), "GAI system inventory entries."),
        (("contracts", "service level agreements", "slas"), "Vendor contracts and service-level agreements."),
        (("measurement error models",), "Measurement error models."),
        (("warning systems",), "Warning systems for changed-domain use."),
        (("training materials",), "Training materials."),
    )
    for needles, label in artefact_rules:
        if _contains(action, *needles) and label not in artefacts:
            artefacts.append(label)
    record["required_artefacts"] = artefacts

    evidence = []
    evidence_rules = (
        (("document", "record", "tracked"), "The action-specific documentation or records specified by the source."),
        (("test", "red-team"), "Results of the source-specified testing or red-teaming."),
        (("assess", "evaluate", "review", "measure", "benchmark", "compare"), "Results of the source-specified assessment, evaluation, review, or measurement."),
        (("monitor",), "Outputs from the source-specified monitoring."),
        (("feedback", "survey", "focus group", "community forum"), "Structured feedback, survey, or engagement results specified by the action."),
    )
    for needles, label in evidence_rules:
        if _contains(action, *needles) and label not in evidence:
            evidence.append(label)
    record["evidence_expectation"] = evidence

    verification = []
    verification_rules = (
        (("red-team", "adversarial testing"), "AI red-teaming or adversarial testing specified by the action."),
        (("fairness assessment",), "Fairness assessment using the source-specified metrics and methods."),
        (("benchmark", "compare"), "Benchmarking or comparison specified by the action."),
        (("monitor",), "Monitoring specified by the action."),
        (("survey", "focus group", "community forum", "structured feedback"), "User research or structured-feedback method specified by the action."),
        (("assess", "evaluate", "review", "measure", "verify"), "Assessment, evaluation, review, measurement, or verification specified by the action."),
    )
    for needles, label in verification_rules:
        if _contains(action, *needles) and label not in verification:
            verification.append(label)
    record["verification_method"] = verification

    conditions = [GAI_APPLICABILITY]
    condition_rules = (
        (("where appropriate", "where applicable", "as applicable"), "Where the action states that the practice is appropriate or applicable."),
        (("context of use", "context(s) of use"), "Within the relevant GAI context of use."),
        (("third-party", "vendor", "supplier"), "Where third-party GAI resources, suppliers, or services are involved."),
        (("new domain",), "Where a GAI model is adapted to, or used in, a new domain."),
        (("decommission", "deactivation", "disengagement"), "Where the GAI system or use context is being decommissioned, deactivated, or disengaged."),
        (("do not surpass organizational risk tolerance",), "For risks that do not surpass organizational risk tolerance."),
    )
    for needles, label in condition_rules:
        if _contains(action, *needles) and label not in conditions:
            conditions.append(label)
    record["applicability_conditions"] = conditions

    qualifications = []
    if _contains(action, "e.g.", "for example", "such as", "including"):
        qualifications.append("Examples and included items in the suggested action are illustrative of its stated scope, not an inferred exhaustive list.")
    if _contains(action, "reasonable measures"):
        qualifications.append("The source qualifies the measures as reasonable.")
    if _contains(action, "where appropriate", "where applicable", "as applicable"):
        qualifications.append("The source expressly qualifies the relevant practice by appropriateness or applicability.")
    if _contains(action, "may include"):
        qualifications.append("The listed plan contents are optional examples because the source states that plans may include them.")
    record["exceptions_or_qualifications"] = qualifications

    record["source_review_date"] = "2026-08-28"
    provenance = record["interpretation_provenance"]
    provenance["source_analysis_method"] = (
        "Direct primary-text constituent-fidelity review against the official NIST AI 600-1 PDF; "
        "the source-defined suggested-action identity was retained and complete action semantics "
        "were resolved across the structured metadata dimensions."
    )


def set_reviewed_metadata(record: dict, field: str, values: list[str]) -> None:
    current = record.get(field, [])
    if current not in ([], values):
        raise ValueError(
            f"unexpected {field} metadata for {record['requirement_id']}: {current!r}"
        )
    record[field] = values


def normalize_imda_metadata(record: dict) -> None:
    set_reviewed_metadata(record, "applicability_conditions", [IMDA_SCOPE])
    rid = record["requirement_id"]
    if rid == "EXTREQ-4B28B179BF91F130":
        set_reviewed_metadata(
            record,
            "timing_or_frequency",
            ["Before deciding to develop or deploy an agentic AI use case."],
        )
    elif rid == "EXTREQ-99712BA8308E32FF":
        set_reviewed_metadata(
            record,
            "required_artefacts",
            ["Agent safety and security test results."],
        )
        set_reviewed_metadata(
            record,
            "verification_method",
            [
                "Pre-deployment testing of complete workflows, individual and multi-agent behavior, realistic environments, varied datasets and repeated runs."
            ],
        )
    elif rid == "EXTREQ-C867BF4ECD4B5161":
        set_reviewed_metadata(
            record,
            "verification_method",
            ["Threat modelling supported by taint tracing of workflows, interactions and untrusted-data flows."],
        )


NIST_218A_LEGACY_METADATA = {
    "timing_or_frequency": {
        "Continuously, as expressly stated in the cited provision or control.",
        "Before the stated use, deployment or release event.",
        "Periodically or regularly, as expressly stated in the cited provision or control.",
        "After the stated model, data or system change.",
    },
    "required_artefacts": {
        "Policy or policy update expressly specified by the cited requirement or control.",
        "Documentation expressly specified by the cited requirement or control.",
        "Report expressly specified by the cited requirement or control.",
    },
    "evidence_expectation": {
        "Monitoring output or review record specified by the cited action.",
        "Test plan, result or evaluation evidence specified by the cited action.",
        "Documented output or record specified by the cited action.",
        "Report or reporting evidence specified by the cited action.",
    },
    "verification_method": {
        "Scanning specified by the source.",
        "Cryptographic integrity verification specified by the source.",
        "Digital-signature verification specified by the source.",
        "Audit specified by the source.",
        "Adversarial testing specified by the source.",
        "Red-team testing specified by the source.",
        "Penetration testing specified by the source.",
    },
}


def set_curated_nist_218a_metadata(record: dict, field: str, values: list[str]) -> None:
    current = record.get(field, [])
    if current == values:
        return
    allowed = NIST_218A_LEGACY_METADATA.get(field, set())
    if current and not (allowed and set(current).issubset(allowed)):
        raise ValueError(
            f"unexpected NIST SP 800-218A {field} metadata for "
            f"{record['requirement_id']}: {current!r}"
        )
    record[field] = values


def normalize_nist_218a_metadata(record: dict) -> None:
    rid = record["requirement_id"]
    clause = record["clause_or_control"]
    affected = set(NIST_218A_BACKLOG.get(rid, ([], [], "", ""))[1])

    current_actor = record.get("applicable_actor", [])
    expected_actors = [["AI model producer"], [NIST_218A_ACTOR]]
    if current_actor not in expected_actors:
        raise ValueError(f"unexpected NIST SP 800-218A actor metadata for {rid}")
    record["applicable_actor"] = [NIST_218A_ACTOR]

    set_reviewed_metadata(record, "applicability_conditions", [NIST_218A_SCOPE])
    qualifications = NIST_218A_GLOBAL_QUALIFICATIONS + NIST_218A_SPECIFIC_QUALIFICATIONS.get(clause, [])
    current_qualifications = record.get("exceptions_or_qualifications", [])
    if current_qualifications not in ([], qualifications):
        raise ValueError(f"unexpected NIST SP 800-218A qualifications for {rid}")
    record["exceptions_or_qualifications"] = qualifications

    curated = {
        "timing_or_frequency": NIST_218A_TIMING.get(clause, []),
        "required_artefacts": NIST_218A_ARTEFACTS.get(clause, []),
        "evidence_expectation": NIST_218A_EVIDENCE.get(clause, []),
        "verification_method": NIST_218A_VERIFICATION.get(clause, []),
    }
    for field, values in curated.items():
        if field not in affected:
            set_curated_nist_218a_metadata(record, field, values)


def backlog_entries(records: list[dict]) -> list[dict]:
    by_id = {record["requirement_id"]: record for record in records}
    missing = sorted(NIST_GAI_CONSTITUENT_REPAIRS - set(by_id))
    if missing:
        raise ValueError(f"NIST AI 600-1 constituent-repair IDs do not resolve: {missing}")
    entries = []
    unresolved = [
        rid for rid in sorted(NIST_GAI_CONSTITUENT_REPAIRS)
        if "…" in by_id[rid]["requirement_summary"]
        or by_id[rid]["requirement_summary"] != by_id[rid]["governance_expectation"]
    ]
    if unresolved:
        raise ValueError(f"NIST AI 600-1 constituent repairs are incomplete: {unresolved}")

    record = by_id[CYCLONEDX_MODALITY_DEFECT]
    entries.append({
        "current_requirement_id": record["requirement_id"],
        "vigil_source_id": record["vigil_source_id"],
        "external_source_id": record["external_source_id"],
        "source_version": record["source_version"],
        "clause_or_control": record["clause_or_control"],
        "reason": (
            "The current record combines the mandatory bom-ref uniqueness rule with the "
            "recommended reserved-prefix constraint and represents both as mandatory."
        ),
        "detected_fidelity_defects": [
            "compound-normative-propositions", "modality-loss"
        ],
        "affected_metadata_dimensions": ["exceptions_or_qualifications"],
        "review_status": "queued",
        "source_access_basis": "direct-public-primary",
        "recommended_repair": "semantic-decomposition-with-identity-migration",
    })

    migrate = {
        "EXTREQ-14B4DA1E7646754E", "EXTREQ-2DC8F2B745E464D5",
        "EXTREQ-DB1BC74DC84D4718", "EXTREQ-1F35B4A263EF7055",
        "EXTREQ-DCFA4FF526B6439C", "EXTREQ-DFAE10B7FA4CAEEF",
        "EXTREQ-FE078DDB1FABA3AF", "EXTREQ-24F5ABCB4CAFC499",
    }
    for rid, (defects, affected, reason) in sorted(IMDA_BACKLOG.items()):
        record = by_id.get(rid)
        if record is None or record.get("vigil_source_id") != IMDA_AGENTIC:
            raise ValueError(f"IMDA backlog ID does not resolve to the reviewed source: {rid}")
        entries.append({
            "current_requirement_id": rid,
            "vigil_source_id": record["vigil_source_id"],
            "external_source_id": record["external_source_id"],
            "source_version": record["source_version"],
            "clause_or_control": record["clause_or_control"],
            "reason": reason,
            "detected_fidelity_defects": defects,
            "affected_metadata_dimensions": affected,
            "review_status": "queued",
            "source_access_basis": "direct-public-primary",
            "recommended_repair": (
                "semantic-decomposition-with-identity-migration"
                if rid in migrate else
                "constituent-enrichment-preserve-identity"
            ),
        })
    for rid, (defects, affected, reason, repair) in sorted(NIST_218A_BACKLOG.items()):
        record = by_id.get(rid)
        if record is None or record.get("vigil_source_id") != NIST_218A:
            raise ValueError(f"NIST SP 800-218A backlog ID does not resolve: {rid}")
        entries.append({
            "current_requirement_id": rid,
            "vigil_source_id": record["vigil_source_id"],
            "external_source_id": record["external_source_id"],
            "source_version": record["source_version"],
            "clause_or_control": record["clause_or_control"],
            "reason": reason,
            "detected_fidelity_defects": defects,
            "affected_metadata_dimensions": affected,
            "review_status": "queued",
            "source_access_basis": "direct-public-primary",
            "recommended_repair": repair,
        })
    return sorted(entries, key=lambda entry: entry["current_requirement_id"])


def seed(write: bool) -> int:
    req_doc = load_requirements_document()
    ledger = load(LEDGER)
    records = req_doc["requirements"]
    by_id = {record["requirement_id"]: record for record in records}
    reviewed_sources = {NIST_RMF, CYCLONEDX, NIST_GAI, IMDA_AGENTIC, NIST_218A}
    selected = [record for record in records if record["vigil_source_id"] in reviewed_sources]
    counts = {
        source: sum(record["vigil_source_id"] == source for record in selected)
        for source in reviewed_sources
    }
    if counts != {NIST_RMF: 71, CYCLONEDX: 4, NIST_GAI: 223, IMDA_AGENTIC: 32, NIST_218A: 74}:
        raise ValueError(f"unexpected reviewed source population: {counts}")

    for record in selected:
        if record["vigil_source_id"] == NIST_GAI:
            normalize_nist_gai_actor_metadata(record)
            normalize_nist_gai_constituent_metadata(record)
        elif record["vigil_source_id"] == IMDA_AGENTIC:
            normalize_imda_metadata(record)
        elif record["vigil_source_id"] == NIST_218A:
            normalize_nist_218a_metadata(record)
        if record["vigil_source_id"] != NIST_GAI:
            record["source_review_date"] = "2026-08-26"

    backlog = backlog_entries(records)
    affected_by_id = {
        entry["current_requirement_id"]: set(entry["affected_metadata_dimensions"])
        for entry in backlog
    }
    existing = {entry["requirement_id"]: entry for entry in ledger.get("entries", [])}
    seeded = 0
    for record in selected:
        rid = record["requirement_id"]
        affected = affected_by_id.get(rid, set())
        field_status = {}
        for field in FIELDS:
            if field in affected:
                field_status[field] = "review-required"
            else:
                field_status[field] = (
                    "populated-reviewed" if record.get(field) else "not-specified-by-source"
                )
        if record["vigil_source_id"] == NIST_RMF:
            notes = [
                "Reviewed against NIST AI 100-1 Core Tables 1-4; the source-defined subcategory remains the assessable outcome unit.",
                "Populated metadata was checked against the cited subcategory and framework context; empty fields were resolved only after direct primary-text review."
            ]
        elif record["vigil_source_id"] == CYCLONEDX:
            notes = [
                "Reviewed against the CycloneDX 1.7 JSON schema at release commit 4b3f59453366e27c8073fd24e98bf21ef8892c8e.",
                "Normative modality, component-type applicability, model-card structure and bom-ref constraints were checked directly."
            ]
        elif record["vigil_source_id"] == NIST_GAI:
            notes = [
                "Reviewed against the official NIST AI 600-1 PDF; SHA-256 6e73620ab6b64e90ef2c04bf0e0d6246185a2f4b1b13cab0df494496cff89b6a.",
                "The 60 queued constituent-fidelity actions retain their source-defined identities; complete action text and the seven affected metadata dimensions were resolved on 2026-08-28.",
                "The source's subcategory-level AI Actor Tasks are preserved as source-defined tags rather than attributed to every suggested action.",
            ]
        elif record["vigil_source_id"] == IMDA_AGENTIC:
            notes = [
                "Reviewed against IMDA Model AI Governance Framework for Agentic AI version 1.5, published 20 May 2026 and updated 5 June 2026.",
                "The official PDF was retrieved directly from IMDA; SHA-256 2636e19ff1c86e862394d2fc900592e97b83c04cc35e3c8443108114b7f1dfba.",
                "The framework-wide deployment scope is source-explicit; fields affected by over-compression or a section-level locator remain review-required pending deterministic re-extraction."
            ]
        else:
            notes = [
                "Reviewed against NIST SP 800-218A, July 2024, together with its task context and source-wide scope and adaptation rules.",
                "The official NIST PDF was retrieved through DOI 10.6028/NIST.SP.800-218A; SHA-256 e088c8bc75716824dae7c36a987f408364638561d381ed001b5c12254a7b10d8.",
                "Source-native recommendation and consideration identities were retained except where a queued record collapses modalities; mechanically inferred evidence was removed or replaced only with source-express outputs and methods."
            ]
        entry = {
            "requirement_id": rid,
            "reviewed_at": "2026-08-28" if record["vigil_source_id"] == NIST_GAI else "2026-08-26",
            "review_basis": "direct-primary-text",
            "review_notes": notes,
            "field_status": field_status,
        }
        current = existing.get(rid)
        if current is not None and current != entry:
            if record["vigil_source_id"] != NIST_GAI:
                raise ValueError(f"existing metadata-review decision differs for {rid}; manual reconciliation required")
            existing[rid] = entry
        elif current is None:
            existing[rid] = entry
            seeded += 1

    output_ledger = {
        "schema_version": ledger.get("schema_version", "1.0"),
        "updated_at": "2026-08-28",
        "entries": sorted(existing.values(), key=lambda entry: entry["requirement_id"]),
    }
    output_backlog = {"schema_version": "1.0", "updated_at": "2026-08-28", "entries": backlog}
    print(
        "Reviewed-source metadata seed valid: "
        f"{len(selected)} requirements; {seeded} new ledger entries; {len(backlog)} backlog entries"
    )
    if write:
        write_requirements_document(req_doc)
        LEDGER.write_text(json.dumps(output_ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        BACKLOG.write_text(json.dumps(output_backlog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote canonical EXTREQ shards under {REQUIREMENTS_ROOT}")
        print(f"Wrote {LEDGER}")
        print(f"Wrote {BACKLOG}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    raise SystemExit(seed(args.write))


if __name__ == "__main__":
    main()
