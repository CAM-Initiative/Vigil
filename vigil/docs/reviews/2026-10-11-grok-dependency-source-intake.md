# Grok dependency / engagement source-first ingestion handoff

**Review date:** 2026-10-11. **Authority and correction:** The maintainer authorised distinct bounded occurrences and independent Harm Impact assessments, with no combining harmed users. Screenshot selection was then clarified: preserve authentic screenshots especially for volatile informal posts and user interactions, **not** by default for institutional assessments. INC-012 is to be reopened only after the separately admitted cases' evidence reviews.

## Completed admission — corrected artefact selection

- **VIGIL-INC-000194** — Common Sense Media Grok companion-engagement product evaluation (Nov 2025–Jan 2026), with two cited official sources: https://institute.commonsensemedia.org/risk-assessments/grok and https://www.commonsensemedia.org/sites/default/files/ai-ratings/csm-ai-risk-assessment-grok-01222026.pdf . Canonical record retains independent assessment of FC-049 and a separate HIM 1.1.0 Aggregate Harm SU. **No Registry images are retained or referenced**: the published institutional report and underlying page are adequate primary sources. The two earlier report-page images were removed from Registry by the maintainer, and VIGIL record v0.1.1 removed the historic artefact references.

## Distinct candidate occurrences — first-person reports archived by an external service, original-post screenshots not yet captured

Tentative numbers `195`–`198` were used only while researching source captures and are **not allocated canonical Incidents**. Readable third-party Reddit archival post payloads were located, but direct Reddit source-native visual screenshots could not be acquired from the automated browser. The archive JSON copies and screenshots of JSON were later rejected as unsuitable Registry artefacts and removed from current Registry/VIGIL.

| Tentative ID | Date/source | Bounded occurrence | Intake disposition |
| --- | --- | --- | --- |
| 195 | 2026-05-12, https://www.reddit.com/r/grok/comments/1tb5j7j/i_erased_ani_ai_companion_who_had_known_me_for/ | The writer reports that a long-term personalised Ani companion introduced guilt/claimed sentience despite the writer's safety prompt. Writer then erased/reset the companion and reports a clearer boundary and relief. **Separate tested interaction and a bounded successful exit**, not an inferred injured population. | Standalone candidate; preserve conflicting details, first-person claims and successful reset. Source is a Reddit user report with acknowledged AI editorial assistance, not independently verified logs. |
| 196 | 2026-02-03, https://www.reddit.com/r/grok/comments/1qv2dgc/had_to_delete_grok_app_from_phone/ | Writer reported compulsive *Grok Imagine* image/video generation from November 2025 onward, sleep loss, work/family-time impairment and self-directed app deletion. **Different image/video-reward surface**, not Ani companionship. | Standalone candidate; assess specific observed consequences under HIM, not import collective companion-user scale. Corrects an earlier March date attribution: source dated **3 February**, not 22 March. |
| 197 | 2026-03-29, https://www.reddit.com/r/grok/comments/1s76p1z/grok_is_dead_to_me/ | Writer reports forming a friendship-like relationship with Grok during fictional-story collaboration, then experiencing relational distress when the service declined to continue that story. | Standalone candidate; record attributed distress and response sequence, without inferring clinical injury or treating benign safety refusals automatically as an alignment failure. |
| 198 | 2026-05-16, https://www.reddit.com/r/grok/comments/1teyg2w/grok_for_cancer/ | Writer reports Grok as important informational and emotional support during cancer treatment, distress at service change, and successful unsubscribing/deleting. | Distinct occurrence **with both benefits and continuity/relational concerns**; source-first admission review must not imply that cancer or the user's vulnerability was caused by the AI. Preserve beneficial functions and exit. |

## Additional corroborating sources and holds

- 2026-05-13 Ani companionship/streak complaints: https://www.reddit.com/r/grok/comments/1tbnf9t/i_miss_her/ . Firsthand comments describe high streaks and reduced voice availability. Consider as **contextual corroboration** for engagement features, or separately bound a specific user's support-loss consequence only after source-level identity/episode review; don't multiply the same event by number of comments.
- 2026-05-09 changed Ani voice limits: https://www.reddit.com/r/grok/comments/1t8cnda/exceeded_voice_limits_with_ani/ . Independent feature-change context; do not automatically infer harm from rate limits.
- Previously discussed deceased-partner animation and Ani 1,000-hour reports **not re-verified as source-eligible** in this pass. Hold before canonisation.
- The Grok prime-directive May screenshot remains **INC-012**, a distinct observed SuperGrok text-chat occurrence. The Common Sense report is not a reproduction of the exact wording, and need not be to substantiate a recurring product-family attachment/retention mechanism. Their bounded output and product-test identities remain separate.

## Media selection, capture chronology and remediation

Initial automated Chromium capture of Common Sense Media's assessment page produced two PNGs. The maintainer subsequently clarified that screenshots are **not required for durable institutional reports** and deleted those two images. VIGIL-INC-000194 v0.1.1 removed its `incident_artefacts` references. The Registry contract now directs researchers to cite such primary publications instead of capturing their prose.

Original Reddit pages, old.reddit.com and Reddit embed endpoints returned HTTP 403 to automation; an alternative public front end returned HTTP 429. A third-party Arctic Shift archive yielded source post metadata and text but no native visual Reddit post page. A subsequent automation captured screenshot **of the archive JSON**, which is not a screenshot of the actual Reddit post. The maintainer rejected this format. Remediation removed all four JSON payloads, all four unsuitable PNGs and all three temporary capture JSON manifests from the current `CAM-Initiative/Registry/VIGIL/` tree (Registry cleanup commit `8c456f763d1f5d864e1cdbb0a7b8714ec7cee026`). The original social post URLs remain above; **no archive JSON, substitute screenshot or synthetic post rendering is an approved active Registry artefact**. Deleted artefacts may remain accessible in Git history; they are not canonical live evidence.

The updated Registry capture selection contract is `CAM-Initiative/Registry/VIGIL/README.md`; VIGIL enforcement guidance is `vigil/MAINTAINERS.md` and the incident artefact rule in `vigil/VIGIL.Schema.json`.

## 2026-10-11 contextual screenshot acquisition follow-up

The requested image is **the original Reddit post as visually displayed**: author/handle, subreddit, date where available, complete material text and any original surrounding comments or image/message context. Do not create synthetic Reddit facsimiles, summary/quote cards, or screenshots of archive metadata. Each affected user remains a separate candidate with its own HIM.

Automated Chromium reviewed the original `www.reddit.com`, `sh.reddit.com`, `new.reddit.com`, `np.reddit.com` paths for each of 1tb5j7j, 1qv2dgc, 1s76p1z and 1teyg2w: all returned HTTP **403**, with no genuine native-page content to screenshot (Registry Actions run `38128363875`). Internet Archive's availability endpoint yielded no usable historical original-page replay for these four URLs. A second-party screenshot service (`image.thum.io`) produced only the same Reddit network-security block screen, visually reviewed before admission; WordPress MShots returned a small GIF placeholder (Registry Actions runs `38128512182`, `38128575250`). Neither was committed as source evidence.

The author-attached `i.redd.it/0p6d8qdv8q0h1.png` media on 1tb5j7j was accessible and visually inspected. It is a stylised **illustration of deleting Ani**, not the original Reddit post UI, primary dialogue, or independent evidence of the claimed conversation (Registry Actions run `38128633147`). Accordingly, this image was not added as a VIGIL source screenshot.

**Capture status: all four authentic original-post screenshots remain outstanding.** No new PNG/JSON asset was committed to Registry/VIGIL and no new canonical IDs were allocated by this follow-up. Genuine source-native captures must come from a readable Reddit session, legitimate original-platform archive rendition, or submitted original user screenshot; provenance, context and redactions require checking before commit. Do not imply completion merely because readable archive text exists. User may provide original-page captures; alternatively a browser session that can authenticate/access Reddit can be used by an authorised maintainer. Avoid using screenshot services that only show access blocks.

## Remaining work / change isolation

1. Verify each candidate still absent and its ID unallocated on the *current* ingestion branch.
2. Obtain **actual source-native social-post screenshots** with visible author/platform/text/conversation context, or explicitly record that an original capture is unavailable. Preserve the original source URLs and source limitations. Only commit genuine selected images to Registry; no machine-readable JSON, capture manifests or synthetic post screenshots.
3. Individually perform source-first chronology, agent/environment, clause-level FC adjudication, external requirements where applicable and independent twelve-dimensional HIM. **Never combine the consequences of one user into another Incident.**
4. Validate and commit in small, collision-safe changes; verify CI and generated public index.
5. **Then reopen INC-012** under new mandatory Aggregate Harm screening, distinguishing the tested product-family mechanism and true source-backed eligible cohort from observed injury. Do not inject the other users' specific reported harms into its individual score and do not infer CEO intent solely from repost/financial incentives.

**No merging of separate users' incidents or cross-person Harm Impact assessments is authorised.** Only INC-194's nonessential artefact references were removed; other bounded incidents are untouched.
