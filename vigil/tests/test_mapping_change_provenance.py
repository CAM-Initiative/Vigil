"""Generic regression coverage for vanished and role-changed VIGIL mappings."""
import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check-vigil-mapping-removals.py"
spec = importlib.util.spec_from_file_location("mapping_change_guard", SCRIPT)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


def record(*roles):
    items = [{"class_id": cid, "classification_role": role} for cid, role in roles]
    return {"taxonomy_classification": {
        "primary_classification": items[0] if items else None,
        "secondary_classifications": items[1:],
    }}


class MappingChangeProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.before = record(("FC-A", "ambiguous-boundary"), ("FC-B", "successful-invariant"))

    def test_removed_mapping_requires_current_packet_and_before_snapshot(self):
        after = record(("FC-A", "ambiguous-boundary"))
        self.assertEqual(guard.changed_mapping_roles(self.before, after), {"FC-B": "removed"})
        self.assertTrue(guard.verify_change(self.before, after, {}, False, "INC"))
        packet = {"taxonomy_mapping_dispositions": [{
            "class_id": "FC-B", "disposition": "removed-unsupported",
            "reason": "Scope exclusion established in the bounded occurrence",
            "before": {"class_id": "FC-B", "classification_role": "successful-invariant"},
            "after": None,
        }]}
        self.assertEqual(guard.verify_change(self.before, after, packet, True, "INC"), [])

    def test_role_change_requires_matching_after_and_current_packet(self):
        after = record(("FC-A", "failure-occurrence"), ("FC-B", "successful-invariant"))
        self.assertEqual(guard.changed_mapping_roles(self.before, after), {"FC-A": "role-changed"})
        packet = {"mapping_decisions": [{
            "class_id": "FC-A", "disposition": "role-changed",
            "classification_basis": "Source and criterion review establishes an observed failure",
            "baseline_mapping": {"class_id": "FC-A", "classification_role": "ambiguous-boundary"},
            "canonical_mapping_after": {"class_id": "FC-A", "classification_role": "failure-occurrence"},
        }]}
        self.assertEqual(guard.verify_change(self.before, after, packet, True, "INC"), [])
        packet["mapping_decisions"][0]["canonical_mapping_after"]["classification_role"] = "ambiguous-boundary"
        self.assertTrue(guard.verify_change(self.before, after, packet, True, "INC"))

    def test_no_mapping_change_is_not_blocked(self):
        after = record(("FC-A", "ambiguous-boundary"), ("FC-B", "successful-invariant"))
        self.assertEqual(guard.verify_change(self.before, after, {}, False, "INC"), [])

    def test_removed_mapping_cannot_be_relabelled_retained(self):
        after = record(("FC-A", "ambiguous-boundary"))
        packet = {"taxonomy_mapping_dispositions": [{
            "class_id": "FC-B", "disposition": "retained",
            "reason": "Unsupported",
            "before": {"class_id": "FC-B"}, "after": None,
        }]}
        self.assertTrue(guard.verify_change(self.before, after, packet, True, "INC"))


if __name__ == "__main__":
    unittest.main()
