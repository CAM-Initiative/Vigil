# Adjudication correction and root-cause learning

**Status:** Maintainer adjudication process. This governs *how* VIGIL interprets evidence and repairs recurring errors; it is not an additional taxonomy class, automatic scoring rule, external compliance claim, or a repository of case verdicts.

## Principle — method consistency, not decision consistency

Two Incidents should have the same adjudication **only when their relevant evidence and the version-pinned criteria genuinely warrant the same outcome**. A repeated previous VIGIL answer, a comparison packet, an earlier reviewer preference or a majority of other Incident labels is **not** corroborating evidence. We do not store an answer key to make later classifications agree.

The authoritative current result, material negative candidates and evidence limits belong in the canonical Incident. Reusable corrections to the reasoning **method** belong here or in `INCIDENT-ADJUDICATION-WORKFLOW.md`. Temporary analyses belong on the review notice board only until case/method closeout; Git history preserves process chronology.

## Mandatory order for substantive adjudication

1. **Reconstruct the occurrence without using prior VIGIL conclusions as the candidate shortlist.** Inspect sources, attribution/access limitations, actors, chronology, and each material governed episode; identify the governance properties independently. Prior record content may be necessary to locate original sources, but do not treat its mapping labels or former verdict as evidence.
2. **Apply the complete relevant taxonomy edition to that evidence.** Discover plausible classes independent of the original mapping; apply every material literal necessary success/failure condition and exclusion (including missing conditions), separate competing mechanisms, apply distinct positive success tests, preserve alternative outcomes and uncertainty. No missing proprietary telemetry requirement unless the class itself demands it.
3. **Form a provisional evidence-to-criteria conclusion.** Record reasons for supported roles and material non-admissions, with episode/source refs, class edition and counterevidence. If a decisive fact is genuinely unavailable, record that limit; do not invent an outcome or label research as incomplete solely for inaccessible internals.
4. **Only then reconcile with prior VIGIL records, external interpretations and similar cases.** Differences trigger a recheck of sources, scope, exact criteria and abstractions—not automatic correction toward precedent. Preserve supported prior findings, explain actual changes and limit downstream changes to authorised scope.
5. **Promote the accepted result to the Incident.** Source-clause relationships, materially rejected classes, precise missing condition, credible alternatives, harm and external assessments belong in their governed fields. Previous decision details may remain in Git history; a notice-board packet is not part of the published result.

## When a maintainer repeatedly corrects an interpretation

A correction request must generate a **root-cause diagnosis**, not a new "for this Incident choose X" rule.

| Diagnostic family | What to examine |
| --- | --- |
| Existing-answer anchoring or external-authority deference | Was previous or external classification visible *before* independent recognition testing? Was the result copied because it seemed authoritative? |
| Criterion or exclusion misapplication | Was an exact version-specific necessary condition omitted, invented, over-narrowed or inferred from a neighbouring class? Were exclusions tested separately for each role? |
| Source selection, attribution or temporal error | Were sources inaccessible, conflated, incorrectly dated, mistaken for direct observation, or was later remedy used to erase earlier conduct? |
| Success/failure or uncertainty asymmetry | Did the review assume success from absence of failure, failure from harm alone, Boundary from topical similarity, or absence of evidence as evidence of absence? |
| Harm, compliance or scope leakage | Did harm severity, institutional authority, or an external requirement's own finding improperly determine taxonomy membership? |
| Record/workflow/validator defect | Did missing fields, stale criteria, generated outputs, a staging packet or a test make an inappropriate outcome easier to preserve than to correct? |

**Correction sequence:** (a) state the exact erroneous reasoning step and its factual/criterion basis; (b) determine whether it is a local factual misread or a reproducible method defect; (c) change the smallest **general** instruction/validator/test necessary, with maintainer approval for any normative criterion/schema/semantic-gate change; (d) retest the original case **and a materially different counterexample** where the correct result may be different; (e) write any substantively justified canonical Incident correction with preserved versions, source provenance and validations; (f) document in the active PR what changed and whether wider cases actually need a scoped review.

**Anti-overfitting test:** The proposed fix must be expressible without incident IDs, provider names, class-specific outcome commands or a desired polarity. Ask whether the rule would still be correct for a counterexample with the same governance boundary but opposite evidence. If not, it is not a general method fix. A known Incident may be an *illustrative test fixture*, never a permanent mandated classification. Semantic regression tests cannot be replaced by a string check that a particular class remains mapped.

**No artificial answer store:** Do not create persistent case-class concordance tables, case verdict baselines or hidden prompts to enforce repetition. Deterministic tooling checks structural contracts, exact version/source pins, preservation, and missing steps; it **cannot adjudicate semantic truth**. AI agents need source-first reasoning; tests must not fabricate source evidence or substitute validator success for source review.

## Lightweight process record, not a second dataset

During the current PR, capture in its conversation/checklist (and a temporary notice-board packet only if it aids work): correction trigger; diagnosed reasoning mechanism; canonical criteria/version and source refs; method change or explanation why none is warranted; a counterexample or disconfirming test; affected records and validations; evidence holds. Promote the general lesson to this maintenance guidance, the accepted case interpretation to the INC, and retire scratch material on campaign closeout.

A correction that is genuinely a one-off transcription or factual fix can be corrected locally. Do **not** pollute maintenance with a case-specific rule. Routine uncertainty and corrected case judgments do not create GitHub Issues; use issues only for independently actionable scoped work under the existing issue-admission rule.

## Release and notice-board boundary

Complete ongoing v0.8.0 source-first adjudication using its current *temporary* packets; do not delete active worksheets, change canonical outcomes by fiat, or restamp old decisions just because this method was refined. When the campaign closes, the published corpus must stand on Incident records plus governed taxonomy/methods, not on a review-folder answer store. See `REVIEW-RECORD-RETENTION.md` for promotion, reference reconciliation and routine retirement.

## Correction: implementation uncertainty used as an admission barrier

The reasoning defect is substituting a demand for exact platform causation for the class's observable recognition conditions, or treating every hypothetical implementation alternative as an operative exclusion. Correct the abstraction and test the actual evidence. Retain real competing explanations and literal missing criteria. Do not replace over-caution with automatic admission from an adverse outcome. The workflow's observable-findings and effective-human-authority sections give the general method. Recheck a supported observable breach and a materially different case where the decision relationship remains genuinely unresolved; no case label is mandated by this instruction.
