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

    def test_historical_audit_counts_reconcile_to_frozen_decisions(self):
        """The dated September audit is immutable; later incident intake is not part of it."""
        audit = json.loads(AUDIT.read_text(encoding="utf-8"))
        decisions = audit["record_decisions"]
        self.assertEqual(audit["active_incidents_reviewed"], len(decisions))
        self.assertEqual(
            len(decisions), len({decision["incident_id"] for decision in decisions})
        )
        for field, count_key in (
            ("deployment_state", "deployment_state_counts"),
            ("external_reach", "external_reach_counts"),
            ("activity_actor", "activity_actor_counts"),
        ):
            counted = Counter(decision[field] for decision in decisions)
            self.assertEqual(audit[count_key], dict(sorted(counted.items())))
            self.assertEqual(sum(counted.values()), len(decisions))
        context_counts = Counter(
            context for decision in decisions for context in decision["activity_contexts"]
        )
        self.assertEqual(
            audit["activity_context_counts"], dict(sorted(context_counts.items()))
        )
        self.assertEqual(
            sum(audit["prior_operational_setting_counts"].values()), len(decisions)
        )
        self.assertEqual(
            sum(audit["deployment_state_counts"].values()),
            audit["active_incidents_reviewed"],
        )

    def test_current_corpus_environment_values_remain_valid(self):
        """Validate today's records against current semantics, not the historical counts."""
        audit = json.loads(AUDIT.read_text(encoding="utf-8"))
        allowed = audit["new_semantics"]
        self.assertTrue(self.records)
        self.assertEqual(
            len(self.records), len({record["id"] for record in self.records})
        )
        for record in self.records:
            with self.subTest(incident=record["id"]):
                env = record["system_context"]["occurrence_environment"]
                for field in ("deployment_state", "external_reach", "activity_actor"):
                    self.assertIn(env[field], allowed[field])
                self.assertTrue(env["activity_contexts"])
                for context in env["activity_contexts"]:
                    self.assertIn(context, allowed["activity_contexts"])

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
