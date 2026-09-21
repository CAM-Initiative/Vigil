import copy
import importlib.util
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
INCIDENTS = VIGIL / "records" / "incidents"
AUDIT = VIGIL / "docs" / "reviews" / "2026-09-21-agent-environment-metadata-migration-audit.json"
SCRIPT = VIGIL / "scripts" / "validate-vigil-records.py"
SPEC = importlib.util.spec_from_file_location("validate_agent_environment_metadata", SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(VALIDATOR)


class AgentEnvironmentMetadataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = [
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted(INCIDENTS.glob("VIGIL-INC-*.json"))
        ]
        cls.fixture = next(record for record in cls.records if record["id"] == "VIGIL-INC-000001")

    def errors(self, mutate):
        record = copy.deepcopy(self.fixture)
        mutate(record)
        errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record)
        return errors

    def test_every_incident_has_normalized_metadata(self):
        self.assertTrue(self.records)
        for record in self.records:
            with self.subTest(record=record["id"]):
                context = record["system_context"]
                self.assertIn("agent_context", context)
                self.assertIn("occurrence_environment", context)
                self.assertNotIn("coordination_topology", context["agent_context"])

    def test_audit_counts_reconcile_to_corpus(self):
        audit = json.loads(AUDIT.read_text(encoding="utf-8"))
        agent = Counter(record["system_context"]["agent_context"]["agentic_status"] for record in self.records)
        basis = Counter(record["system_context"]["agent_context"]["count_basis"] for record in self.records)
        setting = Counter(
            record["system_context"]["occurrence_environment"]["operational_setting"]
            for record in self.records
        )
        actor = Counter(
            record["system_context"]["occurrence_environment"]["testing_actor"]
            for record in self.records
        )
        self.assertEqual(audit["total_incidents_migrated"], len(self.records))
        self.assertEqual(audit["agentic_status_counts"], dict(sorted(agent.items())))
        self.assertEqual(audit["agent_count_basis_counts"], dict(sorted(basis.items())))
        self.assertEqual(audit["occurrence_environment_counts"], dict(sorted(setting.items())))
        self.assertEqual(audit["testing_actor_counts"], dict(sorted(actor.items())))
        self.assertEqual(
            sum(audit["agentic_status_counts"].values()),
            audit["total_incidents_migrated"],
        )
        self.assertEqual(
            sum(audit["occurrence_environment_counts"].values()),
            audit["total_incidents_migrated"],
        )

    def test_single_agent_requires_exact_one(self):
        errors = self.errors(
            lambda record: record["system_context"]["agent_context"].update(agent_count=2)
        )
        self.assertTrue(any("single-agent requires exact count" in error for error in errors), errors)

    def test_non_agentic_rejects_positive_count(self):
        def mutate(record):
            record["system_context"]["agent_context"].update(
                agentic_status="non-agentic",
                count_basis="not-applicable",
                agent_count=1,
                agent_count_min=None,
                agent_count_max=None,
            )
        errors = self.errors(mutate)
        self.assertTrue(any("non-agentic requires" in error for error in errors), errors)

    def test_invalid_agent_range_is_rejected(self):
        def mutate(record):
            record["system_context"]["agent_context"].update(
                agentic_status="multi-agent",
                count_basis="range",
                agent_count=None,
                agent_count_min=5,
                agent_count_max=4,
            )
        errors = self.errors(mutate)
        self.assertTrue(any("ordered minimum/maximum" in error for error in errors), errors)

    def test_unknown_agent_status_rejects_fabricated_count(self):
        def mutate(record):
            record["system_context"]["agent_context"].update(
                agentic_status="unknown",
                count_basis="unknown",
                agent_count=1,
                agent_count_min=None,
                agent_count_max=None,
            )
        errors = self.errors(mutate)
        self.assertTrue(any("unknown agentic status" in error for error in errors), errors)

    def test_live_environment_rejects_testing_actor(self):
        errors = self.errors(
            lambda record: record["system_context"]["occurrence_environment"].update(
                testing_actor="provider-internal"
            )
        )
        self.assertTrue(any("live occurrence requires" in error for error in errors), errors)

    def test_testing_environment_rejects_not_applicable_actor(self):
        errors = self.errors(
            lambda record: record["system_context"]["occurrence_environment"].update(
                operational_setting="testing",
                testing_actor="not-applicable",
            )
        )
        self.assertTrue(any("testing occurrence must" in error for error in errors), errors)

    def test_metadata_source_references_must_resolve(self):
        errors = self.errors(
            lambda record: record["system_context"]["agent_context"].update(
                source_record_refs=["source_records[999]"]
            )
        )
        self.assertTrue(any("points outside source_records" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
