import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "vigil" / "scripts" / "audit-vigil-external-assessment-candidates.py"
SPEC = importlib.util.spec_from_file_location("external_assessment_candidate_audit", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class ExternalAssessmentCandidateAuditTests(unittest.TestCase):
    def test_reconciled_corpus_has_no_unresolved_candidate_flags(self):
        self.assertEqual(AUDIT.unresolved_candidates(), [])

    def test_incident_database_is_not_an_automatic_candidate(self):
        source = {
            "source_type": "incident database entry",
            "source_title": "Incident registry assessment and analysis",
            "source_context": "The registry records that an incident occurred.",
        }
        self.assertFalse(AUDIT.source_is_candidate(source))

    def test_technical_evaluation_is_a_review_flag(self):
        source = {
            "source_type": "technical report",
            "source_title": "Evaluation of model behaviour",
            "source_context": "The evaluator reports measured findings.",
        }
        self.assertTrue(AUDIT.source_is_candidate(source))


if __name__ == "__main__":
    unittest.main()

