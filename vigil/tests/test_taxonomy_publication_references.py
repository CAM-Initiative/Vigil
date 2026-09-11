"""Regression tests for the canonical-reference publication projection."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

TAXONOMY_ROOT = Path(__file__).resolve().parents[1] / "taxonomy"
sys.path.insert(0, str(TAXONOMY_ROOT))
SPEC = importlib.util.spec_from_file_location(
    "render_taxonomy_publication", TAXONOMY_ROOT / "render_taxonomy_publication.py"
)
RENDERER = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(RENDERER)


class TaxonomyPublicationReferenceTests(unittest.TestCase):
    def test_shared_reference_retains_class_specific_evidence_notes(self):
        families = [
            {
                "classes": [
                    {
                        "class_id": "VIGIL-FC-000001",
                        "name": "First class",
                        "external_references": [
                            {
                                "title": "Primary source",
                                "publisher": "Publisher",
                                "date": "2026-01-01",
                                "url": "https://example.test/source",
                                "reference_role": "authoritative-guidance",
                                "evidence_note": "Supports the first boundary.",
                            }
                        ],
                    },
                    {
                        "class_id": "VIGIL-FC-000002",
                        "name": "Second class",
                        "external_references": [
                            {
                                "title": "Primary source",
                                "publisher": "Publisher",
                                "date": "2026-01-01",
                                "url": "https://example.test/source/",
                                "reference_role": "authoritative-guidance",
                                "evidence_note": "Supports only the second condition.",
                            }
                        ],
                    },
                ]
            }
        ]

        references = RENDERER.collect_external_references(families)
        self.assertEqual(len(references), 1)
        self.assertEqual(
            [item["evidence_note"] for item in references[0]["classes"]],
            ["Supports the first boundary.", "Supports only the second condition."],
        )

        rendered = RENDERER.bibliography_html(families)
        self.assertEqual(rendered.count('class="bibliography-entry"'), 1)
        self.assertIn("Supports the first boundary.", rendered)
        self.assertIn("Supports only the second condition.", rendered)

    def test_distinct_provisions_at_one_url_remain_distinct_citations(self):
        families = [
            {
                "classes": [
                    {
                        "class_id": "VIGIL-FC-000001",
                        "name": "First class",
                        "external_references": [
                            {
                                "title": "Instrument, Article 5",
                                "publisher": "Publisher",
                                "date": "2026-01-01",
                                "url": "https://example.test/instrument",
                                "reference_role": "regulatory-evidence",
                            }
                        ],
                    },
                    {
                        "class_id": "VIGIL-FC-000002",
                        "name": "Second class",
                        "external_references": [
                            {
                                "title": "Instrument, Article 12",
                                "publisher": "Publisher",
                                "date": "2026-01-01",
                                "url": "https://example.test/instrument",
                                "reference_role": "regulatory-evidence",
                            }
                        ],
                    },
                ]
            }
        ]

        references = RENDERER.collect_external_references(families)
        self.assertEqual(
            [item["title"] for item in references],
            ["Instrument, Article 5", "Instrument, Article 12"],
        )


    def test_subtype_publication_hierarchy_avoids_orphaned_headings_without_forced_pages(self):
        item = {
            "subtypes": [
                {
                    "name": "Delegation Scope Expansion",
                    "historical_class_id": "VIGIL-FC-000008",
                    "historical_class_code": "DELEGATION_SCOPE_EXPANSION",
                    "plain_english": "A prior permission is stretched into a materially new action.",
                    "definition": "A bounded subtype definition.",
                    "recognition": {"required_conditions": ["A required condition is present."]},
                    "exclusions": ["A bounded exclusion applies."],
                    "examples": ["A bounded illustrative example."],
                }
            ]
        }

        rendered = RENDERER.base.subtype_html(item, heading="h3")
        self.assertIn('class="subtypes-heading"', rendered)
        self.assertIn('class="subtype-title"', rendered)

        print_style = RENDERER.base.PRINT_STYLE
        self.assertIn(".subtypes-heading{", print_style)
        self.assertIn("break-after:avoid-page", print_style)
        self.assertIn(".subtype-title{", print_style)
        self.assertIn(".subtypes{margin-top:8mm", print_style)
        self.assertIn("break-before:auto", print_style)
        self.assertNotIn(".subtypes{break-before:page", print_style)

if __name__ == "__main__":
    unittest.main()
