# VIGIL Observatory — scholarly release readiness

**Status: PREPARATION ONLY. No approved v1.0.0 GitHub tag, GitHub Release, Zenodo deposit or certified corpus.**
**Reviewed:** 25 October 2026 (post-merge release-preparation checkpoint; not a publication approval).
**Historical Gate 2 control source:** f031c4421f772e1af5b945bc388363aa81e1a179. This is NOT the final release source. Final snapshot must be rebuilt after reconciliation and merge to main.

## Historical baseline — original 23 October Gate 2 control (not current release state)

- PR #140 was merged 21 October 2026 and published the Alignment Taxonomy v0.8.0 with 17 families and 80 selectable Fidelity Classes.
- PR #141 completed selective repository housekeeping, preserving retired audit history in Git.
- PR #155 was merged 23 October 2026 and placed 200 canonical Incident records in main alongside the revised geography-v2 projection.
- Current example record versions: INC-000003 v0.8.13, INC-000129 v0.3.19 and INC-000117 v0.1.21. Their recorded taxonomy editions are v0.8.0, v0.6.11 and v0.6.9 respectively. Do not rewrite historical decisions to the latest taxonomy without new adjudication.
- Outstanding evidentiary and methodological follow-ups in GitHub Issues remain legitimate unresolved work. Green CI and AI-authored reviews do not establish independent source authentication, inter-rater reliability or complete external validation.

## Research release candidate

The intended candidate is **VIGIL Observatory dataset v1.0.0**, distinct from the independently published **Alignment Taxonomy v0.8.1**. The original 23 October main commit was a valid control snapshot, not the final proposed release commit; a new manifest must be generated from the merged main commit after reconciliation. No release is created merely by preparing a manifest.

PR #162 has merged. Any further Incident changes require their own authorised workflow; the five deferred promotions are not being applied for v1.0.0. No migration by changing taxonomy version strings is permitted. Canonical records, derived projections and documentation must agree at the final release commit.

The preflight generator under vigil/releases/siai-2026/ builds a deterministic per-file Git-object and SHA-256 inventory of the **current checkout commit**. Once merged, run on main with `--require-main`; only that result can support a main-based release. Its CI workflow provides an artifact, not a published deposit. README, provisional citation metadata and release paperwork are deliberately outside the scientific digest to avoid self-reference. A future approved tag and source archive still require separate inspection.

## Post-merge release position — 25 October 2026

- PR [#162](https://github.com/CAM-Initiative/Vigil/pull/162) **merged into `main` on 25 October 2026** (merge commit `034c9407fe0797f7ff6c335989ba2dc7715c89cb`); subsequent automated taxonomy-publication commits have advanced `main`. The exact final v1.0.0 release commit is **not frozen**.
- The documented v0.8.1 reconciliation checkpoint contains **200 active canonical Incident records**, with **164 stamped taxonomy v0.8.1** and **36 retaining historical editions**. All counts must be reconfirmed from the final scientific manifest. The release does **not** imply independently human-certified classifications.
- Five deferred focused promotions (INC-034/062/101/145/195) are assigned to GitHub Issues, **not required for the v1.0.0 release**. The obsolete one-time `apply_approved_five.py` operator script is to be retired as release preparation, without running it. INC-118 retains its evidence hold.
- Release blockers are the **main-based scientific preflight and full validation**, corrected metadata, verified licence/deposit settings, third-party material review, and explicit maintainer/rights-holder publication approval.
- [Zenodo deposit packet](vigil/releases/siai-2026/ZENODO-DEPOSIT-PACKET.md) is a proposed publication handoff only. No DOI, tag or release has been assigned or approved.


## Gate 1 — document and rights reconciliation

- [x] Reconcile stale 194-record and draft-PR-140 claims with the merged 200-Incident corpus and taxonomy v0.8.0.
- [x] Preserve existing rights and licensing files without changing their proprietary permissions.
- [x] Separate the dataset v1.0.0 candidate from the independently governed taxonomy edition.
- [x] Release-preparation CFF identifies candidate dataset v1.0.0 and its custom licence URL. The historical 0.1.0 / 2026-06-01 fields were retired; actual publication date and DOI remain unset until release approval. Recheck the exact tagged-main snapshot after the final date is recorded.
- [ ] Rights-holder to confirm the **manual dataset deposit** (preferred unless custom terms are demonstrably preserved), file visibility and the custom VIGIL Observatory Proprietary Licence. Public inspectability is not CC BY or an open-source licence.
- [ ] Verify publication pages, reviewer requests and Springer CCIS/LNCS template outside repository release scope.

## Gate 2 — freeze and reproducibility checks

- [x] Generate and inspect the **original control** preflight manifest for the exact pinned source commit. It records all in-scope file sizes, Git blob identifiers and SHA-256 digests, plus a deterministic aggregate inventory SHA-256.
- [x] Confirm **original control** held 200 incident records, 17 taxonomy families, 80 classes and taxonomy version 0.8.0 at the frozen source commit.
- [x] Run the complete record/test/rights/provenance/taxonomy/external-requirement checks **for the original control snapshot** and record actual pass/fail/skipped outcomes for the branch.
- [x] Verify original snapshot generated indexes and publication projections are consistent with canonical source.
- [ ] Confirm release files, source access, third-party material rights and any unverified evidence limitations are accurately described.

## Gate 3 — intentionally withheld

After final-HEAD validation and metadata approval: record the actual release date in `CITATION.cff`, identify the final main source commit, run `build_research_snapshot.py --write --require-main` and `--check --require-main`, inspect the actual deposit archive and verify its **separate** checksum. Do not treat the workflow's temporary preflight artifact as a deposited dataset. The GitHub source archive may contain files outside the scientific manifest scope: disclose this distinction or deposit a rights-reviewed scientific-scope bundle.


After explicit maintainer release sign-off: finalise the CFF release date, approve proprietary Zenodo configuration, create immutable dataset tag/GitHub Release, inspect the actual downloadable archive, and verify Zenodo's licence, file visibility, files, checksums and version DOI. If automatic GitHub–Zenodo integration cannot preserve the rights terms, do not use its default publication settings.

## Limitations for SIAI

The corpus is principally AI-assisted and human-governed, not demonstrably double-blind independently coded. Different Incident records may preserve different adjudication-era taxonomy versions. This release will be a traceable snapshot with bounded source evidence, not proof of universal taxonomy completeness, absence of all classification errors, legal compliance, or deployed runtime-control effectiveness.

## Gate 2 validation checkpoint (23 October 2026)

All technical preflight checks passed: 200 canonical records, 1,185 individually SHA-256-hashed source files, 735 source-record entries, 333 regression tests and full validation. Aggregate checksum: 7da6b83b0f1e049c8b2e688a523f38190674c8dd8b938794e336f70eeded9d7f. See https://github.com/CAM-Initiative/Vigil/actions/runs/39965642552 and the dedicated release-gates record. This does not clear independent-review, rights-holder or Zenodo publication gates.

## Working-branch reconciliation and post-merge publication controls

The reconciled release branch was merged as PR #162. The older checksum above is historical evidence only. The final publication manifest and release content must be rebuilt from the same approved main commit, after CI settles and after any final citation changes. The unused CAM institutional applicability/coverage assessment dataset, dedicated validator and tests have been removed from the working branch; no EXTREQ registry or occurrence-level compliance reasoning is being retired.

See `vigil/releases/siai-2026/TAXONOMY-080-RECONCILIATION.md` for the evidence, review and decision requirements. Do not infer an automatic taxonomy migration or assert that every Incident is fully adjudicated simply because it has been screened.
