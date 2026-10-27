# Alignment Taxonomy: dedicated development branch

**Maintainer workflow — 24 October 2026.** The branch is a working lane, not a second published taxonomy. Published authority remains `main`.

## The three work lanes

- **`agent/taxonomy-development`** — only place to originate changes to normative family/class definitions, invariants, recognition conditions, exclusions, class identities, scope, taxonomy schema, and taxonomy release proposals.
- **`agent/incident-ecosystem-ingestion`** — only branch authorised to allocate new Incident IDs.
- **Other working/release branches** — existing Incident adjudication, evidence, harm, external requirements and generated outputs. They consume *published* taxonomy from `main`, not unmerged taxonomy proposals.

The taxonomy branch starts from `main`. A proposed change is normally reviewed through a **taxonomy-only pull request targeting main**, subject to an explicit maintainer-authorised integrated evidence scope below. Do not bring unrelated Incident corpus or SIAI release work onto this branch. Do not copy unmerged taxonomy changes into other branches as an expedient.

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

## Integrated standards and taxonomy programme — authorised 27 October 2026

For [issue #171](https://github.com/CAM-Initiative/Vigil/issues/171), the maintainer explicitly requires protected-information and authentication-custody taxonomy development, ISO/NIST source-version registration, external requirement extraction and standards-to-class relationships on **the same `agent/taxonomy-development` branch and in one integrated PR to main**. Standards traceability is part of the taxonomy design. Do not create a separate standards branch or PR for this programme. This bounded exception supersedes the earlier separate-standards proposal and the taxonomy-only wording for this programme; it does not authorise unrelated Incident edits or standards work.

Use the source registry, sharded EXTREQ architecture, source-scope, source-fidelity and existing `external_references` contracts. Keep source-native modality, voluntary normative force, internal conformance conditions and independent legal applicability separate. Metadata-only ISO registration is permitted; unseen licensed provisions and unverified control relationships are not.

Candidate class and family payloads may be retained as REVIEW material without canonical identities while abstraction and boundary approval is pending. Do not add them to selectable family files or allocate their canonical IDs before that review. Supporting requirements whose only defensible relationship is to a proposed class remain review-stage extraction payloads until the approved identity and relationship can resolve through the existing supporting-source gate. Do not weaken the gate or invent an existing-class relationship to bypass this dependency. Promote the approved classes, requirements, metadata review, fidelity evidence and relationships together in this same PR.

The canonical `working_release` is introduced only when approved canonical family/class content changes exist. The existing release validator rejects a candidate release with unchanged canonical content. Before admission, retain the conditional release proposal in the dated review packet; never add a fictitious canonical amendment just to activate a version. Once admission is approved, select at most one working release from published main at the highest required change level. Human approval and the established main-only publication workflow remain required. An ISO access blocker remains explicit until authorised control text and any needed permission are available.
