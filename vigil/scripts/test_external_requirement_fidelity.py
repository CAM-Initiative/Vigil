import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).with_name("validate-external-requirement-fidelity.py")
spec = importlib.util.spec_from_file_location("validate_external_requirement_fidelity", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class ExternalRequirementFidelityTests(unittest.TestCase):
    def test_current_fidelity_ledger_is_structurally_valid(self):
        errors, warnings, summary = module.validate()
        self.assertEqual(errors, [])
        self.assertGreaterEqual(summary["historical_complete_sources"], 2)
        self.assertEqual(summary["fidelity_assured_effective_complete_sources"], 6)
        self.assertGreaterEqual(summary["effective_partial_due_fidelity"], 1)
        self.assertTrue(any("effective downgrade" in warning for warning in warnings))

    def test_eu_ai_act_is_not_fidelity_assured(self):
        fidelity = module.load(module.FIDELITY_PATH)
        target = next(
            entry
            for entry in fidelity["entries"]
            if entry["external_source_id"] == "EU-AI-ACT-2024-1689"
            and entry["source_version"] == "2026-07-27"
        )
        self.assertEqual(target["fidelity_status"], "requires-reextraction")
        self.assertEqual(target["effective_extraction_status"], "partial")

    def test_reviewed_source_fidelity_dispositions_are_explicit(self):
        fidelity = module.load(module.FIDELITY_PATH)
        status = {
            (entry["external_source_id"], entry["source_version"]): entry["fidelity_status"]
            for entry in fidelity["entries"]
        }
        self.assertEqual(status[("NIST-AI-100-1", "1.0")], "assured")
        self.assertEqual(status[("CYCLONEDX-SPEC", "1.7")], "assured")
        self.assertEqual(status[("NIST-AI-600-1", "2024")], "assured")
        self.assertEqual(status[("NIST-SP-800-218A", "2024")], "assured")
        self.assertEqual(status[("IMDA-AGENTIC-AI-MGF", "2026-05")], "assured")
        self.assertEqual(status[("AAM-SDOS-RUNTIME-GOVERNANCE", "1.10")], "assured")


if __name__ == "__main__":
    unittest.main()
