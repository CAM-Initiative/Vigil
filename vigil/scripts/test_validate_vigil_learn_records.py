#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
MODULE_PATH = SCRIPT_DIR / "validate-vigil-learn-records.py"
SPEC = importlib.util.spec_from_file_location("validate_vigil_learn_records", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load VIGIL LEARN validator")
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)

VIGIL_DIR = SCRIPT_DIR.parent
SCHEMA = json.loads((VIGIL_DIR / "VIGIL.Learn.Schema.json").read_text(encoding="utf-8"))
EXEMPLAR = json.loads(
    (
        VIGIL_DIR
        / "records"
        / "learn"
        / "2026"
        / "VIGIL-2026-LEARN-0001.json"
    ).read_text(encoding="utf-8")
)


class LearnCompletionContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.records = VALIDATOR.canonical_records()

    def validate(self, record):
        return VALIDATOR.validate_record(
            Path(f"{record['id']}.json"),
            record,
            SCHEMA,
            {**self.records, record["id"]: record},
        )

    def proposal_optional_record(self):
        record = copy.deepcopy(EXEMPLAR)
        record["learning_basis"]["proposal_records"] = []
        record["linked_records"]["related_proposals"] = []
        record["report_section_sources"]["section_02_record"]["record_ids"] = [
            "VIGIL-2026-FM-0044",
            "VIGIL-2026-PATCH-0025",
            "VIGIL-2026-LEARN-0001",
        ]
        record["report_section_sources"]["section_04_diagnosis"] = {
            "record_ids": [
                "VIGIL-2026-FM-0044",
                "VIGIL-2026-PATCH-0025",
            ],
            "source_fields": ["triage", "change_details"],
            "basis": "The FM and PATCH populate diagnosis without a separate proposal.",
        }
        return record

    def test_complete_sections_do_not_require_proposal(self):
        errors = self.validate(self.proposal_optional_record())
        self.assertEqual(errors, [])

    def test_declared_source_field_must_exist(self):
        record = self.proposal_optional_record()
        record["report_section_sources"]["section_04_diagnosis"]["source_fields"] = [
            "field_that_does_not_exist"
        ]
        errors = self.validate(record)
        self.assertTrue(any("field_that_does_not_exist" in error for error in errors))

    def test_section_five_must_cite_authoritative_patch(self):
        record = self.proposal_optional_record()
        record["report_section_sources"]["section_05_repair"]["record_ids"] = [
            "VIGIL-2026-FM-0044"
        ]
        errors = self.validate(record)
        self.assertTrue(any("section_05_repair must cite a PATCH" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
