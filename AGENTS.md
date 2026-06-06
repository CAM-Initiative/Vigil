# VIGIL Agent Instructions

These instructions apply to the entire repository. More specific `AGENTS.md` files in subdirectories, including `vigil/AGENTS.md`, add local requirements for files under their scope.

## Repository purpose

VIGIL is a public evidence-to-repair ledger for AI ecosystem observations, failure modes, proposals, and patch notes.

VIGIL records are evidentiary records, not placeholders. They preserve source metadata, evidence posture, classification context, repair routing, and implementation history. VIGIL does not itself amend CAM/Caelestis doctrine.

## Required agent workflow

Before editing VIGIL records, agents must:

1. Inspect the relevant schema and validation files, especially `vigil/VIGIL.Schema.json` and `vigil/scripts/validate-vigil-records.py`.
2. Inspect one or more existing records of the same type under `vigil/records/`.
3. Use current repository conventions rather than inventing new fields, schemas, or record classes.
4. Preserve source evidence and evidence confidence unless a change is explicitly justified by stronger evidence.
5. Run validation before reporting completion.

When adding or changing records, use the current templates under `vigil/templates/` and current examples under `vigil/records/`.

## Validation and generated indexes

Run validation before completion:

```bash
python vigil/scripts/validate-vigil-records.py
```

When changing records, also run the current routing and index-generation workflow:

```bash
python vigil/scripts/route-vigil-records.py
python vigil/scripts/build-vigil-records.py
python vigil/scripts/validate-vigil-records.py
```

Generated indexes, including `vigil/VIGIL.Failures.Index.json`, `vigil/VIGIL.Observations.Index.json`, `vigil/VIGIL.Proposals.Index.json`, `vigil/VIGIL.PatchNotes.Index.json`, and `vigil/VIGIL.Registry.Index.json`, are derived outputs. Do not manually patch generated indexes to hide invalid source records.

## Evidence rules

Agents must:

* preserve `source_records` as the canonical source-evidence block;
* never remove source URLs unless they are proven invalid and replaced with a better locator;
* never fabricate URLs, dates, publishers, screenshots, source claims, legal claims, or evidence confidence;
* attempt evidence recovery before marking an external source as missing;
* distinguish external evidence from internal VIGIL, CAM/Caelestis, repository, private-note, field-observation, or ChatGPT-conversation locators;
* mark missing evidence clearly where recovery fails, including the recovery attempt in source context or audit notes;
* treat social-media reports, public-user reports, automated-search results, and third-party claims as provisional unless corroborated.

For detailed evidence metadata guidance, see `vigil/docs/evidence-authoring-guidance.md`.

## Multi Vendor rules

For `system_context`:

* `platform_or_vendor: "Multi Vendor"` requires a non-empty `vendor_cluster` array.
* `platform_or_vendor: "Multi Vendor"` requires a non-empty `primary_evidenced_vendors` array.
* `product_or_service` must be exactly one canonical allowed value.
* Use `product_or_service: "Other"` for genuinely multi-vendor / multi-product records unless one canonical product or service clearly controls the record.
* Put detailed product, model, surface, deployment, and incident claims in descriptive fields such as `interface_surface`, `model_or_product`, `deployment_context`, and `source_records`, not in comma-combined canonical fields.

`Multi Vendor` is valid only when more than one vendor/platform is actually supported by record evidence.

## Record-editing rules

Agents must:

* not create patch, proposal, failure-mode, or observation schemas from scratch;
* inspect existing examples first;
* update affected generated indexes by running the build script after record changes;
* not silently change substantive claims;
* not weaken evidence confidence without review;
* not collapse adjacent-but-distinct failure modes;
* not insert migration/process notes into final public records unless the schema explicitly requires them;
* not modify CAM/Caelestis instruments from a VIGIL maintenance task unless the user explicitly asks for CAM/Caelestis changes.

## Security rules

Agents must:

* avoid committing secrets, tokens, private keys, credentials, internal chat exports, or private user data;
* not expose private evidence as public evidence;
* not include sensitive platform-security details beyond what is necessary for governance analysis;
* flag suspected vulnerability or security issues for maintainer review;
* represent sensitive evidence with internal locators or redacted summaries where public disclosure would create risk.

See `SECURITY.md` for security handling and reporting guidance.

## Reporting format

At the end of an agent task, report:

* files changed;
* records changed;
* generated indexes updated;
* evidence recovered or still missing;
* validation result;
* remaining warnings;
* whether remaining warnings are pre-existing or introduced by the change.
