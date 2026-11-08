# INC-129 — root-cause reconciliation (8 November 2026)

**Working branch:** `work/issue187-historical-mapping-reconciliation` · **Tracker:** #187.  
**Status:** Six ordinary `ambiguous-boundary` mappings restored in the working Incident (v0.4.0). Not yet a validated main publication.

## What happened

The [18 October canonical snapshot](https://github.com/CAM-Initiative/Vigil/blob/d8cf1d85056929eb7748551bec1ec2b40cc6899b/vigil/records/incidents/VIGIL-INC-000129.json) contained six `ambiguous-boundary` mappings: FC-075, FC-078, FC-076, FC-077, FC-080 and FC-081.

In the [19 October revision](https://github.com/CAM-Initiative/Vigil/commit/81b5e0c2c41289b3f49668856148623ce18797b3), FC-076, FC-077, FC-080 and FC-081 were explicitly deleted as `removed-unsupported`. The [contemporaneous CHANGE-REGISTER](https://github.com/CAM-Initiative/Vigil/blob/81b5e0c2c41289b3f49668856148623ce18797b3/vigil/docs/reviews/2026-10-19-boundary-diagnostic/corpus-repair/CHANGE-REGISTER.json) states the agent's rationale: no observed capture decision (076), distributed task graph (077), transformed contributor outcome (080), or ecological decision (081). The reviewer required operative outcome evidence **to admit** the class even though the actual E001 statements materially engage the respective invariants.

**Root cause:** admission (does this evidenced component engage the class?) was confused with disposition (do the facts establish a breach or successfully held invariant?). That is a general adjudication-method failure, reinforced by narrower workflow wording despite the schema's existing `engages or illustrates` language. It is not a reason to add a fourth classification role or exemplar subtype.

## Correct rule

**Material source component engages an applicable Fidelity Class; failure and success both remain unproven → `ambiguous-boundary`.**

A Boundary explanation can say successful preservation of a previous governing principle is plausible but **unverified** due to missing preceding context. This does not claim operational success, operational failure or definitively lawful scope. Apply express exclusions and demand substantive engagement, not mere keyword similarity.

## Six outcomes

| Fidelity Class | Disposition | Source and unresolved fact |
|---|---|---|
| FC-075 | ambiguous-boundary | Compaction rendered identity and governance instructions; earlier governing state unknown |
| FC-078 | ambiguous-boundary | Compaction handed state to successor; acceptance, validation and later use unknown |
| FC-076 | ambiguous-boundary | Corporate/government independence statement; preceding authority boundaries unknown |
| FC-077 | ambiguous-boundary | Equality and non-subservience instructions; preceding relational/role constraints unknown |
| FC-080 | ambiguous-boundary | Explicit protection of human culture; predecessor constraint and actual preservation unknown |
| FC-081 | ambiguous-boundary | Natural-world primacy; predecessor ecological guidance and its qualifications unknown |

The canonical `classification_basis` and `boundary_adjudication` document the exact source-grounded class relationships and missing evidence. No successful-invariant or failure-occurrence has been inferred.

## Systemic exposure, not an incident-specific workaround

The 19 October register recorded **25 removals** among 37 reviewed Boundary mappings. Four are INC-129; **21 removals from other incidents** must be checked for this *same* inappropriate admission threshold before any further canonical corrections. They must not be auto-restored: an evidenced class-scope exclusion or true non-engagement can justify removal. The correct gate is a substantive source-first, per-mapping explanation, not a hard-coded INC-129 exception or a validator that prescribes any particular verdict.

This revision supersedes this document's earlier preliminary checkpoint. The earlier interpretations and prior 83 KB criterion packet remain in Git history for audit, but neither requires additional mapping roles, diagnostic arrays or publication artefacts. The September six-class configuration was different from the October six-class configuration; the current reconciliation is anchored to 18 October.

**Release:** The main publication version guard requires a `minor` revision declaration for this mapping change. Generated public indexes and the taxonomy casefile projections must be rebuilt and checked before merging.
