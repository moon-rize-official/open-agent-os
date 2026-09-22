#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=[json.loads(x) for x in (root/"generated/agent-resource-profiles.ndjson").read_text(encoding="utf-8").splitlines() if x.strip()]
assert len(rows)==1548
assert len({r["id"] for r in rows})==1548
missing=[]
for r in rows:
    for key in ("common_pack","department_pack","role_overlay"):
        if not (root/r[key]).exists(): missing.append(r[key])
if missing: raise SystemExit("Missing packs:\n"+"\n".join(sorted(set(missing))))
print("OK: 1548 unique profiles; all pack references resolve.")
