#!/usr/bin/env python3
import base64
import re
import subprocess
import zlib

VALIDATED_APPLICATOR_COMMIT = "1679884fb14e1bd643e7ce01abc9d56c65733652"
PATH = "scripts/build_vigil_patch_0031.py"

wrapper = subprocess.check_output(
    ["git", "show", f"{VALIDATED_APPLICATOR_COMMIT}:{PATH}"],
    text=True,
)
match = re.search(r'^payload = "([A-Za-z0-9+/=]+)"$', wrapper, re.MULTILINE)
if not match:
    raise SystemExit("Unable to recover validated PATCH-0031 applicator payload")

source = zlib.decompress(base64.b64decode(match.group(1))).decode("utf-8")
proposal_verification_block = '''    proposal["repair_scope"]["verification_by_failure_mode"] = {
        FM_ID: {
            "status": "implemented-branch-only",
            "patch_id": PATCH_ID,
            "verification": "corpus-verified",
            "canonical_adoption": "pending",
        }
    }
'''
if proposal_verification_block not in source:
    raise SystemExit("Expected proposal-verification block not found in validated applicator")
source = source.replace(proposal_verification_block, "")

relied_upon_block = '''            "instruments_relied_upon_without_amendment": [
                "CAM-EQ2026-OPERATIONS-003-SUP-01",
                "CAM-EQ2026-ARBITRATION-001-PLATINUM",
                "CAM-EQ2026-MENTIS-001-PLATINUM",
            ],
'''
if relied_upon_block not in source:
    raise SystemExit("Expected relied-upon provenance block not found in validated applicator")
source = source.replace(
    relied_upon_block,
    '''            "instruments_relied_upon_without_amendment": [],
''',
)

exec(compile(source, PATH, "exec"))
