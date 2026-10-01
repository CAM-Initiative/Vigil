# Ordered architecture refactor — 1 October 2026

Baseline: `f0984da0cc916a6763b7d69f694427009ba8dce7`, integration branch `work/integrate-external-requirements-001-179`.

## Stage 1 — complete

All 76 selectable classes now distinguish a neutral definition and invariant from explicit success and failure occurrence conditions. Each has individually authored success recognition addressing a relevant context, positively observed property holding, and evidence adequate to that bounded outcome. Existing failure recognition moved intact to `failure_recognition`; schema version is 0.4.0. Families retain their neutral domains and separately scoped diagnostic failure boundaries; class-specific success admission does not need a duplicated family structure.

The acceptance inventory verifies that all pre-existing class fields, immutable IDs/codes/names, family membership, invariants, exclusions, boundaries, aliases, examples and references are unchanged. No boundary defect was silently repaired. Publication renderers expose both conditions and recognition structures. Isolated tests establish that neither missing polarity evidence, failed success recognition nor exclusion from failure establishes the other polarity. Evidence-admission helpers require complete condition evidence sets; citations still require substantive adjudication by their caller.

## Stage 2 — structural teardown implemented; corpus adoption pending

Retired the global Incident × EXTREQ candidate CSV, summary, builder and matrix-specific tests. Current maintenance instructions use the disposable one-clause resolver. Dated historical audits retain their historical matrix references. Harm Impact Matrix terminology is unaffected.

The resolver reads only supported reviewed direct/strong-supporting relationships and resolving EXTREQs. An unresolved clause, contextual reference or unreviewed relationship produces no candidate. No Cartesian product or persistent candidate dataset is created.

Independent occurrence assessment validation owns requirement identity, applicability, independent findings, resolving source evidence and optional clause-scoped reviewed derivation. Independently identified requirements no longer need an FC mapping. Requirement findings use `met`, `not-met`, `evidence-insufficient` and `not-assessable`; taxonomy polarity is not a compliance vocabulary. Applicability retains applicable, insufficient-evidence and not-applicable.

Retired the rule requiring local successful or ambiguous relationships to be globally classified and pre-admitted as textbook exemplars. Local evidentiary polarity, whole-Incident completeness and exemplar publication are independent decisions. Removed substantive external-assessment payloads from the navigation index; counts and search terms route readers to canonical records. Regenerated the indexes using the builder. Thin cross-dataset integrity validates endpoints without adjudicating meaning.

The replacement occurrence checks currently report 1,288 diagnostics across 111 Incidents. These are explicit reconciliation work, not proof that underlying facts or prior applicability decisions are false. The complete diagnostics are recorded here. **The full Incident validator is not green.** Canonical Incident records have not been rewritten to satisfy new machinery before the ordered standards audit. No existing sources, factual narratives, harm findings, taxonomy roles, applicability bases or historical provenance were deleted.

## Stage 3 — in progress, not complete

The audit inventories all 1,099 canonical EXTREQs and all 139 FC references with hashes and explicit pending/unresolved states. Structural source, requirement, metadata and fidelity validators pass. That result is not a fresh source-fidelity assurance or reverse semantic coverage review.

A primary-text pilot reviewed eight cited provisions from official NIST AI RMF 1.0 and NIST AI 600-1 PDFs, assessing 12 existing FC references. Four are strong supporting constituent relationships; eight are contextual. None expresses a whole direct invariant. The audit records exact supported components, scope differences and downloaded primary-copy hashes. Existing reference notes are not treated as authority for their strength. The results remain review material; active relationships have not been rebuilt before completion of the ordered audit. The empty relationship registry therefore expresses pending review, not absence of correspondence.

Fresh substantive access to the registered licensed IEEE editions is unavailable in this session. The official IEEE GET route returned HTTP 418 and the IEEE 7014.1 publisher page HTTP 403; no substantive exact-edition copy was available for comparison. Existing recorded licensed-access provenance is preserved and not represented as fresh access. Publisher metadata, summaries and search results are not substituted for primary clauses. Canada and IEEE 7003 remain not-started; the EU AI Act and C2PA remain partial.

Continuation: the official January 2023 NIST AI RMF 1.0 PDF was compared against all 71 existing Core records. Corrected 39 summaries that omitted scope, qualifications or operational conditions, or added unsupported duties. All original IDs are preserved. Missing MANAGE 4.3 now has two independently assessable records: incident/error communication and following/documenting tracking, response and recovery processes. The bounded Core now represents all 72 subcategories with 73 records. Part 1 framing, category headings, function narrative, Profiles, appendices and the companion Playbook are excluded from this control extraction. The corpus contains 1,099 records.

The dated `nist-ai-rmf-integrity-review.json` records every comparison, before/after wording, exact source identity and primary-copy hash. It does not certify per-record atomicity, all applicability fields or reverse coverage. NIST AI RMF fidelity is therefore **provisional**, with effective extraction **partial**, replacing the earlier sample-based assurance. Bounded Core coverage remains complete; that coverage is distinct from fidelity assurance. Existing provenance and human-review status are preserved. No FC mappings or Incident records were changed.

`primary-access-review.json` records fresh access triage for the source and reference URLs, separating downloaded-but-unverified content, abstracts, short responses and access challenges. Exact-version substantive authority remains unresolved wherever it has not been inspected. In particular, the 2026 consolidated EU text returned an empty challenge response, and the IMDA page supplied identity/date without the framework body. These transport results do not erase earlier recorded primary-access provenance.

Preliminary reverse-coverage issues from the RMF comparison include organization-level resource allocation, workforce diversity and proficiency, representative human-subject evaluation, fairness/bias evaluation and environmental-impact assessment. Operational evidence, oversight and safe exit may support constituent taxonomy properties, but do not establish coverage of those broader institutional or impact outcomes. These are review questions, not confirmed missing classes; the full reverse review remains pending. No class creation or boundary change follows from this observation.

Next: obtain lawful substantive exact-edition primary text for inaccessible sources, complete the per-requirement primary comparison and all-reference review, classify reverse coverage and gaps, and then rebuild supported relationships. The inventories explicitly remain unresolved until that work occurs; they do not assert completed substantive review merely because every ID is listed.

## Stage 4 — not started

The full review of 170 current Incidents and 536 material clauses is held behind Stage 3 as instructed. The assessment diagnostics identify the structural work to combine with independent actor/system/time/jurisdiction/force and evidence review. Do not mechanically copy taxonomy findings into requirement findings, erase prior scope decisions, or manufacture positive criterion evidence to clear those diagnostics.

## Validation

This continuation also passes 10 targeted source, requirement, generated-output, metadata, fidelity, referential-integrity and historical-seeder checks, recorded in `stage3-validation-results.json`. The historical metadata seeder retains its original population; it does not infer field assurance for the two new records.

23 targeted schema, publication, referential-integrity, provenance and retained-subsystem checks pass; exact results are recorded in `validation-results.json`. The full Incident and occurrence-assessment gates remain failing as explicitly recorded above. No successful broad corpus validation is claimed.

## Supporting artefact classification

LIVE: taxonomy families/schema, domain validators and evidence-admission/resolver code, empty reviewed-relationship registry, current maintenance instructions.

GENERATED: public Incident index and registry manifest, built from canonical records. Publication HTML was rendered for verification; the maintained PDF remains a main-branch release workflow output.

REVIEW: polarity acceptance inventory, external/reference review queues, assessment diagnostics and this status record. These are bounded audit/review inventories, not authoritative candidate datasets.

RETIRE: global candidate matrix, candidate summary, builder and matrix-specific tests. Historical provenance remains available in Git and dated audit documents.
