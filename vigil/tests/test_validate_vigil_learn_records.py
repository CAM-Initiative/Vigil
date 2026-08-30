#!/usr/bin/env python3
"""Regression check for the current public LEARN boundary.

LEARN records are intentionally withdrawn to ``vigil/drafts`` while their design,
schema, and publication model are under review. Public validation must therefore
not load or resolve them.
"""

from __future__ import annotations

import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VIGIL_DIR = SCRIPT_DIR.parent
PUBLIC_LEARN_ROOT = VIGIL_DIR / "records" / "learn"


class LearnPublicBoundaryTests(unittest.TestCase):
    def test_no_public_learn_record_tree_exists(self) -> None:
        self.assertFalse(PUBLIC_LEARN_ROOT.exists())


if __name__ == "__main__":
    unittest.main()
