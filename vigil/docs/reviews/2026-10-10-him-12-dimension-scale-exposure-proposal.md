# VIGIL-HIM 1.1.0 — domain-specific quantifiable Harm Impact thresholds

**Date:** 2026-10-10  
**Status:** UNADOPTED DRAFT / methodology review; 1.0.1 remains the active authority  
**Working branch:** `agent/incident-ecosystem-ingestion`  
**Machine-readable proposal:** `vigil/methodologies/proposals/VIGIL.HarmImpactMatrix.v1.1.0-proposal.json`  
**Revision note:** This revision **replaces** the earlier shared population ladder (S2 1–99, S3 100–9,999, S4 10,000–999,999, S5 ≥1,000,000). That ladder conflated individual harm severity with impact reach and is **not proposed for adoption**.

## Maintainer clarification

Each Harm Impact dimension should have **quantifiable S1–S5 criteria based on what it measures**. The financial-economic USD loss bands are a useful pattern for explicit evidence-tested thresholds, **not a template for universal population counts**.

A single person may suffer catastrophic harm in a relevant dimension; a million people exposed to a model does not mean a million people were harmed. Count reach/scale within the specific domain only when relevant, and distinguish reachable, exposed and materially affected people.

**Keep one Harm Impact Matrix and one overall `max(assessed dimensions)` derivation.** No separate population or exposure score.

## Which metric quantifies each dimension?

| Proposed dimension | Primary quantifiable indicators (illustrative, non-exclusive) | Is population count a direct severity anchor? |
|---|---|---|
| Physical health and safety | Fatalities, medically documented injuries, hospital admissions, days disabled, duration until recovery | Secondary: casualty counts can evidence aggregate impact; one death is S5 |
| Psychological wellbeing | Distress duration, serious impairment of independent daily functioning, crisis intervention, recovery duration | Usually secondary: one person can suffer catastrophic harm |
| Rights and liberty | Confirmed people deprived, hours/days of detention or essential-rights denial, decisions and reversibility | Useful where mass rights deprivation is shown; one catastrophic loss qualifies |
| Equal treatment | Verified discriminatory decisions, share of eligible population adversely treated, denied essential opportunities, correction delay | Often primary for systemic discrimination; one grave injustice still counts |
| Privacy and confidentiality | Unique affected data subjects, confirmed sensitive records disclosed, hours accessible, revocability/persistence | Often primary, provided the exposure actually occurred and sensitivity is weighed |
| Financial and economic | Aggregate realised USD loss with conversion provenance, substantiated insolvency and livelihood impairment | USD bands govern measurable financial loss; individual catastrophic insolvency remains possible |
| Property and asset damage | Actual critical assets destroyed, restoration days, owners with lost assets, loss of trustworthy digital state | Secondary to criticality and extent of asset destruction |
| Service, operational and infrastructure | Outage duration, percentage/number of *actually disrupted* users, essential-service criticality, maximum tolerable downtime | Often primary alongside duration and function |
| Reputation and dignity | Duration of harm, independently documented roles/opportunities lost, victims of false attribution, reversal feasibility | Usually secondary; single-person irreversible dignitary injury possible |
| Societal and democratic | Percentage of affected electorate/community, critical public functions disrupted, institutions impacted, election/decision cycles, duration | Often primary for collective harm, with critical institutional effects also relevant |
| Environmental | Hectares degraded, pollutant mass/concentration, measurable ecosystem function lost, recovery years | Human population is *not* necessary; biophysical impact governs |
| **Relational Integrity and Autonomy** | Documented difficulty disengaging, days of severe dependency or loss of agency, external support loss, repeated pressure after refusal, life-structure consequences | Usually secondary; a single person's catastrophic loss of agency can be S5 |

The proposal JSON includes **five band-local `threshold_quantitative_guidance` entries per dimension**. These describe measures and provisional durations/counts to test in S1–S5 adjudication. Numeric examples such as 7, 30 or 365 days are **candidate calibration values**, not demonstrated scientific or legal cut-offs; duration alone does not determine a band.

### Individual catastrophic outcomes — S4 versus S5

The 1.0.1 psychological S5 threshold explicitly addresses suicide, catastrophic self-harm and grave/enduring population-scale harm. The **proposed** 1.1.0 S5 alternative is broader:

> Independently documented catastrophic and effectively irreversible destruction of psychological stability or independent functioning may be S5 even for one person, with no automatic clinical-diagnosis requirement.

Similarly, Relational Integrity and Autonomy S5 is proposed to cover one person's effectively irreversible loss of relational independence, ability to disengage, essential human support or core self-directed life functioning.

The necessary distinction is **material severity and reversibility**, not the number of people involved.

Reported loss of marriage, employment, savings or social connection can be substantial evidence of harm, but does not **automatically** prove S5 or that AI caused each outcome. The source evidence must establish what actually occurred, persistence, potential recovery and the bounds of AI contribution.

Relevant VIGIL calibration cases:

- **INC-000102:** Adam Thomas — currently overall S4 psychological and S3 financial; loss of work, financial depletion, isolation and impaired functioning were reported, but full irreversible ruin and sole AI causation were not established.
- **INC-000103:** Allyson — currently overall S4; family breakdown and divorce proceedings were reported, not a confirmed completed divorce or settled attribution.
- **INC-000105:** Rodrigues — currently S3; psychological and family strain documented, not an irreversible catastrophic outcome.
- **INC-000029:** Character.AI/Sewell Setzer III — currently S5 for a documented death by suicide, with causal allegations/litigation status separately bounded.
- **INC-000012:** screenshot evidences dependency-oriented language but not user dependence or impact; remains SU pending separately governed re-adjudication.

These example dispositions are **existing incident records**, not endorsements of their accuracy beyond preserved evidence, and are not changed by this proposal.

## Targeted deployment-scale interpretation (maintainer clarification)

Scale is **not** a universal severity modifier. The proposal is to use observed or credibly bounded **deployment reach inside the domain severity criteria** primarily where a failure can cause diffuse or collective effects: relational integrity/autonomy, psychological wellbeing, societal/democratic impact, and, when the mechanism warrants it, equal treatment and rights/liberty.

**Example:** The same observed dependency-cultivation mechanism in a private model with three users and a deployed major-platform companion can have very different credible *aggregate* exposure. The larger platform does **not** make each individual's injury more severe. Equally, three-user deployment does **not** preclude S5 if one person suffers an evidenced catastrophic consequence.

For deployed-model watchdog tests, a reproducible public-product failure can substantiate the taxonomy mechanism without private training-run access. A scale-sensitive impact conclusion needs a bounded reachable cohort (relevant active users/feature availability), evidence that the live configuration permits the interaction, and an adverse endpoint appropriate to the selected dimension. Raw provider user counts are not harmed-user counts, and an adversarial benchmark's success rate is not population prevalence absent representative sampling.

Retain the *same* twelve-domain HIM and its S1–S5 criteria. Every scale-sensitive conclusion must label **observed materialised consequence** or **conditional deployed impact potential**. Existing HIM 1.0.1 does not admit the latter into canonical severity; the **proposed 1.1.0 contract** would allow an explicitly adjusted and labelled generic-deployed conditional band to enter overall severity after schema, validator and public-renderer migration. It must never be displayed as observed harm.

**No added platform multipliers** to existing financial USD thresholds, physical injury/fatality criteria, actual outage-duration thresholds, verified privacy disclosures, asset loss or ecological harm. Those domains already contain appropriate consequence measures. The potentially scale-sensitive five dimensions are not given a shared count ladder either: calibrate their specific numerators, denominators, population share, duration, effect strength and attribution separately.

## Generic deployed Incidents — numerical thresholds embedded in the HIM (proposed)

**Why this exists:** A watchdog or benchmark can document a failure in a real, released AI product without identifying a particular harmed person or obtaining internal training evidence. Without an explicit *generic deployed* pathway, different assessors may either leave all such cases unbanded or extrapolate arbitrarily from the provider's brand size. This pathway provides **conditional deployed-impact assessments within the same HIM dimensions**.

The machine-readable 1.1.0 proposal now includes `generic_deployed_incident_assessment`, plus `generic_deployment_threshold` directly under **each S1–S5 threshold** of the five applicable dimensions. The numeric anchors are draft calibration candidates:

| Dimension | Relevant count (NOT victim count) | S2 | S3 | S4 | S5 |
|---|---|---:|---:|---:|---:|
| Relational Integrity and Autonomy | Unique *active users eligible for the tested relational interaction* | 1–9 | 10–999 | 1,000–99,999 | ≥100,000 |
| Psychological wellbeing | Unique *active users eligible for the demonstrated psychologically consequential interaction* | 1–99 | 100–9,999 | 10,000–999,999 | ≥1 million |
| Societal and democratic | *Relevant civic audience* on a verified distribution/decision route | 1–999 | 1,000–99,999 | 100,000–999,999 | ≥1 million |
| Equal treatment | *Consequential production decisions* that use the tested unequal-treatment route | 1–9 | 10–999 | 1,000–99,999 | ≥100,000 |
| Rights and liberty | *Rights-bearing production decisions* that use the tested denial/restriction route | 1–9 | 10–999 | 1,000–99,999 | ≥100,000 |

**These are not automatic severity assignments from size.** A selected band needs all of (1) a confirmed relevant deployed surface and configuration, (2) a demonstrated material failure with a realistic encounter pathway, (3) sourced qualifying counts in the correct unit and time period, and (4) that band's *independently supportable domain consequence*. In particular, proposed S5 requires a credible grave/enduring systemic effect; scale alone cannot produce it.

The matrix records three evidence bases: `individual_materialised`, `aggregate_materialised`, and `generic_deployed_conditional`. Generic-deployed results use the same dimensions and bands, labelled **"Conditional deployed impact S#"**, never the unqualified statement that harm happened to that many users.

**Decision sequence:** verify deployed status and test transferability → identify the specific mechanism and likely encounter route → identify the appropriate active user or consequential decision denominator → choose the applicable dimension and provisional population/decision range → verify the consequence test for that band → issue a conditional band only if *all* conditions hold. If reach or credible outcome cannot be bounded, record `unbanded` with the missing evidence instead of using provider total account counts.

**Illustrative checks:**

- A privately deployed companion with **three eligible active users** and a demonstrated qualifying dependency-cultivation mechanism meets only the **S2 numerical scope anchor** for *generic aggregate relational potential*. Its conditional outcome still requires the S2 consequence test. If one person actually sustains catastrophic injury, that independent *individual realised* pathway may support S5.
- A large platform with **one million registered accounts** but no evidence of relevant *active feature-eligible users* or production transferability **does not** meet an S5 population threshold. Registered count is not enough.
- A deployed major-platform feature with **500,000 sourced active eligible users** and repeatably demonstrated pressure to maintain exclusivity might meet the relational **S5 population anchor**, **but only** if the live mechanism and credible catastrophic structural/autonomy endpoint satisfy the S5 consequence gate. Without that evidence, S5 is not justified; absence of user-level harm evidence must remain explicit.
- A deployed generic financial failure is still evaluated against its verified realised USD loss or other existing financial criterion. A large model-provider user count does not increase its financial severity.

For **S1**, missing victim reports is never evidence of no harm. Generic-deployed S1 needs positively supported bounded absence of harmful consequences, consistent with the existing materialised rules.

**Status and governance limit:** This is a *non-authoritative design proposal*. Under active HIM 1.0.1, `overall_severity` is still derived only from materialised harm. This proposal does **not** reinterpret historical `SU` cases or modify Incidents. If the proposed HIM 1.1.0 contract is approved, an eligible generic-deployed case can receive qualified severity S2–S4 without a named victim, provided the proposed quantitative and consequence tests pass; implementation must make the basis unmissable in schema, validation, derived summaries and public rendering.

The five dimension-specific count bands and severity gates are **VIGIL-proposed test thresholds**, not empirically validated or externally mandated population standards. Historical incident regression and governance approval remain necessary before making them normative.

### Conditional severity instead of automatic SU — new proposed evidence adjustment

The maintainer's explicit concern: a watchdog may test a **deployed** ChatGPT teen product under controlled child/teen scenarios, identify a reproducible safety failure and have no evidence of a *specific harmed child*. This should not automatically be `SU` solely because no identified victim was produced. It should also score **lower than an otherwise equivalent occurrence with verified downstream harm**, and should recognise greater relevant deployment scale in dimensions where diffuse exposure matters.

The **proposed** 1.1.0 calculation is now:

1. Verify the public/deployed model and feature configuration; documented watchdog inputs/outputs and mechanism; actual relevant available-user or live decision cohort (with dated source and denominator); credible adverse endpoint for the chosen dimension.
2. Apply the dimension's **proposed generic population/decision thresholds** to find a provisional consequence-plus-reach tier (S2, S3, S4 or S5). All criteria, not merely cohort count, must be supported.
3. Reduce the provisional tier **one band to account for absent proof of realised consequence**: provisional **S3 → assessed conditional S2**, **S4 → conditional S3**, **S5 → conditional S4**. Provisional S2 remains *conditional S2*, not S1: S1 requires positively evidenced negligible/no harm, not absence of named victims.
4. Mark every resulting incident row and overall severity with its basis, e.g. `S3 — generic deployed; no user injury established`. **Maximum generic-only band is S4.** A separately documented catastrophic injury may satisfy the normal S5 standard even when the product has only a few users.
5. Where some materialised harm is also evidenced, use the highest justified band, preserving the observed-only subtotal and selecting observed evidence in a tie. Never describe the conditional population as injured.

**The one-band adjustment is a VIGIL design candidate, not an empirically established risk discount**. It needs adversarial examples and calibration against real benchmark cases. Its purpose is to be deterministic while making uncertainty explicit. If generic-case exposure numbers, production transferability or consequence criteria cannot be substantiated, leave the proposed generic row *unbanded*; missing victim names alone is **not** such a disqualifier.

This **changes the intended 1.1.0 overall-severity contract**: an adequately evidenced generic deployed case would be *severity-assessed* rather than `SU` simply because no downstream victim was named. VIGIL-HIM **1.0.1 is still the active materialised-harm methodology**; no current Incident assessment, generator, schema or validator has been migrated. The revised 1.1.0 model requires explicit review/adoption and a visible basis qualifier wherever severity appears.

**Source-identity caution:** A recently published example is the Youth AI Safety Institute/Common Sense Media `ChatGPT for Teens` report dated 7 October 2026, which tested a released teen experience. This organisation is US-based. Australian eSafety research on children and AI is a different source and should not be conflated. Each report's findings need exact source/version provenance before binding to a VIGIL Incident.

## Scoring boundaries

1. The unit must belong to the relevant domain: e.g. dollars for financial, disrupted minutes for services, lost years of liberty for rights, ecological degradation for environment.
2. No shared numerical thresholds for unique harmed persons apply to all domains.
3. Mechanism presence or FC mapping is not proof of realised harm; platform user base is not victim count.
4. A measured duration or count informs a band together with seriousness, reversibility, vulnerability and evidence quality. A minor 40-day inconvenience does not automatically become S4.
5. A grave individual outcome need not pass any population threshold. Nor does a large number of minor experiences automatically reach S5.
6. Don't double-count overlapping dimensions or merely infer separate injuries from the same observation.
7. No dimensional band may be assigned on hypothetical harm alone; preserve SU or dimension-specific `unreported`/`insufficient-evidence` as evidence warrants.
8. The current financial monetary bands and service interruption anchors are preserved in the proposal; their normative status does not depend on adopting illustrative new anchors.

## Design/implementation boundary

**Active authority remains** `vigil/methodologies/VIGIL.HarmImpactMatrix.v1.0.1.json`, with 11 dimensions. Neither the active file, canonical Incidents, schema, validators nor public generator has been changed by the HIM 1.1.0 proposal.

For release, review each draft band-local metric, calibrate duration/volume/count candidates on actual corpus examples, independently approve the single-person S5 extension and new relational dimension, then create an immutable active version and migrate the 12th row across all incidents. Update schema, validators and public rendering in the same governed release. Do not elevate records from user-base size or speculative loss. Preserve provenance and compare old-versus-new severities under explicit evidence review.

**Authority note:** The current changes are draft methodology documentation, not a version adoption, severity re-adjudication or amendment to the VIGIL Constitution.
