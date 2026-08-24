# VIGIL Failure Taxonomy — Technical Standard

This directory contains a portable, machine-readable technical reference for AI-governance failure mechanisms. It is separate from incident, severity, harm, evidence-confidence, triage, jurisdiction, vendor, repair-state, and other event metadata.

## Architecture

```text
VIGIL.FailureTaxonomy.Index.json
VIGIL.FailureTaxonomy.Schema.json
families/
  VIGIL-FF-0001-authority-boundary-integrity.json
  VIGIL-FF-0002-provenance-lineage-integrity.json
  VIGIL-FF-0003-verification-completion-integrity.json
  VIGIL-FF-0004-observability-audit-integrity.json
generated/
  one complete HTML page per family
  VIGIL.FailureTaxonomy.FullReference.html
migration/
  Caelestis.LegacyFailure.MigrationLedger.json
  Caelestis.LegacyFailure.InventoryReview.md
```

Family JSON is canonical. HTML and Markdown references are generated projections. The migration ledger is non-normative source-analysis evidence and is not a dependency of the portable taxonomy.

## Taxonomic boundary

A family is admissible only when every child can coherently complete:

> Every class in this family is a way in which **the same bounded structural invariant** fails.

Broad organisational containers such as governance, UX, safety, security, or AI-system failure are not families merely because failures can appear there. A candidate family normally requires a bounded invariant, meaningful inclusion and exclusion rules, at least two distinct mechanisms absent a compelling singleton case, and independence from vendor, framework, locus, governor, harm, and severity.

The hierarchy is:

**Failure Taxonomy → Failure Family → Failure Class → Variant where justified**

One JSON file contains one bounded family. Classes and variants remain inside that file.

## Immutable identity and semantic codes

Identity is independent from naming:

- family IDs use `VIGIL-FF-NNNN`;
- class IDs use `VIGIL-FC-NNNNNN`;
- `family_code` and `class_code` are human-readable semantic codes;
- relationships target immutable class IDs;
- prior public codes remain in `aliases`;
- optional `supersession` metadata records controlled deprecation.

IDs survive renaming. A class ID also survives movement between families. Semantic codes may change in a controlled taxonomy revision. A class identity must never be computed from its current family, code, filename, filesystem order, or array position.

### Allocation rules

1. Allocate the next unused numeric ID from the catalogue-wide sequence.
2. Record the ID in the family file and index before public use.
3. Never reuse, renumber, or silently recycle an allocated ID.
4. When an entity is removed, reserve its ID in index `removed_ids`.
5. Preserve prior semantic codes in `aliases` after renaming.
6. Use `supersession` only for an explicit deprecated-to-successor transition; do not change identity for an ordinary rename or family move.
7. Allocate an ID only after the proposed concept has passed its abstraction and boundary review.

Family filenames use `<family_id>-<human-readable-slug>.json`. The immutable ID provides durable location identity; the slug aids readers. The generated index resolves current locations. Filesystem position and alphabetical order carry no taxonomic meaning, and nested domain directories are not used.

## Family and class content

Every family defines its immutable ID, semantic code, canonical name, version, status, abstraction, plain-English explanation, technical definition, governing invariant, scope, inclusion rule, exclusion rule, aliases, and allowed class IDs/codes.

Every class or variant defines its immutable ID, semantic code, current family ID, canonical name, abstraction, status, plain-English explanation, technical definition, recognition criteria, exclusions, examples, aliases, typed relationships where relevant, and optional external mappings or supersession metadata.

Definitions must not contain incident-specific values. Severity, harm, persistence, reproducibility, visibility, incident status, evidence confidence, jurisdiction, vendor/model, manifestation, locus, repair side, propagation, observability state, evidence state, and repair status remain orthogonal event dimensions.

## Relationships

Supported relationship types are `child_of`, `parent_of`, `peer_of`, `distinguish_from`, `can_cooccur_with`, `may_result_in`, and `may_be_result_of`. Targets use `VIGIL-FC-NNNNNN`, never a mutable compound semantic path.

A variant has exactly one in-family class parent. Definitions are not duplicated merely to express co-occurrence or distinction.

## Generation

Generate every complete family page and the combined full-reference book:

```bash
python vigil/taxonomy/render_taxonomy.py \
  --catalogue \
  --output-dir vigil/taxonomy/generated
```

Generate one Markdown family reference when needed:

```bash
python vigil/taxonomy/render_taxonomy.py \
  vigil/taxonomy/families/VIGIL-FF-0001-authority-boundary-integrity.json \
  --format markdown \
  --output /tmp/VIGIL-FF-0001.md
```

Regenerate the migration review projection:

```bash
python vigil/taxonomy/render_migration_inventory.py \
  vigil/taxonomy/migration/Caelestis.LegacyFailure.MigrationLedger.json \
  --output vigil/taxonomy/migration/Caelestis.LegacyFailure.InventoryReview.md
```

## Validation

Run catalogue-wide schema and integrity validation:

```bash
python vigil/taxonomy/validate_taxonomy.py
```

The validator checks every family against the JSON Schema and enforces duplicate-ID/code detection, family membership, variant parentage, relationship targets, duplicate relationships, allowed-list drift, index/file agreement, filename identity, removed-ID references, mandatory descriptions, and supersession-chain integrity.

## Portability

No Caelestis instrument, path, authority field, constitutional relationship, CAM control dependency, or “implements provision” relationship belongs in canonical family JSON. Legacy sources may be analysed only in the separate migration ledger. The standard must remain understandable and usable without access to CAM or Caelestis.
