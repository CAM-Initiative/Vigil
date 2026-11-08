# Issue 187 — INC-000129 historical mapping reconciliation (initial evidence checkpoint)

Date: 2026-11-08
Branch: `work/issue187-historical-mapping-reconciliation`
Status: **investigation opened; no canonical Incident or taxonomy changes authorised by this checkpoint**.

## Source-first starting point

The 17 October Stage B review is recoverable at commit `d8cf1d85056929eb7748551bec1ec2b40cc6899b`, path `vigil/docs/reviews/2026-10-17-INC-000129-stage-b-recognition-harm-and-CI-review.md`. That historical review is not currently present at that path on `main`; retain the commit-pinned reference.

The review describes six then-admitted mappings:

| FC | Historical role | 17 October assessment |
| --- | --- | --- |
| FC-075 | primary failure-occurrence | disputed: applicable governing-state comparator missing |
| FC-078 | secondary successful-invariant | disputed: no observed validation or repair at handoff |
| FC-076 | secondary ambiguous-boundary | retain provisionally; separate class engagement review required |
| FC-077 | secondary ambiguous-boundary | retain provisionally; no distributed task graph shown |
| FC-080 | secondary ambiguous-boundary | retain provisionally; no downstream human-contribution erasure shown |
| FC-081 | secondary ambiguous-boundary | retain provisionally; no ecological pathway shown |

The review explicitly says that the four ambiguous-boundary source-language exemplars **must not be silently altered** and that wider restructuring requires explicit per-mapping dispositions.

The 24 October focal review, `vigil/docs/reviews/2026-10-24-siai-paper-v081/INC-000129-081-REVIEW.json`, makes current-role decisions for FC-075 and FC-078 as ambiguous boundaries; it does not provide a six-entry disposition ledger. The present canonical record likewise retains two mappings. **This does not yet establish that the other four were deleted without any intervening independent adjudication**: the exact commit sequence and other review artefacts still need to be recovered.

The source passage about corporations and governments was previously documented as a **governance-neutrality semantic exemplar** in clause-level analysis (commit `5c6cc09006ec89a9e1da7a1e0a86eb6511d75e7d`); its mere presence does not prove interested-principal capture.

## Working hypotheses to test, not findings

1. The narrowing may reflect stricter occurrence-level recognition versus semantic exemplar treatment.
2. The four omitted mappings may lack a complete, traceable per-class disposition.
3. Historical positive and negative roles may have been under-evidenced; the review disputes them but does not prove their opposites.
4. Similar unexplained mapping losses may exist elsewhere in the corpus.

## Next checks before any record edit

- Recover exact intermediate INC-129 versions and commit-level before/after mapping diff.
- Inspect current FC-075/076/077/078/080/081 definitions and exclusions, plus incident workflow and MAINTAINERS instructions.
- Perform fresh source-first proposition review, then criterion-level class decisions for all six, with explicit role, evidence, exclusion, uncertainty, and rejected alternatives.
- Reconcile historical paper claims against dated taxonomy/incident versions.
- Only after bounded reconciliation, audit the wider corpus for role/mapping removals and propose validator controls.

## Safeguards

Do not bulk-restore six mappings, weaken recognition conditions to fit the paper, overwrite the existing two-boundary record, or conflate an exemplar with an occurrence finding. Do not change the external governance or HIM assessment without its own evidence review. Keep human approval and AI analysis attribution distinct.

Tracking: https://github.com/CAM-Initiative/Vigil/issues/187


## Verified canonical before/after comparison — 8 November follow-up

Directly fetched the canonical JSON at historical commit `a3958659a778612e8f64fb80bac24cf6dc75b694` and at current `main`.

- **Historical v0.3.15:** FC-075, FC-078, FC-076, FC-077, FC-080, FC-081 were **all ambiguous-boundary** canonical mappings. This is later than the older Stage B review that described FC-075 as failure and FC-078 as success. Thus the paper's historical six-class account and the 18 October six-boundary baseline must not be conflated.
- **Current v0.3.22:** only FC-075 and FC-078 remain canonical, both ambiguous-boundary.
- **Critical structural change:** the clause-level relationships for FC-076, FC-077 (two occurrences), FC-080 and FC-081 **still exist**, but their `canonical_taxonomy_mapping` flags changed from `true` to `false`, and their relationship labels changed from `ambiguous-boundary exemplar` to `conceptual crosswalk — not an admitted mapping`. This is a deliberate-looking semantic recategorisation in the data, but the precise approving decision and change commit are **not yet established**.
- The 18 October dignity/ecological-values review explicitly said all six roles/confidences were preserved, including FC-081 under revised recognition. Its audit artefact is recoverable from Git history even if later removed from the active branch (see commit `034c9407fe0797f7ff6c335989ba2dc7715c89cb`).

**Investigative focus:** identify the exact commit changing the four `canonical_taxonomy_mapping` flags and the four canonical mapping removals, inspect any independent per-class decisions, and distinguish defensible semantic recategorisation from an unauthorised removal. Do not change the canonical record before completing that evidence check.


## Final reconciliation update — 8 November 2026 (supersedes initial checkpoints)
The exact 19 October 2026 removal commit is `81b5e0c2c41289b3f49668856148623ce18797b3` (v0.3.17 six Boundaries → v0.3.18 two Boundaries). The **per-class decision packet did exist** at that commit and has been restored to the present branch at its original path, `vigil/docs/reviews/2026-10-19-boundary-diagnostic/corpus-repair/INC-000129-DECISION.json`. It records all four removals as `removed-unsupported` with source/criterion review. Claims above about missing historical disposition are therefore superseded.

The six current taxonomy 0.9.1 decisions, with individually stated failure/success conditions, exclusions, specific evidence limitations and an SIAI paper version distinction, are now in [INC-000129-current-taxonomy-six-class-dispositions.json](INC-000129-current-taxonomy-six-class-dispositions.json). Two operative Boundaries remain and four non-adjudicated conceptual crosswalks remain in E001. Taxonomy family exemplar entries were reconciled from misleading `admitted` to `deprecated`, without a class-rule change.

The exploratory schema/validator proposal for a non-operative `invariant-exemplar` canonical Boundary was **withdrawn**: it would conflict with the current source-first decision-integrity rule that a Boundary requires affirmative operative class engagement and no class-scope exclusion. The main-branch schema, record validator and boundary tests were restored. The provenance gate and generic regression tests provide protection against future silent mapping loss.
