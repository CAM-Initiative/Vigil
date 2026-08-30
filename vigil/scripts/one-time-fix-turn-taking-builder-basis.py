#!/usr/bin/env python3
"""Make the FC-000056 mapping basis explicitly Incident-scoped for validator compatibility."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILDER = ROOT / "vigil" / "scripts" / "build-incident-registry.py"
OLD = '                "Three synthetic ChatGPT voice participants reportedly responded independently with identical or "\n'
NEW = '                "In this Incident, three synthetic ChatGPT voice participants reportedly responded independently with identical or "\n'


def main() -> None:
    text = BUILDER.read_text(encoding="utf-8")
    if OLD in text:
        text = text.replace(OLD, NEW, 1)
    elif NEW not in text:
        raise SystemExit("Could not locate FC-000056 classification basis in patched builder")
    BUILDER.write_text(text, encoding="utf-8")
    print("Made INC-000078 classification basis explicitly Incident-specific.")


if __name__ == "__main__":
    main()
