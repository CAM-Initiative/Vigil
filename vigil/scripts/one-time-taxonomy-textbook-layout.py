#!/usr/bin/env python3
from pathlib import Path

path = Path("vigil/taxonomy/render_taxonomy.py")
text = path.read_text(encoding="utf-8")

old = '''    system_context = record.get("system_context") if isinstance(record.get("system_context"), dict) else {}
    identity = record.get("record_identity") if isinstance(record.get("record_identity"), dict) else {}
    provider = str(system_context.get("platform_or_vendor") or "").strip()
'''
new = '''    system_context = record.get("system_context") if isinstance(record.get("system_context"), dict) else {}
    source_records = record.get("source_records")
    if not isinstance(source_records, list):
        source_records = []
    provider = str(system_context.get("platform_or_vendor") or "").strip()
'''
if text.count(old) != 1:
    raise SystemExit(f"Refusing source-record patch: expected one anchor, found {text.count(old)}")
text = text.replace(old, new, 1)

old = '''    recorded = record.get("date_recorded") or identity.get("created")
    return {"provider": provider, "product": product, "date": publication_date(recorded)}
'''
new = '''    evidence_source = next(
        (
            source
            for source in source_records
            if isinstance(source, dict)
            and source.get("source_date")
            and "evidence" in str(source.get("source_role", "")).lower()
        ),
        None,
    )
    if evidence_source is None:
        evidence_source = next(
            (
                source
                for source in source_records
                if isinstance(source, dict) and source.get("source_date")
            ),
            None,
        )
    source_date = evidence_source.get("source_date") if evidence_source else None
    return {"provider": provider, "product": product, "date": publication_date(source_date)}
'''
if text.count(old) != 1:
    raise SystemExit(f"Refusing date patch: expected one anchor, found {text.count(old)}")
text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
