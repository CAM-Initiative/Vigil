#!/usr/bin/env python3
"""Source-field-derived jurisdiction geography; not an incident-location finding.

The normalized index is strictly a *projection* of canonical jurisdictional_context.
It never rewrites Incident evidence or asserts where harm occurred, an operator was
located, or which law applies. No NLP inference from titles/vendors/search terms.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
INCIDENTS = ROOT / "vigil" / "records" / "incidents"
OUTPUT = ROOT / "vigil" / "VIGIL.Incidents.Jurisdictions.Index.json"
VERSION = "1.0.0"

# Stable ISO 3166-1 alpha-2 identifiers. Synonyms are explicit and conservative;
# avoid geopolitical / local abbreviations that could create false positives.
NAMES = {
    "AU": ("australia", "australian"),
    "US": ("united states", "united states of america", "u.s.a.", "usa"),
    "GB": ("united kingdom", "great britain", "england", "scotland"),
    "CA": ("canada", "canadian"),
    "FR": ("france",),
    "DE": ("germany",),
    "IN": ("india",),
    "JP": ("japan",),
    "CN": ("china", "people's republic of china"),
    "KR": ("south korea", "republic of korea"),
    "NZ": ("new zealand",),
    "NL": ("netherlands",),
    "ES": ("spain",),
    "BR": ("brazil",),
    "IE": ("ireland",),
    "IT": ("italy",),
    "CH": ("switzerland",),
    "SG": ("singapore",),
    "IL": ("israel",),
    "RU": ("russia", "russian federation"),
    "KE": ("kenya",),
    "SE": ("sweden",),
    "PL": ("poland",),
    "ID": ("indonesia",),
    "AR": ("argentina",),
    "FI": ("finland",),
    "AE": ("united arab emirates", "uae"),
    "DK": ("denmark",),
    "BE": ("belgium",),
    "NO": ("norway",),
    "GR": ("greece",),
    "TR": ("türkiye", "turkey"),
    "SA": ("saudi arabia",),
    "MX": ("mexico",),
    "ZA": ("south africa",),
    "PH": ("philippines",),
    "TW": ("taiwan",),
    "UA": ("ukraine",),
    "RO": ("romania",),
    "CZ": ("czechia", "czech republic"),
    "AT": ("austria",),
    "PT": ("portugal",),
    "CL": ("chile",),
    "NG": ("nigeria",),
    "EG": ("egypt",),
    "MY": ("malaysia",),
    "VN": ("vietnam",),
    "EE": ("estonia",),
    "PK": ("pakistan",),
    "HK": ("hong kong",),
    "TH": ("thailand",),
    "BD": ("bangladesh",),
    "CO": ("colombia",),
}
# Subdivision matches require a same-country parent; ambiguous names such as
# Georgia are never accepted without an explicitly named country.
SUBDIVISIONS = {
    "AU": {
        "AU-NSW": ("new south wales", "nsw"),
        "AU-VIC": ("victoria",),
        "AU-WA": ("western australia",),
        "AU-QLD": ("queensland",),
        "AU-SA": ("south australia",),
        "AU-TAS": ("tasmania",),
        "AU-ACT": ("australian capital territory",),
        "AU-NT": ("northern territory",),
    },
    "US": {
        "US-CA": ("california",),
        "US-NY": ("new york",),
        "US-NJ": ("new jersey",),
        "US-NM": ("new mexico",),
        "US-OK": ("oklahoma",),
        "US-CT": ("connecticut",),
        "US-FL": ("florida",),
        "US-WA": ("washington",),
        "US-OR": ("oregon",),
        "US-MI": ("michigan",),
    },
    "CA": {"CA-BC": ("british columbia",)},
    "GB": {"GB-WLS": ("wales",)},  # Subdivision only after explicit GB country.
}
UNKNOWN = re.compile(r"^(not established|unknown|unspecified|jurisdiction not established|not specified)\b", re.I)
GLOBAL = re.compile(r"^(global|international|worldwide)\b", re.I)
CROSS = re.compile(r"^(cross.border|multi.jurisdictional)\b", re.I)
SIMULATION = re.compile(r"^(not applicable|controlled simulation|controlled training)\b", re.I)

def mentioned(text: str, names: tuple[str, ...]) -> bool:
    return any(re.search(r"(?<![a-z])" + re.escape(name.casefold()) + r"(?![a-z])", text.casefold()) is not None for name in names)

def country_codes(text: str) -> list[str]:
    return sorted(code for code, names in NAMES.items() if mentioned(text, names))

def subdivision_codes(text: str, parent_code: str) -> list[str]:
    return sorted(code for code, names in SUBDIVISIONS.get(parent_code, {}).items() if mentioned(text, names))

def project(record: dict[str, Any]) -> dict[str, Any]:
    details = record.get("jurisdictional_context")
    details = details if isinstance(details, dict) else {}
    primary = details.get("primary_jurisdiction")
    primary = primary.strip() if isinstance(primary, str) else ""
    secondary = details.get("secondary_jurisdictions")
    secondary = [item.strip() for item in secondary if isinstance(item, str) and item.strip()] if isinstance(secondary, list) else []
    primary_codes = country_codes(primary)
    secondary_codes = sorted({code for value in secondary for code in country_codes(value)})
    # Secondary jurisdictions must not silently replace an unknown primary.
    all_codes = sorted(set(primary_codes + secondary_codes))
    lower = primary.casefold()
    if not primary or UNKNOWN.match(primary):
        scope = "not-established"
    elif SIMULATION.match(primary):
        scope = "non-geographic"
    elif GLOBAL.match(primary):
        scope = "global"
    elif CROSS.match(primary):
        scope = "cross-border"
    elif len(primary_codes) > 1 or len(all_codes) > 1:
        scope = "multi-jurisdiction"
    elif len(primary_codes) == 1 and re.search(r"[/;]\s*(global|international|worldwide)\b", lower):
        scope = "mixed-global"
    elif len(primary_codes) == 1:
        scope = "single-country"
    else:
        scope = "unresolved"

    # Safe anchors are only for *jurisdiction association* (not event location).
    # If countries appear only in secondary descriptions, leave primary unmapped.
    mapped = scope == "single-country" and len(primary_codes) == 1 and len(all_codes) == 1
    subdivisions = set()
    if mapped:
        anchor_code = primary_codes[0]
        for line in [primary, *secondary]:
            subdivisions.update(subdivision_codes(line, anchor_code))
    else:
        anchor_code = None

    return {
        "incident_id": record["id"],
        "record_version": record.get("record_identity", {}).get("version"),
        "scope": scope,
        "primary_jurisdiction_text": primary,
        "secondary_jurisdictions_text": secondary,
        "country_codes_mentioned": all_codes,
        "anchor_country_code": anchor_code,
        "subdivision_codes_mentioned": sorted(subdivisions),
        "map_eligible": mapped,
        "anchor_semantics": "recorded-primary-jurisdiction-not-incident-location" if mapped else None,
        "source_fields": [
            "jurisdictional_context.primary_jurisdiction",
            "jurisdictional_context.secondary_jurisdictions",
        ],
        "evidence_review_status": "source-field-derived-not-independently-verified",
        "requires_review": not mapped,
    }

def build_projection(records: list[dict[str, Any]]) -> dict[str, Any]:
    entries = [project(record) for record in sorted(records, key=lambda r: r["id"])]
    counts: dict[str, int] = {}
    for item in entries:
        counts[item["scope"]] = counts.get(item["scope"], 0) + 1
    return {
        "registry_type": "incident_jurisdiction_projection",
        "schema_version": VERSION,
        "generated_from": "vigil/records/incidents/",
        "generated_notice": (
            "Deterministic source-field projection from canonical VIGIL Incidents. "
            "Country references describe recorded jurisdictional context; they are not "
            "incident coordinates, legal-applicability findings or verified event locations."
        ),
        "authorship_provenance": {
            "content_origin": "deterministically-generated",
            "generation_mode": "deterministic-generation",
            "human_authorship": False,
            "human_review_status": "not-reviewed",
            "human_verification_status": "not-verified",
            "upstream_provenance": ["vigil/records/incidents/"],
        },
        "record_count": len(entries),
        "scope_counts": dict(sorted(counts.items())),
        "map_eligible_count": sum(bool(e["map_eligible"]) for e in entries),
        "records": entries,
    }

def main() -> int:
    records = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(INCIDENTS.glob("VIGIL-INC-*.json"))]
    result = build_projection(records)
    out = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if "--check" in sys.argv:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != out:
            print("Jurisdiction projection is stale. Rebuild it before review.", file=sys.stderr)
            return 1
        print(f"Validated {result['record_count']} jurisdiction projections.")
        return 0
    OUTPUT.write_text(out, encoding="utf-8")
    print(f"Wrote {result['record_count']} jurisdiction projections; "
          f"{result['map_eligible_count']} single-country associations; "
          f"{result['scope_counts']}.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
