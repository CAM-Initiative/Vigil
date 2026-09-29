import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "vigil" / "scripts" / "build-incident-external-requirement-candidate-matrix.py"
SPEC = importlib.util.spec_from_file_location("build_vigil_extreq_candidate_matrix", SCRIPT)
BUILDER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(BUILDER)

REQ_A = "EXTREQ-0123456789ABCDEF"
REQ_STALE = "EXTREQ-AAAAAAAAAAAAAAAA"


class ExternalRequirementCandidateMatrixTests(unittest.TestCase):
    def setUp(self):
        self.classes = {
            "VIGIL-FC-000001": {
                "external_references": [
                    {"requirement_id": REQ_A, "reference_role": "regulatory-evidence", "clause_or_control": "Article 1"},
                    {"title": "Research paper", "publisher": "Example Lab", "date": "2025-01-01", "url": "https://example.invalid/paper", "reference_role": "research-evidence"},
                ],
            },
            "VIGIL-FC-000002": {
                "external_references": [
                    {"requirement_id": REQ_A, "reference_role": "regulatory-evidence", "clause_or_control": "Article 1"},
                    {"requirement_id": REQ_STALE, "reference_role": "regulatory-evidence", "title": "Stale citation"},
                ],
            },
            "VIGIL-FC-000003": {
                "external_references": [
                    {"title": "Context only", "publisher": "Example", "date": "2025-01-01", "url": "https://example.invalid/context", "reference_role": "authoritative-guidance"},
                ],
            },
        }
        self.requirements = {
            REQ_A: {
                "requirement_id": REQ_A,
                "external_source_id": "EU-AI-ACT",
                "source_version": "2026-07-27",
                "canonical_source_identifier": {"value": "02024R1689-20260727"},
            },
        }
        self.records = [{
            "id": "VIGIL-INC-000001",
            "record_state": "active",
            "record_identity": {"title": "Synthetic incident"},
            "taxonomy_classification": {
                "primary_classification": {"class_id": "VIGIL-FC-000001", "classification_role": "ambiguous-boundary"},
                "secondary_classifications": [{"class_id": "VIGIL-FC-000002", "classification_role": "failure-occurrence"}],
            },
            "standards_and_regulatory_references": [f"Context only {REQ_A}"],
        }]

    def test_candidates_merge_classes_but_do_not_adjudicate(self):
        rows, summary = BUILDER.build_candidates(self.records, self.classes, self.requirements)
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["requirement_id"], REQ_A)
        self.assertEqual(row["derived_from_class_ids"], ["VIGIL-FC-000001", "VIGIL-FC-000002"])
        self.assertEqual(row["adjudication_status"], "needs-applicability-adjudication")
        self.assertEqual(row["taxonomy_reference_roles"], ["regulatory-evidence"])
        self.assertEqual(summary["unique_incident_requirement_relationships"], 1)
        self.assertEqual(summary["relationships_derived_from_multiple_fidelity_classes"], 1)

    def test_unstructured_context_and_unresolved_ids_do_not_create_candidates(self):
        rows, summary = BUILDER.build_candidates(self.records, self.classes, self.requirements)
        self.assertEqual([row["requirement_id"] for row in rows], [REQ_A])
        self.assertIn(REQ_STALE, summary["unresolved_structured_requirement_ids"])
        self.assertEqual(summary["unmapped_external_reference_rows_without_requirement_id"], 2)
        self.assertEqual(summary["standards_and_regulatory_context_overlap"]["explicit_requirement_ids_in_context_text_only"], [REQ_A])

    def test_monitoring_record_is_in_current_corpus(self):
        record = dict(self.records[0], record_state="monitoring")
        _, summary = BUILDER.build_candidates([record], self.classes, self.requirements)
        self.assertEqual(summary["current_incident_records"], 1)
        self.assertEqual(summary["record_state_breakdown"], {"monitoring": 1})


if __name__ == "__main__":
    unittest.main()
