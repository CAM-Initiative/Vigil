# VIGIL v0.8.0 — Incident classification reconciliation campaign

> **Historical campaign notice — 25 October 2026.** This file documents the former v0.8.0 reconciliation workflow. The temporary `build_taxonomy_080_worklist.py` generator and its `TAXONOMY-080-WORKLIST.json` CI artifact have been retired by maintainer direction following the move to published taxonomy v0.8.1. Any commands or current-worklist references below are historical and must not be executed as current release gates. The former script is recoverable in [the pre-retirement Git commit](https://github.com/CAM-Initiative/Vigil/blob/02c4acb4c82265a04f8ed3cc029854532075a656/vigil/releases/siai-2026/build_taxonomy_080_worklist.py). Historical Incident adjudication packets and their evidence limits remain available; ordinary canonical and release validation is retained.

**Authority:** maintainer-directed working-branch reconciliation, before merging the SIAI release-readiness branch.
**Working branch:** chore/siai-2026-release-readiness-20261023.
**Starting baseline:** main at f031c4421f772e1af5b945bc388363aa81e1a179; subsequent work recorded explicitly in the branch.
**Taxonomy:** published Alignment Taxonomy v0.8.0 (17 families, 80 selectable Fidelity Classes).
**Release:** VIGIL Observatory dataset v1.0.0 is a candidate. It does not pre-release the taxonomy, preassign a DOI or substitute the unmerged branch for main.

## What must be reconciled

At start: 200 canonical Incidents. Existing classification statuses are 139 classified, 37 unclassified, 19 provisionally-classified, 3 requires-human-review and 2 classification-disputed. Only 14 records currently name v0.8.0 as their recorded taxonomy edition. Older recorded editions are valid adjudication provenance, not proof that a case was not reviewed against later criteria.

For every active Incident, complete a **current-v0.8.0 applicability screen** against the full class catalogue and exclusions. This screen is not a mechanical modification to historical adjudications. For cases in which the screen reveals an applicable new/changed class, unrecognised success, unsupported old mapping, or inadequate explanation, perform a source-grounded case re-adjudication. Preserve historical version lineage and precise per-mapping disposition. Record a current v0.8.0 assessment separately from earlier editions as the schema permits; if schema lacks such versioned-review fields, retain the dated audit packet without inventing unsupported JSON keys or rewriting prior dates.

### Priority order

1. **Paper-focal and high-risk decisions:** INC-003, INC-117 and INC-129 (SIAI paper); human-review INC-196–198; disputed INC-073/129; the remaining provisional cases. This includes the more recent incident intake batch, but a provisional evidence limitation need not become a forced classification.
2. **Unclassified cases:** 37 records. Distinguish genuinely no supported mapping from admissions awaiting evidence or incomplete processing. Complete outstanding intake where source evidence permits.
3. **Legacy-classified cases:** all older editions, by functional class family and known v0.8.0 class changes; start with recently amended classes and the success/boundary polarity controls. Existing mappings have no privileged presumption of correctness.
4. **Already v0.8.0 cases:** verify the current classification was actually based on sufficient evidence and applicable recognition criteria; do not alter merely to change a status label.

Each row in the generated machine-readable worklist is **queued for screening**, not represented as independently checked. The source is the current branch HEAD; regenerate after canonical edits.

## Single-incident decision packet (required for changed interpretations)

- Record identity, baseline SHA/revision, source-access modality, evidence sufficiency, relevant chronology, contested claims and counterevidence.
- All applicable 0.8.0 candidate Fidelity Classes, with exact canonical required conditions and exclusions. Include both success and failure polarity, with Boundary only when the invariant is materially engaged but neither polarity is supported.
- A disposition for **every previous primary and secondary mapping**: retained, role-changed, confidence-changed, role-confidence-changed, superseded, or removed-unsupported. Supply source-grounded reasons for removal and independent reasons for each new mapping.
- Statement of whether old taxonomy edition stays as historical provenance; explicit current review date, ruleset/edition, reviewer provenance and limits.
- Harm Impact and external-requirement assessment: open independently when new evidence demands it, otherwise preserve; absence of taxonomy mapping does not automatically mean no incident severity or compliance issue.
- Deliberate handling of any provisional, disputed or requires-human-review hold. If remaining uncertainty is honest and source-bounded, preserve it rather than generating a false final finding.
- Append interpretive review history without asserting independent human review not performed. Where case-file text changes, keep original evidentiary quotes and chronology. Prevent accidental loss using incident-rebuild guard.

## Execution and merge checkpoints

1. Regenerate the list: python vigil/releases/siai-2026/build_taxonomy_080_worklist.py --write. Confirm by running --check. It is a workflow artifact and not automatic adjudication.
2. Review priority cases and append dated decision packets under vigil/docs/reviews/2026-10-23-taxonomy-080-reconciliation/. Begin with INC-117 and INC-129 (SIAI) and the 24 non-final cases. Search existing decisions and prior reviews; check GitHub Issues only if a **separate practical task** passes the maintainer four-part issue-admission test. Inaccessible vendor internals and contested recognition evidence remain Incident/review-level limits, not issue-register tasks.
3. For each changed canonical record, validate full-rebuild manifest, run record/context/source/interpretive/rights/taxonomy/EXTREQ validators and regenerate public indexes. Commit the complete before/after evidence packet and all downstream projections. Any new class requires a separately governed taxonomy release, not a silent 0.8.0 mutation.
4. Maintain a campaign ledger with one explicit screened/needs-rebuild/blocked/not-yet-reviewed disposition for **all 200 IDs**. A reproducible worklist alone does not satisfy this human-adjudication checkpoint.
5. Do not merge merely because CI is green: reconcile every changed mapping, sign off unresolved evidence holds and confirm SIAI paper-focal conclusions. Recheck website/public schema consumers.
6. After approval merge to main; let generated-output workflows settle. Build the final SHA-256 manifest from **the resulting main HEAD** using --require-main. Apply final citation/version and legal release metadata approval; if that changes main, regenerate the manifest and freeze the final main commit before tagging v1.0.0. Verify archive and Zenodo rights/DOI.

## Evidence and publication warning

Automated screening is a candidate detector, not external verification or a substitute for human authorisation. With the camera-ready submission due 25 October 2026 AoE, a complete externally sourced 200-case re-adjudication might exceed the manuscript window. Preserve a stable, honestly described state rather than rushing disputed/unknown cases into forced outcomes. The paper may accurately discuss the current taxonomy even when some record review statuses remain unresolved; whether the repository release itself waits for completed full screening is a maintainer gate.
