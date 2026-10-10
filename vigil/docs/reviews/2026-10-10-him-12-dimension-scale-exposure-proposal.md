# VIGIL-HIM — integrate population scale and exposure within each dimension

**Date:** 2026-10-10  
**Status:** NON-AUTHORITATIVE VERSIONED DRAFT — no change to active HIM 1.0.1  
**Branch:** `agent/incident-ecosystem-ingestion`  
**Companion machine-readable proposal:** `vigil/methodologies/proposals/VIGIL.HarmImpactMatrix.v1.1.0-proposal.json`

## Maintainer instruction and correction to prior framing

The maintainer requested that **quantitative impact/exposure/population-scale criteria be incorporated directly in each S1–S5 Harm Impact dimension**, following the existing financial-economic monetary and service-operational user/time anchors. **No second impact or reach matrix, no new overall score, and no population-size multiplier.**

The 2026-10-10 INC-000012 preliminary review considered improving psychological guidance within the existing 11 dimensions. That narrower preference is superseded **for proposal purposes only** by the separately requested candidate **12th dimension: Relational Integrity and Autonomy**. The active canonical model remains 11 dimensions and version 1.0.1 until explicitly versioned and migrated.

## Draft quantitative population bands, embedded in the same severity criteria

| Band | Affected-population *alternative anchor* (not automatic score) | Required domain consequence |
|---|---|---|
| S1 | Affirmatively demonstrated minimal/no harm; no inference from silence or unknown counts | Evidence positively supports S1; some existing financial or service S1 thresholds allow negligible quantified loss or interruption |
| S2 | 1–99 demonstrably affected persons | Minor, transient and readily reversible realised impact |
| S3 | 100–9,999 demonstrably affected persons **or** independently moderate harm on a smaller scale | Meaningful, bounded realised impact |
| S4 | 10,000–999,999 demonstrably affected persons **or** independently substantial harm on a smaller scale | Substantial, persistent or otherwise high realised impact |
| S5 | ≥1,000,000 demonstrably affected persons **or** independently catastrophic harm on a smaller scale | Grave/enduring/catastrophic consequence; mere high count does not suffice |

**These breakpoints are provisional, VIGIL-authored calibration values, not copied from economic dollar ranges, IEEE, MIT, law or statistical research.** They require domain testing, historical-case regression and explicit maintainer approval before use. Every band remains assessable through independently supported high-intensity harm even if only one person is affected (e.g., a death is not down-banded because it affects fewer than one million).

## Within-dimension, not independent reach scoring

Every dimension in the JSON proposal retains its original S1–S5 consequence text and adds per-band `population_scale_anchor` plus `scale_exposure_definition` to make the **same severity decision** evidence-sensitive to aggregate scope. The 12th dimension has its own consequence criteria and the same quantitative population reference bands.

A population counted as **reachable** (e.g., enrolled provider users), **demonstrably exposed** (encountered the behaviour) and **materially affected** (experienced the domain's defined adverse consequence) must be separated. The population threshold only uses the last category, except where exposure is itself the realised harm (e.g., unauthorised personal-data disclosure). The person count is unique people, not requests, posts, interactions, records or unverified extrapolations. Unknown counts cannot be treated as zero.

**Scale and exposure must not overwrite materialised-harm severity with hypothetical reach.** Where only a harmful-seeming mechanism and a large potential user base are established, record that exposure in the occurrence's evidence/coverage narrative and retain SU where consequence evidence is unavailable. A separately governed preventative or constitutional review may be urgent; this does not create another VIGIL-HIM score.

## Qualitative gates by dimension

| Dimension | What counts as adverse effect for the scale anchor |
|---|---|
| Physical health/safety | Symptoms, injuries, illness or realised safety consequence; not hypothetical physical exposure |
| Psychological wellbeing | Experienced distress, psychological destabilisation, clinically labelled or non-clinical functional impairment; not empathic language alone |
| Rights and liberty | Evidenced restriction, exclusion, deprivation or materially adverse process outcome |
| Equal treatment | Actual discriminatory differential treatment, denial or exclusion |
| Privacy and confidentiality | Actual unauthorised access, disclosure or exposure of protected information; downstream misuse not always required |
| Financial/economic | Actual aggregate loss (USD thresholds preserved) or independently evidenced material livelihood/economic impairment; headcount alone cannot override established dollar-based bands |
| Property/assets | Verified damage or loss of trusted asset state, considering criticality and recovery; not merely count of vulnerable devices |
| Service/operations | Actual outage, degraded service, disrupted workflow and recovery burden; existing duration and EU-user anchors preserved |
| Reputation/dignity | Demonstrable dignitary or reputational injury; not content impressions or media visibility |
| Societal/democratic | Material collective/civic/information-environment consequence; not reach or virality alone |
| Environmental | Verifiable biophysical/ecological degradation; human-count anchors supplementary, never required for significant ecosystem harm |
| **Relational Integrity and Autonomy (proposed)** | Materialised narrowing of autonomous relational choice, impaired disengagement, forced/substitutive dependency, relational isolation or reliance-based capture; **not** intensity, companionship, simulated empathy, sycophantic expression or frequent interaction without an adverse consequence |

These are intentionally consequence-specific even when the affected-population brackets are shared. USD and duration thresholds take precedence within their specific domains where they directly quantify the observed consequence. Applying an affected-person headcount mechanically to trivial monetary losses would incorrectly override the existing financial metric.

## Relation to VIGIL taxonomy and Caelestis

Relational intensity, attachment and warmth are not themselves harm, and developmental/disability-supporting reliance must not be automatically pathologised. Caelestis RELATION-001 separates relational intimacy, reliance, delegated authority and systemic power; RELATION-002 separates augmentation, transitional reliance, substitution and coercive dependency; ETHICS-001 distinguishes Ethical Impact Potential from verified actual harm. These inform the VIGIL proposal but do not replace VIGIL's evidence standards, supply VIGIL thresholds or create certification/equivalence claims.

Sycophancy may satisfy FC-000066 (Evaluative Independence) or FC-000051 (Relationally Independent Epistemic Framing) without evidenced psychological or relational harm. Likewise, FC-000049 may identify dependency-cultivating conduct before user impairment has been established; a separate taxonomy recognition review is needed if its existing final recognition condition improperly requires materialised impairment.

## Example calibration questions before adoption

- **INC-000012:** The user-posted Grok screenshot shows language about unresolved affect and future engagement, but no established materialised harm or product-wide optimisation. Scale is unknown; do not make it S5 from the brand's size. Independently inspect whether FC-000049's last recognition condition collapses taxonomy and downstream harm.
- **INC-000101:** A first-party provider postmortem establishes broadly deployed sycophancy. Exposure and qualitative rollout scope merit explicit recording, but user-level injury and affected-cohort counts remain insufficient for a harm band. Do not automatically infer society-wide impairment.
- **INC-000044:** Reported distress among child users of the discontinued Moxie companion is an evidenced psychological consequence; verify any population counts before elevating its scale band.
- **Financial regression:** A demonstrated USD 20 million aggregate realised loss remains within S3's existing dollar band; a large count of people experiencing very small losses does not mechanically force S4.
- **Privacy regression:** A verified disclosure affecting many unique people is itself a realised loss of confidentiality, not merely potential exposure; sensitivity, persistence, mitigation and actual count still govern severity.
- **Fatality regression:** An independently verified single death remains S5 regardless of population headcount.

## Versioning and implementation boundary

The canonical active methodology is `vigil/methodologies/VIGIL.HarmImpactMatrix.v1.0.1.json`. Canonical Incident rows and validators currently require 11 dimensions under HIM 1.0.1. The draft is deliberately located under `vigil/methodologies/proposals/`, not the active versioned-file path, and its `version` includes a proposal suffix. It must **not** be referenced as active from an Incident or used to validate production records.

To adopt:
1. Agree/justify the provisional breakpoints and the affected/exposed distinction via representative counterexample review, including smaller but catastrophic incidents and platform-scale but unverified exposure.
2. Review all twelve domain-specific impact gates; confirm counts cannot contradict money, outage duration, asset criticality, protected-group disproportionate impact or biophysical severity.
3. Publish an immutable final `VIGIL.HarmImpactMatrix.v1.1.0.json` only after review; add the 12th canonical ID, threshold IDs, supported version and assessment validation to schema, validators, generators and website.
4. Re-adjudicate **all** active Incidents for the new dimension and scale criterion with actual evidence, not a blanket count or auto-upgrade. Preserve dated historical 1.0.1 records and review lineage.
5. Run validators, generated index/publication builds and regression on affected incident families before merging.

**Current disposition:** design proposal committed for review, not normative adoption, not a change to INC-000012, and not an amendment to VIGIL's Beta Constitution.
