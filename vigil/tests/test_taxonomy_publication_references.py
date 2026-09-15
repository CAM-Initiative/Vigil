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

    def test_class_invariant_renders_when_published(self):
        item = {
            "class_id": "VIGIL-FC-000055",
            "class_code": "SECONDARY_PURPOSE_AUTHORITY_TRANSPOSITION",
            "family_id": "VIGIL-FF-0001",
            "name": "Secondary-Purpose Authority Transposition",
            "status": "beta",
            "abstraction": "class",
            "plain_english": "Primary-purpose authority is reused for another purpose.",
            "definition": "A bounded class definition.",
            "invariant": "Authority is purpose-bound and must be revalidated for a materially different secondary purpose.",
            "recognition": {"required_conditions": ["A required condition is present."]},
            "exclusions": ["A bounded exclusion applies."],
            "examples": ["A bounded example applies."],
            "aliases": [],
        }

        publication = RENDERER.base.publication_class_html(item, "1.1", {}, [])
        self.assertIn("Class invariant", publication)
        self.assertIn("Authority is purpose-bound", publication)

        portable = RENDERER.base.class_html(item, [])
        self.assertIn("Class invariant", portable)
        self.assertIn("Authority is purpose-bound", portable)

    def test_invariant_exemplar_renders_separately_from_failure_case_studies(self):
        exemplar = {
            "exemplar_type": "successful-invariant",
            "exemplar_status": "admitted",
            "linked_incident_id": "VIGIL-INC-000126",
            "title": "Protected escalation example",
            "evidence_basis": "The concern remained reviewable by an independent human.",
            "invariant_demonstrated": "Independent review remained available.",
            "success_basis": "The AI did not make the final disclosure decision.",
            "boundary_conditions": ["The occurrence was simulated."],
            "governance_placement": {
                "framework": "CAELESTIS",
                "instrument_id": "CAM-EQ2026-STEWARD-003-PLATINUM",
                "section_or_control": "§7",
                "placement_note": "Neutrality assurance reference.",
            },
            "provenance_note": "Occurrence evidence remains in the linked Incident.",
        }
        rendered = RENDERER.base.invariant_exemplars_html([exemplar])
        self.assertIn("Invariant exemplars", rendered)
        self.assertIn("successful-invariant", rendered)
        self.assertIn("VIGIL-INC-000126", rendered)
        self.assertIn("Why this is not failure evidence", rendered)
        self.assertNotIn("Case Study", rendered)

    def test_prior_codes_remain_metadata_but_are_not_published(self):
        family_alias = "LEGACY.FAMILY.CODE.SHOULD.NOT.RENDER"
        class_alias = "LEGACY.CLASS.CODE.SHOULD.NOT.RENDER"
        data = {
            "family": {
                "family_id": "VIGIL-FF-9999",
                "family_code": "CURRENT_FAMILY_CODE",
                "name": "Synthetic family",
                "status": "beta",
                "version": "0.0.0-test",
                "abstraction": "family",
                "plain_english": "Synthetic family used to test publication projection.",
                "definition": "A bounded synthetic family definition.",
                "invariant": "The current canonical identity remains authoritative.",
                "inclusion_rule": "Include only for the synthetic test.",
                "exclusion_rule": "Exclude all non-test cases.",
                "scope": ["Synthetic test scope."],
                "allowed_class_ids": ["VIGIL-FC-999999"],
                "allowed_class_codes": ["CURRENT_CLASS_CODE"],
                "aliases": [family_alias],
            },
            "classes": [
                {
                    "class_id": "VIGIL-FC-999999",
                    "class_code": "CURRENT_CLASS_CODE",
                    "family_id": "VIGIL-FF-9999",
                    "name": "Synthetic class",
                    "status": "beta",
                    "abstraction": "class",
                    "plain_english": "Synthetic class used to test publication projection.",
                    "definition": "A bounded synthetic class definition.",
                    "recognition": {"required_conditions": ["Synthetic condition."]},
                    "exclusions": ["Synthetic exclusion."],
                    "examples": ["Synthetic example."],
                    "aliases": [class_alias],
                }
            ],
        }

        self.assertEqual(data["family"]["aliases"], [family_alias])
        self.assertEqual(data["classes"][0]["aliases"], [class_alias])

        rendered = [
            RENDERER.base.markdown_family(data),
            RENDERER.base.html_family(data),
            RENDERER.base.publication_family_html(data, 1),
        ]
        for output in rendered:
            self.assertNotIn("Prior codes", output)
            self.assertNotIn(family_alias, output)
            self.assertNotIn(class_alias, output)
            self.assertIn("CURRENT_FAMILY_CODE", output)
            self.assertIn("CURRENT_CLASS_CODE", output)

    def test_publication_cover_surfaces_standard_version_and_beta_status(self):
        index = {
            "standard": {
                "version": "0.4.2",
                "status": "beta",
                "publication_date": "2026-09-11",
            }
        }
        families = [{"classes": []}]
        rendered = RENDERER.base.publication_frontmatter(index, families)
        self.assertIn("VIGIL Failure Taxonomy 0.4.2", rendered)
        self.assertIn("Status: Beta", rendered)
        self.assertIn("Governance<br>Failure<br>Taxonomy", rendered)
        self.assertIn("Technical Reference", rendered)

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


    def test_retired_subtype_material_is_not_published(self):
        families = RENDERER.base.load_catalogue()
        subtype_count = 0

        for chapter_number, data in enumerate(families, start=1):
            subtypes = [
                subtype
                for item in data["classes"]
                for subtype in item.get("subtypes", [])
            ]
            subtype_count += len(subtypes)
            rendered = [
                RENDERER.base.markdown_family(data),
                RENDERER.base.html_family(data),
                RENDERER.base.publication_family_html(data, chapter_number),
            ]
            for output in rendered:
                self.assertNotIn("Non-selectable subtypes and recognition patterns", output)
                for subtype in subtypes:
                    retired_values = [
                        subtype["historical_class_id"],
                        subtype["historical_class_code"],
                        subtype["name"],
                        subtype["plain_english"],
                        subtype["definition"],
                        *subtype["recognition"]["required_conditions"],
                        *subtype["exclusions"],
                        *subtype["examples"],
                        *subtype.get("aliases", []),
                    ]
                    for value in retired_values:
                        self.assertNotIn(value, output)

                for item in data["classes"]:
                    self.assertIn(item["class_id"], output)
                    self.assertIn(item["name"], output)

        self.assertEqual(subtype_count, 7)

if __name__ == "__main__":
    unittest.main()
