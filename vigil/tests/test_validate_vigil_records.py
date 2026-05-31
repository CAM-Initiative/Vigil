import importlib.util
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


if __name__ == "__main__":
    unittest.main()
