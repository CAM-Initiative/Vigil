# VIGIL Maintainer Guide

## Purpose

VIGIL is a public workflow, observation, failure-mode, proposal, and patch-note registry for preserving AI governance signals, triaging failure patterns, developing CAM-specific repair proposals, and recording implemented CAM changes.

VIGIL is subordinate to CAM's constitutional and operational order. VIGIL does not create doctrine, amend adopted instruments, determine liability, or verify final factual truth.

A VIGIL record may inform CAM governance work, but it is not itself a CAM amendment.

## Registry Philosophy

VIGIL separates four different activities that must not be collapsed:

```text
OBS   preserves observed signals and source evidence.
FM    records and triages confirmed or strongly evidenced failure modes.
PROP  develops CAM-specific governance repair logic.
PATCH records implemented CAM changes.
```

The registry is source-data-first and record-class-specific.

External users should be able to understand a VIGIL record from its source data, system context, jurisdictional context, and record type without needing to understand CAM instrument numbering.

CAM routing remains important, but it is internal maintainer metadata.

## Current Record Classes

### OBS — Observation Record

An Observation Record captures an observed signal, event, report, source item, public development, platform behaviour, system behaviour, jurisdictional development, or early warning input that may be relevant to AI governance, robotics governance, platform governance, UX safety, public legitimacy, or CAM.

Observation records are not automatically failure modes.

Use OBS when:

* something relevant has been observed;
* evidence may be incomplete, emerging, disputed, or provisional;
* the record should preserve source evidence before governance meaning is fully known;
* the record may later inform a Failure Mode or Proposal record.

OBS records must not include failure-mode triage or CAM repair logic.

### FM — Failure Mode Record

A Failure Mode Record captures a confirmed, strongly evidenced, recurring, or clearly triage-worthy failure pattern.

Use FM when:

* a system behaviour has failed in a recognizable way;
* harm, risk, procedural breakdown, safety degradation, or governance instability is evident;
* the same pattern may recur across systems, platforms, contexts, or jurisdictions;
* the issue requires triage, mitigation, classification, escalation, or CAM proposal development.

FM records must include failure definition, failure threshold, classification, triage, evidence, and routing implications.

### PROP — Proposal Record

A Proposal Record captures CAM-specific governance development, repair recommendation, amendment logic, template improvement, registry change, interface update, validator change, automation improvement, doctrinal clarification, or operational design proposal.

Use PROP when:

* CAM governance development is being proposed;
* an observation or failure mode suggests CAM may need repair, expansion, or clarification;
* a registry, template, validator, automation, interface, or instrument should be updated;
* a governance idea needs to be preserved before implementation.

PROP records must not claim implementation.

### PATCH — Patch Note Record

A Patch Note Record captures an implemented CAM-specific change, repair, update, amendment, registry correction, template update, schema update, validator update, automation update, interface update, crosswalk update, or documentation change.

Use PATCH only when:

* a change has actually been implemented;
* maintainers need a public and machine-readable record of what changed and why;
* a proposal has been adopted or partially implemented;
* a failure mode has resulted in a concrete repair.

PATCH records must distinguish completed work from remaining work.

## Template Files

Approved record templates are stored under `vigil/templates/`.

```text
observation-record-template.md
observation-record-template.json

failure-mode-record-template.md
failure-mode-record-template.json

proposal-record-tempate.md
proposal-record-tempate.json

patch-note-record-template.md
patch-note-record-template.json
```

The Markdown templates define the human-readable meaning of each record type.

The JSON templates define the machine-readable skeletons.

If a filename typo exists in the repository, preserve the existing filename until a deliberate rename patch updates all references.

## Schema Rules

The canonical schema-rules contract is:

```text
vigil/VIGIL.Schema.json
```

This file replaces the previous schema file as the authoritative rules contract for record-class validation and schema generation.

Maintainers should treat it as a source of implementation requirements for JSON Schema files, validation scripts, test fixtures, and index generation.

Do not use schema work to redesign record ontology.

## Decision Model

### Use OBS when the record is a signal.

Examples:

* a news report about agentic AI deployment;
* a public platform behaviour that may matter later;
* a jurisdictional development;
* an unverified social media observation;
* an early warning source item;
* a relevant but not-yet-triaged system behaviour.

### Use FM when the record is a failure.

Examples:

* a confirmed or strongly evidenced system failure;
* a recurring failure pattern;
* a safety breakdown;
* a procedural or governance collapse;
* a failure that requires triage;
* an operational harm pattern.

### Use PROP when the record is a CAM proposal.

Examples:

* proposed instrument amendment;
* proposed template repair;
* proposed schema repair;
* proposed validator repair;
* proposed interface update;
* proposed automation update;
* proposed doctrinal clarification.

### Use PATCH when the record is an implemented change.

Examples:

* implemented schema update;
* implemented template update;
* implemented validator update;
* implemented interface update;
* implemented CAM instrument repair;
* implemented registry correction;
* implemented automation change.

## Source Preservation Rules

Source evidence is load-bearing.

Maintainers must:

* preserve rich source records in `source_records`;
* preserve machine-readable source mirrors in `source_data.sources` where required;
* keep source title, author/publisher/account, date, URL, archive URL, retrieved date, source type, source platform, system/product, model/algorithm, deployment context, source context, URL status, and relevance note where available;
* never flatten rich source data into a single URL field;
* never replace known source values with placeholders;
* never invent missing source values.

If source data is unknown, use explicit placeholder values such as:

```text
unknown
to be assessed
to be confirmed
not applicable
TODO
```

depending on the template.

## CAM Internal Routing

CAM routing fields are internal maintainer metadata.

Use different routing language by record class:

```text
OBS   → related_or_similar_* fields
FM    → affected_* fields
PROP  → target_* fields
PATCH → changed_* fields
```

This distinction matters.

An observation may be relevant to CAM without affecting a CAM instrument.

A failure mode may affect or implicate CAM governance areas.

A proposal may target CAM instruments or infrastructure.

A patch note records what actually changed.

## Field-Boundary Rules

Maintainers must preserve field boundaries.

OBS records must not contain:

```text
failure_classification
triage
proposal_scope
proposal_rationale
implementation_notes
change_classification
change_details
implementation_verification
impact_summary
remaining_work
date_implemented
```

FM records must contain:

```text
failure_mode_definition
failure_threshold
failure_classification
triage
```

PROP records must contain:

```text
proposal_rationale
proposal_type
proposal_scope
implementation_notes
external_relevance
next_action
```

PATCH records must contain:

```text
date_implemented
change_classification
change_details
implementation_verification
impact_summary
remaining_work
```

## Linked Records

VIGIL records may link to related records, but linking must not invent a lifecycle.

OBS records may link to:

```text
related observations
external references
research
standards
```

FM records may link to:

```text
related observations
related failure modes
related proposals
related patch notes
external references
research
standards
```

PROP records may link to:

```text
related observations
related failure modes
related proposals
related patch notes
external references
research
standards
```

PATCH records may link to:

```text
related observations
related failure modes
related proposals
related patch notes
external references
research
standards
commits
pull requests
issues
```

A proposal must not list itself as a patch note.

A patch note must not claim to implement a proposal unless implementation actually occurred.

## External Ingestion

Third parties should be able to consume VIGIL records without knowing CAM.

Public-facing fields should prioritise:

```text
record identity
record type
source records
source data
system context
jurisdictional context
evidence confidence
failure classification, for FM only
triage, for FM only
proposal scope, for PROP only
change details, for PATCH only
linked records
```

CAM-specific fields are available for maintainers but should not be required to understand the public meaning of a record.

## Automation Notes

* Individual record files under `vigil/records/` are the source of truth.
* `python vigil/scripts/route-vigil-records.py` routes records into open, cluster, or closed folders.
* `python vigil/scripts/validate-vigil-records.py` validates individual records.
* `python vigil/scripts/build-vigil-records.py` generates aggregate JSON outputs.
* `vigil/VIGIL.ActiveRecords.json` is the canonical active/live aggregate for interface ingestion.
* `vigil/VIGIL.ClosedRecords.json` is the archival aggregate for closed records.
* `vigil/VIGIL.Records.Index.json` is the canonical lightweight global registry index.
* `vigil/VIGIL.Schema.json` is the canonical schema-rules contract.
* `.github/workflows/vigil-records.yml` runs VIGIL validation/build automation in GitHub Actions, if present.

## Generated JSON Outputs

Do not manually edit generated aggregates:

```text
vigil/VIGIL.ActiveRecords.json
vigil/VIGIL.ClosedRecords.json
vigil/VIGIL.Records.Index.json
```

Generated outputs must be rebuilt from individual record files.

No `VIGIL.Records.json` legacy aggregate should be reintroduced unless explicitly required for downstream compatibility.

## Maintenance Rules

```text
Do not delete source evidence.
Do not overwrite uncertainty with certainty.
Do not flatten source records.
Do not make CAM instruments the primary public classification layer.
Do not create a failure mode from a weak signal.
Do not create a proposal when only an observation exists.
Do not create a patch note unless implementation occurred.
Do not claim validation passed unless it was run.
Do not mutate adopted CAM instruments from a VIGIL pass unless separately instructed.
Preserve stable IDs.
Prefer additive migrations over destructive rewrites.
Prefer small, inspectable changes.
```

## Safe Change Sequence

When changing VIGIL infrastructure:

```text
1. Update templates manually.
2. Update schema rules.
3. Update validators and tests.
4. Validate with fixtures.
5. Migrate one record of each class.
6. Rebuild indexes.
7. Review generated outputs.
8. Only then consider broader migration.
```

Do not redesign schema, migrate records, and update the interface in the same pass.
