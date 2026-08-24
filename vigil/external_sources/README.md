# External Governance Sources

This directory is VIGIL's canonical registry of external governance source identity, version, lifecycle, publisher metadata, durable public knowledge and source-review workflow state. It is not a VIGIL evidentiary record class and it does not create CAM authority.

VIGIL's source identification, abstraction, classification and maintenance content is AI-authored and semi-autonomous under human contract approval unless an explicit provenance override says otherwise. External laws, standards and publications retain their own authorship and authority. See `../provenance/AUTHORSHIP-PROVENANCE.json`.

## Boundary

The governance flow is:

`external source -> external requirement -> CAM applicability/coverage assessment -> VIGIL routing/repair`

Source registration records what an external instrument is, its bounded relevance to AI governance and whether it has changed. It MUST NOT determine whether the source applies to CAM, manufacture an external requirement, create a CAM coverage finding, or create a substantive VIGIL repair record automatically.

## Public knowledge and internal curation

`public_summary`, `ai_governance_relevance`, `applicable_lifecycle_stages`, `relevance_scope` and `last_substantive_reviewed` are the canonical public source-knowledge fields. `notes` remains optional internal curation and provenance metadata; it is not a public description and must not be used as one.

Public source knowledge fields SHALL be written as durable governance knowledge for an external reader who has no access to the authoring conversation, repository work plan, migration context, maintenance workflow or agent handoff. Internal curation, review tasking, reconciliation, branch, validator and workflow language SHALL NOT appear in public narrative fields.

The controlled theme and lifecycle vocabularies are shared with `../external_requirements/external-requirement.schema.json`. A public summary may describe only what the available official source text, official metadata, official abstract or other authoritative publisher material supports. It must not reconstruct inaccessible clauses or imply legal applicability.

## Substantive review freshness

Every review-eligible source requires a `last_substantive_reviewed` date. A source becomes review-due when its substantive assessment is more than 90 days old. Source polling, metadata refresh, unchanged-source checks, file modification and schema migration do not reset that date.

A substantive review checks source/version currency, newer or consolidated text, changed AI-governance relevance, relevant authoritative guidance, the public summary, thematic classification, lifecycle applicability, relevance scope and material applicability qualifications. A material metadata change reopens `review_state`; it does not silently claim that the substantive review was completed.

## Source authority

The canonical authority for legal or standards status is the official publisher, regulator or legislature. Third-party trackers may be used only for discovery.

`review_state` is VIGIL source-review workflow state. It is not a CAM applicability, conformance or coverage finding.

## Stable identity and metadata fingerprint

Each source/version has an internal `vigil_source_id` plus a publisher-native `canonical_identifier`. The durable source key is `external_source_id + source_version`.

`source_metadata_fingerprint` is a SHA-256 of VIGIL's material source-metadata projection. It supports deterministic source/version change detection. It is **not** a digest of a reviewed PDF, HTML capture, licensed standard file or other primary artefact.

Exact reviewed-source artefact digests belong in `../external_requirements/source-review-assurance.json`. Historical reviewed artefacts for which no digest was recorded remain `not-recorded`; VIGIL does not manufacture retrospective digests.

## Files

- `source-matrix.json` — publisher/source families, authority posture, lifecycle mappings and retrieval readiness.
- `source-registry.schema.json` — canonical source-registry contract.
- `source-registry.json` — maintained current source/version registry.
- `source-review-queue.json` — generated source-review queue.
- `SOURCE-CATALOGUE.md` — generated human-readable current source catalogue.
- `../scripts/manage-external-sources.py` — deterministic source registry maintenance and generation.

## Commands

```bash
python vigil/scripts/manage-external-sources.py build
python vigil/scripts/manage-external-sources.py validate --check-generated
```

For normalized observations from an official-source adapter:

```bash
python vigil/scripts/manage-external-sources.py ingest --source <source-id> --input /path/to/items.json
```

Semantic external-requirement extraction belongs under `../external_requirements/`. CAM applicability and coverage assessment belongs under `../cam_assessment/`.
