#!/usr/bin/env python3
"""Validate exhaustive VIGIL Incident × Failure Class role adjudication."""
import argparse
import re
import runpy
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V = ROOT / "vigil"
T = V / "taxonomy"
MATRIX = T / "VIGIL.FailureTaxonomy.Adjudications.json"
INC = V / "records" / "incidents"
SYNC = runpy.run_path(str(V / "scripts" / "sync-vigil-taxonomy-adjudications.py"))
load = SYNC["load"]
current_classes = SYNC["current_classes"]

ROLE_DECISIONS = (
    "failure-occurrence",
    "successful-invariant",
    "ambiguous-boundary",
)
ALLOWED = set(ROLE_DECISIONS) | {"no-mapping", "unresolved", "MISSING"}
BAD_NO_MAPPING = (
    "no evidence",
    "not evidenced",
    "not established",
    "insufficient evidence",
    "unclear",
    "unknown",
    "not disclosed",
    "cannot determine",
    "could not determine",
)
UNRESOLVED_MARKERS = (
    "not public",
    "not publicly",
    "does not show",
    "does not establish",
    "not described",
    "not disclosed",
    "unresolved",
    "cannot establish",
    "unknown",
    "missing",
    "insufficient",
)
BOILERPLATE_PATTERNS = (
    r"^no material .+ mechanism is present in the bounded occurrence",
    r"required (?:failure )?conditions are outside the evidenced pathway",
    r"^(?:this |the )?class (?:does not apply|is not applicable)",
    r"^(?:not applicable|n/?a)[\.!]?$",
    r"^(?:no|none)\s*[-:]?\s*(?:applicable|relevant)[\.!]?$",
)

# Section 02 uses occurrence-level prose labels, but only these exact values
# are admitted as canonical role encodings. Similar-sounding strings such as
# "canonical failure mapping" are not silently interpreted as a role.
SECTION02_RELATIONSHIP_ROLES = {
    "failure-occurrence": "failure-occurrence",
    "failure-occurrence contribution": "failure-occurrence",
    "successful-invariant": "successful-invariant",
    "ambiguous-boundary exemplar": "ambiguous-boundary",
}


def canonical_mappings_by_role(record):
    block = record.get("taxonomy_classification", {})
    rows = [block.get("primary_classification")] + list(
        block.get("secondary_classifications") or []
    )
    result = {role: set() for role in ROLE_DECISIONS}
    invalid = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        class_id = row.get("class_id")
        role = row.get("classification_role")
        if not isinstance(class_id, str):
            continue
        if role in result:
            result[role].add(class_id)
        else:
            invalid.append((class_id, role))
    return result, invalid


def section02_mappings_by_role(record):
    assessment = record.get("vigil_assessment", {})
    analysis = assessment.get("source_clause_analysis", {}) if isinstance(assessment, dict) else {}
    clauses = analysis.get("clauses", []) if isinstance(analysis, dict) else []
    result = {role: set() for role in ROLE_DECISIONS}
    invalid = []
    for clause in clauses if isinstance(clauses, list) else []:
        if not isinstance(clause, dict):
            continue
        relationships = clause.get("taxonomy_relationships", [])
        for relationship in relationships if isinstance(relationships, list) else []:
            if not isinstance(relationship, dict):
                continue
            if relationship.get("canonical_taxonomy_mapping") is not True:
                continue
            class_id = relationship.get("class_id")
            label = relationship.get("relationship")
            if not isinstance(class_id, str):
                continue
            role = SECTION02_RELATIONSHIP_ROLES.get(label)
            if role is None:
                invalid.append((class_id, label))
            else:
                result[role].add(class_id)
    return result, invalid


def admitted_exemplars():
    """Return admitted reciprocal exemplar Incident IDs by class and role."""
    index = load(T / "VIGIL.FailureTaxonomy.Index.json")
    result = defaultdict(set)
    for family in index.get("families", []):
        data = load(T / family["file"])
        for item in data.get("classes", []):
            if not isinstance(item, dict):
                continue
            class_id = item.get("class_id")
            for exemplar in item.get("invariant_exemplars", []):
                if not isinstance(exemplar, dict):
                    continue
                role = exemplar.get("exemplar_type")
                incident_id = exemplar.get("linked_incident_id")
                if (
                    role in {"successful-invariant", "ambiguous-boundary"}
                    and exemplar.get("exemplar_status") == "admitted"
                    and isinstance(class_id, str)
                    and isinstance(incident_id, str)
                ):
                    result[(class_id, role)].add(incident_id)
    return result


def reciprocal_actions(incident_id, roles, exemplars):
    actions = []
    for role in ("successful-invariant", "ambiguous-boundary"):
        for class_id in sorted(roles[role]):
            if incident_id not in exemplars.get((class_id, role), set()):
                actions.append(
                    f"{incident_id}: {role} {class_id} lacks a matching admitted "
                    "taxonomy invariant_exemplar"
                )
    return actions


def compare_role_surfaces(incident_id, matrix_roles, record, exemplars):
    actions = []
    canonical, invalid_canonical = canonical_mappings_by_role(record)
    section02, invalid_section02 = section02_mappings_by_role(record)
    for class_id, role in invalid_canonical:
        actions.append(
            f"{incident_id}: canonical mapping {class_id} has unsupported "
            f"classification_role {role!r}"
        )
    for class_id, relationship in invalid_section02:
        actions.append(
            f"{incident_id}: Section 02 canonical taxonomy assessment {class_id} "
            f"has non-canonical relationship {relationship!r}"
        )
    for role in ROLE_DECISIONS:
        matrix_set = matrix_roles[role]
        canonical_set = canonical[role]
        section_set = section02[role]
        for class_id in sorted(canonical_set - matrix_set):
            actions.append(
                f"{incident_id}: canonical {role} mapping {class_id} is not "
                f"adjudicated {role}"
            )
        for class_id in sorted(matrix_set - canonical_set):
            actions.append(
                f"{incident_id}: matrix {role} {class_id} is not a canonical "
                f"{role} mapping"
            )
        for class_id in sorted(canonical_set - section_set):
            actions.append(
                f"{incident_id}: canonical {role} mapping {class_id} is missing "
                "from Section 02 with the same role"
            )
        for class_id in sorted(section_set - canonical_set):
            actions.append(
                f"{incident_id}: Section 02 {role} {class_id} is not a canonical "
                f"{role} mapping"
            )
        for class_id in sorted(matrix_set - section_set):
            actions.append(
                f"{incident_id}: matrix {role} {class_id} is missing from "
                "Section 02 with the same role"
            )
        for class_id in sorted(section_set - matrix_set):
            actions.append(
                f"{incident_id}: Section 02 {role} {class_id} is not adjudicated "
                f"{role} in the matrix"
            )
    actions.extend(reciprocal_actions(incident_id, canonical, exemplars))
    actions.extend(reciprocal_actions(incident_id, matrix_roles, exemplars))
    return list(dict.fromkeys(actions))


def validate_architecture_incidents(incident_ids):
    errors = []
    exemplars = admitted_exemplars()
    for incident_id in incident_ids:
        path = INC / f"{incident_id}.json"
        if not path.exists():
            errors.append(f"{incident_id}: canonical Incident missing")
            continue
        record = load(path)
        canonical, invalid = canonical_mappings_by_role(record)
        section02, invalid_section02 = section02_mappings_by_role(record)
        for class_id, role in invalid:
            errors.append(
                f"{incident_id}: canonical mapping {class_id} has unsupported "
                f"classification_role {role!r}"
            )
        for class_id, relationship in invalid_section02:
            errors.append(
                f"{incident_id}: Section 02 canonical taxonomy assessment "
                f"{class_id} has non-canonical relationship {relationship!r}"
            )
        for role in ROLE_DECISIONS:
            if canonical[role] != section02[role]:
                errors.append(
                    f"{incident_id}: canonical and Section 02 {role} sets differ "
                    f"({sorted(canonical[role])} != {sorted(section02[role])})"
                )
        errors.extend(reciprocal_actions(incident_id, canonical, exemplars))
    return errors


def validate(incident_filter=None):
    errors = []
    version, ids = current_classes()
    expected = set(ids)
    matrix = load(MATRIX)
    if matrix.get("schema_version") != "0.2.0":
        errors.append("schema_version must be 0.2.0")
    if matrix.get("taxonomy_version") != version:
        errors.append(f"taxonomy_version must be {version}")
    incidents = matrix.get("incidents", {})
    if not isinstance(incidents, dict) or not incidents:
        return errors + ["incidents must be a non-empty object"], []
    if incident_filter:
        absent = sorted(set(incident_filter) - set(incidents))
        if absent:
            return errors + [
                f"{incident_id}: Incident is not enrolled in the matrix"
                for incident_id in absent
            ], []
        incidents = {
            incident_id: incidents[incident_id]
            for incident_id in incident_filter
        }

    reviewed = {}
    for incident_id, rows in sorted(incidents.items()):
        path = INC / f"{incident_id}.json"
        if not path.exists():
            errors.append(f"{incident_id}: canonical Incident missing")
            continue
        if not isinstance(rows, dict):
            errors.append(f"{incident_id}: adjudications must be an object")
            continue
        missing = expected - set(rows)
        extra = set(rows) - expected
        if missing:
            errors.append(f"{incident_id}: missing {','.join(sorted(missing))}")
        if extra:
            errors.append(f"{incident_id}: non-current {','.join(sorted(extra))}")
        roles = {role: set() for role in ROLE_DECISIONS}
        seen_reasons = {}
        for class_id in sorted(expected & set(rows)):
            row = rows[class_id]
            label = f"{incident_id} {class_id}"
            if not isinstance(row, dict):
                errors.append(f"{label}: row must be an object")
                continue
            decision = row.get("decision")
            reason = row.get("reason", "")
            if decision not in ALLOWED:
                errors.append(f"{label}: invalid decision")
                continue
            prior = row.get("prior_failure_adjudication")
            if prior is not None and not (
                isinstance(prior, dict)
                and prior.get("decision") == "NO"
                and isinstance(prior.get("reason"), str)
                and prior["reason"].strip()
            ):
                errors.append(f"{label}: invalid prior_failure_adjudication")
            if decision == "MISSING":
                errors.append(f"{label}: MISSING")
                continue
            if not isinstance(reason, str) or not reason.strip():
                errors.append(f"{label}: reason required")
                continue
            if len(reason.strip()) > 280:
                errors.append(f"{label}: reason too long")
            lowered = reason.lower().strip()
            if any(re.search(pattern, lowered) for pattern in BOILERPLATE_PATTERNS):
                errors.append(
                    f"{label}: boilerplate adjudication reason is not permitted"
                )
            normalised = re.sub(
                r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", lowered)
            ).strip()
            if normalised in seen_reasons:
                errors.append(
                    f"{label}: adjudication reason duplicates "
                    f"{seen_reasons[normalised]}; reasons must be class-specific"
                )
            else:
                seen_reasons[normalised] = class_id
            if decision == "no-mapping" and any(
                marker in lowered for marker in BAD_NO_MAPPING
            ):
                errors.append(
                    f"{label}: evidence uncertainty must be unresolved, not "
                    "no-mapping"
                )
            if decision == "unresolved" and not any(
                marker in lowered for marker in UNRESOLVED_MARKERS
            ):
                errors.append(
                    f"{label}: unresolved reason must identify the missing or "
                    "indeterminate recognition fact"
                )
            if decision in roles:
                roles[decision].add(class_id)
        reviewed[incident_id] = (path, roles)

    # Matrix-quality failures must be repaired before canonical drift can be
    # treated as a genuine record-update action.
    if errors:
        return errors, []

    actions = []
    exemplars = admitted_exemplars()
    for incident_id, (path, roles) in sorted(reviewed.items()):
        actions.extend(
            compare_role_surfaces(incident_id, roles, load(path), exemplars)
        )
    return [], list(dict.fromkeys(actions))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--architecture-incident",
        action="append",
        default=[],
        help="check canonical/Section 02/exemplar role reciprocity without the matrix",
    )
    parser.add_argument(
        "--incident",
        action="append",
        default=[],
        help="validate only the named enrolled Incident(s), using the same rules",
    )
    args = parser.parse_args()
    if args.architecture_incident:
        architecture_errors = validate_architecture_incidents(
            args.architecture_incident
        )
        if architecture_errors:
            for item in architecture_errors:
                print("ERROR:", item, file=sys.stderr)
            raise SystemExit(1)
        print(
            "Validated taxonomy-role architecture for: "
            + ", ".join(args.architecture_incident)
        )
        raise SystemExit(0)

    errors, actions = validate(args.incident or None)
    if errors:
        for item in errors:
            print("ERROR:", item, file=sys.stderr)
        raise SystemExit(1)
    if actions:
        for item in actions:
            print("GMAIL ACTION REQUIRED:", item, file=sys.stderr)
        raise SystemExit(1)
    matrix = load(MATRIX)
    validated_incidents = (
        args.incident if args.incident else list(matrix["incidents"])
    )
    print(
        f"Validated taxonomy adjudications: {len(validated_incidents)} "
        f"Incident(s), {sum(len(matrix['incidents'][incident_id]) for incident_id in validated_incidents)} "
        "decisions, zero gaps."
    )
    print(
        "Gmail notification not required: the clean matrix matches canonical "
        "Incident and Section 02 mappings role-by-role."
    )
