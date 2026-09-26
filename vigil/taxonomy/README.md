# VIGIL Observatory Alignment Taxonomy — Technical Standard

This directory contains a portable, machine-readable technical reference for AI-governance alignment invariants and their occurrence mappings. It is separate from incident, severity, harm, evidence-confidence, triage, jurisdiction, vendor, repair-state, and other event metadata.

## Rights and citation

The family JSON files remain the canonical taxonomy; the maintained Full Reference PDF is a generated publication projection. The taxonomy and associated original material are proprietary VIGIL Observatory Materials. Public accessibility and inspectability do not grant permission to copy, redistribute, adapt, derive from, translate, systematically extract, incorporate into another taxonomy or product, or train or evaluate machine-learning systems with the material. Citation, reference and linking with attribution to **CAM Initiative and VIGIL Observatory** are permitted. Other reuse requires prior written licence; see [`../../LICENSE.md`](../../LICENSE.md) and [`../../RIGHTS.json`](../../RIGHTS.json).

© 2026 Phoenix Covenant Pty Ltd trading as CAM Initiative (ABN 14 692 195 529). All rights reserved.

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
  VIGIL-FF-0010-infrastructural-authority-integrity.json
  VIGIL-FF-0011-value-appropriation-integrity.json
  VIGIL-FF-0012-objective-pursuit-integrity.json
  VIGIL-FF-0013-economic-influence-integrity.json
  VIGIL-FF-0014-governance-independence-neutrality-integrity.json
  VIGIL-FF-0015-identity-evaluative-integrity.json
generated/
  VIGIL.FailureTaxonomy.CaseFileExamples.json
  VIGIL.Observatory.AlignmentTaxonomy.FullReference.pdf
migration/
  Caelestis.LegacyFailure.MigrationLedger.json
  Caelestis.LegacyFailure.InventoryReview.md
```

Family JSON is canonical. The maintained PDF is a generated publication projection.

### Naming compatibility

The public standard and maintained PDF publication are the **VIGIL Observatory Alignment Taxonomy**. Existing machine-readable dataset filenames containing `FailureTaxonomy` and immutable `VIGIL-FF-*` / `VIGIL-FC-*` identifiers are retained as compatibility surfaces until a separately governed migration is approved.

Within the Alignment Taxonomy, `FF` denotes **Fidelity Family** and `FC` denotes **Fidelity Class**. These terms identify the structural invariant boundary being assessed without presupposing the outcome of an occurrence. The immutable `VIGIL-FF-*` and `VIGIL-FC-*` identifiers remain unchanged. Consumers must not infer occurrence polarity from those legacy filename or identifier stems; polarity is carried by each Incident mapping's `classification_role`. The maintained publication filename is `VIGIL.Observatory.AlignmentTaxonomy.FullReference.pdf`. Generated HTML is not a VIGIL Observatory publication asset; HTML emitted by the renderer is transient build material only. The migration ledger is non-normative source-analysis evidence and is not a dependency of the portable taxonomy.

Current publications render only active families and selectable classes. Historical or retired class material retained in canonical `subtypes` for migration integrity is not publication content and must not appear in Markdown, HTML, or PDF output.

`generated/VIGIL.FailureTaxonomy.CaseFileExamples.json` is a non-normative reverse mapping derived from canonical Incident `taxonomy_classification` blocks. It lets public interfaces discover Case File examples for immutable family and class IDs without embedding incident-specific record IDs in portable taxonomy definitions. Each projected example declares whether the mapping is the Incident's primary structural mechanism or an independently evidenced secondary mechanism. Unclassified Incidents remain valid registry records but do not enter this classification projection until a primary classification exists.

Canonical Incident classification preserves one principal mechanism in `primary_classification`. The optional `secondary_classifications` array records zero or more additional, independently evidenced structural mechanisms. Primary/secondary is the mapping position; each mapping independently carries `classification_role` as `failure-occurrence`, `successful-invariant`, or `ambiguous-boundary`. The ambiguous-boundary role records a material, admitted relationship to the class invariant where the bounded occurrence establishes neither failure nor successful invariant holding. A secondary classification is not inherently a failure and is not a harm, consequence, manifestation, sector, locus, hypothesis, or merely conceivable upstream cause. Primary and secondary class IDs must be distinct and resolve to the canonical taxonomy.

## Taxonomic boundary

A family is admissible only when every child can coherently complete:

> Every class in this family is a way in which **the same bounded structural invariant** fails.

Broad organisational containers such as governance, UX, safety, security, or AI-system failure are not families merely because failures can appear there. A candidate family normally requires a bounded invariant, meaningful inclusion and exclusion rules, at least two distinct mechanisms absent a compelling singleton case, and independence from vendor, framework, locus, governor, harm, and severity.

The hierarchy is:

**Alignment Taxonomy → Fidelity Family → selectable Fidelity Class → non-selectable subtype or recognition pattern where justified**

One JSON file contains one bounded family. Selectable classes remain peer records in `classes`. A narrower manifestation of the same mechanism is embedded under its canonical class in `subtypes`; it is not independently selectable and does not appear in the family's allowed-class lists.

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

### Canonical naming polarity

Canonical family and class names describe the governed integrity property or invariant boundary, not the failed manifestation. The Alignment Taxonomy remains diagnostic, but polarity is carried by the occurrence mapping rather than baked into the canonical family or class label.

For an Incident mapping:

- `failure-occurrence` means the mapped invariant failed in the bounded occurrence;
- `successful-invariant` means the mapped invariant held under relevant failure pressure; and
- `ambiguous-boundary` means the occurrence materially engages the invariant but the evidence establishes neither failure nor successful holding.

Accordingly, a class such as `Required Control Activation` may support all three roles without producing constructions such as “Required Control Non-Activation — successful invariant”. Failure definitions, recognition conditions, exclusions and failure examples remain failure-oriented diagnostic content. Canonical names and semantic codes should instead identify the positive or polarity-neutral property being assessed.

Renaming for polarity does not create a new class. Immutable family and class IDs are preserved, prior public names and semantic codes are retained in `aliases`, and historical Incident classifications remain attached to the same IDs unless their substantive mechanism is separately re-adjudicated.

Every family defines its immutable ID, semantic code, canonical name, version, status, abstraction, plain-English explanation, technical definition, governing invariant, scope, inclusion rule, exclusion rule, aliases, and allowed class IDs/codes.

Every selectable class defines its immutable ID, semantic code, current family ID, canonical name, class abstraction, status, plain-English explanation, technical definition, canonical `invariant`, recognition criteria, exclusions, examples, aliases, typed relationships where relevant, and optional external mappings or supersession metadata. The class invariant is the positive mechanism-specific structural property that must hold to prevent or repair that class. It must remain narrower than, and consistent with, the parent family invariant. Consumers must load the applicable family invariant once and add each applicable class invariant. They must not synthesise, infer, or substitute a missing class invariant from the class definition or the broader family invariant. An embedded subtype preserves its semantic name, explanation, definition, recognition criteria, exclusions, examples, aliases and any historical retired class ID/code without becoming a peer class.

The effective constraint set is therefore:

```text
parent family invariant
+ each applicable class invariant
```

Where multiple classes from the same family apply, the family invariant is loaded once and each class contributes only its mechanism-specific additional constraint. Renderers and consumers must expose these as distinct family and class fields rather than duplicating the parent family invariant as class text.

Families and classes may optionally contain structured `invariant_exemplars`. These link an evidenced VIGIL Incident to a successful-invariant, ambiguous-boundary, or repaired-post-control relationship without classifying that Incident as a failure. The linked Incident remains authoritative for occurrence facts, sources, severity, uncertainty and interpretive provenance; the taxonomy records only why the occurrence demonstrates, tests or restores the invariant. Short hypothetical failure illustrations remain in `examples`, and classified failure occurrences remain in the generated Incident-backed Case File projection. These three evidence roles must not be conflated.

Repair and generated failure-case projections operate per mapping. Only mappings with `classification_role = failure-occurrence` contribute a failed invariant to Repair or the generated failure-case examples. `successful-invariant` and `ambiguous-boundary` mappings remain linked for exemplar retrieval and traceability but are excluded from those failure projections. A mixed Incident may therefore contribute a failure example to one class while preserving successful-invariant or ambiguous-boundary relationships to others.

### Semantic roles of family prose

The three principal family fields are complementary and must not be used as interchangeable summaries:

- `plain_english` describes the recognisable **failure condition** in accessible language. It must say how the family is not working; a sentence that states only the healthy or required condition belongs in `invariant`.
- `definition` gives the technical boundary of the **bounded failure set**. It must encompass every admitted child mechanism, distinguish neighbouring families, and avoid becoming either an incident example or a normative aspiration.
- `invariant` states the positive **bounded structural property that must hold**. Every admitted child class must be a distinct way that this same property fails.

Parent prose must be re-tested whenever a class is added, moved, narrowed, or widened. A valid child cannot be left outside the parent's `plain_english`, `definition`, `invariant`, and inclusion boundary merely because its immutable membership is machine-valid. Conversely, parent wording must not be broadened to import mechanisms that remain assigned to another family.

Definitions must not contain incident-specific values. Severity, harm, persistence, reproducibility, visibility, incident status, evidence confidence, jurisdiction, vendor/model, manifestation, locus, repair side, propagation, observability state, evidence state, and repair status remain orthogonal event dimensions.

## Dataset and publication versioning

The version in `VIGIL.FailureTaxonomy.Index.json` is the version of the downloadable Alignment Taxonomy dataset. The maintained Full Reference PDF is a composite technical reference and therefore surfaces both the canonical Alignment Taxonomy version and the canonical VIGIL Harm & Severity methodology version. The publication renderer resolves the current VIGIL-HIM methodology from `vigil/methodologies/`, so a methodology version change is reflected in the technical reference without falsely advancing the taxonomy dataset version.

Dataset releases follow these rules:

- lifecycle states progress through `prototype`, `draft`, `beta`, `active` and `deprecated` as applicable;
- `draft` dataset releases use the `-draft` prerelease suffix; a deliberate graduation to `beta` or `active` removes that suffix and it must not later be reintroduced;
- an amendment, addition, movement, deprecation, lifecycle graduation, or other change to an existing family or class collection increments the third digit;
- admission of a new fidelity family increments the second digit and resets the third digit to zero;
- the first digit is reserved for a deliberately approved, materially incompatible re-foundation of the taxonomy and is never inferred from routine record maintenance;
- every dataset release records a fixed ISO `publication_date`; generation must not substitute the current clock date;
- historical classification stamps remain unchanged unless the mappings are substantively re-adjudicated.

The index `release_history` records the canonical family/class content digest, family-ID set, class count, change level, dataset version, and publication date. Taxonomy validation rejects changed canonical family/class content unless the release history, dataset version, and publication date have been advanced consistently. It also rejects a patch increment for a newly admitted family and a minor increment for an ordinary existing-record change.

## Relationships

Supported peer-class relationship types are `peer_of`, `distinguish_from`, `can_cooccur_with`, `may_result_in`, and `may_be_result_of`. Targets use current selectable `VIGIL-FC-NNNNNN` identifiers, never a mutable compound semantic path or a retired subtype ID.

A subtype is nested directly under exactly one canonical class and cannot be emitted as an independent primary or secondary classification. Current peer classes use relationships only for genuine distinction, co-occurrence or directional effects; a narrower manifestation is not modeled as a `child_of` peer.

## Generation

Generate the maintained Full Reference PDF with:

```bash
python vigil/taxonomy/render_taxonomy_publication.py \
  --catalogue \
  --output-dir vigil/taxonomy/generated \
  --pdf
```

The PDF is a deterministic projection of the canonical family JSON, the current VIGIL Harm & Severity methodology, and their consolidated external references; it is generated rather than hand-edited. The renderer may emit HTML internally while composing the PDF, but those files are transient build material and are not committed publication assets. Pull requests validate the taxonomy contract, rebuild the Incident-backed Case File projection, and apply evidence exclusions without requiring publication regeneration. After changes land on `main`, the publication workflow uses the repository's established PDF renderer to regenerate, validate, and commit the refreshed PDF asset.

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

The validator checks every family against the JSON Schema and enforces duplicate-ID/code detection, family membership, selectable-class abstraction, non-selectable subtype ownership, deterministic retired-ID successor mappings, current relationship targets, duplicate relationships, allowed-list drift, index/file agreement, filename identity, removed-ID reservation, mandatory descriptions, same-kind supersession, and supersession-chain integrity.

## Portability

No Caelestis path, authority field, constitutional relationship, CAM control dependency, or “implements provision” relationship belongs in canonical family JSON. Legacy sources may be analysed in the separate migration ledger. An `invariant_exemplar.governance_placement` may name an external framework or instrument as a non-normative placement cross-reference, but it does not make that framework a portable taxonomy dependency or confer authority through the taxonomy. The standard must remain understandable and usable without access to CAM or Caelestis.
