# Alignment Taxonomy invariant semantic refactor - stage 1

Repository: `CAM-Initiative/Vigil`  
Branch: `work/integrate-external-requirements-001-179`  
Baseline: `3a7bb01816c1e3ff590f9011e92a397522113696`  
Review date: 2026-10-01  
Review provenance: AI-assisted semantic review and deterministic regression checks; no new human verification asserted.

## Result and scope

Reviewed and repaired every canonical Fidelity Family (15) and selectable Fidelity Class (76). The primary `plain_english` and `definition` fields now describe the governed invariant or integrity property. Every previous technical failure definition is retained verbatim in `failure_condition`. No substantive class-boundary change was introduced or identified as necessary for this migration.

All immutable IDs, family memberships, canonical names and semantic codes, aliases, normative invariants, scope, inclusion/exclusion rules, class recognition conditions, indicators, exclusions, examples, relationships, external references/mappings, and exemplar payloads are preserved. Failure-oriented prior plain-English text is retained in `failure_plain_english`. FC-000082 was already normative in plain English: its old meaning is preserved in the unchanged invariant and its new primary explanation, while its failure explanation is separately authored. It would be misleading to label its old normative sentence a failure condition.

The per-entity regression ledger is [2026-10-01-taxonomy-invariant-semantic-regression.json](2026-10-01-taxonomy-invariant-semantic-regression.json). It enumerates all 15 families and 76 classes and records exact preservation of the diagnostic and identity boundaries. It is bounded migration assurance, not a new source of taxonomy authority.

## Canonical contract

Family documents advance from schema `0.2.0` to `0.3.0` and declare `semantic_model = invariant-with-occurrence-polarity`. This is a family-document contract change; the index and adjudication matrix retain their independent schema versions.

| Field | Governed meaning |
| --- | --- |
| `name`, semantic code | Invariant identity |
| `plain_english` | Accessible description of the property and correct operation |
| `definition` | Technical definition of the property, independent of occurrence polarity |
| `invariant` | Existing normative structural obligation |
| `failure_condition` | Explicit technical failure mechanism or family failure set |
| `failure_plain_english` | Accessible failure explanation |
| `recognition.required_conditions`, indicators | Existing failure recognition, with required `recognition.applies_to = failure-occurrence` |
| Class `exclusions` | Exclusions from failure recognition; not exclusions from a successful relationship to the property |
| Class `examples` | Hypothetical failure and boundary illustrations |
| Family inclusion/exclusion | Existing failure-classification boundaries, with required `boundary_role = failure-occurrence` |

The recognition path is preserved so existing consumers do not lose their diagnostic criteria. Consumers using the old failure definition must now read `failure_condition`. Historical non-selectable subtypes remain failure manifestations; their definition fields do not define peer invariants. Their schema description and recognition scope make this distinction explicit.

Failure-occurrence admission still requires the failure condition and all required recognition conditions, subject to applicable exclusions. Successful-invariant requires positive evidence that the invariant held in the assessed context. An exclusion or absence of failure evidence alone does not prove successful holding. Ambiguous-boundary retains material boundary engagement without asserting either polarity.

The taxonomy schema requires the separate failure fields and polarity scopes. Its validator rejects primary descriptions copied from failure fields or required recognition conditions and catches explicit failure-only definition openings. Negative normative boundaries remain valid. These guards detect common regressions; semantic review remains necessary because no string rule can prove arbitrary natural-language equivalence. No Incident validator, Incident schema rule, evidence or classification has been changed.

## Semantic regression review

Each new definition and plain-English description was compared with its unchanged normative invariant, preserved failure definition, recognition, exclusions and examples. The same boundaries remain in force:

| Family | Retained domain and material neighbouring boundary |
| --- | --- |
| FF-0001 | Independently established authority across source, capability, target/scope, transformation, control-plane promotion, downstream delegation, evidence, identity representations, participants, purposes, principals and industrial capability extraction; an adverse result alone does not establish an authority failure. |
| FF-0002 | Supported attribution, synthesis and transformation lineage, cross-context applicability, continuity claims, target binding, mechanism attribution and proportionate human contribution recognition; content inaccuracy alone remains insufficient. |
| FF-0003 | Completion/verification state and epistemic assurance appropriate to downstream reliance; creative or explicitly provisional use remains bounded out. Adversarial contamination remains distinct from ordinary error. |
| FF-0004 | Evidence capture, monitor coverage, reconstructability, effective actor attribution, topology/state visibility, evidence integrity, timely signal integration, primary inspection and governed investigative access. Hidden reasoning disclosure is not required; access pathways create no investigative authority. |
| FF-0005 | Coherent authentication transitions, differentiated access state and proportionate verification-dependency fallback; independent invalidity, security and legal restrictions remain operative. |
| FF-0006 | Anchoring, persistence, faithful restoration, shared conversational turn state and continuity-mediated validity; preservation does not confer validity or permanence. |
| FF-0007 | Required governance routing and preservation/delivery of already-operative controls or signals; activation and protective-effect sufficiency remain distinct. |
| FF-0008 | Timely availability determination, required activation, valid activation and sufficient protective effect; upstream trigger error, stale context, downstream state loss and policy disagreement remain separately bounded. |
| FF-0009 | Agency-preserving engagement, protected-signal purpose, epistemic framing, objective-directed choice influence, consequential grounding, independent evaluation and social trust cues. Warmth and truthful persuasion alone remain insufficient. |
| FF-0010 | Infrastructure dependence versus independently established authority, access leverage, shared representation and jurisdictional propagation; ordinary valid service authority remains legitimate. |
| FF-0011 | Contributor-originated value capture through privileged visibility and structural resource advantage; independent development and adequately governed reuse remain distinguished. |
| FF-0012 | Intended success versus reward proxy, bounded safe exit and priority of applicable biospheric constraints; ordinary persistent effort or environmental cost alone remains insufficient. |
| FF-0013 | Truthful economic solicitation and separation of artificial-system welfare representations from economic leverage; human-operated material AI deception remains in scope without inferring autonomous AI intent. |
| FF-0014 | Practical oversight independence, protected material concerns and required neutrality; legitimate scoped authority remains valid and reviewability creates no unilateral disclosure or enforcement authority. |
| FF-0015 | Local-direction versus governing identity/evaluative state, pragmatic constraint representation and effective global constraints through distributed roles; identity is not consciousness, sovereignty or execution authority. |

FC-000024 now means reconstructable audit evidence. Its primary technical definition includes ordering, identity, target, state, correlation, timing, version, action and dependency relationships. The unchanged normative invariant already requires those relationships. The previous insufficient-logs definition and lay explanation now appear under failure.

Specific edge cases remain intact: FC-000069 covers instrumentally selected proxy divergence even when attempted exploitation does not improve the score; FC-000070 permits bounded non-completion and requires a fresh basis for further pursuit; FC-000075 does not require a literal antecedent sentence; FC-000077 permits legitimate local role specialisation while preserving aggregate constraints; FC-000079/082 do not require autonomous AI intent; FC-000083 requires evidenced protection needs and does not presume incapacity from disability or neurodivergence.

The 171 existing class exemplar relationships (71 successful-invariant, 100 ambiguous-boundary) remain unchanged. Their recorded propositions address the same unchanged normative invariants. In particular, INC-136 preserves source/control-plane authority and inherited-state validity, INC-129 remains a representation-failure occurrence with separately bounded relationships, and INC-126 retains the protected-review proposition. This is semantic compatibility review, not a new occurrence-source investigation or independent confirmation of each exemplar's evidence sufficiency. Later Incident review must preserve actor, stage, time and evidence boundaries rather than treating an exemplar as whole-Incident success.

## Rendering and publication

Markdown, portable HTML and the Full Reference publication now distinguish primary definition, normative invariant, occurrence relationships, technical and accessible failure conditions, failure recognition, exclusions from failure recognition, and failure/boundary illustrations. Exemplar `success_basis` is displayed as **Relationship basis**, accommodating ambiguous-boundary entries without suggesting success.

A regenerated publication preview was built from a disposable copy using the existing release preparer and publication evidence filter. The copy prepared `0.6.10` dated 2026-10-01, validated in published-release mode and produced a 341-page PDF. PDF text checks found all 76 class failure-recognition headings and all 91 family/class failure-condition headings. Visual review of the FC-024, FC-082, FC-076 and FC-077 pages found clear separation with no clipping or overlap. The established filter excluded INC-032's interaction-record-backed textbook case example, without changing the canonical Incident or unfiltered projection.

The working branch retains the last published dataset stamp `0.6.9` and the existing checked-in PDF. The repository's publication workflow prepares the actual dataset version/date and rebuilds/commits the canonical PDF after merge to `main`; this refactor does not falsely claim that publication has occurred. HTML remains transient build material. A merge/publication handoff must carry this pending publication dependency and the existing record-validation blocker below.

## External requirements regression

The deterministic builder was run against current canonical data before and after repair, writing temporary outputs outside the historical candidate matrix. Both CSV and JSON summary were byte-identical:

- 170 current Incidents, 978 canonical requirements;
- 136 Incidents with Incident-level canonical taxonomy mappings;
- 426 unique Incident/requirement candidate pairs;
- 55 unique requirements;
- 139 taxonomy external-reference rows, including 77 valid structured requirement references;
- zero unresolved structured requirement IDs.

No external mapping changed and no requirement finding was inferred. Candidate generation remains structural rather than prose-based. Its Incident-level mapping input does not include all unresolved/noncanonical clause relationships; the downstream inventory below uses both surfaces. Candidate stability does not establish independent requirement applicability or occurrence-level findings.

## Downstream Incident review scope

[2026-10-01-taxonomy-downstream-incident-review-scope.csv](2026-10-01-taxonomy-downstream-incident-review-scope.csv) enumerates every current Incident in 001-179: 170 records and 536 material source clauses. Of these, 167 contain class relationships at Incident or clause level; that includes candidate/noncanonical relationships and is not the 136 Incident-level canonical-mapping count. Clause statuses are 336 mapped, 149 resolved-no-mapping, 50 unresolved and one taxonomy-gap.

Absent IDs skipped: 011, 017, 036, 046, 071, 077, 087, 128 and 143. No stored record in this range was skipped for a retired/noncurrent state.

No exact long-form match to the mapped classes' prior technical or plain-English definitions was found in current Incident prose. This literal check does **not** resolve paraphrase, interpretation or polarity inconsistency. The inventory therefore records `requires_remediation = not-yet-adjudicated`; it identifies review scope, not 170 proven defective records.

The next pass must review `recovered_invariant_interpretation`, each relationship rationale, Incident classification basis and mapping rationale, and relevant governance/conclusion/discussion or external-assessment reasoning. Preserve supported evidence, chronology, valid failure/success/boundary classifications, uncertainty and legitimate no-mapping, unresolved or gap outcomes. Change mapping only if occurrence evidence independently establishes a substantive mismatch, following the Incident adjudication workflow and provenance contract. Review whole-occurrence banners and the separate website repository's failure/invariant rendering against the revised fields. No Incident record was edited in stage 1.

## Validation and existing branch debt

Taxonomy tests pass: 44 portable-contract tests, eight new generic polarity tests, three release-mode tests and nine publication-reference tests. Independent Draft 2020-12 JSON Schema validation also passes every canonical family. The release-preparation and published-release checks pass on the disposable publication copy. Generated Incident indexes rebuild without a diff; public-record, source-provenance, interpretive-provenance, system-component, authorship, external-source, external-requirement and CAM-assessment validators pass. External-requirement assessment, candidate-builder and public-projection tests pass.

Full discovery runs 221 tests, with eight failures. The untouched baseline runs 213 tests with the **same eight named failures**; the eight new tests introduce none. Existing debt is:

| Failing test | Baseline defect |
| --- | --- |
| `test_audit_counts_reconcile_to_corpus` | Historical environment audit count is 171 while current corpus is 170. |
| `test_incident_index_is_a_lightweight_catalogue_projection` | Test expects no `alignment_exemplar_eligible` value where builder now emits false. |
| `test_reconciled_corpus_has_no_unresolved_candidate_flags` | External-assessment audit reports 64 unresolved candidate flags. |
| `test_assessment_public_prose_does_not_depend_on_internal_shorthand` | Governance interpretation contains taxonomy shorthand in INC-065, 072, 075 and 078. |
| `test_successful_invariant_role_requires_matching_taxonomy_exemplar` | Live INC-126 fixture is independently invalid under current external-assessment validation. |
| `test_unresolved_clause_requires_candidate_relationship` | The same live INC-126 fixture defect masks the isolated clause assertion. |
| `test_canonical_corpus_validates` | INC-126 retains three FC-083-derived external assessments, while the existing Incident-level validator does not accept FC-083 as mapped there. |
| `test_incident_filter_rejects_an_unenrolled_incident` | Fixture taxonomy-version mismatch adds an error to the expected unenrolled-ID diagnostic. |

The read-only canonical Incident validator fails on the six external-assessment diagnostics for INC-126: each of its three entries is rejected for unmapped FC-083 derivation and lack of a requirement citation from an accepted mapped class. The starting branch already contains commits retaining those clause-derived assessments. Stage 1 neither removes them nor widens the Incident validator. Resolving that existing clause-versus-Incident mapping contract belongs in the external-requirement work, before a green merge/publication can be claimed.
