# VIGIL

VIGIL is a minimal public observation and workflow visibility layer for CAM-adjacent review activity. It records:

1. emerging technology / industry signals;
2. failure-mode observations;
3. clusters of related observations; and
4. development and expansion proposals.

> VIGIL is the public watchstanding layer for CAM-adjacent observations, failure signals, unresolved governance questions, and development proposals. It records what has been seen, why it may matter, how it is being classified, and whether it has been routed, clustered, deferred, actioned, or closed.

## Principles

- VIGIL records what has been observed, what may require review, and what is being worked on.
- VIGIL does not create binding CAM doctrine.
- VIGIL does not amend adopted instruments.
- VIGIL does not determine liability, fault, or final factual truth.
- VIGIL preserves source attribution, dates, confidence state, and routing context.
- VIGIL records public/social/news/automated signals as provisional unless corroborated.
- CAM amendment, classification, harmonisation, and closure remain governed by existing CAM instruments, especially OPERATIONS-005 and OPERATIONS-003-SUP-01.

## Clustering

VIGIL supports clustering because multiple observations may disclose a single governance pattern. A cluster may later become one proposal, one candidate amendment, one taxonomy expansion, or no action after review. VIGIL does not assume a one-to-one relationship between observations and amendments.

## Record Workflow

The source of truth is the set of individual JSON record files in `vigil/records/`; generated aggregates must not be manually edited. Route records by status/type before validating or rebuilding:

- active observations and proposals belong in `vigil/records/open/`;
- cluster records belong in `vigil/records/clusters/`;
- closed or actioned records are moved to `vigil/records/closed/` by `vigil/scripts/route-vigil-records.py`.

Each individual record file contains exactly one JSON object, not an aggregate wrapper. Use a filename that matches the record ID, such as `vigil/records/open/VIGIL-OBS-2026-0001.json`.

Route records after status changes:

```bash
python vigil/scripts/route-vigil-records.py
```

Validate records before rebuilding the aggregates:

```bash
python vigil/scripts/validate-vigil-records.py
```

Rebuild generated records after record changes:

```bash
python vigil/scripts/build-vigil-records.py
```

Generated outputs:

- `vigil/VIGIL.ActiveRecords.json` is generated from open and cluster records for interface/live ingestion.
- `vigil/VIGIL.ClosedRecords.json` is generated from closed records for archival use.
- `vigil/VIGIL.Records.Index.json` is the lightweight global registry across all records.
- `vigil/VIGIL.Records.json` remains a temporary backwards-compatible aggregate of all records.

## Foundation Files

- `VIGIL.Register.md` is the human-readable register for open, clustered, proposal, and closed records.
- `VIGIL.Schema.json` defines the minimal JSON structure for VIGIL records.
- `VIGIL.ActiveRecords.json` is a generated active-record aggregate for interface/live ingestion.
- `VIGIL.ClosedRecords.json` is a generated archival aggregate for closed records.
- `VIGIL.Records.Index.json` is a generated lightweight global registry.
- `VIGIL.Records.json` is a temporary backwards-compatible generated aggregate; edit individual record files instead.
- `examples/VIGIL.Record.Template.md` provides a copy/paste Markdown template for new observations.
- `templates/` contains specialised Markdown templates for each supported record type.
- `AGENTS.md` gives local instructions for agents working inside the VIGIL layer.

TODO: Add VIGIL as a public catalogue/workflow layer in the CAM governance interface once the catalogue ingestion path is confirmed.
