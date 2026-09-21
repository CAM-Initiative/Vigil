# VIGIL Agent Instructions

VIGIL is an Incident-centred public observatory. Its sole active public record class is:

```text
INC — bounded occurrence-level Incident record
```

Canonical records are stored only under `vigil/records/incidents/`. FM, OBS, RESEARCH, PROP, PATCH and LEARN are retired record classes. Do not create, restore, load, publish, validate or resolve them as active records. Their historical content remains available through Git history and `stabilization/pre-fm-schema-migration`.

The taxonomy, external-governance datasets and CAM assessment are separate retained subsystems. VIGIL does not amend CAM/Caelestis doctrine, determine liability or establish final factual truth.

## Incident authority and provenance

- Preserve `source_records` as the only canonical source-evidence block.
- Preserve source URLs, evidence status, evidence modality, source residence, source role, access limitations and uncertainty.
- Do not invent sources, dates, affected systems, causal claims, legal findings, severity or taxonomy mappings.
- Keep occurrence-level facts in `summary` and `vigil_assessment.factual_basis`; keep governed diagnosis in `vigil_assessment.governance_interpretation`.
- Keep structured `harm_impact_assessment` as substantive occurrence-level diagnosis under VIGIL-HIM. Overall severity is the highest supported assessed materialised-harm band; never average or sum dimensions, and never encode unreported harm as S1. Keep severity independent of taxonomy classification, source prestige, workflow priority and hypothetical worst-case harm.
- Keep taxonomy classification separately governed and allow an Incident to remain unclassified.
- Preserve append-only interpretive provenance and do not represent AI review as human review or verification.

Legacy record classes and migration artefacts remain recoverable through Git history. Active Incident records contain only information required by the current VIGIL data model. Do not restore retired payloads, migration-source metadata or retired-record links to active records.

## Clause-level taxonomy assessment contract

When an Incident contains `vigil_assessment.source_clause_analysis.clauses[]`, its public clause-level assessment has three distinct layers:

1. `source_anchor` or `source_paraphrase` — the source-language basis.
2. `recovered_invariant_interpretation` — the general principle recovered from that source language.
3. `taxonomy_relationships[].rationale` — the occurrence-specific explanation published in the **Taxonomy assessment** column.

The rationale is public analytical content, not internal mapping metadata. Derive it from the source clause, the canonical taxonomy definition, invariant and recognition conditions, and the bounded Incident evidence. Explain what the clause demonstrates in this occurrence.

Do not replace the rationale with relationship-type boilerplate such as “the clause contributes to the recorded failure mechanism.” Do not use a Failure Class name, family name, identifier or mapping result as a substitute for the explanation. Structured identifiers, relationship roles and canonical-mapping state remain in their formal taxonomy fields.

Where a clause has multiple taxonomy relationships, preserve each distinct rationale in source order. Together they must form a coherent assessment without duplicating the same explanation. For adjacent, ambiguous-boundary, exemplar or other non-failure relationships, state precisely what the clause demonstrates and which occurrence condition is not established; semantic adjacency must not be converted into a canonical failure classification.

## Schema and publication

The sole VIGIL record-rules contract is `vigil/VIGIL.Schema.json`. Subsystem schemas remain scoped to taxonomy, external governance and CAM assessment.

Generated public record outputs are:

```text
vigil/VIGIL.Incidents.Index.json
vigil/VIGIL.Registry.Index.json
vigil/taxonomy/generated/VIGIL.FailureTaxonomy.CaseFileExamples.json
```

Build them only with:

```bash
python vigil/scripts/build-vigil-public-records.py
```

Do not manually edit generated indexes. The public master registry must expose only the Incident registry.

The public indexes are navigation projections, not duplicate record stores:

- `VIGIL.Incidents.Index.json` contains only the fields required for catalogue display, filtering/search, dates, severity/classification state and canonical record routing.
- Canonical Incident diagnosis, evidence, severity analysis, taxonomy objects and provenance remain only in `vigil/records/incidents/`.
- `VIGIL.Registry.Index.json` is a registry manifest. It must not duplicate the Incident `records` array.

## Test maintenance contract

Permanent tests must protect stable repository contracts: schema and validator behaviour, generic cross-record integrity, publication/build invariants, or an explicitly immutable ID/allocation contract.

Do not add permanent CI tests whose only purpose is to prove a completed migration, current branch state, exact current class count, one work package's source composition, or one Incident's adjudication. Preserve those acceptance results in the relevant audit record or run them as bounded one-off validation during the work package.

When testing validator behaviour, prefer an isolated fixture or direct rule mutation. Do not make a unit test depend on the unrelated validity of a live canonical Incident unless the test is intentionally a corpus regression. A single record defect should not cause unrelated rule tests to fail.

Dataset-specific snapshot tests are appropriate only where the underlying value is explicitly immutable (for example, stable allocated IDs). Avoid duplicating the same invariant through hard-coded counts, version strings and incident-specific assertions.

## Required workflow

Before editing an Incident, inspect `vigil/VIGIL.Schema.json`, the Incident template, the validator and comparable Incident records. Preserve stable IDs and substantive evidence.

Run at least:

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/validate-vigil-records.py
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/scripts/validate-vigil-interpretive-provenance.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/validate-authorship-provenance.py
```

Run taxonomy, external-governance and CAM-assessment validators when those retained subsystems are touched.

Do not reset, rebase, merge, cherry-pick, force-push or rewrite shared history as maintenance. Do not restore retired records from main, migration inputs or generated artefacts.
