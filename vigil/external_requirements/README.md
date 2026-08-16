# Authoritative External AI-Governance Requirements Baseline

This directory is VIGIL **Layer 1**: source-scope classification and requirement-level analytical reference data derived from registered external governance sources.

It is not a CAM compliance database. Inclusion of an external requirement does not establish that the requirement applies to CAM, that CAM has adopted a voluntary standard, or that CAM currently complies, conforms or aligns.

VIGIL's extraction, abstraction, classification and crosswalk preparation are AI-authored and semi-autonomous under human contract approval unless an explicit artefact-level provenance override says otherwise. Contract approval does not imply substantive human review or source verification. See `../provenance/AUTHORSHIP-PROVENANCE.json`.

## Layer separation

- **Layer 0 — `../external_sources/`**: external source identity, version, lifecycle and source-change workflow.
- **Layer 1 — this directory**: external source scope, requirement meaning, authority semantics, access/review state and derivative crosswalks.
- **Layer 2 — `../cam_conformance/`**: separate CAM applicability and coverage assessments against a specific CAM corpus commit.

The direction is one-way:

`Layer 0 source -> Layer 1 EXTREQ -> Layer 2 applicability/coverage assessment -> VIGIL routing/repair`

Layer 1 MUST NOT contain CAM instrument mappings, CAM coverage states or CAM conformance findings.

## Frozen maintained baseline and effective Layer 1

The maintained historical baseline remains schema v1.1:

- `requirements.json`
- `source-scope.json`
- `external-requirement.schema.json`
- `extensions/*.json`

Those files are preserved so historical inputs remain reproducible.

`manage-external-requirements-effective.py` builds the normalized effective Layer 1 v1.2 projection. The effective schema is `effective-external-requirement.schema.json`.

## Source provenance: metadata fingerprint versus reviewed artefact

Historical `source_fingerprint` values in frozen v1.1 inputs are **metadata fingerprints**. They identify VIGIL's registered source/version metadata projection; they are not hashes of the PDF, HTML capture or other primary-source artefact that was reviewed.

Effective Layer 1 therefore uses:

- `source_metadata_fingerprint` — SHA-256 of VIGIL's material source-metadata projection; and
- `reviewed_source_digest` — SHA-256 of the exact reviewed primary-source artefact, when such a digest was actually recorded.

Historical direct-source extractions for which no exact artefact digest was preserved are emitted as `reviewed_source_digest_status: not-recorded`. The repository does not manufacture retrospective digests.

For licensed standards, a digest and non-copyrighted artefact metadata may be retained. The licensed source text itself must not be committed unless redistribution rights permit it.

## Normative force, source posture and downstream claim vocabulary

Three different questions are represented separately:

1. `requirement_posture` — what the source itself says about the represented clause or control (`mandatory-normative`, `recommended-practice`, and so on);
2. `normative_force` — what kind of external authority the source has (`binding-law`, `voluntary-consensus-standard`, `government-voluntary-framework`, etc.); and
3. `alignment_relationship` — the appropriate downstream claim family if applicability or adoption is later established (`compliance`, `conformance`, `alignment`, `reference-only`).

A mandatory clause inside a voluntary consensus standard is still a mandatory clause **for conformance to that standard**; it is not thereby a legally binding duty on CAM. Actual CAM applicability is a Layer 2 judgement.

## Human assurance without authorship inflation

`source-review-assurance.json` is the maintained sidecar for:

- exact reviewed-source artefact digests; and
- post-production human review or verification.

Human assurance supplements the original AI authorship provenance. It does not rewrite AI-authored material as human-authored.

The sidecar is intentionally empty until evidence supports a specific assurance claim. Absence of an assurance record means that no additional human review or verification is established.

## Access, retrieval and analysis are different states

`source_access_status` records the available access route, for example public-primary, licensed-primary, official extract or metadata-only.

Generated `source-coverage-manifests.json` separately records:

- `source_retrieval_state`;
- `analysis_state`;
- represented requirement/control counts;
- known unreviewed and inaccessible sections;
- the bounded completeness criterion; and
- source-digest and human-assurance status.

This prevents an available public route from being mistaken for proof that the source artefact was actually retrieved and reviewed.

## Bounded completeness

A source with extraction state `complete` is projected as coverage state `bounded-complete`.

`bounded-complete` means that governance-significant material identified by the recorded extraction criterion is represented. It does **not** prove that every sentence, note or informative annex was atomised into an EXTREQ record.

## Extension packs and state transitions

Extension packs are additive reviewed inputs. Filename order is not authority.

If more than one extension pack changes the Layer 1 scope state for the same source/version, the transition must be registered explicitly in `extension-transitions.json` with:

- previous pack and state;
- later pack and state; and
- a rationale.

An unregistered repeated update is a validation failure.

The current registry records the seven deliberate IEEE extraction-state promotions made during EXTREQ-02.

## Derivative crosswalk boundary

Derivative publisher or VIGIL crosswalks may be stored for discovery and later comparison, but they cannot:

- manufacture missing source wording;
- convert a metadata-only source into a reviewed normative source;
- assert CAM applicability; or
- assert compliance, conformance or implementation.

## Copyright and controlled standards

For ISO/IEC, IEEE and other controlled standards:

- use official publisher metadata for identity and lifecycle;
- use lawfully accessed primary text for clause-level extraction;
- do not reconstruct unseen requirements from titles, abstracts, tables of contents, third-party summaries or crosswalks; and
- do not commit copyrighted primary text without redistribution rights.

`BLOCKED-SOURCE-PRIORITIES.md` remains the access-planning view for sources whose normative text is not lawfully available in the repository workflow.

## Commands

Build the frozen maintained baseline:

```bash
python vigil/scripts/manage-external-requirements.py build
```

Build and validate effective Layer 1:

```bash
python vigil/scripts/manage-external-requirements-effective.py build
python vigil/scripts/manage-external-requirements-effective.py validate --check-generated
python vigil/tests/test_external_requirements_extended.py
```

Validate Layer 2 separately:

```bash
python vigil/scripts/validate-cam-conformance.py
python vigil/tests/test_cam_conformance.py
```
