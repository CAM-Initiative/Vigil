#!/usr/bin/env python3
"""One-shot normalization for source enums introduced by the 002-020 rebuild."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "records" / "incidents"
fixes = {
    6: {2: {"source_type": "legal filing or decision"}},
    7: {2: {"source_type": "governance record", "evidence_status": "allegation-on-record"}},
    8: {2: {"source_type": "legal filing or decision"}},
    13: {2: {"source_type": "official announcement"}},
}
for inc, source_fixes in fixes.items():
    p = ROOT / f"VIGIL-INC-{inc:06d}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    for idx, values in source_fixes.items():
        d["source_records"][idx].update(values)
    p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
