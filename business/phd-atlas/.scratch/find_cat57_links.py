import urllib.request
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

req = urllib.request.Request("https://catalog.utk.edu/index.php?catoid=57", headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode("utf-8", errors="replace")

for m in re.finditer(r'href=["\']([^"\']*)["\'][^>]*>([^<]+)<', html):
    link = m.group(1)
    text = m.group(2).strip()
    if any(k in text.lower() for k in ["policy", "admission", "degree", "requirement", "program"]):
        print(f"{text} -> https://catalog.utk.edu/{link}")
