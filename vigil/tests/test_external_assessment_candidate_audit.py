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
    def test_review_flags_are_traceable_and_not_auto_admitted(self):
        """Candidates are an accountable review queue, not automatically failed assessments."""
        import json

        flags = AUDIT.unresolved_candidates()
        self.assertEqual(
            len(flags),
            len({(flag["incident"], flag["source_ref"]) for flag in flags}),
            "Review candidates must have unique incident/source references",
        )
        for flag in flags:
            with self.subTest(incident=flag["incident"], source=flag["source_ref"]):
                incident_path = AUDIT.INCIDENT_DIR / (flag["incident"] + ".json")
                self.assertTrue(incident_path.is_file())
                record = json.loads(incident_path.read_text(encoding="utf-8"))
                self.assertEqual(record["id"], flag["incident"])
                self.assertTrue(flag["source_ref"].startswith("source_records["))
                self.assertTrue(flag["source_ref"].endswith("]"))
                source_index = int(flag["source_ref"][len("source_records["):-1])
                source = record["source_records"][source_index]
                self.assertTrue(AUDIT.source_is_candidate(source))
                self.assertNotIn(
                    (record["id"], source_index), AUDIT.REVIEWED_NON_ASSESSMENTS
                )
                assessed_refs = {
                    ref
                    for assessment in (record.get("external_assessments") or [])
                    for ref in (assessment.get("source_record_refs") or [])
                }
                self.assertNotIn(flag["source_ref"], assessed_refs)
                for field, source_field in (
                    ("publisher", "author_or_publisher"),
                    ("source_type", "source_type"),
                    ("source_title", "source_title"),
                    ("source_url", "source_url"),
                ):
                    self.assertEqual(flag[field], source.get(source_field))
                self.assertIn("review required", flag["review_note"].lower())

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

