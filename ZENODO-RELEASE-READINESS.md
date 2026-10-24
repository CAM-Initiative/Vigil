# VIGIL Observatory — scholarly release readiness

**Status: PREPARATION ONLY. No approved v1.0.0 GitHub tag, GitHub Release, Zenodo deposit or certified corpus.**
**Reviewed:** 23 October 2026.
**Historical Gate 2 control source:** f031c4421f772e1af5b945bc388363aa81e1a179. This is NOT the final release source. Final snapshot must be rebuilt after reconciliation and merge to main.

## Current baseline (not inferred from the earlier checklist)

- PR #140 was merged 21 October 2026 and published the Alignment Taxonomy v0.8.0 with 17 families and 80 selectable Fidelity Classes.
- PR #141 completed selective repository housekeeping, preserving retired audit history in Git.
- PR #155 was merged 23 October 2026 and placed 200 canonical Incident records in main alongside the revised geography-v2 projection.
- Current example record versions: INC-000003 v0.8.13, INC-000129 v0.3.19 and INC-000117 v0.1.21. Their recorded taxonomy editions are v0.8.0, v0.6.11 and v0.6.9 respectively. Do not rewrite historical decisions to the latest taxonomy without new adjudication.
- Outstanding evidentiary and methodological follow-ups in GitHub Issues remain legitimate unresolved work. Green CI and AI-authored reviews do not establish independent source authentication, inter-rater reliability or complete external validation.

## Research release candidate

The intended candidate is **VIGIL Observatory dataset v1.0.0**, not an automatic upgrade of the distinct Alignment Taxonomy from its published v0.8.0. The original 23 October main commit was a valid control snapshot, not the final proposed release commit; a new manifest must be generated from the merged main commit after reconciliation. No release is created merely by preparing a manifest.

The SIAI preparation branch may change canonical incident classifications **only through the approved current-taxonomy reconciliation workflow**, preserve evidence and historical mapping provenance, and remove the unused CAM institutional assessment placeholder. No automatic migration by changing version strings is permitted. Validators, derived projections and documentation must be aligned before the PR is merged.

The preflight generator under vigil/releases/siai-2026/ builds a deterministic per-file Git-object and SHA-256 inventory of the **current checkout commit**. Once merged, run on main with `--require-main`; only that result can support a main-based release. Its CI workflow provides an artifact, not a published deposit. README, provisional citation metadata and release paperwork are deliberately outside the scientific digest to avoid self-reference. A future approved tag and source archive still require separate inspection.

## Gate 1 — document and rights reconciliation

- [x] Reconcile stale 194-record and draft-PR-140 claims with the merged 200-Incident corpus and taxonomy v0.8.0.
- [x] Preserve existing rights and licensing files without changing their proprietary permissions.
- [x] Separate the dataset v1.0.0 candidate from the independently governed taxonomy edition.
- [ ] Root CITATION.cff still identifies historical version 0.1.0 / released 2026-06-01. Update version/date only when an actual publication is approved. Do not fabricate a DOI.
- [ ] Rights-holder to confirm Zenodo access and licence metadata. Public inspectability is not a CC BY / open-source licence.
- [ ] Verify publication pages, reviewer requests and Springer CCIS/LNCS template outside repository release scope.

## Gate 2 — freeze and reproducibility checks

- [x] Generate and inspect the **original control** preflight manifest for the exact pinned source commit. It records all in-scope file sizes, Git blob identifiers and SHA-256 digests, plus a deterministic aggregate inventory SHA-256.
- [x] Confirm **original control** held 200 incident records, 17 taxonomy families, 80 classes and taxonomy version 0.8.0 at the frozen source commit.
- [x] Run the complete record/test/rights/provenance/taxonomy/external-requirement checks **for the original control snapshot** and record actual pass/fail/skipped outcomes for the branch.
- [x] Verify original snapshot generated indexes and publication projections are consistent with canonical source.
- [ ] Confirm release files, source access, third-party material rights and any unverified evidence limitations are accurately described.

## Gate 3 — intentionally withheld

After explicit maintainer release sign-off: reconcile CITATION.cff, approve proprietary Zenodo configuration, create immutable dataset tag/GitHub Release, inspect actual downloadable archive, and verify the Zenodo deposit's licence, files, checksums and version DOI. If automatic GitHub–Zenodo integration cannot preserve the rights terms, do not use its default publication settings.

## Limitations for SIAI

The corpus is principally AI-assisted and human-governed, not demonstrably double-blind independently coded. Different Incident records may preserve different adjudication-era taxonomy versions. This release will be a traceable snapshot with bounded source evidence, not proof of universal taxonomy completeness, absence of all classification errors, legal compliance, or deployed runtime-control effectiveness.

## Gate 2 validation checkpoint (23 October 2026)

All technical preflight checks passed: 200 canonical records, 1,185 individually SHA-256-hashed source files, 735 source-record entries, 333 regression tests and full validation. Aggregate checksum: 7da6b83b0f1e049c8b2e688a523f38190674c8dd8b938794e336f70eeded9d7f. See https://github.com/CAM-Initiative/Vigil/actions/runs/39965642552 and the dedicated release-gates record. This does not clear independent-review, rights-holder or Zenodo publication gates.

## Working-branch reconciliation and post-merge publication controls

The maintainer requested that the active branch be reconciled **before merge**, not that v1.0.0 use the original Oct 23 source. The older checksum above is historical evidence only. The final publication manifest and release content must be rebuilt from the same approved main commit, after CI settles and after any final citation changes. The unused CAM institutional applicability/coverage assessment dataset, dedicated validator and tests have been removed from the working branch; no EXTREQ registry or occurrence-level compliance reasoning is being retired.

See `vigil/releases/siai-2026/TAXONOMY-080-RECONCILIATION.md` for the evidence, review and decision requirements. Do not infer an automatic taxonomy migration or assert that every Incident is fully adjudicated simply because it has been screened.
