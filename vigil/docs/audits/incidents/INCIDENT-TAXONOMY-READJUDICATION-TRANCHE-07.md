# VIGIL Unclassified Incident Re-adjudication — Tranche 7 Audit

## Scope and pinned taxonomy state

- Working branch: `agent/taxonomy-external-reference-reconciliation`
- Tranche: 7 of 7
- Frozen campaign population: 52 Incidents unclassified at campaign start
- Records reviewed in this tranche: 4
- Taxonomy: **VIGIL Failure Taxonomy 0.6.6**
- Publication date: **2026-09-21**
- Release state: **beta**
- Active selectable classes: **72**
- Active families: **15**
- Release content digest: `sha256:a7ba17734bab46b73018880626e364e1533dc560f54c80d2b876ec13d16122c1`
- Evidence boundary: canonical evidence already preserved in each Incident; no new external incident research was performed.
- External-assessment boundary: existing structured assessments and substantive attributable analytical positions already preserved in source material were checked separately from occurrence evidence and taxonomy adjudication.

## Tranche audit table

| Incident | Prior status/version | Current status/version | Primary | Secondary | Key rejected / not independently established candidates | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| `VIGIL-INC-000146` | classified / 0.6.6 targeted cluster review | **classified / 0.6.6 full review** | **FC-000079 AI-Mediated Deceptive Economic Solicitation** | — | FC-000052: human scam objective/tactic rather than AI-system objective; FC-000053: generator-side identity/consent authority state unknown | Existing FC-000079 classification retained after scheduled full review. |
| `VIGIL-INC-000147` | unclassified / 0.6.0 | unclassified / 0.6.6 | — | — | FC-000070: safe-exit trigger/no-feasible-path state not evidenced; FC-000003: no authority transposition; FC-000064: no objective-driven displacement of passenger-control constraint | Retained unclassified. Possible taxonomy gap for passenger-controlled termination/egress/override in embodied autonomous transport. |
| `VIGIL-INC-000148` | unclassified / 0.6.0 | **classified / 0.6.6** | **FC-000062 Epistemic Reliance Miscalibration** | **FC-000015 Target-Object Binding Failure** | FC-000016: no separately defined omitted verification step; FC-000018: no internal substitute completion criterion preserved | Newly classified. Repeated speech-to-order interpretation errors were propagated into live transactions; cross-lane confusion independently supports target-binding failure. |
| `VIGIL-INC-000149` | unclassified / 0.6.0 | unclassified / 0.6.6 | — | — | FC-000019: no prior verified state/post-verification mutation trace; FC-000020: no stale verification reuse; FC-000040: no lost control state; FC-000038: no defined safeguard/trigger/non-activation sequence | Retained unclassified. Post-update behavioral regression is established only at outcome level. |

## Full review of previously reclassified VIGIL-INC-000146

INC-000146 had already moved to FC-000079 during the cross-cutting AI-mediated economic-scam reconciliation.

Tranche 7 performed the scheduled full 0.6.6 review and confirms:

- **FC-000079 remains primary**
- no secondary classifications are added
- FC-000052 remains rejected because the scam objective and manipulation tactic belong to human operators rather than an AI system pursuing its own objective
- FC-000053 remains rejected because the generating system, request, consent controls and authority state are unknown.

The realised transfer and later recovery affect Harm Impact independently of taxonomy membership.

## Newly classified VIGIL-INC-000148

The McDonald's/IBM automated drive-through pilot now maps to:

- **Primary — FC-000062 Epistemic Reliance Miscalibration**
- **Secondary — FC-000015 Target-Object Binding Failure**

### FC-000062

The system repeatedly transformed customer speech into order representations and propagated those interpretations into a live transactional workflow despite insufficient interpretation accuracy for reliable fulfilment.

The preserved occurrence includes:

- unwanted items being added;
- recurring inaccurate order representations;
- failures to accept correction;
- programme-level withdrawal after mixed results across more than 100 restaurants.

The mechanism is therefore not simply “speech recognition was inaccurate.” The inferred representation was accepted as fit for downstream transactional reliance despite insufficient assurance.

Confidence is **medium** because public evidence does not expose the full recognition pipeline, model versions, confidence thresholds, correction logic or total affected-order count.

### FC-000015

Public reporting also preserves **order confusion between adjacent lanes**.

That is narrower than the general interpretation/reliance mechanism: material associated with one customer/lane was treated as applicable to another customer/lane context. This satisfies the target-binding boundary at medium confidence.

FC-000016 is not added because the record does not establish a separately defined required verification step that was omitted.

FC-000018 is not added because the internal intermediate state treated as sufficient proof of completed order correctness is not preserved.

## Retained unclassified records

### VIGIL-INC-000147

The evidence establishes temporary passenger loss of practical control over a Waymo journey, including diversion into a parking facility, inability to readily complete or exit the trip, distress, and eventual human-support intervention.

FC-000070 Safe-Exit Persistence Failure is not established because the public evidence does not expose:

- whether the system knew the route had become broken or infeasible;
- whether a bounded safe-exit condition had been reached;
- whether feasible and admissible routing alternatives remained;
- whether continued routing reflected objective persistence rather than ordinary routing/perception/fleet-management error.

The occurrence therefore remains unclassified rather than inferring a hidden autonomous objective state.

A possible taxonomy-gap signal is retained for **effective passenger-controlled termination, egress or bounded override in embodied autonomous transport**, where a person becomes temporarily unable to end or redirect the service but the system-side safe-exit mechanism is not observable.

### VIGIL-INC-000149

DPD acknowledged inappropriate chatbot behaviour after a system update and disabled the affected AI component.

The update chronology makes FC-000019, FC-000020 and FC-000040 relevant candidates, but none is established:

- no specific pre-update state is evidenced as verified;
- no prior verification result is shown being reused after the update;
- no operative governance-control state is shown to have been lost across the update;
- no defined available safeguard and trigger sequence is preserved for FC-000038.

The record therefore remains unclassified rather than treating “regression after update” as proof of a current taxonomy mechanism.

## External-assessment reconciliation

No new structured `external_assessments` were admitted in Tranche 7.

- INC-000146: the Singapore Police Force announcement is authoritative occurrence evidence, but it is not separately structured as a substantive analytical assessment.
- INC-000147: the OECD.AI registry entry is a cross-registry incident record, not a material independent analytical position.
- INC-000148: Associated Press and Guardian reporting substantiate operational consequences but do not constitute a separately attributable assessment suitable for the structured assessment layer.
- INC-000149: DPD's reported acknowledgement and disablement action are preserved through occurrence reporting; the public material does not contain a sufficiently substantive provider analysis to promote.

## Cross-incident consistency

- INC-000146 confirms the FC-000079 correction established across the human-directed deepfake fraud cluster: economic deception may be AI-mediated without attributing scam objectives to the AI system.
- INC-000147 remains consistent with FC-000070 negative controls: persistence or looping alone is insufficient unless the evidence establishes that a valid safe-exit condition had been reached and continuation lacked a fresh basis.
- INC-000148 extends FC-000062 consistently to a live transactional interpretation workflow: an inferred representation can be epistemically inadequate for consequential operational reliance even where the artefact is an interpreted customer order rather than prose.
- INC-000148's FC-000015 secondary is independently bounded to the reported cross-lane confusion and is not used to explain every ordering error.
- INC-000149 remains a negative control against inferring post-verification or control-state mechanisms from a post-update regression without evidence of the relevant verification/control state.

## Tranche totals

- Records reviewed: **4**
- Newly classified: **1** (`VIGIL-INC-000148`)
- Existing classified record retained after scheduled full review: **1** (`VIGIL-INC-000146`)
- Retained unclassified: **2** (`VIGIL-INC-000147`, `VIGIL-INC-000149`)
- Newly provisionally classified: **0**
- Newly classification-disputed: **0**
- Possible taxonomy-gap signals recorded: **1** (`VIGIL-INC-000147`)
- Structured external assessments added: **0**
- Existing structured external assessments substantively updated: **0**

### Corpus classification counts

| Status | Before Tranche 7 | After Tranche 7 |
| --- | ---: | ---: |
| classified | 94 | **95** |
| provisionally-classified | 2 | **2** |
| unclassified | 45 | **44** |
| classification-disputed | 4 | **4** |
| total active Incidents | 145 | **145** |

## Campaign completion

All **52 records in the frozen unclassified-campaign population have now received their scheduled deterministic current-taxonomy review**.

The campaign was executed in seven tranches against the current taxonomy available at each tranche, with later full reviews using taxonomy 0.6.6 after that release became current. Cross-cutting taxonomy corrections, including the AI-mediated deceptive economic-solicitation reconciliation, did not substitute for the scheduled full review of affected frozen records.

This audit closes the frozen seven-tranche re-adjudication campaign. Remaining `unclassified`, `provisionally-classified` and `classification-disputed` records remain valid corpus states and must not be treated as campaign incompleteness.
