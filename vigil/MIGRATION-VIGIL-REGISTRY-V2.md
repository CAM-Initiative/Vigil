# VIGIL Registry v2 Migration Note


## Audit findings

The v2 migration audited these repository-local VIGIL files and consumers:

- Individual source records: `vigil/records/open/*.json`.
- Research note: `vigil/records/research/VIGIL-2026-RESEACH-001.md` (not a generated JSON source record and not migrated in this pass).
- Legacy-compatible schema: `vigil/VIGIL.Schema.json`.
- V2 schema: `vigil/VIGIL.Schema.v2.json`.
- Templates: `vigil/templates/*.md` and new v2 JSON templates under `vigil/templates/`.
- Generated JSON: `vigil/VIGIL.ActiveRecords.json`, `vigil/VIGIL.ClosedRecords.json`, and `vigil/VIGIL.Records.Index.json`.
- Registry scripts: `vigil/scripts/route-vigil-records.py`, `vigil/scripts/validate-vigil-records.py`, and `vigil/scripts/build-vigil-records.py`.
- Automation workflow: `.github/workflows/vigil-records.yml`.
- Existing maintainer instructions: `vigil/AGENTS.md`.

No existing records were deleted. Near-duplicate generated JSON outputs are preserved because they have distinct compatibility roles: active/live aggregate, closed/archive aggregate, and lightweight global index.

## Why VIGIL is changing

VIGIL is moving from a CAM-document-first registry shape to a source-data-first registry shape. The old structure made CAM mappings and affected instruments highly visible, which was useful for internal governance work but less suitable for public observation records, external ingestion, reusable failure-mode classification, robotics or embodied-system records, and regulator-facing analysis.

The v2 structure keeps CAM routing data, but it makes the public canonical record flow:

```text
OBS → FM → PROP → CAM Patch Queue
```

## CAM instruments remain important but are no longer the primary public classification layer

Affected CAM instruments, annexes, domains, validators, automations, templates, and interfaces remain important in `cam_internal`. They are used for routing and patch work. They should not be the primary way an external reader understands an observation. External readers should be able to start with source evidence, system context, jurisdictional context, failure modes, harm vectors, severity, linked proposals, and patch status.

## OBS, FM, PROP, and Patch Queue relationship

- `observation` records preserve source evidence and describe what was observed.
- `failure_mode` records are reusable classification objects, not tags.
- `proposal` records preserve repair logic, governance notes, and candidate changes.
- `patch` records represent downstream CAM patch queue routing.
- `crosswalk` records may map VIGIL records to external taxonomies, legal/regulatory categories, standards, or CAM-internal structures.

The chain may be partial. Observations can exist without proposals. Proposals can exist without observations. Observations may link one or more failure modes. Proposals may link observations and/or failure modes. Patch queue routing should be explicit and machine-readable through `linked_records` and `cam_internal`.

## Robotics and embodied-system compatibility

The v2 schema includes optional `robotics_context` fields. Non-robotics records do not need these fields. Robotics or embodied-agent records should use both `system_context` and `robotics_context` to capture embodiment status, robot class, mobility, actuation, physical environment, proximity to humans, safety boundary, human override, emergency stop, operator presence, physical harm potential, property harm potential, deployment context, jurisdiction, and regulatory surface.

## Legacy fields preserved for compatibility

The migration is additive. Existing flat fields such as `id`, `record_type`, `status`, `date_recorded`, `summary`, `why_it_matters_to_CAM`, `evidence_confidence`, `source_records`, `possible_CAM_mapping`, `affected_domains`, `affected_instruments`, `platform`, `system_or_product`, `model_or_algorithm`, `deployment_context`, `failure_mode`, `failure_family`, `candidate_amendment_id`, and `related_record_ids` are preserved where present.

Records now also include v2 blocks such as `record_identity`, `source_data`, `system_context`, `jurisdictional_context`, `failure_classification`, `linked_records`, and `cam_internal`. `legacy_record_type` preserves the former record type where the top-level `record_type` has been moved to a first-class v2 value.

Uncertain mappings were preserved with explicit migration notes instead of invented facts. For example, legacy `candidate_amendment_id` values are preserved as candidate patch references unless a VIGIL proposal link is explicitly known.

## Future authoring guidance

Future records should be authored from the relevant v2 template:

- `templates/observation-record.json`
- `templates/failure-mode-record.json`
- `templates/proposal-repair-record.json`
- `templates/patch-queue-record.json`
- `templates/robotics-observation-extension.json`

Author observations as source-data-first records. Reuse an existing failure mode when it fits. Create a new failure mode only when the existing classification set is insufficient. Create proposals only when there is repair logic. Create patch queue items only when there is concrete CAM routing. Keep CAM routing in `cam_internal`.

## Generated JSON files

The source of truth remains individual record files under `vigil/records/`. Generated outputs are rebuilt with `python vigil/scripts/build-vigil-records.py`.

- `VIGIL.ActiveRecords.json` is the canonical active/live aggregate for interface ingestion.
- `VIGIL.ClosedRecords.json` is the canonical closed-record archive aggregate.
- `VIGIL.Records.Index.json` is the canonical lightweight global index.

All three remain for compatibility. Do not delete near-duplicate generated outputs until downstream consumers have migrated.

## Downstream interface changes required later

Downstream CAM Interface work should later consume `record_identity`, `source_data`, `system_context`, `jurisdictional_context`, `failure_classification`, `linked_records`, and `cam_internal` directly. The interface should stop assuming CAM affected instruments are the primary public classification. It should support partial chains such as `OBS only`, `OBS → FM`, `PROP only`, and `PROP → CAM Patch Queue`, and should expose robotics context only when relevant.
