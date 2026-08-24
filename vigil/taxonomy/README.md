# VIGIL Failure Taxonomy — Prototype

This directory prototypes a portable, machine-readable **technical reference standard for AI governance failure mechanisms**.

The prototype is deliberately separate from VIGIL evidence-to-repair records. A failure taxonomy class describes **what kind of structural failure exists**. An incident or VIGIL Failure Mode record may later apply one or more taxonomy codes, but severity, evidence confidence, vendor, date, harm, triage state and repair status do not belong inside the taxonomy definition itself.

## Prototype architecture

```text
VIGIL.FailureTaxonomy.Index.json
        |
        +-- families/
              |
              +-- authority-boundary-integrity.json   <- canonical data

VIGIL.FailureTaxonomy.Schema.json                     <- machine contract
validate_taxonomy.py                                  <- integrity checks
render_taxonomy.py                                    <- human renderer
previews/*.md / *.html                                <- generated review views
```

The intended scale is **one JSON file per bounded failure family**, not one file per failure class and not one file per broad organisational domain.

A family is acceptable only when every child class can complete this sentence coherently:

> Every class in this family is a way in which **the same bounded structural invariant** fails.

Broad containers such as `governance`, `UX`, `safety`, or `AI system failure` are not suitable family names merely because many failures can appear there.

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

The JSON file is canonical, but nobody should have to review raw JSON.

Generate the Markdown preview:

```bash
python vigil/taxonomy/render_taxonomy.py \
  vigil/taxonomy/families/authority-boundary-integrity.json \
  --format markdown \
  --output vigil/taxonomy/previews/authority-boundary-integrity.md
```

Generate the standalone HTML preview:

```bash
python vigil/taxonomy/render_taxonomy.py \
  vigil/taxonomy/families/authority-boundary-integrity.json \
  --format html \
  --output vigil/taxonomy/previews/authority-boundary-integrity.html
```

Validate internal integrity:

```bash
python vigil/taxonomy/validate_taxonomy.py \
  vigil/taxonomy/families/authority-boundary-integrity.json
```

## Prototype question

This first family is intentionally substantial enough to test scale. The review question is not “are these nine class names final?” It is:

> Does this family/file model remain understandable, bounded, searchable and extensible if VIGIL eventually contains hundreds or thousands of failure classes?

No Caelestis instrument, path, authority field or CAM-specific control dependency is part of the portable taxonomy data model.
