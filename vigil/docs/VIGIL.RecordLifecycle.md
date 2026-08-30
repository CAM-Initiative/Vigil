# VIGIL Record Lifecycle and Routing Model

VIGIL is a public evidence-to-repair observatory. Its public record lifecycle preserves evidence, research, failure diagnosis, taxonomy classification, triage state, ecosystem state and CAM-side coverage/repair assessment without making VIGIL itself a source of CAM authority.

The lifecycle is **conditional, not mandatory**. A matter may begin as an OBS, FM or RESEARCH record depending on the evidence and analytical state.

## Publication boundary

Current public record classes are stored only under:

```text
vigil/records/observations/
vigil/records/failures/
vigil/records/research/
```

PROP, PATCH and LEARN records are currently withdrawn from publication and retained under `vigil/drafts/`. Public builders, validators, lifecycle checks and interfaces must not load or resolve those draft files.

Historical PROP/PATCH/LEARN identifiers may remain in the provenance of a public record where they document prior repository history. That does not make the retained draft target public or authoritative.

## OBS — Observation

OBS preserves a material unresolved governance proposition, early-warning signal, incident or system behaviour that is not already adequately represented by an existing FM or RESEARCH record.

An OBS should answer:

- what was observed;
- what evidence supports the observation;
- what system or deployment is implicated;
- why the proposition is governance-relevant;
- what remains uncertain; and
- what review or routing action comes next.

OBS must not contain full failure-mode diagnosis or triage merely because a source appears important. Evidence that only strengthens an existing FM belongs in that FM's `source_records`, not in a duplicative OBS.

## RESEARCH — Research Record

RESEARCH preserves substantive non-binding analysis that independently warrants publication and may supply evidence, comparison or synthesis for one or more VIGIL records.

A published RESEARCH record should answer:

- what question was examined;
- what method and source corpus were used;
- what findings and counter-evidence were identified;
- what limitations remain; and
- what governance significance follows without overstating authority.

Published RESEARCH must satisfy the quality contract in `vigil/VIGIL.Schema.json`.

Short, single-source or lightly synthesised material belongs in an existing record's `source_records` or, where it is a distinct unresolved proposition, in OBS.

## FM — Failure Mode

FM is the authoritative public diagnostic record for an ecosystem failure pattern.

An FM should answer:

- what failed;
- what threshold distinguishes the failure from adjacent behaviour;
- what evidence supports the diagnosis;
- how the case maps to the VIGIL Observatory failure taxonomy;
- what harms, interests, scope and recurrence characteristics are supported;
- what triage state applies now;
- whether the ecosystem failure remains active or recurring; and
- what CAM-side coverage or repair state has been established.

Failure-mode `failure_classification` contains event/case dimensions such as severity, likelihood, harm, scope, recurrence, persistence, reproducibility and visibility.

VIGIL-native taxonomy membership belongs in `taxonomy_classification`. Peer class membership is a taxonomy-layer relationship and must not be recreated through `linked_records.related_failure_modes`.

The canonical taxonomy is under `vigil/taxonomy/`. Historical CAM failure-taxonomy references do not override the current VIGIL taxonomy architecture.

## Public routing patterns

Common public routing patterns include:

```text
OBS -> FM
RESEARCH -> FM
OBS -> RESEARCH
FM -> monitoring
FM -> CAM coverage assessment
FM -> CAM repair assessment
```

A new source may also be added directly to an existing FM without creating another record.

No sequence is compulsory. An observation does not need to become a failure mode; a failure mode does not need a research record; and public VIGIL does not manufacture a proposal or patch record merely to make a chain look complete.

## Repair and coverage state

FM keeps CAM-side repair and ecosystem state separate.

- `repair_status` describes the CAM-side governance response.
- `corpus_coverage` records what current CAM/Caelestis corpus content was assessed and what coverage state was established.
- `ecosystem_status` describes whether the external failure remains active, recurring, improving, externally resolved or unknown.

A CAM-side repair does not prove that an external vendor/system has adopted the repair or that the ecosystem failure has ceased.

Historical patch IDs may remain in FM provenance where they document how a repair state was established. While PATCH files remain withdrawn under `vigil/drafts/`, public interfaces must not resolve those IDs as public records.

## Record state and triage state

`record_state` is the lifecycle state of the VIGIL record.

For failure modes, `triage.triage_status` is the operational workflow state and `triage.triage_priority` is the urgency of the next VIGIL/CAM action. Severity is a property of the failure; priority is not a proxy for severity.

`ecosystem_status.monitoring_required` is continuing external observation and does not itself justify an active P0–P3 queue priority.

Allowed values are controlled by `vigil/VIGIL.Schema.json` and enforced by the validators. Do not create alternative lifecycle/status vocabularies in documentation or interfaces.

## Source-evidence rule

For individual public records, `source_records` is the only canonical source-evidence block.

A source may be:

- external evidence;
- CAM-internal governance/provenance material; or
- VIGIL-internal record cross-reference provenance.

These residences and roles must remain explicit. VIGIL interpretive prose about an external source does not convert that external source into a VIGIL-internal source.

## Linked records

Links must preserve authority boundaries.

OBS, FM and RESEARCH may cross-reference other public records where the relevant schema permits it. A link does not automatically create a lifecycle transition, repair relationship, causal claim or taxonomy relationship.

Withdrawn PROP/PATCH/LEARN identifiers may appear as historical provenance but are intentionally non-resolvable while those classes remain under `vigil/drafts/`.

CAM instruments are not external standards. CAM/Caelestis identifiers belong in the appropriate `cam_internal` routing/coverage fields rather than being misrepresented as external standards references.

## Source of truth and generated indexes

Individual public record files under `vigil/records/` are the source of truth.

Current generated public indexes are:

```text
vigil/VIGIL.Failures.Index.json
vigil/VIGIL.Observations.Index.json
vigil/VIGIL.Research.Index.json
vigil/VIGIL.Registry.Index.json
```

Build them with:

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/enrich-vigil-indexes.py
```

Do not manually edit generated indexes and do not recreate withdrawn-class indexes as though those classes were public.

## Authority boundary

VIGIL records preserve evidence and analysis. They do not amend CAM/Caelestis instruments.

CAM authority arises only through the separate CAM/Caelestis governance, validation and adoption process. Repository housekeeping, schema changes, validators, migrations, index rebuilds and audit work are maintenance activity and do not create VIGIL PROP or PATCH authority.
