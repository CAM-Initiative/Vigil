# VIGIL Evidence Authoring Guidance

VIGIL records are evidentiary records, not placeholders. Source metadata should allow a maintainer, reviewer, journalist, researcher, or downstream governance process to understand what evidence supports a record and how strongly it supports the claim.

## Required source metadata for external sources

For external sources, records should include:

* `source_title`
* `author_or_publisher`
* `source_date`
* `source_url`
* `archive_url`, if available
* `retrieved_date`
* `source_type`
* `source_platform`
* `deployment_context`
* `source_context`
* `source_url_status`
* `relevance_note`

Use `source_records` as the canonical evidence block. Do not add `source_data`, `source_data.sources`, or flattened one-off URL fields to individual records.

## Source URL status conventions

The current validator does not enforce a closed enum for `source_url_status`, but repository practice uses clear descriptive values. Prefer these conventions:

* `available` — URL is present and usable.
* `recovered` — URL was located during an evidence-recovery pass and added to the record.
* `archived` — archive URL is the main stable locator or supplements the source URL.
* `partial` — evidence is partially locatable but incomplete.
* `unavailable` or `not available` — source is known but no longer available.
* `missing_url_requires_research` — source is external/public but no unique usable URL has been recovered.
* `not applicable` — source is an internal linked VIGIL/CAM/repository/governance locator or otherwise not a public external URL.
* `local / pending canonical repository confirmation` or similar local-status text — source is repository-local or staged and awaiting canonical public locator confirmation.

Do not invent a new status when an existing clear convention fits. If a status needs to be added for a new workflow, update documentation, templates, and validation expectations together.

## Evidence recovery before marking a gap

Before marking an external source as missing, attempt reasonable evidence recovery. Recovery may include searching:

* repository history;
* linked VIGIL records;
* referenced usernames, publishers, article titles, incident names, and organisations;
* platform status pages;
* public documentation;
* public news reports;
* public social-media, forum, or video posts;
* web archives;
* related records, notes, and discussions.

If a unique or high-confidence source is recovered, update the source record with the recovered URL, source metadata, retrieval date, `source_url_status: "recovered"`, source context, and relevance note.

If multiple candidate sources exist and confidence is insufficient, do not guess. Keep `source_url` blank, use `source_url_status: "missing_url_requires_research"`, and document candidate sources or the failed recovery attempt in the audit report or source context.

Never fabricate URLs, dates, publishers, screenshots, quotes, source context, or relevance notes.

## Internal evidence handling

Internal evidence includes:

* internal VIGIL records;
* CAM/Caelestis instruments;
* repository notes and local files;
* ChatGPT conversations or private governance discussions;
* private notes and field observations;
* maintainer-provided material that is not publicly accessible.

Internal evidence should remain internal. Do not represent it as external public evidence. Use the best available internal locator, mark `source_url_status` as `not applicable` or a clear local-status value, and avoid exposing private content, credentials, private user data, or sensitive platform-security details.

## Multi Vendor evidence handling

`platform_or_vendor: "Multi Vendor"` is valid only when source evidence supports more than one vendor or platform. Multi Vendor records must include non-empty `vendor_cluster` and `primary_evidenced_vendors` arrays.

Keep `product_or_service` to one canonical value. For genuinely multi-vendor and multi-product records, use `product_or_service: "Other"` unless one canonical product clearly controls the record. Put specific product, model, surface, and incident claims in descriptive fields and source-level metadata.

## Related audit material

See also:

* `vigil/docs/2026-evidence-integrity-audit.md`
* `vigil/docs/VIGIL.AuthoringGuidance.md`
* root `AGENTS.md`
* `CONTRIBUTING.md`
* `SECURITY.md`
