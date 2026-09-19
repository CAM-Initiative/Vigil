import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INCIDENTS = ROOT / "vigil" / "records" / "incidents"

INTERNAL_PROSE_PATTERNS = {
    "taxonomy identifier": re.compile(r"VIGIL-(?:FC|FF)-|\bFC-\d|VIGIL-\d{4}-FM-", re.IGNORECASE),
    "record-maintenance language": re.compile(
        r"canonical Incident|classifier narrative|taxonomy gap|post-promotion|"
        r"current branch|review pass|(?:schema|taxonomy|record) migration|\b(?:mapped|unmapped)\b",
        re.IGNORECASE,
    ),
}


def public_prose(record):
    assessment = record.get("vigil_assessment", {})
    harm = record.get("harm_impact_assessment", {})
    yield "summary", record.get("summary", "")
    for field in (
        "factual_basis",
        "governance_interpretation",
        "significance_to_cam",
    ):
        yield f"vigil_assessment.{field}", assessment.get(field, "")
    for index, value in enumerate(assessment.get("assessment_boundaries", [])):
        yield f"vigil_assessment.assessment_boundaries[{index}]", value
    for field in ("coverage_note", "no_materialised_harm_basis"):
        yield f"harm_impact_assessment.{field}", harm.get(field, "")
    for index, dimension in enumerate(harm.get("dimensions", [])):
        yield (
            f"harm_impact_assessment.dimensions[{index}].assessment_basis",
            dimension.get("assessment_basis", ""),
        )
    for index, source in enumerate(record.get("source_records", [])):
        for field in ("relevance_note", "evidence_status_basis"):
            yield f"source_records[{index}].{field}", source.get(field, "")


class PublicProseQualityTests(unittest.TestCase):
    def test_public_prose_does_not_depend_on_taxonomy_or_maintenance_shorthand(self):
        failures = []
        for path in sorted(INCIDENTS.glob("VIGIL-INC-*.json")):
            record = json.loads(path.read_text(encoding="utf-8"))
            for field, value in public_prose(record):
                if not isinstance(value, str):
                    continue
                for label, pattern in INTERNAL_PROSE_PATTERNS.items():
                    match = pattern.search(value)
                    if match:
                        failures.append(
                            f"{record['id']} {field}: {label} {match.group(0)!r}"
                        )
        self.assertEqual(failures, [], "\n" + "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
