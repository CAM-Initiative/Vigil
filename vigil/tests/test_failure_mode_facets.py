import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "vigil" / "scripts" / "validate-vigil-records.py"
spec = importlib.util.spec_from_file_location("validate_vigil_records_facets", VALIDATOR)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class FailureModeFacetsTest(unittest.TestCase):
    def _record(self):
        path = ROOT / "vigil" / "tests" / "fixtures" / "valid" / "VIGIL-2026-FM-0001.json"
        return json.loads(path.read_text(encoding="utf-8"))

    def _validate(self, record):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / f"{record['id']}.json"
            path.write_text(json.dumps(record), encoding="utf-8")
            return validator.validate(path)

    def _valid_facets(self):
        return {
            "schema_version": "1.0",
            "event_state": "incident",
            "manifestation": ["Agent claimed completion although the external state did not change."],
            "mechanism_or_cause": ["Completion assessment relied on internal narration rather than external state verification."],
            "cause_status": "hypothesised",
            "failure_locus": ["tool-environment-interface"],
            "repair_side": ["harness", "tool-environment-interface"],
            "execution_phase": ["completion-assessment", "verification"],
            "observability": "differentially-observable",
            "evidence_state": "observed",
            "effect_or_harm": ["False success state presented to the user."],
            "propagation": "local",
            "completion_state": "false-completion",
            "verification_state": "incomplete",
            "execution_pattern": "single-pass",
            "reporting_notes": "Locus and repair side are intentionally separate.",
            "external_taxonomy_refs": ["OECD AI incident reporting framework", "IEC 60812:2018"]
        }

    def test_legacy_failure_without_facets_remains_valid(self):
        self.assertEqual(self._validate(self._record()), 0)

    def test_valid_faceted_failure_passes(self):
        record = self._record()
        record["failure_classification"]["faceted_analysis"] = self._valid_facets()
        self.assertEqual(self._validate(record), 0)

    def test_unknown_failure_locus_is_rejected(self):
        record = self._record()
        facets = self._valid_facets()
        facets["failure_locus"] = ["mystery-layer"]
        record["failure_classification"]["faceted_analysis"] = facets
        self.assertNotEqual(self._validate(record), 0)

    def test_unsubstantiated_custom_observability_label_is_rejected(self):
        record = self._record()
        facets = self._valid_facets()
        facets["observability"] = "fail-plausible"
        record["failure_classification"]["faceted_analysis"] = facets
        self.assertNotEqual(self._validate(record), 0)

    def test_economic_legitimacy_is_schema_valid(self):
        record = self._record()
        record["failure_classification"]["canonical_failure_group"] = "economic-legitimacy"
        record["failure_classification"]["related_failure_groups"] = ["economic-legitimacy"]
        self.assertEqual(self._validate(record), 0)


if __name__ == "__main__":
    unittest.main()
