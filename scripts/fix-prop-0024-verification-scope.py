#!/usr/bin/env python3
import json
from pathlib import Path

path = Path("vigil/records/proposals/2026/VIGIL-2026-PROP-0024.json")
data = json.loads(path.read_text(encoding="utf-8"))

repair_scope = data.get("repair_scope")
if not isinstance(repair_scope, dict):
    raise SystemExit("PROP-0024 repair_scope is missing or not an object")

verification = repair_scope.get("verification_by_failure_mode")
expected = {
    "VIGIL-2026-FM-0044": "A future PATCH must demonstrate that the optimiser-level repair prevents a globally inadmissible pathway from being assembled through individually executable credential, privilege, and access transitions."
}

if verification == {}:
    print("PROP-0024 verification_by_failure_mode is already empty.")
    raise SystemExit(0)
if verification != expected:
    raise SystemExit(f"Unexpected PROP-0024 verification content: {verification!r}")

repair_scope["verification_by_failure_mode"] = {}
implementation_notes = data.setdefault("implementation_notes", {})
validator_changes = implementation_notes.setdefault("validator_changes", [])
statement = expected["VIGIL-2026-FM-0044"]
if statement not in validator_changes:
    validator_changes.append(statement)

path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("PROP-0024 proposal verification scope repaired without deleting the future PATCH verification requirement.")
