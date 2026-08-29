#!/usr/bin/env python3
"""Update the taxonomy publication imprint to the current CAM publishing identity."""
from pathlib import Path

path = Path("vigil/taxonomy/render_taxonomy.py")
text = path.read_text(encoding="utf-8")
old = '''    <dt>Failure families</dt><dd>{len(families)}</dd>\n    <dt>Failure classes</dt><dd>{class_count}</dd>\n    <dt>Author and rights holder</dt><dd>Dr Michelle O'Rourke</dd>'''
new = '''    <dt>Failure families</dt><dd>{len(families)}</dd>\n    <dt>Failure classes</dt><dd>{class_count}</dd>\n    <dt>Publisher</dt><dd>CAM Initiative</dd>\n    <dt>Governance editor</dt><dd>Dr M.V. O'Rourke</dd>\n    <dt>Business entity</dt><dd>Phoenix Covenant Pty Ltd</dd>\n    <dt>ABN</dt><dd>14 692 195 529</dd>\n    <dt>Rights holder</dt><dd>Dr Michelle O'Rourke</dd>'''
if old not in text:
    raise SystemExit("publication metadata block not found or already changed")
text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")
print("Updated taxonomy publication identity metadata")
