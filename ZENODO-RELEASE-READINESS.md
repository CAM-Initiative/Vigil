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

## Curated corpus and historical-review retirement

**Research-release curation is selective, not archival maximalism.** The active repository is not a complete institutional work log. On 19 October, a second aggressive housekeeping tranche retires **1098 tracked historical files**, following the earlier bounded deletion of 13 superseded materials. The number and precise list are reproducible from the draft cleanup PR and its pinned parent snapshots. The staging tree is still **NOT approved as paper-ready**.

Retired surfaces in this tranche:
- all legacy `vigil/docs/audits/` material (419 files), covering prior model-generated corpus claims, intermediate source and taxonomy audits, migration/reconciliation reports, and duplicated snapshots;
- most `vigil/docs/reviews/` material (666 files), including earlier model-era corpus campaigns, dated handoffs, unadopted proposals and obsolete issue/checkpoint inventories;
- historical completed migration scripts and unadopted taxonomy/HIM proposals (13 files).

These deletions are **not findings that every earlier audit was factually wrong**. They mean those earlier artefacts do not meet the acceptance bar to participate in the current citable research record. Their original content and commit history remain recoverable from `290b8d82c5e238e8ccdea82aa018e491e6d229fb` and its ancestors, but are not treated as validated methodological evidence.

Retained selected recent packets under `vigil/docs/reviews/` include the bounded HIM 1.1.0 completion and corpus-count report, adopted animal-welfare method amendment, source/requirement explanation repair reviews, recent admission/record-completion decisions, selected governance-class admissions and approved validator-scope evidence. These are **traceability records, not proof of independent human validation**. Ten additional older source-linked snapshots are deliberately retained because nine current canonical `review_reference` fields point to exact older HIM reconsideration manifests and one existing regression test reads a dated environment audit. They are **legacy reference evidence, not accepted contemporary independent review**. The final Boundary adjudication PR #140 must produce a fresh explicitly approved evidence/methodological packet for the paper.

**Functional preservation rule:** retain the canonical Incidents, their versioned taxonomy/HIM/EXTREQ contracts and source references, public generated data, active builders, validators, tests, rights, citation and normative maintenance instructions. The cleanup must not alter their bytes or claim successful substantive re-adjudication from green CI.

**Review-document acceptance rule:** retain a working audit only when it is current, tied to a specific still-applicable accepted decision or methodological change, references verifiable inputs, and cannot be replaced by canonical records plus exact Git history. Interesting future possibilities are not sufficient reason to keep old review debris. **Prospective changes, unapproved Gate 1/2 proposals, extraction gaps and work queues are GitHub Issues, not dataset artefacts.** Their original drafts can be recovered through Git history; an issue is a task tracker and does not confer substantive approval. Current transferred decisions are issues #142–#146. Draft and rejected proposals do not sit beside the released study.

The release archive is a **selected versioned research artefact, not a reproducibility certificate for historical model-written decisions**. Journal methods must say what was independently checked, by whom, and what remains evidence-limited. An old snapshot's validator-success report does not establish original-source authentication, construct validity, inter-rater agreement or reviewer independence.

## Crucial licensing and access gate

VIGIL’s current `LICENSE.md` and `RIGHTS.json` assert **proprietary / all-rights-reserved** materials. Zenodo’s deposit interface can default to **CC BY 4.0** unless a deliberate, valid licence choice is made, and its GitHub connector resolves licence metadata from `.zenodo.json`, then `CITATION.cff`, then the GitHub repository, then a default.

**Do not publish a GitHub release through Zenodo on the assumption that the presence of `LICENSE.md` automatically preserves the proprietary terms.** The existing `CITATION.cff` does not specify a Zenodo-recognised licence. Confirm the licence and any access conditions with the human rights-holder and verify the actual previewed deposit metadata before publication. Do not insert an invented SPDX licence, imply CC BY / open source, or claim this cleanup permits reuse.

Zenodo supports custom licences through its deposit interface, but the GitHub-integration compatibility of a custom proprietary licence must be confirmed before relying on an automatic release. If the automatic integration cannot faithfully express the rights, use an appropriately configured manual Zenodo deposit or resolve the metadata first.

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
