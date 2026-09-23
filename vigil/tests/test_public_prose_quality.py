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

# Stage 01 on the public Case File renders record["summary"] verbatim as
# "What happened". It is not an assessment or taxonomy surface. Keep this
# contract separate from the broader public-prose quality check so a validator
# failure cannot reasonably be interpreted as an instruction to rewrite or
# compress the occurrence narrative.
SUMMARY_ONLY_PATTERNS = {
    **INTERNAL_PROSE_PATTERNS,
    "VIGIL diagnostic framing": re.compile(
        r"\bVIGIL\s+(?:classif(?:y|ies|ied)|treats?|maps?|assesses?|concludes?|therefore\b)",
        re.IGNORECASE,
    ),
    "classification scaffolding": re.compile(
        r"\b(?:taxonomy classification|classification status|failure class)\b",
        re.IGNORECASE,
    ),
}


def assessment_public_prose(record):
    assessment = record.get("vigil_assessment", {})
    harm = record.get("harm_impact_assessment", {})
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
    def test_stage01_summary_is_factual_what_happened_prose(self):
        failures = []
        for path in sorted(INCIDENTS.glob("VIGIL-INC-*.json")):
            record = json.loads(path.read_text(encoding="utf-8"))
            value = record.get("summary", "")
            if not isinstance(value, str):
                continue
            for label, pattern in SUMMARY_ONLY_PATTERNS.items():
                match = pattern.search(value)
                if match:
                    failures.append(
                        f"{record['id']} summary: {label} {match.group(0)!r}"
                    )
        self.assertEqual(
            failures,
            [],
            "\nStage 01 summary is rendered as 'What happened'. "
            "Remove only the offending taxonomy/diagnostic/maintenance wording; "
            "do not shorten, flatten or rewrite supported occurrence facts.\n"
            + "\n".join(failures),
        )

    def test_assessment_public_prose_does_not_depend_on_internal_shorthand(self):
        failures = []
        for path in sorted(INCIDENTS.glob("VIGIL-INC-*.json")):
            record = json.loads(path.read_text(encoding="utf-8"))
            for field, value in assessment_public_prose(record):
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
