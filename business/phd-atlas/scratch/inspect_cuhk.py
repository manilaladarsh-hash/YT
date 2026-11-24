import glob, json

out_lines = []
for path in sorted(glob.glob(".cache/pages/*.json")):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    url = d.get("url", "")
    if "cuhk.edu.hk" in url:
        out_lines.append("=" * 80)
        out_lines.append(f"URL: {url}")
        out_lines.append(f"CACHE: {path}")
        out_lines.append("-" * 80)
        out_lines.append(d.get("text", ""))
        out_lines.append("")

with open("scratch/cuhk_dump.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
print(f"Wrote {len(out_lines)} CUHK sections")
