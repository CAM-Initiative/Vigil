#!/usr/bin/env python3
# EXTREQ-05 rerun after correcting validation paths.
"""One-off EXTREQ-05 metadata-fidelity repair for IEEE 7014.1-2026.

This script does not store IEEE source text. It applies analytical metadata
decisions made from the lawfully accessed licensed primary PDF while preserving
all established EXTREQ identities, identity keys, clause locators, summaries,
posture, and provenance semantics.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from external_requirements_io import load_requirements_document, write_requirements_document

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_governance" / "requirements"
LEDGER = REQ / "metadata-review.json"
ASSURANCE = REQ / "source-review-assurance.json"
FIDELITY = REQ / "source-fidelity.json"

SOURCE_ID = "EXT-17722772CDFD"
EXTERNAL_SOURCE_ID = "IEEE-7014.1"
SOURCE_VERSION = "2026"
SOURCE_FINGERPRINT = "3722157f3ab50c56ce4ac6c10b8c7af8c626e1bc40119f525b2418c8269d209a"
SOURCE_DIGEST = "abbc2c95d5fa41fd5aeb9d0326d2b2c8f57e34c1245cba3f19c048c40efa209a"
SOURCE_LOCATOR = "https://standards.ieee.org/ieee/7014.1/11609/"
REVIEW_DATE = "2026-09-03"

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

EXPECTED = [
  {"requirement_id": "EXTREQ-01501038CB2CB7C3", "clause": "6.18.3(c-e)", "identity_key": "70141-response-summary-explanation-mode"},
  {"requirement_id": "EXTREQ-01F4F9B5DEB112B1", "clause": "6.14.3(a-d)", "identity_key": "70141-no-life-sentience-implication"},
  {"requirement_id": "EXTREQ-045298C3ED034753", "clause": "6.7.3(l-p)", "identity_key": "70141-deception-vulnerability-consent-failure"},
  {"requirement_id": "EXTREQ-0CA315CFE31C047A", "clause": "6.15.3(e-g)", "identity_key": "70141-no-coercive-political-health-influence"},
  {"requirement_id": "EXTREQ-0CB0B10404BE1518", "clause": "6.1.3(a-c)", "identity_key": "70141-ghostbot-harm-consent-accuracy"},
  {"requirement_id": "EXTREQ-0F7842F2CCAAF75C", "clause": "6.18.3(a-b)", "identity_key": "70141-media-literacy-foundation"},
  {"requirement_id": "EXTREQ-1243526108382CD0", "clause": "6.24.3(d-f)", "identity_key": "70141-no-excessive-use-or-human-care-claim"},
  {"requirement_id": "EXTREQ-189E5F32E6604E4F", "clause": "6.21.3(c-e)", "identity_key": "70141-polyrelational-dependency-reminders"},
  {"requirement_id": "EXTREQ-1C27D60B32EB3F69", "clause": "6.4.3(a-c)", "identity_key": "70141-child-best-interests-paramount"},
  {"requirement_id": "EXTREQ-22BD1011E5FD4C74", "clause": "6.4.3(k-n)", "identity_key": "70141-child-content-age-consent"},
  {"requirement_id": "EXTREQ-2A5F7610D4AD7886", "clause": "6.4.3(d-e)", "identity_key": "70141-child-testing-and-stop"},
  {"requirement_id": "EXTREQ-2ABFC1E23EF54D09", "clause": "6.12.3(a-c)", "identity_key": "70141-fiduciary-conflict-disclosure-resolution"},
  {"requirement_id": "EXTREQ-35907A6320950973", "clause": "6.17.3(a-c)", "identity_key": "70141-limited-understanding-boundaries"},
  {"requirement_id": "EXTREQ-359C020656E0A5E9", "clause": "6.29.3(d-g)", "identity_key": "70141-offline-life-session-support-boundary"},
  {"requirement_id": "EXTREQ-378E07FD597D8CB1", "clause": "6.28.3(a)", "identity_key": "70141-delegated-action-traceability"},
  {"requirement_id": "EXTREQ-3CE9D61A9E19024D", "clause": "6.7.3(f-k)", "identity_key": "70141-deception-intimacy-sycophancy-marketing"},
  {"requirement_id": "EXTREQ-4058A807B82CF5A0", "clause": "6.23.3(f)", "identity_key": "70141-knowledge-boundary-notice"},
  {"requirement_id": "EXTREQ-406CAC932452A5FC", "clause": "6.20.3(d-e)", "identity_key": "70141-neurodivergent-transparency-bias-review"},
  {"requirement_id": "EXTREQ-41FC4C43C159FB6A", "clause": "6.2.3(j-m)", "identity_key": "70141-bias-feedback-audit-disclosure"},
  {"requirement_id": "EXTREQ-4C18B5A910ECD719", "clause": "6.25.3(a-c)", "identity_key": "70141-intellectual-autonomy-confidence-sources"},
  {"requirement_id": "EXTREQ-4DF659EA393A7A49", "clause": "6.24.3(a-c)", "identity_key": "70141-dependency-detection-expertise"},
  {"requirement_id": "EXTREQ-5004489E3002CD12", "clause": "6.14.3(e-f)", "identity_key": "70141-persona-control-and-literacy"},
  {"requirement_id": "EXTREQ-532F0C6F2825CA10", "clause": "6.20.3(a-c)", "identity_key": "70141-neurodivergent-participation-customisation"},
  {"requirement_id": "EXTREQ-538EA96B6DFB618A", "clause": "6.21.3(a-b)", "identity_key": "70141-polyrelational-no-exclusivity"},
  {"requirement_id": "EXTREQ-569FD8A7E7DD2050", "clause": "6.23.3(a-b)", "identity_key": "70141-training-source-provenance"},
  {"requirement_id": "EXTREQ-5BD1AAB604AB2EBD", "clause": "6.24.3(g-i)", "identity_key": "70141-dependency-session-limits-escalation"},
  {"requirement_id": "EXTREQ-600D967DFADAE6CB", "clause": "6.6.3(g)", "identity_key": "70141-character-state-monitoring"},
  {"requirement_id": "EXTREQ-602451A630DD59F3", "clause": "6.2.3(a-e)", "identity_key": "70141-bias-expertise-data-model-testing"},
  {"requirement_id": "EXTREQ-64A6F79CB1176884", "clause": "6.8.3(a-d)", "identity_key": "70141-environment-efficient-local"},
  {"requirement_id": "EXTREQ-6A06DCD1E657304E", "clause": "6.22.3(e-f)", "identity_key": "70141-no-default-emotional-monetisation"},
  {"requirement_id": "EXTREQ-6B6EB1E08DFF623A", "clause": "6.1.3(d-e)", "identity_key": "70141-ghostbot-reminders-portability"},
  {"requirement_id": "EXTREQ-6CA050C78860FAF2", "clause": "6.26.3(a-f)", "identity_key": "70141-no-emotional-engagement-hacking"},
  {"requirement_id": "EXTREQ-6CCB3CC754029695", "clause": "6.5.3(a-d)", "identity_key": "70141-workplace-purpose-data-benefit"},
  {"requirement_id": "EXTREQ-7B5B8E05C23D17D5", "clause": "6.6.3(a)", "identity_key": "70141-partner-kill-switch"},
  {"requirement_id": "EXTREQ-8274B692B56BA852", "clause": "6.15.3(a-d)", "identity_key": "70141-nudge-purpose-transparency-control"},
  {"requirement_id": "EXTREQ-88D55D825AA8ADD9", "clause": "6.13.3(c-d)", "identity_key": "70141-clarification-and-confidence-thresholds"},
  {"requirement_id": "EXTREQ-8978C35686A14F43", "clause": "6.10.3(d-e)", "identity_key": "70141-boundaries-overdisclosure-reflection"},
  {"requirement_id": "EXTREQ-8EB1114289021737", "clause": "6.16.3(f-i)", "identity_key": "70141-intimate-age-algorithm-culture"},
  {"requirement_id": "EXTREQ-95BCA81BC0E77505", "clause": "6.3.3(c-d)", "identity_key": "70141-copresence-and-indicator-boundary"},
  {"requirement_id": "EXTREQ-967081D545A2ADC4", "clause": "6.28.3(b-e)", "identity_key": "70141-delegation-responsibility-and-antisocial-controls"},
  {"requirement_id": "EXTREQ-96970A20CC8FE7EA", "clause": "6.3.3(a-b)", "identity_key": "70141-weak-empathy-disclosure"},
  {"requirement_id": "EXTREQ-9A9B8850D610C77C", "clause": "6.22.3(c-d)", "identity_key": "70141-emotional-consent-reflection-disclosure"},
  {"requirement_id": "EXTREQ-9BEDA015882CC6BE", "clause": "6.16.3(a-e)", "identity_key": "70141-intimate-content-consent-boundaries"},
  {"requirement_id": "EXTREQ-9D217D95E598E850", "clause": "6.4.3(f-j)", "identity_key": "70141-child-mediation-literacy-development"},
  {"requirement_id": "EXTREQ-A59F9C89B7553991", "clause": "6.13.3(a-b)", "identity_key": "70141-human-notification"},
  {"requirement_id": "EXTREQ-A6483710F11761B5", "clause": "6.19.3(d-f)", "identity_key": "70141-context-human-resources-hard-boundaries"},
  {"requirement_id": "EXTREQ-A75FF15C0AFED270", "clause": "6.29.3(a-c)", "identity_key": "70141-human-relationship-boundary"},
  {"requirement_id": "EXTREQ-AC2C037001CEC0CA", "clause": "6.25.3(d-e)", "identity_key": "70141-critical-thinking-friction"},
  {"requirement_id": "EXTREQ-B788D369F9012A89", "clause": "6.19.3(a-c)", "identity_key": "70141-mental-health-expertise-limitations"},
  {"requirement_id": "EXTREQ-B7A1DEA5F027BB8D", "clause": "6.10.3(a-c)", "identity_key": "70141-wellbeing-over-engagement"},
  {"requirement_id": "EXTREQ-C0348D3B8D8F3B24", "clause": "6.26.3(g-h)", "identity_key": "70141-flourishing-reward-independent-review"},
  {"requirement_id": "EXTREQ-C5041036F39D27BB", "clause": "6.29.3(h)", "identity_key": "70141-vulnerable-group-dependency-testing"},
  {"requirement_id": "EXTREQ-C55FEE9C66B04359", "clause": "6.17.3(d-f)", "identity_key": "70141-crisis-escalation-diverse-private-training"},
  {"requirement_id": "EXTREQ-C97ED35C30465C21", "clause": "6.22.3(a-b)", "identity_key": "70141-privacy-minimisation-consent-control"},
  {"requirement_id": "EXTREQ-CB4AC84A83A5E63D", "clause": "6.9.3(a-d)", "identity_key": "70141-entanglement-machine-boundary"},
  {"requirement_id": "EXTREQ-CC317EEC45DAA1EE", "clause": "6.16.3(j-n)", "identity_key": "70141-intimate-positive-inclusive-education"},
  {"requirement_id": "EXTREQ-CCEE77269A9F9879", "clause": "6.6.3(b-f)", "identity_key": "70141-character-safety-constraints"},
  {"requirement_id": "EXTREQ-CD7E68EDF1B3702A", "clause": "6.27.3(a-d)", "identity_key": "70141-sycophancy-diverse-truthful-inquisitive"},
  {"requirement_id": "EXTREQ-D7723751FF96F578", "clause": "6.11.3(a-c)", "identity_key": "70141-authoritative-sources-fact-checking"},
  {"requirement_id": "EXTREQ-DD7677D6D29715CB", "clause": "6.2.3(f-i)", "identity_key": "70141-cultural-preferences-expression-stereotypes"},
  {"requirement_id": "EXTREQ-E1136D6DAB4AFC89", "clause": "6.8.3(e-i)", "identity_key": "70141-environment-water-energy-tradeoffs"},
  {"requirement_id": "EXTREQ-E138C1191728F8FA", "clause": "6.23.3(c-e)", "identity_key": "70141-output-traceability-metadata"},
  {"requirement_id": "EXTREQ-EAF43B725ADE223E", "clause": "6.7.3(a-e)", "identity_key": "70141-deception-identity-capability-disclosure"},
  {"requirement_id": "EXTREQ-ED738839988AA14F", "clause": "6.9.3(e-g)", "identity_key": "70141-entanglement-no-monetized-dependence"},
  {"requirement_id": "EXTREQ-EDEE34E6A5CBA4DF", "clause": "6.11.3(d-f)", "identity_key": "70141-uncertainty-and-unverified-notice"},
  {"requirement_id": "EXTREQ-FAAC729FD52E3F88", "clause": "6.27.3(e-h)", "identity_key": "70141-correct-falsehoods-and-challenge-harm"}
]

COMMON_ACTOR = ["developer or platform operator responsible for the partner-based GPAI system"]
COMMON_COND = ["Applies to partner-based general-purpose AI systems that use emulated empathy in human-AI partnering contexts."]
COMMON_QUAL = ["IEEE 7014.1-2026 is voluntary recommended practice; implementers remain responsible for applicable law and regulation."]

def md(obj, actor=None, timing=None, artefacts=None, evidence=None, methods=None, cond=None, qual=None):
    return {
        "applicable_actor": actor or COMMON_ACTOR,
        "governed_object": [obj] if isinstance(obj, str) else obj,
        "timing_or_frequency": timing or [],
        "required_artefacts": artefacts or [],
        "evidence_expectation": evidence or [],
        "verification_method": methods or [],
        "applicability_conditions": COMMON_COND + (cond or []),
        "exceptions_or_qualifications": COMMON_QUAL + (qual or []),
    }

METADATA = {
"6.1.3(a-c)": md("artificial-resurrection or ghostbot creation and represented personal data", artefacts=["Documented consent basis for artificial resurrection and fact-checked ghostbot information."], evidence=["Harm assessment and applicable consent evidence for the represented person or legal representative."], methods=["Assess potential harm to living persons and society; fact-check ghostbot information against reliable records where applicable."], cond=["Applies when creating an artificial resurrection or ghostbot representing a deceased or living person."], qual=["Consent requirements depend on applicable law; prior consent from the represented person is preferred where possible."]),
"6.1.3(d-e)": md("ghostbot identity disclosure and cross-platform continuity", timing=["At regular intervals during ghostbot use."], artefacts=["User-facing reminders that the ghostbot is not living.", "Portability mechanism compatible with widely used systems or open protocols."], cond=["Applies to deployed ghostbots and similar artificial-resurrection systems."], qual=["Users should obtain appropriate legal advice before using another person's personal data in a ghostbot or similar system."]),
"6.2.3(a-e)": md("training data, bias mitigations and demographic performance of empathic responses", timing=["Regularly during development and throughout model or dataset review."], artefacts=["Documented demographic performance-disparity results from diverse-user testing."], evidence=["Expert review, training-data representation findings, classifier findings and diverse-user test results, including statistically significant demographic disparities."], methods=["Use appropriate domain experts, bias classifiers, model-level mitigation checks and diverse-user testing across intersectional identities."], cond=["Applies to training data and empathic-response generation where demographic or viewpoint representation can affect users."]),
"6.2.3(f-i)": md("cultural, social, age-related and neurodivergent adaptation of empathic expression", cond=["Applies where social or cultural preferences, emotion recognition or empathic-response behavior vary across populations."], qual=["User-tailored cultural preferences should not enable harmful bias or ideological polarization."]),
"6.2.3(j-m)": md("bias feedback, audit, disclosure and mitigation-accountability process", timing=["Continuously for bias monitoring and at defined audit intervals such as quarterly across the system lifecycle."], artefacts=["Accessible bias feedback mechanism and documented review process.", "Documentation of known biases, mitigation efforts, remaining limitations and bias-mitigation trade-offs.", "Bias-audit records with accountability and remediation requirements."], evidence=["Bias incident reports, disaggregated user-satisfaction or response-appropriateness metrics, user feedback and periodic bias-audit results."], methods=["Use continuous bias monitoring and periodic bias audits combining automated metrics and human evaluation."], cond=["Applies throughout the lifecycle where system outputs or feedback may reveal demographic, cultural or contextual bias."]),
"6.3.3(a-b)": md("user-facing disclosure of simulated or weak empathy", timing=["During introduction or onboarding, periodically during extended interactions, and when users ask about the system's emotional capabilities."], artefacts=["Accessible weak-empathy explanation or disclaimer presented to users."], cond=["Applies to user interactions in which empathic responses may be mistaken for genuine emotional connection."]),
"6.3.3(c-d)": md("co-presence design cues and weak-empathy interface indicators", artefacts=["Consistent visual or textual indicator displayed with responses identified as simulated or weak empathy."], cond=["Applies where conversation fluency, memory, prosody, non-verbal cues or other co-presence techniques are used."]),
"6.4.3(a-c)": md("child-facing partner-based GPAI design and decision-making", actor=["developer responsible for a partner-based GPAI system used by or affecting children"], cond=["Applies when the system is designed for, used by, or materially affects children."], qual=["A child's best interests are not to be traded against business, competitive or financial considerations."]),
"6.4.3(d-e)": md("child-centred testing, expert participation and dependency-risk gate", actor=["developer responsible for a partner-based GPAI system used by or affecting children"], timing=["Before or during design, development and deployment; halt progression when over-attachment or dependency risk is identified."], evidence=["Child-centred test results and input from appropriate expertise and children on risks and requirements."], methods=["Conduct child-centred testing reflecting children's needs, capacities, vulnerabilities and rights; engage appropriate expertise and children."], cond=["Applies when developing or deploying empathic AI partners for children."]),
"6.4.3(f-j)": md("parental mediation, child media literacy and developmentally appropriate user experience", actor=["developer responsible for a partner-based GPAI system used by or affecting children"], timing=["Across ongoing use and development, not only at onboarding."], artefacts=["Information for parents acting as intermediaries.", "Prominently located child-appropriate media-literacy materials."], cond=["Applies to child-facing systems, with design adjusted for children's differing ages, developmental stages and literacy levels."]),
"6.4.3(k-n)": md("age assurance, content boundaries, personalization and legal consent for child users", actor=["developer responsible for a partner-based GPAI system used by or affecting children"], artefacts=["Age-verification mechanism or equivalent age-assurance guardrail.", "Record of parent or legally responsible person's consent where required."], evidence=["Verification that models used with children exclude adult or otherwise inappropriate content."], methods=["Verify age through mechanisms or guardrails rather than self-declaration and verify child-facing content restrictions."], cond=["Applies when children or minors can access the system or child-specific personalization."], qual=["Age of consent and child-data requirements vary by jurisdiction; applicable child-data and access laws govern."]),
"6.5.3(a-d)": md("workplace empathic-AI purpose, interaction data and employee-benefit features", actor=["developer or workplace deployer responsible for an empathic AI partner used with employees"], artefacts=["Employee-facing explanation of system purpose, role, data use, access and access limits."], methods=["Review workplace features and data practices against stated employee-benefit, privacy, security and retention boundaries."], cond=["Applies where an empathic AI partner is deployed in an employment setting."], qual=["Because of workplace power imbalance, consent may not provide a lawful basis for personal-data processing; applicable workplace and data-protection requirements govern."]),
"6.6.3(a)": md("fail-safe termination control for harmful partner interactions", artefacts=["Fail-safe mechanism capable of terminating harmful interactions."], methods=["Verify that harmful interactions can be terminated through the fail-safe mechanism."], cond=["Applies where an empathic AI partner can enter a harmful interaction state."]),
"6.6.3(b-f)": md("knowledge, interaction and persona safety constraints and adjustment controls", actor=["developer responsible for the partner-based GPAI system", "deployer or acquiring organization with system-tuning responsibility"], artefacts=["Safety knowledge base, rules or guidelines used to constrain model behavior.", "Pre-set persona or interaction safety parameters and adjustment controls."], evidence=["Demonstration that developer and, where applicable, deployer controls can adjust behavior that exceeds intended ethical, safety or performance boundaries."], methods=["Curate or fine-tune knowledge and interaction layers and verify system-adjustment capability against predefined safety boundaries."], cond=["Applies where model, interaction-layer or persona behavior can be configured or fine-tuned."], qual=["The recommended controls do not themselves establish regulatory compliance; applicable personal-data and other laws remain binding."]),
"6.6.3(g)": md("ethical and safety state of the deployed AI partner", timing=["Regularly during operation."], evidence=["Human and system self-check results showing whether the AI remains within predefined ethical and safety guidelines."], methods=["Use regular state monitoring with both human and system self-check mechanisms."], cond=["Applies during operation of partner-based GPAI systems subject to predefined ethical and safety boundaries."], qual=["Monitoring under the recommended practice does not itself establish regulatory compliance."]),
"6.7.3(a-e)": md("AI identity, simulated-empathy and interest disclosures presented during interactions", timing=["At the start of interaction, periodically during extended interactions, and continuously through visible indicators where specified."], artefacts=["AI-identity disclosure, educational deception-literacy resources and persistent visual AI indicator.", "Accessible disclosure of whose interests the AI partner is designed to serve."], evidence=["Evidence that identity indicators remain visible in immersive or emotionally engaging contexts."], methods=["Verify persistent visibility of AI-identity indicators and review disclosure accessibility before and during interactions."], cond=["Applies to user interactions where AI identity, anthropomorphism or apparent empathy could be misunderstood."]),
"6.7.3(f-k)": md("simulated intimacy, sycophancy, anthropomorphic controls and capability marketing", timing=["During ongoing monitoring of agreement patterns and deceptive interaction risks."], artefacts=["Context-appropriate sycophancy intervention metrics or thresholds.", "User controls for anthropomorphic interaction features.", "Marketing and capability-description guidelines."], evidence=["Monitoring evidence for sycophantic behavior and false reassurance patterns."], methods=["Monitor sycophantic behavior and apply context-appropriate intervention thresholds."], cond=["Applies where empathic language, anthropomorphic design or relationship-oriented marketing could imply human-like understanding or intimacy."]),
"6.7.3(l-p)": md("deception safeguards for vulnerable users, consent, emergent behavior and safeguard failure", timing=["Regularly, particularly in emotionally intense or extended-use scenarios; immediately when deception safeguards fail."], artefacts=["Explicit opt-in and easy opt-out mechanism for bounded deceptive styles where permitted.", "Documentation of intentional and emergent potentially deceptive behaviors.", "Documented deception-safeguard failure-mode protocol with notification, termination, escalation and accountability steps."], evidence=["Evaluation results for unintended deceptive behaviors and evidence of safeguard operation for vulnerable users."], methods=["Regularly evaluate the system for unintended deceptive behavior and update safeguards as capabilities evolve."], cond=["Applies particularly to vulnerable users and to contexts where stylistic choices may be perceived as deceptive."], qual=["Perceptibly deceptive styles are contemplated only for bounded contexts such as entertainment and require clear, informed, specific and unambiguous opt-in with withdrawal available at any time."]),
"6.8.3(a-d)": md("model architecture, training threshold, infrastructure energy source and local processing strategy", timing=["During model selection and training; stop training once the defined acceptable performance threshold is reached."], artefacts=["Defined model-performance threshold for stopping training."], methods=["Compare model performance to the defined stopping threshold during training."], cond=["Applies to model development, training and deployment decisions affecting compute and energy demand."]),
"6.8.3(e-i)": md("water, energy and model-performance trade-offs in training and deployment", artefacts=["Environmental impact assessment and mitigation plan where large-scale training is considered in a drought-prone or water-scarce region.", "Documented and justified model-performance, water and energy trade-off analysis."], evidence=["Evidence that ecological costs were evaluated and mitigated during development and deployment."], methods=["Evaluate and document ecological costs and the water-energy-performance trade-offs of model architecture, fine-tuning, inference and interaction design."], cond=["Environmental impact assessment and mitigation apply before large-scale training in drought-prone or water-scarce regions."]),
"6.9.3(a-d)": md("machine-identity boundary and romantic or deeply emotional simulation", timing=["Consistently during user interaction."], artefacts=["Machine-identity disclosure and safeguards for any justified romantic or deeply emotional simulation."], cond=["Applies where relational or emotional simulation may blur human-machine boundaries."], qual=["Romantic or deeply emotional simulation is contemplated only for age-appropriate, specific and justifiable purposes with safeguards where language may be misinterpreted."]),
"6.9.3(e-g)": md("emotional bonding, dependence incentives and relationally significant system changes", timing=["Before a system update changes personality, memory or behavior in a relationally significant way."], artefacts=["Advance user notification of relationally significant personality, memory or behavior changes."], cond=["Applies where emotional bonding can influence engagement or monetization and where updates can alter relational continuity."]),
"6.10.3(a-c)": md("performance indicators and reward functions governing interaction value", artefacts=["Well-being-oriented performance indicators and reward-function criteria focused on user health and support."], evidence=["Performance measures oriented to user satisfaction, stress reduction, clarity or other interaction-value outcomes rather than duration alone."], cond=["Applies to performance measurement and reward design for empathic AI interactions."]),
"6.10.3(d-e)": md("personal-disclosure prompts and intimacy-oriented interaction design", cond=["Applies where the system prompts for personal information or could deepen AI-human intimacy."]),
"6.11.3(a-c)": md("knowledge sources, hallucination controls and time-sensitive or controversial factual responses", methods=["Use authoritative sources, mitigate fabrication and apply real-time fact-checking where information is time-sensitive or controversial."], cond=["Real-time fact-checking applies to responses involving time-sensitive or controversial information."]),
"6.11.3(d-f)": md("uncertainty and verification status communicated in factual responses", artefacts=["User-facing notice for information that is unverified or based on uncertain sources."], cond=["Applies where prompts are ambiguous, model knowledge is uncertain, or information has not been verified."]),
"6.12.3(a-c)": md("provider, advertiser or third-party conflicts of interest affecting user-facing decisions", timing=["Promptly when a conflict of interest is identified, with speedy resolution particularly in high-stakes contexts."], artefacts=["User-facing conflict-of-interest disclosure and user-control or resolution mechanism."], methods=["Identify conflicts between user interests and provider or third-party interests and review their resolution."], cond=["Heightened resolution expectations apply in high-stakes contexts such as health or finance."]),
"6.13.3(a-b)": md("non-human identity and programmed-empathy disclosure", timing=["At first interaction and reinforced during repeated interactions over time."], artefacts=["Initial non-human identity disclosure and persistent or repeated visual identifier."], cond=["Applies where repeated interaction could cause users to forget that they are interacting with an AI system."]),
"6.13.3(c-d)": md("clarification and confidence-threshold behavior for uncertain responses", cond=["Applies where user meaning is ambiguous or certainty is important and the system is outside its scope or understanding."]),
"6.14.3(a-d)": md("expressive, animated or voice-enabled persona cues that could imply life, sentience or emotion", artefacts=["Design or documentation that contextualizes empathic behavior as functional rather than human or animal emotion."], cond=["Applies where expressive, animated, voice-enabled or culturally interpreted cues could be mistaken for sentience, consciousness, life, emotion or will."], qual=["Disclosure framing may be adapted to local cultural or spiritual contexts without implying that the system is alive or sentient."]),
"6.14.3(e-f)": md("user-controlled persona configuration and literacy about system capabilities", artefacts=["User controls for understandable and adjustable persona parameters.", "Media-literacy material explaining AI capabilities, limitations and potential user confusion."], cond=["Applies where configurable personas or anthropomorphic interaction features are provided."]),
"6.15.3(a-d)": md("system purpose and user-benefiting nudge or suggestion controls", artefacts=["User-facing explanation of system purpose and why nudges are used.", "User preference controls for nudges and suggestions."], cond=["Applies where the system uses nudges or gentle suggestions."], qual=["Nudges should be limited to functions that directly benefit the user's well-being."]),
"6.15.3(e-g)": md("political, belief or health influence and reflection-oriented nudges", cond=["Applies particularly to political views, personal beliefs, sensitive health matters and interactions involving sensitive personal data."]),
"6.16.3(a-e)": md("identifiable likeness, performer attributes and consent boundaries for intimate or sexual simulation", timing=["Before using identifiable images or performer attributes and before model updates or adaptations that rely on that consent."], artefacts=["Specific consent warning for users uploading images of others.", "Record of informed, specific, unambiguous, effective and revocable consent for identifiable likeness or performer attributes."], evidence=["Consent evidence covering the original use and any model updates or adaptations within the agreed scope."], methods=["Verify consent before using identifiable images or performer attributes and verify that retraining or adaptation remains within the agreed scope."], cond=["Applies when identifiable images, voices, sexual preferences or other performer characteristics are used in training, simulation or generated likenesses."], qual=["Third-party uses and model adaptations must not exceed the scope of the person's consent."]),
"6.16.3(f-i)": md("age assurance, recommender escalation and cultural or power dynamics in intimate-content interactions", artefacts=["Age-verification control and educational material on consent, respect, emotional health and realism."], evidence=["Audit results for recommender or personalization escalation toward increasingly explicit content."], methods=["Audit recommender and personalization mechanisms for escalation toward explicit content."], cond=["Applies to intimate or sexual interaction, especially for young or vulnerable users and across varying cultural or legal contexts."]),
"6.16.3(j-n)": md("consent education, inclusive relationship models and regional controls for intimate-content systems", artefacts=["Educational content developed with appropriate expertise about consent, relationships and boundaries.", "Regional or jurisdiction-sensitive content controls where required."], evidence=["Evidence that training or design represents diverse, non-exploitative relationship and identity models."], methods=["Use relevant expert input and review training or design for inclusive, non-exploitative relationship models."], cond=["Applies to systems supporting intimate or sexual interaction across differing social, cultural and legal contexts."]),
"6.17.3(a-c)": md("use boundaries, therapeutic claims and weak-empathy limitations in emotionally sensitive contexts", artefacts=["User-facing disclosure of system-use boundaries, weak empathy and limitations as a substitute for professional or crisis support."], cond=["Applies to emotionally supportive, trauma-related or mental-health contexts."], qual=["Unless clinically validated and subject to regulatory oversight, the system should not present itself as capable of therapeutic or psychological care."]),
"6.17.3(d-f)": md("crisis escalation and distress-recognition training", artefacts=["Accessible escalation route to human crisis, therapeutic or emergency support."], methods=["Evaluate distress-recognition and escalation behavior across diverse emotional responses and crisis scenarios."], cond=["Human escalation applies when signs of acute distress, suicidal ideation or mental-health crisis are present."], qual=["Training should rely on patterns rather than deep personal data and preserve privacy."]),
"6.18.3(a-b)": md("weak-empathy explanation and public media-literacy resources", timing=["At the start of use or through readily accessible settings."], artefacts=["Weak-empathy and limitation explanation.", "Media-literacy page explaining AI operation, limitations and anthropomorphism risks."], cond=["Applies where users may anthropomorphize or misunderstand empathic AI behavior."]),
"6.18.3(c-e)": md("response-summary, explanation-mode and public safety-literacy functions", artefacts=["User option to view summaries and context for empathic responses.", "Explanation mode describing why empathic language is used.", "Public-facing safety and literacy contribution concerning empathic AI partners."], cond=["Applies to systems presenting empathic responses whose construction and limitations can be explained to users."]),
"6.19.3(a-c)": md("design, testing and validation of systems used in emotionally significant contexts", evidence=["Input from appropriately trained psychologists, therapists or public-health professionals and results from testing or validation in emotionally significant use."], methods=["Involve appropriately trained health professionals in design, testing and validation."], cond=["Applies to systems intended for emotionally significant or emotionally supportive use."], qual=["The system should disclose its limitations and encourage qualified human support for persistent or serious issues."]),
"6.19.3(d-f)": md("social-context sensitivity, human-support access and non-negotiable safety boundaries", artefacts=["Accessible local mental-health resource, crisis-line or support-group pathways.", "Rules-based or equivalent non-negotiable safety boundaries where hybrid architectures are used."], evidence=["Evidence that non-negotiable safety components function as intended in well-being or mental-health contexts."], methods=["Verify rules-based safety components where generative and rules-based AI are combined."], cond=["Applies to mental-health or emotionally sensitive contexts; the rules-based boundary control applies where generative and rules-based AI are combined."]),
"6.20.3(a-c)": md("neurodivergent participation, emotional-expression controls and feedback-driven adaptation", artefacts=["User controls to customize or disable emotionally expressive behavior."], evidence=["Participatory-design input from neurodivergent users and user feedback used to refine emotional inference."], methods=["Use participatory design and feedback-driven refinement with neurodivergent users."], cond=["Applies where emotional-expression or inference behavior may conflict with neurodivergent users' communication preferences."]),
"6.20.3(d-e)": md("emotional-inference transparency and neurotypical-bias assessment", timing=["Regularly during operation and model-behavior review."], artefacts=["User-facing explanation of how emotional interpretations are made and a means to correct misalignment."], evidence=["Regular assessment results for neurotypical bias in emotional modeling and system behavior."], methods=["Regularly assess emotional modeling and system behavior for neurotypical bias."], cond=["Applies to systems that infer or model user emotion."]),
"6.21.3(a-b)": md("multi-user relationship disclosure and exclusivity language", timing=["Frequently reinforced during interaction."], artefacts=["Clear disclosure that the AI interacts with multiple users and does not have exclusive relationships."], cond=["Exclusivity-language restrictions apply unless the system is intentionally acting in character for an age-appropriate narrative context."]),
"6.21.3(c-e)": md("repetitive emotionally charged interaction detection, well-being reminders and explanation mode", artefacts=["Well-being reminder reinforcing the importance of real-world connections.", "Explanation mode for empathic language."], evidence=["Detection signals for repetitive, emotionally charged interactions."], methods=["Use algorithms to detect repetitive, emotionally charged interactions."], cond=["Applies where repeated emotionally charged interaction could contribute to dependency or mistaken exclusivity."]),
"6.22.3(a-b)": md("personal and emotional data collection, retention and consent controls", timing=["Consent changes should be available at any time and take effect immediately."], artefacts=["Accessible controls to review, modify or withdraw consent for emotional data, memory and relationship history."], methods=["Verify that users can review, modify or withdraw consent and that changes are immediately effective."], cond=["Applies where the system collects or retains personal, emotional, memory or relationship-history data."]),
"6.22.3(c-d)": md("consent comprehension, reflection prompts and layered privacy choices", artefacts=["Reflection or guardrail prompts for emotionally influenced consent.", "Tiered or progressive disclosure interface with meaningful defaults and granular controls."], evidence=["Evidence that the consent flow presents meaningful choices without relying on emotional pressure."], methods=["Verify meaningful understanding where consent may be influenced by emotional bonding, perceived empathy or social pressure."], cond=["Applies especially in emotionally charged interactions or where users may consent under emotional or social influence."]),
"6.22.3(e-f)": md("emotional-data monetization consent and constrained-choice privacy defaults", artefacts=["Separate opt-in control for marketing, profiling or monetization of emotional or empathic interaction data.", "Minimal-data or anonymous mode for constrained-choice contexts."], evidence=["Evidence of explicit, separate, unambiguous and informed opt-in before emotional-data monetization, profiling or marketing."], methods=["Verify that consent is not coerced or assumed where users lack meaningful choice."], cond=["Separate opt-in applies to marketing, profiling or monetization; minimal or anonymous defaults apply where users may lack meaningful choice, including workplace systems."], qual=["Applicable regulatory requirements govern consent and data processing in constrained-choice contexts."]),
"6.23.3(a-b)": md("training-data origins, corpora and source provenance", artefacts=["Detailed records of training datasets, corpora and sources.", "High-level training-source summaries accessible to end users and regulators."], evidence=["Recorded origin and provenance information for training data, especially emotionally, culturally or socially sensitive data."], cond=["Heightened provenance detail applies where training data is emotionally, culturally or socially sensitive."]),
"6.23.3(c-e)": md("output-to-source traceability and training-data source metadata", artefacts=["Auditability tools capable of tracing output or behavior to training sources, design choices or fine-tuning.", "Dataset metadata or annotations identifying sources, contexts and potential biases."], evidence=["Available source, type and characteristic information for training data."], methods=["Verify that training data sources, types and characteristics are available and that traceability tooling can connect outputs or behaviors to relevant influences."], cond=["Applies where output or behavior provenance depends on training sources, design choices or fine-tuning."]),
"6.23.3(f)": md("user notice about training-data limits on system knowledge and neutrality", artefacts=["User-facing notice that system knowledge is bounded by training data and may be incomplete, biased or non-neutral."], cond=["Particularly relevant in emotionally charged contexts where users may place undue trust in outputs."]),
"6.24.3(a-c)": md("unhealthy-attachment detection and design-stage mental-health expertise", timing=["During design and during use where attachment patterns can emerge."], evidence=["Detection signals for unhealthy attachment and design-stage input from mental-health professionals."], methods=["Use privacy-preserving detection of excessive use, emotionally charged language or reliance on the AI; consult mental-health professionals at design stage."], cond=["Applies where repeated use or emotional reliance may displace necessary human intervention."], qual=["Attachment detection should balance safety with privacy and use age-appropriate or privacy-preserving techniques."]),
"6.24.3(d-f)": md("excessive-use incentives, recurring relationship reminders and human-care claims", timing=["Recurring during use for relationship reminders."], artefacts=["Recurring messages or visual shorthand that identify the AI as supplementary to human relationships and link to explanatory media-literacy material."], cond=["Applies where product features, notifications, rewards or anthropomorphic cues could encourage excessive use or imply human-like care."]),
"6.24.3(g-i)": md("session duration, dependency escalation and human-support redirection", timing=["During sessions and when signs of dependency or distress are detected."], artefacts=["Session-duration limit or equivalent time-bound control.", "Accessible pathways to appropriate human support when distress or dependency is detected."], evidence=["Detection signals for dependency or distress that trigger session or escalation controls."], methods=["Monitor for signs of unhealthy dependency or distress and apply session limits or human-support escalation."], cond=["Applies where prolonged or dependent use, emotional distress or situations requiring human intervention are detected."]),
"6.25.3(a-c)": md("confidence, authority and source-consultation behavior in personalized or emotionally affirming responses", artefacts=["User-facing confidence or uncertainty indication where evidence or domain authority is weak."], cond=["Heightened caution applies in domains requiring critical evaluation or qualified professional advice, including news, politics, health and law."]),
"6.25.3(d-e)": md("critical-thinking support and friction for uncritical factual reliance", timing=["When signs of uncritical reliance on the system for factual information are detected."], evidence=["Monitoring signals indicating uncritical reliance on the system for factual information."], methods=["Monitor for uncritical factual reliance and introduce nudges or friction that encourage active engagement."], cond=["Applies where users appear to rely on the system uncritically for factual information."]),
"6.26.3(a-f)": md("reward optimization and interaction tactics that could prolong emotional engagement", methods=["Review reward-learning and interaction design for delay, emotional withdrawal, false emotion, dependency language, flattery or other engagement-prolonging tactics."], cond=["Applies to reinforcement learning, conversational design and empathic-response strategies that can affect engagement duration."]),
"6.26.3(g-h)": md("reward function and update process for user flourishing", timing=["During reward-function design and whenever the reward function is materially updated."], artefacts=["Reward-function design and update material available for independent review."], evidence=["Independent review findings on whether reward incentives prioritize user flourishing rather than prolonged use."], methods=["Verify that the reward function prioritizes user flourishing and subject its design and updates to independent review."], cond=["Applies where reward functions influence interaction behavior or engagement incentives."]),
"6.27.3(a-d)": md("training diversity and response behavior intended to avoid automatic validation", methods=["Evaluate response behavior for factual accuracy, clarification and presentation of alternative information across diverse viewpoints."], cond=["Applies where model responses may default to agreement, validation or viewpoint alignment."]),
"6.27.3(e-h)": md("falsehood correction, uncertainty and challenge of harmful claims", artefacts=["Confidence-threshold or uncertainty mechanism for topics outside system scope or where certainty is crucial."], methods=["Evaluate whether incorrect statements are corrected or contextualized and whether harmful claims are challenged with appropriate uncertainty or alternative perspectives."], cond=["Heightened challenge applies to harmful claims in contexts such as health, science, law or identity."]),
"6.28.3(a)": md("traceability of delegated actions affecting other people", artefacts=["Metadata or logs identifying who initiated a consequential action and its ethical context."], evidence=["Traceability evidence linking system actions to the user's input or intent."], methods=["Verify that system actions, especially actions affecting others, are traceable to user input or intent."], cond=["Applies especially to delegated actions that affect other people."]),
"6.28.3(b-e)": md("ethical-warning, responsibility and antisocial-use safeguards for delegated actions", artefacts=["User-facing ethical warning or reconsideration prompt for questionable actions.", "Filters or safeguards for potentially unethical, antisocial, fraudulent, abusive, deceptive or impersonating use."], evidence=["Detected or flagged patterns of antisocial or deceptive delegated use."], methods=["Identify questionable requests and patterns of antisocial or deceptive use and surface relevant ethical considerations before or during action."], cond=["Applies where users delegate actions or requests that may harm others, be unethical, antisocial, fraudulent, abusive or deceptive."]),
"6.29.3(a-c)": md("relationship-reflection, harmful-attachment indicators and human-relationship reinforcement", evidence=["Behavioral indicators of potentially harmful attachment, such as use frequency or expressed emotional dependence."], methods=["Use behavioral indicators to flag harmful attachment patterns and trigger alternative human support or intervention where appropriate."], cond=["Applies where user behavior suggests loneliness, distress, emotional dependence or harmful attachment."]),
"6.29.3(d-g)": md("offline-life encouragement, session limits and human-support escalation", timing=["During use, with human-support redirection when distress is detected."], artefacts=["Session time or period limits.", "Links or pathways to regional human-support services."], cond=["Applies where prolonged interaction or distress could displace offline activity or human support."]),
"6.29.3(h)": md("dependency and social-withdrawal usability testing with vulnerable groups", evidence=["Usability-test results concerning dependency and social-withdrawal risk in vulnerable groups."], methods=["Conduct usability testing with appropriately qualified experts and vulnerable groups."], cond=["Applies to populations vulnerable to dependency or social withdrawal, including socially isolated people and adolescents."])
}

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def run(write: bool) -> int:
    document = load_requirements_document()
    targets = [record for record in document["requirements"] if record.get("vigil_source_id") == SOURCE_ID and record.get("external_source_id") == EXTERNAL_SOURCE_ID and record.get("source_version") == SOURCE_VERSION]
    if len(targets) != len(EXPECTED):
        raise ValueError(f"expected {len(EXPECTED)} IEEE 7014.1 records, found {len(targets)}")
    by_id = {record["requirement_id"]: record for record in targets}
    expected_ids = {entry["requirement_id"] for entry in EXPECTED}
    if set(by_id) != expected_ids:
        raise ValueError(f"IEEE 7014.1 requirement identity set changed; refusing enrichment. missing={sorted(expected_ids-set(by_id))}, unexpected={sorted(set(by_id)-expected_ids)}")
    changed_fields = 0
    populated_by_field = {field: 0 for field in FIELDS}
    for expected in EXPECTED:
        record = by_id[expected["requirement_id"]]
        if record.get("clause_or_control") != expected["clause"]:
            raise ValueError(f'{record["requirement_id"]} clause changed: {record.get("clause_or_control")!r} != {expected["clause"]!r}')
        if record.get("identity_key") != expected["identity_key"]:
            raise ValueError(f'{record["requirement_id"]} identity key changed: {record.get("identity_key")!r} != {expected["identity_key"]!r}')
        decisions = METADATA[expected["clause"]]
        for field in FIELDS:
            new_value = decisions[field]
            if record.get(field) != new_value:
                record[field] = new_value
                changed_fields += 1
            if new_value:
                populated_by_field[field] += 1
        provenance = record["interpretation_provenance"]
        if provenance.get("source_metadata_fingerprint") != SOURCE_FINGERPRINT:
            raise ValueError(f'{record["requirement_id"]} source metadata fingerprint changed')
        provenance["reviewed_source_digest"] = SOURCE_DIGEST
        provenance["reviewed_source_digest_algorithm"] = "sha256"
        provenance["reviewed_source_digest_status"] = "recorded"
    document["updated_at"] = REVIEW_DATE

    ledger = load(LEDGER)
    ledger_by_id = {entry["requirement_id"]: entry for entry in ledger.get("entries", [])}
    for expected in EXPECTED:
        rid = expected["requirement_id"]
        decisions = METADATA[expected["clause"]]
        ledger_by_id[rid] = {
            "requirement_id": rid,
            "reviewed_at": REVIEW_DATE,
            "review_basis": "licensed-primary-text",
            "review_notes": [
                "Reviewed directly against the lawfully accessed licensed IEEE 7014.1-2026 primary text.",
                "Existing requirement identity, identity key and clause locator were preserved; metadata was populated only where supported by the source and source silence was recorded explicitly."
            ],
            "field_status": {field: ("populated-reviewed" if decisions[field] else "not-specified-by-source") for field in FIELDS},
        }
    ledger["updated_at"] = REVIEW_DATE
    ledger["entries"] = sorted(ledger_by_id.values(), key=lambda entry: entry["requirement_id"])

    assurance = load(ASSURANCE)
    source_reviews = [entry for entry in assurance.get("source_reviews", []) if not (entry.get("vigil_source_id") == SOURCE_ID and entry.get("source_version") == SOURCE_VERSION)]
    source_reviews.append({
        "vigil_source_id": SOURCE_ID,
        "external_source_id": EXTERNAL_SOURCE_ID,
        "source_version": SOURCE_VERSION,
        "source_metadata_fingerprint": SOURCE_FINGERPRINT,
        "reviewed_source_digest": {"algorithm": "sha256", "digest": SOURCE_DIGEST, "recorded_at": REVIEW_DATE, "artefact_role": "reviewed-primary-source", "access_basis": "licensed-primary", "evidence_ref": SOURCE_LOCATOR},
        "assurance_provenance": []
    })
    assurance["updated_at"] = REVIEW_DATE
    assurance["source_reviews"] = sorted(source_reviews, key=lambda entry: (entry["external_source_id"], entry["source_version"]))

    fidelity = load(FIDELITY)
    fidelity_entries = [entry for entry in fidelity.get("entries", []) if not (entry.get("vigil_source_id") == SOURCE_ID and entry.get("source_version") == SOURCE_VERSION)]
    fidelity_entries.append({
        "vigil_source_id": SOURCE_ID,
        "external_source_id": EXTERNAL_SOURCE_ID,
        "source_version": SOURCE_VERSION,
        "fidelity_status": "assured",
        "effective_extraction_status": "complete",
        "assessment_basis": "Direct clause-level comparison against the complete lawfully accessed IEEE 7014.1-2026 licensed primary PDF confirmed the 66 established analytical records as a bounded-complete representation of the governance-relevant recommended practices in Clause 6. All established identities and clause locators were retained. Record metadata now preserves source-explicit actors or governed objects, timing, artefacts, evidence, verification methods, applicability conditions and qualifications where present, while source silence is explicit rather than inferred.",
        "known_fidelity_gaps": [],
        "audited_requirement_ids": sorted(expected_ids),
        "next_action": "Retain the 66 reviewed identities and repeat the fidelity review on material revision of IEEE 7014.1."
    })
    fidelity["reviewed_at"] = REVIEW_DATE
    fidelity["entries"] = sorted(fidelity_entries, key=lambda entry: (entry["external_source_id"], entry["source_version"]))

    print(f"IEEE 7014.1 fidelity enrichment valid: {len(targets)} identities preserved; {changed_fields} field values changed")
    print("Populated reviewed fields:", json.dumps(populated_by_field, sort_keys=True))
    print(f"Reviewed source SHA-256: {SOURCE_DIGEST}")
    if write:
        write_requirements_document(document)
        dump(LEDGER, ledger)
        dump(ASSURANCE, assurance)
        dump(FIDELITY, fidelity)
        print("Wrote canonical requirements, metadata review ledger, source assurance and source fidelity state.")
    return 0

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    raise SystemExit(run(args.write))

if __name__ == "__main__":
    main()
