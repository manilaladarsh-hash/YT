import json
from pathlib import Path

cache = Path(".cache/pages")
uh_pages = {}
for p in cache.glob("*.json"):
    try:
        rec = json.loads(p.read_text(encoding="utf-8"))
        url = rec.get("url", "")
        if "uh.edu" in url:
            uh_pages[url] = rec.get("text", "")
    except Exception as e:
        pass

print(f"Loaded {len(uh_pages)} UH pages.")
for url in sorted(uh_pages.keys()):
    text = uh_pages[url]
    print(f"=== URL: {url} (length: {len(text)}) ===")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    for line in lines[:25]:
        print("  ", line[:100])
