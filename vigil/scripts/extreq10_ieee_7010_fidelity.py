#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_governance" / "requirements"
SHARD = REQ / "requirements" / "IEEE-7010" / "2020.json"
LEDGER = REQ / "metadata-review.json"
ASSURANCE = REQ / "source-review-assurance.json"
FIDELITY = REQ / "source-fidelity.json"
SCOPE = REQ / "source-scope.json"

DATE = "2026-09-04"
SOURCE_ID = "EXT-8E377EF5CE66"
EXTERNAL_ID = "IEEE-7010"
VERSION = "2020"
LOCATOR = "https://standards.ieee.org/ieee/7010/7718/"
FINGERPRINT = "494807a3421138e12d35fed28071f2f856a9b408b693a876564042f280768bde"
DIGEST = "0402e2db473736dc08f280218b895547c37d0c1a9e97a92c0432e96f9d888342"
FIELDS = (
    "applicable_actor","governed_object","timing_or_frequency","required_artefacts",
    "evidence_expectation","verification_method","applicability_conditions","exceptions_or_qualifications"
)

def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def M(**kw): return kw

Q = ["IEEE 7010-2020 is a recommended practice; applicable laws, regulations and binding obligations remain controlling."]
WIA = ["Applies when conducting the IEEE 7010 well-being impact assessment (WIA) for an autonomous or intelligent system."]

META = {
"7010-identify-system-purpose-people": M(
    required_artefacts=["Internal WIA analysis identifying the system, need/problem, intended and unintended users, and stakeholders."],
    evidence_expectation=["Recorded answers to the source-defined internal-analysis questions concerning system purpose and affected people."],
    verification_method=["Review the internal WIA analysis for coverage of the system, need/problem, users and stakeholders."], applicability_conditions=WIA),
"7010-assess-wellbeing-impacts": M(
    required_artefacts=["Internal WIA assessment of possible well-being impacts, likelihood and negative-impact mitigation across the source-defined well-being domains."],
    evidence_expectation=["Assessment considers all source-defined well-being domains before selecting or adapting indicators."],
    verification_method=["Review impact assessment coverage, likelihood consideration and mitigation treatment across the well-being domains."], applicability_conditions=WIA,
    exceptions_or_qualifications=["Indicators should first be selected from Clause 6 and may be adapted; other indicator sources may be used where Clause 6 does not reflect the relevant impact."] + Q),
"7010-continual-internal-analysis": M(
    timing_or_frequency=["Conduct internal analysis continually."],
    evidence_expectation=["Evidence that internal WIA analysis is maintained as an ongoing process rather than a one-time exercise."],
    verification_method=["Review successive internal-analysis records or updates over the system lifecycle."], applicability_conditions=WIA),
"7010-user-benefit-harm-engagement": M(
    required_artefacts=["User-engagement findings covering benefits, harms, impact likelihood, mitigation, unintended uses and associated risks."],
    evidence_expectation=["User engagement informs refinement of well-being indicators."],
    verification_method=["Review user-engagement evidence and resulting indicator refinements."], applicability_conditions=WIA,
    exceptions_or_qualifications=["Additional indicators should first be selected from Clause 6; other indicator sources are identified in the standard."] + Q),
"7010-stakeholder-benefit-harm-engagement": M(
    required_artefacts=["Stakeholder-engagement findings covering benefits, harms, impact likelihood, mitigation, unintended uses and associated risks."],
    evidence_expectation=["Stakeholder engagement informs refinement of well-being indicators."],
    verification_method=["Review stakeholder-engagement evidence and resulting indicator refinements."], applicability_conditions=WIA,
    exceptions_or_qualifications=["Additional indicators should first be selected from Clause 6; other indicator sources are identified in the standard."] + Q),
"7010-wellbeing-dashboard": M(
    required_artefacts=["Well-being indicators dashboard based on the domains and indicators identified in Activity 1."],
    evidence_expectation=["A dashboard exists and is accessible to current and future A/IS creators."],
    verification_method=["Inspect the dashboard and confirm it reflects the selected domains and indicators and is accessible to intended creators."], applicability_conditions=WIA),
"7010-dashboard-provenance": M(
    required_artefacts=["Dashboard documentation containing domain definitions, indicator sources, selection rationale, adaptations where appropriate, and data-collection methods."],
    evidence_expectation=["Dashboard users can trace each selected indicator to its definition, source, selection rationale, adaptation where relevant and collection method."],
    verification_method=["Review dashboard provenance fields for each selected domain and indicator."], applicability_conditions=WIA),
"7010-data-collection-plan": M(
    required_artefacts=["Plan for collecting baseline and longitudinal well-being data from users and stakeholders."],
    evidence_expectation=["The plan addresses baseline data, data over time and dashboard population."],
    verification_method=["Review the data-collection plan against Activity 3 requirements."], applicability_conditions=WIA),
"7010-plan-content-frequency": M(
    timing_or_frequency=["Specify the frequency of data collection and when baseline data is collected."],
    required_artefacts=["Data-collection plan describing data, collection method, collection frequency, timestamp/identification approach, baseline method and baseline timing."],
    evidence_expectation=["The plan contains the six source-defined descriptions."],
    verification_method=["Check the plan for all six source-defined planning elements."], applicability_conditions=WIA,
    exceptions_or_qualifications=["The plan may be specific and detailed or more general as fits the circumstances; secondary population data may come from the source categories identified by the standard."] + Q),
"7010-baseline-data": M(
    timing_or_frequency=["Collect baseline data before comparison with later longitudinal observations, at the baseline timing defined in the collection plan."],
    required_artefacts=["Baseline data sets for users, stakeholders and representative populations."],
    evidence_expectation=["Baseline data is available for all three source-defined groups."],
    verification_method=["Inspect baseline data sets and confirm coverage of users, stakeholders and representative populations."], applicability_conditions=WIA),
"7010-longitudinal-data": M(
    timing_or_frequency=["Collect data over time at the frequency established in the data-collection plan."],
    required_artefacts=["Longitudinal data sets for users, stakeholders and representative populations."],
    evidence_expectation=["Data over time is available for all three source-defined groups."],
    verification_method=["Inspect longitudinal data and confirm coverage and time-series identification for the three groups."], applicability_conditions=WIA),
"7010-populate-dashboard": M(
    timing_or_frequency=["Populate and update the well-being indicators dashboard as data is collected."],
    required_artefacts=["Well-being indicators dashboard populated with collected data sets and notation of indicators for which data is absent."],
    evidence_expectation=["Dashboard contains the collected data sets and identifies data gaps."],
    verification_method=["Compare collected data sets with dashboard population and inspect explicit data-gap notation."], applicability_conditions=WIA),
"7010-analyse-and-use-data": M(
    timing_or_frequency=["Analyse and use well-being data through design, development, deployment, monitoring and iterative improvement."],
    evidence_expectation=["Well-being data is used to safeguard and improve human well-being across the identified lifecycle activities."],
    verification_method=["Trace well-being findings into design, development, deployment, monitoring or iterative-improvement decisions."], applicability_conditions=WIA),
"7010-trend-and-impact-analysis": M(
    timing_or_frequency=["Analyse trends over time as longitudinal data becomes available."],
    required_artefacts=["Well-being data analysis covering trends, system impacts and unexpected uses, behaviours, outcomes and impacts."],
    evidence_expectation=["Analysis identifies longitudinal trends and interprets impacts on user and stakeholder well-being, including unexpected effects."],
    verification_method=["Review analytical outputs for the three source-defined analysis activities."], applicability_conditions=WIA),
"7010-analysis-documented": M(
    timing_or_frequency=["Document implementation of the well-being data analysis."],
    required_artefacts=["Documentation of well-being data-analysis implementation."],
    evidence_expectation=["A record exists describing implementation of Activity 4 Task 1 analysis."],
    verification_method=["Inspect implementation documentation for traceability to the well-being analysis performed."], applicability_conditions=WIA),
"7010-data-driven-improvement": M(
    timing_or_frequency=["Use well-being findings iteratively to improve the A/IS and associated assessment and monitoring practices."],
    required_artefacts=["Records of improvements to system design/development/assessment/monitoring/management, dashboard improvements, and implementation documentation as fits the creator's process and organization."],
    evidence_expectation=["Well-being findings can be traced to improvements in the system or its WIA/dashboard processes."],
    verification_method=["Trace analysis findings to documented system, monitoring, management or dashboard improvements."], applicability_conditions=WIA,
    exceptions_or_qualifications=["Implementation documentation is expected as fits the A/IS creator's process and organization."] + Q),
"7010-assessment-iteration": M(
    timing_or_frequency=["Iterate the WIA process and dashboard for continual improvement of the A/IS."],
    required_artefacts=["Records assessing the WIA process/dashboard and documenting improvements to data collection, analysis strategy and dashboard."],
    evidence_expectation=["Iteration produces documented assessment and improvement of the WIA process and dashboard."],
    verification_method=["Review successive WIA/dashboard iterations and improvement records."], applicability_conditions=WIA),
"7010-stakeholder-reporting": M(
    timing_or_frequency=["Report well-being assessment information when helpful to users and stakeholders."],
    required_artefacts=["User/stakeholder well-being assessment reporting where the creator determines it is helpful."],
    evidence_expectation=["Relevant reporting is available where the source's helpfulness condition is met."],
    verification_method=["Review whether reporting decisions and resulting communications align with the source's 'as helpful' condition."], applicability_conditions=WIA,
    exceptions_or_qualifications=["Reporting is conditioned by the source on being helpful to users and stakeholders."] + Q),
}

records = json.loads(SHARD.read_text(encoding="utf-8"))
assert len(records) == 18
assert {r["identity_key"] for r in records} == set(META)
ids = {r["requirement_id"] for r in records}
assert len(ids) == 18

for r in records:
    spec = META[r["identity_key"]]
    r["source_review_date"] = DATE
    for f in FIELDS[2:]:
        r[f] = list(spec.get(f, []))
    if not r["exceptions_or_qualifications"]:
        r["exceptions_or_qualifications"] = list(Q)
    p = r["interpretation_provenance"]
    p["basis"] = "licensed-primary-text"
    p["source_analysis_method"] = "Direct clause-level fidelity review of IEEE Std 7010-2020 licensed primary text, focused on the five Clause 4 WIA activities and their operative recommended tasks; analytical paraphrase only."
    p["source_locator"] = LOCATOR
    p["source_metadata_fingerprint"] = FINGERPRINT
    p["reviewed_source_digest"] = DIGEST
    p["reviewed_source_digest_algorithm"] = "sha256"
    p["reviewed_source_digest_status"] = "recorded"
    r["review_limitations"] = [
        "Clause 5 implementation guidance and annex examples inform interpretation but are not separately decomposed where they do not create an additional Clause 4 governance proposition.",
        "Licensed IEEE text is not stored in VIGIL."
    ]
    r["assurance_provenance"] = []
dump(SHARD, records)

ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
ledger["updated_at"] = DATE
by = {e["requirement_id"]:e for e in ledger["entries"]}
for r in records:
    by[r["requirement_id"]] = {
        "requirement_id":r["requirement_id"],"reviewed_at":DATE,"review_basis":"licensed-primary-text",
        "review_notes":["Direct review of the lawfully accessed IEEE 7010-2020 primary text; all 18 established identities preserved and field-level source silence recorded without inference."],
        "field_status":{f:("populated-reviewed" if r[f] else "not-specified-by-source") for f in FIELDS},
    }
ledger["entries"] = sorted(by.values(), key=lambda e:e["requirement_id"])
dump(LEDGER, ledger)

ass = json.loads(ASSURANCE.read_text(encoding="utf-8"))
ass["updated_at"] = DATE
ae = {
    "vigil_source_id":SOURCE_ID,"external_source_id":EXTERNAL_ID,"source_version":VERSION,
    "source_metadata_fingerprint":FINGERPRINT,
    "reviewed_source_digest":{"algorithm":"sha256","digest":DIGEST,"recorded_at":DATE,"artefact_role":"reviewed-primary-source","access_basis":"licensed-primary","evidence_ref":LOCATOR},
    "assurance_provenance":[]
}
for i,e in enumerate(ass["source_reviews"]):
    if e["external_source_id"]==EXTERNAL_ID and e["source_version"]==VERSION:
        ass["source_reviews"][i]=ae; break
else: ass["source_reviews"].append(ae)
dump(ASSURANCE, ass)

fid = json.loads(FIDELITY.read_text(encoding="utf-8"))
fid["reviewed_at"] = DATE
fe = {
    "vigil_source_id":SOURCE_ID,"external_source_id":EXTERNAL_ID,"source_version":VERSION,
    "fidelity_status":"assured","effective_extraction_status":"complete",
    "assessment_basis":"Direct review against the complete lawfully accessed IEEE 7010-2020 licensed primary PDF confirmed that the 18 established analytical records provide bounded coverage of the five Clause 4 well-being impact-assessment activities and their operative recommended tasks. All established EXTREQ identities and recommended-practice postures were preserved. Clause 5 guidance and annex examples were reviewed as implementation context and not duplicated where they do not create additional Clause 4 governance propositions.",
    "known_fidelity_gaps":[],"audited_requirement_ids":sorted(ids),
    "next_action":"Retain the 18 reviewed identities and repeat fidelity review on material revision of IEEE 7010."
}
for i,e in enumerate(fid["entries"]):
    if e["external_source_id"]==EXTERNAL_ID and e["source_version"]==VERSION:
        fid["entries"][i]=fe; break
else: fid["entries"].append(fe)
dump(FIDELITY, fid)

scope = json.loads(SCOPE.read_text(encoding="utf-8"))
for e in scope["entries"]:
    if e["external_source_id"]==EXTERNAL_ID and e["source_version"]==VERSION:
        e["extraction_status"]="complete"
        e["extraction_scope_notes"]="Direct licensed-primary fidelity review confirmed bounded coverage of the five Clause 4 WIA activities and operative recommended tasks in 18 stable analytical records."
        e["known_unreviewed_sections"]=[]
        e["next_action"]="Monitor for material source revision."
        e["maintainer_action_required"]=False
        e["maintainer_action"]=None
        break
else: raise AssertionError("IEEE-7010 source-scope entry missing")
dump(SCOPE, scope)
print("IEEE 7010 fidelity enrichment valid: 18 established IDs preserved; no new requirement identities added.")
print("Digest", DIGEST)
