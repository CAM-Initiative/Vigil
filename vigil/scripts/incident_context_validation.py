"""Gate 1 opt-in canonical context validation for Incidents.

Validate only *new* structured relationships. Existing jurisdictional_context text,
system_context, source evidence, classification and harm remain unchanged.
No assertion here proves the underlying claim or legal applicability.
"""
from __future__ import annotations

import re
from typing import Any

COUNTRY_CODES = frozenset((
    "AD AE AF AG AI AL AM AO AQ AR AS AT AU AW AX AZ BA BB BD BE BF BG BH BI BJ BL BM BN BO BQ BR BS BT BV BW BY BZ CA CC CD CF CG CH CI CK CL CM CN CO CR CU CV CW CX CY CZ DE DJ DK DM DO DZ EC EE EG EH ER ES ET FI FJ FK FM FO FR GA GB GD GE GF GG GH GI GL GM GN GP GQ GR GS GT GU GW GY HK HM HN HR HT HU ID IE IL IM IN IO IQ IR IS IT JE JM JO JP KE KG KH KI KM KN KP KR KW KY KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MF MG MH MK ML MM MN MO MP MQ MR MS MT MU MV MW MX MY MZ NA NC NE NF NG NI NL NO NP NR NU NZ OM PA PE PF PG PH PK PL PM PN PR PS PT PW PY QA RE RO RS RU RW SA SB SC SD SE SG SH SI SJ SK SL SM SN SO SR SS ST SV SX SY SZ TC TD TF TG TH TJ TK TL TM TN TO TR TT TV TW TZ UA UG UM US UY UZ VA VC VE VG VI VN VU WF WS YE YT ZA ZM ZW"
).split())

SOURCE_REF = re.compile(r"source_records\[(\d+)\]\Z")
PARTY_ID = re.compile(r"PARTY-\d{3,}\Z")
GEO_ID = re.compile(r"GEO-\d{3,}\Z")
SUBDIVISION_CODE = re.compile(r"[A-Z]{2}-[A-Z0-9]{1,3}\Z")

def nonblank(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())

def source_refs(value: Any, label: str, record: dict[str, Any], errors: list[str], *, mandatory: bool):
    if not isinstance(value, list):
        errors.append(f"{label}.source_record_refs must be an array")
        return
    if mandatory and not value:
        errors.append(f"{label}.source_record_refs requires evidence for an asserted relationship")
    sources = record.get("source_records")
    for ref in value:
        match = SOURCE_REF.fullmatch(ref) if isinstance(ref, str) else None
        if match is None or not isinstance(sources, list) or int(match.group(1)) >= len(sources):
            errors.append(f"{label}.source_record_refs contains invalid source_records[N] reference")
    if len(value) != len({repr(ref) for ref in value}):
        errors.append(f"{label}.source_record_refs must be unique")

def validate(record: dict[str, Any], rules: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    party_ids: set[str] = set()
    parties = record.get("affected_party_context")
    if parties is not None:
        if not isinstance(parties, dict) or set(parties) != {"entities"} or not isinstance(parties.get("entities"), list):
            errors.append("affected_party_context must contain only an entities array")
        else:
            for i, party in enumerate(parties["entities"]):
                label = f"affected_party_context.entities[{i}]"
                if not isinstance(party, dict):
                    errors.append(f"{label} must be an object")
                    continue
                allowed = {"party_id", "name", "kind", "roles", "evidence_state", "evidence_basis", "source_record_refs"}
                if set(party) - allowed:
                    errors.append(f"{label} contains unknown fields: {sorted(set(party)-allowed)}")
                party_id = party.get("party_id")
                if not isinstance(party_id, str) or PARTY_ID.fullmatch(party_id) is None:
                    errors.append(f"{label}.party_id must use PARTY-NNN")
                elif party_id in party_ids:
                    errors.append(f"{label}.party_id must be unique within the Incident")
                else:
                    party_ids.add(party_id)
                if not nonblank(party.get("name")):
                    errors.append(f"{label}.name must be non-empty")
                if party.get("kind") not in rules["party_kinds"]:
                    errors.append(f"{label}.kind must be an allowed kind")
                roles = party.get("roles")
                if not isinstance(roles, list) or not roles or any(not isinstance(r, str) or r not in rules["party_roles"] for r in roles):
                    errors.append(f"{label}.roles must be a non-empty controlled array")
                elif len(roles) != len(set(roles)):
                    errors.append(f"{label}.roles must be unique")
                state = party.get("evidence_state")
                if state not in rules["evidence_states"]:
                    errors.append(f"{label}.evidence_state must be allowed")
                if not nonblank(party.get("evidence_basis")):
                    errors.append(f"{label}.evidence_basis must be non-empty")
                source_refs(party.get("source_record_refs"), label, record, errors, mandatory=state != "unresolved")

    jurisdiction = record.get("jurisdictional_context")
    if not isinstance(jurisdiction, dict) or "normalized_geography" not in jurisdiction:
        return errors
    geo = jurisdiction["normalized_geography"]
    if not isinstance(geo, dict) or set(geo) != {"scope", "relations"} or not isinstance(geo.get("relations"), list):
        errors.append("jurisdictional_context.normalized_geography requires scope and relations array, with no other fields")
        return errors
    if geo["scope"] not in rules["geographic_scopes"]:
        errors.append("jurisdictional_context.normalized_geography.scope must be allowed")
    relation_ids: set[str] = set()
    for i, relation in enumerate(geo["relations"]):
        label = f"jurisdictional_context.normalized_geography.relations[{i}]"
        if not isinstance(relation, dict):
            errors.append(f"{label} must be an object")
            continue
        allowed = {"relationship_id", "role", "evidence_state", "evidence_basis", "source_record_refs", "locations", "party_refs"}
        if set(relation) - allowed:
            errors.append(f"{label} contains unknown fields: {sorted(set(relation)-allowed)}")
        rel_id = relation.get("relationship_id")
        if not isinstance(rel_id, str) or GEO_ID.fullmatch(rel_id) is None:
            errors.append(f"{label}.relationship_id must use GEO-NNN")
        elif rel_id in relation_ids:
            errors.append(f"{label}.relationship_id must be unique within the Incident")
        else:
            relation_ids.add(rel_id)
        if relation.get("role") not in rules["geographic_roles"]:
            errors.append(f"{label}.role must be allowed")
        state = relation.get("evidence_state")
        if state not in rules["evidence_states"]:
            errors.append(f"{label}.evidence_state must be allowed")
        if not nonblank(relation.get("evidence_basis")):
            errors.append(f"{label}.evidence_basis must be non-empty")
        source_refs(relation.get("source_record_refs"), label, record, errors, mandatory=state != "unresolved")
        refs = relation.get("party_refs", [])
        if not isinstance(refs, list) or len(refs) != len({repr(v) for v in refs}) or any(not isinstance(v, str) or v not in party_ids for v in refs):
            errors.append(f"{label}.party_refs must uniquely reference affected_party_context.entities[].party_id")
        locations = relation.get("locations")
        if not isinstance(locations, list):
            errors.append(f"{label}.locations must be an array")
            continue
        if state in {"supported", "attributed", "disputed"} and not locations:
            errors.append(f"{label}.locations must identify evidenced jurisdictions for asserted relationships")
        if state == "unresolved" and locations:
            errors.append(f"{label}.locations must be empty for unresolved geographic claims; use an evidence-bounded asserted state if a location is identified")
        seen: set[str] = set()
        for j, location in enumerate(locations):
            place = f"{label}.locations[{j}]"
            if not isinstance(location, dict) or set(location) - {"country_code", "subdivision_code", "locality"}:
                errors.append(f"{place} must contain only country_code, subdivision_code and optional locality")
                continue
            country = location.get("country_code")
            if country not in COUNTRY_CODES:
                errors.append(f"{place}.country_code must be ISO 3166-1 alpha-2")
            subdivision = location.get("subdivision_code")
            if subdivision is not None and (not isinstance(subdivision, str) or not SUBDIVISION_CODE.fullmatch(subdivision) or not subdivision.startswith(str(country) + "-")):
                errors.append(f"{place}.subdivision_code must use ISO 3166-2 syntax and match country_code")
            if "locality" in location and not nonblank(location["locality"]):
                errors.append(f"{place}.locality must be non-empty when present")
            key = repr(sorted(location.items()))
            if key in seen:
                errors.append(f"{place} duplicates a jurisdiction in this relationship")
            seen.add(key)
    return errors
