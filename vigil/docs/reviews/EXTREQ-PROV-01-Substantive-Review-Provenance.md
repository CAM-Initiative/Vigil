# EXTREQ-PROV-01 — Substantive-Review Provenance Transmutation

## Purpose

This migration corrects missing provenance metadata in the external-governance dataset. It does not change source meaning, extracted requirement meaning, normative force, source authority, access status, extraction scope or human-assurance status.

The August 2026 EXTREQ programme recorded review dates and source-specific access and scope boundaries, but did not preserve the specific AI model responsible for the substantive analytical review. Contemporaneous programme evidence establishes the reviewing system as OpenAI ChatGPT using GPT-5.6 Sol.

## Canonical representation

`vigil/external_sources/source-registry.json` owns a chronological `substantive_review_provenance.review_events` history for each source version. Each event records the reviewing provider, platform and model; AI role; generation mode; access and scope method; bounded review scope; human role; and human review and verification states. Source-specific access, inaccessible material and extraction limitations remain canonical in `vigil/external_requirements/source-scope.json` and are referenced rather than duplicated.

The current review event is projected deterministically into source review queues, public source catalogues and source coverage manifests. The next substantive-review date is derived as exactly 90 calendar days after the event date; metadata refreshes do not reset that clock.

## Migration boundary

The migration covers the 81 source versions substantively reassessed in the August 2026 EXTREQ/EXTSRC programme. It records 99 review events: 18 structured requirement-extraction events dated 15–16 August 2026 and 81 public-governance-knowledge reviews dated 24 August 2026. All 99 events use the historically established `OpenAI / ChatGPT / GPT-5.6 Sol` identity. The migration script does not infer that identity for unrelated records or future reviews.

## Human assurance boundary

AI substantive-review provenance is distinct from authorship provenance and post-production human assurance. The migrated events retain the historical posture: human role `contract-approver`, substantive review `not-reviewed`, and independent source verification `not-verified`. `vigil/external_requirements/source-review-assurance.json` remains the canonical sidecar for separately evidenced human assurance and reviewed-source artefact digests; it is not used to store AI analytical-review provenance.

Future substantive review events must record model identity contemporaneously. Unknown identity must be represented explicitly where permitted by the applicable schema and must never be silently inferred from unrelated repository activity.

## Migration audit

- Working branch: `agent/failure-taxonomy-prototype`
- Remote head before bounded reconciliation: `dc447fb18c821f4a376042f21f9119025d283157`
- Authorized EXTSRC source-data commit copied from `main`: `9fcaf0e498ca5f7ea0db7c925da4f9c10a4a6891` (locally replayed without conflict)
- Source versions inspected and migrated: 81
- Review events: 99 (10 on 15 August, 8 on 16 August and 81 on 24 August 2026)
- Access methods across events: 43 official-metadata-only, 38 direct-public-primary and 18 direct-licensed-primary
- Current next substantive-review date: 22 November 2026 for all 81 source versions
- Human substantive-review or verification claims added: 0
- Records requiring unknown model attribution: 0 within the bounded migration set
- Canonical substantive source fields changed: 0; comparison after excluding the new provenance object is byte-equivalent to the pre-migration registry

Schema and tooling changes upgrade the source registry to `1.2`, require structured event provenance for review-eligible sources, preserve provenance during metadata ingestion, validate method/access/scope consistency, and project the current event into generated coverage and public review outputs. The coverage manifest schema is upgraded to `1.1`. The repository authorship declaration now explicitly separates authorship, AI substantive review and post-production human assurance.

Validation completed on 25 August 2026:

- 132 repository tests passed.
- External-source validation and deterministic generated-output checks passed for 81 source versions.
- External-requirement validation and deterministic generated-output checks passed for 81 source versions and 845 requirements.
- Authorship provenance, VIGIL source provenance and CAM-assessment validation passed.
- Python bytecode compilation and `git diff --check` passed.
- Repository-wide record validation retained the pre-existing unresolved research-to-PROP/PATCH errors and unrelated record-link warnings; this migration introduced no VIGIL record changes.
