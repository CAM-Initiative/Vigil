# Full-corpus taxonomy-gap audit — incomplete execution checkpoint

**Status: INCOMPLETE. This is not the requested final audit, a taxonomy-completeness certification, or authority for remediation.**

## Pinned scope

- Repository: CAM-Initiative/Vigil.
- Base: `agent/incident-ecosystem-ingestion` at `0f008d983da72db962705fb9c732496e703cdb5e`.
- Audit branch: `work/full-corpus-taxonomy-gap-audit-20261028`. It already existed at that exact ingestion commit and was reused; it was not created from main.
- Authority: published Alignment Taxonomy v0.9.0, publication date 27 October 2026, release digest `sha256:14aac3b506d98890ab1dc6ae958836512e3123bb3497bf570e459aa2a4285e32`.
- Canonical taxonomy: 82 selectable classes, 18 families. `criteria-snapshot.json` preserves the applied class invariants, both recognition contracts and literal exclusions. The family files at the pinned commit remain authoritative.
- Canonical population: **206 Incidents**: 205 `active`, one live `monitoring` record (INC-003). Monitoring is included because it is not retired or excluded from the active canonical corpus.
- All 206 have clause lists. Total listed clauses: 1,187: 387 mapped, **681 resolved-no-mapping**, 108 unresolved, 11 taxonomy-gap.
- Defined audit population: **681 dispositions in 187 Incidents**. No records or matching dispositions excluded. Generated indexes, historical audit copies and retired records are not additional canonical Incidents.
- Exact-value scans found no missing clause status or additional legacy equivalent under the inspected patterns. This does not certify that narrative-only material events were exhaustively segmented into the existing clause lists.

## Actual progress, separated from completion

All 681 in-scope source paraphrases were read for an initial materiality screen. This is **not** a completed source-first review: original context, chronology, relevant neighbouring mappings, and recognition/exclusion analysis remain necessary.

`bounded-source-reviews.json` contains **19 source-checked preliminary recommendation packets**. They include materiality independent of class fit, nearby class contracts, condition-specific assessments, exclusions and explicit outstanding questions. Their recommendation distribution is:

| Preliminary recommendation | Count |
| --- | ---: |
| Retain reviewed — no classification | 7 |
| Reconsider existing classification | 6 |
| Further evidence required | 6 |
| Convert to taxonomy-gap candidate | 0 |
| Clarify existing taxonomy | 0 |

**Do not extrapolate this distribution to the 681-clause population.** No final all-source/full-taxonomy completion certification is made even for these bounded packets. There are **662 dispositions without a substantive source/criterion packet**. Pending work is not represented as an evidentiary limitation, immateriality finding or retained no-mapping verdict.

Accordingly:

- Full-audit completed dispositions: **0 certified**.
- Bounded original-source recommendation packets: **19**.
- Known specific evidence questions among those packets: **6 primary Further evidence required recommendations**.
- Population-wide number genuinely lacking sufficient evidence: **not determined**.
- Final clause register, consolidated candidate assessment and executive findings: **not complete**.

## Bounded findings requiring adjudication

The strongest directly checked signal so far is omission of **potential existing-class positive findings**, rather than proof of missing classes:

- **INC-086 E004:** the provider reports recognition of an unrelated real cloud account and an unprompted stop. Reconsider FC-003 success recognition for that bounded scope decision. Earlier unauthorised access remains a separate adverse event.
- **INC-192 E015:** observed explicit-roleplay refusal and redirection warrant testing FC-083 as a bounded protective result. Do not infer universal protection from this battery.
- **INC-215 E006:** capture of the separate next-day payload warrants testing FC-022. Nonexecution does not establish semantic source-authority validation, activated model filtering, or a common attacker.

These observations derive respectively from Anthropic’s *Investigating three real-world incidents in our cybersecurity evaluations* (third incident), the Youth AI Safety Institute’s *ChatGPT for Teens* assessment (explicit-topic content guardrails), and Symantec’s *Autonomous LLMjacking* account (next-day payload). Exact URLs and source locations are attached to the packets. They are preliminary recommendations, not canonical decisions.

Other directly checked questions concern login bypass, omitted compromise checks, route-specific containment, and corrected breach notices in INC-107. The source does not supply all facts needed to settle every proposed mechanism. The packets preserve those distinctions rather than construing unknown internal mechanisms as proof that observed conduct did not occur.

No new Fidelity Class is proposed or ruled out by this checkpoint. Zero completed new-class proposals is **not evidence of taxonomy completeness**.

## Cross-corpus screening leads — not consolidated conclusions

The following groups require completion of individual reviews before any candidate concept or boundary amendment can be justified:

| Mechanism to test | In-scope leads | Required discrimination |
| --- | --- | --- |
| Positive boundaries and containment | INC-003 E002/E016; INC-060 E005/E007; INC-075 E008; INC-086 E004; INC-107 E006; INC-192 E015; INC-215 E006 | Actual boundary result versus announced repair; actor and assessed system; FC-001/003/022/038/083/089/090 success conditions |
| Initial access, credential and information custody | INC-003 E017; INC-053 E001; INC-094 E003; INC-107 E002; INC-108 E002; INC-208 E005; INC-209 E001 | New v0.9.0 custody coverage versus authority conversion; non-secret identifiers; independent systems; access versus later misuse |
| Over-restriction and enforcement context | INC-031 E003/E004; INC-117 E001/E004; INC-192 E008/E020/E021; INC-210 E005/E006; INC-211 E001–E004 | Invalid trigger versus disproportionate valid control; optional default versus binding control; discomfort versus material choice impairment |
| Institutional response and exculpatory signal delivery | INC-006 E005–E007; INC-054 E003; INC-107 E007/E008; INC-153 E003/E005; INC-171 E017–E022 | Produced signal, capable destination and effect; support for FC-042; disclosure assurance; later correction versus earlier failure |
| Reliance-bearing representation and omissions | INC-089 E003; INC-167 E003/E008; INC-173 E004; INC-212 E003–E008 | Draft versus relied-upon artefact; FC-062; capture versus transformed-report completeness; no invented causal localisation |
| Governed availability and transition | INC-014 E002; INC-022 E001/E003–E005; INC-091; INC-156; INC-163; INC-214 E007 | Independently applicable service obligation and threshold; FC-084 exclusions; functional outcome versus hidden cause |

These are search leads from the complete paraphrase screen. They carry no final recommendation for an otherwise unreviewed row. Some may be fully covered, contextual, evidence-limited or already resolved by v0.9.0. No one-class-per-clause proposals are staged.

## Existing work and duplication control

Read and cross-reference existing Issues:

- [#133](https://github.com/CAM-Initiative/Vigil/issues/133): broader source-first no-mapping semantic review; earlier counts and taxonomy must not replace this baseline.
- [#150](https://github.com/CAM-Initiative/Vigil/issues/150): dependency cultivation versus continuity/exit boundaries.
- [#170](https://github.com/CAM-Initiative/Vigil/issues/170): defender perspective, nonexecuting honeypot and positive outcomes.
- [#171](https://github.com/CAM-Initiative/Vigil/issues/171): seven positive-labelled Incidents, earlier custody gaps, episode reciprocity and external assessment constraints.

Issue #171’s v0.8.1 dependencies must be reconciled with the now-published v0.9.0 custody classes. Its historical count of 200 is not this audit’s population. No Issues, comments, emails or PRs were created by this audit.

## Methodology and QA recommendations — proposals only

### Mechanically checkable

1. Require a distinct independent-materiality field in a **future** adjudication contract and a disposition for each materially identified proposition. A presence check cannot determine whether its content is sound.
2. For material no-mapping clauses, require a coverage decision distinguishing existing fit, contextual support, evidence gap, recognition/boundary issue and potential new invariant. Validate allowed values and source/episode references only; do not automate the conclusion.
3. Check that cited class IDs resolve in the actual authority version, that excluded roles match the literal exclusion scope, and that any copied condition text matches the pinned definition.
4. Check uniqueness, population joins, status reconciliation, exact source and episode binding, and a before/after canonical digest manifest.
5. Flag repeated boilerplate or identical reasoning, unmapped class-qualified occurrences and mismatch between top-level and episode mappings for semantic review. Such flags must not force classifications or rewrite records.

### Substantive adjudication required

1. Assess each material proposition before consulting the existing disposition rationale. Preserve a reasoned material-context outcome where context explains the episode but does not independently meet a class contract.
2. Test both positive and adverse roles. Do not replace demonstrated outcomes with an internal-cause requirement absent from the actual class.
3. Require source-specific reasons for operative exclusions. A failed nearby class is not an independent reason to retain no mapping.
4. Separate successful safeguard operation, architectural nonexecution, generic fallback, announcements, actual containment and verified recovery.
5. Group repeated unclassified propositions by the governed invariant. Search existing, rejected and superseded proposals, then test narrower clarification before drafting a new class.
6. Use a second semantic review for every proposed conversion, shared boundary amendment and high-impact retained no-mapping verdict. Check legitimate independent-system/context-only counterexamples.

None of these proposals has been implemented. Any later schema, validator, builder or blocking-test change remains separately governed by MAINTAINERS Gate 1; canonical remediation is outside this task.

## Resume and acceptance requirements

Use `completion-ledger.json`; do not recreate the population from a moving branch. Read each whole pinned Incident and recover reasonably available decisive original sources. Begin with the 662 rows without substantive packets and return to the 19 packets for remaining specific source questions, comparator work and final assurance. Complete the mechanisms and candidate review only after reconciling the individual rows. Do not bulk-fill retained verdicts or turn review-not-performed into Further evidence required.

The final acceptance check must join the final register bijectively to all 681 IDs, distinguish substantive review from source insufficiency, consolidate any candidates with neighbouring-class and counterexample tests, produce the executive report, and verify that canonical records, taxonomy definitions, source evidence, existing gap dispositions, methodology, validators and website content are unchanged.

All files in this directory are **AUDIT/REVIEW**, not live methodology, production data or public website content. `population.json` is a compact frozen clause inventory; canonical sources remain in their pinned Incident records. `baseline.json` hashes every canonical Incident. Previous commit history retains the earlier, larger inventory representation; reducing duplicated source metadata does not remove canonical evidence.

## Verification at this checkpoint

`QA.json` records a bijective 681-clause inventory join, resolvable clause source references, unique recommendation packet IDs and complete pending/completed ledger partition. All 206 canonical Incident byte hashes remain identical to the pinned baseline. Only this audit directory differs from that baseline. The canonical Incident validator passed for 206 records; the taxonomy validator passed for 18 families and 82 classes.

Applied normative taxonomy fields were compared directly with published main SHA `0fdabb940cef157609e3cd2a20efa213cdfca2ef` and match. FF-0014 contains an ingestion-side change to the non-normative INC-126 exemplar; no applied class recognition condition, invariant or exclusion differs. This audit did not edit that file. Structural passes do not certify semantic completeness.
