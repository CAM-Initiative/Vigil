import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "vigil" / "scripts" / "validate-vigil-records.py"
spec = importlib.util.spec_from_file_location("validate_vigil_records", VALIDATOR)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class ValidateVigilRecordsTest(unittest.TestCase):
    def test_valid_fixtures_pass(self):
        self.assertEqual(validator.validate(ROOT / "vigil" / "tests" / "fixtures" / "valid"), 0)

    def test_invalid_fixtures_fail(self):
        invalid_dir = ROOT / "vigil" / "tests" / "fixtures" / "invalid"
        for fixture in sorted(invalid_dir.glob("*.json")):
            with self.subTest(fixture=fixture.name):
                self.assertNotEqual(validator.validate(fixture), 0)

    def test_source_data_is_forbidden(self):
        fixture = ROOT / "vigil" / "tests" / "fixtures" / "invalid" / "invalid-obs-source-data.json"
        self.assertNotEqual(validator.validate(fixture), 0)

    def validate_mutated_fixture(self, fixture_name, mutate):
        fixture = ROOT / "vigil" / "tests" / "fixtures" / "valid" / fixture_name
        with fixture.open(encoding="utf-8") as handle:
            record = json.load(handle)
        mutate(record)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / f"{record['id']}.json"
            path.write_text(json.dumps(record), encoding="utf-8")
            return validator.validate(path)

    def test_canonical_path_validation_by_record_type_and_year(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_records = Path(temp_dir) / "records"
            fixture = ROOT / "vigil" / "tests" / "fixtures" / "valid" / "VIGIL-2026-OBS-0001.json"
            wrong_path = temp_records / "proposals" / "2026" / "VIGIL-2026-OBS-0001.json"
            wrong_path.parent.mkdir(parents=True)
            shutil.copy2(fixture, wrong_path)

            originals = (validator.RECORDS_ROOT, validator.RECORD_TYPE_DIRS)
            try:
                validator.RECORDS_ROOT = temp_records
                validator.RECORD_TYPE_DIRS = [
                    temp_records / "observations",
                    temp_records / "failures",
                    temp_records / "proposals",
                    temp_records / "patches",
                    temp_records / "research",
                ]
                self.assertNotEqual(validator.validate(), 0)
            finally:
                validator.RECORDS_ROOT, validator.RECORD_TYPE_DIRS = originals

    def test_clean_observation_records_pass(self):
        for record_id in ("VIGIL-2026-OBS-0002", "VIGIL-2026-OBS-0003"):
            with self.subTest(record=record_id):
                path = ROOT / "vigil" / "records" / "observations" / "2026" / f"{record_id}.json"
                self.assertEqual(validator.validate(path), 0)

    def test_clean_proposal_records_pass(self):
        proposal_dir = ROOT / "vigil" / "records" / "proposals" / "2026"
        for path in sorted(proposal_dir.glob("VIGIL-2026-PROP-*.json")):
            with self.subTest(record=path.name):
                self.assertEqual(validator.validate(path), 0)

    def test_fm_requires_canonical_failure_group(self):
        def mutate(record):
            record["failure_classification"].pop("canonical_failure_group", None)

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-FM-0001.json", mutate), 0)

    def test_fm_rejects_unknown_canonical_failure_group(self):
        def mutate(record):
            record["failure_classification"]["canonical_failure_group"] = "legacy-runtime"

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-FM-0001.json", mutate), 0)

    def test_fm_requires_failure_family(self):
        def mutate(record):
            record["failure_classification"].pop("failure_family", None)

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-FM-0001.json", mutate), 0)

    def test_legacy_source_record_keys_are_rejected(self):
        def mutate(record):
            record["source_records"][0]["title"] = record["source_records"][0].pop("source_title")
            record["source_records"][0]["url"] = record["source_records"][0].pop("source_url")
            record["source_records"][0]["platform"] = record["source_records"][0].pop("source_platform")

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-OBS-0001.json", mutate), 0)

    def test_record_identity_status_is_rejected(self):
        def mutate(record):
            record["record_identity"]["status"] = "open"

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-OBS-0001.json", mutate), 0)

    def test_prop_rejects_patch_status_and_empty_scope(self):
        def mutate(record):
            record["patch_status"] = "implemented"
            record["proposal_scope"] = {}

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-PROP-0001.json", mutate), 0)

    def test_obs_rejects_patch_status(self):
        def mutate(record):
            record["cam_internal"]["patch_status"] = "open"

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-OBS-0001.json", mutate), 0)

    def test_patch_rejects_empty_changed_implementation_fields(self):
        def mutate(record):
            record["change_details"] = {}
            record["implementation_verification"] = {}

        self.assertNotEqual(self.validate_mutated_fixture("VIGIL-2026-PATCH-0001.json", mutate), 0)


if __name__ == "__main__":
    unittest.main()
