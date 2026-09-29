# External Requirement Adjudication

Status: maintainer methodology

Applies to: VIGIL Incident-level assessment of external requirements represented by canonical `EXTREQ-*` records.

## Purpose and boundaries

The taxonomy-led candidate matrix is an indexing aid. It identifies which canonical external requirements are linked from the Fidelity Classes already mapped to an Incident. It does not determine legal or standards applicability, compliance, failure, or success.

Keep the following surfaces distinct:

- `taxonomy_classification` records VIGIL's occurrence-level Fidelity Class mappings and their mapping-local roles.
- `external_requirement_assessments` records VIGIL's separate assessment of a particular canonical external requirement against the bounded occurrence.
- `external_assessments` records analytical positions published by third parties.
- `standards_and_regulatory_references` preserves contextual cross-references. It is not the source of candidate requirements and must retain its current meaning.
- `source_records` preserves evidence. It remains the only canonical evidence and bibliography block.

An Incident-level requirement finding is about the specific occurrence and requirement. It is not a determination that a named provider, deployer, organisation, system, or jurisdiction is generally compliant or non-compliant.

## Deterministic candidate generation

Run:

```bash
python vigil/scripts/build-incident-external-requirement-candidate-matrix.py
```

The script reads current Incident records, canonical taxonomy family files, and canonical EXTREQ shards. For each Incident it takes the primary and secondary Fidelity Class mappings, resolves each mapped class's `external_references[]`, admits only a structured `requirement_id` that exactly matches `EXTREQ-[A-F0-9]{16}` and resolves in the canonical requirement shards, then deduplicates by Incident and requirement ID. `derived_from_class_ids` preserves every mapped class on that Incident that cites the same ID.

The candidate output is deterministic and sorted by Incident ID and requirement ID. It contains no applicability or finding decisions. Taxonomy reference roles and Incident mapping roles are carried for review context only; neither controls the external-requirement finding.

References with no structured `requirement_id` remain in their taxonomy records and do not become candidates, even when they are research, authoritative guidance, a standard, or regulatory context. IDs appearing as prose inside `standards_and_regulatory_references` also do not create candidates. A well-formed taxonomy ID that does not resolve in the canonical shards is reported as an unresolved citation and excluded from the matrix; maintainers must not silently substitute a nearby requirement.

The generated files are:

- `vigil/docs/audits/external-requirements/incident-requirement-candidate-matrix.csv`
- `vigil/docs/audits/external-requirements/incident-requirement-candidate-summary.json`

The matrix is a candidate audit artefact, not a substitute for the taxonomy adjudication ledger. It must be regenerated after taxonomy mapping or external-reference changes.

## Incident data contract

`external_requirement_assessments` is optional. Do not add it to `required_top_level_fields`, mechanically backfill empty arrays, or migrate the entire Incident corpus as part of candidate generation.

Each admitted entry contains only:

- `requirement_id`: a canonical ID resolving in the EXTREQ shards;
- `derived_from_class_ids`: a non-empty, unique list containing every mapped Fidelity Class on the Incident that cites this requirement;
- `applicability_status`: `applicable`, `insufficient-evidence`, or `not-applicable`;
- `applicability_basis`: a substantive occurrence-specific explanation;
- `finding` and `finding_basis`: present only when status is `applicable`;
- `assessed_on`: the date of the current assessment in `YYYY-MM-DD` form.

Do not add `evidence_refs`, copied requirement metadata, external source summaries, legal conclusions about an organisation, or extra status values. The canonical EXTREQ record remains the source for instrument, jurisdiction, force, lifecycle, applicability conditions and qualifications.

For `applicable`, assess the requirement's own conditions and preserve an independent finding of `failure-occurrence`, `successful-invariant`, or `ambiguous-boundary`. State why the bounded occurrence meets, fails, or leaves unresolved the particular requirement. A successful-invariant requires positive evidence that the requirement held under relevant pressure; silence or an absence of reported harm is not a pass. An ambiguous-boundary requires material engagement plus a concrete unresolved condition.

For `insufficient-evidence`, state which material applicability fact is missing or unresolved and omit both finding fields. For `not-applicable`, state the affirmative scope reason (for example, time, jurisdiction, system, actor, lifecycle, or a condition of the cited instrument) and omit both finding fields. Do not use `not-applicable` to encode an evidentiary gap.

Applicability review considers, as relevant, the requirement's legal or voluntary force, actor, governed system or practice, lifecycle, jurisdiction, effective date and transition rules, applicability conditions, exceptions, and the Incident's source-supported facts. Requirements sourced from voluntary frameworks or standards require evidence that the actor adopted or undertook the framework where that is a scope condition; taxonomy correspondence alone does not establish adoption.

The assessment's `finding_basis` is independent from taxonomy mapping roles and `classification_basis`. A source class may be `ambiguous-boundary` while an independently scoped external requirement has a `failure-occurrence` finding, or vice versa. Do not copy class rationale into either assessment basis.

## Evidence and taxonomy gaps

Read the admitted Incident sources and the canonical external requirement record before writing an assessment. The basis should identify the controlling facts and limits in plain language. Evidence remains in `source_records`; this contract does not add row-local source links.

If a potentially applicable external requirement concerns a runtime issue that no current Fidelity Class adequately represents, record the taxonomy gap through the taxonomy adjudication workflow. Do not skip taxonomy adjudication and attach an external finding directly to an unrepresented issue. Update the taxonomy and its review artefacts through the appropriate approval and validation path before deriving a candidate from a new class reference.

## Public projection

The generated public Incident index carries `external_requirement_assessments` without duplicating canonical EXTREQ metadata. Future interfaces may present two separate collections: applicable requirement findings, and assessments whose applicability is undetermined or not applicable. Candidate rows with no admitted assessment must remain visibly pending review; they must not be presented as findings.

## Validation

The Incident validator enforces the field allowlist, canonical ID formats and resolution, mapped-class provenance, exact contributor coverage, applicability/finding conditions, dates, and unique requirement IDs per Incident. The candidate-builder tests verify deterministic deduplication and ensure contextual references do not generate candidates.
