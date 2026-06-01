import importlib.util
import json
import shutil
import tempfile
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
        matches = sorted((ROOT / "vigil" / "records").rglob(f"{record_id}.json"))
        self.assertEqual(len(matches), 1, record_id)
        with matches[0].open(encoding="utf-8") as handle:
            return json.load(handle)

    def load_valid_fixture(self, record_id):
        record_path = ROOT / "vigil" / "tests" / "fixtures" / "valid" / f"{record_id}.json"
        with record_path.open(encoding="utf-8") as handle:
            return json.load(handle)

    def test_recursive_discovery_under_type_year_folders(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir) / "records"
            nested = base / "observations" / "2026"
            nested.mkdir(parents=True)
            target = nested / "VIGIL-2026-OBS-9999.json"
            target.write_text("{}", encoding="utf-8")
            original_dirs = builder.RECORD_TYPE_DIRS
            try:
                builder.RECORD_TYPE_DIRS = [base / "observations"]
                self.assertEqual(builder.record_files(), [target])
            finally:
                builder.RECORD_TYPE_DIRS = original_dirs

    def test_observation_generated_summary_excludes_cam_summary(self):
        record = self.load_record("VIGIL-2026-OBS-0001")
        summaries = builder.generated_summaries(record)

        self.assertIn("source_summary", summaries)
        self.assertIn("system_summary", summaries)
        self.assertIn("jurisdiction_summary", summaries)
        self.assertNotIn("cam_summary", summaries)
        self.assertNotIn("cam_internal", summaries)
        self.assertNotIn("affected_instruments", json.dumps(summaries))
        self.assertNotIn("related_or_similar_instruments", json.dumps(summaries))

    def test_failure_mode_generated_summary_excludes_cam_summary(self):
        record = self.load_record("VIGIL-2026-FM-0002")
        summaries = builder.generated_summaries(record)

        self.assertIn("source_summary", summaries)
        self.assertIn("system_summary", summaries)
        self.assertIn("jurisdiction_summary", summaries)
        self.assertIn("classification_summary", summaries)
        self.assertIn("triage_summary", summaries)
        self.assertNotIn("cam_summary", summaries)
        self.assertNotIn("cam_internal", summaries)
        self.assertNotIn("affected_instruments", json.dumps(summaries))
        self.assertEqual(summaries["classification_summary"]["canonical_failure_group"], "arbitration")

    def test_proposal_generated_summary_may_include_cam_summary(self):
        record = self.load_valid_fixture("VIGIL-2026-PROP-0001")
        summaries = builder.generated_summaries(record)

        self.assertIn("source_summary", summaries)
        self.assertIn("system_summary", summaries)
        self.assertIn("proposal_summary", summaries)
        self.assertIn("external_relevance_summary", summaries)
        self.assertIn("cam_summary", summaries)
        self.assertIn("target_instruments", summaries["cam_summary"])
        self.assertNotIn("proposal_owner", summaries["cam_summary"])

    def test_patch_generated_summary_may_include_cam_summary(self):
        record = self.load_valid_fixture("VIGIL-2026-PATCH-0001")
        summaries = builder.generated_summaries(record)

        self.assertIn("source_summary", summaries)
        self.assertIn("system_summary", summaries)
        self.assertIn("change_summary", summaries)
        self.assertIn("verification_summary", summaries)
        self.assertIn("impact_summary", summaries)
        self.assertIn("cam_summary", summaries)
        self.assertEqual(summaries["cam_summary"], {"governance_layer": "unknown"})
        self.assertNotIn("changed_instruments", summaries["cam_summary"])

    def test_fm_0002_generated_summaries_distinguish_source_and_system(self):
        record = self.load_record("VIGIL-2026-FM-0002")
        aggregate = builder.prune_empty(builder.aggregate_record(record))

        self.assertEqual(aggregate["source_summary"]["primary_source_platform"], "TikTok")
        self.assertEqual(
            aggregate["source_summary"]["primary_source_author_or_publisher"], "@Huskistaken"
        )
        self.assertEqual(aggregate["system_summary"]["platform_or_vendor"], "OpenAI")
        self.assertEqual(
            aggregate["system_summary"]["product_or_service"], "ChatGPT Advanced Voice Mode"
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

    def test_empty_cam_arrays_are_pruned_from_generated_summaries(self):
        record = self.load_valid_fixture("VIGIL-2026-PATCH-0001")
        summaries = builder.generated_summaries(record)

        self.assertIn("cam_summary", summaries)
        self.assertNotIn("changed_instruments", summaries["cam_summary"])
        self.assertNotIn("changed_annexes", summaries["cam_summary"])
        self.assertNotIn("changed_domains", summaries["cam_summary"])

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
                    "none identified",
                ],
            }
        )

        self.assertNotIn("empty_values", pruned)
        self.assertEqual(
            pruned["uncertainty_values"],
            [
                "unknown",
                "to be assessed",
                "to be confirmed",
                "not applicable",
                "possible",
                "no",
                "none identified",
            ],
        )

    def test_individual_records_keep_source_records_only(self):
        for path in sorted((ROOT / "vigil" / "records").rglob("*.json")):
            with self.subTest(record=path.name):
                with path.open(encoding="utf-8") as handle:
                    record = json.load(handle)
                self.assertIn("source_records", record)
                self.assertNotIn("source_data", record)

    def test_generated_index_includes_all_individual_records_and_no_legacy_aggregate(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            temp_records = temp / "records"
            for source in sorted((ROOT / "vigil" / "records").rglob("*.json")):
                relative = source.relative_to(ROOT / "vigil" / "records")
                target = temp_records / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)

            originals = (
                builder.RECORD_TYPE_DIRS,
                builder.ACTIVE_OUTPUT_PATH,
                builder.CLOSED_OUTPUT_PATH,
                builder.INDEX_OUTPUT_PATH,
            )
            try:
                builder.RECORD_TYPE_DIRS = [
                    temp_records / "observations",
                    temp_records / "failures",
                    temp_records / "proposals",
                    temp_records / "patches",
                    temp_records / "research",
                ]
                builder.ACTIVE_OUTPUT_PATH = temp / "VIGIL.ActiveRecords.json"
                builder.CLOSED_OUTPUT_PATH = temp / "VIGIL.ClosedRecords.json"
                builder.INDEX_OUTPUT_PATH = temp / "VIGIL.Records.Index.json"
                builder.build()
                index = json.loads(builder.INDEX_OUTPUT_PATH.read_text(encoding="utf-8"))
                self.assertEqual(index["record_count"], len(list(temp_records.rglob("*.json"))))
                self.assertFalse((temp / "VIGIL.Records.json").exists())
            finally:
                (
                    builder.RECORD_TYPE_DIRS,
                    builder.ACTIVE_OUTPUT_PATH,
                    builder.CLOSED_OUTPUT_PATH,
                    builder.INDEX_OUTPUT_PATH,
                ) = originals


if __name__ == "__main__":
    unittest.main()
