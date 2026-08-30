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

### Evidence source platform versus affected system

`source_platform` is **source provenance**: it identifies the platform, publication surface, repository, status page, social network, or other location through which the evidence is supplied. It does not, by itself, identify the AI/platform system affected by the failure. A TikTok video about ChatGPT therefore has `source_platform: "TikTok"` while the affected system remains OpenAI / ChatGPT.

Where an external source identifies an affected system, populate these structured fields as well:

* `system_or_product` — the affected platform, product, service, tool, or system stated by the evidence;
* `model_or_algorithm` — the affected model, runtime, algorithm, or model family where established.

These fields describe the affected system **established by that source**, not every system, provider, mitigation, comparator, or control discussed in the source. A source that supplies contextual or supplementary governance information without establishing that the discussed system suffered the Failure Mode should use the appropriate `source_role`, normally `contextual-background`; its discussed system must not thereby enter the Failure Mode affected-system projection.

Do not infer either field from the publisher or hosting platform. Where the evidence does not establish a model, use the existing bounded uncertainty convention rather than guessing.

For Failure Modes, detailed model/runtime names in `evidenced_models_or_runtimes`, `evidenced_systems`, and `specific_model_or_runtime` are intentionally open-ended. The compatibility summaries `platform_or_vendor` and `product_or_service` remain constrained to the controlled values admitted by the current schema. Do not expand those closed vocabularies merely to accommodate a newly evidenced model name; use the evidence-backed arrays for exact identities and `Multi Vendor`, `Other`, or another existing compatible summary where appropriate.

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

Keep `product_or_service` to one canonical compatibility value. For genuinely multi-vendor and multi-product records, use `product_or_service: "Other"` unless one canonical product clearly controls the record. Record the actual affected vendors/products/models in `system_or_product`, `model_or_algorithm`, and the FM evidence-backed system projection; do not use `source_platform` as a substitute.

## Published research quality

A RESEARCH record is a substantive analytical artefact, not a container for a report summary. Before setting `publication_status: "published"`, the record must:

* answer a bounded research question;
* describe its scope, source-selection method and exclusions;
* present findings with claim-level links;
* preserve counter-evidence and alternative explanations;
* state evidence, access, measurement and generalisation limitations;
* distinguish governance implications from adopted CAM doctrine;
* identify open questions;
* provide a public bibliography and structured `source_corpus`; and
* qualify the basis of `corroborated` where all evidence comes from one institutional publisher.

The validator enforces a minimum floor for structure, length and source traceability. Those checks do not prove research quality. Human editorial review and substantive comparison of claims against the cited sources remain necessary.

Short single-source material should normally be added to the `source_records` of the record it evidences. Use an OBS only where the material establishes a distinct unresolved governance proposition. Do not create RESEARCH merely to raise the apparent status of a source note.

## Related guidance and audit material

See also:

* `vigil/docs/audits/records/2026-evidence-integrity-audit.md`
* `vigil/MAINTAINERS.md`
* `vigil/AGENTS.md`
* root `AGENTS.md`
* `CONTRIBUTING.md`
* `SECURITY.md`
