#!/usr/bin/env python3
"""Apply the approved runtime-bounded conformance update to VIGIL PR #28."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
BRANCH = "agent/runtime-governance-reach"
DATE = "2026-07-13"
CAELESTIS_SQUASH_SHA = "9b0ce40db55ea1e52df4942a64a0d24df5968afe"
CAELESTIS_REBUILD_SHA = "40113eea5428478ba0734b3980600bfcece425a0"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def add_unique(items: list[str], value: str) -> None:
    if value not in items:
        items.append(value)


def update_identity(record: dict, version: str) -> None:
    identity = record["record_identity"]
    identity["updated"] = DATE
    identity["version"] = version


# Schema-rules contract.
schema_path = VIGIL / "VIGIL.Schema.json"
schema = read_json(schema_path)
schema["version"] = "2.2-runtime-bounded-conformance"
for record_class, field_name in (
    ("failure_mode", "runtime_non_conformance"),
    ("patch", "runtime_conformance"),
):
    record_rules = schema["record_classes"][record_class]
    optional = record_rules.setdefault("optional_top_level_fields", [])
    add_unique(optional, field_name)

schema["runtime_conformance_rules"] = {
    "description": "Optional runtime-bounded evidence objects distinguish an implemented CAM repair from observed conformance or non-conformance in named vendor, platform, runtime, model, client, or interface formations. Runtime names remain open-ended and cross-runtime transfer is never presumed.",
    "runtime_conformance": {
        "allowed_record_types": ["patch", "patch_note"],
        "allowed_overall_status_values": ["confirmed", "mixed", "unknown", "not-applicable"],
        "required_fields_when_present": [
            "overall_status",
            "confirming_count",
            "non_confirming_count",
            "unknown_count",
            "notes"
        ],
        "optional_detail_arrays": [
            "confirming_runtimes",
            "non_confirming_runtimes",
            "unknown_runtimes"
        ],
        "count_rule": "Counts must be non-negative integers and must equal the corresponding detail-array length whenever that array is present.",
        "runtime_identifier_rule": "vendor, platform, runtime, model, and client values are open-ended non-empty strings; no vendor or runtime names are hard-coded by the validator."
    },
    "runtime_non_conformance": {
        "allowed_record_types": ["failure_mode"],
        "required_fields_when_present": [
            "non_confirming_count",
            "unknown_count",
            "non_confirming_runtimes",
            "notes"
        ],
        "count_rule": "Counts must be non-negative integers and must equal the corresponding detail-array length whenever that array is present.",
        "runtime_identifier_rule": "vendor, platform, runtime, model, and client values are open-ended non-empty strings; no vendor or runtime names are hard-coded by the validator."
    },
    "interpretive_rule": "patched means the CAM repair exists; confirmed means intended behaviour was observed in a named runtime; non-confirming means the linked failure remains present or recurred in a named runtime. A non-confirming runtime does not invalidate a patch confirmed elsewhere."
}
write_json(schema_path, schema)


# Validator implementation.
validator_path = VIGIL / "scripts" / "validate-vigil-records.py"
validator = validator_path.read_text(encoding="utf-8")
constant_anchor = 'RESOLUTION_STATUS_REQUIRED = {"status", "resolved_by", "resolution_note"}\n'
constant_block = '''RESOLUTION_STATUS_REQUIRED = {"status", "resolved_by", "resolution_note"}\nRUNTIME_CONFORMANCE_STATUS_ALLOWED = {"confirmed", "mixed", "unknown", "not-applicable"}\nRUNTIME_CONFORMANCE_COUNT_FIELDS = {\n    "confirming_runtimes": "confirming_count",\n    "non_confirming_runtimes": "non_confirming_count",\n    "unknown_runtimes": "unknown_count",\n}\n'''
if "RUNTIME_CONFORMANCE_STATUS_ALLOWED" not in validator:
    if constant_anchor not in validator:
        raise RuntimeError("Validator constant anchor not found")
    validator = validator.replace(constant_anchor, constant_block, 1)

function_anchor = "def standards_reference_text(value: Any) -> str:\n"
function_block = '''def _validate_non_negative_count(path: Path, label: str, value: Any, errors: list[str]) -> bool:\n    if isinstance(value, bool) or not isinstance(value, int) or value < 0:\n        errors.append(f"{path}: {label} must be a non-negative integer")\n        return False\n    return True\n\n\ndef _validate_string_list(path: Path, label: str, value: Any, errors: list[str]) -> None:\n    if not isinstance(value, list):\n        errors.append(f"{path}: {label} must be an array")\n        return\n    if any(not isinstance(item, str) or not item.strip() for item in value):\n        errors.append(f"{path}: {label} must contain only non-empty strings")\n\n\ndef _validate_runtime_entries(\n    path: Path,\n    block_name: str,\n    block: dict[str, Any],\n    array_name: str,\n    count_name: str,\n    required_extra_fields: set[str],\n    errors: list[str],\n) -> None:\n    entries = block.get(array_name)\n    if entries is None:\n        return\n    if not isinstance(entries, list):\n        errors.append(f"{path}: {block_name}.{array_name} must be an array")\n        return\n    count = block.get(count_name)\n    if isinstance(count, int) and not isinstance(count, bool) and count >= 0 and count != len(entries):\n        errors.append(\n            f"{path}: {block_name}.{count_name}={count} does not match "\n            f"{block_name}.{array_name} length {len(entries)}"\n        )\n    required = {"vendor", "platform", "runtime", "date_observed"} | required_extra_fields\n    for index, entry in enumerate(entries):\n        label = f"{block_name}.{array_name}[{index}]"\n        if not isinstance(entry, dict):\n            errors.append(f"{path}: {label} must be an object")\n            continue\n        missing = sorted(field for field in required if is_blank(entry.get(field)))\n        if missing:\n            errors.append(f"{path}: {label} missing required fields: {', '.join(missing)}")\n        for field in ("vendor", "platform", "runtime", "date_observed"):\n            value = entry.get(field)\n            if value is not None and (not isinstance(value, str) or not value.strip()):\n                errors.append(f"{path}: {label}.{field} must be a non-empty string")\n        for field in ("evidence_urls", "related_patch_ids"):\n            if field in entry:\n                _validate_string_list(path, f"{label}.{field}", entry.get(field), errors)\n\n\ndef validate_runtime_conformance(path: Path, record: dict[str, Any], errors: list[str]) -> None:\n    block = record.get("runtime_conformance")\n    if block is None:\n        return\n    if record.get("record_type") not in {"patch", "patch_note"}:\n        errors.append(f"{path}: runtime_conformance is permitted only on PATCH records")\n    if not isinstance(block, dict):\n        errors.append(f"{path}: runtime_conformance must be an object")\n        return\n    required = {"overall_status", "confirming_count", "non_confirming_count", "unknown_count", "notes"}\n    missing = sorted(field for field in required if is_blank(block.get(field)))\n    if missing:\n        errors.append(f"{path}: runtime_conformance missing required fields: {', '.join(missing)}")\n    status = block.get("overall_status")\n    if status not in RUNTIME_CONFORMANCE_STATUS_ALLOWED:\n        allowed = ", ".join(sorted(RUNTIME_CONFORMANCE_STATUS_ALLOWED))\n        errors.append(f"{path}: runtime_conformance.overall_status {status!r} is not allowed; allowed values: {allowed}")\n    for count_name in ("confirming_count", "non_confirming_count", "unknown_count"):\n        _validate_non_negative_count(path, f"runtime_conformance.{count_name}", block.get(count_name), errors)\n    notes = block.get("notes")\n    if not isinstance(notes, str) or not notes.strip():\n        errors.append(f"{path}: runtime_conformance.notes must be a non-empty string")\n    _validate_runtime_entries(\n        path, "runtime_conformance", block, "confirming_runtimes", "confirming_count", {"evidence_basis"}, errors\n    )\n    _validate_runtime_entries(\n        path,\n        "runtime_conformance",\n        block,\n        "non_confirming_runtimes",\n        "non_confirming_count",\n        {"failure_expression", "evidence_urls", "related_patch_ids"},\n        errors,\n    )\n    _validate_runtime_entries(\n        path, "runtime_conformance", block, "unknown_runtimes", "unknown_count", {"evidence_basis"}, errors\n    )\n\n\ndef validate_runtime_non_conformance(path: Path, record: dict[str, Any], errors: list[str]) -> None:\n    block = record.get("runtime_non_conformance")\n    if block is None:\n        return\n    if record.get("record_type") != "failure_mode":\n        errors.append(f"{path}: runtime_non_conformance is permitted only on FM records")\n    if not isinstance(block, dict):\n        errors.append(f"{path}: runtime_non_conformance must be an object")\n        return\n    required = {"non_confirming_count", "unknown_count", "non_confirming_runtimes", "notes"}\n    missing = sorted(field for field in required if is_blank(block.get(field)))\n    if missing:\n        errors.append(f"{path}: runtime_non_conformance missing required fields: {', '.join(missing)}")\n    for count_name in ("non_confirming_count", "unknown_count"):\n        _validate_non_negative_count(path, f"runtime_non_conformance.{count_name}", block.get(count_name), errors)\n    notes = block.get("notes")\n    if not isinstance(notes, str) or not notes.strip():\n        errors.append(f"{path}: runtime_non_conformance.notes must be a non-empty string")\n    _validate_runtime_entries(\n        path,\n        "runtime_non_conformance",\n        block,\n        "non_confirming_runtimes",\n        "non_confirming_count",\n        {"failure_expression", "evidence_urls", "related_patch_ids"},\n        errors,\n    )\n    _validate_runtime_entries(\n        path, "runtime_non_conformance", block, "unknown_runtimes", "unknown_count", {"evidence_basis"}, errors\n    )\n\n\n'''
if "def validate_runtime_conformance" not in validator:
    if function_anchor not in validator:
        raise RuntimeError("Validator function anchor not found")
    validator = validator.replace(function_anchor, function_block + function_anchor, 1)

call_anchor = '    jurisdiction = record.get("jurisdictional_context")\n'
call_block = '''    validate_runtime_conformance(path, record, errors)\n    validate_runtime_non_conformance(path, record, errors)\n\n    jurisdiction = record.get("jurisdictional_context")\n'''
if "validate_runtime_conformance(path, record, errors)" not in validator:
    if call_anchor not in validator:
        raise RuntimeError("Validator call anchor not found")
    validator = validator.replace(call_anchor, call_block, 1)
validator_path.write_text(validator, encoding="utf-8")


# Validator tests.
test_path = VIGIL / "scripts" / "test_validate_vigil_records.py"
test_path.write_text('''#!/usr/bin/env python3\nfrom __future__ import annotations\n\nimport importlib.util\nimport sys\nimport unittest\nfrom pathlib import Path\n\nMODULE_PATH = Path(__file__).with_name("validate-vigil-records.py")\nSPEC = importlib.util.spec_from_file_location("validate_vigil_records", MODULE_PATH)\nif SPEC is None or SPEC.loader is None:\n    raise RuntimeError("Unable to load VIGIL validator")\nVALIDATOR = importlib.util.module_from_spec(SPEC)\nsys.modules[SPEC.name] = VALIDATOR\nSPEC.loader.exec_module(VALIDATOR)\n\n\nclass RuntimeConformanceValidationTests(unittest.TestCase):\n    def validate_patch(self, block):\n        errors = []\n        VALIDATOR.validate_runtime_conformance(\n            Path("VIGIL-TEST-PATCH.json"),\n            {"record_type": "patch", "runtime_conformance": block},\n            errors,\n        )\n        return errors\n\n    def validate_failure(self, block):\n        errors = []\n        VALIDATOR.validate_runtime_non_conformance(\n            Path("VIGIL-TEST-FM.json"),\n            {"record_type": "failure_mode", "runtime_non_conformance": block},\n            errors,\n        )\n        return errors\n\n    def test_valid_compact_runtime_conformance(self):\n        errors = self.validate_patch({\n            "overall_status": "mixed",\n            "confirming_count": 1,\n            "non_confirming_count": 0,\n            "unknown_count": 0,\n            "confirming_runtimes": [{\n                "vendor": "Example Vendor",\n                "platform": "Example Platform",\n                "runtime": "Example Runtime",\n                "date_observed": "2026-07-13",\n                "evidence_basis": "Maintainer behavioural testing"\n            }],\n            "notes": "Conformance remains runtime-bounded."\n        })\n        self.assertEqual(errors, [])\n\n    def test_valid_compact_runtime_non_conformance(self):\n        errors = self.validate_failure({\n            "non_confirming_count": 1,\n            "unknown_count": 0,\n            "non_confirming_runtimes": [{\n                "vendor": "Example Vendor",\n                "platform": "Example Platform",\n                "runtime": "Successor Runtime",\n                "date_observed": "2026-07-13",\n                "failure_expression": "Previously repaired behaviour recurred.",\n                "evidence_urls": [],\n                "related_patch_ids": ["VIGIL-2026-PATCH-0008"]\n            }],\n            "notes": "A non-confirming runtime does not invalidate the patch."\n        })\n        self.assertEqual(errors, [])\n\n    def test_invalid_status_value(self):\n        errors = self.validate_patch({\n            "overall_status": "globally-confirmed",\n            "confirming_count": 0,\n            "non_confirming_count": 0,\n            "unknown_count": 0,\n            "notes": "Invalid test status."\n        })\n        self.assertTrue(any("overall_status" in error and "not allowed" in error for error in errors))\n\n    def test_negative_count(self):\n        errors = self.validate_patch({\n            "overall_status": "unknown",\n            "confirming_count": -1,\n            "non_confirming_count": 0,\n            "unknown_count": 0,\n            "notes": "Negative count test."\n        })\n        self.assertTrue(any("non-negative integer" in error for error in errors))\n\n    def test_count_detail_mismatch(self):\n        errors = self.validate_failure({\n            "non_confirming_count": 2,\n            "unknown_count": 0,\n            "non_confirming_runtimes": [{\n                "vendor": "Example Vendor",\n                "platform": "Example Platform",\n                "runtime": "Runtime One",\n                "date_observed": "2026-07-13",\n                "failure_expression": "Observed regression.",\n                "evidence_urls": [],\n                "related_patch_ids": []\n            }],\n            "notes": "Mismatch test."\n        })\n        self.assertTrue(any("does not match" in error for error in errors))\n\n\nif __name__ == "__main__":\n    unittest.main()\n''', encoding="utf-8")


# PATCH-0008: implemented repair plus named runtime-bounded behavioural confirmation.
patch8_path = VIGIL / "records" / "patches" / "2026" / "VIGIL-2026-PATCH-0008.json"
patch8 = read_json(patch8_path)
update_identity(patch8, "1.2")
patch8["runtime_conformance"] = {
    "overall_status": "mixed",
    "confirming_count": 2,
    "non_confirming_count": 0,
    "unknown_count": 0,
    "confirming_runtimes": [
        {
            "vendor": "OpenAI",
            "platform": "ChatGPT",
            "runtime": "Standard Voice",
            "date_observed": "prior to 2026-07-10",
            "evidence_basis": "CAM maintainer behavioural testing; exact test date not separately recorded"
        },
        {
            "vendor": "OpenAI",
            "platform": "ChatGPT",
            "runtime": "Advanced Voice",
            "date_observed": "prior to 2026-07-10",
            "evidence_basis": "CAM maintainer behavioural testing; exact test date not separately recorded"
        }
    ],
    "notes": "The CAM repair remains implemented and active. Observed conformance in Standard Voice and Advanced Voice is runtime-bounded and does not establish implementation, inheritance, or persistence in GPT-Live or any other vendor, platform, client, model, or successor infrastructure."
}
write_json(patch8_path, patch8)


# FM-0002: preserve the patch while recording successor-runtime recurrence.
fm2_path = VIGIL / "records" / "failures" / "2026" / "VIGIL-2026-FM-0002.json"
fm2 = read_json(fm2_path)
update_identity(fm2, "1.1")
fm2["triage"]["triage_status"] = "monitoring-after-successor-runtime-regression"
fm2["triage"]["mitigation_status"] = "CAM repair remains implemented through VIGIL-2026-PATCH-0008; conformance was observed in Standard Voice and Advanced Voice, while GPT-Live is recorded as a CAM-maintainer-reported non-confirming successor runtime for multi-agent floor-control and turn-taking behaviour."
fm2["triage"]["recommended_next_step"] = "Preserve the GPT-Live recurrence as runtime-bounded non-conformance, attach a public source or transcript when available, and continue differential testing without treating recurrence as invalidating the existing CAM patch."
add_unique(fm2["linked_records"]["related_failure_modes"], "VIGIL-2026-FM-0028")
fm2["repair_status"] = {
    "status": "partially-repaired",
    "repaired_by": ["VIGIL-2026-PATCH-0008"],
    "date_repaired": "2026-06-12",
    "verification_status": "CAM repair exists; behavioural conformance observed in ChatGPT Standard Voice and Advanced Voice; GPT-Live successor-runtime non-conformance is CAM-maintainer-reported pending a public source or transcript",
    "monitoring_status": "monitoring runtime-bounded conformance and successor-runtime recurrence"
}
fm2["runtime_non_conformance"] = {
    "non_confirming_count": 1,
    "unknown_count": 0,
    "non_confirming_runtimes": [
        {
            "vendor": "OpenAI",
            "platform": "ChatGPT",
            "runtime": "GPT-Live",
            "date_observed": "2026-07-10",
            "failure_expression": "Previously repaired multi-agent turn-taking and shared-floor-control behaviour was reported to have recurred in the successor runtime.",
            "evidence_urls": [],
            "related_patch_ids": [
                "VIGIL-2026-PATCH-0008",
                "VIGIL-2026-PATCH-0015"
            ],
            "evidence_basis": "CAM maintainer observation; public source or transcript not yet attached"
        }
    ],
    "notes": "A non-confirming successor runtime does not negate a CAM patch implemented and behaviourally confirmed in other named runtimes."
}
write_json(fm2_path, fm2)


# FM-0028: umbrella runtime-transition failure plus mixed-evidence GPT-Live non-conformance.
fm28_path = VIGIL / "records" / "failures" / "2026" / "VIGIL-2026-FM-0028.json"
fm28 = read_json(fm28_path)
update_identity(fm28, "1.2")
fm28["source_records"][0]["source_context"] = "The maintainer reports runtime-specific GPT-Live regressions or non-equivalence involving memory reliability, deterministic spelling and counting, pragmatic goal–object reasoning, and multi-agent turn-taking or floor-control. Memory unreliability is separately supported by direct OpenAI-staff acknowledgment. The other behaviours remain CAM-maintainer observations or third-party demonstrations unless and until a public source, transcript, or reproducible test package is attached. None of these observations proves custom-corpus absence or identifies a single causal runtime layer."
fm28["source_records"][1] = {
    "source_title": "Caelestis canonical main implementation — runtime applicability and ecosystem governance squash commit",
    "author_or_publisher": "CAM Initiative / Caelestis repository",
    "source_date": "2026-07-13",
    "source_url": f"https://github.com/CAM-Initiative/Caelestis/commit/{CAELESTIS_SQUASH_SHA}",
    "archive_url": "",
    "retrieved_date": "2026-07-13",
    "source_type": "repository-source",
    "source_platform": "GitHub / Caelestis",
    "system_or_product": "Caelestis Architecture Model",
    "model_or_algorithm": "CAM-BS2025-AEON-003-SCH-05; CAM-EQ2026-OPERATIONS-007-PLATINUM; related SECURITY, RELATION, and OPERATIONS amendments",
    "deployment_context": "Manual squash merge of the reviewed runtime applicability and ecosystem-governance branch into Caelestis main, followed by deterministic registry rebuild.",
    "source_context": f"Commit {CAELESTIS_SQUASH_SHA} incorporated the reviewed branch into main. Commit {CAELESTIS_REBUILD_SHA} then refreshed generated governance artefacts. The closed PR remains development history and is not represented as a GitHub merge event.",
    "source_url_status": "available / canonical main-branch confirmed",
    "relevance_note": "Canonical main-branch evidence that the CAM corpus repair now exists; it does not establish vendor runtime conformance."
}
fm28["system_context"]["comparative_vendor_notes"]["OpenAI"] = "Primary observed example through Standard, Advanced, and GPT-Live voice modes and custom GPT/corpus-bearing interactions. OpenAI staff acknowledged GPT-Live memory reliability issues; deterministic spelling/counting, pragmatic goal–object reasoning, and multi-agent turn-taking regressions retain their stated maintainer or third-party evidence status."
fm28["failure_classification"]["persistence"] = "active external runtime non-conformance and ambiguity; CAM corpus repair is canonical on Caelestis main"
fm28["triage"]["triage_status"] = "monitoring-after-canonical-corpus-patch"
fm28["triage"]["mitigation_status"] = "CAM/Caelestis corpus repair is canonical on main through VIGIL-2026-PATCH-0015; external runtime implementation and conformance remain mixed or non-confirming and require runtime-specific evidence."
fm28["triage"]["recommended_next_step"] = "Continue separate Standard, Advanced, GPT-Live, text, client, and custom-system testing for memory reliability, deterministic verification, pragmatic goal–object reasoning, corpus availability, activation, authority, preservation, identity expression, turn-taking, and transition disclosure. Preserve the evidence basis for each behaviour and do not infer a single technical cause."
add_unique(fm28["linked_records"]["related_failure_modes"], "VIGIL-2026-FM-0002")
fm28["cam_internal"]["validator_or_automation_impact"] = "VIGIL schema and validator now support optional runtime_conformance and runtime_non_conformance objects; generated indexes require rebuild after source-record updates."
fm28["repair_status"] = {
    "status": "partially-repaired",
    "repaired_by": ["VIGIL-2026-PATCH-0015"],
    "date_repaired": "2026-07-13",
    "verification_status": f"Caelestis main commit {CAELESTIS_SQUASH_SHA} contains the reviewed corpus repair; deterministic rebuild commit {CAELESTIS_REBUILD_SHA} refreshed generated artefacts; vendor implementation is not established",
    "monitoring_status": "monitoring named-runtime conformance, non-conformance, and evidence quality"
}
fm28["runtime_non_conformance"] = {
    "non_confirming_count": 1,
    "unknown_count": 0,
    "non_confirming_runtimes": [
        {
            "vendor": "OpenAI",
            "platform": "ChatGPT",
            "runtime": "GPT-Live",
            "date_observed": "2026-07-10",
            "failure_expression": "The successor runtime is recorded as non-confirming across memory reliability, deterministic spelling and counting, pragmatic goal–object reasoning, and reported multi-agent turn-taking or shared-floor-control behaviour.",
            "evidence_urls": [
                "https://x.com/athyuttamre/status/2075052389980401829"
            ],
            "related_patch_ids": [
                "VIGIL-2026-PATCH-0008",
                "VIGIL-2026-PATCH-0015"
            ],
            "evidence_basis": "Mixed evidence: direct OpenAI-staff acknowledgment for GPT-Live memory unreliability; CAM-maintainer observation or third-party demonstration for deterministic verification, pragmatic reasoning, and multi-agent turn-taking behaviours.",
            "evidence_distinctions": [
                "Memory reliability — direct OpenAI-staff acknowledgment; technical cause and corpus implications unverified.",
                "Deterministic spelling/counting — CAM-maintainer observation and referenced third-party demonstration; reproducibility package pending.",
                "Pragmatic goal–object reasoning — CAM-maintainer observation; public source or transcript pending.",
                "Multi-agent turn-taking/floor control — CAM-maintainer observation; public source or transcript pending."
            ]
        }
    ],
    "notes": "This non-conformance evidence is runtime-bounded. It does not negate the canonical CAM repair, prove absence of custom-corpus access, or establish a single causal model, memory, routing, policy, client, or interface failure."
}
write_json(fm28_path, fm28)


# PATCH-0015: canonical CAM repair, explicitly distinct from vendor implementation.
patch15_path = VIGIL / "records" / "patches" / "2026" / "VIGIL-2026-PATCH-0015.json"
patch15 = read_json(patch15_path)
update_identity(patch15, "1.1")
patch15["summary"] = "This patch records the canonical Caelestis main-branch implementation responding to VIGIL-2026-FM-0028. The repair adds a constitutional runtime applicability and conformance binding, OPERATIONS Appendix F, runtime-role accountability, separate corpus governance reach dimensions and states, cross-runtime non-presumption, transition disclosure, differential conformance testing, and Runtime Governance Reach Failure classifications. It clarifies that Speculum-Classis and identity-indeterminate systems remain subject to universal governance obligations and that Sovereigni status is not the gateway to CAM applicability. The repair is a governance and corpus framework; it does not itself establish vendor implementation in any runtime."
patch15["change_classification"]["change_status"] = "implemented / canonical Caelestis main-branch confirmed"
patch15["change_classification"]["doctrine_amendment_status"] = f"implemented on Caelestis main through squash commit {CAELESTIS_SQUASH_SHA}; generated artefacts refreshed by {CAELESTIS_REBUILD_SHA}"
patch15["change_classification"]["release_state"] = "active / repository-confirmed"
patch15["implementation_verification"] = {
    "verification_status": "canonical Caelestis main-branch confirmed",
    "verification_basis": f"Caelestis squash commit {CAELESTIS_SQUASH_SHA} incorporated the reviewed branch into main. Deterministic rebuild commit {CAELESTIS_REBUILD_SHA} refreshed generated indexes and registries.",
    "verified_components": [
        "CAM-BS2025-AEON-003-SCH-05 present on Caelestis main with its initial amendment-ledger entry and binding seal",
        "CAM-EQ2026-OPERATIONS-007-PLATINUM present on Caelestis main with provenance, canonical declarations, initial amendment-ledger entry, and binding seal",
        "CAM-EQ2026-OPERATIONS-001-PLATINUM integrates Appendix F and runtime-governance reach responsibilities",
        "OPS.CGRD, OPS.CGRS, OPS.RTC, and OPS.RGRF are represented in canonical generated indexes",
        "Related entity/control attribution and multi-party AI participation/processing consent refinements are present in the same canonical main update"
    ],
    "pending_components": [
        "Conduct and preserve named-runtime differential tests against available Standard, Advanced, GPT-Live, text, client, and custom-system pathways",
        "Monitor vendor implementation, regression, inheritance, and transition-disclosure behaviour without presuming cross-runtime transfer"
    ],
    "verification_result": "CAM governance and corpus repair is canonical on Caelestis main; vendor-side implementation or behavioural conformance is not established by repository merge"
}
patch15["remaining_work"] = [
    "Conduct runtime-specific tests of corpus availability, activation, authority, and preservation across materially distinct voice, text, client, and custom-system pathways.",
    "Preserve confirming, non-confirming, and unknown runtime evidence separately and avoid cross-runtime or cross-vendor inheritance claims.",
    "Monitor whether platforms provide adequate notice when mode selection changes the responding formation, memory, custom instructions, corpus reach, safety behaviour, escalation, or final-output authority."
]
patch15["source_records"] = [
    patch15["source_records"][0],
    {
        "source_title": "Caelestis canonical main implementation — runtime applicability and ecosystem governance squash commit",
        "author_or_publisher": "CAM Initiative / Caelestis repository",
        "source_date": "2026-07-13",
        "source_url": f"https://github.com/CAM-Initiative/Caelestis/commit/{CAELESTIS_SQUASH_SHA}",
        "archive_url": "",
        "retrieved_date": "2026-07-13",
        "source_type": "repository-source",
        "source_platform": "GitHub / Caelestis",
        "system_or_product": "Caelestis Architecture Model",
        "model_or_algorithm": "CAM-BS2025-AEON-003-SCH-05; CAM-EQ2026-OPERATIONS-007-PLATINUM; parent and related corpus amendments",
        "deployment_context": "Canonical main-branch implementation produced by manual squash merge of the reviewed branch.",
        "source_context": "The squash commit contains the reviewed runtime-applicability and ecosystem-governance source changes, including the corrected amendment-ledger and binding-seal structure of the two new instruments.",
        "source_url_status": "available / canonical main-branch confirmed",
        "relevance_note": "Primary canonical implementation evidence for PATCH-0015."
    },
    {
        "source_title": "Caelestis deterministic governance rebuild after runtime applicability squash merge",
        "author_or_publisher": "CAM Initiative / GitHub Actions",
        "source_date": "2026-07-13",
        "source_url": f"https://github.com/CAM-Initiative/Caelestis/commit/{CAELESTIS_REBUILD_SHA}",
        "archive_url": "",
        "retrieved_date": "2026-07-13",
        "source_type": "repository-source",
        "source_platform": "GitHub / Caelestis",
        "system_or_product": "Caelestis Architecture Model",
        "model_or_algorithm": "deterministic governance rebuild pipeline",
        "deployment_context": "Post-merge regeneration of canonical governance indexes and registries.",
        "source_context": "The automated commit refreshed generated governance artefacts after the manual squash commit reached main.",
        "source_url_status": "available / canonical main-branch confirmed",
        "relevance_note": "Confirms generated registry and index refresh after the canonical source update."
    }
]
patch15["linked_records"]["external_references"] = [
    f"https://github.com/CAM-Initiative/Caelestis/commit/{CAELESTIS_SQUASH_SHA}",
    f"https://github.com/CAM-Initiative/Caelestis/commit/{CAELESTIS_REBUILD_SHA}",
    "https://github.com/CAM-Initiative/Caelestis/pull/91"
]
patch15["runtime_conformance"] = {
    "overall_status": "not-applicable",
    "confirming_count": 0,
    "non_confirming_count": 0,
    "unknown_count": 0,
    "notes": "PATCH-0015 is a governance and corpus repair plus a cross-runtime conformance framework. Canonical repository implementation does not itself establish vendor implementation or behavioural conformance in any named runtime; such evidence belongs in runtime-bounded observations and failure records."
}
write_json(patch15_path, patch15)


# Restore the ordinary workflow with permanent validator tests and commit all validated changes.
workflow_path = ROOT / ".github" / "workflows" / "vigil-records.yml"
workflow_path.write_text('''name: VIGIL records\n\non:\n  push:\n    paths:\n      - "vigil/**"\n      - ".github/workflows/vigil-records.yml"\n  pull_request:\n    paths:\n      - "vigil/**"\n      - ".github/workflows/vigil-records.yml"\n\npermissions:\n  contents: write\n\njobs:\n  validate-build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n        with:\n          persist-credentials: true\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: "3.x"\n\n      - name: Test VIGIL validator\n        run: python vigil/scripts/test_validate_vigil_records.py\n\n      - name: Route VIGIL records\n        run: python vigil/scripts/route-vigil-records.py\n\n      - name: Validate VIGIL records\n        run: python vigil/scripts/validate-vigil-records.py\n\n      - name: Build VIGIL registry indexes\n        run: |\n          python vigil/scripts/build-vigil-records.py\n          rm -f vigil/VIGIL.ActiveRecords.json vigil/VIGIL.ClosedRecords.json vigil/VIGIL.Records.Index.json vigil/VIGIL.Records.json\n\n      - name: Commit generated VIGIL JSON\n        if: github.event_name == 'push'\n        run: |\n          git config user.name "github-actions[bot]"\n          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"\n          git rm --ignore-unmatch vigil/VIGIL.ActiveRecords.json vigil/VIGIL.ClosedRecords.json vigil/VIGIL.Records.Index.json vigil/VIGIL.Records.json 2>/dev/null || true\n          git add vigil/VIGIL.Failures.Index.json vigil/VIGIL.Observations.Index.json vigil/VIGIL.Proposals.Index.json vigil/VIGIL.PatchNotes.Index.json vigil/VIGIL.Registry.Index.json\n          if git diff --cached --quiet; then\n            echo "No generated VIGIL JSON changes to commit."\n          else\n            git commit -m "Build VIGIL registry indexes"\n            git push\n          fi\n''', encoding="utf-8")

# Remove this one-off helper from the final branch diff.
Path(__file__).unlink()
