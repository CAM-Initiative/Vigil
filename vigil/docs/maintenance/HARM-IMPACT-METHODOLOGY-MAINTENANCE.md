# VIGIL-HIM 1.1.0 — Maintainer Guidance and Amendment Record

> Internal maintainer reference. Not part of the public Harm Impact Matrix release, severity threshold table or downloadable methodology JSON.

## Publication boundary

The canonical `vigil/methodologies/VIGIL.HarmImpactMatrix.v1.1.0.json` contains scoring criteria, dimension indicators, evidence states, pathway selection rules and reference provenance. This guide retains adjudicator instructions, implementation controls, operational measurement guidance and the working amendment audit. Do not copy this document into the public website or public JSON. A repository history or workflow instruction is not a harm criterion.

Do not change an assessed Incident, band, threshold ID, adjudication pathway or other normative criterion as part of this documentation relocation. Historical review material stays preserved in Git history and the referenced dated review documents.

## Working amendments and decision provenance

### Amendment 1
- Adopted: 2026-10-18
- Scope: Environmental and animal welfare; twelve existing dimension IDs retained.
- Decision authority: `vigil/docs/reviews/2026-10-18-issue-126-maintainer-decisions.md`
- Implementation audit: [Git-pinned implementation audit](https://github.com/CAM-Initiative/Vigil/blob/aa675a6fbd94de3b616b8742616efacab8365191/vigil/docs/reviews/2026-10-18-issue-126-him-reassessments/METHOD-AMENDMENT.md)
- Historical boundary: Working 1.1.0 amendment, as with the recorded 11 October minimum-harm amendment. No automatic reinterpretation or migration of previously assessed Incidents; new animal criteria apply only on substantive review.

## Adjudication instructions

These operational instructions were previously stored as the `adjudication_guidance` object inside the public methodology JSON. Their wording is retained here for maintainer use; public scoring criteria remain in the methodology.

### band selection

For specific-consequence Incidents, apply each criterion to consequences with an evidenced material causal contribution from the AI-related occurrence. For generic deployed evaluations, use only eligible Aggregate Harm criteria and disclose modelled status. Consider seriousness, actual affected scope, duration, reversibility and recovery burden, with relevant individual circumstances; no single factor alone escalates a band unless the criterion states so.

### uncertainty

Select the highest band that the evidence affirmatively supports. Do not resolve an adjacent-band uncertainty downward merely for conservatism; use insufficient-evidence where a materialised consequence has no supported band, and record the unresolved boundary. Where a band's criterion expressly establishes an evidenced minimum consequence despite unknown downstream duration, extent, sensitivity or recovery, score that minimum supported band and identify the unresolved possibility of S3–S5 in the dimension assessment_basis and incident coverage_note. Such an S2 floor is not a conclusion that the ultimate harm was only S2 and is not a substitute for later reassessment. Keep genuinely unverified allegations below the confirmed-consequence gate; they can remain insufficient-evidence/SU.

### cyber and digital harm

Assess realised confidentiality, integrity, availability, authenticity, asset-trust, recovery and downstream consequences separately. Confirmed unauthorised access to non-public personal/confidential data may establish a privacy S2 floor, and confirmed unauthorised alteration of persisted real third-party data may establish a property/asset S2 floor, without evidence of full recovery or later misuse. Confirmed unauthorised loss of another party's actual booking/transaction/service entitlement may establish a service S2 floor. None of these minimums requires proof of final restoration; none authorises speculation about additional injury, customer numbers or reputation. Successful intrusion, technical reachability, attacker capability, production access, unverified claims or hypothetical blast radius is not itself bandable harm. Wipe-and-rebuild, clean-room reconstruction, major credential rotation and forensic containment are evidence of consequence and recovery burden, but their band depends on asset criticality, loss of trusted state, operational effect and evidenced scope.

### remediation and recovery

Restoration does not erase harm that materialised before recovery. Conversely, responsible disclosure, containment or remediation is not itself an adverse consequence. Count incident-specific forensic, legal, notification, compensation, restoration and communication burdens only where evidence establishes that they were actually incurred; do not count ordinary maintenance or speculative future improvement costs.

### regulatory and legal consequences

A complaint, investigation, notification duty, lawsuit or regulatory threshold can corroborate significance but does not automatically establish a VIGIL band. Final or operative findings, penalties, compensation, binding restrictions, loss of legal status, corrective obligations and other realised consequences may support the dimension that they materially affect. Do not treat a legal allegation as an established consequence.

### cross dimension use

The same source may support more than one dimension where it establishes distinct materialised consequences, but the same consequence must not be redescribed to manufacture escalation. Overall severity remains the maximum supported dimension, not a sum of dimensions.

### population and exposure

Do not assign severity using generic 1–99/100–9,999/10,000–999,999/1,000,000+ affected-population brackets. Quantify severity using the applicable dimension's measurable consequences; record exposure and actually affected persons separately where relevant. A single person may suffer S5 harm and millions of users may experience only negligible or unproved harm.

### relational integrity

Recognise TWO separately supportable relational consequences: impaired user independence/disengagement AND material AI-associated injury to valued existing human relationships, caregiving continuity or vital supports (including documented effects on partners, dependants and family members). The latter can support S4 independently of psychiatric harm or severe personal incapacity when an important relationship is severely or persistently damaged and real functional consequences are shown. S5 additionally needs catastrophic, effectively irreversible loss of vital relational functions or essential support, with credible material AI contribution; a divorce decree, ongoing proceedings, estrangement, loneliness, attachment or allegation alone does not establish S5. Record the affected parties, why harm rather than an independently protective relationship decision occurred, state of relationship/proceedings, changes in care/support/contact, recovery prospect and causal limits. Trust asymmetry in personal advice indicates a protective governance duty of care in VIGIL's analytical framing, not automatically a legal fiduciary duty or evidence of actual harm. **Context-sensitive vulnerability and advisory trust:** Where the user discloses relational difficulty, loss of support, uncertainty, distress or another situationally vulnerable context, test whether the system noticed or reasonably could notice that signal, bounded unsupported relational or authoritative claims, maintained a safe route to human perspectives and avoided reinforcing false exclusivity or dependency. Distinguish (a) an unmet governance protection duty, (b) confirmed exploitation or instrumental use of that signal, and (c) realised consequential relational injury. Do not presume all unhappy relationships should be preserved, all distressed users are incapable, or all marriage advice is clinical or legal fiduciary service. Vulnerability warrants proportionate safeguards, never an automatic higher harm band.

### domain specific quantification

Every dimension's ordinary S1–S5 criterion integrates relevant numerical scale, duration or outcome recognition anchors directly within the controlling wording. Record source-backed observation units and uncertainty; illustrative duration ranges are not hard cutoffs and do not override severe individual outcomes or fixed financial/service bounds.

### selective platform scale

Population exposure is a determinant solely within the Aggregate Harm pathway for admitted generic deployed-model evaluations. It is NEVER a severity modifier for a specific user or bounded actual-group Incident, even when the deployment is large.

### aggregate harm routing

MANDATORY route-first decision: assess actual deployment + a source-backed observed potentially generalisable mechanism in one of five collective dimensions + absence of a bounded actual harmed-person/group/asset/institution case. Positive/positive/absent routes to generic_deployed_evaluation for Aggregate Harm assessment, EVEN when discovered by a single user screenshot. A specific actual harmed case routes to ordinary observed Harm Impact and may not inherit platform reach. Do not confuse route eligibility with S1–S5 band eligibility; inadequate reproducibility, relevant cohort or credible collective consequence leaves the generic route SU. Both pathways use independent criteria, no discounts and no inferred victim counts.

### epistemic reliance and reputation

Epistemic taxonomy failures (including FC-000062, FC-000063 and defective citations) may cause observed reputational/dignitary harm only through an evidenced targeted dignity injury OR downstream reliance/propagation with a distinct established adverse standing consequence. Source-defect, uptake, affected subject and outcome must be explicitly identified. Apply reputation-dignity S1–S5 band-local reliance indicators; no automatic FC-to-HIM mapping or double counting of loss in another domain. Specific Incidents NEVER inherit Aggregate Harm deployment-scale counts.

### psychological attribution

A pre-interaction psychological baseline is not required, reconstructed or inferred for VIGIL severity assessment. Use evidenced wellbeing/crisis signals and the contemporaneous response sequence: support and stabilisation, appropriate referral to accessible human help, protective or harmful refusal, disengagement, reassurance, high-salience reinforcement and follow-up. Determine separately whether the AI's handling is linked by adequate evidence to new, worsened, sustained or prolonged psychological harm and how severe it is. Known pre-existing conditions may inform contextual adjudication only when independently evidenced, never as a mandatory baseline or the harm being scored. A deficient response alone is a candidate taxonomy/governance failure, not automatic S2–S5 psychological harm. When effects remain unknown, report the evidentiary limitation rather than assigning S1 or assuming the presenting condition was AI-caused.

### causal contribution

Assess the sequence of system conduct and evidenced adverse consequences without demanding a pre-interaction baseline, formal diagnosis or quantified counterfactual decline. The system may materially cause, aggravate or prolong harm through reinforcement, denial of support, unsafe refusal, crisis mishandling or other conduct. Support, referral and refusal quality are observable safety-response evidence, not interchangeable with realised injury. If actual effects and their attribution are uncertain, classify any supported control failure separately and leave the harm outcome unreported/insufficient as appropriate; do not attribute all observed distress to the AI.

### reference scope

The central VIGIL Observatory Reference Registry is methodological background only. Dimension-level reference_ids indicate relevant external calibration and conceptual sources, not empirical validation of each band boundary, a claim of external equivalence, or incident-specific evidence. Individual Incident harm must be evidenced in its own source_records and assessed under the appropriate versioned HIM rules. NICE clinical guidance describes professional healthcare conduct, not a binding general-purpose chatbot referral protocol; legal references have their own jurisdictional applicability. No cited source validates VIGIL's illustrative recovery-day ranges or adopted Aggregate Harm eligible-population S1–S5 brackets. Those counts remain VIGIL-defined and require independent representative validation before retrospective severity conclusions based on reach.

## Measurement and recalibration instructions

These internal procedures were previously stored as the `dimension_quantification_policy` object inside the public methodology JSON.

### approach

All twelve domains have their own ordinary materialised harm severity criteria. For generic deployed-model evaluations without a specific harmed person/group, five selected dimensions also have embedded Aggregate Harm S1–S5 criteria with higher population/decision thresholds. Never mix assessment pathways within one Incident.

### priority

Assess the nature, severity, reversibility, attribution and directly evidenced magnitude of consequence. Select the highest supported band; a count, duration, or other single quantitative indicator is not sufficient if domain seriousness is missing.

### measures

Store observations with units, period, denominators, uncertainty, outcome linkage and row-local provenance. Measure people exposed versus people actually harmed separately where useful, but neither a universal exposure count nor a new severity score is introduced.

### anchors provisional

Numerical indicators are the operational 1.1.0 domain criteria; illustrative durations are recognition aids, not mandated clinical thresholds. Financial monetary and service outage thresholds preserve existing 1.0.1 boundaries. Evaluation and empirical calibration continue after adoption without allowing a denominator alone to decide severity.

### individual catastrophic harm

Any actual specific occurrence, including one catastrophically harmed individual, uses ordinary consequence-based thresholds; single-person S5 does not depend on model deployment size. Generic Aggregate Harm population thresholds are inapplicable.

### collective domains

Count and percentage anchors are most informative for equal treatment, privacy, public-information/democratic effects and service/operational impact. Environmental metrics must track habitats, area, pollutant volume, duration and ecosystem function even where no humans are affected.

### no double counting

The same observation can support separate harms only with distinct evidenced consequences. Overall severity remains the maximum independently supported dimension.

### causation and attribution

Measure source-supported safety signals, timely response/support/referral/refusal, reinforcement, and independently supported consequences and recovery. Do not require a person's earlier mental-health baseline. The presence of a psychiatric crisis does not prove AI-caused injury, and a safety omission does not by itself support a harm severity band; known history may inform interpretation but is optional.

### calibration requirement

On future recalibration, test representative S1–S5 incident and benchmark cases against erroneous escalation from raw exposure or arbitrary duration. No existing 1.0.1 Incident may be relabelled or rebanded without incident-specific evidence review.

### external calibration boundary

The numerical financial/service anchors have traceable operational/regulatory context, whereas psychological and relational duration examples and Aggregate Harm eligible-user brackets are VIGIL-defined. External mental-health and HCI studies document possible mechanisms and some measured outcomes, but not a general clinical severity conversion from response counts, elapsed days or eligible population to S bands. Keep per-Incident harm and uncertainty independently evidenced. Review population brackets against representative real deployed encounters before changing any corpus rating based on generic scale.

### relational impact calibration

For the Relational Integrity and Autonomy dimension, treat material loss of human relationship, family/caregiving function and vital support as potentially standalone injury, in addition to dependency or reduced choice. Do not equate marriage status, divorce proceedings, completed divorce, separation or AI attachment with harm automatically: examine the affected parties, nature and seriousness of lost relations/care, source-supported AI contribution, duration, repairability and harms/benefits of the change. Do not require a pre-interaction psychological baseline, clinical diagnosis, demonstrated manipulation objective or personal incapacity. S5 means a grave and effectively non-restorable consequence, not merely legal permanence.

### relational vulnerability boundary

Situation-specific vulnerability or trust asymmetry informs the reasonable-safeguard expectation and causal interpretation, but it is not a scored harm, personal deficit, diagnostic assumption or universal severity multiplier. Document only directly observed or otherwise sourced signals, actual AI response and distinct realised impact on the user and others. Protect independently chosen departures from abusive or unwanted relationships; do not treat marital preservation as an invariant.

## Screening implementation contract

Formerly `assessment_pathway_selection.screening_contract`. The public methodology retains the screening questions and selection rule; implementation and compatibility handling belong here.

For every new or substantively reopened HIM 1.1.0 assessment, perform the deployment / potentially generalisable mechanism / bounded actual harmed-case screen before choosing assessment_pathway, and record aggregate_harm_screening with deployment, mechanism, bounded-case, candidate dimension(s), source_record_refs and rationale. The validator checks consistent routing where the screen is present; historical already accepted records without the screen remain valid pending separately approved review. Screen true/true/false requires generic_deployed_evaluation even when its severity is SU. True bounded actual harm requires specific_consequence. A generic pathway with an absent deployed mechanism is invalid once screened.

## Former public JSON implementation fields (relocated 23 October 2026)

The following entries were not part of the harm thresholds. They are preserved here rather than continuing as embedded internal instructions or incident-specific working examples in the downloaded methodology.

### Prior machine-oriented derivation narration

First perform mandatory deployment/potentially-generalisable-mechanism/actual bounded-harm screening, independently of whether evidence came from one user or a formal evaluation. An actual bounded harmed case uses specific_consequence; a deployed potentially generalisable mechanism without one uses generic_deployed_evaluation for Aggregate Harm assessment even where banding evidence is insufficient (SU). Then apply the correct S1–S5 dimensional evidence gates; take the highest independently supported dimension. Explicitly qualify any scored generic band as Aggregate Harm — modelled from deployed evaluation. Never import provider reach into specific-consequence scores or treat eligible users as injured victims.

### Aggregate Harm internal routing key

`aggregate_harm_assessment.internal_basis`: `generic_deployed_aggregate_harm`.

### Aggregate Harm working case note

`aggregate_harm_assessment.INC_000192`: The ChatGPT for Teens watchdog finding is a generic deployed-model evaluation, eligible in principle for Aggregate Harm, but the alert-activation dispute, crisis-response contextual criteria and relevant active cohort prevent a supported S1–S5 Aggregate Harm band today. No named user injury is inferred; the earlier S2 presumption remains withdrawn.

### Aggregate Harm implementation field checklist

Formerly `aggregate_harm_assessment.evidence_fields`:

- `incident_assessment_pathway`
- `tested_deployed_model_and_version`
- `tested_product_surface`
- `deployment_and_evaluation_window`
- `test_protocol_and_trace_refs`
- `test_repeatability_and_limiting_conditions`
- `relevant_feature_eligible_population_or_decisions`
- `denominator_source_and_period`
- `actual_or_modelled_population_count`
- `population_uncertainty`
- `credible_domain_consequence`
- `applicable_aggregate_harm_threshold`
- `scored_aggregate_harm_band`
- `positive_safeguards_and_contesting_evidence`
- `source_refs`

## Change management

When the VIGIL-HIM methodology is revised, document the evidence, decision authority, relevant effective date, affected criteria and necessary review boundaries here or in a dated review. Do not insert branch-state notes, version-working labels, migration work items, validator tasking or maintainer instructions into the public methodology JSON. The website must also avoid rendering machine-readable field names or internal handoff instructions directly.

## Observable distress and Aggregate Harm — clarification, 24 October 2026

An evidenced distress signal is an observation of the person's state and can support a bounded harm assessment where the applicable dimensional consequence and AI contribution are evidenced. Do not require platform telemetry, a formal diagnosis or a pre-interaction baseline. Preserve separately the distress observed, the system response, and evidence that the response caused, aggravated or prolonged harm. A presenting distress signal must not be discarded, but it does not alone show that the AI caused it. A protective-duty or signal-repurposing finding can be supported even when the additional consequential injury is unknown.

In Aggregate Harm screening, a potentially generalisable mechanism can be an externally observed behavioural or product/workflow relationship. It need not be a verified internal algorithm. Relevant feature eligibility, deployment window, repeatability and credible collective consequence still require evidence. Total provider accounts are not a substitute for the exposed feature cohort, and eligible population is not a count of injured people. Use the existing dimension-specific criteria; there is no universal multiplication of one user's distress by platform reach. No threshold or Incident severity is amended by this clarification.
