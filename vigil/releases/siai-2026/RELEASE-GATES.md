# SIAI 2026 dataset release preflight — Gates 1 and 2

**Branch:** chore/siai-2026-release-readiness-20261023
**Pinned scientific source:** f031c4421f772e1af5b945bc388363aa81e1a179
**Dataset candidate:** VIGIL Observatory v1.0.0 (not published)
**Current Alignment Taxonomy:** v0.8.0, 17 families, 80 classes
**Canonical Incident count:** 200

The manuscript's central records must retain their exact identity and version lineage:

| Incident | Canonical record | Recorded taxonomy |
|---|---|---|
| INC-000003 | 0.8.13 | 0.8.0 |
| INC-000129 | 0.3.19 | 0.6.11 (later boundary criteria separately recorded) |
| INC-000117 | 0.1.21 | 0.6.9 |

**Build:** python vigil/releases/siai-2026/build_research_snapshot.py --write --verify-preservation

**Verify:** python vigil/releases/siai-2026/build_research_snapshot.py --check --verify-preservation

The preflight CI exports the full per-file SHA-256 manifest as a downloadable workflow artifact. It does not modify the scientific payload or commit an automatically generated PR head. A checksum of the release manifest cannot include the manifest itself; the eventual signed-off Git tag/archive is a separate Gate 3 verification.

## Approval boundary

- Gates 1–2: prepare docs, inventory scientific bytes, validate current state, make an auditable draft PR.
- Gate 3: separate human decision on final citations, licence/deposit conditions, repository merge, v1.0.0 tag and public Zenodo release.
- Do not assert that structural validation certifies source fidelity, human independent coding or inter-rater agreement.

The source baseline may continue to contain recorded unknowns and versioned historical adjudications. These must remain visible and faithfully represented in the camera-ready paper rather than mechanically rewritten.

## Gate 2 verified results — 23 October 2026

Validated against fixed scientific source commit f031c4421f772e1af5b945bc388363aa81e1a179:

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
