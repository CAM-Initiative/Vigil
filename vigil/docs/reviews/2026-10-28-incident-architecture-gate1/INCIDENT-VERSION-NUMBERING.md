# Proposed Incident version numbering — explicit Gate 1 contract

**28 October 2026 — proposal, not an approved validator/release rule.**

**Issues:** [#175](https://github.com/CAM-Initiative/Vigil/issues/175) (primary), [#168](https://github.com/CAM-Initiative/Vigil/issues/168), [#176](https://github.com/CAM-Initiative/Vigil/issues/176); coordinated [#133](https://github.com/CAM-Initiative/Vigil/issues/133).  
**Source baseline:** `main` at `0fdabb940cef157609e3cd2a20efa213cdfca2ef`; ingestion branch `agent/incident-ecosystem-ingestion` at `0f008d983da72db962705fb9c732496e703cdb5e`.  
**Canonical version field:** existing `record_identity.version`, independently scoped to **one Incident ID**, not to the taxonomy dataset or entire corpus.

## Why the earlier patch-only proposal is insufficient

The original Gate 1 draft proposed one `patch` bump for *every* substantive changed Incident and deferred semantics for `major` and `minor`. That controlled commit frequency but did **not** say what `MAJOR.MINOR.PATCH` means. It could also conceal significant new outcomes as minor editorial updates. **This proposal replaces that candidate with explicit per-Incident change levels and one highest applicable increment on the final main publication.** The automated version check is mechanical; the substantive choice of level must be explained in a reviewable per-Incident change declaration.

## Proposed semantics — one Incident, one edition lineage

| Level | Precise reason | Sample from an existing `1.4.11` record | Gate |
| --- | --- | --- | --- |
| `MAJOR` | Materially incompatible reinterpretation of the **same Incident's identity or bounded subject**: assessed system, actor/system perspective, occurrence boundary or case identity changes so previously published uses might refer to a different occurrence. **Normally prefer a separate new Incident ID** rather than redefining an old one. | `1.4.11 → 2.0.0` | Explicit human approval of retained identity and meaning, plus usual substantive approval |
| `MINOR` | New or changed **substantive evidentiary or adjudicative content**, while the bounded Incident stays the same: new materially distinct episode; changed central event finding or supported chronology; addition/removal/polarity change of an FC mapping; new/withdrawn taxonomy gap; material success, Boundary or confidence reassessment; independent HIM dimension/severity change; independently justified EXTREQ aligned/not-aligned/Boundary change. | `1.4.11 → 1.5.0` | Ordinary applicable source-first adjudication and Gate 2 where needed |
| `PATCH` | Non-substantive **record maintenance** that does not change supported occurrence facts, applicable governance properties or admitted outcomes: corrected typo or source URL, faithful readability wording, missing non-decisive metadata, provenance/history representation migration, approved review-challenge **workflow marker only**, clarification of an existing rationale that preserves its substance. | `1.4.11 → 1.4.12` | Appropriate reviewed content change; schema/validator controls independently gated |
| `NONE` | No canonical Incident bytes beyond excluded bookkeeping changed: temporary audit packets, issue/PR discussions, changed website source, generated public indexes, taxonomy criterion updates without an actual Incident edit, or idempotent rebuild. | remains `1.4.11` | No Incident version increment |

### Necessary classification distinctions

- **Evidence addition without new findings:** adding a supplementary source or repairing its provenance may be `PATCH` only if the record's substantive supported occurrence content and conclusions do not change. If that source establishes a new material episode, reverses a previous claim or changes a class/harm/EXTREQ outcome, it is `MINOR`.
- **Re-adjudication:** adding/removing a supported FC, reversing success/failure, changing real Boundary disposition or resolving a material taxonomy gap is `MINOR`, whether the record's previous top-level classification label changes or not. Reasoning text alone is not automatically `PATCH` if it materially changes the supported meaning.
- **Review-challenge marker:** adding the approved orthogonal “prior no-mapping under review” marker, **without** changing the admitted adjudication itself, is `PATCH`; the eventual substantive mapping correction is separately a `MINOR`. A temporary GitHub/audit-only marker with no canonical record change is `NONE`.
- **Storage migration:** compacting obsolete historical review objects under a genuinely lossless, Gate-1/2-approved schema would be `PATCH`, not a new substantive Incident finding. If any evidentiary content changes, it cannot be labelled mere storage migration.
- **Major should be exceptional:** if the actual governed occurrence has changed to a separate case, allocate a new Incident ID with an appropriate relationship instead of repurposing the prior ID. Never silently produce `MAJOR` just because a global schema version changed.
- **Taxonomy evolution:** `taxonomy_classification.taxonomy_version` documents the actual recognition criteria applied. The Incident's `record_identity.version` tracks that one case's revisions. A newly published taxonomy edition does not bump untouched Incidents.

## Examples using real observed version lines (examples are not authorised edits)

| Starting version and reason | Next **published** version |
| --- | --- |
| INC001 on main `1.4.11`: typo/source URL correction, same occurrence and mapping | `1.4.12` |
| INC001 on main `1.4.11`: newly substantiated FC mapping or change in Harm Impact | `1.5.0` |
| INC001 on main `1.4.11`: identity/scope fundamentally redefined, exceptional approved retention of same ID | `2.0.0` |
| INC034 on ingestion baseline `1.1.23`: approved *provenance-only* compaction after verifying published-main baseline | major/minor remain `1.1`; increment the **published main** patch (not blindly `1.1.24` if main differs) |
| INC145 on ingestion baseline `0.1.16`: existing-class adjudication materially changes | compute from **published main** `0.M+1.0`; e.g. `0.1.16 → 0.2.0` only if main also publishes `0.1.16` |
| INC145 on ingestion baseline `0.1.16`: approved review marker with classification untouched | `0.1.17` if main also publishes `0.1.16` |
| Two major/minor/patch-type changes to same Incident in **one final main PR** | **one highest level** (major wins over minor; minor over patch), not one increment per clause/commit |
| Three work PRs merged to ingestion, then one final ingestion→main PR touching the same Incident | one final increment relative to main; preserve all intermediate source-first decisions in Git history/review metadata |
| A new approved Incident ID not present on main, created with the existing template | first version **`0.1.0`** (not `0.1.1` just because it was edited three times before its first publication) |
| Taxonomy v0.9.0→v0.10.0 with no Incident source change | **no Incident bump** |

**First publication and historical transition:** The existing template uses `0.1.0` and the ingestion branch contains new records at that value. Preserve this initial release value **prospectively**; a leading `0` must *not* be interpreted as “not published” or “not classified”—`record_state`, classification fields and actual published-main presence govern those claims. Many historic Incidents already have `0.x.y` and `1.x.y` versions, including documented intermediate increments on ingestion. **Do not reset/downgrade them mechanically to `0.1.0` during transition.** For already-staged unpublished new Incidents with larger historically assigned versions, obtain an exact per-record reconciliation/exception rather than deleting prior revision history. A future change to make first publication `1.0.0` would be a *separate* prospective version-policy decision, not part of this Gate 1 rollout.

## Calculation — no hidden counter or global numbering

For an existing published Incident, parse `record_identity.version = MAJOR.MINOR.PATCH` from **current published main**.

```text
NEXT(base, MAJOR) = (major+1).0.0
NEXT(base, MINOR) = major.(minor+1).0
NEXT(base, PATCH) = major.minor.(patch+1)
NEXT(base, NONE)  = base
```

For multiple kinds of edits in one publication, select the **highest required level once**. Incidents have separate sequences; e.g. revising INC034 and INC145 in the same PR increments each independently, with different old/new numbers.

**Version is not the commit count.** A commit, PR, branch update or review packet does not itself create an Incident release. The **final successful integration into `main`** is the publication boundary for changed Incidents; the candidate stamped before merge is not published until it lands there. The published version is supported by a generated release manifest containing the exact canonical content digest and source commit. The published manifest and generated index writes must not alter `record_identity.version` after merge.

## Reconciliation with the existing ingestion branch

The branch `agent/incident-ecosystem-ingestion` is the established authoring source. It can carry version values already incremented through historic work. For example, INC001 at verified main commit `0fdabb940cef157609e3cd2a20efa213cdfca2ef` has `1.4.11`, while the ingestion commit `0f008d983da72db962705fb9c732496e703cdb5e` has `1.4.12`. That is **not yet a new published-main version** merely because it exists on ingestion.

At final integration:
1. Pin **fresh main** and both the source-content and existing version for each changed Incident.
2. Compare the complete ingestion change against **main's last published canonical payload** and assemble the source-first decision manifest, including intermediate review history; do not merely increment ingestion's value, or trust its earlier patch as semantically sufficient.
3. Select one highest justified level; prepare the corresponding next published version from **main**.
4. If this differs from an ingestion working stamp, preserve those earlier review/revision references in PR/Git provenance; never erase accepted substantive reasoning or claim old working numbers were published.
5. A later published-main change to the same Incident before merge **invalidates** the planned candidate until the content/diff is independently reconciled and the number recalculated. An unchanged branch need not increment merely for a rebase.
6. New previously-unpublished Incident IDs have no main baseline and require initial-publication treatment, not `next(main version)`.

## Gate 1 enforcement proposal (not implemented)

**Declarative per-PR change manifest, for each changed Incident:** `incident_id`, `published_main_base_sha`, `previous_published_version` (or `absent` for new), `proposed_change_level`, `material_change_basis`, `relevant_field_paths`, `candidate_version`, `updated_date_basis`, and a bounded source/provenance preservation reference.

- Authors/reviewers decide **what changed and its semantic level**. Code can detect actual changed payload, ensure one level was declared, check numeric arithmetic, baseline hashes, per-record uniqueness, manifest and generated-index parity. Code **cannot prove** from JSON syntax that an evidentiary change is substantive or that a human has approved a major redefinition. Humans/AI adjudicators must perform source-first review and governance approvals where specified.
- Reject a missing/incorrect numeric bump, arbitrary patch for an explicitly substantive mapping delta, gratuitous bump for unchanged record, omitted changed Incident, duplicate ID, mismatched authoring/version origin, or stale same-ID main baseline. Report the exact record and fields.
- **Current versus proposed:** today a correctly shaped record can pass while its `record_identity.version` is unchanged despite substantive edits; after this approved contract, the final-main integration PR would fail until a correct candidate is declared and prepared. Conversely, a working ingestion branch with unincremented interim versions must remain admissible until final-main publication, avoiding a false failure of ongoing authoring.
- Changes to `record_identity.updated` are **not by themselves** evidence of semantic change. Retain the actual justified record update date and store the **publication date separately** in the manifest. Never silently backdate review chronology or change all `updated` dates to the CI runner date.
- Avoid a self-referential manifest: identify a stable canonical source-input commit/content digest rather than the generated bot commit itself; check idempotent regeneration.
- The **exact** post-approval validator/programme/website enforcement design must disclose its cross-branch publication scope, pass/fail delta, impact and potential data loss before implementation; Gate 2 separately approves any corpus changes.

## Explicit maintainer decisions

1. **Approve change-level semantics?** Major = rare identity/boundary incompatibility; minor = substantive evidence/adjudication; patch = non-substantive record maintenance; none = no canonical modification.
2. **Approve prospectively keeping `0.1.0` as initial published new-Incident version?** Preserve existing legacy lines and reconcile already-staged exceptions; do not reset corpus versions.
3. **Approve one highest-level increment per Incident per final main publication, not per intermediate ingestion commit?**
4. **Approve a per-Incident change-level declaration and deterministic numeric/main-freshness CI checks**, with source-first review required to validate the declaration's meaning?
5. **Approve treating historical ingestion-stamped versions as unpublished working history if not yet on main**, preserving Git/review evidence when computing publication candidates from fresh main?

**STOP:** this is a written proposal only. No schema, validator, builder, CI, canonical Incident or published-version edit may follow until the user approves the semantic contract under `vigil/MAINTAINERS.md` Gate 1. A later Gate 2 is required before broad record repair.
