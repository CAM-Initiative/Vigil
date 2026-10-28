#!/usr/bin/env python3
"""Isolated synthetic tests for the final-main Incident publication version guard."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check-incident-publication-versions.py"
spec = importlib.util.spec_from_file_location("vigil_incident_release_guard", SCRIPT)
guard = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(guard)

ID = "VIGIL-INC-000001"
FILE = "vigil/records/incidents/VIGIL-INC-000001.json"


def record(version="1.4.11", mapped=False, summary="Original"):
    rel = ([{"class_id": "VIGIL-FC-000089", "relationship": "failure-occurrence",
             "canonical_taxonomy_mapping": True}] if mapped else [])
    return {
        "id": ID,
        "record_identity": {"record_id": ID, "version": version, "updated": "2026-10-28"},
        "summary": summary,
        "taxonomy_classification": {
            "classification_status": "classified" if mapped else "unclassified",
            "primary_classification": (
                {"class_id": "VIGIL-FC-000089", "classification_role": "failure-occurrence"}
                if mapped else None
            ),
            "secondary_classifications": [],
        },
        "vigil_assessment": {"source_clause_analysis": {
            "clauses": [{"episode_id": "E001", "adjudication_status": "mapped" if mapped else "resolved-no-mapping",
                         "taxonomy_relationships": rel}]
        }},
    }


def row(level, version, blob, ident=ID):
    return {"incident_id": ident, "level": level,
            "reason": "Reviewed source-linked governance change to canonical case",
            "base_version": version, "base_blob": blob}


class ArithmeticContract(unittest.TestCase):
    def test_minor_for_new_taxonomy_mapping(self):
        old, new = record(), record(version="1.5.0", mapped=True)
        self.assertEqual(guard.next_version("1.4.11", "minor"), "1.5.0")
        self.assertEqual(guard.verify_record(ident=ID, published=old, candidate=new,
                                            declaration=row("minor", "1.4.11", "a"*40), blob="a"*40), "1.5.0")

    def test_mapping_as_patch_rejected(self):
        with self.assertRaisesRegex(guard.ReleaseError, "MINOR"):
            guard.verify_record(ident=ID, published=record(),
                                candidate=record("1.4.12", mapped=True),
                                declaration=row("patch", "1.4.11", "a"*40), blob="a"*40)

    def test_historical_major_two_continues(self):
        self.assertEqual(guard.next_version("2.0.7", "minor"), "2.1.0")
        self.assertEqual(guard.next_version("2.0.7", "major"), "3.0.0")

    def test_zero_major_minor(self):
        self.assertEqual(guard.next_version("0.1.16", "minor"), "0.2.0")

    def test_patch_typo(self):
        self.assertEqual(guard.verify_record(ident=ID, published=record(), candidate=record("1.4.12", summary="Typo fixed"),
                                            declaration=row("patch", "1.4.11", "b"*40), blob="b"*40), "1.4.12")

    def test_no_version_only_revision(self):
        with self.assertRaisesRegex(guard.ReleaseError, "version-only"):
            guard.verify_record(ident=ID, published=record(), candidate=record("1.4.12"),
                                declaration=row("patch", "1.4.11", "a"*40), blob="a"*40)

    def test_stale_version_declaration(self):
        with self.assertRaisesRegex(guard.ReleaseError, "does not match"):
            guard.verify_record(ident=ID, published=record(), candidate=record("1.4.12", summary="Changed"),
                                declaration=row("patch", "1.4.10", "a"*40), blob="a"*40)

    def test_nonmatching_candidate_bump(self):
        with self.assertRaisesRegex(guard.ReleaseError, "expected 1.5.0"):
            guard.verify_record(ident=ID, published=record(), candidate=record("1.4.12", summary="Changed"),
                                declaration=row("minor", "1.4.11", "a"*40), blob="a"*40)

    def test_new_staged_record_keeps_version(self):
        self.assertEqual(guard.verify_record(ident=ID, published=None, candidate=record("0.1.1"),
                                            declaration=row("initial", None, None), blob=None), "0.1.1")

    def test_malformed_number(self):
        with self.assertRaises(guard.ReleaseError):
            guard.parse_version("01.2.0")

    def test_duplicate_pr_declarations(self):
        packet = {"records": [row("patch", "1.4.11", "a"*40)]*2}
        with self.assertRaisesRegex(guard.ReleaseError, "duplicate"):
            guard.declaration_from_body("~~~vigil-incident-release\n"+json.dumps(packet)+"\n~~~", True)

    def test_missing_declarations(self):
        with self.assertRaisesRegex(guard.ReleaseError, "require"):
            guard.declaration_from_body("", True)

    def test_unmodified_pr_does_not_require_declaration(self):
        self.assertEqual(guard.declaration_from_body("Docs only.", False), {})


class SyntheticGitIntegration(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.run_git("init", "-b", "main")
        self.run_git("config", "user.email", "tests@example.invalid")
        self.run_git("config", "user.name", "VIGIL Test Fixture")
        self.file = self.root / FILE
        self.file.parent.mkdir(parents=True, exist_ok=True)
        self.write_record(record())
        self.run_git("add", ".")
        self.run_git("commit", "-m", "Initial published Incident")
        self.base = self.run_git("rev-parse", "HEAD")
        self.blob = self.run_git("rev-parse", "HEAD:"+FILE)
        self.run_git("update-ref", "refs/remotes/origin/main", self.base)
        self.run_git("checkout", "-b", "feature")

    def run_git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args], text=True, stderr=subprocess.STDOUT).strip()

    def write_record(self, value):
        self.file.write_text(json.dumps(value, indent=2)+"\n", encoding="utf-8")

    def commit(self, value):
        self.write_record(value)
        self.run_git("add", FILE)
        self.run_git("commit", "-m", "Working Incident revision")
        return self.run_git("rev-parse", "HEAD")

    def event(self, head, rows):
        return {"pull_request": {"base": {"ref": "main", "sha": self.base},
                                 "head": {"sha": head},
                                 "body": "~~~vigil-incident-release\n"+json.dumps({"records": rows})+"\n~~~"}}

    def test_complete_pr(self):
        head = self.commit(record("1.5.0", mapped=True))
        output = guard.inspect(self.event(head, [row("minor", "1.4.11", self.blob)]), self.root)
        self.assertEqual(output[0]["candidate_version"], "1.5.0")

    def test_stale_pr_base_rejected(self):
        head = self.commit(record("1.5.0", mapped=True))
        self.run_git("update-ref", "refs/remotes/origin/main", head)
        with self.assertRaisesRegex(guard.ReleaseError, "stale main"):
            guard.inspect(self.event(head, [row("minor", "1.4.11", self.blob)]), self.root)

    def test_deleted_incident_rejected(self):
        self.file.unlink()
        self.run_git("add", "-u")
        self.run_git("commit", "-m", "Accidental deletion")
        head = self.run_git("rev-parse", "HEAD")
        with self.assertRaisesRegex(guard.ReleaseError, "deletion"):
            guard.inspect(self.event(head, [row("minor", "1.4.11", self.blob)]), self.root)

    def test_nochange_docs_only(self):
        (self.root / "notes.txt").write_text("review", encoding="utf-8")
        self.run_git("add", "notes.txt")
        self.run_git("commit", "-m", "Docs")
        head = self.run_git("rev-parse", "HEAD")
        self.assertEqual(guard.inspect({"pull_request": {"base": {"ref": "main", "sha": self.base},
                                                      "head": {"sha": head}, "body": "review only"}}, self.root), [])



MANIFEST_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build-incident-publication-manifest.py"
_manifest_spec = importlib.util.spec_from_file_location("vigil_incident_publication_manifest", MANIFEST_SCRIPT)
manifest = importlib.util.module_from_spec(_manifest_spec)
assert _manifest_spec and _manifest_spec.loader
_manifest_spec.loader.exec_module(manifest)


class ManifestIntegration(SyntheticGitIntegration):
    def test_manifest_matches_committed_source(self):
        document = manifest.build(self.root)
        self.assertEqual(document["record_count"], 1)
        entry = document["records"][0]
        self.assertEqual(entry["incident_id"], ID)
        self.assertEqual(entry["source_commit"], self.base)
        self.assertEqual(entry["version"], "1.4.11")
        self.assertEqual(entry["previous_version"], None)
        self.assertEqual(entry["git_blob"], self.blob)

    def test_manifest_stable_after_generated_only_commit(self):
        original = manifest.build(self.root)
        (self.root / "test-index.json").write_text('{"generated":true}\n', encoding="utf-8")
        self.run_git("add", "test-index.json")
        self.run_git("commit", "-m", "Generated output only")
        self.assertEqual(original, manifest.build(self.root))

    def test_manifest_detects_uncommitted_canonical_edit(self):
        self.write_record(record("1.4.12", summary="uncommitted"))
        with self.assertRaisesRegex(ValueError, "differs from committed"):
            manifest.build(self.root)

    def test_manifest_new_revision_has_predecessor(self):
        self.run_git("checkout", "main")
        self.commit(record("1.5.0", mapped=True))
        entry = manifest.build(self.root)["records"][0]
        self.assertEqual(entry["version"], "1.5.0")
        self.assertEqual(entry["previous_version"], "1.4.11")


if __name__ == "__main__":
    unittest.main()
