"""Gate 1: retain current review attribution, not cumulative AI review diaries."""
from __future__ import annotations

import copy
import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"


def load_script(filename: str, name: str):
    spec = importlib.util.spec_from_file_location(name, VIGIL / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


MAIN = load_script("validate-vigil-records.py", "vigil_current_provenance_main")
SECOND = load_script("validate-vigil-interpretive-provenance.py", "vigil_current_provenance_second")


def current():
    return {
        "review_id": "test-review-2026-10-28",
        "reviewer_type": "AI analytical reviewer",
        "reviewer_platform": "test fixture",
        "reviewer_model": "synthetic",
        "review_date": "2026-10-28",
        "review_scope": "Current source-first assessment",
        "capability_profile": {"source_checks": True},
        "known_limitations": ["No human source verification asserted"],
        "review_outcome": "Current findings retained without accumulating previous process passes.",
    }


def incident():
    return {
        "id": "VIGIL-INC-000001",
        "record_identity": {"created": "2026-10-27"},
        "date_recorded": "2026-10-27",
        "interpretive_provenance": {
            "current_ai_review": current(),
            "human_governance_editor": None,
        },
        "source_records": [],
    }


class CurrentReviewProvenanceTest(unittest.TestCase):
    def structural_errors(self, record):
        errors = []
        MAIN.validate_provenance(Path("synthetic.json"), record, errors)
        return errors

    def file_validator(self, record):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = root / "incidents"
            directory.mkdir()
            (directory / "VIGIL-INC-000001.json").write_text(
                json.dumps(record, indent=2) + "\n", encoding="utf-8"
            )
            with patch.object(SECOND, "RECORDS", root):
                with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                    return SECOND.main()

    def test_current_only_passes_both_validators(self):
        row = incident()
        self.assertEqual(self.structural_errors(row), [])
        self.assertEqual(self.file_validator(row), 0)

    def test_complete_existing_legacy_history_remains_accepted(self):
        row = incident()
        row["interpretive_provenance"]["review_history"] = [copy.deepcopy(current())]
        self.assertEqual(self.structural_errors(row), [])
        self.assertEqual(self.file_validator(row), 0)

    def test_legacy_history_must_not_be_empty_if_explicitly_retained(self):
        row = incident()
        row["interpretive_provenance"]["review_history"] = []
        self.assertTrue(any("review_history" in x for x in self.structural_errors(row)))
        self.assertEqual(self.file_validator(row), 1)

    def test_legacy_current_must_reconcile_to_retained_history(self):
        row = incident()
        old = current()
        old["review_id"] = "old-review"
        row["interpretive_provenance"]["review_history"] = [old]
        self.assertTrue(any("resolve" in x for x in self.structural_errors(row)))
        self.assertEqual(self.file_validator(row), 1)

    def test_does_not_drop_full_current_review_requirements(self):
        row = incident()
        del row["interpretive_provenance"]["current_ai_review"]["known_limitations"]
        self.assertTrue(any("missing" in x for x in self.structural_errors(row)))
        self.assertEqual(self.file_validator(row), 1)

    def test_human_authorship_cannot_be_fabricated_by_current_reviewer(self):
        row = incident()
        row["interpretive_provenance"]["current_ai_review"]["reviewer_type"] = "human reviewer"
        self.assertTrue(any("AI analytical reviewer" in x for x in self.structural_errors(row)))
        self.assertEqual(self.file_validator(row), 1)

    def test_provenance_index_and_archive_are_not_permitted(self):
        for extra in ("review_history_index", "review_archive_batches"):
            with self.subTest(extra=extra):
                row = incident()
                row["interpretive_provenance"][extra] = []
                self.assertTrue(any(extra in x for x in self.structural_errors(row)))
                self.assertEqual(self.file_validator(row), 1)

    def test_current_review_must_not_predate_record(self):
        row = incident()
        row["interpretive_provenance"]["current_ai_review"]["review_date"] = "2026-10-20"
        self.assertEqual(self.file_validator(row), 1)

    def test_current_review_date_must_be_calendar_date(self):
        row = incident()
        row["interpretive_provenance"]["current_ai_review"]["review_date"] = "2026-13-99"
        self.assertEqual(self.file_validator(row), 1)

    def test_source_evidence_and_findings_untouched_by_compaction(self):
        row = incident()
        row["vigil_assessment"] = {"source_clause_analysis": {"clauses": [{"episode_id": "E1"}]}}
        row["taxonomy_classification"] = {"classification_basis": "Synthetic bounded result"}
        before = copy.deepcopy(row)
        row["interpretive_provenance"].pop("review_history", None)
        self.assertEqual(row, before)


if __name__ == "__main__":
    unittest.main()
