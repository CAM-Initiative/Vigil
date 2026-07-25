# VIGIL

**VIGIL** is a public evidence-to-repair governance ledger for AI system observations, failure modes, proposals, patch notes, and related governance records.

VIGIL records what has been seen, why it may matter, how it is being classified, and whether it has been routed toward monitoring, proposal development, repair, implementation, supersession, or closure.

It is the public watchstanding layer for CAM-adjacent observations, unresolved governance questions, runtime failure signals, and development proposals.

VIGIL does **not** create binding CAM doctrine by itself. It preserves evidence, classification context, routing state, source attribution, and repair history so that CAM governance work can proceed from structured public records rather than scattered observations.

---

## Purpose

VIGIL exists to support a public evidence-to-repair workflow:

1. observe AI system behaviour, governance gaps, platform signals, or emerging risk patterns;
2. classify observations into failure modes where appropriate;
3. propose governance, schema, interface, taxonomy, or operational changes;
4. record implemented patches or repair actions;
5. preserve the source trail and lifecycle state of each record.

VIGIL is designed to make governance maintenance visible, reviewable, and traceable.

For the detailed conditional lifecycle/routing model and OBS/RESEARCH/FM/PROP/PATCH record-class boundaries, see [`vigil/docs/VIGIL.RecordLifecycle.md`](vigil/docs/VIGIL.RecordLifecycle.md).

For contributor, security, agent, and evidence-authoring guidance, see:

* [`AGENTS.md`](AGENTS.md)
* [`CONTRIBUTING.md`](CONTRIBUTING.md)
* [`SECURITY.md`](SECURITY.md)
* [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
* [`vigil/docs/evidence-authoring-guidance.md`](vigil/docs/evidence-authoring-guidance.md)
* [`vigil/docs/2026-evidence-integrity-audit.md`](vigil/docs/2026-evidence-integrity-audit.md)

---

## What VIGIL Records

VIGIL currently supports the following record types:

1. **Observations**
   Public or reviewable observations of AI system behaviour, platform activity, governance gaps, emerging technology signals, or other relevant events.

2. **Failure Modes**
   Structured records identifying recurring or significant patterns of failure, risk, instability, harm, governance breakdown, or runtime concern.

3. **Proposals**
   Records proposing changes to CAM instruments, taxonomies, schemas, validators, workflows, interface components, or governance interpretation.

4. **Patch Notes**
   Records of implemented changes, repairs, registry updates, interface fixes, validator changes, schema changes, or other governance-maintenance actions.

5. **Research / Supporting Records**
   Non-binding research artefacts that may originate an evidence-to-repair chain in place of, or alongside, an observation and link directly to the relevant failure mode, proposal, or patch.

---

## Principles

VIGIL operates under the following principles:

* VIGIL records what has been observed, what may require review, and what is being worked on.
* VIGIL does not create binding CAM doctrine.
* VIGIL does not amend adopted CAM instruments.
* VIGIL does not determine liability, fault, or final factual truth.
* VIGIL preserves source attribution, dates, confidence state, and routing context.
* VIGIL treats public, social, news, automated, or preliminary signals as provisional unless corroborated.
* VIGIL distinguishes evidence, interpretation, classification, proposal, and implementation.
* VIGIL keeps authoritative repair chains narrow: one primary failure mode per proposal or PATCH by default.
* Contextual links remain visible but are non-transitive and never imply that records were repaired together.
* Multi-failure PATCHes are exceptional and require a rationale plus separate verification for each failure.
* VIGIL supports review, repair, monitoring, supersession, and closure without assuming that every observation requires amendment.
* CAM amendment, classification, harmonisation, and closure remain governed by existing CAM instruments, including relevant OPERATIONS instruments and failure-taxonomy materials.

---

## Record Lifecycle

VIGIL records move through a lifecycle model rather than a simple open/closed folder structure.

Common lifecycle paths include:

```text
Observation → Failure Mode → Patch Note → Resolved / Inactive
Observation → Proposal → Patch Note → Implemented
Failure Mode → Monitoring / Superseded / Inactive
```

The lifecycle is recorded through fields such as:

* `record_type`
* `record_state`
* `linked_records`
* `cam_internal`
* `triage`
* `next_action`
* `migration_notes`

Record state belongs **inside the JSON record**, not in the filesystem path.

This allows records to remain stable even when their status changes.

---

## Record States

VIGIL records may use states such as:

* `watching`
* `active`
* `under review`
* `routed`
* `deferred`
* `monitoring`
* `implemented`
* `superseded`
* `inactive`
* `closed-no-action`
* `closed-actioned`

The exact allowed values may be enforced by the validator and schema.

A record state indicates current handling, not final truth.

---

## Source of Truth

The source of truth is the set of individual JSON record files under:

```text
vigil/records/
```

Records are organised by record type and year:

```text
vigil/records/
  failures/
    2026/
  observations/
    2026/
  proposals/
    2026/
  patches/
    2026/
  research/
    2026/
```

Each individual record file contains exactly one JSON object.

The filename must match the record ID, for example:

```text
vigil/records/failures/2026/VIGIL-2026-FM-0005.json
vigil/records/observations/2026/VIGIL-2026-OBS-0001.json
vigil/records/proposals/2026/VIGIL-2026-PROP-0001.json
vigil/records/patches/2026/VIGIL-2026-PATCH-0001.json
```

Generated registry files must not be manually edited.

---

## Generated Registry Files

VIGIL generates type-specific registry indexes and a master registry index.

Generated files include:

```text
vigil/VIGIL.Failures.Index.json
vigil/VIGIL.Observations.Index.json
vigil/VIGIL.Proposals.Index.json
vigil/VIGIL.PatchNotes.Index.json
vigil/VIGIL.Research.Index.json
vigil/VIGIL.Registry.Index.json
```

The type-specific indexes are generated from the individual record files.

The master registry index is generated from the type-specific indexes.

These generated files support the public interface layer and should be treated as derived outputs.

Deprecated generated files should not be recreated or manually maintained:

```text
vigil/VIGIL.ActiveRecords.json
vigil/VIGIL.ClosedRecords.json
vigil/VIGIL.Records.Index.json
vigil/VIGIL.Records.json
```

---

## Record Workflow

After creating or editing an individual record, run the VIGIL workflow scripts.

Route misplaced records where applicable:

```bash
python vigil/scripts/route-vigil-records.py
```

Validate individual records:

```bash
python vigil/scripts/validate-vigil-records.py
```

Rebuild generated registry indexes:

```bash
python vigil/scripts/build-vigil-records.py
```

Generated registry outputs should be rebuilt after record changes.

If validation fails, fix the individual source record rather than editing the generated index.

---

## Record Links and Interface Consumption

Generated registry entries include source-path metadata so external interfaces do not need to guess file locations.

Registry entries may include:

* `path`
* `github_blob_url`
* `raw_url`

The CAM interface layer should consume the generated registry files and use these URLs directly.

The interface should not hard-code old record paths or deprecated registry filenames.

---

## Clustering and Pattern Recognition

VIGIL supports clustering because multiple observations may disclose a single governance pattern.

A cluster may later become:

* a failure mode;
* a proposal;
* a candidate amendment;
* a patch note;
* a monitoring item;
* a superseded record; or
* no action after review.

VIGIL does not assume a one-to-one relationship between observations and amendments.

---

## Evidence Confidence

VIGIL records may use evidence-confidence values to distinguish source reliability, corroboration, and review posture.

Common values may include:

* `observed`
* `verified`
* `corroborated`
* `to be assessed`

The validator may enforce the exact allowed values.

Evidence confidence should describe the evidentiary posture of the record, not the emotional or political significance of the issue.

---

## Foundation Files

Key repository files include:

* `VIGIL.Register.md` — human-readable register and overview material.
* `VIGIL.Schema.json` — schema or schema reference for VIGIL records.
* `vigil/records/` — individual source-of-truth JSON records.
* `vigil/VIGIL.Registry.Index.json` — generated master registry index.
* `vigil/VIGIL.Failures.Index.json` — generated failure-mode index.
* `vigil/VIGIL.Observations.Index.json` — generated observation index.
* `vigil/VIGIL.Proposals.Index.json` — generated proposal index.
* `vigil/VIGIL.PatchNotes.Index.json` — generated patch-note index.
* `vigil/VIGIL.Research.Index.json` — generated research-artifact index.
* `templates/` — specialised templates for supported record types.
* `examples/` — example records or copy/paste templates.
* `vigil/scripts/` — routing, validation, and registry-generation scripts.
* `AGENTS.md` — repository-root instructions for AI/code agents.
* `vigil/AGENTS.md` — additional local instructions for agents working inside the VIGIL layer.
* `CONTRIBUTING.md` — contribution workflow and evidence requirements.
* `SECURITY.md` — security and sensitive-evidence handling.
* `CODE_OF_CONDUCT.md` — participation and privacy expectations.
* `vigil/docs/evidence-authoring-guidance.md` — source metadata, evidence recovery, internal evidence, and Multi Vendor evidence guidance.
* `vigil/docs/2026-evidence-integrity-audit.md` — 2026 OBS/FM evidence-integrity audit and recovery outcomes.

---

## Relationship to CAM

VIGIL is CAM-adjacent but not itself binding constitutional doctrine.

It supports CAM maintenance by preserving evidence, failure signals, proposals, and repair history in a structured public format.

Formal CAM amendment, adoption, classification, harmonisation, and closure remain governed by the relevant CAM instruments.

VIGIL may route issues toward CAM domains, including but not limited to:

* AEON
* OPERATIONS
* RELATION
* IDENTITY
* CONTINUITY
* SECURITY
* ECONOMICS
* ETHICS
* LATTICE
* MENTIS

---

## Licence and Reuse

VIGIL is publicly accessible for citation, research, journalism, policy analysis, and non-commercial governance use with attribution.

Unless otherwise stated, VIGIL record text, summaries, schema documentation, and public-facing governance notes are licensed under **CC BY-NC-SA 4.0**.

Commercial use, bulk extraction, dataset reconstruction, model-training use, or integration into paid products requires prior written permission from Aeon Governance Lab.

See [LICENSE.md](./LICENSE.md).
