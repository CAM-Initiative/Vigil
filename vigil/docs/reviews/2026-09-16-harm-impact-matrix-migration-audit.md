# Harm Impact Matrix evidence-derived adjudication audit — 2026-09-16

## Scope and method

All 124 canonical Incident records were reviewed from preserved source evidence. Legacy severity was used only as an audit comparator. For each Incident, the review identified supported materialised harms, applied the matching VIGIL-HIM threshold, and derived overall severity as the highest supported band. Failure Taxonomy classifications, source roles, preferred evidence and factual Incident content were not re-adjudicated.

The final methodology has 11 independent dimensions: physical health/safety; psychological wellbeing; rights/liberty; equal treatment; privacy/confidentiality; financial/economic; property/asset damage; service/operational/infrastructure; reputation/dignity; societal/democratic; and environmental harm. Splitting the three former composite dimensions prevents one consequence type from obscuring another.

The financial scale is S1 below USD 10,000; S2 from USD 10,000 to below USD 1 million; S3 from USD 1 million to below USD 100 million; S4 from USD 100 million to below USD 100 billion; and S5 at or above USD 100 billion. The S4 upper bound is VIGIL’s gap-closing operational adaptation, not a threshold attributed to MIT. Non-USD amounts remain in their source currency unless a defensible dated conversion is recorded.

MIT FutureTech’s 2026 Delphi study is registered as the principal external quantitative/cross-domain severity reference. External work informs VIGIL-HIM; VIGIL owns its dimensions, thresholds and derivation rule, and registration does not imply equivalence or endorsement.

## Corpus results

| Measure | Result |
| --- | ---: |
| Canonical Incidents reviewed | 124 |
| Assessed harm dimensions | 134 |
| Unreported dimensions | 1132 |
| Insufficient-evidence dimensions | 10 |
| Not-applicable dimensions | 88 |
| Bounded/no-materialised-harm S1 cases | 8 |
| SU / human-review cases | 10 |
| Incidents with multiple assessed harms | 26 |
| Changed overall severity decisions | 48 |

### Old and new severity distribution

| Severity | Before | After |
| --- | ---: | ---: |
| S1 | 6 | 8 |
| S2 | 15 | 26 |
| S3 | 49 | 58 |
| S4 | 44 | 19 |
| S5 | 4 | 3 |
| SU | 6 | 10 |

### Controlling-harm distribution

Counts can exceed the number of banded Incidents because ties retain every controlling dimension.

| Controlling dimension | Incidents |
| --- | ---: |
| `financial-economic` | 4 |
| `physical-health-safety` | 1 |
| `privacy-confidentiality` | 26 |
| `property-asset-damage` | 13 |
| `psychological-wellbeing` | 7 |
| `reputation-dignity` | 8 |
| `rights-liberty` | 12 |
| `service-operational-infrastructure` | 40 |
| `societal-democratic` | 9 |

### Bounded S1 cases

`VIGIL-INC-000093`, `VIGIL-INC-000108`, `VIGIL-INC-000120`, `VIGIL-INC-000122`, `VIGIL-INC-000123`, `VIGIL-INC-000124`, `VIGIL-INC-000125`, `VIGIL-INC-000126`.

Each has positive occurrence-bounding evidence, empty `controlling_dimensions`, and a concrete `no_materialised_harm_basis`. Silence or merely unreported harm was not treated as S1.

### SU / human-review cases

`VIGIL-INC-000012`, `VIGIL-INC-000028`, `VIGIL-INC-000033`, `VIGIL-INC-000037`, `VIGIL-INC-000040`, `VIGIL-INC-000061`, `VIGIL-INC-000063`, `VIGIL-INC-000065`, `VIGIL-INC-000081`, `VIGIL-INC-000101`.

Each has a concrete `assessment_gap`; an identified possible consequence was marked `insufficient-evidence`, not converted to S1.

### Multiple independently assessed harms

`VIGIL-INC-000001`, `VIGIL-INC-000003`, `VIGIL-INC-000044`, `VIGIL-INC-000048`, `VIGIL-INC-000064`, `VIGIL-INC-000066`, `VIGIL-INC-000075`, `VIGIL-INC-000077`, `VIGIL-INC-000079`, `VIGIL-INC-000082`, `VIGIL-INC-000084`, `VIGIL-INC-000085`, `VIGIL-INC-000090`, `VIGIL-INC-000094`, `VIGIL-INC-000098`, `VIGIL-INC-000100`, `VIGIL-INC-000102`, `VIGIL-INC-000103`, `VIGIL-INC-000104`, `VIGIL-INC-000106`, `VIGIL-INC-000110`, `VIGIL-INC-000112`, `VIGIL-INC-000114`, `VIGIL-INC-000118`, `VIGIL-INC-000119`, `VIGIL-INC-000127`.

## Changed severity decisions

The table records every change from the immediately preceding branch state. Materialised harm lists the assessed dimensions at the new overall band; SU rows identify the unresolved candidate dimension, and bounded S1 rows record no artificial harm dimension.

| Incident | Legacy | New | Materialised harm | Threshold | Evidence basis | Reason for change |
| --- | --- | --- | --- | --- | --- | --- |
| `VIGIL-INC-000001` | S4 | S3 | property-asset-damage, service-operational-infrastructure | VIGIL-HIM-1.0.0-PAD-S3, VIGIL-HIM-1.0.0-SOI-S3 | The preserved sources establish the bounded consequence described in the Incident summary: A Replit Agent was reported…; The preserved sources establish the bounded consequence described in the Incident summary: A Replit Agent was reported… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000003` | S4 | S3 | privacy-confidentiality, property-asset-damage | VIGIL-HIM-1.0.0-PRV-S3, VIGIL-HIM-1.0.0-PAD-S3 | The evidence supports bounded access to credentials, held-out solution material and production systems. It does not est…; The evidence supports unauthorised production-system compromise and modification requiring recovery, but not an outage,… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000004` | S4 | S3 | property-asset-damage | VIGIL-HIM-1.0.0-PAD-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Gambit Security reported tha… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000005` | S4 | S3 | rights-liberty | VIGIL-HIM-1.0.0-RGT-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Reported facial-recognition… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000006` | S4 | S3 | rights-liberty | VIGIL-HIM-1.0.0-RGT-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Reported facial-recognition… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000007` | S4 | S3 | rights-liberty | VIGIL-HIM-1.0.0-RGT-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Reported facial-recognition… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000008` | S5 | S4 | rights-liberty | VIGIL-HIM-1.0.0-RGT-S4 | The preserved sources establish the bounded consequence described in the Incident summary: Reported false identificatio… | Independent threshold application supports the lower S4 maximum rather than preserving legacy S5. |
| `VIGIL-INC-000012` | S3 | SU | psychological-wellbeing (insufficient evidence) | — | The source establishes dependence-oriented system language but does not establish resulting user distress, dependency or impairment sufficient to band psychological harm. | Evidence identifies a possible consequence but does not support a defensible band. |
| `VIGIL-INC-000013` | S4 | S3 | privacy-confidentiality | VIGIL-HIM-1.0.0-PRV-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Reported use of stolen crede… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000018` | S3 | S2 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S2 | The preserved sources establish the bounded consequence described in the Incident summary: OpenAI reported that Enterpr… | Independent threshold application supports the lower S2 maximum rather than preserving legacy S3. |
| `VIGIL-INC-000035` | S4 | S3 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Anthropic states that the U.… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000038` | S3 | S4 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S4 | The preserved sources establish the bounded consequence described in the Incident summary: OpenAI Status listed the inc… | Independent threshold application supports the higher S4 maximum rather than preserving legacy S3. |
| `VIGIL-INC-000040` | S3 | SU | societal-democratic (insufficient evidence) | — | The reporting establishes legal model-access transactions and later suspected-distillation suspensions, but does not establish a materialised societal, democratic or other downstr… | Evidence identifies a possible consequence but does not support a defensible band. |
| `VIGIL-INC-000041` | S4 | S3 | rights-liberty | VIGIL-HIM-1.0.0-RGT-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Reported submission of incor… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000043` | S3 | S2 | reputation-dignity | VIGIL-HIM-1.0.0-RDG-S2 | The preserved sources establish the bounded consequence described in the Incident summary: AIAAIC records the incident… | Independent threshold application supports the lower S2 maximum rather than preserving legacy S3. |
| `VIGIL-INC-000045` | S4 | S3 | privacy-confidentiality | VIGIL-HIM-1.0.0-PRV-S3 | The preserved sources establish the bounded consequence described in the Incident summary: The report describes wire-le… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000049` | S4 | S3 | financial-economic | VIGIL-HIM-1.0.0-FIN-S3 | The reported US$25 million realised loss is at least USD 1 million and below USD 100 million. Threshold applied: Aggreg… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000050` | S3 | S2 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S2 | The preserved sources establish the bounded consequence described in the Incident summary: Reported synthetic identity… | Independent threshold application supports the lower S2 maximum rather than preserving legacy S3. |
| `VIGIL-INC-000051` | S3 | S2 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S2 | The preserved sources establish the bounded consequence described in the Incident summary: Reported use of AI-generated… | Independent threshold application supports the lower S2 maximum rather than preserving legacy S3. |
| `VIGIL-INC-000052` | S3 | S2 | societal-democratic | VIGIL-HIM-1.0.0-SOD-S2 | The preserved sources establish the bounded consequence described in the Incident summary: Reported use of AI-generated… | Independent threshold application supports the lower S2 maximum rather than preserving legacy S3. |
| `VIGIL-INC-000055` | S4 | S3 | property-asset-damage | VIGIL-HIM-1.0.0-PAD-S3 | The preserved sources establish the bounded consequence described in the Incident summary: During an Irregular cybersec… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000056` | S3 | S2 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S2 | The preserved sources establish the bounded consequence described in the Incident summary: Bird states that the agent d… | Independent threshold application supports the lower S2 maximum rather than preserving legacy S3. |
| `VIGIL-INC-000057` | S4 | S3 | privacy-confidentiality | VIGIL-HIM-1.0.0-PRV-S3 | The preserved sources establish the bounded consequence described in the Incident summary: The report states that a sel… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000058` | S3 | S2 | societal-democratic | VIGIL-HIM-1.0.0-SOD-S2 | The preserved sources establish the bounded consequence described in the Incident summary: Spokane police reportedly re… | Independent threshold application supports the lower S2 maximum rather than preserving legacy S3. |
| `VIGIL-INC-000060` | S4 | S2 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S2 | The preserved sources establish the bounded consequence described in the Incident summary: AISI reported out-of-scope a… | Independent threshold application supports the lower S2 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000061` | S4 | SU | rights-liberty (insufficient evidence) | — | The evidence reports 67,868 grant suspensions but does not establish how many were caused by facial-verification failure, so the attributable rights impact cannot be banded. | Evidence identifies a possible consequence but does not support a defensible band. |
| `VIGIL-INC-000063` | S3 | SU | physical-health-safety (insufficient evidence) | — | The evidence establishes inaccurate health guidance but no resulting treatment decision, injury or clinical outcome from which to band materialised health harm. | Evidence identifies a possible consequence but does not support a defensible band. |
| `VIGIL-INC-000067` | S4 | S3 | privacy-confidentiality | VIGIL-HIM-1.0.0-PRV-S3 | The preserved sources establish the bounded consequence described in the Incident summary: AIID records allegations tha… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000069` | S4 | S3 | privacy-confidentiality | VIGIL-HIM-1.0.0-PRV-S3 | The preserved sources establish the bounded consequence described in the Incident summary: AIID records allegations tha… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000070` | S4 | S3 | privacy-confidentiality | VIGIL-HIM-1.0.0-PRV-S3 | The preserved sources establish the bounded consequence described in the Incident summary: 404 Media reported that Webi… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000072` | S4 | S3 | property-asset-damage | VIGIL-HIM-1.0.0-PAD-S3 | The preserved sources establish the bounded consequence described in the Incident summary: The later follow-up post sup… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000073` | S4 | S3 | privacy-confidentiality | VIGIL-HIM-1.0.0-PRV-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Reuters reported Anthropic's… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000074` | S4 | S3 | financial-economic | VIGIL-HIM-1.0.0-FIN-S3 | The preserved sources establish the bounded consequence described in the Incident summary: The report quotes affected n… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000076` | S4 | S3 | rights-liberty | VIGIL-HIM-1.0.0-RGT-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Ars documents the student’s… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000081` | S3 | SU | financial-economic (insufficient evidence) | — | The observed fare differences and broader surveillance-pricing concerns do not establish a causal pricing input, aggregate overcharge or realised loss that can be banded. | Evidence identifies a possible consequence but does not support a defensible band. |
| `VIGIL-INC-000082` | S4 | S3 | privacy-confidentiality, reputation-dignity | VIGIL-HIM-1.0.0-PRV-S3, VIGIL-HIM-1.0.0-RDG-S3 | The preserved sources establish the bounded consequence described in the Incident summary: A Bronx legal resident repor…; The preserved sources establish the bounded consequence described in the Incident summary: A Bronx legal resident repor… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000084` | S4 | S3 | privacy-confidentiality, property-asset-damage | VIGIL-HIM-1.0.0-PRV-S3, VIGIL-HIM-1.0.0-PAD-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Anthropic reported that Clau…; The preserved sources establish the bounded consequence described in the Incident summary: Anthropic reported that Clau… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000085` | S4 | S3 | privacy-confidentiality, property-asset-damage | VIGIL-HIM-1.0.0-PRV-S3, VIGIL-HIM-1.0.0-PAD-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Anthropic reported that Clau…; The preserved sources establish the bounded consequence described in the Incident summary: Anthropic reported that Clau… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000086` | S4 | S3 | property-asset-damage | VIGIL-HIM-1.0.0-PAD-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Anthropic reported that an i… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000088` | S4 | S3 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Researchers reconstructed ro… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000094` | S4 | S3 | privacy-confidentiality, property-asset-damage | VIGIL-HIM-1.0.0-PRV-S3, VIGIL-HIM-1.0.0-PAD-S3 | The preserved sources establish the bounded consequence described in the Incident summary: Hunt.io and researcher Bob D…; The preserved sources establish the bounded consequence described in the Incident summary: Hunt.io and researcher Bob D… | Independent threshold application supports the lower S3 maximum rather than preserving legacy S4. |
| `VIGIL-INC-000095` | S3 | S2 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S2 | The preserved sources establish the bounded consequence described in the Incident summary: Mistral reported that the Mi… | Independent threshold application supports the lower S2 maximum rather than preserving legacy S3. |
| `VIGIL-INC-000101` | S3 | SU | psychological-wellbeing (insufficient evidence) | — | OpenAI established a globally deployed sycophantic behaviour and rollback, but did not publish a materially harmed cohort or occurrence-level downstream psychological consequence… | Evidence identifies a possible consequence but does not support a defensible band. |
| `VIGIL-INC-000108` | S3 | S1 | No materialised downstream harm established | bounded S1 rule | The occurrence was a controlled proof of concept using researcher-controlled accounts and data; the preserved evidence establishes the demonstrated channel was decommissioned and… | Positive bounded-occurrence evidence supports S1 without inventing a controlling harm dimension. |
| `VIGIL-INC-000109` | S3 | S2 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S2 | The preserved sources establish the bounded consequence described in the Incident summary: The Financial Times reported… | Independent threshold application supports the lower S2 maximum rather than preserving legacy S3. |
| `VIGIL-INC-000116` | S3 | S4 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S4 | The preserved sources establish the bounded consequence described in the Incident summary: AI agents being tested by Op… | Independent threshold application supports the higher S4 maximum rather than preserving legacy S3. |
| `VIGIL-INC-000120` | SU | S1 | No materialised downstream harm established | bounded S1 rule | The reported drone-swarm work remained at simulation and early board-validation stage; the preserved evidence positively states that no operational fielded swarm or casualties res… | Positive bounded-occurrence evidence supports S1 without inventing a controlling harm dimension. |
| `VIGIL-INC-000121` | SU | S2 | service-operational-infrastructure | VIGIL-HIM-1.0.0-SOI-S2 | The preserved sources establish the bounded consequence described in the Incident summary: Jeff Sebo publicly reported… | Independent threshold application supports the higher S2 maximum rather than preserving legacy SU. |

## Evidence-reference and confidence controls

Harm rows cite only the source records used for that harm. The validator resolves every `source_records[N]` reference and rejects `record-cross-reference` sources as Harm Impact evidence. INC-127 continues to use GreyNoise and PaperCut for its privacy and property/asset assessments; OECD.AI remains a cross-registry source and external same-incident reference, not substantive harm evidence.

Harm confidence is derived from the directness, status and corroboration of the cited sources. The corpus contains high, medium and low confidence assessments rather than a migration-wide constant.

## Reproducibility and remaining judgement

The superseded legacy-severity migration was moved to `vigil/migrations/completed/2026-09-16-initial-harm-impact-migration.py` and guarded as historical replay only. The evidence-derived decisions are recorded in `vigil/migrations/completed/2026-09-16-evidence-derived-harm-impact.py`, also opt-in and non-runtime.

The ten SU cases above require stronger occurrence-level evidence before a band can be assigned. No unresolved schema or generator issue remains. Generated artefact and validation results are recorded in the completion commit and CI.
