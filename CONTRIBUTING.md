# Contributing to VIGIL

Thank you for helping maintain VIGIL.

VIGIL is a public evidence-to-repair governance ledger for AI ecosystem observations, failure modes, proposals, and patch notes. Contributions should improve the accuracy, traceability, evidence quality, schema consistency, or lifecycle state of VIGIL records.

## Contribution types

Useful contributions include:

* new observation records for public or reviewable AI ecosystem signals;
* new or revised failure-mode records where a pattern is confirmed, strongly evidenced, recurring, or sufficiently clear for triage;
* proposal records for VIGIL/CAM-adjacent governance, taxonomy, schema, validator, or workflow changes;
* patch-note records for implemented changes;
* evidence recovery for existing source gaps;
* metadata corrections that preserve the substantive claim;
* documentation, templates, validator, routing, and generated-index maintenance.

Avoid broad drive-by schema changes. If a schema or validator change is needed, explain the record or workflow failure it repairs and update templates/docs consistently.

## Evidence requirements

VIGIL records are evidentiary records, not placeholders. Observations and failure modes must preserve the evidence trail in `source_records`.

For external sources, provide as much source metadata as possible:

* source title or clear description;
* author, publisher, platform, or account name;
* source date or observation date;
* source URL;
* archive URL, if available;
* retrieved date;
* source type;
* source platform;
* deployment context;
* source context;
* source URL status;
* relevance note explaining how the source supports the record.

External contributors should provide URLs, dates, publisher/platform information, screenshots only where lawful and appropriate, and relevance notes. Do not submit fabricated URLs, fabricated dates, invented publisher information, or unverified screenshots.

If an external source is referenced but not yet located, attempt evidence recovery before marking it missing. Search repository history, linked records, referenced usernames, publishers, titles, status pages, public reports, archives, and related records. If recovery fails, keep the gap visible and document the recovery attempt.

Internal evidence, including VIGIL records, CAM/Caelestis instruments, repository notes, private notes, field observations, local files, and ChatGPT conversations, must not be represented as external public evidence.

## Proposing records

Before proposing a new record:

1. Inspect the relevant template under `vigil/templates/`.
2. Inspect one or more existing records of the same type under `vigil/records/`.
3. Preserve record-class boundaries:
   * OBS records preserve early source signals and should not contain failure-mode triage.
   * FM records classify confirmed or strongly evidenced failure patterns.
   * PROP records propose governance, schema, taxonomy, validator, interface, or workflow repairs.
   * PATCH records only record implemented changes.
4. Use the next appropriate sequential ID for the record type/year and preserve existing record IDs.
5. Keep `source_records` as the canonical source-evidence block.
6. Do not add `source_data` or flatten evidence into a single URL field.

## Multi Vendor records

Use `platform_or_vendor: "Multi Vendor"` only when more than one vendor/platform is evidenced.

Multi Vendor records must include non-empty `vendor_cluster` and `primary_evidenced_vendors` arrays. `product_or_service` must contain one canonical value only. Do not put comma-separated product lists into `product_or_service`; use `Other` for genuinely multi-vendor / multi-product records unless a single canonical product clearly controls the record. Put detailed product and surface claims in descriptive fields and source-level metadata.

## Validation

Run validation before submitting changes:

```bash
python vigil/scripts/validate-vigil-records.py
```

For record changes, run the full record workflow:

```bash
python vigil/scripts/route-vigil-records.py
python vigil/scripts/build-vigil-records.py
python vigil/scripts/validate-vigil-records.py
```

If validation fails, fix the source record or template rather than manually editing generated indexes.

## Pull request expectations

A contribution should state:

* which files and records changed;
* what evidence was added, recovered, or remains missing;
* whether generated indexes were rebuilt;
* validation command output;
* any remaining warnings and whether they are pre-existing or introduced.

Do not modify CAM/Caelestis instruments as part of a VIGIL maintenance contribution unless the task explicitly asks for those changes.
