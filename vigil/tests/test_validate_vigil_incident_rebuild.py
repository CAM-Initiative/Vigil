import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate-vigil-incident-rebuild.py"


def write_json(path: Path, value):
    path.write_text(json.dumps(value, indent=2), encoding="utf-8")


def record(role="failure-occurrence", confidence="high", include_mapping=True):
    primary = {
        "family_id": "VIGIL-FF-0001",
        "class_id": "VIGIL-FC-000001",
        "classification_role": role,
        "classification_basis": "Occurrence-specific basis.",
        "classification_confidence": confidence,
    } if include_mapping else None
    return {
        "id": "VIGIL-INC-009999",
        "record_type": "incident",
        "summary": "A sufficiently detailed baseline occurrence narrative preserves the important actors, actions, chronology, outcome, and uncertainty for this fixture.",
        "vigil_assessment": {
            "factual_basis": "The preserved fixture evidence establishes the bounded occurrence and the material facts required for this generic rebuild test."
        },
        "source_records": [
            {
                "source_title": "Primary report",
                "source_url": "https://example.invalid/primary",
            }
        ],
        "taxonomy_classification": {
            "taxonomy_version": "0.test",
            "classification_status": "classified" if include_mapping else "unclassified",
            "classification_basis": "Fixture basis.",
            "primary_classification": primary,
            "secondary_classifications": [],
            "classification_review_provenance": {"method": "fixture"},
        },
    }


def manifest(disposition="retained"):
    return {
        "incident_id": "VIGIL-INC-009999",
        "review_mode": "full-rebuild",
        "baseline": {"ref": "fixture"},
        "evidence_search": {
            "status": "performed",
            "queries": ["fixture evidence search"],
            "sources_added": [],
            "notes": "fixture",
        },
        "taxonomy_review": {
            "taxonomy_version": "0.test",
            "current_taxonomy_loaded": True,
            "complete_class_set_review": True,
            "candidate_classes_tested": [
                {
                    "class_id": "VIGIL-FC-000001",
                    "outcome": "retained-candidate",
                    "recognition_and_exclusion_note": "fixture",
                }
            ],
        },
        "taxonomy_mapping_dispositions": [
            {
                "class_id": "VIGIL-FC-000001",
                "disposition": disposition,
                "reason": "fixture reason",
            }
        ],
        "new_taxonomy_mappings": [],
        "source_dispositions": [],
        "prose_changes": {
            "summary_reduction_reason": None,
            "factual_basis_reduction_reason": None,
        },
        "harm_review": {"status": "reviewed", "notes": "fixture"},
        "governance_interpretation_review": {"status": "reviewed", "notes": "fixture"},
    }


class IncidentRebuildValidatorTests(unittest.TestCase):
    def run_validator(self, baseline, candidate, review_manifest):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            baseline_path = tmp / "baseline.json"
            candidate_path = tmp / "candidate.json"
            manifest_path = tmp / "manifest.json"
            write_json(baseline_path, baseline)
            write_json(candidate_path, candidate)
            write_json(manifest_path, review_manifest)
            return subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--baseline-file",
                    str(baseline_path),
                    "--candidate-file",
                    str(candidate_path),
                    "--manifest",
                    str(manifest_path),
                ],
                capture_output=True,
                text=True,
            )

    def test_unchanged_mapping_requires_retained_disposition(self):
        result = self.run_validator(record(), record(), manifest("retained"))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_silent_mapping_deletion_fails(self):
        candidate = record(include_mapping=False)
        review = manifest("retained")
        result = self.run_validator(record(), candidate, review)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must be superseded or removed-unsupported", result.stderr)

    def test_explicit_unsupported_removal_passes(self):
        candidate = record(include_mapping=False)
        review = manifest("removed-unsupported")
        result = self.run_validator(record(), candidate, review)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_role_change_must_be_declared(self):
        candidate = record(role="successful-invariant")
        result = self.run_validator(record(), candidate, manifest("retained"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("role-changed", result.stderr)

    def test_material_prose_compaction_requires_reason(self):
        baseline = record()
        baseline["summary"] = " ".join(["detail"] * 100)
        candidate = record()
        candidate["summary"] = " ".join(["detail"] * 20)
        result = self.run_validator(baseline, candidate, manifest("retained"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("summary_reduction_reason", result.stderr)


if __name__ == "__main__":
    unittest.main()
