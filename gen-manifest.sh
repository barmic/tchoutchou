#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

python3 - <<'PY' > manifest.json
import json, os
out = {}
for d in sorted(os.listdir(".")):
    if not os.path.isdir(d) or d.startswith("."):
        continue
    pngs = sorted(f for f in os.listdir(d) if f.lower().endswith(".png"))
    if pngs:
        out[d] = pngs
print(json.dumps(out, indent=2, ensure_ascii=False))
PY

python3 - <<'PY'
import json
m = json.load(open("manifest.json"))
total = sum(len(v) for v in m.values())
print(f"manifest.json écrit : {len(m)} couleur(s), {total} train(s)")
for k, v in m.items():
    print(f"  {k}: {len(v)}")
PY

python3 - <<'PY'
import hashlib, pathlib
h = hashlib.sha256()
for p in ("manifest.json", "index.html", "sw.template.js"):
    h.update(pathlib.Path(p).read_bytes())
version = h.hexdigest()[:12]
tpl = pathlib.Path("sw.template.js").read_text()
pathlib.Path("sw.js").write_text(tpl.replace("__CACHE_VERSION__", version))
print(f"sw.js écrit : version {version}")
PY
