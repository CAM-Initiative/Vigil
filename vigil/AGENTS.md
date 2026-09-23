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
- Keep the lay occurrence narrative in `summary`; keep evidence adjudication in `vigil_assessment.factual_basis`; keep governance significance in `vigil_assessment.significance_to_cam`; keep the integrated governed conclusion in `vigil_assessment.governance_interpretation`. Before editing any of these fields, read the website-rendering crosswalk in `vigil/MAINTAINERS.md`.
- Keep structured `harm_impact_assessment` as substantive occurrence-level diagnosis under VIGIL-HIM. Overall severity is the highest supported assessed materialised-harm band; never average or sum dimensions, and never encode unreported harm as S1. Keep severity independent of taxonomy classification, source prestige, workflow priority and hypothetical worst-case harm.
- Keep taxonomy classification separately governed and allow an Incident to remain unclassified.
- Preserve append-only interpretive provenance and do not represent AI review as human review or verification.

Legacy record classes and migration artefacts remain recoverable through Git history. Active Incident records contain only information required by the current VIGIL data model. Do not restore retired payloads, migration-source metadata or retired-record links to active records.

## Stage 01 “What happened” contract

The full field-to-render contract is maintained in `vigil/MAINTAINERS.md` under **Incident authoring and website-rendering crosswalk**. Treat that crosswalk as mandatory reading before Incident prose maintenance.


- The canonical `summary` is rendered verbatim on the public Case File as **Stage 01 → Incident → What happened**.
- `summary` answers the lay occurrence question only: what happened, to whom or what, when materially relevant, what happened next, and material consequences. It may attribute disputed facts and preserve essential uncertainty, but evidence adjudication such as what the preserved evidence establishes or does not establish belongs in `vigil_assessment.factual_basis`.
- Do not use `summary` as a taxonomy, governance-diagnosis, Harm Impact, maintenance or workflow surface. VIGIL classification belongs in `taxonomy_classification`; governed diagnosis belongs in `vigil_assessment.governance_interpretation`.
- A prose-quality validator failure in `summary` authorises only the smallest edit required to remove the offending internal identifier, maintenance phrase or VIGIL diagnostic framing. **Do not shorten, flatten, summarise away, or otherwise rewrite supported occurrence detail merely to satisfy that validator.**
- Do not perform corpus-wide `summary` rewrites as a mechanical response to a prose-quality test. Review each affected Incident individually and preserve its established chronology, actors, systems, consequences, source-bounded detail and uncertainty.
- Rich factual detail is expected where the evidence supports it. The purpose of the Stage 01 boundary is separation of facts from diagnosis, not brevity.

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

## Human-maintainer approval gate for validator and schema changes

Before changing any validator, schema rule, permanent corpus test, builder rule or publication guard that can change which canonical Incident content passes or fails, read **Human-maintainer stop conditions for validators, schema rules and corpus-wide tests** in `vigil/MAINTAINERS.md`.

For any semantic change, first tell the human maintainer:

- what the rule does now;
- exactly what will change;
- what content will newly pass or fail;
- which fields and website stages are affected;
- how many records may be affected, or that the scope is not yet measured;
- whether the change could induce record rewrites or information loss; and
- why the validator, rather than the schema/renderer/documentation, is the correct enforcement point.

Then **STOP and obtain explicit human approval before editing the validator**.

Approval to change the validator is not approval to repair the corpus. After the change, run it read-only, report the failures, and **STOP again before semantic, multi-record or corpus-wide repairs**.

If a validator conflicts with the field-to-render contract, do not “fix” the records to satisfy it. Escalate the conflict to the human maintainer.

## Test maintenance contract

Permanent tests must protect stable repository contracts: schema and validator behaviour, generic cross-record integrity, publication/build invariants, or an explicitly immutable ID/allocation contract.

Do not add permanent CI tests whose only purpose is to prove a completed migration, current branch state, exact current class count, one work package's source composition, or one Incident's adjudication. Preserve those acceptance results in the relevant audit record or run them as bounded one-off validation during the work package.

When testing validator behaviour, prefer an isolated fixture or direct rule mutation. Do not make a unit test depend on the unrelated validity of a live canonical Incident unless the test is intentionally a corpus regression. A single record defect should not cause unrelated rule tests to fail.

Dataset-specific snapshot tests are appropriate only where the underlying value is explicitly immutable (for example, stable allocated IDs). Avoid duplicating the same invariant through hard-coded counts, version strings and incident-specific assertions.


## Incident rebuild and re-adjudication gate

Substantive Incident rebuilds, refactors and taxonomy re-adjudications MUST follow `vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md`.

A rebuild is non-destructive by default. Before rewriting, establish the canonical baseline, search for additional occurrence evidence, preserve supported factual detail, recover every existing taxonomy mapping, load the current taxonomy, and adjudicate mappings against recognition criteria and exclusions. Existing mappings and sources may change only through explicit disposition.

For a full rebuild, create a maintainer adjudication manifest from `vigil/templates/incident-rebuild-adjudication-template.json` and run:

```bash
python vigil/scripts/validate-vigil-incident-rebuild.py \
  --baseline-ref <baseline-ref-or-commit> \
  --candidate-file vigil/records/incidents/<INCIDENT>.json \
  --manifest <adjudication-manifest.json>
```

The guard must pass before the rebuilt record is accepted. Every baseline taxonomy mapping must be accounted for as retained, changed, superseded or removed-unsupported. Silent mapping deletion is prohibited. Material shortening of `summary` or `vigil_assessment.factual_basis` requires an explicit fidelity reason in the manifest.

Do not use an older working branch's taxonomy labels or mappings as the adjudication authority when the current canonical taxonomy is available.


### Gmail staging requirement

When Incident adjudication produces a taxonomy gap or another unresolved maintainer action, follow the Gmail staging protocol in `vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md`. In a connected ChatGPT maintenance session, use the Gmail connector to read the latest labelled `[CURRENT VIGIL QA ACTION]` queue, merge the new unresolved action into that queue, send the replacement self-email, and apply the `VIGIL/CURRENT QA ACTION` label.

Do not leave a material next action only in conversational handoff text. Do not overwrite unresolved queue items with a one-item email. If Gmail is unavailable, explicitly report that staging was not completed and preserve the full ready-to-send payload.

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
