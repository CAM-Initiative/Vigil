# VIGIL Maintainer Guide

## Purpose

VIGIL is the public workflow, observation, classification, and proposal registry for tracking AI governance failures and repair work before they become CAM amendments or implementation changes. It relates to CAM governance by preserving externally legible source data, reusable failure-mode classification, and proposal/patch routing metadata without itself creating CAM doctrine or amending adopted instruments.

VIGIL is source-data-first so public observations can be understood by external researchers, platform operators, UX reviewers, robotics and embodied-AI reviewers, and regulators without needing to understand CAM instrument numbering. CAM affected instruments remain important, but they are internal routing metadata rather than the primary public classification layer.

VIGIL supports external ingestion by keeping source data, system context, jurisdictional context, failure modes, harm vectors, severity, linked proposals, and patch status in machine-readable fields. This makes the registry suitable for UX, platform, robotics, embodied AI, regulator-facing, and third-party records.

## Registry philosophy

```text
Observation records are source-data-first.
Failure mode records are reusable classification objects.
Proposal records are governance repair notes.
CAM affected instruments are internal routing metadata.
```

Source evidence belongs in an observation. Reusable classification belongs in a failure mode. Repair logic belongs in a proposal. CAM patch routing belongs in `cam_internal`.

## Canonical chain

The canonical VIGIL chain is:

```text
OBS → FM → PROP → CAM Patch Queue
```

The chain may be partial. Valid examples include:

```text
OBS only
OBS → FM
OBS → FM → PROP
PROP only
PROP → CAM Patch Queue
OBS → FM → PROP → CAM Patch Queue
```

Use `linked_records.observations`, `linked_records.failure_modes`, `linked_records.proposals`, and `linked_records.patches` to connect the chain. Link records rather than duplicating long descriptions.

## Decision model

Create an **observation** when there is source evidence of a public, platform, product, system, governance, UX, robotics, or embodied-agent event or pattern. Do not add repair logic beyond immediate next-action notes.

Create a **failure mode** when several observations or proposals need a reusable classification object, or when a single well-defined failure pattern should be available for future records. Failure modes are not tags; they have IDs, names, definitions, applicable system types, known observations, known proposals, harm vectors, mitigation pathways, and jurisdictional or sector relevance where known.

Create a **proposal** when VIGIL has repair logic, governance amendments, validator changes, templates, or design recommendations. Proposals may exist without observations, but they should link observations or failure modes where continuity matters.

Create a **patch queue item** when a proposal or observation has been routed to a concrete CAM instrument, validator, automation, template, or governance-interface update.

Create a **crosswalk** when the purpose is to map VIGIL classifications to external taxonomies, laws, standards, regulator categories, platform taxonomies, or CAM-internal structures.

Maintainers should distinguish observation from proposal, distinguish failure mode from tag, distinguish external-facing source data from CAM-internal routing, classify jurisdictional relevance cautiously, preserve uncertainty rather than overstate evidence, and link records rather than duplicate descriptions.

## Field guidance

### `record_identity`

Stable identity for all VIGIL v2 records. Use `record_id`, first-class `record_type` (`observation`, `failure_mode`, `proposal`, `patch`, or `crosswalk`), title, status, created date, updated date, and version. Preserve stable IDs.

### `source_data`

External evidence and provenance. Observations should carry source URL, platform, author/account, observed/published dates, archive status, evidence availability, confidence, and reproducibility. For reusable failure modes or internal proposals, use conservative values such as `not applicable`, `to be confirmed`, or classification provenance rather than inventing evidence.

### `system_context`

Describes the system being observed or repaired: system type, vendor/platform, model/product, interaction mode, embodiment status, deployment context, user role, and affected population. Use this for external-facing context rather than CAM instrument numbers.

### `jurisdictional_context`

Captures primary jurisdiction, secondary jurisdictions, regulatory surface, sector, cross-border relevance, and public-interest relevance. Treat unclear jurisdictional mapping as `to be confirmed` or `unknown` rather than overstating legal relevance.

### `failure_classification`

Machine-readable failure classification. Use `failure_mode_ids` for reusable failure-mode records and keep `failure_family`, harm vectors, severity, likelihood, confidence, and affected rights/interests cautious and evidence-aligned.

### `linked_records`

Connects OBS, FM, PROP, and Patch Queue records. Observations may link one or more failure modes. Proposals may link observations and/or failure modes. Patch queue items should link proposals or observations that justify routing. External references may point to non-VIGIL sources.

### `cam_internal`

CAM routing metadata only. Use affected instruments, affected annexes, affected domains, governance layer, patch status, and validator/automation impact to help CAM maintainers route work. Do not make these fields the primary public taxonomy.

### `robotics_context`

Optional extension for robotics or embodied-system observations. Non-robotics records do not need this block. Use it when physical embodiment, actuation, proximity to humans, safety boundaries, override, emergency stop, operator presence, physical harm, or property harm is relevant.

## Maintenance rules

```text
Do not delete source evidence.
Do not overwrite uncertainty with certainty.
Do not make CAM instruments the primary public classification layer.
Do not create a proposal when only an observation exists.
Do not create a new failure mode if an existing one already fits.
Do create linked records where continuity matters.
Keep legacy compatibility until migration is complete.
Update generated indexes after record changes.
Preserve stable IDs.
Prefer additive migrations over destructive rewrites.
```

## External ingestion

Third parties should be able to consume VIGIL without understanding CAM. Prefer these fields for external ingestion:

- `record_identity`
- `source_data`
- `system_context`
- `jurisdictional_context`
- `failure_classification.failure_mode_ids`
- `failure_classification.harm_vectors`
- `failure_classification.severity`
- `linked_records.proposals`
- `cam_internal.patch_status`

CAM-specific fields are available for maintainers but should not be required for a regulator, platform, UX reviewer, or robotics reviewer to understand the record.

## CAM internal routing

CAM maintainers should use `cam_internal.affected_instruments`, `cam_internal.affected_annexes`, `cam_internal.affected_domains`, `cam_internal.governance_layer`, `cam_internal.validator_or_automation_impact`, and `cam_internal.patch_status` to decide whether a VIGIL record should route to a doctrine patch, validator update, automation change, template revision, or downstream governance-interface update.

## Robotics compatibility

For robotics or embodied-agent records, set `system_context.embodiment_status` to `embodied` or a similarly precise value and add `robotics_context`. Capture robot class, mobility, actuation, physical environment, proximity to humans, safety boundary, human override availability, emergency stop availability, operator presence, physical harm potential, property harm potential, deployment environment, jurisdiction, and regulatory surface. Leave unknown values explicit rather than inferred.

## Automation notes

- Individual record files under `vigil/records/` are the source of truth.
- `python vigil/scripts/route-vigil-records.py` routes records into open, cluster, or closed folders.
- `python vigil/scripts/validate-vigil-records.py` validates individual records, v2 identity/link structure, and linked VIGIL IDs.
- `python vigil/scripts/build-vigil-records.py` generates aggregate JSON outputs.
- `vigil/VIGIL.ActiveRecords.json` is the canonical active/live aggregate for interface ingestion.
- `vigil/VIGIL.ClosedRecords.json` is the archival aggregate for closed records.
- `vigil/VIGIL.Records.Index.json` is the canonical lightweight global registry index.
- `vigil/VIGIL.Schema.v2.json` is the v2 source-data-first record schema.
- `vigil/VIGIL.Schema.json` remains a legacy-compatible schema used by the current validation script.
- `.github/workflows/vigil-records.yml` runs VIGIL validation/build automation in GitHub Actions.
- GitHub Pages or downstream interface publication beyond these generated files is to be confirmed.

## Duplicate or near-duplicate JSON outputs

This repository currently keeps multiple generated JSON outputs for compatibility:

- `VIGIL.ActiveRecords.json`: full active/open record aggregate, canonical for live/interface ingestion.
- `VIGIL.ClosedRecords.json`: full closed-record archive aggregate.
- `VIGIL.Records.Index.json`: lightweight global registry index, canonical for discovery and public indexing.

No `VIGIL.Records.json` legacy aggregate should exist; validation treats it as deprecated if reintroduced.
