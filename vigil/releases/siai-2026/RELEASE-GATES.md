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
