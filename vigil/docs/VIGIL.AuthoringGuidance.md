# VIGIL Authoring Guidance

VIGIL records are evidentiary records. Do not treat source blocks as placeholders: external claims should be supported by source metadata whenever a source can reasonably be recovered.

## Multi Vendor system-context requirements

Use `"platform_or_vendor": "Multi Vendor"` only when the record is genuinely supported by evidence from more than one vendor or platform.

When `platform_or_vendor` is `Multi Vendor`, the record must also include:

```json
"vendor_cluster": [
  "OpenAI",
  "Anthropic"
],
"primary_evidenced_vendors": [
  "OpenAI",
  "Anthropic"
]
```

Authoring rules:

* `platform_or_vendor: "Multi Vendor"` is valid only when evidence records substantiate more than one vendor or platform.
* `vendor_cluster` must be a non-empty array of non-empty vendor/platform names.
* `primary_evidenced_vendors` must be a non-empty array of non-empty vendor/platform names that are directly evidenced by `source_records`.
* `product_or_service` must contain exactly one canonical allowed value.
* Do not place comma-separated product lists into `product_or_service`.
* If a record spans multiple products/services across vendors, set `product_or_service` to `Other` unless a single canonical value clearly controls the record.
* Put specific vendor, product, surface, model, deployment, and incident details in descriptive fields such as `interface_surface`, `model_or_product`, `deployment_context`, and `source_records`, not in canonical database fields.

Example Multi Vendor block:

```json
"system_context": {
  "platform_or_vendor": "Multi Vendor",
  "vendor_cluster": [
    "OpenAI",
    "Anthropic"
  ],
  "primary_evidenced_vendors": [
    "OpenAI",
    "Anthropic"
  ],
  "product_or_service": "Other",
  "interface_surface": "Multiple evidenced access surfaces; specify details in source_records and deployment_context."
}
```

### Rationale

Multi-vendor records require separated vendor evidence because top-level database fields are controlled values for indexing, filtering, validation, and UI routing. Detailed vendor, product, surface, and source claims belong in evidence metadata, not comma-combined canonical fields.

## Evidence integrity

Before marking an external source as missing, attempt reasonable evidence recovery through repository history, linked records, referenced titles, publishers, usernames, platform status pages, public documentation, public reporting, public social-media/forum posts, archives, related VIGIL records, and repository notes.

If a high-confidence source is recovered, write it back into `source_records` with a usable URL, retrieval date, source type, source context, and relevance note. If no unique source can be recovered, keep the evidence gap visible with `source_url_status: "missing_url_requires_research"` and document the recovery attempt.

See `vigil/docs/2026-evidence-integrity-audit.md` for the 2026 OBS/FM evidence-integrity audit and recovery outcomes.


## Related guidance

For detailed source metadata conventions, source URL status conventions, evidence recovery, internal evidence handling, and Multi Vendor evidence handling, see `vigil/docs/evidence-authoring-guidance.md`.
