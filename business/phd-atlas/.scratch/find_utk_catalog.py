import urllib.request
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

req = urllib.request.Request("https://catalog.utk.edu/", headers={"User-Agent": "Mozilla/5.0"})
try:
    html = urllib.request.urlopen(req).read().decode("utf-8", errors="replace")
    for m in re.finditer(r'href=["\']([^"\']*)["\'][^>]*>([^<]*)<', html):
        link = m.group(1)
        text = m.group(2).strip()
        if "graduate" in text.lower() or "graduate" in link.lower():
            print(f"{text} -> {link}")
except Exception as e:
    print(f"Error: {e}")
