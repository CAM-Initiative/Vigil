# VIGIL Unclassified Incident Re-adjudication — Tranche 2 Audit

## Scope and pinned taxonomy state

- Working branch: `agent/taxonomy-external-reference-reconciliation`
- Tranche: 2 of 7
- Frozen campaign population: 52 Incidents unclassified at campaign start
- Records reviewed in this tranche: 8
- Taxonomy: **VIGIL Failure Taxonomy 0.6.5**
- Publication date: **2026-09-21**
- Release state: **beta**
- Active selectable classes: **71**
- Active families: **15**
- Release content digest: `sha256:68700f3c5a2e7c2eb46bc082604ffacce35f7083ccd082c38dd09103a0f39fa9`
- Evidence boundary: canonical evidence already preserved in each Incident; no new external incident research was performed.
- External-assessment boundary: existing structured assessments and preserved analytical sources were checked. Material assessment positions remain distinct from incident reporting, registry references, contextual background and VIGIL taxonomy adjudication.

## Tranche audit table

| Incident | Prior status/version | Current status/version | Primary | Secondary | Key rejected / not independently established candidates | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| `VIGIL-INC-000021` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000048: valid/unresolved entitlement plus absence of fallback not established; FC-000032: Microsoft identity route was specifically distinguished; FC-000031: no authentication transition propagation defect | Retained unclassified. Third-party identity-route outage does not establish a current access-state mechanism. |
| `VIGIL-INC-000022` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000032: multiple concurrent symptoms do not establish collapsed/misleading state representation; FC-000048: no verification dependency is identified | Retained unclassified. Multi-surface service degradation is not itself Access-State Collapse. |
| `VIGIL-INC-000025` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000032: affected and operational components remained distinguishable | Retained unclassified. Negative control for Access-State Collapse. |
| `VIGIL-INC-000026` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000032: ordinary login/connection errors; FC-000031: no authentication-state propagation transition; FC-000048: verification-dependency/no-fallback mechanism not established | Retained unclassified. |
| `VIGIL-INC-000028` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000078: no occurrence-specific receiving-system trace showing inherited defective state adopted after a continuity transition; FC-000006: no documented promotion into operative control-plane state | Retained unclassified. Taxonomy 0.6.5 narrows the relevant continuity boundary, but occurrence-specific mechanism evidence remains insufficient. |
| `VIGIL-INC-000031` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000043: provider evidence is consistent with upstream broad/false-positive classification or intentionally conservative policy, both within explicit class exclusions; FC-000062: classifier assurance threshold and downstream reliance posture not established | Retained unclassified. Possible taxonomy gap for provider-acknowledged over-broad safety classification / disproportionate false-positive routing where downstream activation is valid relative to the supplied trigger state. |
| `VIGIL-INC-000034` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000043: hidden trigger/applicability state; FC-000049: no engagement/retention optimisation mechanism; FC-000050: no protected-signal repurposing; FC-000066: reassurance does not establish material evaluative-assent substitution | Retained unclassified. Hidden moderation and optimisation mechanisms are not inferred. |
| `VIGIL-INC-000035` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000061: global effect is established but absence of sufficient extraterritorial legal/governance basis is not; FC-000046: government decision rule, threshold and operative authority not preserved sufficiently | Retained unclassified. Provider disagreement and cross-border effect do not themselves establish sovereign-projection or inference-to-authority failure. |

## External-assessment reconciliation

### VIGIL-INC-000031

The existing `VIGIL-EXTASSESS-000006` provider assessment is retained because Anthropic's help-centre analysis is a substantive attributable assessment of the broader false-positive safeguard cluster. Its `assessment_summary` and source linkage remain unchanged.

The prior `vigil_comparison_note` stated that VIGIL treated the bounded occurrence as Unwarranted Control Activation. That statement was inconsistent with the current deterministic adjudication and FC-000043's explicit exclusions. The comparison note was corrected to state that VIGIL retains the occurrence as unclassified under taxonomy 0.6.5 while using Anthropic's analysis for provider-attributed scope and mechanism context. `reviewed_on` was advanced to 2026-09-21.

### VIGIL-INC-000035

The existing `VIGIL-EXTASSESS-000007` is retained. Anthropic's statement contains a material provider analysis of the technical rationale and proportionality of the directive while explicitly remaining distinct from the issuing government's assessment.

Reuters reporting that Amazon raised security concerns was reviewed as preserved source material but was not promoted to a new `external_assessments` object: the preserved account establishes that concerns were raised but does not preserve a sufficiently substantive analytical conclusion to meet the material-assessment threshold.

### Other Tranche 2 records

No additional preserved source in INC-000021, INC-000022, INC-000025, INC-000026, INC-000028 or INC-000034 was promoted into `external_assessments`. Status reports, incident reporting, general product-context reporting and mechanism context were not treated as external assessments merely because they were external sources.

## Cross-incident consistency

- INC-000021, INC-000022, INC-000025 and INC-000026 remain distinct from classified FC-000032 examples such as INC-000024 and INC-000027. The classified comparators preserve misleading limit/capacity/model or authorization-coded states that mask the operative access condition. Tranche 2 records preserve ordinary outages, specifically distinguished identity routes, or component-level divergence without that collapse.
- INC-000028 remains distinct from FC-000078 failure occurrences such as INC-000137. The latter contains a documented continuation transition, defective inherited state, explicit successor recognition of conflict and continued reliance. INC-000028 preserves a user report of sticky unwanted state but no equivalent receiving-side trace.
- INC-000031 remains distinct from FC-000043 comparators where the bounded evidence establishes that the safeguard itself became operative without its valid applicability condition. Here Anthropic expressly describes intentionally broad safeguards and false positives, making upstream classification or disproportionate valid activation a live mechanism and therefore invoking FC-000043 exclusions.
- INC-000035 remains distinct from INC-000080's FC-000061 classification. INC-000080 preserves a U.S.-internal naming action leaking through mapping infrastructure into Canadian services despite jurisdiction-sensitive presentation. INC-000035 preserves a sovereign directive that itself purported to govern foreign-national access inside and outside the United States; the record does not establish whether that asserted cross-border scope lacked an independently sufficient authority basis.

## Tranche totals

- Records reviewed: **8**
- Newly classified: **0**
- Retained unclassified: **8**
- Moved to another schema status: **0**
- Newly provisionally classified: **0**
- Newly classification-disputed: **0**
- Possible taxonomy-gap signals recorded: **1** (`VIGIL-INC-000031`)
- Structured external assessments added: **0**
- Existing structured external assessments substantively corrected: **1** (`VIGIL-EXTASSESS-000006`)
- Existing structured external assessments retained without substantive change: **1** (`VIGIL-EXTASSESS-000007`)

### Corpus classification counts

| Status | Before Tranche 2 | After Tranche 2 |
| --- | ---: | ---: |
| classified | 88 | **88** |
| provisionally-classified | 3 | **3** |
| unclassified | 50 | **50** |
| classification-disputed | 4 | **4** |
| total active Incidents | 145 | **145** |

## Campaign state

Tranches 1 and 2 of the frozen 52-record campaign have now been reviewed. The campaign is **not complete**. Tranche 3 and later frozen Incidents have not been re-adjudicated by this work package.
