#!/usr/bin/env python3
"""One-off migration from EXTREQ work-package scaffolding to canonical VIGIL architecture.

This script promotes the branch's current effective external-source and external-
requirement state into the maintained canonical state. It removes the historical
baseline/effective replay machinery and the temporary Layer 0/1/2 work-package
vocabulary without changing EXTREQ identities or manufacturing CAM findings.
"""

from __future__ import annotations

import importlib.util
import json
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
SOURCES = VIGIL / "external_sources"
REQ = VIGIL / "external_requirements"
SCRIPTS = VIGIL / "scripts"
TESTS = VIGIL / "tests"
WORKFLOWS = ROOT / ".github" / "workflows"
PROVENANCE_REF = "vigil/provenance/AUTHORSHIP-PROVENANCE.json"
PRE_NORMALISATION_COMMIT = "fcce747d8c34806b6a305e542b2795295e96e161"

DEFAULT = {
    "content_origin": "ai-authored",
    "generation_mode": "semi-autonomous",
    "human_role": "contract-approver",
    "human_authorship": False,
    "human_review_status": "not-reviewed",
    "human_verification_status": "not-verified",
    "declaration": PROVENANCE_REF,
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def import_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def rename_priority(value: str) -> str:
    return {
        "critical-alignment-source": "critical-governance-source",
        "high-value-alignment-source": "high-value-governance-source",
        "supporting-specialist-source": "supporting-specialist-source",
        "low-immediate-priority": "low-immediate-priority",
    }[value]


def review_state(value: str) -> str:
    if value in {"unassigned", "review-required", "superseded-before-review"}:
        return value
    return "reviewed"


def source_registry_schema() -> dict[str, Any]:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://github.com/CAM-Initiative/Vigil/vigil/external_sources/source-registry.schema.json",
        "title": "VIGIL External Governance Source Registry",
        "description": "Canonical registry of external governance source identity, version, lifecycle, metadata fingerprint and source-review workflow state. It does not record CAM applicability or coverage.",
        "type": "object",
        "required": ["schema_version", "updated_at", "authorship_provenance", "entries"],
        "properties": {
            "schema_version": {"const": "1.0"},
            "updated_at": {"type": ["string", "null"]},
            "authorship_provenance": {"type": "object"},
            "entries": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": [
                        "vigil_source_id", "external_source_id", "source_version", "canonical_identifier",
                        "issuer", "jurisdiction", "source_class", "source_lifecycle_state", "official_locator",
                        "upstream_source_id", "source_metadata_fingerprint", "change_state", "review_state",
                        "review_eligible", "first_seen", "last_seen",
                    ],
                    "properties": {
                        "vigil_source_id": {"type": "string", "pattern": "^EXT-[A-F0-9]{12}$"},
                        "external_source_id": {"type": "string", "minLength": 1},
                        "source_version": {"type": "string", "minLength": 1},
                        "canonical_identifier": {
                            "type": "object",
                            "required": ["scheme", "value"],
                            "properties": {
                                "scheme": {"type": "string", "minLength": 1},
                                "value": {"type": "string", "minLength": 1},
                            },
                            "additionalProperties": False,
                        },
                        "title": {"type": ["string", "null"]},
                        "issuer": {"type": "string", "minLength": 1},
                        "jurisdiction": {"type": "string", "minLength": 1},
                        "source_class": {"type": "string", "minLength": 1},
                        "source_lifecycle_state": {"type": "string", "minLength": 1},
                        "publication_date": {"type": ["string", "null"]},
                        "effective_date": {"type": ["string", "null"]},
                        "official_locator": {"type": "string", "minLength": 1},
                        "upstream_source_id": {"type": "string", "minLength": 1},
                        "upstream_record_id": {"type": ["string", "null"]},
                        "upstream_release": {"type": ["string", "null"]},
                        "source_metadata_fingerprint": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
                        "change_state": {"enum": ["new", "changed", "superseded", "withdrawn", "unchanged"]},
                        "review_state": {"enum": ["unassigned", "review-required", "reviewed", "superseded-before-review"]},
                        "review_eligible": {"type": "boolean"},
                        "first_seen": {"type": "string", "minLength": 1},
                        "last_seen": {"type": "string", "minLength": 1},
                        "notes": {"type": ["string", "null"]},
                    },
                    "additionalProperties": False,
                },
            },
        },
        "additionalProperties": False,
    }


def source_readme() -> str:
    return """# External Governance Sources

This directory is VIGIL's canonical registry of external governance source identity, version, lifecycle, publisher metadata and source-review workflow state. It is not a VIGIL evidentiary record class and it does not create CAM authority.

VIGIL's source identification, abstraction, classification and maintenance content is AI-authored and semi-autonomous under human contract approval unless an explicit provenance override says otherwise. External laws, standards and publications retain their own authorship and authority. See `../provenance/AUTHORSHIP-PROVENANCE.json`.

## Boundary

The governance flow is:

`external source -> external requirement -> CAM applicability/coverage assessment -> VIGIL routing/repair`

Source registration records what an external instrument is and whether it has changed. It MUST NOT determine whether the source applies to CAM, manufacture an external requirement, create a CAM coverage finding, or create a substantive VIGIL repair record automatically.

## Source authority

The canonical authority for legal or standards status is the official publisher, regulator or legislature. Third-party trackers may be used only for discovery.

`review_state` is VIGIL source-review workflow state. It is not a CAM applicability, conformance or coverage finding.

## Stable identity and metadata fingerprint

Each source/version has an internal `vigil_source_id` plus a publisher-native `canonical_identifier`. The durable source key is `external_source_id + source_version`.

`source_metadata_fingerprint` is a SHA-256 of VIGIL's material source-metadata projection. It supports deterministic source/version change detection. It is **not** a digest of a reviewed PDF, HTML capture, licensed standard file or other primary artefact.

Exact reviewed-source artefact digests belong in `../external_requirements/source-review-assurance.json`. Historical reviewed artefacts for which no digest was recorded remain `not-recorded`; VIGIL does not manufacture retrospective digests.

## Files

- `source-matrix.json` — publisher/source families, authority posture, lifecycle mappings and retrieval readiness.
- `source-registry.schema.json` — canonical source-registry contract.
- `source-registry.json` — maintained current source/version registry.
- `source-review-queue.json` — generated source-review queue.
- `SOURCE-CATALOGUE.md` — generated human-readable current source catalogue.
- `../scripts/manage-external-sources.py` — deterministic source registry maintenance and generation.

## Commands

```bash
python vigil/scripts/manage-external-sources.py build
python vigil/scripts/manage-external-sources.py validate --check-generated
```

For normalized observations from an official-source adapter:

```bash
python vigil/scripts/manage-external-sources.py ingest --source <source-id> --input /path/to/items.json
```

Semantic external-requirement extraction belongs under `../external_requirements/`. CAM applicability and coverage assessment belongs under `../cam_assessment/`.
"""


def requirements_readme() -> str:
    return """# External AI-Governance Requirements

This directory is VIGIL's canonical analytical corpus of governance requirements, controls, definitions and guidance derived from registered external sources.

It is **not** a CAM compliance database. Inclusion of an external requirement does not establish that the requirement applies to CAM, that CAM has adopted a voluntary standard, or that CAM currently complies, conforms or aligns.

VIGIL's extraction, abstraction, classification and crosswalk preparation are AI-authored and semi-autonomous under human contract approval unless an explicit artefact-level provenance override says otherwise. Contract approval does not imply substantive human review or source verification. See `../provenance/AUTHORSHIP-PROVENANCE.json`.

## Current-state architecture

The maintained current state is represented directly by:

- `requirements.json` — canonical EXTREQ corpus;
- `source-scope.json` — source access, extraction and review-priority state;
- `external-requirement.schema.json` and `source-scope.schema.json` — canonical contracts;
- `source-review-assurance.json` — exact reviewed-source digests and separately evidenced human review/verification;
- `source-coverage-manifests.json` — generated access/retrieval/analysis/completeness view.

Historical baseline/effective replay machinery is not part of the current architecture. Git history preserves prior states.

## Semantic separation

The governance flow is:

`external source -> external requirement -> CAM applicability/coverage assessment -> VIGIL routing/repair`

External requirements MUST NOT contain CAM instrument mappings, CAM coverage states or CAM conformance findings. Those judgements belong in `../cam_assessment/` and must be assessed against a specific CAM corpus commit.

## Source provenance: metadata fingerprint versus reviewed artefact

`source_metadata_fingerprint` is a SHA-256 of VIGIL's registered source/version metadata projection. It is not a hash of the PDF, HTML capture or other primary-source artefact reviewed.

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
python vigil/tests/test_external_requirements.py
```

CAM applicability and coverage are validated separately under `../cam_assessment/`.
"""


def cam_readme() -> str:
    return """# CAM Applicability and Coverage Assessments

This directory records the separate assessment of whether an external `EXTREQ-*` requirement is applicable to a specific CAM corpus state and what evidence-backed coverage disposition exists.

It is deliberately separate from:

- `vigil/external_sources/` — external-source identity, version, lifecycle and source-review workflow; and
- `vigil/external_requirements/` — external requirement meaning, authority semantics, access and extraction state.

## Boundary

The governance flow is:

`external source -> external requirement -> CAM applicability/coverage assessment -> VIGIL routing/repair`

A CAM assessment MUST NOT mutate external-source facts, manufacture missing external requirements, or convert a source-level `alignment_relationship` into a claim that CAM currently complies, conforms or aligns.

Every assessment must reference an existing canonical `EXTREQ-*` record and a specific CAM corpus commit. Applicability, coverage and evidence are then assessed independently.

## Assessment states

`applicability_state`:

- `applicable`
- `conditionally-applicable`
- `reference-only`
- `not-applicable`
- `unresolved`

`coverage_state`:

- `full`
- `partial`
- `absent`
- `conflicting`
- `indeterminate`
- `not-applicable`

`full` is a substantive evidence-backed assessment, not a synonym for textual similarity or the presence of a related instrument.

## Provenance and assurance

CAM assessments inherit VIGIL's default AI-authored, semi-autonomous provenance unless an explicit record-level authorship override is present.

Post-production human review or verification is recorded in `assurance_provenance`. Assurance does **not** rewrite AI authorship. Repository acceptance, publication, contract approval or human presence does not imply substantive review or verification.

## Current state

`assessments.json` remains intentionally empty until an actual CAM applicability/coverage assessment is performed. The existence of this structure does not retroactively assert that any EXTREQ applies to, is satisfied by, or is implemented in CAM.

## Validation

```bash
python vigil/scripts/validate-cam-assessments.py
python vigil/tests/test_cam_assessments.py
```
"""


def final_workflow() -> str:
    return """name: External governance corpus

on:
  push:
    paths:
      - "vigil/external_sources/**"
      - "vigil/external_requirements/**"
      - "vigil/cam_assessment/**"
      - "vigil/provenance/AUTHORSHIP-PROVENANCE.json"
      - "vigil/scripts/manage-external-sources.py"
      - "vigil/scripts/manage-external-requirements.py"
      - "vigil/scripts/validate-cam-assessments.py"
      - "vigil/scripts/validate-authorship-provenance.py"
      - "vigil/tests/test_external_sources.py"
      - "vigil/tests/test_external_requirements.py"
      - "vigil/tests/test_cam_assessments.py"
      - "vigil/tests/test_authorship_provenance.py"
      - ".github/workflows/external-governance.yml"
  pull_request:
    paths:
      - "vigil/external_sources/**"
      - "vigil/external_requirements/**"
      - "vigil/cam_assessment/**"
      - "vigil/provenance/AUTHORSHIP-PROVENANCE.json"
      - "vigil/scripts/manage-external-sources.py"
      - "vigil/scripts/manage-external-requirements.py"
      - "vigil/scripts/validate-cam-assessments.py"
      - "vigil/scripts/validate-authorship-provenance.py"
      - "vigil/tests/test_external_sources.py"
      - "vigil/tests/test_external_requirements.py"
      - "vigil/tests/test_cam_assessments.py"
      - "vigil/tests/test_authorship_provenance.py"
      - ".github/workflows/external-governance.yml"
  workflow_dispatch:

concurrency:
  group: external-governance-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: write

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          persist-credentials: true
          show-progress: false
      - uses: actions/setup-python@v6
        with:
          python-version: "3.x"
      - name: Build and validate external source registry
        run: |
          python vigil/scripts/manage-external-sources.py build
          python vigil/scripts/manage-external-sources.py validate --check-generated
          python vigil/tests/test_external_sources.py
      - name: Build and validate external requirements
        run: |
          python vigil/scripts/manage-external-requirements.py build
          python vigil/scripts/manage-external-requirements.py validate --check-generated
          python vigil/tests/test_external_requirements.py
      - name: Validate CAM assessments
        run: |
          python vigil/tests/test_cam_assessments.py
          python vigil/scripts/validate-cam-assessments.py
      - name: Validate authorship and assurance provenance
        run: |
          python vigil/tests/test_authorship_provenance.py
          python vigil/scripts/validate-authorship-provenance.py
      - name: Check generated outputs on pull request
        if: github.event_name == 'pull_request'
        run: |
          if ! git diff --quiet -- \
            vigil/external_sources/source-review-queue.json \
            vigil/external_sources/SOURCE-CATALOGUE.md \
            vigil/external_requirements/requirements-index.json \
            vigil/external_requirements/completeness-report.json \
            vigil/external_requirements/source-coverage-manifests.json \
            vigil/external_requirements/EXTERNAL-AI-GOVERNANCE-REQUIREMENTS.md \
            vigil/external_requirements/SOURCE-ACCESS-LIMITATIONS.md \
            vigil/external_requirements/BLOCKED-SOURCE-PRIORITIES.md \
            vigil/external_requirements/derivative-crosswalk-index.json \
            vigil/external_requirements/DERIVATIVE-CROSSWALKS.md; then
            echo "External governance generated outputs are stale."
            git diff --stat -- vigil/external_sources vigil/external_requirements
            exit 1
          fi
      - name: Commit generated outputs
        if: github.event_name == 'push' && github.actor != 'github-actions[bot]'
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add \
            vigil/external_sources/source-review-queue.json \
            vigil/external_sources/SOURCE-CATALOGUE.md \
            vigil/external_requirements/requirements-index.json \
            vigil/external_requirements/completeness-report.json \
            vigil/external_requirements/source-coverage-manifests.json \
            vigil/external_requirements/EXTERNAL-AI-GOVERNANCE-REQUIREMENTS.md \
            vigil/external_requirements/SOURCE-ACCESS-LIMITATIONS.md \
            vigil/external_requirements/BLOCKED-SOURCE-PRIORITIES.md \
            vigil/external_requirements/derivative-crosswalk-index.json \
            vigil/external_requirements/DERIVATIVE-CROSSWALKS.md
          if git diff --cached --quiet; then
            echo "External governance generated outputs already current."
          else
            git commit -m "Rebuild external governance projections"
            git push
          fi

# Network ingestion remains deliberately disabled. Source ingestion and derivative
# processing may not create CAM findings or substantive VIGIL repair records.
"""


def migrate() -> None:
    effective = import_module(SCRIPTS / "manage-external-requirements-effective.py", "current_effective")
    sources_context, scopes_context, reviewed_at, context_errors = effective.extension_context()
    outputs, errors = effective.effective()
    all_errors = list(context_errors) + list(errors)
    if all_errors:
        raise ValueError("Current effective state is invalid before normalization:\n" + "\n".join(all_errors))

    effective_ledger = json.loads(outputs[effective.ELED])
    effective_requirements = json.loads(outputs[effective.EREQ])
    effective_crosswalks = json.loads(outputs[effective.XDATA])

    if len(effective_ledger["entries"]) != len(sources_context):
        raise ValueError("effective source count differs from extension context")
    if set(scopes_context) != set(sources_context):
        raise ValueError("effective source-scope coverage is not one-to-one before normalization")

    legacy_dispositions = []
    source_entries = []
    for original in effective_ledger["entries"]:
        entry = json.loads(json.dumps(original))
        old_alignment = entry.pop("alignment_state", "unassigned")
        old_eligible = bool(entry.pop("alignment_eligible", False))
        assessed_commit = entry.pop("caelestis_assessed_commit", None)
        crosswalk_refs = entry.pop("caelestis_crosswalk_refs", [])
        if assessed_commit or crosswalk_refs:
            legacy_dispositions.append({
                "vigil_source_id": entry["vigil_source_id"],
                "external_source_id": entry["external_source_id"],
                "source_version": entry["source_version"],
                "legacy_alignment_state": old_alignment,
                "legacy_caelestis_assessed_commit": assessed_commit,
                "legacy_caelestis_crosswalk_refs": crosswalk_refs,
            })
        entry.pop("source_metadata_fingerprint_semantics", None)
        entry.pop("fingerprint", None)
        entry["review_state"] = review_state(old_alignment)
        entry["review_eligible"] = old_eligible
        source_entries.append(entry)

    source_registry = {
        "schema_version": "1.0",
        "updated_at": reviewed_at,
        "authorship_provenance": DEFAULT,
        "entries": sorted(source_entries, key=lambda x: (x["external_source_id"], x["source_version"])),
    }
    write_json(SOURCES / "source-registry.json", source_registry)
    write_json(SOURCES / "source-registry.schema.json", source_registry_schema())

    matrix = load(SOURCES / "source-matrix.json")
    rules = matrix.get("design_rules", {})
    if "drafts_enter_alignment_queue" in rules:
        rules["drafts_enter_source_review_queue"] = rules.pop("drafts_enter_alignment_queue")
    for item in matrix.get("sources", []):
        if "alignment_eligible_states" in item:
            item["review_eligible_states"] = item.pop("alignment_eligible_states")
    write_json(SOURCES / "source-matrix.json", matrix)

    scope_entries = []
    for scope in scopes_context.values():
        value = json.loads(json.dumps(scope))
        value["review_priority"] = rename_priority(value.pop("alignment_priority"))
        value["review_priority_rationale"] = value.pop("alignment_priority_rationale")
        scope_entries.append(value)
    write_json(REQ / "source-scope.json", {
        "schema_version": "1.2",
        "reviewed_at": reviewed_at,
        "entries": sorted(scope_entries, key=lambda x: (x["external_source_id"], x["source_version"])),
    })

    requirement_doc = {
        key: value for key, value in effective_requirements.items()
        if key not in {"generated_from", "generation_provenance"}
    }
    requirement_doc["schema_version"] = "1.2"
    requirement_doc["updated_at"] = reviewed_at
    requirement_doc["authorship_provenance"] = DEFAULT
    requirement_doc["requirement_count"] = len(requirement_doc["requirements"])
    write_json(REQ / "requirements.json", requirement_doc)

    crosswalk_doc = {
        key: value for key, value in effective_crosswalks.items()
        if key not in {"generation_provenance"}
    }
    crosswalk_doc["authorship_provenance"] = DEFAULT
    write_json(REQ / "derivative-crosswalks.json", crosswalk_doc)

    requirement_schema = load(REQ / "effective-external-requirement.schema.json")
    requirement_schema["$id"] = "https://github.com/CAM-Initiative/Vigil/vigil/external_requirements/external-requirement.schema.json"
    requirement_schema["title"] = "VIGIL External AI-Governance Requirement"
    requirement_schema["description"] = (
        "Canonical analytical reference data derived from an authoritative external source. Normative-force and relationship fields classify the external source; they do not determine CAM applicability or assert compliance, conformance, alignment or implementation."
    )
    write_json(REQ / "external-requirement.schema.json", requirement_schema)

    scope_schema = load(REQ / "source-scope.schema.json")
    scope_schema["title"] = "VIGIL External AI-Governance Source Scope"
    scope_schema["properties"]["schema_version"] = {"const": "1.2"}
    props = scope_schema["properties"]["entries"]["items"]["properties"]
    required = scope_schema["properties"]["entries"]["items"]["required"]
    required[required.index("alignment_priority")] = "review_priority"
    required[required.index("alignment_priority_rationale")] = "review_priority_rationale"
    priority = props.pop("alignment_priority")
    priority["enum"] = ["critical-governance-source", "high-value-governance-source", "supporting-specialist-source", "low-immediate-priority"]
    props["review_priority"] = priority
    props["review_priority_rationale"] = props.pop("alignment_priority_rationale")
    write_json(REQ / "source-scope.schema.json", scope_schema)

    # Promote the staged canonical managers and tests.
    source_manager = (SCRIPTS / "manage-external-sources-next.py").read_text(encoding="utf-8")
    source_manager = source_manager.replace(
        'if entry.get("review_eligible") is not isinstance(entry.get("review_eligible"), bool):',
        'if not isinstance(entry.get("review_eligible"), bool):',
    )
    (SCRIPTS / "manage-external-sources.py").write_text(source_manager, encoding="utf-8")
    shutil.copyfile(SCRIPTS / "manage-external-requirements-next.py", SCRIPTS / "manage-external-requirements.py")
    shutil.copyfile(TESTS / "test_external_sources-next.py", TESTS / "test_external_sources.py")
    shutil.copyfile(TESTS / "test_external_requirements-next.py", TESTS / "test_external_requirements.py")

    # Rename CAM assessment area and remove work-package numbering terminology.
    old_cam = VIGIL / "cam_conformance"
    new_cam = VIGIL / "cam_assessment"
    if new_cam.exists():
        shutil.rmtree(new_cam)
    new_cam.mkdir(parents=True)
    shutil.copyfile(old_cam / "assessments.json", new_cam / "assessments.json")
    cam_schema_text = (old_cam / "cam-applicability.schema.json").read_text(encoding="utf-8")
    cam_schema_text = cam_schema_text.replace("cam_conformance", "cam_assessment")
    cam_schema_text = cam_schema_text.replace("cam-applicability.schema.json", "assessment.schema.json")
    cam_schema_text = cam_schema_text.replace("Layer 2", "CAM assessment")
    (new_cam / "assessment.schema.json").write_text(cam_schema_text, encoding="utf-8")
    (new_cam / "README.md").write_text(cam_readme(), encoding="utf-8")

    cam_validator = (SCRIPTS / "validate-cam-conformance.py").read_text(encoding="utf-8")
    cam_validator = cam_validator.replace('"""Validate VIGIL Layer 2 CAM applicability/conformance assessments."""', '"""Validate VIGIL CAM applicability and coverage assessments."""')
    cam_validator = cam_validator.replace('LAYER2 = ROOT / "cam_conformance"', 'CAM_ASSESSMENT = ROOT / "cam_assessment"')
    cam_validator = cam_validator.replace('ASSESSMENTS = LAYER2 / "assessments.json"', 'ASSESSMENTS = CAM_ASSESSMENT / "assessments.json"')
    cam_validator = cam_validator.replace('EFFECTIVE_REQUIREMENTS = ROOT / "external_requirements" / "effective-requirements.json"', 'REQUIREMENTS = ROOT / "external_requirements" / "requirements.json"')
    cam_validator = cam_validator.replace("effective_document", "requirements_document")
    cam_validator = cam_validator.replace("EFFECTIVE_REQUIREMENTS", "REQUIREMENTS")
    cam_validator = cam_validator.replace("effective Layer 1 EXTREQ", "canonical EXTREQ")
    cam_validator = cam_validator.replace("Layer 2 assessments schema_version", "CAM assessments schema_version")
    cam_validator = cam_validator.replace("Layer 2 dataset authorship provenance", "CAM assessment dataset authorship provenance")
    cam_validator = cam_validator.replace("Layer 2 assessment", "CAM assessment")
    cam_validator = cam_validator.replace("VIGIL Layer 2 CAM conformance validation", "VIGIL CAM assessment validation")
    (SCRIPTS / "validate-cam-assessments.py").write_text(cam_validator, encoding="utf-8")

    cam_test = (TESTS / "test_cam_conformance.py").read_text(encoding="utf-8")
    cam_test = cam_test.replace("VIGIL Layer 2 CAM applicability/conformance separation", "VIGIL CAM applicability/coverage separation")
    cam_test = cam_test.replace('validate-cam-conformance.py', 'validate-cam-assessments.py')
    cam_test = cam_test.replace('"cam_conformance"', '"cam_assessment"')
    cam_test = cam_test.replace("CamConformanceTests", "CamAssessmentTests")
    cam_test = cam_test.replace("cls.effective = MODULE.load(MODULE.EFFECTIVE_REQUIREMENTS)", "cls.requirements_doc = MODULE.load(MODULE.REQUIREMENTS)")
    cam_test = cam_test.replace('cls.extreq = cls.effective["requirements"][0]', 'cls.extreq = cls.requirements_doc["requirements"][0]')
    cam_test = cam_test.replace("self.effective", "self.requirements_doc")
    cam_test = cam_test.replace("test_current_layer2_state_is_empty_and_valid", "test_current_assessment_state_is_empty_and_valid")
    cam_test = cam_test.replace("test_layer1_normative_semantics_drift_is_rejected", "test_external_requirement_semantics_drift_is_rejected")
    cam_test = cam_test.replace("normative_force differs from effective Layer 1 EXTREQ", "normative_force differs from canonical EXTREQ")
    (TESTS / "test_cam_assessments.py").write_text(cam_test, encoding="utf-8")

    # Normalize provenance dataset declarations.
    provenance_path = VIGIL / "provenance" / "AUTHORSHIP-PROVENANCE.json"
    provenance = load(provenance_path)
    inherited_default = provenance["default_provenance"]
    provenance["dataset_declarations"] = {
        "external-governance-sources-and-requirements": {
            "applies_to": ["vigil/external_sources/", "vigil/external_requirements/"],
            "covers": ["source identification", "requirement extraction", "analytical paraphrase", "classification", "crosswalk preparation"],
            "provenance": inherited_default,
            "external_source_authorship_unchanged": True,
            "boundary": "External-source facts and external-requirement meaning are distinct from CAM applicability and coverage assessment.",
        },
        "cam-assessment": {
            "applies_to": ["vigil/cam_assessment/"],
            "covers": ["CAM applicability assessment", "CAM coverage assessment", "claim-family disposition", "remediation routing preparation"],
            "provenance": inherited_default,
            "boundary": "CAM assessments may reference canonical EXTREQ records but must not rewrite external-source facts or external-requirement meaning.",
        },
    }
    write_json(provenance_path, provenance)

    provenance_validator_path = SCRIPTS / "validate-authorship-provenance.py"
    pv = provenance_validator_path.read_text(encoding="utf-8")
    pv = pv.replace('"external-governance-layer-0-and-layer-1", {}', '"external-governance-sources-and-requirements", {}')
    pv = pv.replace("Layer 0/Layer 1 provenance differs", "external governance source/requirement provenance differs")
    old_block_start = '''    for relative in (\n        "external_sources/effective-ledger.json",\n        "external_requirements/effective-requirements.json",\n        "external_requirements/derivative-crosswalks.json",\n    ):\n'''
    old_block_end = '''    for relative in (\n        "external_requirements/requirements-index.json",\n'''
    start = pv.index(old_block_start)
    end = pv.index(old_block_end, start)
    maintained_block = '''    for relative in (\n        "external_sources/source-registry.json",\n        "external_requirements/requirements.json",\n        "external_requirements/derivative-crosswalks.json",\n    ):\n        document = load(VIGIL / relative)\n        provenance = document.get("authorship_provenance")\n        errors.extend(validate_provenance(provenance, relative, require_declaration=True))\n        if isinstance(provenance, dict):\n            for field, value in DEFAULT.items():\n                if provenance.get(field) != value:\n                    errors.append(f"{relative}: {field} must be {value!r}")\n\n'''
    pv = pv[:start] + maintained_block + pv[end:]
    pv = pv.replace(
        '''    for relative in (\n        "external_requirements/requirements-index.json",\n        "external_requirements/completeness-report.json",\n        "external_requirements/derivative-crosswalk-index.json",\n    ):''',
        '''    for relative in (\n        "external_sources/source-review-queue.json",\n        "external_requirements/requirements-index.json",\n        "external_requirements/completeness-report.json",\n        "external_requirements/source-coverage-manifests.json",\n        "external_requirements/derivative-crosswalk-index.json",\n    ):''',
    )
    provenance_validator_path.write_text(pv, encoding="utf-8")

    (SOURCES / "README.md").write_text(source_readme(), encoding="utf-8")
    (REQ / "README.md").write_text(requirements_readme(), encoding="utf-8")

    review = f"""# EXTREQ-04 — External Governance Architecture Normalisation

## Authority and boundary

- Normalisation date: 2026-08-19
- Human governance role: Dr Michelle Vivian O’Rourke — contract approver
- Substantive human review: not established
- Human source verification: not established
- Working branch: `agent/instrumental-coercive-influence-capability-revalidation`
- Pre-normalisation repository state: `{PRE_NORMALISATION_COMMIT}`

## Reason for normalisation

The previous `Layer 0`, `Layer 1` and `Layer 2` labels were introduced as temporary sub-work-package sequencing language. They were not intended to become permanent domain semantics. The baseline/effective/extension architecture was likewise a migration scaffold used to preserve stable historical inputs while provenance, source-access and external-requirement semantics were repaired.

Retaining that scaffold as the operational architecture created multiple current-looking source catalogues, duplicated baseline/effective requirement datasets, replay-only extension packs and compatibility builders. The repository therefore required knowledge of the EXTREQ implementation history merely to identify the current source of truth.

## Normalised architecture

The current effective state was promoted directly into the maintained canonical state:

`external source -> external requirement -> CAM applicability/coverage assessment -> VIGIL routing/repair`

The normalisation preserves:

- all current external source/version identities;
- stable `EXTREQ-*` identities;
- source access, retrieval and analysis distinctions;
- metadata-fingerprint versus reviewed-artefact-digest separation;
- AI authorship and human-assurance provenance;
- normative-force and downstream claim-family semantics;
- bounded-completeness reporting;
- derivative-crosswalk source-authority boundaries; and
- strict separation between external requirement meaning and CAM applicability/coverage findings.

The normalisation does **not** create or alter any CAM applicability finding and does not assert new external source requirements.

## Historical state

Git history preserves the former baseline/effective/extension machinery and its historical work-package terminology. Historical EXTREQ review records may therefore use `Layer 0/1/2`, baseline, effective and extension terminology when describing the architecture that existed at the time. Those terms are historical provenance, not current repository architecture.
"""
    (VIGIL / "docs" / "reviews" / "EXTREQ-04-external-governance-architecture-normalisation.md").write_text(review, encoding="utf-8")
    if legacy_dispositions:
        write_json(VIGIL / "docs" / "reviews" / "EXTREQ-04-legacy-source-dispositions.json", {
            "schema_version": "1.0",
            "pre_normalisation_commit": PRE_NORMALISATION_COMMIT,
            "entries": legacy_dispositions,
        })

    (WORKFLOWS / "external-governance.yml").write_text(final_workflow(), encoding="utf-8")

    # Remove migration/replay scaffolding only after the canonical state exists.
    obsolete_files = [
        SOURCES / "ledger.json",
        SOURCES / "effective-ledger.json",
        SOURCES / "alignment-queue.json",
        SOURCES / "ledger.schema.json",
        SOURCES / "EXTERNAL-GOVERNANCE-SOURCES.md",
        SOURCES / "EFFECTIVE-GOVERNANCE-SOURCES.md",
        REQ / "effective-requirements.json",
        REQ / "effective-external-requirement.schema.json",
        REQ / "extension-transitions.json",
        SCRIPTS / "manage-external-governance-ledger.py",
        SCRIPTS / "apply-external-governance-baseline.py",
        SCRIPTS / "manage-external-requirements-effective.py",
        SCRIPTS / "manage-external-requirements-extended.py",
        SCRIPTS / "validate-cam-conformance.py",
        TESTS / "test_external_governance_ledger.py",
        TESTS / "test_external_requirements_extended.py",
        TESTS / "test_cam_conformance.py",
        WORKFLOWS / "external-governance-ledger.yml",
        SCRIPTS / "manage-external-sources-next.py",
        SCRIPTS / "manage-external-requirements-next.py",
        TESTS / "test_external_sources-next.py",
        TESTS / "test_external_requirements-next.py",
    ]
    for path in obsolete_files:
        if path.exists():
            path.unlink()
    if (SOURCES / "baseline-release-2").exists():
        shutil.rmtree(SOURCES / "baseline-release-2")
    if (REQ / "extensions").exists():
        shutil.rmtree(REQ / "extensions")
    if old_cam.exists():
        shutil.rmtree(old_cam)

    # The one-off migration artefacts delete themselves from the resulting commit.
    one_off_workflow = WORKFLOWS / "normalise-external-governance.yml"
    if one_off_workflow.exists():
        one_off_workflow.unlink()
    Path(__file__).unlink()

    print(f"Promoted {len(source_entries)} source versions and {len(requirement_doc['requirements'])} requirements to canonical state.")


if __name__ == "__main__":
    migrate()
