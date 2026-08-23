# VIGIL Draft Records

This directory contains retained VIGIL working records that are **not part of the public canonical record registry**.

The following record classes are currently withdrawn from publication while their design, schema, content and public-interface role are under review:

- `proposals/`
- `patches/`
- `learn/`

Existing record identifiers and file contents are preserved. Draft records are excluded from the canonical source tree under `vigil/records/` and therefore from generated public registry indexes.

Public validators, lifecycle checks, triage audits, registry builders and interface consumers **must not load or resolve records from `vigil/drafts/`**. A retained draft identifier may remain as historical text in an existing public record, but its target is intentionally non-resolvable while the record class is withdrawn.

Do not treat presence in this directory as publication, adoption, implementation authority, validated repair, or validated learning closure.
