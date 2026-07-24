#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("validate-vigil-patch-trace.py")
SPEC = importlib.util.spec_from_file_location("validate_vigil_patch_trace", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load VIGIL PATCH trace validator")
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


class PatchTraceValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.caelestis = self.root / "Caelestis"
        self.records = self.root / "records"
        self.caelestis.mkdir()
        self.records.mkdir()
        subprocess.run(["git", "init", "-b", "main"], cwd=self.caelestis, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=self.caelestis, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=self.caelestis, check=True)
        source = self.caelestis / "Governance" / "Charters" / "CAM-TEST.md"
        source.parent.mkdir(parents=True)
        source.write_text("# CAM-TEST\n\n## 1 Exact Control\n\nLiteral implemented wording.\n", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=self.caelestis, check=True)
        subprocess.run(["git", "commit", "-m", "test corpus"], cwd=self.caelestis, check=True, capture_output=True)
        self.commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.caelestis,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

    def tearDown(self):
        self.temporary.cleanup()

    def write_record(self, resulting_text: str) -> None:
        record = {
            "id": "VIGIL-TEST-PATCH-0001",
            "corpus_implementation": {
                "canonical_state": "canonical-main",
                "entries": [
                    {
                        "section_heading": "1 Exact Control",
                        "prior_text": None,
                        "prior_text_status": "new-clause",
                        "resulting_text": resulting_text,
                        "source": {
                            "commit": self.commit,
                            "path": "Governance/Charters/CAM-TEST.md",
                        },
                        "verification": {
                            "current_clause_status": "current",
                        },
                    }
                ],
            },
        }
        (self.records / "VIGIL-TEST-PATCH-0001.json").write_text(json.dumps(record), encoding="utf-8")

    def test_exact_commit_text_passes(self):
        self.write_record("## 1 Exact Control\n\nLiteral implemented wording.")
        self.assertEqual(VALIDATOR.validate(self.caelestis, self.records, "main"), [])

    def test_paraphrased_text_fails(self):
        self.write_record("## 1 Exact Control\n\nParaphrased wording.")
        errors = VALIDATOR.validate(self.caelestis, self.records, "main")
        self.assertTrue(any("not an exact substring" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
