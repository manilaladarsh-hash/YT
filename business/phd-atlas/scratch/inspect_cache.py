import glob, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sub = sys.argv[1] if len(sys.argv) > 1 else ""
mode = sys.argv[2] if len(sys.argv) > 2 else "list"
out = open(sys.argv[3], "w", encoding="utf-8") if len(sys.argv) > 3 else sys.stdout

for f in sorted(glob.glob(str(ROOT / ".cache" / "pages" / "*.json"))):
    d = json.load(open(f, encoding="utf-8"))
    url = d.get("url", "")
    if sub in url:
        text = d.get("text", "")
        if mode == "list":
            print(f, url, len(text), file=out)
        elif mode == "dump":
            print(f"=== {url} ({f}) len={len(text)} ===", file=out)
            print(text, file=out)
            print("\nLINKS:", file=out)
            for lbl, href in d.get("links", []):
                print(f"  {lbl!r} -> {href}", file=out)
