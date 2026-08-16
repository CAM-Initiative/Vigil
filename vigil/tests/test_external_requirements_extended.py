#!/usr/bin/env python3
"""Guard the effective external-requirements extension architecture."""
from __future__ import annotations

import importlib.util
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "manage-external-requirements-extended.py"
SPEC = importlib.util.spec_from_file_location("extended_requirements", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class EffectiveExternalRequirementsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        outputs, errors = MODULE.effective()
        cls.assert_errors = errors
        cls.requirements = MODULE.json.loads(outputs[MODULE.EREQ])["requirements"]

    def test_effective_build_has_no_contract_errors(self) -> None:
        self.assertEqual(self.assert_errors, [])

    def test_priority_ieee_sources_have_substantive_direct_extractions(self) -> None:
        counts = Counter(r["external_source_id"] for r in self.requirements)
        minimums = {
            "IEEE-7000": 50,
            "IEEE-7001": 30,
            "IEEE-7007": 10,
            "IEEE-7009": 50,
            "IEEE-7010": 18,
            "IEEE-7014": 40,
            "IEEE-7014.1": 60,
        }
        for source_id, minimum in minimums.items():
            self.assertGreaterEqual(counts[source_id], minimum, source_id)

    def test_recommended_practices_are_not_inflated_to_mandatory(self) -> None:
        for record in self.requirements:
            if record["external_source_id"] in {"IEEE-7010", "IEEE-7014.1"}:
                self.assertEqual(record["requirement_posture"], "recommended-practice")

    def test_ontology_is_not_converted_into_operational_duties(self) -> None:
        records = [r for r in self.requirements if r["external_source_id"] == "IEEE-7007"]
        self.assertTrue(records)
        self.assertTrue(all(r["requirement_posture"] == "definitional" for r in records))
        self.assertTrue(all(r["expectation_type"] == "definition" for r in records))

    def test_access_blocked_source_has_no_reconstructed_requirements(self) -> None:
        self.assertFalse(any(r["external_source_id"] == "IEEE-2863" for r in self.requirements))

    def test_supporting_sources_remain_outside_exhaustive_decomposition(self) -> None:
        supporting = {"IEEE-2089", "IEEE-7002", "IEEE-7005", "IEEE-7012"}
        self.assertFalse(any(r["external_source_id"] in supporting for r in self.requirements))

    def test_annex_a3_stable_records_are_not_duplicated(self) -> None:
        records = [
            r for r in self.requirements
            if r["external_source_id"] == "IEEE-7009"
            and r["clause_or_control"].startswith("Annex A.3 / 7009-ASR-")
        ]
        self.assertEqual(len(records), 16)
        self.assertEqual(len({r["requirement_id"] for r in records}), 16)


if __name__ == "__main__":
    unittest.main()
