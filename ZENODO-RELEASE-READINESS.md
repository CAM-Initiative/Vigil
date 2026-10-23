# VIGIL Observatory — scholarly release readiness

**Status: PREPARATION ONLY. No approved v1.0.0 GitHub tag, GitHub Release, Zenodo deposit or certified corpus.**
**Reviewed:** 23 October 2026.
**Immutable research baseline:** f031c4421f772e1af5b945bc388363aa81e1a179 (main, merged PR #155).

## Current baseline (not inferred from the earlier checklist)

- PR #140 was merged 21 October 2026 and published the Alignment Taxonomy v0.8.0 with 17 families and 80 selectable Fidelity Classes.
- PR #141 completed selective repository housekeeping, preserving retired audit history in Git.
- PR #155 was merged 23 October 2026 and placed 200 canonical Incident records in main alongside the revised geography-v2 projection.
- Current example record versions: INC-000003 v0.8.13, INC-000129 v0.3.19 and INC-000117 v0.1.21. Their recorded taxonomy editions are v0.8.0, v0.6.11 and v0.6.9 respectively. Do not rewrite historical decisions to the latest taxonomy without new adjudication.
- Outstanding evidentiary and methodological follow-ups in GitHub Issues remain legitimate unresolved work. Green CI and AI-authored reviews do not establish independent source authentication, inter-rater reliability or complete external validation.

## Research release candidate

The intended candidate is **VIGIL Observatory dataset v1.0.0**, not an automatic upgrade of the distinct Alignment Taxonomy from its published v0.8.0. The fixed 23 October main commit is the source baseline for a reproducibility preflight; no release is created merely by preparing a manifest.

The SIAI preparation branch may update publication documentation and release scaffolding. Canonical incidents, their provenance, taxonomy families/index, harm methodology, external governance, CAM assessments, source registries, schema, public projections, active validators, test fixtures and substantive review history must remain unchanged from the pinned scientific baseline.

The preflight generator under vigil/releases/siai-2026/ builds a deterministic per-file Git-object and SHA-256 inventory. Its CI workflow provides a manifest artifact, not a published deposit. README, provisional citation metadata and release paperwork are deliberately outside the scientific digest to avoid self-reference. A future approved tag and source archive still require separate inspection.

## Gate 1 — document and rights reconciliation

- [x] Reconcile stale 194-record and draft-PR-140 claims with the merged 200-Incident corpus and taxonomy v0.8.0.
- [x] Preserve existing rights and licensing files without changing their proprietary permissions.
- [x] Separate the dataset v1.0.0 candidate from the independently governed taxonomy edition.
- [ ] Root CITATION.cff still identifies historical version 0.1.0 / released 2026-06-01. Update version/date only when an actual publication is approved. Do not fabricate a DOI.
- [ ] Rights-holder to confirm Zenodo access and licence metadata. Public inspectability is not a CC BY / open-source licence.
- [ ] Verify publication pages, reviewer requests and Springer CCIS/LNCS template outside repository release scope.

## Gate 2 — freeze and reproducibility checks

- [x] Generate and inspect the CI-exported preflight manifest for the exact pinned source commit. It records all in-scope file sizes, Git blob identifiers and SHA-256 digests, plus a deterministic aggregate inventory SHA-256.
- [x] Confirm 200 incident records, 17 taxonomy families, 80 classes and taxonomy version 0.8.0 at the frozen source commit.
- [x] Run the complete record/test/rights/provenance/taxonomy/external-requirement checks and record actual pass/fail/skipped outcomes for the branch.
- [x] Verify generated indexes and publication projections are consistent with canonical source.
- [ ] Confirm release files, source access, third-party material rights and any unverified evidence limitations are accurately described.

## Gate 3 — intentionally withheld

After explicit maintainer release sign-off: reconcile CITATION.cff, approve proprietary Zenodo configuration, create immutable dataset tag/GitHub Release, inspect actual downloadable archive, and verify the Zenodo deposit's licence, files, checksums and version DOI. If automatic GitHub–Zenodo integration cannot preserve the rights terms, do not use its default publication settings.

## Limitations for SIAI

The corpus is principally AI-assisted and human-governed, not demonstrably double-blind independently coded. Different Incident records may preserve different adjudication-era taxonomy versions. This release will be a traceable snapshot with bounded source evidence, not proof of universal taxonomy completeness, absence of all classification errors, legal compliance, or deployed runtime-control effectiveness.

## Gate 2 validation checkpoint (23 October 2026)

All technical preflight checks passed: 200 canonical records, 1,185 individually SHA-256-hashed source files, 735 source-record entries, 333 regression tests and full validation. Aggregate checksum: 7da6b83b0f1e049c8b2e688a523f38190674c8dd8b938794e336f70eeded9d7f. See https://github.com/CAM-Initiative/Vigil/actions/runs/39965642552 and the dedicated release-gates record. This does not clear independent-review, rights-holder or Zenodo publication gates.
