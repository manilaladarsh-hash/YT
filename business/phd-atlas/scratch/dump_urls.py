import hashlib, json, pathlib, sys

urls = sys.argv[1:-1]
out_path = pathlib.Path(sys.argv[-1])
out = []
for u in urls:
    key = hashlib.sha1(u.encode()).hexdigest()[:16]
    p = pathlib.Path(".cache/pages") / f"{key}.json"
    if p.exists():
        d = json.loads(p.read_text(encoding="utf-8"))
        out.append(f"URL: {u} (final: {d.get('final_url','')}) [{p.name}]\n" + d.get("text", ""))
    else:
        out.append(f"MISSING: {u} [{p.name}]")
out_path.write_text("\n\n" + ("=" * 80 + "\n").join(out), encoding="utf-8")
print(f"Wrote {len(out)} pages to {out_path}")
