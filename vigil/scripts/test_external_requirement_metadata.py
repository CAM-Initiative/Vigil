#!/usr/bin/env python3
"""Regression checks for the EXTREQ metadata-review contract."""
from __future__ import annotations
import importlib.util
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQ = ROOT / "external_requirements"
SCRIPTS = ROOT / "scripts"
FIELDS = {
    "applicable_actor",
    "governed_object",
    "timing_or_frequency",
    "required_artefacts",
    "evidence_expectation",
    "verification_method",
    "applicability_conditions",
    "exceptions_or_qualifications",
}
STATUSES = {
    "populated-reviewed",
    "not-specified-by-source",
    "not-applicable",
    "review-required",
}


def load_script(name: str):
    path = SCRIPTS / name
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def assert_conflict_intolerant(script_name: str, requirement_id: str) -> None:
    module = load_script(script_name)
    ledger = json.loads((REQ / "metadata-review.json").read_text(encoding="utf-8"))
    target = next(entry for entry in ledger["entries"] if entry["requirement_id"] == requirement_id)
    field = "applicable_actor"
    target["field_status"][field] = (
        "review-required" if target["field_status"][field] != "review-required" else "populated-reviewed"
    )
    with tempfile.TemporaryDirectory() as directory:
        conflict = Path(directory) / "metadata-review.json"
        conflict.write_text(json.dumps(ledger), encoding="utf-8")
        module.LEDGER = conflict
        try:
            module.seed(False)
        except ValueError as error:
            assert "manual reconciliation required" in str(error)
        else:
            raise AssertionError(f"{script_name} accepted a conflicting review decision")


def main():
    schema = json.loads((REQ / "metadata-review.schema.json").read_text(encoding="utf-8"))
    ledger = json.loads((REQ / "metadata-review.json").read_text(encoding="utf-8"))
    assert schema["properties"]["schema_version"]["const"] == "1.0"
    required = set(schema["properties"]["entries"]["items"]["properties"]["field_status"]["required"])
    assert required == FIELDS
    enum = set(schema["$defs"]["status"]["enum"])
    assert enum == STATUSES
    assert ledger["schema_version"] == "1.0"
    assert isinstance(ledger["entries"], list)
    ids = [entry["requirement_id"] for entry in ledger["entries"]]
    assert len(ids) == len(set(ids))
    assert len(ids) == 539

    backlog_schema = json.loads((REQ / "reextraction-backlog.schema.json").read_text(encoding="utf-8"))
    backlog = json.loads((REQ / "reextraction-backlog.json").read_text(encoding="utf-8"))
    assert backlog_schema["properties"]["schema_version"]["const"] == "1.0"
    backlog_ids = [entry["current_requirement_id"] for entry in backlog["entries"]]
    assert len(backlog_ids) == len(set(backlog_ids)) == 0
    assert sum(entry["external_source_id"] == "NIST-AI-600-1" for entry in backlog["entries"]) == 0
    assert sum(entry["external_source_id"] == "CYCLONEDX-SPEC" for entry in backlog["entries"]) == 0
    assert sum(entry["external_source_id"] == "IMDA-AGENTIC-AI-MGF" for entry in backlog["entries"]) == 0
    assert sum(entry["external_source_id"] == "NIST-SP-800-218A" for entry in backlog["entries"]) == 0
    assert sum(entry["external_source_id"] == "AAM-SDOS-RUNTIME-GOVERNANCE" for entry in backlog["entries"]) == 0

    sdos = json.loads((REQ / "requirements" / "AAM-SDOS-RUNTIME-GOVERNANCE" / "1.10.json").read_text(encoding="utf-8"))
    sdos_by_control = {record["clause_or_control"]: record for record in sdos}
    assert len(sdos) == 24
    assert all(record["source_review_date"] == "2026-08-28" for record in sdos)
    assert all(
        record["interpretation_provenance"]["reviewed_source_digest"]
        == "547bfa9615f137429871951e2beb8de8f306ed8ae4995e6ef95dfcfbcc23c52b"
        for record in sdos
    )
    assert all(record["related_external_requirements"] for record in sdos)
    assert all(record["governed_object"] != ["agentic AI runtime governance system"] for record in sdos)
    assert "explicit re-authorization" in sdos_by_control["SDOS-IN-02"]["timing_or_frequency"][0]
    assert any("correctness guarantee" in value for value in sdos_by_control["SDOS-DE-01"]["exceptions_or_qualifications"])

    nist_218a = json.loads((REQ / "requirements" / "NIST-SP-800-218A" / "2024.json").read_text(encoding="utf-8"))
    nist_218a_by_clause = {record["clause_or_control"]: record for record in nist_218a}
    assert len(nist_218a) == 75
    assert nist_218a_by_clause["PW.7.1 R1"]["requirement_id"] == "EXTREQ-CFC9864F6289630A"
    assert nist_218a_by_clause["PW.7.1 C1"]["requirement_id"] == "EXTREQ-1FFE1710582A469A"
    assert nist_218a_by_clause["PW.7.1 R1"]["requirement_posture"] == "recommended-practice"
    assert nist_218a_by_clause["PW.7.1 C1"]["requirement_posture"] == "informative-guidance"
    assert all("…" not in record["requirement_summary"] for record in nist_218a)
    assert all(
        record["interpretation_provenance"]["reviewed_source_digest"]
        == "e088c8bc75716824dae7c36a987f408364638561d381ed001b5c12254a7b10d8"
        for record in nist_218a
    )

    cyclonedx = json.loads((REQ / "requirements" / "CYCLONEDX-SPEC" / "1.7.json").read_text(encoding="utf-8"))
    cyclonedx_by_id = {record["requirement_id"]: record for record in cyclonedx}
    assert len(cyclonedx) == 5
    assert cyclonedx_by_id["EXTREQ-FA1B882FFAD54D93"]["requirement_posture"] == "conformity-evidence-expectation"
    assert cyclonedx_by_id["EXTREQ-F2C81603A7B306F6"]["requirement_posture"] == "recommended-practice"
    assert "must be unique" in cyclonedx_by_id["EXTREQ-FA1B882FFAD54D93"]["requirement_summary"]
    assert "should not start" in cyclonedx_by_id["EXTREQ-F2C81603A7B306F6"]["requirement_summary"]
    assert all(
        record["interpretation_provenance"]["reviewed_source_digest"]
        == "df472ef4aaf593904c479293723a1a5c191d6672715c93b3c0b5c318f3914221"
        for record in cyclonedx
    )

    reviewed_module = load_script("seed-reviewed-source-metadata.py")
    imda = json.loads((REQ / "requirements" / "IMDA-AGENTIC-AI-MGF" / "2026-05.json").read_text(encoding="utf-8"))
    imda_by_id = {record["requirement_id"]: record for record in imda}
    assert len(imda) == 39
    assert len(reviewed_module.IMDA_FIDELITY_REPAIRS) == 27
    assert reviewed_module.IMDA_FIDELITY_REPAIRS <= set(imda_by_id)
    assert all(
        record["interpretation_provenance"]["reviewed_source_digest"]
        == "2636e19ff1c86e862394d2fc900592e97b83c04cc35e3c8443108114b7f1dfba"
        for record in imda
    )
    for rid in {"EXTREQ-4253F163EB11C1C9", "EXTREQ-47EE577CC52EF131", "EXTREQ-82D791A7B54305B0", "EXTREQ-90553A3F265B9C63", "EXTREQ-99712BA8308E32FF"}:
        assert imda_by_id[rid]["parent_section_or_group"] in {"2.2.1", "2.3.2", "2.4.2"}

    nist_gai = json.loads((REQ / "requirements" / "NIST-AI-600-1" / "2024.json").read_text(encoding="utf-8"))
    nist_gai_by_id = {record["requirement_id"]: record for record in nist_gai}
    reviewed_module = load_script("seed-reviewed-source-metadata.py")
    repairs = reviewed_module.NIST_GAI_CONSTITUENT_REPAIRS
    assert len(repairs) == 60
    assert repairs <= set(nist_gai_by_id)
    review_by_id = {entry["requirement_id"]: entry for entry in ledger["entries"]}
    generic_values = {
        "Generative AI system and associated risk-management practices",
        "Documentation expressly specified by the cited requirement or control.",
        "Documented output or record specified by the cited action.",
        "Monitoring output or review record specified by the cited action.",
    }
    for rid in repairs:
        record = nist_gai_by_id[rid]
        assert "…" not in record["requirement_summary"]
        assert record["requirement_summary"] == record["governance_expectation"]
        assert record["source_review_date"] == "2026-08-28"
        assert record["interpretation_provenance"]["reviewed_source_digest"] == reviewed_module.NIST_GAI_REVIEW_DIGEST
        assert all(
            value not in generic_values
            for field in FIELDS
            for value in record.get(field, [])
        )
        assert all(review_by_id[rid]["field_status"][field] != "review-required" for field in FIELDS)

    validator = (SCRIPTS / "validate-external-requirement-metadata.py").read_text(encoding="utf-8")
    assert '"source_summary"' in validator
    assert '"field_observation"' in validator
    assert '"field_summary"' in validator
    assert '"blocked_sources"' in validator
    assert '"reextraction_defect_categories"' in validator
    assert "--write-report" in validator
    assert "--strict" in validator

    seeder = (SCRIPTS / "seed-eu-ai-act-metadata-review.py").read_text(encoding="utf-8")
    assert '"direct-primary-text"' in seeder
    assert '"not-specified-by-source"' in seeder
    assert "manual reconciliation required" in seeder
    assert "--write" in seeder

    reviewed_seeder = (SCRIPTS / "seed-reviewed-source-metadata.py").read_text(encoding="utf-8")
    assert "NIST_GAI_CONSTITUENT_REPAIRS" in reviewed_seeder
    assert "IMDA_FIDELITY_REPAIRS" in reviewed_seeder
    assert "NIST_218A_REPAIRS" in reviewed_seeder
    assert "SDOS_REVIEW_DIGEST" in reviewed_seeder
    assert (SCRIPTS / "migrate-nist-218a-pw71.py").is_file()
    assert "CYCLONEDX_MODALITY_REPAIRS" in reviewed_seeder
    assert (SCRIPTS / "migrate-cyclonedx-bom-ref-modality.py").is_file()
    assert (SCRIPTS / "migrate-imda-agentic-fidelity.py").is_file()
    assert (SCRIPTS / "migrate-sdos-runtime-fidelity.py").is_file()
    assert "AI Actor Tasks (subcategory-level)" in reviewed_seeder
    assert "manual reconciliation required" in reviewed_seeder
    assert "--write" in reviewed_seeder

    assert_conflict_intolerant("seed-eu-ai-act-metadata-review.py", "EXTREQ-8406A6A9A7ECFCB6")
    assert_conflict_intolerant("seed-reviewed-source-metadata.py", "EXTREQ-0055BCF6AB20FDB7")

    print("External requirement metadata-review contract regression passed")


if __name__ == "__main__":
    main()
