# Alignment Taxonomy: dedicated development branch

**Maintainer workflow — 24 October 2026.** The branch is a working lane, not a second published taxonomy. Published authority remains `main`.

## The three work lanes

- **`agent/taxonomy-development`** — only place to originate changes to normative family/class definitions, invariants, recognition conditions, exclusions, class identities, scope, taxonomy schema, and taxonomy release proposals.
- **`agent/incident-ecosystem-ingestion`** — only branch authorised to allocate new Incident IDs.
- **Other working/release branches** — existing Incident adjudication, evidence, harm, external requirements and generated outputs. They consume *published* taxonomy from `main`, not unmerged taxonomy proposals.

The taxonomy branch starts from `main`. A proposed change is reviewed through a **taxonomy-only pull request targeting main**. Do not bring unrelated Incident corpus or SIAI release work onto this branch. Do not copy unmerged taxonomy changes into other branches as an expedient.

## Controlled taxonomy version

Keep `standard.version`, `standard.publication_date`, and `release_history` equal to current published main throughout development. Use **at most one `working_release`** with `base_version` set to main's published version. Revise that single proposal in place; do not accumulate multiple intermediate version bumps on one branch. Apply the one authorised publication bump only via the existing merge/release controls.

Any class/criterion change that affects existing Incident conclusions creates a *reconciliation obligation*, not automatic permission to rewrite them. After the taxonomy PR is approved and merged:
1. Verify actual current `main` and the newly published taxonomy;
2. Synchronize active Incident, ingestion and release branches with that main, without dropping concurrent commits;
3. Re-adjudicate affected Incidents source-first against exact new criteria;
4. Rebuild projections, validate, and merge those branches through their own PRs.

Never globally restamp an Incident's taxonomy version simply because main advanced.

## Branch lifecycle

Do not reset, recreate, force-push or delete the dedicated branch when unmerged work is present. If main advances while taxonomy work is underway, merge or otherwise safely reconcile main into the taxonomy branch while preserving work. Once a taxonomy PR is fully merged and no unmerged work remains, fast-forward the branch to latest main or recreate it from latest main for the next candidate. Do not silently merge to main.

## Changes that are not normative taxonomy revisions

An Incident reconciliation may legitimately update **non-normative `invariant_exemplars`** in an otherwise unchanged family JSON or rebuild generated case-example indexes/publications. These do not alter the governing class invariant or criteria. They are allowed outside the dedicated taxonomy branch only when tied to evidence-grounded, accepted Incident decisions and validated. A family change to *any other field* is a taxonomy-source amendment and belongs on the taxonomy branch.

Taxonomy tools and the publication schema are also maintained in the taxonomy lane. The dedicated-branch CI distinguishes true normative family changes from strictly case-exemplar changes; it does not claim an exemplar is factually accurate.

## Existing in-flight SIAI release

`chore/siai-2026-release-readiness-20261023` continues its existing source-first taxonomy v0.8.0 Incident reconciliation against **published** criteria. Keep its working packets and Incident changes intact. Any new G01 or other normative-class amendment goes on the taxonomy branch, is reviewed there, and must merge into main *before* the release branch re-synchronizes and re-adjudicates affected records. No silent copy, premature version increase, broad reclassification or SIAI merge is authorised by this setup.

**Order of authority:** taxonomy proposal branch → approved main taxonomy → Incident branch sync and source-first reconciliation → release branch validation → approved main dataset release.
