"""Case-neutral checks of taxonomy branch governance, not Incident verdicts."""
import importlib.util
import json
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check-taxonomy-branch-ownership.py"
spec = importlib.util.spec_from_file_location("taxonomy_branch_guard", SCRIPT)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class TaxonomyBranchOwnershipTests(unittest.TestCase):
    def test_canonical_sources_are_protected(self):
        for path in (
            "vigil/taxonomy/families/FF.json",
            "vigil/taxonomy/VIGIL.FailureTaxonomy.Index.json",
            "vigil/taxonomy/VIGIL.FailureTaxonomy.Schema.json",
            "vigil/taxonomy/validate_taxonomy.py",
        ):
            with self.subTest(path=path):
                self.assertTrue(guard.controlled(path))

    def test_projections_not_normative(self):
        for path in (
            "vigil/taxonomy/generated/examples.json",
            "vigil/taxonomy/assets/logo.png",
            "vigil/records/incidents/VIGIL-INC-000001.json",
        ):
            with self.subTest(path=path):
                self.assertFalse(guard.controlled(path))

    def test_exemplar_only_change_is_not_authority_change(self):
        path = "vigil/taxonomy/families/FF.json"
        before = {"family": {"family_id": "F"}, "classes": [
            {"class_id": "C", "invariant": "I", "invariant_exemplars": [{"evidence_basis": "A"}]}]}
        after = {"family": {"family_id": "F"}, "classes": [
            {"class_id": "C", "invariant": "I", "invariant_exemplars": [{"evidence_basis": "B"}]}]}
        blob = lambda x: json.dumps(x).encode("utf-8")
        self.assertFalse(guard.normative_change(path, blob(before), blob(after)))
        after["classes"][0]["invariant"] = "Different invariant"
        self.assertTrue(guard.normative_change(path, blob(before), blob(after)))

    def test_added_or_deleted_family_is_protected(self):
        path = "vigil/taxonomy/families/new.json"
        data = b'{"classes":[]}'
        self.assertTrue(guard.normative_change(path, None, data))
        self.assertTrue(guard.normative_change(path, data, None))

    def test_working_release_index_change_is_protected(self):
        self.assertTrue(guard.normative_change(
            "vigil/taxonomy/VIGIL.FailureTaxonomy.Index.json",
            b'{"working_release":null}',
            b'{"working_release":{"version":"next"}}'))


if __name__ == "__main__":
    unittest.main()
