#!/usr/bin/env python3
from __future__ import annotations
import copy, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / 'external_governance' / 'requirements'
SHARD = REQ / 'requirements' / 'IEEE-7014' / '2024.json'
LEDGER = REQ / 'metadata-review.json'
ASSURANCE = REQ / 'source-review-assurance.json'
FIDELITY = REQ / 'source-fidelity.json'
SCOPE = REQ / 'source-scope.json'
DATE = '2026-09-03'
SOURCE_ID = 'EXT-8D54F96680C4'
EXTERNAL_ID = 'IEEE-7014'
VERSION = '2024'
FINGERPRINT = '25c22e8e007b7acbe5cd0111c5828088f0b005dc2c671f0e2f5882afcc2865ab'
DIGEST = '237d4d782aabf0585170e0eef8d0f313fc353b8f90cd4f94a2db0d993c45c43b'
LOCATOR = 'https://standards.ieee.org/ieee/7014/7648/'
FIELDS = (
    'applicable_actor','governed_object','timing_or_frequency','required_artefacts',
    'evidence_expectation','verification_method','applicability_conditions','exceptions_or_qualifications'
)

ESTABLISHED_IDS = {
    "EXTREQ-02D226AB756E319A", "EXTREQ-0EC62DE00B448D8E", "EXTREQ-0EF26D6D174C2DCE",
    "EXTREQ-23EE57392E75BFB8", "EXTREQ-29B0D0B21F7E80D4", "EXTREQ-34FD56083CEA645E",
    "EXTREQ-38FD0063E98199E9", "EXTREQ-3DF5DD271DC23C92", "EXTREQ-3E6D02A72B66B9DC",
    "EXTREQ-42A1CFE7EF635572", "EXTREQ-4AFD90EB3C518B5F", "EXTREQ-55CAAB7FB9174CAF",
    "EXTREQ-62877173BD54BD9E", "EXTREQ-64E9E595CFF7DE6A", "EXTREQ-65D7E193EE4A942B",
    "EXTREQ-68B1E8EF3CF94A5C", "EXTREQ-6DC66967479E1698", "EXTREQ-6E38B5BF78558873",
    "EXTREQ-7033840016B023BC", "EXTREQ-719786837E5A6D9B", "EXTREQ-71E4BCCCB69D1E91",
    "EXTREQ-7C34BE7150B572DA", "EXTREQ-8C7DA8D83414FF85", "EXTREQ-915C1C74C7E78C60",
    "EXTREQ-9CB430C2CA057762", "EXTREQ-AAD0CB1FB151574D", "EXTREQ-B197A3D8996165B7",
    "EXTREQ-B8D7C1A87AFB24C8", "EXTREQ-BF238AD2E0373C07", "EXTREQ-C1CBAA44088FE2A3",
    "EXTREQ-CD5CDF96299089DE", "EXTREQ-D57F5E807D837AF8", "EXTREQ-D62D5EEFA80787DA",
    "EXTREQ-D7520BF14ED60A9B", "EXTREQ-D8BDF2032891259A", "EXTREQ-E20773A941B61CD4",
    "EXTREQ-E673B76B9E79C2FA", "EXTREQ-E7923A307C756F51", "EXTREQ-EBAA17D768C656E2",
    "EXTREQ-ED9ECFAF64B12C73", "EXTREQ-F0346554861A7BF3",
}

def req_id(clause: str, identity: str) -> str:
    seed = '|'.join((SOURCE_ID, VERSION, clause.strip(), identity.strip()))
    return 'EXTREQ-' + hashlib.sha256(seed.encode()).hexdigest()[:16].upper()

def dump(path: Path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

NEW = [
    ('4.1.1.2(c-d)', '7014-continuous-learning-collaboration', 'Maintain continuing education on the wider empathic-AI context and foster continuous learning and collaboration with specialists and affected stakeholders.', '7014-skills-and-learning-evidence'),
    ('4.2.1.2(a-c)', '7014-wia-method-conflict-independent-review', 'Use a recognized well-being impact assessment process, assess stakeholder hierarchy conflicts, and use third-party assessment or peer review.', '7014-published-wellbeing-impact-assessment'),
    ('4.2.2.2(j)', '7014-third-party-risk-assessment', 'Use a qualified third party for risk, issue and impact assessment where possible.', '7014-eais-risk-assessment'),
    ('4.2.2.2(k-m)', '7014-personalized-bias-aware-risk-interaction', 'Personalize system behavior to subject circumstances and risk tolerance, help identify cognitive biases, and use human-like communication where possible to improve risk management.', '7014-monitor-mitigate-ethical-cultural-risk'),
    ('4.2.3.1', '7014-explainability-replicability', 'As far as possible, make explainability documentation support replication of system outputs for testing by appropriate parties.', '7014-publish-required-materials'),
    ('4.2.3.2(i)', '7014-expanded-transparency-explanations', 'Publish explanations of system capabilities and limitations, data, inputs and outputs, transformations, purpose fit, theoretical frameworks, affective models, and decision rationale.', '7014-publish-required-materials'),
    ('4.2.3.2(j)', '7014-ethical-explainability-approach-justification', 'Use ethical-explainability documentation to describe main design, build and operation approaches, their possible implications, and why each approach is ethically justified.', '7014-ethical-purpose-and-scope-explanation'),
    ('4.2.4.2(d-e)', '7014-diverse-affective-data-sourcing-labeling', 'Use diverse affective data sources and labels that accurately reflect the perspectives and experiences of the people who provided the data.', '7014-diverse-validated-clean-data'),
    ('4.2.4.2(f-g)', '7014-subject-data-control-inference-access', 'Give subjects controls over data processing and system intervention and facilities to access and securely share inferences and decisions made about them.', '7014-ethical-data-origin'),
    ('4.2.4.2(h-j)', '7014-human-oversight-calibration-representation', 'Provide qualified human oversight, subject calibration, and a competent representative where a subject may lack adequate mental capacity.', '7014-ethical-data-origin'),
    ('4.2.5.2(d-e)', '7014-bias-identification-mitigation', 'Make reasonable efforts to identify, record and reduce potential bias and use methods or tools for checking and mitigating bias.', '7014-affective-rights-bias-context'),
    ('4.2.5.2(f-g)', '7014-contextual-adaptation', 'Include contextual factors in system functioning and adapt to contextual variations that can affect affective interpretation and interaction.', '7014-affective-rights-bias-context'),
    ('4.2.6.1(f)', '7014-post-production-quality-monitoring', 'Account for adaptive learning and training in quality assurance and monitor the EA/IS after it enters production.', '7014-quality-performance-claims'),
    ('4.3.1.2(d-f)', '7014-subject-primacy-vulnerable-default-human-centered', 'Give subjects primacy where possible, treat vulnerable parties as part of the default audience unless formally restricted otherwise, and apply a human-centered lifecycle approach.', '7014-stakeholder-research-publication'),
    ('4.3.2.2 (post-p)', '7014-consent-service-non-withholding', 'Where possible, do not unduly withhold service solely because a subject chooses not to provide, or fails to provide, effective informed consent.', '7014-active-bounded-consent-record'),
    ('4.3.4.2(d-e)', '7014-training-data-quality-modality-diversity', 'Use high-quality recognized third-party affective datasets and multiple data modes when doing so is likely to improve system quality and robustness.', '7014-training-method-diversity-feedback'),
    ('4.3.5.2 (post-f)', '7014-subject-intimacy-obtrusiveness-calibration', 'Where possible, let subjects calibrate the degree of intimacy and obtrusiveness of system behavior.', '7014-affective-model-documentation'),
    ('4.3.6.2(e-g)', '7014-independent-realtime-human-monitoring', 'Use qualified third-party assessment and auditing, monitor as close to real time as feasible, and provide human oversight and intervention where required.', '7014-ongoing-monitoring'),
]

META = {
'7014-affective-data-expiry': dict(timing_or_frequency=['At the expiry date specified by the system data-retention policy.'], required_artefacts=['The system data-retention policy and plan governing affective data.'], applicability_conditions=['Applies to affective data governed by the system data-retention policy.']),
'7014-purpose-limited-affective-data': dict(timing_or_frequency=['Obtain additional permission before reusing affective data for a new purpose.'], required_artefacts=['Records of informed consent or additional permission for the intended use of affective data.'], evidence_expectation=['The stated intended use and consent basis for affective-data use or reuse.'], applicability_conditions=['Applies to acquisition, use or reuse of affective data.'], exceptions_or_qualifications=['General-use permission is not acceptable.', 'Affective data is not to be acquired or used for purposes that can foreseeably harm subjects, discriminate against them, or violate privacy or rights.']),
'7014-publish-required-materials': dict(timing_or_frequency=['Publish required materials before deployment where possible and update them at a reasonable frequency throughout the system life cycle.'], required_artefacts=['Published outcomes and materials required elsewhere by IEEE 7014-2024.', 'Published justification where the audience for required materials is limited.'], evidence_expectation=['Required outcomes made readily accessible to all relevant stakeholders to an appropriate extent.'], applicability_conditions=['Applies wherever IEEE 7014-2024 states that an activity or outcome is to be published.'], exceptions_or_qualifications=['Public access may be limited if the developer publishes a justification for the narrower audience.', 'Pre-deployment publication is required where possible.']),
'7014-data-management-plan': dict(required_artefacts=['Published data-management plan.'], evidence_expectation=['The published data-management plan.']),
'7014-no-unconsented-transfer-or-conditioning': dict(timing_or_frequency=['Obtain prior or revised informed consent before transferring affective data outside the existing consent scope.'], required_artefacts=['Records of prior or revised informed consent for affective-data transfer or sharing.'], applicability_conditions=['Applies to subject affective data and access by internal or external third parties.']),
'7014-lifecycle-risk-renewal': dict(timing_or_frequency=['Renew assessments at each feasible life-cycle stage and at appropriate intervals, or annually.'], required_artefacts=['Updated risk, issue and impact assessments.'], evidence_expectation=['Renewed assessment results covering the relevant life-cycle stage or interval.'], verification_method=['Repeat the risk, issue and impact assessment at the specified life-cycle stages or intervals.']),
'7014-predeployment-decommission-plan': dict(timing_or_frequency=['Publish the decommission and disposal plan before deployment.'], required_artefacts=['Published decommission and disposal plan covering methods, foreseeable impacts and reasonable harm-reduction measures.'], evidence_expectation=['The published plan and its stated treatment of personal, societal, environmental, security and compliance impacts.']),
'7014-lifecycle-bom': dict(timing_or_frequency=['Conduct and publish the bill of materials before deployment and maintain it throughout the system life cycle.'], required_artefacts=['Published bill of materials covering hardware, software and data components and dependencies.'], evidence_expectation=['A current published bill of materials maintained through the system life cycle.']),
'7014-affective-data-source-volume-publication': dict(required_artefacts=['Published explanation of affective-data sources, acquisition methods, volume, types and range.'], evidence_expectation=['The published data-acquisition explanation.']),
'7014-monitoring-feedback-and-restoration': dict(timing_or_frequency=['Engage stakeholders for feedback on ongoing system performance and issues.', 'Publish the restoration procedure and expected restoration time for a service incident or detected issue that could affect subjects.'], required_artefacts=['Published restoration procedure and expected restoration time.'], evidence_expectation=['Stakeholder feedback concerning ongoing system performance and issues.'], applicability_conditions=['The restoration procedure applies following a service incident or detection of an issue that could impact subjects.']),
'7014-monitoring-plan-results-publication': dict(timing_or_frequency=['Publish the monitoring plan and ongoing results during system operation.'], required_artefacts=['Published monitoring plan and ongoing monitoring results, including model metrics, coverage gaps, production-readiness methods and empathic-context monitoring.'], evidence_expectation=['Ongoing monitoring results and performance metrics for each model.'], verification_method=['Use model performance metrics, monitoring coverage and gap analysis, and production-readiness checks described by the monitoring plan.']),
'7014-signed-conformity-statement': dict(timing_or_frequency=['Publish on completion.'], required_artefacts=['Signed statement of conformity to IEEE 7014-2024.'], evidence_expectation=['The signed conformity statement.']),
'7014-ethical-data-origin': dict(evidence_expectation=['Evidence that affective data was ethically obtained and that data subjects are adequately protected.'], verification_method=['Review the basis of data acquisition and protections such as informed consent and anonymization.'], applicability_conditions=['Applies to affective data used by the EA/IS.']),
'7014-affective-model-documentation': dict(required_artefacts=['Published explanation of model-design and use methods and frameworks, modeled affect types, supporting validation and ranges of validity.'], evidence_expectation=['Supporting validation for the model methods and stated validity ranges.'], verification_method=['Validate the model methods and frameworks within their stated ranges of validity.']),
'7014-model-context-and-stakeholder-validation': dict(evidence_expectation=['Results of consistency analysis across foreseeable contexts and effectiveness analysis using representative relevant stakeholders.'], verification_method=['Analyze model consistency across all foreseeable contexts of use.', 'Analyze model effectiveness with a representative sample of all relevant stakeholders.'], applicability_conditions=['Applies across all foreseeable contexts of use and to the relevant stakeholder population.']),
'7014-inference-and-simulation-labels': dict(required_artefacts=['Stakeholder-facing labels or information identifying affective inferences and simulated affect.'], evidence_expectation=['Information provided to potentially affected stakeholders about affective estimates and simulated affect.'], applicability_conditions=['Inference labeling applies when the system makes affective inferences.', 'Simulation disclosure applies when the system simulates affect.'], exceptions_or_qualifications=['Affective inferences are to be presented as estimates rather than truth.', 'Simulated affect is to be identified as a trained or logical response rather than actual emotional expression.', 'For systems designed to operate on groups, notice to the group is recommended.']),
'7014-diverse-validated-clean-data': dict(timing_or_frequency=['Cleanse identifiable affective-data issues frequently and thoroughly.'], evidence_expectation=['Results demonstrating affective-data validation for the intended population and correction of identifiable data issues.'], verification_method=['Validate affective data for representativeness of the intended population.', 'Review and correct identifiable affective-data issues frequently and thoroughly.'], applicability_conditions=['Applies to affective data intended for interaction with a defined population.']),
'7014-safety-test-publication': dict(required_artefacts=['Published safety-test documentation and comprehensive outcomes report.'], evidence_expectation=['Results of safety testing, including robustness and resilience testing against potential vulnerabilities.'], verification_method=['Conduct safety testing such as response to additive random noise or targeted adversarial attacks and report the outcomes.']),
'7014-no-modeling-without-consent': dict(timing_or_frequency=['Obtain prior informed consent before applying affective modeling to identifiable subject affective data.'], required_artefacts=['Record of prior informed consent for affective modeling.'], applicability_conditions=['Applies when affective modeling is applied to subject affective data.'], exceptions_or_qualifications=['Anonymous affective data is excluded from this consent requirement.']),
'7014-quality-performance-claims': dict(required_artefacts=['Published quality, performance, effectiveness and fitness-for-purpose methods and results.', 'Published evidence of performance at the stated purpose in real or realistic contexts.'], evidence_expectation=['Measurement results and evidence supporting stated system performance and any probabilistic claims.'], verification_method=['Measure quality, performance, effectiveness and fitness-for-purpose using appropriate standard methods and metrics.', 'Evaluate performance at the stated purpose in real or realistic contexts.'], applicability_conditions=['Additional proportionality explanation applies if the developer makes an accuracy claim.'], exceptions_or_qualifications=['Use probabilistic measurements such as confidence, certainty or error rather than overstated accuracy claims where appropriate.']),
'7014-consent-withdrawal-and-data-access': dict(timing_or_frequency=['Allow a subject to reclaim their consent license at any time during the system life cycle.'], required_artefacts=['Affective-data use log made available with retrieved subject data.'], evidence_expectation=['Evidence that consent withdrawal and data retrieval facilities are available to subjects.'], applicability_conditions=['Applies to subject affective data and associated informed-consent licenses.'], exceptions_or_qualifications=['Consent withdrawal is not required after data has been generalized or anonymized to the extent that removal is practically infeasible.', 'Data retrieval need not be provided where the developer can demonstrate that retrieval is infeasible or inappropriate.']),
'7014-third-party-disclosure-no-dark-patterns': dict(required_artefacts=['Information identifying relevant third parties that may receive affective data or influence system behavior.'], evidence_expectation=['The third-party disclosure provided to subjects.'], applicability_conditions=['Applies where third parties can be party to affective data or influence system behavior.'], exceptions_or_qualifications=['Deceptive or coercive design patterns are prohibited for influencing subject choices about the system.']),
'7014-published-wellbeing-impact-assessment': dict(required_artefacts=['Published well-being impact assessment.'], evidence_expectation=['Assessment demonstrating the system contribution to subject and affected-stakeholder well-being and, where relevant, wider human flourishing.'], verification_method=['Conduct a well-being impact assessment.'], applicability_conditions=['The assessment covers the subject, other affected stakeholders and wider human well-being where relevant.']),
'7014-affective-data-retention-plan': dict(required_artefacts=['Published data-retention policy and plan for sensitive data, including protection/security, privacy or anonymization, restricted access, deletion arrangements and intended-use definition.'], evidence_expectation=['The published retention policy and plan.'], timing_or_frequency=['Support automatic deletion of affective data based on a preset time period at the request of the subject.'], applicability_conditions=['Applies to sensitive affective data such as personal health data or personally identifiable information.']),
'7014-emulated-empathy-disclosure': dict(timing_or_frequency=['Provide disclosure at a reasonable timeframe and frequency and, where possible, at the point of system use.'], required_artefacts=['Notification, label or accompanying documentation disclosing EA/IS use and the nature of the affective technology.'], evidence_expectation=['Stakeholder-facing disclosure of EA/IS use, non-human status where relevant, and the probabilistic and subjective nature of affective inference.'], applicability_conditions=['Applies where EA/IS is in use or the system was developed using affective data or technology.'], exceptions_or_qualifications=['For systems designed to operate on groups rather than individuals, notice to the group is recommended.']),
'7014-security-privacy-publication': dict(required_artefacts=['Published details of system safety, security and privacy measures.'], evidence_expectation=['The published description of safety, security and privacy measures.']),
'7014-monitor-mitigate-ethical-cultural-risk': dict(timing_or_frequency=['Monitor proactively for unintended risks or issues as they emerge.'], required_artefacts=['Documented monitoring approaches and mitigation strategies for projected and unanticipated risks, issues and impacts.'], evidence_expectation=['Risk assessment coverage of ethics, culture and diversity and documented mitigation approaches.'], verification_method=['Monitor for emerging unintended risks or issues and assess ethics, culture and diversity impacts.']),
'7014-skills-and-learning-evidence': dict(timing_or_frequency=['Maintain a continuous process of learning and skill development relevant to EA/IS.'], required_artefacts=['Published evidence of relevant EA/IS knowledge and skill and of continuing learning and skill development.'], evidence_expectation=['Evidence such as peer-reviewed learning or certified qualifications and evidence of ongoing professional learning.']),
'7014-high-risk-human-stop-watchdog': dict(applicability_conditions=['Applies to high-risk systems.'], evidence_expectation=['System capability showing human oversight and intervention, a subject emergency-stop mechanism, and secondary watchdog monitoring.']),
'7014-stakeholder-research-publication': dict(required_artefacts=['Published findings of stakeholder analysis and explanation of how the findings influence system development, deployment and decommission.'], evidence_expectation=['Stakeholder research findings gathered through methods such as interviews, surveys or focus groups.'], verification_method=['Identify and analyze affected or interacting stakeholders and conduct research into their needs and preferences.'], applicability_conditions=['Covers stakeholders who could interact with or be affected by the system.']),
'7014-training-method-diversity-feedback': dict(timing_or_frequency=['Continuously incorporate stakeholder feedback into system training.'], required_artefacts=['Published explanation and justification of training methods and published approach to continuous stakeholder-feedback incorporation.'], evidence_expectation=['Training-method documentation and evidence of diverse, culturally sensitive affective data and continuing stakeholder feedback.'], verification_method=['Review training data and models for diversity and cultural sensitivity.']),
'7014-eais-risk-assessment': dict(required_artefacts=['Published EA/IS-specific risk, issue and impact assessment.'], evidence_expectation=['Assessment evidence addressing the unique risks, issues and impacts inherent to EA/IS.'], verification_method=['Conduct a risk, issue and impact assessment specific to the EA/IS.'], applicability_conditions=['Treat the system and its components as high risk until the assessment demonstrates that they are low risk.']),
'7014-data-minimisation-and-retention': dict(timing_or_frequency=['Securely delete or anonymize affective data once it is no longer needed for the specific limited purpose.'], applicability_conditions=['Collect only affective data necessary for the developer\'s published specific and limited purpose.']),
'7014-affective-rights-bias-context': dict(required_artefacts=['Published explanation of adherence to affective rights, documentation of potential bias and mitigation steps, and enumerated intended deployment contexts.'], evidence_expectation=['Published bias documentation and contextual deployment scenarios.'], verification_method=['Assess potential bias and enumerate the contexts in which the system is designed to be deployed.']),
'7014-claim-accountability-and-data-review': dict(timing_or_frequency=['Sign off product authentication before deployment and perform affective-data reviews regularly.'], required_artefacts=['Pre-deployment product-authentication sign-off and records of regular affective-data review and correction.'], evidence_expectation=['Evidence of accountable claim sign-off and data-review/correction activity.'], verification_method=['Perform regular reviews of affective data and correct it where necessary.']),
'7014-results-challenge-mechanism': dict(applicability_conditions=['The challenge mechanism is proportionate to the risk level of the system.'], exceptions_or_qualifications=['A low-risk system may use a feedback form, while a high-risk system may require an interactive mechanism for directly disputing results.']),
'7014-stakeholder-and-accountability-scope': dict(required_artefacts=['Documentation identifying the person or persons responsible for system risks, issues and impacts.'], evidence_expectation=['Risk-management documentation covering all potentially affected stakeholders and named responsibility.'], applicability_conditions=['Covers all potentially affected stakeholders.']),
'7014-ethical-purpose-and-scope-explanation': dict(required_artefacts=['Published ethical-stance explanation and published explanation of intended purpose, expected scope of use and conditions for intended functioning.'], evidence_expectation=['Published rationale for the system purpose, development/deployment/decommission approach, intended use and operating conditions.']),
'7014-ongoing-monitoring': dict(timing_or_frequency=['Perform monitoring on an ongoing basis during operation.'], evidence_expectation=['Monitoring results for factors such as goal drift, performance, accuracy metrics, response time and user satisfaction.'], verification_method=['Monitor the EA/IS for operational drift, performance and user-outcome indicators.']),
'7014-no-release-without-safety-evidence': dict(timing_or_frequency=['Before public release of the system.'], evidence_expectation=['Published evidence of system safety.'], applicability_conditions=['Applies before releasing the system publicly.']),
'7014-active-bounded-consent-record': dict(timing_or_frequency=['Obtain active informed consent before relying on subject data and maintain the consent record for the entire system life cycle.', 'Apply spatial and temporal limits to consent licenses.'], required_artefacts=['Record of active informed consent made readily available to the subject.'], evidence_expectation=['Consent records showing freely given, informed, convenient, appropriate and meaningful opt-in consent and its spatial/temporal limits.'], verification_method=['Check consent records and consent-license limits against applicable laws and regulations.'], applicability_conditions=['Applies to subjects or other sources of data acquisition.'], exceptions_or_qualifications=['Consent is to be consistent with all applicable laws and regulations and must be active rather than passive.']),
'7014-continuous-learning-collaboration': dict(timing_or_frequency=['Maintain the learning system and culture of learning and collaboration continuously.'], applicability_conditions=['Applies to wider empathic-AI knowledge and collaboration relevant to the EA/IS.']),
'7014-wia-method-conflict-independent-review': dict(required_artefacts=['Well-being impact assessment including assessment of stakeholder hierarchy conflicts.'], evidence_expectation=['Assessment of the risks and impacts of prioritizing one stakeholder type or group over another.'], verification_method=['Use a recognized well-being impact assessment process and, where practicable, third-party assessment or peer review.'], exceptions_or_qualifications=['Use of a reputable third party or peer review is recommended.']),
'7014-third-party-risk-assessment': dict(verification_method=['Use a qualified third party for risk, issue and impact assessment.'], exceptions_or_qualifications=['Applies where possible.']),
'7014-personalized-bias-aware-risk-interaction': dict(applicability_conditions=['Personalization is based on individual subject circumstances, goals and risk tolerance.'], exceptions_or_qualifications=['Human-like communication is recommended where possible.']),
'7014-explainability-replicability': dict(required_artefacts=['Explainability documentation capable, as far as possible, of supporting replication of system outputs for testing.'], verification_method=['Appropriate parties can use the explainability documentation to test replication of system outputs.'], exceptions_or_qualifications=['Replicability support is required as far as possible.']),
'7014-expanded-transparency-explanations': dict(required_artefacts=['Published explanations of system capabilities and limitations, training/testing data, inputs/outputs, transformations, purpose fit, theoretical frameworks, affective models and decision rationale.'], evidence_expectation=['Supporting evidence for purpose fit and model efficacy where available.'], exceptions_or_qualifications=['Supporting evidence is recommended where possible; theoretical-framework disclosure applies where appropriate.']),
'7014-ethical-explainability-approach-justification': dict(required_artefacts=['Ethical-explainability documentation describing main system approaches, a balanced analysis of possible implications, and the ethical justification for each approach.'], evidence_expectation=['Documented rationale for why each main approach is considered ethical.']),
'7014-diverse-affective-data-sourcing-labeling': dict(verification_method=['Review affective-data sources for diversity and labels for accurate reflection of provider perspectives and experiences.']),
'7014-subject-data-control-inference-access': dict(applicability_conditions=['Applies to subject controls over data processing and to inferences and system decisions made about the subject.']),
'7014-human-oversight-calibration-representation': dict(applicability_conditions=['A competent representative is recommended when the subject may lack adequate mental capacity.']),
'7014-bias-identification-mitigation': dict(evidence_expectation=['Records of identified bias and mitigation activity.'], verification_method=['Use methods or tools to check for bias and mitigate identified bias.'], timing_or_frequency=['Address bias that develops within the system as it is identified.']),
'7014-contextual-adaptation': dict(applicability_conditions=['Applies to contextual variations such as time, location, speed, time of day and changing social norms that can affect affective operation.']),
'7014-post-production-quality-monitoring': dict(timing_or_frequency=['Monitor the EA/IS after it has been put into production.'], verification_method=['Quality-assurance monitoring accounts for adaptive learning and training after production.'], applicability_conditions=['Applies to EA/IS that can adapt through learning or training once operationalized.']),
'7014-subject-primacy-vulnerable-default-human-centered': dict(required_artefacts=['Formal declaration where vulnerable parties are not included in the default audience, including how the system is restricted to other stakeholder classes.'], applicability_conditions=['Treat the default audience as including vulnerable parties unless formally declared and restricted otherwise.'], exceptions_or_qualifications=['Subject primacy is recommended where possible.']),
'7014-consent-service-non-withholding': dict(applicability_conditions=['Applies when a subject chooses not to provide, or fails to provide, effective informed consent.'], exceptions_or_qualifications=['Applies where possible and cautions against unduly withholding service solely because effective informed consent is absent.']),
'7014-training-data-quality-modality-diversity': dict(verification_method=['Use recognized high-quality affective datasets when acquiring data from third parties and assess whether multiple data modes improve quality and robustness.'], applicability_conditions=['High-quality dataset guidance applies when data is acquired from third parties.', 'Multimodal training is recommended where likely to improve system quality and robustness.']),
'7014-subject-intimacy-obtrusiveness-calibration': dict(applicability_conditions=['Applies to subject control over the intimacy and obtrusiveness of system behavior.'], exceptions_or_qualifications=['Provide the calibration facility where possible.']),
'7014-independent-realtime-human-monitoring': dict(timing_or_frequency=['Monitor the system as close to real time as feasible.'], verification_method=['Use qualified third-party assessment and auditing and human oversight/intervention where required.'], exceptions_or_qualifications=['Near-real-time monitoring is recommended to the extent feasible.']),
}

records = json.loads(SHARD.read_text(encoding='utf-8'))
assert len(records) in {41, 59}
by_key = {r['identity_key']: r for r in records}
assert len(by_key) == len(records)
ids_before = {r['requirement_id'] for r in records}
assert ESTABLISHED_IDS <= ids_before

for clause, identity, summary, clone_key in NEW:
    rid = req_id(clause, identity)
    if identity in by_key:
        assert by_key[identity]['requirement_id'] == rid
        continue
    assert rid not in ids_before
    base = copy.deepcopy(by_key[clone_key])
    base['requirement_id'] = rid
    base['identity_key'] = identity
    base['clause_or_control'] = clause
    base['requirement_summary'] = summary
    base['governance_expectation'] = summary
    base['requirement_posture'] = 'recommended-practice'
    base['expectation_type'] = 'guidance'
    base['source_defined_tags'] = [{'scheme':'IEEE-7014-clause','values':[clause]}]
    base['related_external_requirements'] = []
    records.append(base)
    by_key[identity] = base

assert len(records) == 59
assert ESTABLISHED_IDS <= {r['requirement_id'] for r in records}

for r in records:
    identity = r['identity_key']
    assert identity in META, identity
    r['source_review_date'] = DATE
    r['applicable_actor'] = ['EA/IS developer']
    r['governed_object'] = ['emulated-empathy autonomous or intelligent system (EA/IS)']
    for f in FIELDS[2:]:
        r[f] = list(META[identity].get(f, []))
    p = r['interpretation_provenance']
    p['basis'] = 'licensed-primary-text'
    p['source_analysis_method'] = 'Direct clause-level review of IEEE Std 7014-2024 licensed primary text; mandatory and recommended Clause 4 activities analytically paraphrased without reproducing licensed text.'
    p['source_locator'] = LOCATOR
    p['source_metadata_fingerprint'] = FINGERPRINT
    p['reviewed_source_digest'] = DIGEST
    p['reviewed_source_digest_algorithm'] = 'sha256'
    p['reviewed_source_digest_status'] = 'recorded'
    r['review_limitations'] = [
        'Clause 4 life-cycle activities are represented as bounded analytical propositions; closely related source-native subitems may remain grouped where they perform one governance function.',
        'Licensed IEEE text is not stored in VIGIL.'
    ]
    r['assurance_provenance'] = []

records.sort(key=lambda r: r['requirement_id'])
dump(SHARD, records)

ledger = json.loads(LEDGER.read_text(encoding='utf-8'))
ledger['updated_at'] = DATE
review_by = {e['requirement_id']: e for e in ledger['entries']}
for r in records:
    statuses = {}
    for f in FIELDS:
        statuses[f] = 'populated-reviewed' if r[f] else 'not-specified-by-source'
    entry = {
        'requirement_id': r['requirement_id'],
        'reviewed_at': DATE,
        'review_basis': 'licensed-primary-text',
        'review_notes': ['Direct review of the lawfully accessed IEEE 7014-2024 primary text; source-explicit metadata populated and source silence recorded without inference.'],
        'field_status': statuses,
    }
    review_by[r['requirement_id']] = entry
ledger['entries'] = sorted(review_by.values(), key=lambda e: e['requirement_id'])
dump(LEDGER, ledger)

assurance = json.loads(ASSURANCE.read_text(encoding='utf-8'))
assurance['updated_at'] = DATE
review_entry = {
    'vigil_source_id': SOURCE_ID,
    'external_source_id': EXTERNAL_ID,
    'source_version': VERSION,
    'source_metadata_fingerprint': FINGERPRINT,
    'reviewed_source_digest': {
        'algorithm': 'sha256',
        'digest': DIGEST,
        'recorded_at': DATE,
        'artefact_role': 'reviewed-primary-source',
        'access_basis': 'licensed-primary',
        'evidence_ref': LOCATOR,
    },
    'assurance_provenance': [],
}
replaced=False
for i,e in enumerate(assurance['source_reviews']):
    if e['external_source_id']==EXTERNAL_ID and e['source_version']==VERSION:
        assurance['source_reviews'][i]=review_entry; replaced=True; break
if not replaced:
    assurance['source_reviews'].append(review_entry)
dump(ASSURANCE, assurance)

fidelity = json.loads(FIDELITY.read_text(encoding='utf-8'))
fidelity['reviewed_at'] = DATE
fentry = {
    'vigil_source_id': SOURCE_ID,
    'external_source_id': EXTERNAL_ID,
    'source_version': VERSION,
    'fidelity_status': 'assured',
    'effective_extraction_status': 'complete',
    'assessment_basis': 'Direct review against the complete lawfully accessed IEEE 7014-2024 licensed primary PDF confirmed all 41 established mandatory Clause 4 records as source-traceable and preserved every established EXTREQ identity. The historical extraction claimed coverage of mandatory and recommended Clause 4 life-cycle activities but omitted recommended practices. Eighteen source-explicit recommended-practice propositions were added, including two independently normative recommendations in Clause 4 purpose text and two unlettered recommendations following activity lists. The resulting 59-record bounded representation preserves source posture, source-explicit metadata and explicit source silence without reproducing licensed text.',
    'known_fidelity_gaps': [],
    'audited_requirement_ids': [r['requirement_id'] for r in records],
    'next_action': 'Retain the 59 reviewed identities and repeat the fidelity review on material revision of IEEE 7014.',
}
replaced=False
for i,e in enumerate(fidelity['entries']):
    if e['external_source_id']==EXTERNAL_ID and e['source_version']==VERSION:
        fidelity['entries'][i]=fentry; replaced=True; break
if not replaced:
    fidelity['entries'].append(fentry)
dump(FIDELITY, fidelity)

scope = json.loads(SCOPE.read_text(encoding='utf-8'))
for e in scope['entries']:
    if e['external_source_id']==EXTERNAL_ID and e['source_version']==VERSION:
        e['extraction_status']='complete'
        e['extraction_scope_notes']='Governance-relevant mandatory and recommended life-cycle activities in Clause 4 are represented as bounded analytical propositions. All 41 established mandatory records are preserved and 18 source-explicit recommended practices omitted from the historical extraction are added without changing established identities.'
        e['known_unreviewed_sections']=[]
        e['next_action']='Monitor for material source revision.'
        e['maintainer_action_required']=False
        e['maintainer_action']=None
        break
else:
    raise AssertionError('IEEE-7014 scope entry missing')
dump(SCOPE, scope)

print('IEEE 7014 repair valid: 41 established IDs preserved; 18 recommended-practice records added; 59 canonical records.')
print('Digest', DIGEST)
print('New IDs:')
for clause, identity, _, _ in NEW:
    print(req_id(clause, identity), clause, identity)
