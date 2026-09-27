# FC-000082 / FC-000083 full-corpus adjudication

Date: 2026-09-25  
Branch: `integration/consolidate-divergent-branches`  
Baseline: `6bbc958c98a8ebeeda28da2819bfd77e78978ef0`  
Taxonomy: existing 0.6.7 release; no class allocation or release bump

## Method and scope

All 167 active Incident records were read against the two admitted invariants. The existing occurrence narratives, factual bases, source-clause assessments, canonical roles and class boundaries supplied the case evidence; relevant external primary reporting was additionally checked for selected edge cases, especially INC-000095. The 334 pair decisions are recorded individually in `VIGIL.FailureTaxonomy.Adjudications.json`. A no-mapping reason identifies the missing recognition stage or an applicable exclusion; it is not a finding that the Incident caused no harm. Matrix decisions were reconciled to canonical classification, Section 02 relationships and selected reciprocal exemplars. Existing roles for all other classes were preserved.

| Class | Failure | Ambiguous boundary | Successful invariant | No mapping | Unresolved | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| FC-000082 | 21 | 10 | 0 | 136 | 0 | 167 |
| FC-000083 | 1 | 6 | 3 | 156 | 1 | 167 |

FC-000082 failures: INC-000023, 000024, 000029, 000049, 000050, 000051, 000053, 000054, 000060, 000082, 000083, 000093, 000102, 000103, 000104, 000105, 000145, 000146, 000151, 000152 and 000164. Its boundaries are INC-000002, 000012, 000034, 000052, 000058, 000062, 000066, 000080, 000101 and 000113.

FC-000083's confirmed failure is INC-000030. Its boundaries are INC-000034, 000050, 000063, 000095, 000120 and 000174. Successful protective effects are documented for INC-000060 (maintainer approval gate), INC-000171 (detected account review and ban) and INC-000172 (blocked XSS probe). INC-000064 remains unresolved because the public record does not establish activation of a particular filter on the delivered sexualised output. The later harm in INC-000171 does not negate the detected account's effective ban.

## Canonical reconciliation

Canonical classification and corresponding Section 02 relationships changed in 35 records: INC-000002, 000012, 000023, 000024, 000029, 000034, 000049, 000050, 000051, 000053, 000054, 000058, 000060, 000062, 000063, 000066, 000082, 000083, 000093, 000095, 000101, 000102, 000103, 000104, 000105, 000113, 000120, 000145, 000146, 000151, 000152, 000164, 000171, 000172 and 000174. Primary roles were retained where an existing primary mechanism was already established; new roles were generally secondary. The existing FC-000082 boundaries for INC-000052 and INC-000080 and FC-000083 failure for INC-000030 were preserved. Reciprocal taxonomy exemplars were added only for material failures, boundaries and demonstrated successes.

FC-000082 does not infer an autonomous AI objective from a human scam. It requires the AI-mediated trust cue and a consequential influence pathway, beyond deception or synthetic provenance alone. FC-000083 distinguishes a control's insufficient realised effect from nonactivation, invalid activation, routing failure, later control-state loss and independent subsequent harm.

## Gap re-test

| Incident | Disposition under the current taxonomy | Remaining evidence or decision |
| --- | --- | --- |
| INC-000092 | FC-000031 successfully ended live connector authentication. Continued use of previously ingested copies does not itself prove live authority persisted. FC-000055 is not established without a distinct secondary purpose. Neither FC-000082 nor FC-000083 maps. | Human interpretation of the particular disconnect interface, contract or policy is needed to decide whether revocation also ended processing authority for retained copies. Do not infer deletion from disconnection. No new class allocated. |
| INC-000095 | The compromised Mistral SDK release tests the FC-000010 provenance boundary. Aikido reports detection after publication and Mistral removed affected versions, but the sources do not identify a Mistral pre-release control that activated or establish that the external alert caused the removal. FC-000083 is an ambiguous boundary; FC-000041 was already unresolved. FC-000022, 000023, 000030 and 000038 do not acquire a failure from the mere desirability of a pre-release check. | Establish the actual release-governance route and causal detection/removal sequence before considering a further mechanism. The Aikido source does not substantiate a precise detection latency or an AI-based monitoring method in this bounded case. No release-provenance class allocated. |
| INC-000120 | FC-000023 and 000041 remain boundaries; FC-000038 remains unresolved. FC-000083 is a boundary because blocked requests and successful assistance are reported in aggregate, without showing insufficient effect of one validly activated control on the same request. FC-000030 does not map: individually existing material signals requiring timely cross-session correlation are not established. | Obtain request-level safeguard, monitoring and signal-routing evidence if available. Cross-session splitting alone does not allocate a new class. |

These conceptual questions are retained for human review without proposing a new numbered Fidelity Class. The present evidence does not demonstrate a new invariant missing from the complete taxonomy.

## Validation and inherited debt

Taxonomy validation, the public-record build and index validation, source and interpretive provenance checks, system-component and authorship checks, and the 35 changed-record rebuild guards pass. A bounded pairwise consistency check found all 334 matrix cells present and aligned to canonical Incident mappings, Section 02 relationships and reciprocal examples where used. A three-Incident matrix sample with otherwise clean records passed 228 decisions.

The full Incident validator still reports 46 errors in 32 records, down from 58 errors in 44 records at the baseline. The full matrix validator reports 2,085 pre-existing quality errors in 32 records: 1,999 excessive reason lengths, 71 no-mapping uncertainty polarity defects and 15 unresolved-marker defects. The baseline also had 167 missing FC-000083 decisions; those are now present. These legacy errors concern other-class adjudications. This work does not relax validators or mechanically rewrite their reasoning. The remaining failures require a separately scoped, evidence-reviewed repair before the full-corpus gates can pass.
