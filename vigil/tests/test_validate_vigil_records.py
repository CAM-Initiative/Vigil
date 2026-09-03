import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VIGIL = ROOT / "vigil"
SCRIPT = VIGIL / "scripts" / "validate-vigil-records.py"
SPEC = importlib.util.spec_from_file_location("validate_vigil_records", SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(VALIDATOR)


class ValidateIncidentCorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads(
            (VIGIL / "records" / "incidents" / "VIGIL-INC-000001.json").read_text(encoding="utf-8")
        )

    def validate_mutation(self, mutate):
        record = copy.deepcopy(self.fixture)
        mutate(record)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / f"{record['id']}.json"
            path.write_text(json.dumps(record), encoding="utf-8")
            return VALIDATOR.validate(path)

    def test_canonical_corpus_validates(self):
        self.assertEqual(VALIDATOR.validate(), 0)


    def test_schema_declares_only_incident_record_class(self):
        schema = json.loads((VIGIL / "VIGIL.Schema.json").read_text(encoding="utf-8"))
        self.assertEqual(set(schema["record_classes"]), {"incident"})
        self.assertEqual(schema["$defs"]["record_type"]["enum"], ["incident"])

    def test_retired_record_directories_and_indexes_are_absent(self):
        for directory in VALIDATOR.RETIRED_RECORD_DIRS:
            self.assertFalse((VIGIL / "records" / directory).exists(), directory)
        for filename in VALIDATOR.RETIRED_INDEXES:
            self.assertFalse((VIGIL / filename).exists(), filename)

    def test_source_data_and_incident_confidence_are_rejected(self):
        self.assertNotEqual(self.validate_mutation(lambda record: record.update(source_data={})), 0)
        self.assertNotEqual(self.validate_mutation(lambda record: record.update(evidence_confidence="high")), 0)

    def test_source_order_must_be_contiguous(self):
        self.assertNotEqual(
            self.validate_mutation(lambda record: record["source_records"][0].update(incident_source_order=2)),
            0,
        )

    def test_unclassified_incident_cannot_assert_mapping(self):
        def mutate(record):
            record["taxonomy_classification"]["primary_classification"] = {
                "family_id": "VIGIL-FF-0001", "class_id": "VIGIL-FC-000001",
                "classification_basis": "Invalid asserted mapping.", "classification_confidence": "high",
            }
        self.assertNotEqual(self.validate_mutation(mutate), 0)

    def test_allowed_system_values_are_schema_driven(self):
        schema = json.loads((VIGIL / "VIGIL.Schema.json").read_text(encoding="utf-8"))
        schema["system_context_rules"]["allowed_platform_or_vendor_values"].append("Schema Vendor")
        schema["system_context_rules"]["allowed_product_or_service_values"].append("Schema Product")
        with tempfile.TemporaryDirectory() as directory:
            schema_path = Path(directory) / "schema.json"
            schema_path.write_text(json.dumps(schema), encoding="utf-8")
            record = copy.deepcopy(self.fixture)
            record["system_context"]["platform_or_vendor"] = "Schema Vendor"
            record["system_context"]["product_or_service"] = "Schema Product"
            errors, _ = VALIDATOR.validate_record(Path(record["id"] + ".json"), record, schema_path=schema_path)
            self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
