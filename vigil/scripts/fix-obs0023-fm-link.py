#!/usr/bin/env python3
import json
from pathlib import Path

path = Path('vigil/records/observations/2026/VIGIL-2026-OBS-0023.json')
data = json.loads(path.read_text(encoding='utf-8'))
linked = data['linked_records']['related_failure_modes']
if linked == ['VIGIL-2026-FM-0051']:
    print('OBS-0023 link already correct.')
    raise SystemExit(0)
if linked != ['VIGIL-2026-FM-0049']:
    raise SystemExit(f'Unexpected OBS-0023 failure links: {linked!r}')
data['linked_records']['related_failure_modes'] = ['VIGIL-2026-FM-0051']
path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('Corrected OBS-0023 reciprocal failure link to FM-0051.')
