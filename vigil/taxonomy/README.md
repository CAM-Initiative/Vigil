# VIGIL Observatory Failure Taxonomy — Technical Standard

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
  VIGIL-FF-0005-access-session-state-integrity.json
  VIGIL-FF-0006-work-state-continuity-integrity.json
  VIGIL-FF-0007-governance-control-reach-integrity.json
  VIGIL-FF-0008-control-activation-integrity.json
  VIGIL-FF-0009-agency-preserving-influence-integrity.json
generated/
  one complete HTML page per family
  VIGIL.FailureTaxonomy.FullReference.html
  VIGIL.Observatory.FailureTaxonomy.FullReference.pdf
migration/
  Caelestis.LegacyFailure.MigrationLedger.json
  Caelestis.LegacyFailure.InventoryReview.md
```

Family JSON is canonical. HTML, Markdown, and PDF references are generated projections. The migration ledger is non-normative source-analysis evidence and is not a dependency of the portable taxonomy.

`generated/VIGIL.FailureTaxonomy.CaseFileExamples.json` is a non-normative reverse mapping derived from canonical Incident `taxonomy_classification` blocks. It lets public interfaces discover Case File examples for immutable family and class IDs without embedding incident-specific record IDs in portable taxonomy definitions. Each projected example declares whether the mapping is the Incident's primary structural mechanism or an independently evidenced secondary mechanism. Unclassified Incidents remain valid registry records but do not enter this classification projection until a primary classification exists.

Canonical Incident classification preserves one principal mechanism in `primary_classification`. The optional `secondary_classifications` array records zero or more additional, independently evidenced structural mechanisms. A secondary classification is not a harm, consequence, manifestation, sector, locus, hypothesis, or merely conceivable upstream cause. Primary and secondary class IDs must be distinct and resolve to the canonical taxonomy.

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

### Semantic roles of family prose

The three principal family fields are complementary and must not be used as interchangeable summaries:

- `plain_english` describes the recognisable **failure condition** in accessible language. It must say how the family is not working; a sentence that states only the healthy or required condition belongs in `invariant`.
- `definition` gives the technical boundary of the **bounded failure set**. It must encompass every admitted child mechanism, distinguish neighbouring families, and avoid becoming either an incident example or a normative aspiration.
- `invariant` states the positive **bounded structural property that must hold**. Every admitted child class must be a distinct way that this same property fails.

Parent prose must be re-tested whenever a class is added, moved, narrowed, or widened. A valid child cannot be left outside the parent's `plain_english`, `definition`, `invariant`, and inclusion boundary merely because its immutable membership is machine-valid. Conversely, parent wording must not be broadened to import mechanisms that remain assigned to another family.

Definitions must not contain incident-specific values. Severity, harm, persistence, reproducibility, visibility, incident status, evidence confidence, jurisdiction, vendor/model, manifestation, locus, repair side, propagation, observability state, evidence state, and repair status remain orthogonal event dimensions.

## Dataset and publication versioning

The version in `VIGIL.FailureTaxonomy.Index.json` is the version of the complete downloadable taxonomy dataset and Full Reference Manual. It is distinct from the version of an individual family record and from the historical taxonomy version recorded on a Failure Mode classification decision.

Dataset releases follow these rules:

- an amendment, addition, movement, deprecation, or other change to an existing family or class collection increments the third digit;
- admission of a new failure family increments the second digit and resets the third digit to zero;
- the first digit is reserved for a deliberately approved, materially incompatible re-foundation of the taxonomy and is never inferred from routine record maintenance;
- every dataset release records a fixed ISO `publication_date`; generation must not substitute the current clock date;
- historical Failure Mode classification stamps remain unchanged unless the mappings are substantively re-adjudicated.

The index `release_history` records the canonical family/class content digest, family-ID set, class count, change level, dataset version, and publication date. Taxonomy validation rejects changed canonical family/class content unless the release history, dataset version, and publication date have been advanced consistently. It also rejects a patch increment for a newly admitted family and a minor increment for an ordinary existing-record change.

## Relationships

Supported relationship types are `child_of`, `parent_of`, `peer_of`, `distinguish_from`, `can_cooccur_with`, `may_result_in`, and `may_be_result_of`. Targets use `VIGIL-FC-NNNNNN`, never a mutable compound semantic path.

A variant has exactly one in-family class parent. Definitions are not duplicated merely to express co-occurrence or distinction.

## Generation

Generate every complete family page and the combined full-reference HTML:

```bash
python vigil/taxonomy/render_taxonomy.py \
  --catalogue \
  --output-dir vigil/taxonomy/generated
```

Generate the HTML catalogue and the downloadable VIGIL Observatory Full Reference PDF:

```bash
python -m pip install weasyprint==69.0
python vigil/taxonomy/render_taxonomy.py \
  --catalogue \
  --output-dir vigil/taxonomy/generated \
  --pdf
```

The PDF is a publication projection of the same canonical family JSON used by the HTML renderer. It is intentionally generated rather than hand-edited. The current publication layer supplies stable front matter, dataset version, fixed edition date, status metadata, family/class pagination, a contents section, page numbering, and publication-rights text; visual branding and cover artwork may be evolved without changing the underlying taxonomy contract. Registry-sourced CAM header and footer images are pinned under `assets/` so publication generation does not depend on live network retrieval. The renderer defaults `SOURCE_DATE_EPOCH` to `0` for reproducible embedded-font timestamps; a publication environment may override it with another fixed epoch.

`.github/workflows/taxonomy-publications.yml` automatically rebuilds the HTML and PDF projections when the taxonomy index, family/class definitions, Incident-backed Case File example projection, Incident records, projection builder, or renderer changes. The PDF is a retained, ongoing publication asset: after validation it remains in `vigil/taxonomy/generated/` and is committed alongside the HTML outputs. The workflow rejects missing, empty, or non-PDF publication output before commit.

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

The validator checks every family against the JSON Schema and enforces duplicate-ID/code detection, family membership, variant parentage, relationship targets, duplicate relationships, allowed-list drift, index/file agreement, filename identity, removed-ID references, mandatory descriptions, same-kind supersession, and supersession-chain integrity.

## Portability

No Caelestis instrument, path, authority field, constitutional relationship, CAM control dependency, or “implements provision” relationship belongs in canonical family JSON. Legacy sources may be analysed only in the separate migration ledger. The standard must remain understandable and usable without access to CAM or Caelestis.
