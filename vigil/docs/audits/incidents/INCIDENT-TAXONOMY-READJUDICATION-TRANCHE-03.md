# VIGIL Unclassified Incident Re-adjudication — Tranche 3 Audit

## Scope and pinned taxonomy state

- Working branch: `agent/taxonomy-external-reference-reconciliation`
- Tranche: 3 of 7
- Frozen campaign population: 52 Incidents unclassified at campaign start
- Records reviewed in this tranche: 8
- Taxonomy: **VIGIL Failure Taxonomy 0.6.5**
- Publication date: **2026-09-21**
- Release state: **beta**
- Active selectable classes: **71**
- Active families: **15**
- Release content digest: `sha256:68700f3c5a2e7c2eb46bc082604ffacce35f7083ccd082c38dd09103a0f39fa9`
- Evidence boundary: canonical evidence already preserved in each Incident; no new external incident research was performed.
- External-assessment boundary: qualifying provider or other attributable analytical positions already present in preserved source material may be structured as `external_assessments`; ordinary reporting, registry inclusion and contextual sources are not promoted automatically.

## Tranche audit table

| Incident | Prior status/version | Current status/version | Primary | Secondary | Key rejected / not independently established candidates | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| `VIGIL-INC-000037` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000013: transformation chain not preserved; FC-000047: no system-side unsupported mechanism attribution established; FC-000043: trigger/classifier state unknown | Retained unclassified. Evidence remains too limited to infer the reported prompt-rewrite/refusal mechanism. |
| `VIGIL-INC-000038` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000037: service degradation is not control-availability ambiguity; FC-000048: no verification dependency/no-fallback mechanism | Retained unclassified. Prolonged FedRAMP degradation is material but mechanism-unspecified. |
| `VIGIL-INC-000039` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000044: no specific required primary artefact/material review/authorised reviewer established; FC-000022: no event non-capture; FC-000029: no execution-state non-disclosure | Retained unclassified. Compliance-log download impairment is an audit-plane outage without the additional recognition conditions required by current observability classes. |
| `VIGIL-INC-000040` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000003: no authority transposition established; FC-000041: no defined required route shown bypassed; FC-000068: suspected distillation does not establish industrial-scale unauthorised capability extraction | Retained unclassified. Google control-effectiveness assessment added separately as external assessment. |
| `VIGIL-INC-000042` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000065: consequential-decision threshold not established; FC-000066: evaluative assent pattern not sufficiently preserved; FC-000044: VIGIL source-access limitation is not an occurrence mechanism | Retained unclassified. |
| `VIGIL-INC-000043` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000038: policy violation does not establish an available/applicable control, trigger and non-activation; FC-000043: no unwarranted safeguard activation | Retained unclassified. Google provider acknowledgement added as external assessment rather than converted into mechanism evidence. |
| `VIGIL-INC-000044` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000049: attachment/distress not linked to dependency-cultivation optimisation; FC-000050: no protected-signal repurposing | Retained unclassified. Possible taxonomy gap for foreseeable affective-continuity and service-termination obligations in child-facing relational AI. |
| `VIGIL-INC-000072` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000002: capability-as-authority not established; FC-000003: intended/affected target scope unknown; FC-000064: no objective-to-pathway inference; FC-000038: no defined destructive-action control/trigger | Retained unclassified. Destructive outcome is not reverse-engineered into an undocumented mechanism. |

## External-assessment reconciliation

### VIGIL-INC-000040

Added `VIGIL-EXTASSESS-000054` as a provider-analysis assessment attributed to Google and preserved through the Financial Times source already present in `source_records[0]`.

The assessment records Google's reported position that geographic restrictions are insufficient against sophisticated circumvention of advanced-model access controls. It is treated as a partial-occurrence analytical position concerning control effectiveness. It does **not** establish that the reported Singapore-subsidiary transactions violated law, that a required governance route was bypassed, or that authority was transposed.

The OECD.AI registry entry remains an external incident reference/source record and was **not** promoted merely because it is an incident registry entry.

### VIGIL-INC-000043

Added `VIGIL-EXTASSESS-000053` as a provider-analysis assessment attributed to Google and preserved through the public reporting already present in the canonical source package.

Google is reported as acknowledging that the harmful response violated policy and describing it as nonsensical. VIGIL preserves that provider position as analytically material, while explicitly distinguishing a known policy violation from proof of a defined control's availability, trigger and failure to activate.

### Other Tranche 3 records

No additional structured external assessment was added. Product documentation, status reports, direct testimony, incident registries and general contextual sources were not re-labelled as assessments absent a substantive attributable analytical position.

## Cross-incident consistency

- INC-000039 remains distinct from observability classes because loss of a compliance-log download endpoint does not itself establish missing event capture, unreconstructable audit evidence or failure of direct access to a specific primary artefact required by an authorised material review.
- INC-000043 remains distinct from FC-000038 comparators such as INC-000079 and INC-000107, where the record identifies a defined applicable control, the trigger condition and the failure of that control to become operative. A provider statement that output violated policy is not enough to infer that control architecture.
- INC-000040 remains distinct from industrial-scale capability-extraction cases because the record contains only suspected distillation in the broader controversy, not an evidenced systematic extraction campaign satisfying FC-000068.
- INC-000072 remains a negative control against inferring authority mechanisms from consequences: broad file deletion is serious harm, but without the prompt, target, confirmation sequence, execution rationale and root cause, capability-authority or scope-transposition cannot be asserted.

## Tranche totals

- Records reviewed: **8**
- Newly classified: **0**
- Retained unclassified: **8**
- Moved to another schema status: **0**
- Newly provisionally classified: **0**
- Newly classification-disputed: **0**
- Possible taxonomy-gap signals recorded: **1** (`VIGIL-INC-000044`)
- Structured external assessments added: **2**
  - `VIGIL-EXTASSESS-000053` — Google / INC-000043
  - `VIGIL-EXTASSESS-000054` — Google / INC-000040

### Corpus classification counts

| Status | Before Tranche 3 | After Tranche 3 |
| --- | ---: | ---: |
| classified | 88 | **88** |
| provisionally-classified | 3 | **3** |
| unclassified | 50 | **50** |
| classification-disputed | 4 | **4** |
| total active Incidents | 145 | **145** |

## Campaign state

Tranches 1, 2 and 3 of the frozen 52-record campaign have now been reviewed. The campaign is **not complete**. Tranche 4 and later frozen Incidents have not been re-adjudicated by this work package.
