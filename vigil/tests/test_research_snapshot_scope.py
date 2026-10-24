"""Case-neutral regression: temporary review papers are never scientific release data."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
BUILDER = ROOT / "vigil/releases/siai-2026/build_research_snapshot.py"


def release_builder():
    spec = importlib.util.spec_from_file_location("vigil_release_inventory_scope", BUILDER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ReleaseScopeBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.builder = release_builder()

    def test_notice_board_not_part_of_scientific_scope(self):
        for path in (
            "vigil/docs/reviews/2026-10-23-taxonomy-080-reconciliation/PROGRESS.md",
            "vigil/docs/reviews/some-future-campaign/INC-999999.json",
            "vigil/docs/reviews/some-future-campaign/validator.log",
        ):
            with self.subTest(path=path):
                self.assertFalse(self.builder.in_scope(path))

    def test_canonical_evidence_methods_and_controls_still_scientific(self):
        for path in (
            "vigil/records/incidents/VIGIL-INC-000003.json",
            "vigil/taxonomy/VIGIL.FailureTaxonomy.Index.json",
            "vigil/methodologies/VIGIL.HarmImpactMatrix.v1.1.0.json",
            "vigil/external_governance/requirements/README.md",
            "vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md",
            "vigil/docs/maintenance/ADJUDICATION-ROOT-CAUSE-CORRECTIONS.md",
            "vigil/scripts/validate-vigil-records.py",
            "vigil/VIGIL.Schema.json",
        ):
            with self.subTest(path=path):
                self.assertTrue(self.builder.in_scope(path))

    def test_review_folder_not_in_prefixes(self):
        self.assertNotIn("vigil/docs/reviews/", self.builder.PREFIXES)
        self.assertNotIn("vigil/docs/reviews/", self.builder.EXACT)


if __name__ == "__main__":
    unittest.main()
