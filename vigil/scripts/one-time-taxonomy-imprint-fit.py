#!/usr/bin/env python3
"""Tighten publication-information spacing so the imprint remains on one page."""
from pathlib import Path

path = Path("vigil/taxonomy/render_taxonomy.py")
text = path.read_text(encoding="utf-8")
replacements = {
    'font-size:22pt;font-weight:700;margin:0 0 13mm': 'font-size:22pt;font-weight:700;margin:0 0 9mm',
    'grid-template-columns:42mm 1fr;gap:3mm 6mm': 'grid-template-columns:42mm 1fr;gap:2.1mm 6mm',
    'width:100%;margin:14mm 0 8mm': 'width:100%;margin:8mm 0 5mm',
    'margin-top:auto;padding-top:6mm;border-top:.6pt solid #d8d5cc': 'margin-top:auto;padding-top:4mm;border-top:.6pt solid #d8d5cc',
    'margin-top:5mm;font-size:9pt': 'margin-top:3.5mm;font-size:9pt',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f"imprint CSS token not found: {old}")
    text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")
print("Tightened taxonomy publication-information spacing")
