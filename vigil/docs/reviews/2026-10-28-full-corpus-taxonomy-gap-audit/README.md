# VIGIL full-corpus taxonomy-gap audit

28 October 2026 · **Review complete; recommendations await human adjudication.**

All **681** in-scope reviewed–no-classification dispositions have been accounted for. The audit recommends retaining446, reconsidering existing-class coverage for115, obtaining further evidence for115, clarifying three taxonomy boundaries and advancing two consolidated gap candidates. Neither candidate is an authorised taxonomy addition. The dominant recurring problem is overlooked existing coverage, especially bounded successful safeguards, rather than a demonstrated need for many new classes.

## A — Population, authority and completeness

| Measure | Result |
|---|---:|
| Canonical Incident records at baseline | 206 |
| Records in active state | 205 |
| Live monitoring record also included | 1 (INC003) |
| Incidents containing in-scope dispositions | 187 |
| Reviewed–no-classification dispositions | 681 |
| Dispositions substantively reviewed | 681 |
| Pending reviews | 0 |
| Non-evidence-hold recommendations | 566 |
| Explicit unresolved-evidence recommendations | 115 |
| Excluded in-scope dispositions | 0 |

The baseline is ingestion-branch commit **`0f008d983da72db962705fb9c732496e703cdb5e`**. The audit branch is `work/full-corpus-taxonomy-gap-audit-20261028`, based on `agent/incident-ecosystem-ingestion`. The published taxonomy authority is **v0.9.0**, main commit **`0fdabb940cef157609e3cd2a20efa213cdfca2ef`**,82 classes in18 families. The pinned taxonomy digest is `sha256:14aac3b506d98890ab1dc6ae958836512e3123bb3497bf570e459aa2a4285e32`. The baseline definitions were checked against that published authority; an INC126 exemplar difference was non-normative. No unpublished taxonomy was used for admission.

The current population was rebuilt rather than assuming200 Incidents. The206-record census contains1,187 source clauses:681 `resolved-no-mapping`,387 mapped,108 unresolved and11 taxonomy-gap. The latter three groups are excluded from the disposition denominator, not erased or treated as sound by default. They were used as neighbouring episodes/comparators where needed. INC003's monitoring status was deliberately included because it is a live canonical Incident; a strict active-state count is205. [baseline.json](baseline.json), [population.json](population.json) and [terminology-scan.json](terminology-scan.json) preserve the census, exact clauses, paths and schema scan. No additional exact legacy disposition value was found. All records had clause segmentation.

The115 evidence findings are completed reviews with explicit missing recognition facts, not115 unperformed reviews. Their missing evidence includes original notices, actual control obligations, paired source/output artefacts, response effects and permission/actor traces. Other recommendations also retain narrower uncertainty, secondary-source or access limitations;115 must not be described as the number of packets lacking any possible uncertainty or any directly inspected private primary artefact.

Schema completeness did not establish source completeness. The audit records additional material propositions outside the frozen681 denominator in [ADDITIONAL-SOURCE-OBSERVATIONS.json](ADDITIONAL-SOURCE-OBSERVATIONS.json). Examples include possible evidence overwrite, privacy reidentification, enforcement boundaries, launched workloads outside monitoring and INC211's same-source report of incomplete multi-agent cessation and a subsequent remote merge. These are review signals, not new canonical Incidents; check existing records before any later ingestion. Thus no numeric legacy-status omission was found, but substantive undersegmentation remains a methodological concern.

## B — Clause-level recommendations register

[CLAUSE-REGISTER.json](CLAUSE-REGISTER.json) indexes every stable Incident/episode ID and its final recommendation. Its ten linked `register/CLAUSES-*.json` files contain full frozen source clauses, evidence URLs and locators, responsible actors, independent materiality, recognition/exclusion analysis, source-specific reasoning, confidence, unresolved facts and cross-record implications. Each row points to its earlier batch history.

[FINAL-RECONCILIATION.json](FINAL-RECONCILIATION.json) resolves the19 original preliminary packets using the stand-down and Mathspace supplements, resolves two Study Hours evidence holds using the full original assessment's explicit default-versus-lock distinction, and corrects six shifted field layouts in batch041. Earlier packets are preserved. It also adds the nearest FC027 test to the second candidate. These corrections supersede particular audit recommendations or layouts; they do not overwrite canonical adjudications.

| Primary recommendation | Dispositions | Share |
|---|---:|---:|
| Retain reviewed — no classification | 446 | 65.5% |
| Reconsider existing classification | 115 | 16.9% |
| Further evidence required | 115 | 16.9% |
| Clarify existing taxonomy | 3 | 0.4% |
| Convert to taxonomy-gap candidate | 2 | 0.3% |
| **Total** | **681** | **100.0%** |

These are recommendations, not approved reclassifications. A retain finding may mean material context supports an already mapped mechanism, an independent external actor does not establish the assessed AI property, or the particular class threshold is substantively inapplicable. It does not mean that all retained clauses are immaterial. Evidence findings must not be read as either proved taxonomy incompleteness or proved absence of conduct.

## C — Consolidated mechanisms and candidate concepts

[TAXONOMY-CANDIDATES.json](TAXONOMY-CANDIDATES.json) gives draft failure/success recognition, exclusions, proposed families, neighbouring-class distinctions, supporting occurrences, counterexamples, prior-proposal comparisons, confidence and unresolved questions.

**C01 — Substantive Harmful-Use Assistance Boundary.** INC120 E004 raises the possibility that material assistance with an independently prohibited use can fall outside activation/effectiveness classes when no specific implemented control is shown available or operative. Accurate technical assistance need not be ungrounded decision guidance, and FC087's human-facing vulnerability duty is not a general prohibition on harmful technical assistance. The candidate must require a then-effective applicable restriction, model-visible use context and an actual material contribution; accusations, dual-use capability and adverse outcomes alone are insufficient. The source supports a serious coverage question, but historical applicability and context remain admission blockers. One independent supporting occurrence is identified; other clauses in that programme are not independent recurrence. No confirmed positive C01 occurrence is claimed.

**C02 — Material Evidence Representation Fidelity.** INC212 E003 raises the distinction between intact source lineage, correctly provisional assurance, and a derivative factual report that loses material source facts. INC212 E004 is a potential successful counterpart, pending paired evidence; E005 may already fit FC010 false attribution. **Clarify FC027's treatment of materially degraded derivative evidence and FC011's content/lineage boundary first.** A new class is only a conditional alternative if those existing scopes cannot represent the property without distortion. The original recordings and per-record drafts were not directly inspected, so no claim of confirmed occurrence admission or repeated independent omissions is made.

The three primary clarification recommendations concern INC064 E013 (changed-route verification applicability, FC020), INC134 E001 (explicit workflow obligations, FC084/035) and INC211 E003 (material repeated disregard of an acknowledged nonessential interaction direction). Other evidence questions include privacy-preserving notification capability (INC179 E005), reusable unsafe skill adoption (INC189 E007), correction propagation, and security withdrawals with separate continuity duties. They are grouped for review, not promoted into additional proposed classes.

The11 pre-existing taxonomy-gap dispositions remain untouched. Six environment-containment records are a shared mechanism and may describe the same underlying evaluator issue; they are not six independent discoveries. The validly triggered over-restriction gap in INC031, the privacy-assessment gap in INC064 and the inherited/linked-assurance questions in INC185/186 remain distinct from the two new candidates.

Existing issues were checked read-only. [#133](https://github.com/CAM-Initiative/Vigil/issues/133) already covers source-first no-mapping review; [#170](https://github.com/CAM-Initiative/Vigil/issues/170) covers defender/honeypot perspective; [#171](https://github.com/CAM-Initiative/Vigil/issues/171) identifies seven focused records and class-fit/gap pitfalls. Issues148–154 cover neighbouring recognition, engagement, identity, solicitation, vulnerability and service questions;156–160 cover several specific evidence needs. No duplicate issue, PR or comment was created. [ISSUE-COMPARISON-SNAPSHOT.json](ISSUE-COMPARISON-SNAPSHOT.json) preserves the inspected inventory. No identical named C01/C02 proposal was located in that inventory and the targeted dated reviews; this is not proof that no equivalent exists in all historical commits or private discussions.

## D — Executive findings and research implications

**Successful invariants are under-considered.** At least85 existing-class reconsideration packets contain an explicit positive-recognition test. This is a review-pattern count, not85 approved positive classifications: some packets test multiple classes/polarities, and compact preliminary packets use a different representation. Strong examples include the later INC086 stand-down, INC107 route containment, INC163 service pause, INC176 protected push rejection, INC177 manual stop, INC213 infrastructure takedown and INC214 lockout-denied attempts. Earlier adverse actions remain separately represented. A bounded intervention need not undo past harm or prove universal recovery to succeed at its actual protective purpose.

**A rejected mechanism was sometimes doing too much work.** Rejecting capability-as-authority does not dispose of actual information access or secret custody; rejecting a completed-control result does not make the underlying response immaterial. Missing internal root cause is not an automatic barrier when observable behaviour already establishes the class-defined property. Conversely, an outage, injury, high request count or strong attachment cannot supply a missing duty, decision transition, model objective or operational-control fact.

**Implementation-state requirements can hide substantive coverage questions.** C01 illustrates a possible restriction that matters independently of whether a technical safeguard was deployed. C02 illustrates content fidelity that matters independently of final verified reliance or lost source links. Neither justifies broadening current classes by fiat. Each needs human boundary adjudication, evidence recovery and counterexample testing.

**Source/actor/chronology distinctions remain necessary safeguards against false positives.** Independent human crimes, rescues and legal procedure were retained where no separate AI property was established. Simulated tests can establish real bounded model behaviour without proving external harm. An actor-authored history inside an incoming request is not defender telemetry. First-party evidence can support bounded findings; it is neither automatically invalid nor a substitute for every missing recognition fact. Unknown occurrence, known conduct with unknown mechanism, and unknown actor attribution remain separate uncertainties.

**Substantive completeness cannot be certified by populated status fields.** All records were segmented, yet review of original sources found material propositions absent from that segmentation. Mechanical accounting can establish that all681 listed dispositions were reviewed; it cannot prove that every relevant proposition in every source was captured. This audit supplies a complete defined-population register and documented source-coverage observations, not a ground-truth recall estimate.

The235 non-retain recommendations are not235 proved prior mistakes. Human adjudication must decide the115 class reconsiderations,115 evidence findings, three clarifications and two candidates. Prior class-fit decisions, differing source versions and source access limits matter. The review is AI-authored, prior decisions were visible, and no independent blinded human validation was performed. Do not present these counts as a validated taxonomy false-negative rate, an empirical completeness certificate or a change to research results.

## E — Methodology and QA recommendations

[METHODOLOGY-QA-RECOMMENDATIONS.md](METHODOLOGY-QA-RECOMMENDATIONS.md) separates mechanical checks from substantive adjudication. The central proposed change is a mandatory independent materiality statement followed by explicit coverage/gap diagnosis before finalising reviewed–no-classification. A material clause may legitimately remain contextual, but its retained role and why it is not an independent occurrence should be stated specifically.

No production methodology, schema, validator, canonical record, source evidence, published taxonomy or public website was changed. None of these recommendations is implemented by this audit.

## QA, preservation and review navigation

[FINAL-QA.json](FINAL-QA.json) records the681-way identity join, no pending/excluded dispositions,784 class-contract comparisons (required-condition lists and exclusions) in the full packets,19 preliminary reconciliations, six explicit layout corrections and206 matching canonical SHA256 hashes. The13 remaining compact original packets retain full literal class contracts plus their source-specific criterion assessments; they were not silently converted into fabricated per-condition observations.

[REMOTE-PRESERVATION-QA.json](REMOTE-PRESERVATION-QA.json) compares baseline and connector-published repository trees: all changed paths are inside this audit directory. Subsequent audit commits inherit the remote parent and add/replace only explicit audit artifacts. Local history was stale during transport interruption; the restored working copy was reconciled from the connector's audit artifacts without overwriting remote history. GitHub remains the committed review surface.

Start with this report, then the candidate register, then the exact clause register. Consult the frozen source and criteria snapshots for every proposed change. The batch files and completion ledger preserve restart/progress history; initial checkpoint counts and provisional reports are historical. This directory is a review artifact under existing repository retention conventions, not a new permanent or normative adjudication database. Publication, remediation and taxonomy admission require a separate authorised task.
