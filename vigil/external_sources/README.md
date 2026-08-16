# External Governance Source Ledger

This directory is VIGIL **Layer 0**: external-source identity, version, lifecycle and coarse source-change workflow. It is not a VIGIL evidentiary record class and it does not create CAM authority.

VIGIL's source identification, abstraction, classification and maintenance content is AI-authored and semi-autonomous under human contract approval unless an explicit provenance override says otherwise. External laws, standards and publications retain their own authorship and authority. See `../provenance/AUTHORSHIP-PROVENANCE.json`.

Layer 1 under `../external_requirements/` preserves source scope and requirement-level analytical reference data. Layer 2 under `../cam_conformance/` is the separate place for CAM applicability and coverage judgements.

## Boundary

The pipeline is deliberately one-way:

`external source -> Layer 0 source/version -> Layer 1 requirement abstraction -> Layer 2 CAM assessment -> VIGIL routing/repair`

An upstream source change may create or update Layer 0 review state. It MUST NOT directly edit CAM, manufacture a Layer 1 requirement, create a Layer 2 applicability/coverage finding, or create a substantive VIGIL repair record automatically.

## Source authority

The canonical authority for legal or standards status is the official publisher, regulator or legislature. Third-party trackers may be used only for discovery.

Primary source families currently registered include official Australian, EU, UK and US legislative/regulatory sources, ISO/IEC metadata, NIST, IEEE and CEN/CENELEC sources. Discovery services are not authoritative for lifecycle state.

## Lifecycle and workflow state

`source_lifecycle_state` describes the external instrument, for example `draft`, `consultation`, `adopted`, `published`, `effective`, `superseded` or `withdrawn`.

Historical `alignment_state` in Layer 0 is a **coarse VIGIL workflow state** (`unassigned`, `review-required`, `mapped`, `patch-required`, `patched`, `verified`, `no-change-required`, `not-applicable`, `superseded-before-review`). It must not be read as the substantive CAM applicability or conformance finding introduced in Layer 2.

Only configured final/adopted lifecycle states are alignment-eligible. Draft and consultation material may be observed without automatically becoming an internal governance obligation.

## Stable identity

Each source/version has an internal `vigil_source_id` plus a publisher-native `canonical_identifier`. The durable review key is:

`external_source_id + source_version`

Upstream-provider identity is provenance only. Changing discovery providers must not change VIGIL source identity.

## Fingerprint semantics

The Layer 0 historical field `fingerprint` is a SHA-256 of VIGIL's material **source-metadata projection**. It is used for deterministic source/version change detection.

It is **not** a digest of the PDF, HTML capture, licensed standard file or other artefact that was reviewed.

The effective ledger therefore exposes the same value under the explicit name:

`source_metadata_fingerprint`

Exact reviewed-source artefact digests belong to the Layer 1 `source-review-assurance.json` overlay. Historical reviewed artefacts for which no digest was recorded remain `not-recorded`; the repository does not manufacture retrospective source digests.

## Files

- `source-matrix.json` — source families, authority posture, lifecycle mappings and automation readiness.
- `ledger.schema.json` — frozen Layer 0 maintenance-ledger contract.
- `ledger.json` — accepted external-source observations.
- `alignment-queue.json` — generated coarse review queue; not a substantive CAM applicability decision.
- `effective-ledger.json` — generated normalized effective source inventory with explicit metadata-fingerprint semantics.
- `../scripts/manage-external-governance-ledger.py` — deterministic canonicalise/hash/diff/filter/queue engine.
- `../tests/test_external_governance_ledger.py` — lifecycle and transition tests.

## Commands

Validate current files:

```bash
python vigil/scripts/manage-external-governance-ledger.py validate
```

Ingest a normalised JSON array exported from an official-source adapter:

```bash
python vigil/scripts/manage-external-governance-ledger.py ingest \
  --source australia-frl \
  --input /path/to/items.json
```

Regenerate the Layer 0 review queue:

```bash
python vigil/scripts/manage-external-governance-ledger.py queue
```

The normal ingestion path is intentionally model-free:

`fetch -> validate -> canonicalise -> metadata hash -> diff -> lifecycle filter -> queue`

Semantic requirement extraction begins only in Layer 1. CAM applicability and coverage begin only in Layer 2.
