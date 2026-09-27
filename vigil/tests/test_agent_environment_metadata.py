import copy
import importlib.util
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
INCIDENTS = VIGIL / "records" / "incidents"
AUDIT = VIGIL / "docs" / "reviews" / "2026-09-27-environment-metadata-semantic-transmutation-audit.json"
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
        deployment = Counter(
            record["system_context"]["occurrence_environment"]["deployment_state"]
            for record in self.records
        )
        contexts = Counter(
            context
            for record in self.records
            for context in record["system_context"]["occurrence_environment"]["activity_contexts"]
        )
        reach = Counter(
            record["system_context"]["occurrence_environment"]["external_reach"]
            for record in self.records
        )
        actor = Counter(
            record["system_context"]["occurrence_environment"]["activity_actor"]
            for record in self.records
        )
        self.assertEqual(audit["active_incidents_reviewed"], len(self.records))
        self.assertEqual(audit["deployment_state_counts"], dict(sorted(deployment.items())))
        self.assertEqual(audit["activity_context_counts"], dict(sorted(contexts.items())))
        self.assertEqual(audit["external_reach_counts"], dict(sorted(reach.items())))
        self.assertEqual(audit["activity_actor_counts"], dict(sorted(actor.items())))
        self.assertEqual(
            sum(audit["deployment_state_counts"].values()),
            audit["active_incidents_reviewed"],
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

    def test_operational_use_requires_deployment(self):
        errors = self.errors(
            lambda record: record["system_context"]["occurrence_environment"].update(
                deployment_state="unknown"
            )
        )
        self.assertTrue(any("operational-use requires deployed" in error for error in errors), errors)

    def test_unknown_context_rejects_non_unknown_actor(self):
        errors = self.errors(
            lambda record: record["system_context"]["occurrence_environment"].update(
                deployment_state="unknown",
                activity_contexts=["unknown"],
                activity_actor="not-applicable",
            )
        )
        self.assertTrue(any("unknown activity context requires" in error for error in errors), errors)

    def test_predeployment_evaluation_may_reach_live_external_systems(self):
        def mutate(record):
            record["system_context"]["occurrence_environment"].update(
                deployment_state="pre-deployment",
                activity_contexts=["evaluation"],
                external_reach="live-external",
                activity_actor="provider-internal",
            )
        self.assertFalse(self.errors(mutate))

    def test_metadata_source_references_must_resolve(self):
        errors = self.errors(
            lambda record: record["system_context"]["agent_context"].update(
                source_record_refs=["source_records[999]"]
            )
        )
        self.assertTrue(any("points outside source_records" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
