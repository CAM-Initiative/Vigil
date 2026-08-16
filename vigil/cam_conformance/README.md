# CAM Applicability and Conformance Assessments — Layer 2

This directory is VIGIL **Layer 2**. It is deliberately separate from:

- **Layer 0** (`vigil/external_sources/`): external-source identity, lifecycle and source-change workflow; and
- **Layer 1** (`vigil/external_requirements/`): source-scope classification and requirement-level analytical reference data.

Layer 2 is the only external-requirements layer permitted to record a substantive judgement about whether an external requirement applies to the CAM corpus and what the current CAM coverage disposition is.

## Boundary

The data flow is one-way:

`Layer 0 source -> Layer 1 EXTREQ -> Layer 2 applicability/coverage assessment -> VIGIL routing/repair`

Layer 2 MUST NOT mutate Layer 0 or Layer 1, manufacture missing external requirements, or convert a source-level `alignment_relationship` into a claim that CAM currently complies, conforms or aligns.

A Layer 2 assessment must point to an existing effective `EXTREQ-*` record and preserve its source/version, normative-force and permitted claim vocabulary. Applicability, coverage and evidence are then assessed independently against a specific CAM corpus commit.

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

`full` is a substantive evidence-backed assessment, not a synonym for textual similarity or presence of a related instrument.

## Provenance and assurance

Layer 2 analytical assessments inherit VIGIL's default AI-authored, semi-autonomous provenance unless an explicit record-level authorship override is present.

Post-production human review or verification is recorded in `assurance_provenance`. Assurance does **not** rewrite AI authorship. Repository acceptance, publication, contract approval, or human presence does not imply substantive review or verification.

## Current state

`assessments.json` is intentionally empty at introduction. This architecture creates a truthful place for CAM applicability and conformance work without retroactively asserting that any current EXTREQ applies to, is satisfied by, or is implemented in CAM.

## Validation

```bash
python vigil/scripts/validate-cam-conformance.py
python vigil/tests/test_cam_conformance.py
```

The validator checks Layer 2 against `vigil/external_requirements/effective-requirements.json` and rejects source/version or semantics drift, unsupported `full` coverage claims, invalid not-applicable/unresolved state combinations, and malformed assurance provenance.
