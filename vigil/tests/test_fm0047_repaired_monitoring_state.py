#!/usr/bin/env python3
"""Regression coverage for repaired CAM doctrine with unresolved external monitoring."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RECORD = ROOT / "vigil/records/failures/2026/VIGIL-2026-FM-0047.json"


class FM0047RepairedMonitoringStateTests(unittest.TestCase):
    def test_repaired_cam_state_preserves_external_monitoring_gaps(self) -> None:
        record = json.loads(RECORD.read_text(encoding="utf-8"))

        self.assertEqual(record["record_state"], "monitoring")
        self.assertEqual(record["repair_status"]["status"], "repaired")
        self.assertEqual(record["corpus_coverage"]["classification"], "implemented-repair")
        self.assertEqual(record["ecosystem_status"]["status"], "active")
        self.assertTrue(record["ecosystem_status"]["monitoring_required"])
        self.assertTrue(record["repair_status"]["remaining_gaps"])


if __name__ == "__main__":
    unittest.main()
