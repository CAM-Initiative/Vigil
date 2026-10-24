"""Regression tests for the sparse, assessment-only public HIM sidecar."""

import importlib.util
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "build-vigil-public-records.py"
spec = importlib.util.spec_from_file_location("vigil_public_index_generator", MODULE)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class SparseHarmIndexTests(unittest.TestCase):
    def test_only_assessed_rows_are_projected_and_s1_is_retained(self):
        record = {
            "id": "VIGIL-INC-999998",
            "record_identity": {"version": "2.3.0"},
            "harm_impact_assessment": {
                "assessment_pathway": "generic_deployed_evaluation",
                "dimensions": [
                    {"dimension_id": "privacy-confidentiality", "assessment_status": "assessed", "severity": "S3"},
                    {"dimension_id": "psychological-wellbeing", "assessment_status": "unreported"},
                    {"dimension_id": "physical-health-safety", "assessment_status": "assessed", "severity": "S1"},
                    {"dimension_id": "rights-liberty", "assessment_status": "insufficient-evidence"},
                ],
            },
        }
        result = builder.harm_dimension_sidecar([record])
        self.assertEqual(result["record_count"], 1)
        self.assertEqual(result["assessed_record_count"], 1)
        self.assertEqual(result["entries"], [{
            "id": record["id"], "v": "2.3.0",
            "p": "generic_deployed_evaluation",
            "d": [["privacy-confidentiality", "S3"], ["physical-health-safety", "S1"]],
        }])
        self.assertEqual(result["provenance"]["generation_mode"], "deterministic-generation")

    def test_no_assessed_dimensions_does_not_imply_no_harm(self):
        record = {"id": "VIGIL-INC-999997", "harm_impact_assessment": {
            "overall_severity": "SU",
            "dimensions": [{"dimension_id": "privacy-confidentiality", "assessment_status": "unreported"}]}}
        result = builder.harm_dimension_sidecar([record])
        self.assertEqual(result["record_count"], 1)
        self.assertEqual(result["assessed_record_count"], 0)
        self.assertEqual(result["entries"], [])

    def test_invalid_and_duplicate_assessed_dimensions_are_rejected(self):
        base = {"id": "VIGIL-INC-999996", "harm_impact_assessment": {"dimensions": []}}
        for bad in [
            [{"dimension_id": "privacy-confidentiality", "assessment_status": "assessed"}],
            [{"dimension_id": "privacy-confidentiality", "assessment_status": "assessed", "severity": "SU"}],
            [
                {"dimension_id": "privacy-confidentiality", "assessment_status": "assessed", "severity": "S2"},
                {"dimension_id": "privacy-confidentiality", "assessment_status": "assessed", "severity": "S3"},
            ],
        ]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                builder.harm_dimension_sidecar([{**base, "harm_impact_assessment": {"dimensions": bad}}])


if __name__ == "__main__":
    unittest.main()
