# CAM Applicability and Coverage Assessments

This directory records the separate assessment of whether an external `EXTREQ-*` requirement is applicable to a specific CAM corpus state and what evidence-backed coverage disposition exists.

It is deliberately separate from:

- `vigil/external_sources/` — external-source identity, version, lifecycle and source-review workflow; and
- `vigil/external_requirements/` — external requirement meaning, authority semantics, access and extraction state.

## Boundary

The governance flow is:

`external source -> external requirement -> CAM applicability/coverage assessment -> VIGIL routing/repair`

A CAM assessment MUST NOT mutate external-source facts, manufacture missing external requirements, or convert a source-level `alignment_relationship` into a claim that CAM currently complies, conforms or aligns.

Every assessment must reference an existing canonical `EXTREQ-*` record and a specific CAM corpus commit. Applicability, coverage and evidence are then assessed independently.

## Assessment states

`applicability_state`:

- `applicable`
- `conditionally-applicable`
- `reference-only`
- `not-applicable`
- `unresolved`

`coverage_state`:

- `full`
- `partial`
- `absent`
- `conflicting`
- `indeterminate`
- `not-applicable`

`full` is a substantive evidence-backed assessment, not a synonym for textual similarity or the presence of a related instrument.

## Provenance and assurance

CAM assessments inherit VIGIL's default AI-authored, semi-autonomous provenance unless an explicit record-level authorship override is present.

Post-production human review or verification is recorded in `assurance_provenance`. Assurance does **not** rewrite AI authorship. Repository acceptance, publication, contract approval or human presence does not imply substantive review or verification.

## Current state

`assessments.json` remains intentionally empty until an actual CAM applicability/coverage assessment is performed. The existence of this structure does not retroactively assert that any EXTREQ applies to, is satisfied by, or is implemented in CAM.

## Validation

```bash
python vigil/scripts/validate-cam-assessments.py
python vigil/tests/test_cam_assessments.py
```
