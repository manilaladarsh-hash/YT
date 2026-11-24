import json, sys
from pathlib import Path

domain = sys.argv[1]
out_path = Path(sys.argv[2])
chunks = []
for p in sorted(Path(".cache/pages").glob("*.json")):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if domain in u:
        txt = d.get("text", "")
        chunks.append(f"=== {u} (status={d.get('status')}, chars={len(txt)}, file={p.name}) ===\n{txt}\n")

out_path.write_text("\n".join(chunks), encoding="utf-8")
print(f"Wrote {len(chunks)} cached pages for '{domain}' to {out_path} ({out_path.stat().st_size} bytes)")
