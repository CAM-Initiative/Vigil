# VIGIL-TAXONOMY — Failure-Family Semantic and Parent/Child Alignment Repair Audit

## Scope and branch preflight

- Repository: `CAM-Initiative/Vigil`
- Existing branch: `agent/hugging-face-authority-reconciliation`
- Live-verified pre-work remote head: `86332bfb9495f0d6820948f44a9600e529b76d75`
- Supplied handoff head: `86332bfb9495f0d6820948f44a9600e529b76d75`
- Intervening remote commits after the supplied head: none
- Live-verified `main` at preflight: `16dd8ef71a27287dd676dbf26e40937714561f5e`
- Taxonomy version retained: `0.2.0-draft`
- Pre-work catalogue: 9 families, 53 classes and variants, `removed_ids: []`

The existing local HF-02 checkout was one commit behind the live branch and was left untouched. Work proceeded from a fresh checkout of the exact remote branch rather than reconciling that checkout. No reset, rebase, merge, cherry-pick, force-push, branch creation, pull request or history reconciliation was performed.

The post-HF-02 commits from `5530c2c` through `86332bf` were inspected. They preserve legal-rights and citation normalisation, the VIGIL Observatory naming and licence alignment, and the new HTML/PDF publication pipeline. The HF-02 reconciliation commit and all its Failure Mode, observation, source-evidence, classification and generated-index work remain present and unchanged.

## Review method and semantic-role rule

All nine canonical family records and all 53 child classes and variants were reviewed against the family-admission sentence:

> Every class in this family is a way in which the same bounded structural invariant fails.

The authoring contract now distinguishes the three parent fields:

- `plain_english` describes the recognisable failure condition and must not state only the healthy condition;
- `definition` describes the bounded technical failure set and must encompass every admitted child mechanism; and
- `invariant` states the positive bounded structural property that every child is a way of failing.

This rule is recorded both in the taxonomy README and as field descriptions in the JSON Schema. Parent prose must be re-tested whenever a class is added, moved, narrowed or widened.

## Defect chronology

| Family | Defect type | Historical origin | Reconciliation |
| --- | --- | --- | --- |
| `VIGIL-FF-0008` | Original wording inversion | TAXONOMY-04A introduced a `plain_english` sentence describing correct operation rather than failure. | Rewritten as the four recognisable failure states: availability/applicability ambiguity, required non-activation, unwarranted activation and activation-authority suppression. |
| `VIGIL-FF-0007` | Later parent-record narrowing drift | TAXONOMY-04A narrowed the parent to failures occurring only after activation while retaining `FC-000041`, whose mechanism is bypass of a required route and does not require a control to have become operative first. | The parent now covers required-route bypass and, separately, failure of already-operative state or signals to retain effect and reach a capable governed point. |
| `VIGIL-FF-0008` | Later child-admission drift | TAXONOMY-06A admitted `FC-000043 — Unwarranted Control Activation`; the family definition was not widened from its earlier three-mechanism form. | The definition and inclusion boundary now expressly cover activation when valid activation conditions are not satisfied. |
| `VIGIL-FF-0004` | Later child-admission drift | The Evidence Accessibility Review admitted `FC-000044` and `FC-000045`; the parent continued to speak primarily in capture and reconstructability terms. | Parent prose now includes authorised direct access to preserved primary evidence and bounded, governed evidence-production/access pathways without creating investigative authority. |
| `VIGIL-FF-0005` | Later child-admission drift | TAXONOMY-07 admitted `FC-000048 — Verification-Dependency Access Failure`; the parent still required divergence, collapse or inaccurate representation of access/session state. | The common invariant now also preserves practical access through verification-dependency transitions where an otherwise valid or unresolved state requires a proportionate fallback. |

The TAXONOMY-04A, TAXONOMY-06A, TAXONOMY-07 and Evidence Accessibility Review + Validator Closure audits remain unchanged as historical records. Their earlier decisions are not rewritten to imply retrospective consistency.

## Nine-family outcome

| Family | Classes | Outcome |
| --- | ---: | --- |
| `VIGIL-FF-0001 — Authority Boundary Integrity` | 11 | Regression review passed; parent and children remain aligned; unchanged. |
| `VIGIL-FF-0002 — Provenance & Lineage Integrity` | 7 | Regression review passed; unchanged. |
| `VIGIL-FF-0003 — Verification & Completion Integrity` | 7 | Regression review passed; unchanged. |
| `VIGIL-FF-0004 — Observability & Audit Integrity` | 10 | Parent prose repaired; family version `0.1.0` → `0.1.1`. |
| `VIGIL-FF-0005 — Access & Session State Integrity` | 4 | Parent prose repaired; `FC-000048` coherently retained; family version `0.1.0` → `0.1.1`. |
| `VIGIL-FF-0006 — Work-State Continuity Integrity` | 3 | Regression review passed; unchanged. |
| `VIGIL-FF-0007 — Governance Control Reach Integrity` | 3 | Parent route/reach boundary repaired; family version `0.2.0` → `0.2.1`. |
| `VIGIL-FF-0008 — Control Activation Integrity` | 4 | Failure-condition inversion and definition drift repaired; family version `0.1.0` → `0.1.1`. |
| `VIGIL-FF-0009 — Agency-Preserving Influence Integrity` | 4 | Regression review passed; unchanged. |

No family or class ID, semantic code, class membership, abstraction, relationship, recognition condition, exclusion, Failure Mode classification or classification confidence changed. No ID was allocated, removed, reused or renumbered.

## Boundary decisions

- **Activation versus reach:** FF-0008 asks whether a defined control becomes operative when and only when its activation conditions are satisfied. FF-0007 asks whether required conduct traverses a governance route and whether any already-operative control state or signal survives delivery to a capable governed point.
- **Access state versus authority:** FC-000048 remains an access/session-state failure only where incomplete dependent verification makes otherwise valid or unresolved access practically unavailable without proportionate fallback. Treating non-verification as authority for an entitlement decision remains separately classifiable under Authority Boundary Integrity.
- **Evidence access versus investigative authority:** FF-0004 assumes an already-authorised review or investigative role. It covers evidence accessibility and governed production/access pathways but does not create, enlarge or determine investigative authority.
- **Classification stability:** Parent wording repair does not supply independent mechanism evidence for reclassifying any Failure Mode. All existing primary and secondary classifications remain unchanged.

## Publication pipeline

The canonical family JSON was rendered through `vigil/taxonomy/render_taxonomy.py --catalogue --pdf`. All nine standalone family HTML pages, the combined full-reference HTML and the downloadable PDF were regenerated from canonical sources rather than edited by hand.

The new PDF pipeline initially exposed non-deterministic embedded-font timestamps. The renderer now applies the conventional reproducible-build default `SOURCE_DATE_EPOCH=0` unless a publication environment supplies another fixed epoch. Two complete catalogue and PDF renders from identical input were byte-identical.

## Validation

- Taxonomy validator: PASS — 9 family files, 53 classes and catalogue integrity.
- Focused failure-taxonomy tests: PASS — 24 tests.
- Focused taxonomy-classification tests: PASS — 24 tests.
- Full `vigil/tests` suite: PASS — 169 tests.
- Full `vigil/scripts` suite: PASS — 37 tests.
- Repository-wide record validator: PASS — 102 JSON files, 6 research files, 108 unique public records.
- Public-record validator: PASS — 108 public records.
- Failure Mode facet validator: PASS — 72 Failure Modes, 2 faceted records.
- Pipeline-state validator: PASS.
- Lifecycle, corpus-coverage, observatory-boundary and interpretive-provenance validators: PASS — 102 records.
- Authorship provenance: PASS.
- Source provenance: PASS — 336 source records.
- System-component and CAM-assessment validators: PASS.
- External-source registry: PASS — 81 source versions, 0 review-required or review-due.
- External requirements: PASS — 81 source versions, 845 requirements.
- External-requirement fidelity and metadata-review contracts: PASS.
- EU AI Act staged re-extraction check: PASS — 8 retirements, 102 additions and 18 metadata normalisations.
- Deterministic family HTML, full-reference HTML and PDF regeneration: PASS, byte-stable across two complete runs.
- Generated HTML and PDF parsing, JSON parsing, Python bytecode compilation and `git diff --check`: PASS.

The external-requirement fidelity validator continues to report the integrated baseline's 16 effective fidelity downgrades, and the metadata-review validator continues to identify 527 records requiring review. Both validators pass. This package did not modify EXTREQ, external-source, Failure Mode, observation, source-evidence, taxonomy-classification or HF-02 substantive content.

## Completion boundary and provenance

The exact final local and remote commit is reported in the completion handoff because a commit cannot embed its own immutable object ID. No pull request or merge is created by this package.

The reconciliation was performed on 27 August 2026 by OpenAI ChatGPT Work using GPT-5.6 Sol through direct repository analysis, complete nine-family and 53-child review, historical-audit comparison, parent/child invariant testing, schema and authoring-contract repair, deterministic publication generation and repository-wide validation. Dr Michelle O'Rourke supplied and approved the substantive defect findings and task boundaries. AI-authored implementation and validation do not imply line-by-line human verification of the resulting files.
