#!/usr/bin/env python3
"""Remove duplicated top-level chapter numbering from the publication contents page."""
from pathlib import Path

path = Path("vigil/taxonomy/render_taxonomy.py")
text = path.read_text(encoding="utf-8")
old = 'contents.append(f"<li><a href=\\"#{esc(anchor(family[\'family_id\']))}\\"><strong>{chapter_number}. {esc(family[\'name\'])}</strong></a><ul>")'
new = 'contents.append(f"<li><a href=\\"#{esc(anchor(family[\'family_id\']))}\\"><strong>{esc(family[\'name\'])}</strong></a><ul>")'
if old not in text:
    raise SystemExit("top-level contents numbering line not found")
text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")
print("Removed duplicate manual chapter number from Contents")
