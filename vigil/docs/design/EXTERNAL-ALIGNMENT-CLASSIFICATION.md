# External Alignment Classification — data-shape proposal

Status: design proposal only. This document does not amend `vigil/VIGIL.Schema.json`, validators, canonical Incident records, or generated outputs.

## Purpose

Case File Section 03 now distinguishes two different classification authorities:

1. **VIGIL Alignment Classification** — VIGIL's own taxonomy adjudication from `taxonomy_classification`.
2. **External Alignment Classification** — a faithful projection of an admitted external assessor's own classification scheme or rating.

The second surface must not imply that VIGIL has adopted, translated, endorsed, or reconciled the external label into a VIGIL Fidelity Class.

## Current compatibility source

The current Incident model already permits an optional object at:

```text
external_assessments[].classification_or_rating
```

Existing records may contain:

```json
{
  "scheme": "OpenAI model-misalignment reporting framework",
  "value": "misalignment",
  "verbatim_label": "misalignment"
}
```

The website can render the new table from those fields immediately, using the parent `external_assessments[]` object for assessor, assessment URL, title, date, relationship and assessment summary.

## Proposed additive canonical fields

If the schema is later amended, the least disruptive option is to retain `classification_or_rating` and make the following fields available inside the object:

| Field | Type | Purpose | Database mapping |
| --- | --- | --- | --- |
| `scheme` | string | Name of the external classification or rating framework | `external_alignment_classification.scheme` |
| `scheme_version` | string, optional | Version/date/edition of the external scheme where published | `external_alignment_classification.scheme_version` |
| `value` | string | Normalised machine-readable value | `external_alignment_classification.value` |
| `verbatim_label` | string, optional | Exact public label used by the assessor | `external_alignment_classification.verbatim_label` |
| `classification_basis` | string, optional | Assessor-published reason or bounded explanation supporting the label | `external_alignment_classification.classification_basis` |
| `source_locator` | string, optional | Page, section, figure, heading or other locator for the classification statement | `external_alignment_classification.source_locator` |

The parent `external_assessments[]` record remains authoritative for:

- `assessment_id`
- `assessor`
- `assessment_title`
- `assessment_date`
- `assessment_url`
- `assessment_type`
- `relationship_to_incident`
- `assessment_summary`
- `scope_note`
- `vigil_comparison_note`
- `source_record_refs`
- `assessment_status`
- `reviewed_on`

Those fields should not be duplicated inside the classification object merely for rendering convenience.

## Relational database shape

A future SQL implementation can map the nested object to a child table without changing its authority semantics:

```text
external_assessment
  assessment_id PK
  incident_id FK
  assessor
  assessment_title
  assessment_date
  assessment_url
  ...

external_alignment_classification
  external_alignment_classification_id PK
  assessment_id FK
  scheme
  scheme_version NULL
  value
  verbatim_label NULL
  classification_basis NULL
  source_locator NULL
```

One classification row per external assessment is sufficient for the present corpus. If external frameworks later publish multiple independent axes for one assessment, cardinality can expand to one-to-many without overloading VIGIL's own taxonomy model.

## Rendering contract

Section 03 should present the VIGIL classification first, including the VIGIL alignment legend and taxonomy reference. The External Alignment Classification table follows as a separate peer subsection.

Recommended columns:

| Assessor | External classification | Scheme | Published basis / conclusion |
| --- | --- | --- | --- |
| Parent `assessor` + assessment citation | `verbatim_label` falling back to `value` | `scheme` + optional `scheme_version` | `classification_basis` falling back to parent `assessment_summary` |

The table must state that external classifications are shown in the assessor's own terminology and are not VIGIL taxonomy mappings.

## Explicit non-goals

This proposal does **not**:

- map an external label to a VIGIL Fidelity Family or Fidelity Class;
- infer VIGIL alignment outcome from an external provider's use of terms such as "misalignment", "unsafe", "failure" or "successful";
- make an external framework authoritative over VIGIL adjudication;
- move external assessment evidence out of `external_assessments[]`; or
- authorize a schema, validator, migration, or corpus-wide record change.

Any future amendment to `VIGIL.Schema.json`, validators, permanent tests, or canonical records remains subject to the maintainer stop conditions.

## Taxonomy-gap signal boundary

External classifications can also reveal concepts that VIGIL's current taxonomy does not obviously represent, but they are not themselves authority for taxonomy expansion.

Where an external assessor's classification, published basis or conceptual distinction identifies a governance-relevant point that the Incident evidence independently supports, the reviewer should ask whether that point is faithfully representable in the current Alignment Taxonomy.

If it is not, the point should enter the taxonomy-gap test in `vigil/docs/design/TAXONOMY-GAP-DETECTION.md`.

The external framework remains a discovery and comparison source. VIGIL must independently establish:

- the occurrence evidence;
- the recovered governance proposition;
- the nearest current classes and their actual recognition boundaries; and
- whether the mismatch is evidence uncertainty, an existing-class fit, a boundary or terminology repair, a family/decomposition issue, or a genuine taxonomy-coverage gap.

Do not create or broaden a VIGIL Fidelity Class merely to reproduce an external assessor's vocabulary.

