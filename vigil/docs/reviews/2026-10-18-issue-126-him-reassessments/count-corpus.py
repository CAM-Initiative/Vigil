#!/usr/bin/env python3
"""Read-only corpus count from an explicit Git ref; no frozen acceptance counts."""
import collections
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True)


def count(ref):
    commit = git('rev-parse', ref).strip()
    paths = git('ls-tree', '-r', '--name-only', commit,
                '--', 'vigil/records/incidents/').splitlines()
    records = [json.loads(git('show', f'{commit}:{path}'))
               for path in paths if path.endswith('.json')]
    records = [r for r in records if r.get('record_type') == 'incident']
    def distribution(rows):
        return {
            'records': len(rows),
            'workflow_states': dict(sorted(collections.Counter(
                r['record_state'] for r in rows).items())),
            'methodology_versions': dict(sorted(collections.Counter(
                r['harm_impact_assessment']['methodology_version'] for r in rows).items())),
            'overall_severity': dict(sorted(collections.Counter(
                r['harm_impact_assessment']['overall_severity'] for r in rows).items())),
        }
    return {'commit': commit,
            'method': 'Every canonical Incident JSON under vigil/records/incidents at the explicit Git commit; not the generated index. active_only requires record_state exactly active.',
            'current_canonical': distribution(records),
            'active_only': distribution([r for r in records if r['record_state'] == 'active'])}


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: count-corpus.py <git-ref-or-commit>')
    print(json.dumps(count(sys.argv[1]), indent=2))
