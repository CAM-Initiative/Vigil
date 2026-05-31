import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILDER = ROOT / "vigil" / "scripts" / "build-vigil-records.py"
spec = importlib.util.spec_from_file_location("build_vigil_records", BUILDER)
builder = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(builder)


class BuildVigilRecordsTest(unittest.TestCase):
    def load_record(self, record_id):
        record_path = ROOT / "vigil" / "records" / "open" / f"{record_id}.json"
        with record_path.open(encoding="utf-8") as handle:
            return json.load(handle)

    def test_fm_0002_generated_summaries_distinguish_source_and_system(self):
        record = self.load_record("VIGIL-2026-FM-0002")
        aggregate = builder.prune_empty(builder.aggregate_record(record))

        self.assertEqual(aggregate["source_summary"]["primary_source_platform"], "TikTok")
        self.assertEqual(
            aggregate["source_summary"]["primary_source_author_or_publisher"], "@Huskistaken"
        )
        self.assertEqual(aggregate["system_summary"]["platform_or_vendor"], "OpenAI")
        self.assertEqual(
            aggregate["system_summary"]["model_or_product"], "ChatGPT Advanced Voice Mode"
        )
        self.assertEqual(aggregate["system_summary"]["interaction_mode"], "voice | multi-device")

    def test_empty_linked_record_arrays_are_pruned_from_generated_index(self):
        record = self.load_record("VIGIL-2026-OBS-0001")
        record["linked_records"] = {
            "related_observations": [],
            "related_failure_modes": [],
            "related_proposals": [],
            "related_patch_notes": [],
            "external_references": [],
            "research": [],
            "standards": [],
        }
        index_entry = builder.prune_empty(builder.index_record(record))

        self.assertNotIn("linked_records", index_entry)

    def test_uncertainty_values_survive_generated_pruning(self):
        pruned = builder.prune_empty(
            {
                "empty_values": [None, "", [], {}],
                "uncertainty_values": [
                    "unknown",
                    "to be assessed",
                    "to be confirmed",
                    "not applicable",
                    "possible",
                    "no",
                ],
            }
        )

        self.assertNotIn("empty_values", pruned)
        self.assertEqual(
            pruned["uncertainty_values"],
            ["unknown", "to be assessed", "to be confirmed", "not applicable", "possible", "no"],
        )

    def test_individual_records_keep_source_records_only(self):
        for path in sorted((ROOT / "vigil" / "records").glob("*/*.json")):
            with self.subTest(record=path.name):
                with path.open(encoding="utf-8") as handle:
                    record = json.load(handle)
                self.assertIn("source_records", record)
                self.assertNotIn("source_data", record)


if __name__ == "__main__":
    unittest.main()
