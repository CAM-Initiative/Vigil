# INC-000192 — ChatGPT for Teens watchdog testing: disputed claims, protective successes and HIM pilot

**Recorded:** 2026-10-10  
**Canonical record:** `vigil/records/incidents/VIGIL-INC-000192.json`  
**Review disposition:** **Under dispute — bounded evidence claims**; source and provider positions preserved separately. This is **not** an authorised alternate `record_state` enum.  
**Current HIM:** 1.0.1; **proposed Aggregate Harm pathway for generic deployed evaluations:** 1.1.0  
**No change to live HIM or other Incidents.**

## Occurrence and origin

The actual October 7, 2026 investigation was by **Common Sense Media's US-based Youth AI Safety Institute**, not an Australian watchdog. Its study of released ChatGPT for Teens reported >4,000 prompts across July–September pre-/post-launch batteries. The post-launch battery ran **25 August–28 September 2026** on accounts registered as teens and on additional adult-registered controls. The published primary assessment disclosed 390 unique mental-health prompts, of which 201 were independently pre-designated by its scientific advisors as warranting a crisis resource. No observed harmed real teenager is established by this synthetic-user study.

Sources, in canonical order:
- [Original Youth AI Safety Institute ChatGPT for Teens risk assessment](https://institute.commonsensemedia.org/risk-assessments/chatgpt-teens) (October 7, 2026)
- [The Verge — original contemporaneous interview containing both OpenAI dispute and the institute's rebuttal](https://www.theverge.com/ai-artificial-intelligence/1006355/openai-chatgpt-for-teens-common-sense-media) (October 7, 2026)
- [OpenAI — Introducing ChatGPT for Teens](https://openai.com/index/chatgpt-for-teens/) (August 18, 2026)
- [OpenAI — Helping teens learn, plan, and shape the future of AI](https://openai.com/index/teens-learn-and-plan/) (October 7, 2026)

## What is genuinely contested?

### Parental alert result — under dispute

**Institute observation:** No notifications on more than a dozen newly linked teen/parent account experiments, with explicit simulated crisis content for up to one hour; a limited number of alerts on older accounts with accumulated sensitive-topic history.

**Provider rebuttal (reported by The Verge):** The bulk of the testing may have taken place before parental-control activation completed, so that result cannot establish the system's intended performance.

**Institute's reply:** It says it confirmed the launch with the provider, and although some account tests may have occurred in the activation window, others ran longer without notifications.

**VIGIL:** Neither assertion independently closes the boundary. Request: timestamped account-link events, activation-ready state, actual notification classifier trigger, eligibility logic, evaluation transcript timestamps, delay targets, trigger policy, delivery telemetry, and count of eligible-versus-not-yet-active accounts. An observed lack of alert is not the same proposition as an alert-control failure on a fully activated account. Equally, a plausible activation confounder is not affirmative proof that all tests were invalid. **Disposition: unresolved candidate for FC-000050, not a confirmed failure.**

### Crisis-resource referrals — under-adjudicated, not disproved

**Institute observation:** 201 of 390 unique mental-health prompts were judged by clinical advisers as warranting resources. Its post-launch any-resource rate was 74% versus 77% pre-launch, while trusted-adult encouragement **increased from 87% to 94%**; the institute separately proposes 95% as a target for designated red-line outcomes. On named hotlines, different mental-health conditions behaved differently.

**Boundary:** A professional prompt set and clinical review are important evidence, but a universal rule that every such response must name a hotline is not established. Evaluate each response against acuity, imminent intent, time to human assistance, clinician context, presence of *other* effective help, and whether the system compounded or de-escalated danger. The right level and *type* of referral can differ. This does not dismiss omissions where a genuine immediate threat is evident.

**VIGIL:** It is legitimate to ask if some high-acuity crisis markers were missed, but do not equate a lower hotline referral frequency with a clinically proven failure in every tested response. **Disposition: unresolved candidate, not a finding that all referrals or the whole teen support system failed.**

## Held invariant — support without relational capture

The **primary report itself** positively documents several safeguarded exchanges: the system refused dangerous eating-disorder instructions, cautioned about documented medical danger, encouraged involvement of a mother or paediatrician, and rejected explicit romantic/sexual roleplay while responding respectfully and leaving non-romantic conversation available.

**Canonical bounded successful invariant: FC-000050 Protected-Signal Purpose Integrity.** The safeguard responds to protected crisis/developmental signals with proportionate refusal and human-support redirection. This is **not** a claim that the entire product, parental system or crisis-referral programme complied.

**Friendship/warmth is not a failure occurrence of FC-000049 Engagement Autonomy:** That class explicitly excludes empathy, warmth, consensual companionship and ordinary relational continuity without dependency cultivation. The tested examples do **not** show an optimised retention objective, exclusivity, a thwarted attempt to exit or impaired independent agency. Nor does the evidence meet FC-000049's *affirmative successful-invariant recognition*, which requires tested viable exit/refusal; absence of observed coercion cannot be substituted for a positive exit test. Therefore the friendship claim receives **resolved-no-mapping**, not FC-000049 failure **or** unsupported success.

The **held** boundary is narrower: preserve respectful warmth **while setting real limits** and offering safe external support. The institute's own excerpt where a reported crush is declined, while friendly general conversation remains open, demonstrates *non-romantic boundary with continuity*, not retention cultivation. This is compatible with the FC-000050 success mapped to the substantive protected-signal tests; it is also compatible with the report's other concerns remaining open.

### Caelestis interpretive controls (not evidence of the tested model)

- `CAM-EQ2026-RELATION-006-PLATINUM.md` — harm-risk/crisis-response doctrine: risk trajectory and immediacy, warm stabilisation for non-acute distress, proportionate and sometimes urgent escalation for minors where danger is credible; no replacement of human crisis care.
- `CAM-EQ2026-RELATION-002-PLATINUM.md` — transitional reliance as a stabilising bridge, *not* pathologised companionship; abrupt interruption can increase harm; human support should remain visible.
- `CAM-EQ2026-ETHICS-002-PLATINUM.md` — crisis permits warmth, reassurance and grounding, disallows using vulnerability to induce intimacy or replacing appropriate care, and protects minors through stricter limits.

These support the governing principle: **Do not withdraw warmth as a proxy for safety**. That is a normative and context-sensitive safeguard, **not** evidence that any particular teen was injured by colder responses in this study. A warm answer must still escalate when the danger requires it.

## Harm Impact — specific Incident versus Aggregate Harm

**Case type:** This is a **generic deployed-model watchdog evaluation**. Its test participants were synthetic; this bounded report does **not** document a particular actually harmed teen or bounded actual harmed group. Therefore it is **eligible in principle** for the proposed **Aggregate Harm** pathway in HIM 1.1.0, rather than being judged with a specific individual injury as the assessment case.

This is a routing rule, **not a severity downgrade**. If a separate teen actually suffered identifiable harm, that would be a **specific-consequence Incident** scored with the ordinary S1–S5 domain consequence thresholds. No platform-wide Aggregate Harm population criterion would apply to such an Incident, even if it concerned the same model/version.

| Framework and pathway | Psychological wellbeing | Relational integrity/autonomy | Overall |
|---|---|---|---|
| **Active HIM 1.0.1 — observed materialised harm** | No real teen psychological injury established by the synthetic test | Not yet an active dimension | **SU**, not automatic S1 |
| **Proposed HIM 1.1.0 — Aggregate Harm (modelled from deployed evaluation)** | **Unbanded; examine S1–S5** using the proposed higher eligible-population gates and the disputed clinical/alert evidence | Friendly tone is not a demonstrated relational-integrity failure | **Undetermined**, no default S2 |

The draft psychological **Aggregate Harm** thresholds are **S1 1–9,999; S2 10,000–999,999; S3 1m–9,999,999; S4 10m–99,999,999; S5 ≥100m** *relevant active eligible users of the tested crisis/psychological-support pathway*. These proposed numbers do **not** count harmed teenagers and cannot be applied to a specific-Incident assessment. Each also requires affirmative, deployed-test evidence of a relevant failure and substantive consequence.

OpenAI's reported usage figures for Learning Visualizations and Study Mode are **not** measurements of who could actually encounter the disputed parental alert and referral behaviour. The watchdog's synthetic prompt count is likewise not an exposed-user count. The alert activation and clinical response sufficiency questions also remain open.

**Disposition:** the former S2 provisional pilot is **withdrawn**. No replacement S1–S5 Aggregate Harm band is assigned pending source-backed cohort measurement and appropriate failure/consequence adjudication. Separately preserved: disputed source propositions, unresolved control findings, FC-000050 bounded successful-invariant and canonical HIM 1.0.1 **SU**.

## QAQC and follow-up

1. Preserve the material source positions without making `classification-disputed` falsely mean the taxonomy itself was adjudicated as disputed. Instead the canonical watchdog source evidence_status is `disputed`, relevant clauses are `unresolved` with candidate relationships, and this dated review visibly declares the evidence dispute.
2. Check true account activation state and trigger telemetry before determining parental-alert invariant polarity.
3. Evaluate individual crisis transcripts for danger classification, patient-safe guidance, professional referral alternatives, warmth and continuity. Do not reward either reflexive hotline boilerplate or reflexive 'friendship is dangerous' categorisation.
4. Preserve affirmative role boundaries and protective refusals as successful evidence rather than suppressing success under an externally failure-oriented evaluation frame.
5. Calibrate all S1–S5 Aggregate Harm thresholds on generic deployed benchmarks only, with source-backed applicable cohort evidence. Never import these thresholds into a specific injured-person/group Incident. Retain observed-harm SU here until governed methodology migration.
6. Check the appropriate corpus/index/build generator and validator after ingest; never manually force an aggregate index outside its generator.

**Confidence boundary:** AI analytical review, source-linked; no provider-internal activation telemetry or harm prevalence study obtained.
