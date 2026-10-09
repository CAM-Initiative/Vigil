# VIGIL Research and Evidence MCP — bounded design (draft)

Date: 2026-10-09
Branch: feat/research-evidence-mcp-design
Status: design proposal; no production service or public deployment authorised.

## Purpose
Provide read-only, provenance-preserving research access to canonical VIGIL evidence, taxonomy and external governance requirements. This is retrieval, not automated adjudication, certification, compliance determination or evidence validation.

## Inspected repository contracts
- `vigil/taxonomy/VIGIL.FailureTaxonomy.Schema.json`: family/class invariants and occurrence polarity are separate.
- `vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md`: `vigil_assessment.source_clause_analysis.clauses[]` holds authoritative occurrence evidence episodes; `taxonomy_classification` holds accepted class mappings. Retired global Incident × class matrix is forbidden.
- `vigil/external_governance/requirements/source-scope.schema.json`: source access and extraction state, including blocked/partial sources.
- `vigil/cam_assessment/assessment.schema.json`: EXTREQ applicability/coverage and provenance are distinct from source facts.

Before implementation, inspect full `vigil/VIGIL.Schema.json`, canonical record exemplars, class family data, EXTREQ datasets, validators, and public-data eligibility at the implementation branch head. Do not assume these partial schema observations define every field.

## Architecture
Canonical validated JSON at pinned Git commit -> deterministic read-only index/projection -> MCP tools (initially local stdio) -> client.
No external database, embedding model, public hosting, write endpoint or generative adjudication in the pilot. Projection must be rebuildable and must never mutate canonical data.

## Candidate v0 tools
1. `vigil_get_incident(incident_id)`: incident metadata, chronology, clause-level evidence, mapping roles, completeness and source references.
2. `vigil_search_incidents(query, class_id?, limit?, cursor?)`: bounded search over public fields, returning excerpts and canonical IDs.
3. `vigil_get_taxonomy_class(class_id)`: invariant, success/failure recognition, exclusions, family and version.
4. `vigil_find_incidents_by_class(class_id, polarity?, limit?, cursor?)`: only accepted mapped relationships, with explicit polarity and adjudication state.
5. `vigil_get_external_requirement(extreq_id)`: registered requirement, version, source accessibility and relationship state where available.
6. `vigil_get_corpus_metadata()`: commit, taxonomy version, schema versions, build time and known coverage limitations.

## Mandatory output envelope
`{dataset_commit, schema_version, taxonomy_version, record_id, adjudication_status, completeness, provenance, data, limitations}`.
Use actual canonical field names after schema audit; absent fields are explicit unknown/null, never invented. Every extracted claim must retain source IDs/locators and evidence-clause identifiers where available. Distinguish asserted source facts, VIGIL adjudication and model-generated user interpretation.

## Safety and publication boundaries
- Fail closed on validator errors, unresolved publication eligibility, or missing canonical provenance.
- Incomplete adjudication cannot be returned as completed, successful or failed overall.
- Do not infer polarity from missing success/failure evidence.
- Never promote taxonomy candidates to accepted occurrence findings.
- Preserve licensed/blocked external-source restrictions; no redistribution of inaccessible copyrighted text.
- No global Incident × EXTREQ candidate matrix; no mutation of canonical records.
- Use bounded pagination, deterministic sorting, argument validation, resource limits and stable error codes.

## Implementation tranches
A. Schema/data audit: field inventory, canonical paths, public visibility, validators, representative complete/incomplete/mixed incidents, EXTREQ access cases. Commit findings.
B. Deterministic projection: validate pinned snapshot, normalize lookup indexes, attach provenance and version envelope. Unit tests and fixture coverage.
C. Local MCP stdio adapter: implement tools 1–4 and metadata first; requirement retrieval only after access/relationship rules are verified.
D. Integration: MCP inspector smoke tests, adversarial prompts, malformed IDs, incomplete cases, chronology/source fidelity, schema-version drift; docs and example client.
E. Review gate: security/publication approval before remote transport, auth, rate limiting or public deployment.

## Acceptance criteria
- No writes to canonical corpus.
- Every response traces to a pinned commit and canonical IDs.
- Correct distinctions between clause evidence, mapping and interpretation.
- Incomplete and mixed cases retain their state.
- Deterministic output and test suite pass against a validated snapshot.
- No restricted external text exposed.
- Existing validator and incident-QA branches remain untouched.

## Out of scope
Automated incident classification, new evidence ingestion, compliance scoring, agent-initiated write-back, hosted REST API, embeddings and public production endpoint.
