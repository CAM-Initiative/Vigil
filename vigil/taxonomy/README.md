# VIGIL Failure Taxonomy — Prototype

This directory prototypes a portable, machine-readable **technical reference standard for AI governance failure mechanisms**.

The prototype is deliberately separate from VIGIL evidence-to-repair records. A failure taxonomy class describes **what kind of structural failure exists**. An incident or VIGIL Failure Mode record may later apply one or more taxonomy codes, but severity, evidence confidence, vendor, date, harm, triage state and repair status do not belong inside the taxonomy definition itself.

## Prototype architecture

```text
VIGIL.FailureTaxonomy.Index.json
        |
        +-- families/
              |
              +-- authority-boundary-integrity.json
              +-- provenance-lineage-integrity.json
              +-- verification-completion-integrity.json
              +-- observability-audit-integrity.json

VIGIL.FailureTaxonomy.Schema.json                     <- machine contract
validate_taxonomy.py                                  <- integrity checks
render_taxonomy.py                                    <- human renderer
```

The intended scale is **one JSON file per bounded failure family**, not one file per failure class and not one file per broad organisational domain.

A family is acceptable only when every child class can complete this sentence coherently:

> Every class in this family is a way in which **the same bounded structural invariant** fails.

Broad containers such as `governance`, `UX`, `safety`, or `AI system failure` are not suitable family names merely because many failures can appear there.

## Filename and identity rules

Family filenames use a bounded, descriptive, lowercase kebab-case slug:

```text
families/<bounded-family-name>.json
```

Examples:

```text
authority-boundary-integrity.json
provenance-lineage-integrity.json
verification-completion-integrity.json
observability-audit-integrity.json
```

The **stable taxonomy code is the identity**. The filename is only a repository locator. This means a family can be renamed or moved without changing the identity of every downstream record that cites its code.

Filename rules:

- one file contains one failure family;
- a filename describes the bounded invariant, not an organisational domain, harm category, product surface, vendor, or incident;
- failure classes and variants remain inside their family file and do not receive separate files;
- family discovery occurs through `VIGIL.FailureTaxonomy.Index.json`, so filesystem order does not carry taxonomic meaning;
- no conceptual directory tree is created beneath `families/`; relationships belong in structured taxonomy fields, not folder nesting;
- if one family grows so large that its classes no longer share one coherent invariant, the remedy is to identify a genuinely distinct failure family, not to create arbitrary shard files.

This keeps file growth proportional to the number of **meaningful failure families**, not the number of individual failure classes. Hundreds or thousands of classes therefore do not imply hundreds or thousands of files.

## Prototype design influences

The storage and review model borrows proven scaling mechanics from several established resources without adopting their substantive classifications:

- **MITRE CWE** — stable identifiers, abstraction levels, relationships, status, descriptions, examples and multiple views over a large technical weakness catalogue.
- **AI Incident Database (AIID)** — multiple taxonomies can coexist over the same incident corpus rather than forcing incident, cause, harm and technical failure into one hierarchy.
- **OECD AI Incidents and Hazards Monitor / Common Reporting Framework** — incident status and metadata such as harm and severity are treated as dimensions of an event rather than definitions of the failure mechanism itself.
- **MIT AI Risk Repository** — separate causal and domain taxonomies demonstrate the value of keeping orthogonal classification axes separate.

## Family file contract

Each family carries:

- stable family code;
- family name, version, status and abstraction;
- a plain-English explanation;
- a technical definition;
- the invariant the family protects;
- scope;
- explicit inclusion and exclusion rules;
- an enumerated `allowed_codes` list;
- child failure classes and variants.

Each failure class carries:

- stable code and canonical name;
- abstraction (`class` or `variant`);
- plain-English explanation;
- technical definition;
- required recognition conditions;
- explicit exclusions;
- illustrative examples;
- aliases/search terms where useful;
- typed relationships;
- optional external-standard mappings.

## Why both plain English and technical definitions?

The taxonomy must support two users at once:

1. a person asking, “What actually is this failure?”; and
2. a machine, auditor or evaluator that needs deterministic classification fields.

The plain-English explanation is therefore mandatory, not editorial decoration.

## Human review

The JSON file is canonical, but nobody should have to review raw JSON. The renderer produces Markdown or standalone HTML from the same family file without adding implementation commentary to the public reference view.

Generate a Markdown view:

```bash
python vigil/taxonomy/render_taxonomy.py \
  vigil/taxonomy/families/authority-boundary-integrity.json \
  --format markdown \
  --output /tmp/authority-boundary-integrity.md
```

Generate a standalone HTML view:

```bash
python vigil/taxonomy/render_taxonomy.py \
  vigil/taxonomy/families/authority-boundary-integrity.json \
  --format html \
  --output /tmp/authority-boundary-integrity.html
```

Validate all current prototype families:

```bash
python vigil/taxonomy/validate_taxonomy.py vigil/taxonomy/families/*.json
```

## Prototype scale test

The current prototype deliberately uses four bounded families with different structural concerns:

1. **Authority Boundary Integrity Failures** — unjustified creation, expansion, transfer or inheritance of authority.
2. **Provenance & Lineage Integrity Failures** — loss or distortion of origin, authorship, transformation, continuity or target binding.
3. **Verification & Completion Integrity Failures** — unsupported, stale or mismatched claims of verification or completion.
4. **Observability & Audit Integrity Failures** — inadequate capture, attribution, coverage or reconstruction of material system activity.

The review question is:

> Does this family/file model remain understandable, bounded, searchable and extensible when structurally different failure families coexist and the number of failure classes grows substantially?

No Caelestis instrument, path, authority field or CAM-specific control dependency is part of the portable taxonomy data model.
