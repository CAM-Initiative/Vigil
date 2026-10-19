# VIGIL Observatory — research-release readiness

**Status: PREPARATION ONLY. No approved Zenodo deposit or paper-corpus freeze.**  
**Maintained:** 19 October 2026.  
**Starting canonical head:** `290b8d82c5e238e8ccdea82aa018e491e6d229fb` (194 Incident files).

This document distinguishes a scholarly release from ongoing adjudication and internal workflow history. It is not a new source of taxonomy, severity, licence or classification authority.

## What must remain in a citable research snapshot

- `vigil/records/incidents/` — all admitted canonical Incident JSON files, with source identities, uncertainty, adjudication and provenance intact.
- `vigil/VIGIL.Schema.json`, `vigil/VIGIL.Incidents.Index.json`, `vigil/VIGIL.Registry.Index.json` — contracts and reproducible current generated projections.
- `vigil/taxonomy/` — exact adopted taxonomy version, all class/family definitions, recognition criteria, exclusions and reproducible generated publications.
- `vigil/methodologies/` — versioned harm methodology used for each preserved Incident and the interpretation required to read it.
- `vigil/external_governance/`, `vigil/references/` and `vigil/cam_assessment/` — referenced external requirements, source metadata and assessment context.
- `vigil/scripts/`, `vigil/tests/`, `vigil/templates/` and active governance/maintenance instructions — builders, validations and interpretive boundaries needed to interrogate the result.
- `README.md`, `CITATION.cff`, `LICENSE.md`, `RIGHTS.json` and scholarly methodological documentation.
- The **approved final per-mapping adjudication audit**, evidence limitations, review method, and any independent / inter-rater evaluation actually performed. These have not yet been certified complete.

A published `source_records` URL is a citation and evidence locator, **not necessarily an archived copy of third-party material**. Check third-party rights, link stability and preserved source access before the deposit.

## Staging cleanup and preservation

This housekeeping tranche removes only obsolete operational artefacts:

- a superseded HIM 1.0.1 resumption handoff (the substantive corpus audit and methodology remain);
- a 2026-10-02 one-paragraph completion checkpoint (the complete reconciliation report remains);
- five single-use **working** HIM 1.0.1 evidence migration scripts, created for a historical corpus version and not used by the current builders or tests.

All of these remain recoverable from the pinned pre-cleanup Git commit above. Historical audit conclusions must not be silently rewritten simply because a later state supersedes them.

The following categories are deliberately **not bulk-deleted**:

- `vigil/docs/audits/` and substantive `vigil/docs/reviews/` — some are necessary evidence of historical source access, adjudication decisions, preserved counterexamples and version changes;
- open issue / Gate 1 proposals and governance approvals — some still govern authorisation, unresolved evidence and future schema changes;
- current source, references, independent external assessments and generated indexes — publication lineage would be damaged by removing them.

Obsolete website implementation handoffs and open action payloads are separately flagged for review: current audit notes and active review packets refer to them. They should only be retired after pointers are reconciled and their unresolved work is preserved in an authoritative issue or review document.

## Publication gate

1. Finish and approve the source-first Boundary diagnostic audit and mapping dispositions tracked in **draft VIGIL PR #140**. The branch is not yet a fully independently re-adjudicated 194-record research corpus.
2. Verify the exact canonical counts, roles, taxonomy versions, reviewer procedure, remaining evidence limits and provenance at the **final proposed tag commit**, not an older dated inventory.
3. Preserve the approved per-Incident audit packets and any independently assessed inter-rater results actually obtained. **Do not claim inter-rater reliability solely from repeated responses by the same model.**
4. Run the current repository's public/canonical/source/interpretive/authorship/rights, taxonomy, external-requirement and methodology validations, full test suite and generated-output consistency checks on the frozen tree.
5. Review `CITATION.cff` (currently `version: 0.1.0`, `date-released: 2026-06-01`) for the **actual version/tag and authorship before release**. Do not invent a DOI; a new `.zenodo.json` would take precedence over `CITATION.cff` in Zenodo's GitHub integration.
6. Confirm the proprietary `LICENSE.md` and `RIGHTS.json` terms, third-party rights, and selected Zenodo access/licensing metadata reflect the actual release. Public availability does not imply an open-source licence.
7. After maintainer sign-off, create a GitHub release **from the exact approved tag** and only then confirm the Zenodo deposit's version-specific DOI, contents, citation, source-archive behaviour and checksum(s).

### Repository versus GitHub-generated release archive

The repository keeps live governance/CI instructions for maintainers. `.gitattributes` marks CI metadata, the completed one-off migration scripts, and historical website implementation design handoffs as `export-ignore` for Git archive-based **distribution**, while leaving them accessible through normal Git history and branches. It does not remove the source corpus or substantive research audits.

Before deposit, verify the final GitHub release ZIP/TAR and actual Zenodo ingest contain exactly the intended material. A source archive is not automatically proof that all data, source citations, rights and independent adjudication are complete.
