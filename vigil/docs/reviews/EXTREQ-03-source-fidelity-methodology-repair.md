# EXTREQ-03 — Source-Fidelity Methodology Repair

## Review date

2026-08-26

## Starting point

Working branch: `agent/failure-taxonomy-prototype`

Pre-work head: `bab4fed10405a86d1ea961045524447aefe91125`

The starting external-requirements corpus reported 845 EXTREQ records across 81 registered source versions. Existing generation and validation established schema consistency, provenance and extraction-contract conformance, but did not establish substantive human review or human source verification of every analytical interpretation.

## Defect confirmed

A targeted source-fidelity audit confirmed that the existing extraction contract can admit materially lossy records when a source-native structural container is treated as a semantic atomic unit.

The clearest demonstrated examples are the consolidated EU AI Act Article 10 and Article 13 records, which each compress multiple independently assessable propositions into one article-level EXTREQ summary.

The defect is methodological rather than universal. NIST AI RMF Core subcategory extraction and the sampled CycloneDX ML-BOM propositions retain materially better source-native granularity.

## Step 1 — semantic atomicity contract

Completed.

`vigil/external_governance/requirements/SOURCE-FIDELITY-METHODOLOGY.md` now defines:

- independently assessable proposition as the primary atomicity test;
- source-defined compound actions as a separate case;
- material fidelity dimensions covering actor, modality, action, object, applicability, threshold, timing, qualification, exception, artefact, verification, constituent propositions and locator;
- semantic atomicity states;
- source-level fidelity states;
- identity/migration rules for decomposition; and
- a revised effective-completion rule.

## Step 2 — schema change only where necessary

Completed conservatively.

The canonical EXTREQ schema was not bulk-expanded merely to populate synthetic fidelity metadata across 845 existing records.

Instead, a separate `source-fidelity.schema.json` and `source-fidelity.json` were introduced. This preserves historical extraction/provenance while adding an independently auditable fidelity-assurance layer.

Future source re-extraction may justify constituent-proposition fields in the canonical EXTREQ schema, but that change should accompany real semantic re-extraction rather than metadata backfill.

## Step 3 — fidelity/atomicity validation

Implemented.

`vigil/scripts/validate-external-requirement-fidelity.py` validates:

- source/version integrity of fidelity decisions;
- assured-source completion conditions;
- audited requirement ownership;
- effective downgrade of unassured historical-complete sources; and
- basic integrity of semantic-decomposition stress-test artefacts.

`vigil/scripts/test_external_requirement_fidelity.py` adds regression coverage for the initial fidelity dispositions.

The push surface available during this review did not expose a workflow run for the new commit, so this audit does not falsely claim CI execution. The validator/test files were added for the repository test surface and require normal CI/local execution before merge.

## Step 4 — EU AI Act stress-test re-extraction

Completed as a non-canonical migration prototype.

`vigil/external_governance/requirements/fidelity-stress-tests/EU-AI-ACT-2026-07-27.json` decomposes the current coarse Article 10 and Article 13 records into materially distinguishable propositions and records why the existing records fail the new atomicity test.

No replacement EXTREQ IDs were allocated during the stress test. The coarse identities should only be retired after the full source-level decomposition is reviewed and deterministic replacement identities can be allocated consistently.

The consolidated EU AI Act remains `requires-reextraction` / effectively partial.

## Step 5 — NIST/CycloneDX re-audit

Completed for the representative source types selected in the audit.

### NIST AI RMF 1.0

Fidelity status: `assured`.

The existing Core-subcategory granularity follows a source-defined outcome structure and the audited sample does not justify artificial sentence-level fragmentation.

### NIST AI 600-1

Fidelity status: `provisional` / effectively partial.

Suggested-action identity is useful and should generally remain stable, but sampled actions contain material constituent propositions that need explicit preservation rather than prose compression.

### CycloneDX 1.7 ML-BOM

Fidelity status: `assured`.

The audited records already distinguish materially different recommendation, prohibition/conformance, descriptive and identifier-constraint propositions.

## Step 6 — remaining reviewed sources

A conservative corpus-wide reprocessing rule is now active at the fidelity layer:

> A source carrying historical `extraction_status: complete` but lacking explicit `fidelity_status: assured` is fidelity-unassured and effectively partial for clause-level use.

This prevents later IEEE, NIST, technical-framework and licensed-source extractions from inheriting a high-fidelity claim merely because they passed the older extraction contract.

This step deliberately does **not** pretend that every such source has already been re-read line by line. Instead, all unreviewed historical-complete sources are downgraded at the effective fidelity layer and placed into the reprocessing queue. Source-specific re-extraction can now occur without the catalogue overstating its quality in the meantime.

`SOURCE-FIDELITY-STATUS.md` records the usage boundary and recommended reprocessing order.

## Step 7 — completion-state correction

Completed at the effective-assurance layer without destroying historical extraction state.

Only a source that is both:

1. historically extraction-complete; and
2. explicitly fidelity-assured

may now be treated as effectively complete for clause-level use.

At initial admission, the positively assured sources are:

- NIST AI RMF 1.0; and
- CycloneDX 1.7 ML-BOM.

NIST AI 600-1 is provisional/effectively partial.

The consolidated EU AI Act requires re-extraction/effectively partial.

Every other historical-complete source defaults to fidelity-unassured/effectively partial until a source-specific fidelity review is recorded.

## Downstream usage boundary

Until a source is fidelity-assured:

- its records remain useful for discovery and broad governance analysis;
- absence of a record must not be interpreted as proof that the external source contains no corresponding obligation;
- clause-level compliance/conformance claims should not depend on the corpus alone; and
- requirement-to-failure-taxonomy mapping should use only propositions whose source meaning has been independently checked.

## Remaining work

The next substantive source-repair work is not another methodology exercise. It is controlled source-by-source migration:

1. complete the EU AI Act operator-scope decomposition and identity migration;
2. enrich source-defined compound NIST AI 600-1 actions;
3. apply the fidelity test to historically complete licensed IEEE/control standards in governance-priority order;
4. restore effective `complete` only when each source passes.

The repaired methodology now prevents those migrations from being falsely represented as already complete.
