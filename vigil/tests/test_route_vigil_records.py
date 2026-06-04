import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROUTER = ROOT / "vigil" / "scripts" / "route-vigil-records.py"
spec = importlib.util.spec_from_file_location("route_vigil_records", ROUTER)
router = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(router)


class RouteVigilRecordsTest(unittest.TestCase):
    def test_json_decode_error_reports_path_message_line_and_column(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bad-record.json"
            path.write_text('{"id": "VIGIL-2026-PROP-0008"}\n{"extra": true}\n', encoding="utf-8")

            with self.assertRaises(SystemExit) as context:
                router.load_record(path)

        self.assertEqual(
            str(context.exception),
            f"Invalid JSON in {path}: Extra data at line 2 column 1.",
        )

    def test_json_decode_error_reports_repo_relative_path(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temp_dir:
            path = Path(temp_dir) / "bad-record.json"
            path.write_text('{"id": "VIGIL-2026-PROP-0008"}\n{"extra": true}\n', encoding="utf-8")

            with self.assertRaises(SystemExit) as context:
                router.load_record(path)

            relative_path = path.relative_to(ROOT)
            self.assertEqual(
                str(context.exception),
                f"Invalid JSON in {relative_path}: Extra data at line 2 column 1.",
            )


if __name__ == "__main__":
    unittest.main()
