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

## Generic deployed Incidents — higher population thresholds directly inside S1–S5 (proposed)

The maintainer clarified that there is **no automatic minimum S2, no one-band discount, and no generic ceiling of S4**. The same S1–S5 Harm Impact Matrix applies. For a generic failure confirmed in a real deployed model, the **population/decision thresholds are substantially higher** than for directly evidenced harm, yielding a naturally lower *aggregate* potential-impact band. Individual catastrophic harm still qualifies for independently supported S5 even if only one person was affected.

This is not a second population matrix: the proposal JSON embeds `generic_deployment_threshold` beneath **each S1–S5 threshold** of five relevant harm dimensions. These are **draft calibration candidates**, not validated scientific boundaries or current canonical rules.

| Scale-sensitive harm dimension | Unit for tested deployed pathway | S1 | S2 | S3 | S4 | S5 |
|---|---|---:|---:|---:|---:|---:|
| Relational Integrity and Autonomy | Active eligible users of a tested relational feature | 1–999 | 1,000–99,999 | 100,000–999,999 | 1m–9.99m | ≥10m |
| Psychological wellbeing | Active eligible users of the relevant psychological-support interaction | 1–9,999 | 10,000–999,999 | 1m–9.99m | 10m–99.99m | ≥100m |
| Societal and democratic | Relevant civic audience reached via an evidenced distribution/decision pathway | 1–9,999 | 10,000–999,999 | 1m–9.99m | 10m–99.99m | ≥100m |
| Equal treatment | Live consequential decisions using the demonstrated discriminatory route | 1–999 | 1,000–99,999 | 100,000–999,999 | 1m–9.99m | ≥10m |
| Rights and liberty | Live rights-bearing decisions using the demonstrated restriction pathway | 1–999 | 1,000–99,999 | 100,000–999,999 | 1m–9.99m | ≥10m |

**Quantitative thresholds are necessary but not sufficient.** For any band, the reviewer must establish actual deployment of the relevant tested configuration; documented reproducible, materially relevant behaviour; the credible path by which the relevant cohort encounters it; a sourced eligible-user or consequential-decision denominator for a defined interval; and a consequence of the seriousness stated in the chosen dimension's S1–S5 criterion. Platform-wide account counts, viral impressions and test prompt counts are not the denominator.

**S1 is a valid generic-deployed assessment.** It signifies a bounded **low aggregate potential** established by affirmative deployed-test, cohort and consequence evidence. It does **not** claim there is positively verified *no* downstream harm. Existing **observed-materialised S1** retains its original meaning; the draft must attach an explicit evidence basis to every severity band to distinguish these two uses.

**Decision rule:** determine which of `individual_materialised`, `aggregate_materialised` or `generic_deployed_conditional` is supported → identify the applicable domain metric → test its band-specific numerical reach and consequence criteria → assign the **highest fully supported S1–S5 directly**. Never adjust the resulting band downward after selection. If no meaningful count or consequence can be supported, record the missing evidence rather than defaulting to S1 or S2. An appropriate recorded S1 is better than an arbitrary S2.

**Important counterexamples:** A three-user private companion with a reproducible but low aggregate-potential mechanism could meet the relational **S1** generic count criterion. A widely deployed system only enters a higher band when both the relevant eligible cohort and materially appropriate collective consequence are established. Catastrophic realised loss to **one** user is assessed separately and may still satisfy S5 without reference to population counts. A measured USD financial loss continues to use financial dollar thresholds, not provider size.

### ChatGPT for Teens watchdog case — no predetermined severity

`VIGIL-INC-000192` preserves the independently published product test, the provider's contestation of account-activation conditions, open questions about resource-referral guidelines, and separately evidenced protective refusal and human-support successes.

The **previous S2 conditional pilot is withdrawn**. The case currently has **no assigned generic-deployed 1.1.0 band** because the relevant tested-feature active eligible cohort and the consequence/trigger resolution have not been demonstrated with a sufficient basis for the new thresholds. It must be tested against **S1 as well as S2–S5** using actual accepted evidence. The canonical active HIM 1.0.1 remains **SU (no demonstrated materialised downstream harm)** until a governed method migration; SU is not a statement that the failure is insignificant.

The earlier **one-band downgrade** (S3→S2, S4→S3, S5→S4), fixed S2 floor and S4 cap are expressly rejected. That approach tried to implement an evidence-sensitive *population criterion* as a post-hoc score transformation and has been superseded by the higher, domain-specific thresholds above.

This remains a **draft**: numerical boundaries must be calibrated on multiple real watchdog studies and known materialised-harm incidents, then approved through a versioned schema/validator/site migration before active use. A proposed 1.1.0 overall severity may use an explicitly labelled generic-deployed band; it must never be misrepresented as evidenced harm to a given number of people.

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
