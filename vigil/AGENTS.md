# VIGIL Agent Instructions

VIGIL is a public workflow, observation, failure-mode, proposal, and patch-note registry. It is subordinate to CAM's existing constitutional and operational order.

VIGIL does not create doctrine, amend adopted instruments, determine liability, or verify final factual truth. Do not treat a VIGIL record as a CAM amendment.

VIGIL records preserve structured governance evidence and workflow state. CAM instruments remain authoritative only through the normal CAM amendment, validation, and adoption process.

> No VIGIL record without date, source state, evidence confidence, CAM relevance, and next action or implemented-change explanation.

## Record Classes

VIGIL currently recognises four primary record classes:

```text
OBS   — Material unresolved governance observation / early warning record
FM    — Failure Mode / triage record
PROP  — CAM-specific proposal record
PATCH — Implemented CAM patch note
```

### OBS — Observation Record

Use an Observation Record only when the record preserves a material unresolved governance proposition that is not adequately represented by an existing failure mode, proposal, or patch.

Source evidence for an existing record belongs in that record's canonical `source_records` block. An incident, article, status-page entry, or report does not become an OBS merely because it is new.

Observation records must state the governance significance and material uncertainty. They must not contain failure-mode triage, CAM repair logic, patch instructions, curator tasking, or directions such as ‘add this incident to’ another record.

### FM — Failure Mode Record

Use a Failure Mode Record when a failure pattern is confirmed, strongly evidenced, recurring, or sufficiently clear to require triage.

Failure Mode records must include the failure definition, failure threshold, classification, triage information, source records, and routing implications.

Failure Mode records are not generic tags.

### PROP — Proposal Record

Use a Proposal Record when CAM-specific governance development, amendment logic, template repair, schema repair, validator repair, automation repair, interface repair, or operational design is being proposed.

Proposal records may be linked to observations or failure modes, but may also exist without them.

Proposal records must not claim that a patch has already been implemented.

### PATCH — Patch Note Record

Use a Patch Note Record only when a change has actually been implemented.

Patch notes record what changed, where it changed, why it changed, what evidence or proposal prompted it, and how implementation was verified.

Patch notes must distinguish completed work from remaining work.

## Template Files

Use the approved templates before creating or modifying records:

```text
vigil/templates/observation-record-template.md
vigil/templates/observation-record-template.json

vigil/templates/failure-mode-record-template.md
vigil/templates/failure-mode-record-template.json

vigil/templates/proposal-record-tempate.md
vigil/templates/proposal-record-tempate.json

vigil/templates/patch-note-record-template.md
vigil/templates/patch-note-record-template.json
```

If the proposal template filename is later corrected from `tempate` to `template`, update this file and any scripts or references in the same patch.

## Schema Rules

The canonical schema-rules contract is:

```text
vigil/VIGIL.Schema.json
```

This file is a schema-rules contract for VIGIL record classes. Do not treat it as permission to redesign the ontology.

Agents must implement or validate records according to the approved record-class templates and schema rules. Do not infer new record classes, rename fields, flatten source records, or relax validation without explicit instruction.

## Source Evidence Rules

When working in `vigil/`:

* Preserve date, source, retrieval path, source state, evidence confidence, CAM relevance, and next action or implementation explanation for every VIGIL record.
* Preserve rich source packages in `source_records`.
* `source_records` is the only canonical source-evidence block in individual records.
* Source evidence must be embedded in the substantive FM, OBS, PROP, or PATCH it supports; do not create an OBS solely to duplicate or route evidence into an existing record.
* Do not add `source_data` or `source_data.sources` to individual records.
* Do not flatten rich source records into a single URL field.
* Mark public reports, social media observations, automated search results, and third-party claims provisional unless corroborated.
* Do not invent sources, URLs, citations, dates, legal claims, jurisdictions, severity, or harm outcomes.
* If a source is missing, use a clear TODO, `unknown`, or `not applicable` field according to the relevant template.
* Keep uncertainty visible.

## Record-Boundary Rules

Agents must preserve record-class boundaries:

* Do not put failure-mode triage in an OBS record.
* Do not put CAM proposal logic in an OBS record.
* Do not put patch-note claims in a PROP record.
* Do not create a PATCH record unless an implementation has occurred.
* Do not treat CAM-related instruments as affected by an OBS record; use related/similar routing language for observations.
* Do not treat an FM record as a mere tag.
* Do not mutate adopted CAM instruments from inside a VIGIL pass unless separately instructed.

## CAM Routing Rules

CAM routing metadata is internal.

For OBS records, use related/similar CAM routing language.

For FM records, affected CAM routing may be used where the failure is triage-relevant.

For PROP records, use target CAM routing language.

For PATCH records, use changed/implemented CAM routing language.

Do not make CAM affected instruments the primary public classification layer.

## Record Automation Rules

* The source of truth is the individual JSON record files under `vigil/records/`.
* Do not manually edit generated registry indexes:

  * `vigil/VIGIL.Failures.Index.json`
  * `vigil/VIGIL.Observations.Index.json`
  * `vigil/VIGIL.Proposals.Index.json`
  * `vigil/VIGIL.PatchNotes.Index.json`
  * `vigil/VIGIL.Registry.Index.json`
* Do not recreate deprecated generated aggregate files:

  * `vigil/VIGIL.ActiveRecords.json`
  * `vigil/VIGIL.ClosedRecords.json`
  * `vigil/VIGIL.Records.Index.json`
  * `vigil/VIGIL.Records.json`
* Add or modify individual record files under `vigil/records/`.
* Each individual record file must contain one record object, not an aggregate wrapper.
* Run `python vigil/scripts/route-vigil-records.py` to move misplaced records to the correct canonical type/year folder.
* Record files belong under `vigil/records/<record_type>/<year>/`; record state belongs inside `record_state`, not in the filesystem path.
* Run `python vigil/scripts/validate-vigil-records.py` before rebuilding.
* Rebuild generated registry indexes with `python vigil/scripts/build-vigil-records.py` after changing records.
* Use the type-specific registry indexes for interface/live ingestion.
* Use `vigil/VIGIL.Registry.Index.json` as the master registry composed from the generated type indexes.
* Keep placeholder/example records clearly marked as scaffolding in generated registry records.

## Implementation Discipline

Prefer small, inspectable changes.

Do not perform broad deterministic rewrites of existing records unless explicitly instructed.

Do not migrate content and redesign schema in the same pass.

Do not repair schema by weakening validation.

Do not repair record content by deleting uncertainty.

Do not update the CAM Interface layer from a VIGIL pass unless separately instructed.

When in doubt, stop and report the uncertainty rather than inventing a mapping.

## Corpus coverage reconciliation

Every failure mode must preserve a `corpus_coverage` assessment against a named repository, ref, commit, and date.

- `implemented-repair` means a linked patch records an implemented CAM repair.
- `retrospective-coverage` means current canonical doctrine materially governed the failure before VIGIL linked it.
- `partial-coverage` means relevant controls exist but a named primitive or implementation requirement remains missing.
- `uncovered` means no sufficient direct current-corpus control was identified.
- External adoption, runtime conformance, ecosystem persistence, and legal compliance remain separate from CAM coverage.
- Retrospective patches must state the actual control content and distinguish doctrine reviewed, amended, and relied upon without amendment.
