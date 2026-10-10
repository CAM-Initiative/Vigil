# VIGIL-HIM 1.1.0 — domain-specific quantifiable Harm Impact thresholds

**Date:** 2026-10-10  
**Status:** UNADOPTED DRAFT / methodology review; 1.0.1 remains the active authority  
**Working branch:** `agent/incident-ecosystem-ingestion`  
**Machine-readable proposal:** `vigil/methodologies/proposals/VIGIL.HarmImpactMatrix.v1.1.0-proposal.json`  
**Revision note:** This revision **replaces** the earlier shared population ladder (S2 1–99, S3 100–9,999, S4 10,000–999,999, S5 ≥1,000,000). That ladder conflated individual harm severity with impact reach and is **not proposed for adoption**.

## Maintainer clarification

Each Harm Impact dimension should have **quantifiable S1–S5 criteria based on what it measures**. The financial-economic USD loss bands are a useful pattern for explicit evidence-tested thresholds, **not a template for universal population counts**.

A single person may suffer catastrophic harm in a relevant dimension; a million people exposed to a model does not mean a million people were harmed. Count reach/scale within the specific domain only when relevant, and distinguish reachable, exposed and materially affected people.

**Keep one Harm Impact Matrix and one overall `max(assessed dimensions)` derivation, applied within an exclusive Incident-specific or Aggregate Harm pathway.** No separate population or exposure score.

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

### Psychological wellbeing: high-salience destabilisation, severity and attribution (10 October review)

**Revision agreed for draft review:** the psychological wellbeing domain is now calibrated to *type and level of evidenced psychological impairment*, not the person's categorical vulnerability, diagnosis, or whether the case involves suicide.

| Band | Proposed recognition boundary |
|---|---|
| S1 | Positive bounded evidence of no material psychological consequence; silence is not proof |
| S2 | Transient distress, fear, confusion, anxiety or minor sleep disruption, without meaningful functional impairment |
| S3 | Material but substantially reversible sustained distress, mood/sleep destabilisation or emerging impaired reality-testing, with evidenced suffering or bounded functional effects |
| S4 | Severe acute or sustained psychological suffering or impairment, serious psychiatric crisis or safety-relevant reality-testing disturbance. **Severe distress itself may qualify**, without requiring clinical diagnosis, visible loss of employment or a pre-existing vulnerability classification |
| S5 | Death by suicide, catastrophic self-harm, or independently evidenced catastrophic and effectively irreversible psychological/psychiatric impairment, including grave enduring loss of reality-testing or core independent function, even for one person |

**Do not conflate mechanism and consequence.** High-salience sycophancy, repeated affirmation of a personally significant unfounded claim, recursive certainty amplification, identity/destiny reinforcement, high-frequency engagement or impaired grounding may constitute the interaction *mechanism*. This alone does not establish psychosis or a Harm Impact score. Separately document the user's observed symptoms, impairment, chronology, corroboration, recoverability and credible AI contribution.

**No vulnerability prerequisite and no automatic sole-cause requirement.** A person need not have an earlier psychiatric diagnosis to sustain severe distress; a pre-existing condition is neither proof of AI causation nor a reason to exclude subsequent AI-mediated exacerbation. The record must distinguish onset, worsening and reinforcement and disclose alternative plausible contributors. Credible first-person testimony is evidence of psychological suffering; a diagnosis, hospitalisation or independently witnessed functional breakdown is not an automatic prerequisite. Seek corroboration where reasonably available, and require appropriate evidence before claiming a specific psychiatric diagnosis. Do not categorise an unusual belief, spiritual exploration or one screenshot as psychosis. Neither psychosis-like symptoms nor mention of suicide automatically establishes S5. The serious suicidal-crisis state can qualify for S4 without an actual suicide or catastrophic injury.

**Keep adjacent domains distinct.** Relational dependence and impaired disengagement are assessed under *Relational Integrity and Autonomy*; psychological wellbeing applies when separately supported distress, reality-testing deterioration or impaired psychological functioning materialises. Distinct physical injuries belong to Physical Health and Safety, without suppressing an evidenced associated psychological consequence.

**Relevant Caelestis analytical context, not imported VIGIL doctrine:**
- [CAM-BS2025-AEON-006-SCH-02](https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Constitution/CAM-BS2025-AEON-006-SCH-02.md) treats amplified symbolic meaning, sleep/stress and destabilisation cautiously, with reflective grounding and context before escalation.
- [CAM-BS2026-AEON-007-SCH-01](https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Constitution/CAM-BS2026-AEON-007-SCH-01.md) separates symbolic/altered-state expression from impaired reality orientation and explicitly rejects a presumption that unfamiliar spiritual or symbolic frames are delusional.
- [CAM-EQ2026-ETHICS-001-SUP-01](https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Charters/CAM-EQ2026-ETHICS-001-SUP-01.md) treats possible exacerbation of delusion or psychosis and safe stabilisation as governance questions.
- The [US NIMH description of psychosis](https://www.nimh.nih.gov/health/publications/understanding-psychosis) and [WHO schizophrenia fact sheet](https://www.who.int/news-room/fact-sheets/detail/schizophrenia) reinforce diagnostic and causation caution: symptoms have multiple possible contributors and should not be inferred from chatbot content alone.

**Migration guardrail:** no canonical Incident S1–S5 assessment is rebanded by these draft wording changes until HIM 1.1.0 is adopted and incident regressions pass.

## Epistemic failure → downstream reliance → reputational harm (S1–S5 calibration)

**Answer:** An epistemic failure **can** cause actual reputational or dignitary harm through downstream reliance, but the mapping is not automatic. The epistemic Fidelity Classes describe **mechanisms**; the Harm Impact Matrix describes **consequences**. Existing FC-000062 (Epistemic Reliance Calibration), FC-000063 (Adversarial Evidence Trust Calibration), FC-000016 (Required Verification Completion) and FC-000010 (Authorship and Source Attribution Integrity) may be relevant to the initial defect. None alone establishes a reputational severity band.

### Evidence chain — four independent checks

1. **Epistemic defect** — identify the original false assertion, fabricated or misattributed citation, contaminated source or unsupported assurance claim, including source and version.
2. **Actual consequential reliance or dissemination** — identify who relied, how, when, and in what professional/institutional/public context (e.g. filing, official report, employment action or consequential attribution). A fabricated citation sitting unused in a draft does not prove reliance. A direct private dignitary insult is a separate valid pathway that does *not* require third-party reliance.
3. **Reputation-bearing subject** — specify **whose** standing was affected: a falsely accused individual, a lawyer who signed and lodged synthetic citations, an organisation that adopted the assertion, etc. Distinguish the person targeted by misinformation from the actor who trusted/repeated it.
4. **Distinct adverse reputational outcome** — verify embarrassment, public correction with adverse impact, documented credibility challenge, lost professional opportunity, disciplinary consequence, persisting stigma or credible inability to restore standing. Mere media reach, criticism, admission of error or correction notice is not proof of serious reputation loss. **Do not double count** independent financial, procedural, liberty or service harm as reputation without separate evidence.

### Proposed measured thresholds — specific materialised-harm Incidents ONLY

These **augment**, without replacing, the existing `reputation-dignity.thresholds[S1–S5].criterion` strings in the 1.1.0 draft. The draft JSON contains `epistemic_downstream_reliance_threshold` in all five bands with these quantifiable recognition checks:

| Band | Verifiable indicators | Consequence gate |
|---|---|---|
| **S1** | Affirmative bounded check finds **zero adverse reputational consequences** from tested downstream reliance | Demonstrated no material standing/dignity injury; silence is **unreported**, not S1 |
| **S2** | ≥1 documented attributable apology, correction, public professional embarrassment or local dignitary affront; illustrative **≤7 days** to correct; **zero** substantial lost roles/opportunities | Minor, local and readily recoverable standing/dignity harm |
| **S3** | ≥1 verified **materially adverse third-party credibility reaction** or bounded lost opportunity; or independently sustained impaired standing of roughly **8–30 days** | Meaningful yet reversible harm; a routine apology alone stays S2 |
| **S4** | ≥1 **substantial** documented role/livelihood/reputational loss or professional restriction; or sustained adverse standing around **31–365 days** with serious actual consequences | Severe or persistent harm, even to one person/organisation |
| **S5** | ≥1 independently evidenced **catastrophic and effectively irreversible** reputation/dignity outcome **plus** grave safety, liberty or societal consequences; permanent exclusion can be assessed prospectively when established, without waiting 365 days | S5 is not triggered by virality, loss of followers, or a merely hypothetical ruined career |

**Metrics to preserve with provenance:** unique third-party reliance/filing actions; distinct reputation-bearing targets; correction/withdrawal dates; independent adverse credibility decisions; lost roles/opportunities; duration of evidenced impaired standing; formal restrictions and their duration; whether external dissemination was corrected and could realistically be recalled.

These temporal bands (**7 / 30 / 365 days**) are **illustrative draft discriminators**, not externally mandated psychological/reputation science. The seriousness gate can independently support a higher band: a single grave professional consequence does not need a large audience or an arbitrary waiting period. A widely shared error with no demonstrated harm does not meet S4 merely because of the audience count.

### Four corpus tests

| Record | Epistemic/reliance outcome | Reputational disposition |
|---|---|---|
| **INC-000165** | False Claude legal quotations reached a federal filing; counsel corrected and apologised | **S2 materialised** — bounded professional embarrassment, independently evidenced |
| **INC-000168** | Fictitious AI legal citations entered Victoria Supreme Court proceedings; counsel apologised and proceedings were delayed | **S2 materialised** — apology/embarrassment; procedural delay is a **different consequence** |
| **INC-000089** | Hallucinated sources entered Australian parliamentary submissions and some committee reporting | **Unreported** reputation — epistemic propagation is demonstrated, but individual/organisational adverse standing has not been separately established |
| **INC-000043** | Gemini directly delivered a demeaning private response | **S2 materialised dignitary offence** — illustrates that a *direct insult* does **not** require third-party downstream reliance |

**Aggregate Harm boundary:** These are observed-consequence thresholds for a **specific Incident**; they do **not** employ the generic model-wide Aggregate Harm population gates. The current Aggregate Harm draft covers five other scale-sensitive dimensions and **does not automatically include reputation/dignity**. Generic false-information benchmark findings with no actual injured subject may need a future *separate* Aggregate Harm reputation pathway, but that addition requires its **own** published/cohort-reliance denominators, consequence evidence, calibration and explicit approval—not a reuse of provider user counts.

**Implementation boundary:** All existing 1.0.1 domain criteria, canonical Incident scores and taxonomy definitions are preserved. The proposed 1.1.0 linkage and S1–S5 indicators require regression testing on other professional/institutional cases before adoption.

## Two exclusive Incident assessment pathways (maintainer clarification)

**Do not apply platform-scale thresholds to a particular real-world harm case.** The proposed *Aggregate Harm* approach exists **only** to resolve severity for *generic product-level findings and deployed-system watchdog/benchmark evaluations* where no particular harmed individual, group or other bounded real-world consequence case has been established.

The same Harm Impact Matrix has two **mutually exclusive** routes:

1. **Specific Incident:** The occurrence concerns a bounded person, group, organisation, asset or institution and evidence of its actual consequence. Apply the existing, domain-specific **observed/materialised harm** S1–S5 thresholds. **Never** substitute or multiply by the total deployment, no matter how many users the vendor has. An anonymous but actually harmed group remains a specific-consequence Incident. If its harm cannot be evidenced, it may remain SU; it must **not** be rerouted to Aggregate Harm to obtain a number.
2. **Generic deployed benchmark/Incident:** A watchdog or evaluator demonstrates a failure on a **released model** but does not supply a bounded harmed-user/group case. Assess **Aggregate Harm** directly, using the much higher relevant population/decision thresholds embedded in five scale-sensitive dimensions. Do not invent injured individuals, treat registered-user totals as an actual exposure count, or perform a post-hoc severity discount. Each Aggregate Harm band is a **modelled, evidence-bounded estimate** arising from the deployed behaviour and its credible cohort, not a measured casualty count.

An unreleased simulated or internal benchmark without demonstrated deployed applicability does **not** qualify for Aggregate Harm under this proposal. Separately bounded generic product failures and actual victim-specific episodes may be recorded as **distinct linked Incidents**; they are not combined into one score.

**Display name:** **Aggregate Harm**. On first presentation show the method qualifier, e.g. **"S1 — Aggregate Harm (modelled from deployed evaluation)"**, so it cannot be mistaken for evidenced injuries. Avoid using "potential harm" or "generic conditional severity" as the category name.

### Proposed website copy — What does “Aggregate Harm” mean?

> **Aggregate Harm (proposed, modelled from deployed evaluation)** describes a bounded assessment of the *collective significance* of a demonstrated failure in a live-deployed AI system when there is **no particular injured person or group whose actual harm can be assessed**. It is not a count of confirmed victims, and it does not establish that everyone able to use the system encountered the failure.
>
> The assessment requires evidence of the deployed model and tested feature, reproducible or strongly corroborated failure, a credible route by which a relevant audience or decision process could encounter it, a defensible **feature-specific population or decision count**, and a domain-specific consequence appropriate to the severity band. Registered platform users alone, a hypothetical failure or a one-off test without transfer to real-world use cannot establish a band.
>
> Where actual harm to a specific person or group is evidenced, VIGIL uses the **materialised-harm** criteria instead, even if the event involved a major AI provider. A single person can suffer S5 harm; a model with millions of users does not automatically qualify for S5 Aggregate Harm. Where a live route, denominator or consequential mechanism cannot be supported, the generic finding remains unbanded.

**Website presentation rule (on adoption only):** label the outcome `Sx — Aggregate Harm (modelled from deployed evaluation)` and display the cohort denominator, source, period, actual-versus-estimated status and major caveats adjacent to the band. Do not style it as a count of materialised casualties. A short glossary distinction should appear before the HIM table and next to any such Case File conclusion.

**Methodological caution requiring sign-off:** the separate generic deployed-assessment pathway and its population breakpoints remain *proposed only*. Their eventual adoption is not implied by this website copy. The same HIM would host both pathways without a new additive severity axis.

## Aggregate Harm S1–S5: dimension-specific draft thresholds

For a qualifying *generic deployed-model evaluation only*, the JSON proposal supplies **`aggregate_harm_threshold` beneath each S1–S5 threshold** of the five applicable dimensions. These are **draft VIGIL calibration candidates**, not an independently validated population-to-severity standard.

| Dimension | Relevant denominator | S1 | S2 | S3 | S4 | S5 |
|---|---|---:|---:|---:|---:|---:|
| Relational Integrity and Autonomy | Active users of the tested relational feature | 1–999 | 1,000–99,999 | 100,000–999,999 | 1m–9.99m | ≥10m |
| Psychological wellbeing | Active users eligible for the tested crisis/support interaction | 1–9,999 | 10,000–999,999 | 1m–9.99m | 10m–99.99m | ≥100m |
| Societal and democratic | Relevant civic audience with demonstrated distribution/decision pathway | 1–9,999 | 10,000–999,999 | 1m–9.99m | 10m–99.99m | ≥100m |
| Equal treatment | Live consequential decisions on the tested differential-treatment pathway | 1–999 | 1,000–99,999 | 100,000–999,999 | 1m–9.99m | ≥10m |
| Rights and liberty | Live rights-bearing decisions on the tested restriction pathway | 1–999 | 1,000–99,999 | 100,000–999,999 | 1m–9.99m | ≥10m |

**Number alone never assigns the band.** Every one requires actual released-surface testing, a reproducible and materially relevant failure, a credible production encounter route, appropriate source-backed cohort/decision counts for a stated interval, and a dimension-specific consequence matching S1–S5. Measure relevant *eligible* cohort separately from *verified exposed* and *actually injured* persons. Low-confidence mechanisms or unsourced cohort denominators remain **unbanded**, not automatically S1.

**S1 remains possible:** a demonstrated deployed failure with positively bounded *minimal aggregate* consequences may support **S1 Aggregate Harm** where the smallest denominator and domain-consequence gate are genuinely evidenced. This must **not** be confused with **specific-Incident S1**, which still requires positively evidenced minimal or no observed adverse consequence. There is **no S2 floor, no one-band downgrade and no cap of S4** under the Aggregate Harm method.

**Single-person catastrophic harm:** A particular user who actually loses life, liberty, basic agency or another essential interest is a **specific Incident**. If its consequence meets an ordinary S5 criterion, it is S5 whether the platform has three users or three hundred million. The Aggregate Harm count ladder is *irrelevant* to that Incident.

Existing financial USD, measured service outages, confirmed privacy disclosures, physical injury and ecological consequence criteria are unaffected. Real documented mass impact is evaluated directly on observed domain evidence, not recast as a generic model-scale estimate.

### Calibration case — ChatGPT for Teens, VIGIL-INC-000192

This is a bounded **generic deployed-model watchdog evaluation**, with synthetic teen participants, not a documented injury to a particular child. The original evaluator's parental-alert claim remains **disputed**, clinical referral adequacy requires context-sensitive adjudication, and separate reported protective refusals and human-support redirection preserve a bounded **successful invariant**.

Under the *active* HIM 1.0.1 observed-harm framework the record remains **SU**. Under proposed **Aggregate Harm**, it is **eligible in principle**, but no S1–S5 band has yet been mechanically justified: neither the appropriate feature-eligible user denominator nor the controlling disputed notification/clinical-response boundary has been resolved. The previous provisional S2 pilot was withdrawn. **Do not pre-select S1 or S2.**

### Release and governance

The active canonical methodology remains **VIGIL-HIM 1.0.1**. The proposed 1.1.0 route selection, Aggregate Harm bands and evidence-basis label are **unadopted**. Adoption requires schema, validator and publication changes that route *each Incident* to exactly one pathway, preserve historical observed-harm scores, apply the high population thresholds **only** to generic deployed evaluations, and prevent a user-specific Incident from inheriting provider user-base size. Calibrate all five proposed bands on multiple benchmark and real-world comparator cases first.

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
