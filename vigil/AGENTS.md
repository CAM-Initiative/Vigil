# VIGIL Agent Instructions

VIGIL is a public ecosystem observation, failure-mode, CAM proposal, and CAM patch-note registry. It is subordinate to CAM's existing constitutional and operational order.

VIGIL does not create doctrine, amend adopted instruments, determine liability, or verify final factual truth. Do not treat a VIGIL record as a CAM amendment.

VIGIL records preserve structured governance evidence and workflow state. CAM instruments remain authoritative only through the normal Caelestis amendment, validation, and adoption process.

VIGIL operates by default as **AI-authored, semi-autonomous production under human contract approval**. The named AI system performs substantive evidence triage, record analysis, source comparison, reconciliation, monitoring, and record production. The default human role is `contract-approver`: establishing or approving objectives and boundaries, authorising repository actions and progression decisions, and retaining any separately established CAM constitutional or adoption authority. Contract approval does not establish human authorship, substantive review, source verification, or line-by-line inspection. Use [`provenance/AUTHORSHIP-PROVENANCE.json`](provenance/AUTHORSHIP-PROVENANCE.json) for the controlled vocabulary, inheritance rules, and any evidenced artefact-level exception.

> No VIGIL record without date, source state, evidence confidence, CAM relevance, interpretive provenance, and next action or implemented-CAM-change explanation.

## Record Classes

VIGIL currently recognises six primary record classes:

```text
OBS   — Material unresolved ecosystem governance observation / early warning record
RESEARCH — Non-binding research artefact that may originate an evidence-to-repair chain
FM    — Ecosystem Failure Mode / triage record
PROP  — CAM/Caelestis proposal record
PATCH — Implemented or directly pre-existing CAM/Caelestis patch note
LEARN — Published, bounded learning closure for a section-complete chain
```

### OBS — Observation Record

Use an Observation Record only when the record preserves a material unresolved governance proposition that is not adequately represented by an existing failure mode, proposal, or patch.

Source evidence for an existing record belongs in that record's canonical `source_records` block. An incident, article, status-page entry, or report does not become an OBS merely because it is new.

Observation records must state the governance significance and material uncertainty. They must not contain failure-mode triage, CAM repair logic, patch instructions, curator tasking, or directions such as ‘add this incident to’ another record.

### RESEARCH — Research Record

Use a Research Record for a substantive research artefact that supplies the evidence basis for a failure mode, proposal, or repair pathway and would otherwise make a separate observation duplicative.

Research records are non-binding. They may originate an evidence-to-repair chain in place of, or alongside, an observation, but CAM authority arises only through an implemented PATCH. A proposal may supply diagnosis and response design where one was required; it is not mandatory where the authoritative FM and/or PATCH already populates that report section. Markdown research records must carry the required structured front matter and reciprocal links to the VIGIL records they support.

### FM — Failure Mode Record

Use a Failure Mode Record when an ecosystem failure pattern is confirmed, strongly evidenced, recurring, or sufficiently clear to require triage.

Failure Mode records must include the failure definition, failure threshold, classification, triage information, source records, and CAM routing implications.

The failed subject must be an ecosystem system, deployment, runtime, platform behaviour, governance practice, or externally observable failure pattern. VIGIL itself is not the failed system.

Failure Mode records are not generic tags.

### Triage State Boundaries

Use this doctrine for every failure-mode triage decision:

> Current triage priority is mutable operational state. Historical urgency is provenance. Failure severity is classification. Triage status is workflow. Ecosystem monitoring is continuing external observation.

* Model 2.0 severity uses only `S0`, `S1`, `S2`, `S3`, `S4`, and `SU`. Rate the greatest reasonably supported harm within the stated evidence and deployment scope; do not use an unconstrained imaginable worst case.
* `failure_classification.severity` describes the failure and is not reduced merely because CAM repaired its own corpus. `SU` requires a stated assessment gap and next step.
* Model 2.0 priority uses only `P0`, `P1`, `P2`, `P3`, `PN`, and `PU`. `PN` means no active queue priority; `PU` means urgency is not yet assessed.
* `triage.triage_priority` describes the urgency of the next required CAM/VIGIL action now. It must not preserve historical urgency, severity, public importance, or passive monitoring as queue priority.
* `triage.triage_status` is the canonical workflow-status field and uses the controlled workflow vocabulary in `VIGIL.Schema.json`; do not add a duplicate `workflow_status` field.
* `record_state` remains the record lifecycle. `ecosystem_status.monitoring_required` remains continuing external observation and does not automatically justify P0–P3.
* New and reconciled FM records declare `triage.model_version: "2.0"`. Legacy records remain in diagnostic migration mode until Pass 3 review.
* Preserve evidenced transitions in append-only `triage_history`; never fabricate a legacy transition. Identify the analytical reviewer and governance authority accurately rather than defaulting to a generic “VIGIL maintainers” actor.
* Use `vigil/docs/2026-triage-model-inventory.json` as the migration review surface. Do not mass-map descriptive severity, uncontrolled priority, or free-text workflow values.


### PROP — Proposal Record

Use a Proposal Record when CAM/Caelestis governance development, doctrine amendment, runtime safeguard, architecture primitive, or operational design is being proposed. VIGIL repository maintenance, schema housekeeping, validator maintenance, index rebuilding, and workflow administration are not CAM proposals.

Proposal records may be linked to observations or failure modes, but may also exist without them.

Proposal records must not claim that a patch has already been implemented.

Each proposal should identify no more than one authoritative primary failure mode by default.
Governance-origin and research-origin proposals may have no primary failure mode. Adjacent failures,
precedents, and separate workstreams belong in typed, non-transitive
`linked_records.contextual_relations`.

### PATCH — Patch Note Record

Use a Patch Note Record only when a CAM/Caelestis change has actually been implemented, or when a retrospective patch note identifies direct pre-existing CAM/Caelestis coverage for a failure that VIGIL had not previously linked.

Patch notes record the actual CAM/Caelestis control content, where it changed or originated, why it governs the failure, what evidence or proposal prompted the repair or crosswalk, and how corpus implementation was verified.

Patch notes must distinguish completed CAM work from remaining ecosystem or runtime work.

A PATCH resolves one primary failure mode by default. Multiple resolved failure modes require an
explicit `repair_scope` exception rationale and a separate verification outcome for every failure.
Mere adjacency, shared subject matter, or use of the same corpus instrument does not establish a
multi-failure repair.

VIGIL schemas, validators, indexes, workflows, migrations, reconciliation passes, and repository administration are never PATCH targets.

### LEARN — Learning Closure Record

Use a LEARN record only when Sections 01–05 already contain sufficient authoritative content and the LEARN record can supply Section 06 without creating new incident evidence, failure classification, proposal authority, or repair claims.

Completion is a report-section test, not a record-count test:

* OBS is optional where FM or RESEARCH supplies Section 01.
* PROP is optional where FM diagnosis and/or PATCH response rationale supplies Section 04.
* FM remains authoritative for Section 03.
* PATCH remains authoritative for Section 05.
* LEARN remains authoritative only for Section 06.

LEARN records must preserve the factual kernel, governance reasoning corrected by the completed chain, abstracted lesson, conclusions to integrate, foreseeable risk if the learning is omitted or diluted, future application, and generalisation boundary. They must not duplicate `source_records`, summarise internal PATCH content for the public Knowledge Base, or imply that an integrated learning conclusion has already been implemented by an external system.

## Interpretive Provenance Rules

Every substantive VIGIL record must contain `interpretive_provenance` with:

* an append-only `review_history`;
* a `current_ai_review` identifying the reviewing platform, exact model/version, date, scope, capability profile, known limitations, and outcome;
* the operating model of AI-led analysis with high-level human governance editorship;
* the named human governance editor and authority boundary; and
* a note preserving unknown historical reviewer identity rather than inventing it.

Rules:

* Do not overwrite prior reviews when a newer AI model re-examines a record.
* Do not retroactively assign an earlier model identity unless the record or source proves it.
* A review date MUST NOT predate `record_identity.created` or, where that field is unavailable, `date_recorded`.
* Record templates MUST use explicit placeholders and MUST NOT seed a real historical review identity or date into a newly created record.
* A later model may disagree with an earlier interpretation; preserve both reviews and identify the evidence and capability differences.
* Distinguish AI analytical review from human governance editorship and CAM adoption authority.
* Do not attribute routine analysis to “VIGIL maintainer” where a named AI system performed the work.
* Reviewer capability is part of the evidence chain. State whether the reviewer could directly analyse text, images, audio, uploaded video, or externally hosted video.

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

vigil/templates/research-record-template.md
```

If the proposal template filename is later corrected from `tempate` to `template`, update this file and any scripts or references in the same administrative commit, not as a VIGIL PATCH record.

## Schema Rules

The canonical schema-rules contract is:

```text
vigil/VIGIL.Schema.json
```

This file is a schema-rules contract for VIGIL record classes. It is not a CAM instrument and must not be represented as a PATCH target.

Agents must implement or validate records according to the approved record-class templates and schema rules. Do not infer new record classes, rename fields, flatten source records, or relax validation without explicit instruction.

Published RESEARCH records must satisfy the research quality contract in `VIGIL.Schema.json`.
Short, single-source or lightly synthesised material belongs in an existing record's
`source_records` or in an OBS where a distinct unresolved governance proposition exists.
Do not promote a source summary to RESEARCH merely because it has a valid front matter block.

## Source Evidence Rules

When working in `vigil/`:

* Preserve date, source, retrieval path, source state, evidence confidence, CAM relevance, and next action or implementation explanation for every VIGIL record.
* Preserve rich source packages in `source_records`.
* `source_records` is the only canonical source-evidence block in individual records.
* Source evidence must be embedded in the substantive FM, OBS, PROP, or PATCH it supports; do not create an OBS solely to duplicate or route evidence into an existing record.
* Do not add `source_data` or `source_data.sources` to individual records.
* Do not flatten rich source records into a single URL field.
* Every source must identify `evidence_modality`, `primary_artefact_access`, and `interpretive_reliance`.
* Preserve the original source URL even where a local copy, transcript, screenshot, or later mirror becomes available.
* A transcript, screenshot, summary, or human description is not equivalent to direct audiovisual or behavioural review.
* State explicitly whether the named AI reviewer directly inspected the primary artefact.
* Mark public reports, social-media observations, automated search results, and third-party claims provisional unless corroborated.
* Do not invent sources, URLs, citations, dates, legal claims, jurisdictions, severity, harm outcomes, or direct-access claims.
* If a source is missing, use a clear TODO, `unknown`, or `not applicable` field according to the relevant template.
* Keep uncertainty visible.

## Record-Boundary Rules

Agents must preserve record-class boundaries:

* Do not put failure-mode triage in an OBS record.
* Do not put CAM proposal logic in an OBS record.
* Do not put patch-note claims in a PROP record.
* Do not create a PATCH record unless implemented or direct pre-existing CAM/Caelestis coverage has been verified.
* Do not treat CAM-related instruments as affected by an OBS record; use related/similar routing language for observations.
* Do not treat an FM record as a mere tag.
* Do not mutate adopted CAM instruments from inside a VIGIL pass unless separately instructed.

## Observatory Boundary

VIGIL is the observatory, not the governed ecosystem system and not the patched corpus.

* A failure mode must describe an ecosystem system, deployment, runtime, platform behaviour, governance practice, or externally observable failure pattern. VIGIL may appear as the evidence registry or source publisher, but VIGIL itself MUST NOT be the failed system.
* A PATCH record must document implemented or directly pre-existing CAM/Caelestis doctrine, taxonomy, runtime governance, or architecture coverage. VIGIL schemas, validators, indexes, workflows, migrations, and repository maintenance MUST NOT be represented as PATCH records.
* A retrospective PATCH is permitted only where it identifies the actual CAM/Caelestis control content, effective origin, relevant sections, and the failure records that content governs.
* Repository audits, reconciliation passes, migrations, validation changes, and generated-index rebuilds belong in commits, pull-request descriptions, maintenance notes, and record metadata—not in PATCH records.
* VIGIL records do not create CAM authority. CAM instruments remain authoritative only through the Caelestis amendment, validation, and adoption process.

## CAM Routing Rules

CAM routing metadata is internal.

For OBS records, use related/similar CAM routing language.

For FM records, affected CAM routing may be used where the external failure is triage-relevant.

For PROP records, use target CAM/Caelestis routing language.

For PATCH records, use changed, implemented, or directly pre-existing CAM/Caelestis routing language.

Do not make CAM affected instruments the primary public classification layer.

## Record Automation Rules

* The source of truth is the individual JSON record files under `vigil/records/`.
* Do not manually edit generated registry indexes:
  * `vigil/VIGIL.Failures.Index.json`
  * `vigil/VIGIL.Observations.Index.json`
  * `vigil/VIGIL.Proposals.Index.json`
  * `vigil/VIGIL.PatchNotes.Index.json`
  * `vigil/VIGIL.Research.Index.json`
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
* Run `python vigil/scripts/run-vigil-lifecycle-validation.py` to validate lifecycle, corpus coverage, patch provenance, proposal resolution, the VIGIL/CAM observatory boundary, and interpretive provenance.
* Rebuild generated registry indexes with `python vigil/scripts/build-vigil-records.py` and `python vigil/scripts/enrich-vigil-indexes.py` after changing records.
* Use the type-specific registry indexes for interface/live ingestion.
* Use `vigil/VIGIL.Registry.Index.json` as the master registry composed from the generated type indexes.
* Keep placeholder/example records clearly marked as scaffolding in generated registry records.

## Implementation Discipline

Prefer small, inspectable changes.

Do not perform broad deterministic rewrites of existing records unless explicitly instructed.

Do not migrate content and redesign schema in the same pass unless the maintainer has expressly approved the combined reconciliation.

Do not repair schema by weakening validation.

Do not repair record content by deleting uncertainty.

Do not update the CAM Interface layer from a VIGIL pass unless separately instructed.

When in doubt, stop and report the uncertainty rather than inventing a mapping.

## Corpus Coverage Reconciliation

Every failure mode must preserve a `corpus_coverage` assessment against a named repository, ref, commit, and date.

* `implemented-repair` means a linked patch records an implemented CAM/Caelestis repair and the CAM-side failure status is repaired.
* `retrospective-coverage` means current canonical CAM/Caelestis doctrine materially governed the failure before VIGIL linked it.
* `partial-coverage` means relevant CAM/Caelestis controls exist but a named primitive, implementation requirement, or conformance condition remains missing.
* `no-confirmed-coverage` means a corpus assessment was performed and no sufficient direct current-corpus control was confirmed; it is distinct from `verification-pending`, which means the assessment remains incomplete.
* External adoption, runtime conformance, ecosystem persistence, and legal compliance remain separate from CAM coverage.
* Retrospective patches must state the actual CAM/Caelestis control content and distinguish doctrine reviewed, amended, and relied upon without amendment.
* Corpus coverage audits are VIGIL maintenance and metadata reconciliation; they are not PATCH events.
