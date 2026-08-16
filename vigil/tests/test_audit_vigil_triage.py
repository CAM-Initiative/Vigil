import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit-vigil-triage.py"
if not SCRIPT.exists():
    SCRIPT = Path(__file__).with_name("audit-vigil-triage.py")
SPEC = importlib.util.spec_from_file_location("audit_vigil_triage", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class TriageInventoryTests(unittest.TestCase):
    def write_record(self, root, record_class, name, value):
        path = root / "vigil" / "records" / record_class / "2026" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def test_inventory_separates_current_work_from_severity_and_monitoring(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_record(
                root,
                "patches",
                "VIGIL-2026-PATCH-0001.json",
                {"id": "VIGIL-2026-PATCH-0001"},
            )
            self.write_record(
                root,
                "learn",
                "VIGIL-2026-LEARN-0001.json",
                {
                    "id": "VIGIL-2026-LEARN-0001",
                    "learning_basis": {
                        "primary_failure_mode": "VIGIL-2026-FM-0001"
                    },
                    "linked_records": {
                        "related_failure_modes": ["VIGIL-2026-FM-0001"]
                    },
                    "chain_completion": {"overall_status": "complete"},
                },
            )
            self.write_record(
                root,
                "failures",
                "VIGIL-2026-FM-0001.json",
                {
                    "id": "VIGIL-2026-FM-0001",
                    "record_type": "failure_mode",
                    "record_state": "monitoring",
                    "failure_classification": {"severity": "S1"},
                    "triage": {
                        "triage_priority": "PN",
                        "triage_status": "monitoring",
                        "recommended_next_step": "Observe recurrence.",
                    },
                    "repair_status": {
                        "status": "repaired",
                        "repaired_by": ["VIGIL-2026-PATCH-0001"],
                    },
                    "ecosystem_status": {"status": "active", "monitoring_required": True},
                    "linked_records": {
                        "related_patch_notes": ["VIGIL-2026-PATCH-0001"]
                    },
                },
            )

            inventory = AUDIT.build_inventory(root)
            row = inventory["records"][0]
            self.assertEqual(row["severity"], "S1")
            self.assertEqual(row["triage_priority"], "PN")
            self.assertEqual(row["triage_status"], "monitoring")
            self.assertTrue(row["monitoring_required"])
            self.assertTrue(row["linked_patch_records_exist"])
            self.assertTrue(row["evidence_chain_appears_complete"])
            self.assertEqual(row["review_flags"], [])

    def test_legacy_values_are_flagged_without_being_rewritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_record(
                root,
                "failures",
                "VIGIL-2026-FM-0002.json",
                {
                    "id": "VIGIL-2026-FM-0002",
                    "record_type": "failure_mode",
                    "record_state": "monitoring",
                    "failure_classification": {"severity": "medium-high"},
                    "triage": {
                        "triage_priority": "high",
                        "triage_status": "watching-after-patch",
                        "recommended_next_step": "Monitor.",
                    },
                    "repair_status": {"status": "repaired", "repaired_by": []},
                    "ecosystem_status": {"status": "active", "monitoring_required": True},
                    "linked_records": {"related_patch_notes": []},
                },
            )

            row = AUDIT.build_inventory(root)["records"][0]
            self.assertEqual(row["triage_priority"], "high")
            self.assertEqual(row["severity"], "medium-high")
            self.assertIn("invalid-priority", row["review_flags"])
            self.assertIn("invalid-status", row["review_flags"])
            self.assertIn("priority-may-contain-severity", row["review_flags"])
            self.assertIn("legacy-severity-mapping-required", row["review_flags"])


    def test_current_corpus_is_fully_reconciled_to_model_2(self):
        inventory = AUDIT.build_inventory(AUDIT.ROOT)
        self.assertEqual(inventory["scope"]["record_count"], 61)
        self.assertTrue(inventory["migration_safety"]["records_reconciled"])
        self.assertEqual(inventory["migration_safety"]["phase"], "pass-3-record-reconciliation")
        self.assertTrue(all(not row["review_flags"] for row in inventory["records"]))
        self.assertTrue(
            all(
                row["triage_priority"] in AUDIT.ALLOWED_PRIORITIES
                and row["triage_status"] in AUDIT.ALLOWED_STATUSES
                and row["severity"] in AUDIT.PREFERRED_SEVERITIES
                for row in inventory["records"]
            )
        )


if __name__ == "__main__":
    unittest.main()
