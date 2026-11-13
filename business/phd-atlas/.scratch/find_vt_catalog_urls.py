import urllib.request
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

req = urllib.request.Request("https://catalog.vt.edu/graduate/", headers={"User-Agent": "Mozilla/5.0"})
try:
    html = urllib.request.urlopen(req).read().decode("utf-8", errors="replace")
    for m in re.finditer(r'href=["\'](/graduate/[^"\']*)["\'][^>]*>([^<]+)<', html):
        print(f"{m.group(2).strip()} -> https://catalog.vt.edu{m.group(1)}")
except Exception as e:
    print("Error:", e)
