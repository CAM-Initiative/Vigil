# SIAI 2026 dataset release preflight — Gates 1 and 2

**Branch:** chore/siai-2026-release-readiness-20261023
**Original Gate 2 control snapshot:** f031c4421f772e1af5b945bc388363aa81e1a179 (historical, superseded for release after reconciliation)
**Publication source:** the exact future validated merged `main` commit, determined after PR integration; do not assign it in advance
**Dataset candidate:** VIGIL Observatory v1.0.0 (not published)
**Current Alignment Taxonomy:** v0.8.0, 17 families, 80 classes
**Canonical Incident count:** 200

The manuscript's central records must retain their exact identity and version lineage:

| Incident | Canonical record | Recorded taxonomy |
|---|---|---|
| INC-000003 | 0.8.13 | 0.8.0 |
| INC-000129 | 0.3.19 | 0.6.11 (later boundary criteria separately recorded) |
| INC-000117 | 0.1.21 | 0.6.9 |

**Build:** python vigil/releases/siai-2026/build_research_snapshot.py --write

**Verify:** python vigil/releases/siai-2026/build_research_snapshot.py --check

The preflight CI exports a per-file SHA-256 manifest from **the checkout HEAD** as a workflow artifact. After reconciliation and merge, rerun on `main` with `--require-main` and use **that new SHA and checksum** for the v1.0.0 tag and citation. It does not modify the scientific payload or commit an automatically generated PR head. A checksum of the release manifest cannot include the manifest itself; the eventual signed-off Git tag/archive is a separate Gate 3 verification.

## Approval boundary

- Gates 1–2: prepare docs, inventory scientific bytes, validate current state, make an auditable draft PR.
- Gate 3: separate human decision on final citations, licence/deposit conditions, repository merge, v1.0.0 tag and public Zenodo release.
- Do not assert that structural validation certifies source fidelity, human independent coding or inter-rater agreement.

The source baseline may continue to contain recorded unknowns and versioned historical adjudications. These must remain visible and faithfully represented in the camera-ready paper rather than mechanically rewritten.

## Gate 2 verified results — 23 October 2026

**Historical Gate 2 baseline verification only**, before the CAM-subsystem retirement and planned incident reconciliation; not the eventual publication fingerprint. Source commit f031c4421f772e1af5b945bc388363aa81e1a179:

- 200 canonical Incident JSON records and 735 source-record entries; these are not 735 independently authenticated underlying sources.
- 1,185 research files individually SHA-256 hashed.
- Aggregate inventory SHA-256: 7da6b83b0f1e049c8b2e688a523f38190674c8dd8b938794e336f70eeded9d7f.
- Source taxonomy v0.8.0, 17 Fidelity Families and 80 selectable Fidelity Classes.
- 333 regression tests and all additional taxonomy, rights, Incident, evidence/provenance, authorship, external requirement, CAM assessment, jurisdiction and publication checks passed.
- Preflight workflow: https://github.com/CAM-Initiative/Vigil/actions/runs/39965642552
- Standard VIGIL records workflow: https://github.com/CAM-Initiative/Vigil/actions/runs/39965642434
- Downloadable preflight manifest artifact ID 12506304488; Actions retains artifacts 30 days, while the pinned Git source and manifest generator remain reproducible.

Recorded taxonomy versions across Incident records: 0.6.9 (31), 0.6.10 (3), 0.6.11 (139), 0.7.0 (13), 0.8.0 (14). Record classification statuses: 139 classified, 37 unclassified, 19 provisionally classified, 3 requiring human review, and 2 disputed. These reflect preserved canonical statuses; they are not findings of independent factual validation.

Remaining stops are the rights-holder's release and Zenodo licence decision, actual citation-version/date update at publication, archive inspection and camera-ready paper work. No public release, tag or DOI was created.

## Gate 2 amendment — maintainer direction, 23 October 2026

The release branch is now an **editable pre-merge reconciliation branch**. Its previous immutable research hash was a valid dated control snapshot, but is not the future released corpus. CAM institutional assessment scaffolding has been retired on this branch. Reconciliation may change canonical Incident records only with evidence-bounded, version-preserving adjudications and full rebuild validation. Do not merge or tag before this pass is completed and reviewed.

Publication sequence: finish working branch -> rebuild derived outputs -> pass all CI -> merge branch to main on approval -> inspect actual main commit and rerun SHA-256 manifest builder with --require-main -> update CFF with actual version/date and licence approval -> create the approved v1.0.0 tag/GitHub Release -> verify Zenodo metadata/DOI. If updating CFF changes the tagged tree, the final checksum must be regenerated on the final tree before tagging. Recheck that a main CI publisher has not advanced main with its own generated-output commit before the freeze.
