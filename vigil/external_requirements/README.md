# External AI-Governance Requirements

This directory is VIGIL's canonical analytical corpus of governance requirements, controls, definitions and guidance derived from registered external sources.

It is **not** a CAM compliance database. Inclusion of an external requirement does not establish that the requirement applies to CAM, that CAM has adopted a voluntary standard, or that CAM currently complies, conforms or aligns.

VIGIL's extraction, abstraction, classification and crosswalk preparation are AI-authored and semi-autonomous under human contract approval unless an explicit artefact-level provenance override says otherwise. Contract approval does not imply substantive human review or source verification. See `../provenance/AUTHORSHIP-PROVENANCE.json`.

## Current-state architecture

The maintained current state is represented directly by:

- `requirements.json` — canonical EXTREQ corpus;
- `source-scope.json` — source access, extraction and review-priority state;
- `external-requirement.schema.json` and `source-scope.schema.json` — canonical contracts;
- `metadata-review.json` and `metadata-review.schema.json` — field-level source-fidelity review state for machine-critical requirement metadata;
- `METADATA-REVIEW-METHODOLOGY.md` — review-state semantics and completion rules;
- `source-review-assurance.json` — exact reviewed-source digests and separately evidenced human review/verification;
- `source-coverage-manifests.json` — generated access/retrieval/analysis/completeness view.

Historical baseline/effective replay machinery is not part of the current architecture. Git history preserves prior states.

## Semantic separation

The governance flow is:

`external source -> external requirement -> CAM applicability/coverage assessment -> VIGIL routing/repair`

External requirements MUST NOT contain CAM instrument mappings, CAM coverage states or CAM conformance findings. Those judgements belong in `../cam_assessment/` and must be assessed against a specific CAM corpus commit.

## Source provenance: metadata fingerprint versus reviewed artefact

`source_metadata_fingerprint` is a SHA-256 of VIGIL's registered source/version metadata projection. It is not a hash of the PDF, HTML capture or other primary-source artefact reviewed.

The AI system/model and method responsible for substantive source review are recorded canonically in the matching `../external_sources/source-registry.json` review event. That event references `source-scope.json` for maintained access and extraction limitations. It does not replace requirement-level interpretation provenance.

Where an exact reviewed artefact digest was actually recorded, `source-review-assurance.json` records its SHA-256. Historical direct-source extractions for which no exact artefact digest was preserved remain `reviewed_source_digest_status: not-recorded`. VIGIL does not manufacture retrospective digests.

For licensed standards, a digest and non-copyrighted artefact metadata may be retained. Licensed source text itself must not be committed unless redistribution rights permit it.

## External authority semantics

Three different questions remain separate:

1. `requirement_posture` — what the represented source clause or control says (`mandatory-normative`, `recommended-practice`, etc.);
2. `normative_force` — the source's external authority category (`binding-law`, `voluntary-consensus-standard`, `government-voluntary-framework`, etc.); and
3. `alignment_relationship` — the appropriate downstream claim family if applicability or adoption is later established (`compliance`, `conformance`, `alignment`, `reference-only`).

A mandatory clause inside a voluntary consensus standard is mandatory for conformance to that standard; it is not thereby a legally binding duty on CAM. CAM applicability is assessed separately.

## Access, retrieval and analysis are different states

`source_access_status` records the available access route. `source-coverage-manifests.json` separately records `source_retrieval_state`, `analysis_state`, represented requirement/control counts, known unreviewed or inaccessible sections, bounded completeness and assurance status.

An available public or licensed route is therefore not treated as proof that the exact source artefact was retrieved and analysed.

## Bounded completeness

`bounded-complete` means governance-significant material identified by the recorded extraction criterion is represented. It does **not** claim that every sentence, note or informative annex was atomised into an EXTREQ record.

Source-fidelity assurance is stricter than historical extraction completeness. See `SOURCE-FIDELITY-METHODOLOGY.md` and `SOURCE-FIDELITY-STATUS.md`.

## Metadata review state

Empty arrays in fidelity-critical metadata fields are ambiguous unless a review decision has been recorded. `metadata-review.json` distinguishes:

- `populated-reviewed` — values are present and have been checked against the source proposition;
- `not-specified-by-source` — the source was reviewed and does not state that semantic dimension;
- `not-applicable` — the semantic dimension does not apply to the proposition; and
- `review-required` — no defensible source-fidelity decision has yet been recorded.

The tracked fields are `applicable_actor`, `governed_object`, `timing_or_frequency`, `required_artefacts`, `evidence_expectation`, `verification_method`, `applicability_conditions`, and `exceptions_or_qualifications`.

The initial ledger is deliberately conservative: legacy requirements are not automatically marked reviewed merely because fields already contain values. `validate-external-requirement-metadata.py` turns those unresolved decisions into a finite review queue. Default mode reports unresolved review work but fails only on contradictory/malformed review-state contracts; `--strict` also fails while unresolved review decisions remain.

## Derivative crosswalk boundary

Derivative publisher or VIGIL crosswalks may support discovery and comparison, but they cannot manufacture missing source wording, convert metadata-only access into reviewed normative content, determine CAM applicability, or assert compliance/conformance/implementation.

## Copyright and controlled standards

For ISO/IEC, IEEE and other controlled standards:

- use official publisher metadata for identity and lifecycle;
- use lawfully accessed primary text for clause-level extraction;
- do not reconstruct unseen requirements from titles, abstracts, tables of contents, third-party summaries or crosswalks; and
- do not commit copyrighted primary text without redistribution rights.

`BLOCKED-SOURCE-PRIORITIES.md` is the access-planning view for primary sources whose normative text is not available to the review workflow.

## Commands

```bash
python vigil/scripts/manage-external-requirements.py build
python vigil/scripts/manage-external-requirements.py validate --check-generated
python vigil/scripts/validate-external-requirement-metadata.py
python vigil/scripts/validate-external-requirement-metadata.py --write-report
python vigil/scripts/validate-external-requirement-metadata.py --strict
python vigil/tests/test_external_requirements.py
python vigil/scripts/test_external_requirement_metadata.py
```

CAM applicability and coverage are validated separately under `../cam_assessment/`.
