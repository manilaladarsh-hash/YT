import glob, json, os

out_lines = []
for path in sorted(glob.glob(".cache/pages/*.json")):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    url = d.get("url", "")
    if "umdearborn.edu" in url or "umd.umich.edu" in url:
        out_lines.append("=" * 80)
        out_lines.append(f"URL: {url}")
        out_lines.append(f"CACHE: {path}")
        out_lines.append(f"STATUS: {d.get('status')} VIA: {d.get('via')}")
        out_lines.append("-" * 80)
        out_lines.append(d.get("text", ""))
        out_lines.append("")

with open("scratch/umd_edu_dump.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
print(f"Wrote {len(out_lines)} lines across matching cached files")
