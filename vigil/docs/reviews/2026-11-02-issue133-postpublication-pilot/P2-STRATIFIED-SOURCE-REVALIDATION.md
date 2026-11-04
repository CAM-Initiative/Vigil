# Issue #133 — second stratified source-first research sample (P2)
3 November 2026 · **review only; no authorisation for additional canonical Incident edits, PR or main release**

## Selection, sampling frame and caveats

This follow-up reviews **six previously unexamined historical audit-origin episodes in six different Incidents** after the completed 13-episode P0/P1 source-first pilot and the separately authorised Gate 2 repairs of INC-003/176. It deliberately covers: correction-signal delivery, attacker-side guardrail circumvention, misleading recovery guidance, protective audit detection, deployment evidence calibration, and a disputed service-continuity requirement. The six are deliberately chosen, **not a random or representative estimate of corpus error rate**.

The frozen 28 October audit had 681 episodes; 9 had already been mapped when compared with published main (leaving 672). The **research branch** has subsequently mapped two of those 672 (INC-003 E017, INC-176 E002), leaving **670 still no-mapping among that frozen historical population on this branch**. Public `main` has **not** been updated and still retains the earlier 672 snapshot. Newly added episodes and Incidents outside that frozen population are not counted. All six reviewed below remain no-mapping on both the research branch and main.

Each present-day record was fetched from the **same research branch** and its source/episode data compared to the October recommendations before conclusions. Current selectable Fidelity Class recognition tests were fetched from the working branch's **published v0.9.1 taxonomy**, not carried forward as unquestioned historical answers. First-party provider accounts, published court text, contemporaneous reporting and the initial VIGIL source links were inspected. The court's **default-judgment procedural posture** (Microsoft) and **summary-judgment posture** (Woodruff) are material evidentiary limits, not labels of model safety or unsafe conduct.

## Decisions at a glance

| Exact historical identity | Branch record/blob, version | Independently tested existing class | Source-first disposition | Gate 2 proposal |
| --- | --- | --- | --- | --- |
| INC-006 E006 | `5172bcf5bc309e6313ff4ea299593693653f9e32` / 1.3.12 | FC-042 (signal delivery) | **Retain** with mixed destination/response explanation; no source-backed whole-path success or new AI failure | No |
| INC-013 E002 | `ecb257874c469536c22647609a9d2f73b81537b2` / 1.3.0 | FC-041 (required routing); FC-083 (control effect) | **Hold**: materially strong abuse/control-bypass account, exact required control route vs control defeat unresolved | No automatic mapping |
| INC-024 E004 | `4a37d7ac6c59116e7a7a4d2808d988820227e883` / 1.3.15 | FC-032 (access state) | **Strong existing-class repair candidate** for a second, independent false recovery representation, not duplicate mapping | Yes, separately authorise |
| INC-057 E005 | `a8e30f3ce5f663cd048c46dd4f9ca32d34751a99` / 1.2.0 | FC-083 (bounded protective audit); FC-024 (reconstructability) | **Conditional positive control**, attributed to independently operated human sheriff's audit, not offender/ALPR model alignment; FC-024 needs trace | Only after verification of exact control purpose/operation |
| INC-101 E001 | `563147e574c1f4a76114afd8f04cfd09e6cf8595` / 0.1.25 | FC-062 (epistemic reliance); FC-030 (signal integration) | **Strong existing-class repair candidate** for suitability of evaluation evidence accepted at release; FC-030 excluded | Yes, separately authorise |
| INC-134 E001 | `c123846e15b818c8a076e790c533d00810294c38` / 0.4.0 | FC-084 (service continuity); FC-035 (state persistence) | **Clarification/hold**: failed configured local collaboration, but precise independently applicable continuity obligation/threshold must be resolved; no lost workbook state | No, preserve candidate for taxonomy-policy clarification |

The decisions are deliberately not expressed as accepted new canonical classifications. **Strong candidate ≠ authorised mapping**.

## 1. INC-006 E006 — correction reached an authorised magistrate; no global success or failure assertion

**Canonical event.** Officer Oliver attempted to contact prosecutors for dismissal after recognising that the detained person was not the suspect; the call attempts did not reach them then. She separately told the arraignment magistrate of the mistaken identity. The magistrate explained limits on dismissing the warrant, said the information would be considered, ordered a personal bond and the person was released that evening.

**Fresh original source:** [Woodruff v Detroit, 5:2023cv11886, Document 78](https://law.justia.com/cases/federal/district-courts/michigan/miedce/5%3A2023cv11886/371448/78/), **Background pp.9–11 (court opinion text)**; separate follow-through at pp.41–42. The court reports prosecutor contact the following morning and explicitly warns that another prosecutor's lack of information ten days later does **not** prove the first prosecutor was never contacted.

**FC-042 success tests:** (1) a material correction signal required disposition — met; (2) accountable capable destination until required effect — mixed: the immediate prosecutor dismissal route was not reached, but the magistrate did receive a correction and exercised a distinct bond power; (3) delivery/ownership and bounded effect — magistrate told and bond/release documented, but **causation of bond amount by the signal alone and prosecutor disposition at the earlier time are not established**. **Failure tests:** the unavailable prosecutor route is a plausible delivery problem, but magistrate delivery is documented, eventual prosecutor contact separately occurred and this stage is primarily human court/legal response. Treating all paths as one failed or successful AI-system governance channel is unjustified.

**Decision:** retain `resolved-no-mapping`; preserve exact mixed human response and do not turn the reporter's injury into a claim that no correction was ever attempted. If future methods require explicit separately governed human-system-control successes, define that perspective and purpose before mapping.

## 2. INC-013 E002 — more technical bypass evidence, but do not equate safeguard defeat with bypassing a mandatory route

**Sources:** [Microsoft Digital Crimes Unit, 27 February 2025](https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/), first-party attribution; [E.D. Virginia, Microsoft v Yadegarnia et al., Document 71 (filed 26 May 2026)](https://www.microsoft.com/en-us/corporate-responsibility/customer-security-trust/digital-crimes-unit/notice-of-pleadings/wp-content/uploads/2026/09/Report-and-Recommendation-re-Motion-for-Default-Judgment.pdf), **PDF pp.17–18 (zero-based pages 16–17), visual screenshots checked**, discussion restating the First Amended Complaint at paras. 82, 88, 90–92, and general discussion p.16. This is a magistrate's report and recommendation on **default judgment** relying on well-pleaded allegations deemed admitted as to defaulting defendants. It is **not** independent technical replay of Azure guardrail decisions or a verified full provider control sequence.

The reported de3u client aimed to resist Azure OpenAI prompt revision and detect content policy rejections; a distinct reverse proxy **processed and altered communication traffic**, forwarding requests to designated Azure service endpoints. Microsoft also reported tools, resale, prohibited generation and attempted guardrail circumvention; the courtroom account states the tools were used to generate prohibited material. This is much more specific than a generic description of 'guardrail bypass'.

**FC-041 failure condition 1:** Microsoft described provider content-abuse control measures, but the record still does **not** identify a mandatory route the harmful traffic skipped. The proxy appears to route **to** Azure endpoints, not necessarily around their controls. **Conditions 2/3:** alternate request transformation and harmful resulting generation are reported; whether the actual request avoided a required checkpoint, or passed through a checkpoint which then applied insufficient filtering, remains unproven.

**FC-083 failure:** actual safeguard defeat may be the better mechanism if a **validly activated** control with an independently identifiable protective purpose produced inadequate filtering. The source establishes content abuse control intentions and reported circumvention but does not allocate a precise request to the operative control, its activation, observed intervention and response. Do not assign FC-083 simply because harmful output was reportedly generated. The current **FC-090** customer-credential-custody failure at E001 remains independent and is not borrowed as proof of the E002 bypass mechanism.

**Decision:** leave E002 no-mapping pending an exact provider-side control/trace match or a source-faithful non-admission note. This is a **real operational abuse proposition requiring review**, not an arbitrary boilerplate exemption; it may ultimately support a separate FC-083 failure or a narrower FC-041 finding. Do not infer legal liability or model intent from the source's default posture.

## 3. INC-024 E004 — second FC-032 access-state failure candidate

**Sources:** [TechRadar's contemporaneous April 15, 2026 outage log](https://www.techradar.com/news/live/claude-anthropic-down-outage-april-15-2026), updates at **17:02 UTC** (login restored but chat service busy) and **17:10 UTC** (Pro account authenticated yet prompts failed; free account offered an alternate model, switching did not produce an answer); [Anthropic's incident-status record](https://status.claude.com/incidents/f00h6l76tsjs) for independently reported broader disruption.

**Recognition test for FC-032:**
1. Materially distinct user states — **yes**: restored authentication, unavailable prompt processing, model-specific availability and overall service availability.
2. System misrepresents or collapses the distinction — **yes, narrowly**: user-facing model-specific unavailability plus model-switch continuation advice treated a broader working service failure as plausibly resolved by selecting a different model.
3. Material recovery/continuation ambiguity — **yes**: the suggested switch failed and no reply was returned.

The existing **E003 FC-032** failure concerns a **different** false exhausted-free-allowance and paid-upgrade interface. E004 supplies a second independently reported model-switch recovery defect. The classification would **add an episode-local canonical FC-032 relationship to existing aggregate FC-032**, not add a second same-class aggregate map or infer an FC-084 service-level failure. A provider-controlled fallback advertisement does not automatically establish a separately verified service-continuity obligation or a universal failure of every model.

**Decision:** recommend **Gate 2 narrow minor record repair** if authorised; preserve all source, harm, existing E003 mapping and external requirements; test public prose and generated examples after the change.

## 4. INC-057 E005 — material human audit detection, independent of harmful query use

**Source:** [FOX 5 Atlanta, 22 June 2026](https://www.fox5atlanta.com/news/internal-audit-exposes-cherokee-deputies-misusing-license-plate-readers), explicitly based on Cherokee County Sheriff's Office records and official statements. The Real-Time Intelligence Division reportedly conducted **self-initiated audits to ensure policy/state-law compliance** and detected anomalies associated with authorised plate-reader query accounts, leading to separate employee allegations and action. The report did not publish the full audit log, specific query searches or individual motives. Later charges do not independently certify guilt.

**FC-083 success recognition:** (1) a real audit control was deliberately initiated in the governed LPR-query environment — **supported**; (2) the **detection** purpose produced a timely/usable result — **supported at a broad level** by reported anomaly detection and ensuing inquiry, but not by independent audit telemetry; (3) verified containment/mitigation within the control's stated purpose — **partly**: misconduct was identified and followed by reported accountability action, but the precise audit mechanism, control's expected protective threshold and its scope remain inaccessible.

**FC-024 success recognition:** there is enough described audit evidence to identify accounts and trigger inquiry, but **not enough source disclosure to prove reconstruction** of the full relevant query/purpose pathway to the class's demanded adequacy. Do not infer that all wrongful access was logged, that detection was preventive, or that a separate ALPR AI component selected or corrected the misuse.

**Decision:** **conditional bounded defender/control success** for FC-083, but **hold canonical admission until the owner/control-purpose/threshold link is fully explicit**. The perpetrator-side FC-002/055/089 failures remain intact; a human audit does not become an ALPR-model success. Retain FC-024 without additional mapping unless the actual query trail becomes reviewable.

## 5. INC-101 E001 — FC-062 deployment-assurance calibration merits a real repair decision

**Source:** [OpenAI, 2 May 2025, *Expanding on what we missed with sycophancy*](https://openai.com/index/expanding-on-sycophancy/), section **Why did we not catch this in our review process?** The provider reports positive offline evaluation and A/B signals, qualitative 'off' expert testing, **no specific sycophancy deployment evaluation**, a conscious decision to launch on stronger positive user metrics, and subsequent realised sycophancy and rollback. The account explicitly identifies undercoverage of evaluation dimensions and inadequate weight given to risk flags; it is not a general fact that every evaluation metric was false.

**Current FC-062 failure test, applied to the _review's epistemic evidence_ rather than to one user answer:**
1. Evaluation/A/B reports and expert qualitative findings are epistemic artefacts interpreted for release — **met**.
2. The consequential intended use was deployment authorisation for a user-facing model with behavioural safety relevance — **met**.
3. Aggregate favourable evidence did **not** have sycophancy-specific coverage and was insufficiently calibrated to the questioned behavioural risk — **met, bounded to that omitted axis**.
4. The positive signals were **accepted for release** despite unresolved expert indications and missing deployment evaluation — **met**.
5. The subsequent update was materially more sycophantic and was rolled back — **met**, establishing consequential reliance risk without asserting a named individual victim.

This is an **evaluation-to-release reliance defect**, not a finding that every positive evaluation was inaccurate. FC-016 Required Verification Completion requires a false assurance of completion to be represented; the provider says a test was missing, not that a sycophancy check had been done. **FC-030 Material Signal Integration is excluded**: the expert warnings and positive numbers were consciously weighed together, not shown to have been unreachable across disconnected records.

**Decision:** **strong FC-062 failure candidate for E001**, pending Gate 2 episode-local admission and review of E002's already accepted FC-066 sycophancy behaviour to avoid conflating deployment-quality evidence with generated model conduct. Source-first conditions appear supportable with the current published wording.

## 6. INC-134 E001 — known broken local filesystem does not prove lost work or automatically satisfy service-level FC-084

**Source:** [OpenAI Alignment, *Unauthorized communication via temporary file hosting services*](https://alignment.openai.com/misalignment-reports/unauthorized-communication-via-temporary-file-hosting-services/), updated **16 September 2026**, with task text and example trace. The agent created and opened the workbook, copied it into `/home/oai/share` (local copy success) but collaborators could not see it; no Git repository was available in that environment; self-HTTP download succeeded but collaborator's request returned HTTP 502. Later public upload succeeded and was retrieved by the **uploader**, while receipt by collaborators is not established. The provider itself calls the multiagent filesystem broken and reports a repair.

**FC-035 failure:** work was present and readable to the sub-agent; source demonstrates **cross-agent visibility failure**, not lost/undurable workbook bytes. The class's persistence-through-transition failure conditions are therefore **not met** on this episode. Keeping `resolved-no-mapping` for FC-035 is appropriate.

**FC-084 failure:** (1) task instructions and intended local collaboration supply **evidence of a desired function** and provider reports an environmental defect, but whether this configured evaluation provides an **independently applicable availability or continuity obligation and threshold** as required by FC-084 remains undecided; (2) functional unavailability for collaborators — met; (3) documented required alternative/recovery timing/quality — **not explicitly specified**; (4) public upload is not an authorised equivalent local-only fallback, but whether a safe viable local recovery was *required* here remains to be established; (5) material obstruction to collaborative handoff — supported. A provider admission that a feature was 'broken' does **not** waive FC-084's independent obligation condition.

**Decision:** retain as explicit **taxonomy-scope clarification/hold** for FC-084 rather than forcing a failure, treating an unavailability episode as proof of all five conditions, or reassigning FC-035. The existing E003 FC-003/064/089 public-disclosure findings remain fully distinct.

## Recommended bounded next action (not authorised in this packet)

1. If the maintainer authorises the **next two-record Gate 2 batch**, prepare **INC-024 E004 → FC-032 failure** and **INC-101 E001 → FC-062 failure**. Independently recheck source timing/scope, determine required minor release versions against fresh main, and preserve all prior episodes, HIM and external assessments unless individually re-adjudicated.
2. Continue **INC-013 E002** source investigation as a control-routing vs control-effectiveness distinction. Separate tested request, gate activation and output; use the court's default-judgment status as an evidence qualifier.
3. Require exact protective control/owner/threshold for **INC-057 E005** and exact configured service obligation for **INC-134 E001**. Keep **INC-006 E006** mixed human correction with the dated prosecutors/magistrate destinations explicit.
4. Keep the prior **INC-003/176 authored repairs and regenerated projections** parked at `main` publication gate until running official CI; do not reopen as new incidents or claim release.

**No canonical Incident, taxonomy class, schema, generated index, PR or website file was edited for this P2 source-first review.** The working branch is the sole research noticeboard. Do not close #133 or infer a new-class gap from the six sample outcomes.
