#!/usr/bin/env python3
import json
from pathlib import Path

path = Path("vigil/records/observations/2026/VIGIL-2026-OBS-0023.json")
data = json.loads(path.read_text(encoding="utf-8"))
context = data.get("system_context")
if not isinstance(context, dict):
    raise SystemExit("OBS-0023 system_context is missing or invalid")
if context.get("platform_or_vendor") != "Multi Vendor":
    raise SystemExit("OBS-0023 is no longer classified as Multi Vendor")

context["vendor_cluster"] = [
    "GitHub",
    "Hugging Face",
    "Meta",
    "Google",
    "Alibaba",
    "Other"
]
context["primary_evidenced_vendors"] = [
    "GitHub",
    "Hugging Face"
]

path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("OBS-0023 multi-vendor context repaired.")
