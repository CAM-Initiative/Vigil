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

Edit individual JSON files in `vigil/records/` rather than editing the generated aggregate directly:

- active observations and proposals belong in `vigil/records/open/`;
- cluster records belong in `vigil/records/clusters/`;
- closed or actioned records should move to `vigil/records/closed/`.

Each individual record file contains exactly one JSON object. Use a filename that matches the record ID, such as `vigil/records/open/VIGIL-OBS-2026-0001.json`.

Validate records before rebuilding the aggregate:

```bash
python vigil/scripts/validate-vigil-records.py
```

Rebuild the generated catalogue/interface aggregate after record changes:

```bash
python vigil/scripts/build-vigil-records.py
```

`vigil/VIGIL.Records.json` is generated from `vigil/records/` for public catalogue/interface use and should not be manually edited during normal record work.

## Foundation Files

- `VIGIL.Register.md` is the human-readable register for open, clustered, proposal, and closed records.
- `VIGIL.Schema.json` defines the minimal JSON structure for VIGIL records.
- `VIGIL.Records.json` is a generated aggregate for catalogue/interface use; edit individual record files instead.
- `examples/VIGIL.Record.Template.md` provides a copy/paste Markdown template for new observations.
- `templates/` contains specialised Markdown templates for each supported record type.
- `AGENTS.md` gives local instructions for agents working inside the VIGIL layer.

TODO: Add VIGIL as a public catalogue/workflow layer in the CAM governance interface once the catalogue ingestion path is confirmed.
