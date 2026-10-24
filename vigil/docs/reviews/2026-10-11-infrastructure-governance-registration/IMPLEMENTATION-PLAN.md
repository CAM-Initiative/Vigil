# Supporting-source implementation and validation plan

Classification: REVIEW. Date: 11 October 2026. Status: **plan only; Gate 1 approval pending**.
Baseline: `f0baf24b3d05a972705995986c82e1b64770ae34`.

## Atomic steps after explicit approval

| Step | Repository surfaces and dependencies | Reviewable outcome / stop |
| --- | --- | --- |
| 1. Freeze and inventory | Source registry, `source-scope.json`, canonical requirement shards and manifests, `taxonomy-relationships.json`; canonical Incidents and taxonomy | Record exact commit, IDs, versions, role/status combinations, review states and counts. Measure eligible/held sources before changing guards. No automatic source promotion. |
| 2. Implement role/status compatibility together | `vigil/scripts/manage-external-requirements.py`: `validate_scope`, `validate_requirements`, status/count checks; `source-scope.schema.json`, `external-requirement.schema.json` only if needed | Reviewed supporting extraction states can pass; supporting-only remains zero-count. Keep primary, context, excluded, inaccessible and review-completeness controls. Do not change unrelated accepted data. |
| 3. Implement bounded fidelity/admission traceability | `SOURCE-FIDELITY-METHODOLOGY.md`, `source-fidelity.schema.json`, `validate-external-requirement-fidelity.py`, `source-fidelity.json`, metadata-review and source-review-assurance contracts | Extracted supporting sources receive substantive fidelity review rather than role-based not-applicable. Reuse review/assurance fields. Determine how manager admission checks resolving review evidence while substantive reviewers establish actual materiality; no rationale-string proxy. If existing structures cannot express the approved decision faithfully, present that precise schema delta before adding fields. |
| 4. Add isolated generic regressions | `vigil/tests/test_external_requirements.py`, `test_external_requirement_metadata.py`, `test_external_requirement_fidelity.py`, `test_external_sources.py` as appropriate | Temporary fixtures covering eligibility and qualifications, no assertions that the live research queue must be admitted. Tests must not encode task completion or rewrite the corpus. |
| 5. Read-only impact run | Managers, fidelity and occurrence/public/provenance validators; existing tests listed below | Compare before/after accepted set and exact failing fields. Stop under Gate 2 for broad semantic repairs. Do not rebuild or edit records to make an altered rule pass. |
| 6. Separate source registration and bounded extraction | Existing source manager; source/version requirement shards under `vigil/external_governance/requirements/requirements/`; scope/review sidecars | Once admission review permits it, register missing editions accurately, preserve existing source identities and allocate deterministic requirement IDs only for actual approved extraction. Perform actor, conditions, exceptions, modality and atomicity review. No copied copyrighted standard corpus. |
| 7. Separate relationship review | `taxonomy-relationships.json`, taxonomy standards references and dated review artifacts | Admit only source-faithful component correspondences with canonical vocabulary and traceable review. No class definition/recognition changes. Historical pending notes remain recoverable; any later refresh is explicitly dated. |
| 8. Verify generated coverage and public metadata | Existing requirement-manager output functions (`coverage_manifest`, coverage index/reports), source catalogue/queue, `vigil/docs/design/EXTERNAL-REQUIREMENT-WEBSITE-HANDOFF.md` | Manager-generated role/status/force display, stable IDs, no hidden qualifications. Existing vocabulary should need no force-chip category changes. Change builders only if required by approved behaviour. |
| 9. Verify resolver and Section 04 separately | `resolve_clause_external_requirements.py`, `occurrence_requirement_validation.py`, `validate-occurrence-requirement-assessments.py`, `build-vigil-public-records.py`; downstream website repository | Keep contextual and unmapped-clause exclusions. Assert disposable candidates cannot generate assessments or polarity. Section 04 displays only independently justified occurrence rows. Website code is outside this repository: inspect its actual renderer and release contract rather than assuming support. Any required downstream change needs its own scoped review. |
| 10. Consider individual occurrence work | Existing `EXTERNAL-REQUIREMENT-ADJUDICATION.md`, Incident workflow and provenance | This handoff does not authorise an INC-090 edit. Further evidence and substantive occurrence review are required. No mechanical backfill, retained-count target or speculative failure. |

Source registration is not source approval. Extraction review is not relationship approval. Relationship approval is not occurrence applicability or polarity. Implement those dependencies in that order, allowing reviewed staging artifacts to avoid a requirement/relationship identity cycle. Promotion requires both a resolving canonical source and retained invariant-review evidence.

## Proposed isolated fixture coverage

These are test designs, not implemented permanent tests.

| Fixture | Expected result |
| --- | --- |
| Existing valid primary AI requirement and extraction scope | Continues to pass unchanged |
| Supporting law, standard or framework with actual text access, faithful modality, bounded partial scope and complete admission evidence | Passes eligibility without relabelling |
| Supporting-only source with zero requirements / with one requirement | First passes; second fails |
| In-progress/partial supporting scope with declared unreviewed sections | Passes only under existing incompleteness restrictions; cannot claim assured/full review |
| Supporting complete scope that lists decisive unreviewed/inaccessible sections or lacks required review evidence | Fails the applicable completeness/assurance check |
| Context/discovery, excluded source, or commentary treated as a normative duty | Remains ineligible for normative extraction; commentary rejection needs substantive review in addition to structural guards |
| Metadata-only or abstract-access ISO provision with invented clause content | Rejected for full clause extraction; no reconstructed text |
| Voluntary mandatory-normative clause | Retains voluntary force; no binding-law coercion and no adoption gate for alignment |
| Treaty permission, qualified legal prohibition and recommendation | Actor, exceptions and modality survive round-trip generation; no uniform-duty conversion |
| Existing source/version and requirement identity round trip | IDs and version references remain stable; deterministic generators only |
| Contextual relationship or unmapped/candidate-only Incident clause | Produces no class-derived candidate |
| Supported strong-supporting relationship, actual mapped clause, relevant and irrelevant occurrences | Produces candidates only; applicability and polarity remain independent |
| Access interruption without additional concession | Cannot be an FC-059 failure fixture; preserve class contract |
| Documented valid authority with meaningful choice; unsupported authority; unresolved decisive basis | Isolated semantic review examples distinguish successful/failed/boundary outcomes without selecting an external result from class polarity |
| Public supporting requirement projection | Source role and voluntary/binding force preserved; no generated Section 04 row without canonical occurrence assessment |

## Validation commands and dependencies

Use the existing workflow commands and their prescribed environment at the implementation commit. First run source-manager and requirement-manager validation (including generated checks), then fidelity and metadata controls, then canonical Incident, occurrence assessment, public projection and provenance validation. Requirement loading uses `external_requirements_io`; do not manually rewrite the compatibility aggregate or shard manifest.

Relevant existing test suites include external sources/requirements, metadata/fidelity, clause resolver, occurrence role independence, external requirement assessments and public projection. The exact tests are `test_external_sources.py`, `test_external_requirements.py`, `test_external_requirement_metadata.py`, `test_external_requirement_fidelity.py`, `test_clause_requirement_resolver.py`, `test_occurrence_role_independence.py`, `test_external_requirement_assessments.py` and `test_external_requirement_public_projection.py` under `vigil/tests/`. Run meaningful generic fixtures plus existing integration checks; avoid repeated whole-corpus runs without a new failure or change.

Expected baseline: 98 source versions, 1,102 canonical requirements, 189 canonical Incidents. Future requirement/mapping counts are unmeasured, not promised. Preserve existing IDs, versions, assessments and source clauses. Record exact old/new failures before proposing repairs. The earlier [historical validation receipt](https://github.com/CAM-Initiative/Vigil/blob/035b81e88368c92a88088ae1bec8b7d30f81376c/vigil/docs/reviews/2026-10-11-infrastructure-governance-registration/VALIDATION.md) records a pre-existing additional referential-integrity failure concerning FC-084 references in INC-060/189; this research neither repairs it nor reports the repository universally clean.

## Research-pass verification

The amendment is limited to this review directory. No source registry/scope/assurance data, canonical requirement shard, relationship ledger, class definition, Incident, schema, script, builder, workflow or permanent test is modified. Verification checks the diff boundary, relative Markdown links, cited existing requirement identities and unchanged corpus counts. The results are recorded in the README amendment addendum. These checks are temporary verification, not new governance controls.

## Stop

Return the revised Gate 1 and research for maintainer review. Implementation approval must cover the amended behaviour, not merely the earlier treaty-only proposal. Gate 2 remains a separate stop before broad repairs exposed by an approved control change.
