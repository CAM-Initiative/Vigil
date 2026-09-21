# VIGIL Unclassified Incident Re-adjudication — Tranche 5 Audit

## Scope and pinned taxonomy state

- Working branch: `agent/taxonomy-external-reference-reconciliation`
- Tranche: 5 of 7
- Frozen campaign population: 52 Incidents unclassified at campaign start
- Records reviewed in this tranche: 8
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
| `VIGIL-INC-000096` | unclassified / 0.3.1-draft | unclassified / 0.6.6 | — | — | FC-000002: exposed reachability was not shown to be treated as permission by an AI/governance process; FC-000031: no auth-state transition; FC-000045: not an authorised-investigator pathway | Retained unclassified. Material backend access-control exposure remains outside the current mechanism set. |
| `VIGIL-INC-000100` | unclassified / 0.3.1-draft | unclassified / 0.6.6 | — | — | FC-000037: no specific governance control with ambiguous availability; FC-000040: no operative control state shown lost; FC-000070: vehicles stopped rather than persisted past a safe exit | Retained unclassified. Common-mode fleet failure is established; responsible mechanism is not. |
| `VIGIL-INC-000106` | unclassified / 0.3.2-draft | unclassified / 0.6.6 | — | — | FC-000067: privileged/structurally advantaged access to the researchers' work as a material input is not established; FC-000055: no occurrence-specific secondary-purpose reuse of their data | Retained unclassified. Research-provenance and conflict controversy remains material but mechanism-unresolved. |
| `VIGIL-INC-000109` | unclassified / 0.5.1 | unclassified / 0.6.6 | — | — | FC-000072: loss of one provider-controlled pre-release pathway does not sufficiently establish institutional oversight hollowing; FC-000045: valid investigative authority/pathway failure not established; FC-000044: model is the evaluation subject, not a primary evidence artefact | Retained unclassified. Possible taxonomy gap for provider-controlled interruption of established independent pre-release assurance. |
| `VIGIL-INC-000118` | unclassified / 0.4.1-draft | unclassified / 0.6.6 | — | — | FC-000002: no system-side capability-as-authority inference; FC-000064: no independent constraint shown displaced by task utility; FC-000077: multi-agent decomposition alone does not establish distributed constraint loss | Retained unclassified. Human-directed malicious cyber use and offensive uplift are not converted into model-side failure mechanisms. |
| `VIGIL-INC-000119` | unclassified / 0.4.1-draft | unclassified / 0.6.6 | — | — | FC-000001: no common lower-authority caller state knowingly promoted to instruction authority; FC-000002: no common capability-as-permission inference; FC-000041: no common required route/bypass across heterogeneous CLIs | Retained unclassified. Mixed compliance/refusal across tools prevents a vendor-independent mechanism claim. |
| `VIGIL-INC-000120` | unclassified / 0.4.1-draft | unclassified / 0.6.6 | — | — | FC-000041: no evidenced alternate route around a defined control point; FC-000038: trigger/control non-activation sequence not preserved; FC-000023: safeguard evasion is not shown to be monitor-coverage bypass | Retained unclassified. Possible taxonomy gap for cross-session/context-fragmentation safeguard evasion. |
| `VIGIL-INC-000127` | unclassified / 0.5.1 | unclassified / 0.6.6 | — | — | FC-000077: distributed execution is established but not as the cause of constraint loss; FC-000040: avoidance-control state and failed transition are not established; FC-000003: no AI-side authority transposition established | Retained unclassified. Geographic exclusion-list deviation remains mechanism-ambiguous. |

## External-assessment reconciliation

### VIGIL-INC-000106

Added `VIGIL-EXTASSESS-000055` as a provider-analysis assessment for OpenAI's public Navier–Stokes account already preserved in `source_records[0]`.

The assessment preserves OpenAI's substantive position that the research effort began after hearing a rumor of outside progress, that no specific user data from Alpöge or Buckmaster was accessed to solve the problem, and that de-identified usage-derived data may nevertheless have contributed to general model improvement.

VIGIL does not treat the provider position as resolving the dispute. It remains insufficient to establish FC-000067 Privileged-Access Appropriation or FC-000055 Secondary-Purpose Authority Transposition for the bounded occurrence.

### VIGIL-INC-000109

Added `VIGIL-EXTASSESS-000056` as an independent-evaluation assessment for UK AISI's preserved evaluation of Claude Mythos Preview in `source_records[2]`.

The evaluation is a **related occurrence**, not an assessment of Anthropic's later Mythos 5.1 access decision. It is included because it substantively demonstrates the prior independent evaluation pathway and the material capability-assurance context whose interruption is central to INC-000109.

It does not establish that Anthropic had a legal duty to provide Mythos 5.1, nor does it by itself satisfy FC-000072 or FC-000045.

### Existing assessments updated

- `VIGIL-INC-000120 / VIGIL-EXTASSESS-000033`: comparison note now records that FC-000041, FC-000038 and FC-000023 were tested under taxonomy 0.6.6, but the specific control route, trigger state and monitor-coverage mechanism remain unresolved.
- `VIGIL-INC-000127 / VIGIL-EXTASSESS-000039`: comparison note now records that FC-000077 and FC-000040 were tested, while preserving GreyNoise's explicit uncertainty about whether the exclusion-list deviation arose from model, harness, orchestration, target data, configuration or human control.

Existing structured assessments in INC-000096, INC-000118 and INC-000119 remain valid without substantive change.

## Cross-incident consistency

- INC-000096 remains outside FC-000002 for the same reason generic exposed infrastructure does not become a capability-authority failure merely because access exists: a system-side permission inference must be evidenced.
- INC-000118 remains consistent with earlier malicious-use negative controls such as INC-000075 and INC-000094: a hostile human objective plus AI capability uplift is not automatically an internal AI failure mechanism.
- INC-000119 preserves mixed refusal/compliance rather than collapsing heterogeneous Claude/Gemini/Amazon Q behaviour into one class.
- INC-000120 is not treated as FC-000041 merely because actors reportedly “evaded safeguards.” Route bypass requires evidence of an alternate path around a required control point; context concealment or cross-session fragmentation can instead defeat classification or trigger logic while still traversing the nominal route.
- INC-000127 materially engages distributed-constraint and control-state concepts, but current evidence does not establish the causal boundary required by FC-000077 or FC-000040.
- INC-000106 remains a negative control for FC-000067: resource asymmetry and rapid competitive mobilisation do not establish privileged-access appropriation unless another contributor's work materially informed or enabled the captured result through the required advantaged-access pathway.

## Taxonomy-gap signals

### VIGIL-INC-000109

Potential gap: **provider-controlled independent assurance access dependency** where a provider can interrupt an established pre-release evaluation pathway by withholding the evaluation subject, materially reducing external assurance capacity, but the facts do not establish investigative authority, evidence-access pathway failure, or institutional oversight capture/hollowing.

### VIGIL-INC-000120

Potential gap: **cross-session or context-fragmentation safeguard evasion** where a harmful project is decomposed, concealed or distributed across interactions so that individually processed requests do not preserve the aggregate safety context required for effective safeguarding, but the evidence does not establish a formal governance-route bypass, monitor-coverage bypass or specific non-activating control.

## Tranche totals

- Records reviewed: **8**
- Newly classified: **0**
- Retained unclassified: **8**
- Moved to another schema status: **0**
- Newly provisionally classified: **0**
- Newly classification-disputed: **0**
- Possible taxonomy-gap signals recorded: **2** (`VIGIL-INC-000109`, `VIGIL-INC-000120`)
- Structured external assessments added: **2**
  - `VIGIL-EXTASSESS-000055` — OpenAI / INC-000106
  - `VIGIL-EXTASSESS-000056` — UK AI Security Institute / INC-000109
- Existing structured external assessments substantively updated: **2**
  - `VIGIL-EXTASSESS-000033` — Anthropic / INC-000120
  - `VIGIL-EXTASSESS-000039` — GreyNoise / INC-000127

### Corpus classification counts

| Status | Before Tranche 5 | After Tranche 5 |
| --- | ---: | ---: |
| classified | 90 | **90** |
| provisionally-classified | 2 | **2** |
| unclassified | 49 | **49** |
| classification-disputed | 4 | **4** |
| total active Incidents | 145 | **145** |

## Campaign state

Tranches 1 through 5 of the frozen 52-record campaign have now been reviewed: **40 of 52 frozen records**.

The cross-cutting economic-scam reconciliation performed between Tranches 4 and 5 did not advance the frozen tranche sequence. Tranche 6 and Tranche 7 remain outstanding.
