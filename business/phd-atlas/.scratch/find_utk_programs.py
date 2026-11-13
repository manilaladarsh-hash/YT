import urllib.request
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Let's inspect the majors/programs page for catoid=57
# earlier we saw:
# Academic Policies -> navoid=12403
# Index for Academic Policies -> navoid=12393

# Let's check majors / programs link in catoid=57
url = "https://catalog.utk.edu/content.php?catoid=57&navoid=12403"
req = urllib.request.Request("https://catalog.utk.edu/index.php?catoid=57", headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode("utf-8", errors="replace")

for m in re.finditer(r'href=["\']([^"\']*)["\'][^>]*>([^<]+)<', html):
    link = m.group(1)
    text = m.group(2).strip()
    if "majors" in text.lower() or "programs" in text.lower() or "degrees" in text.lower() or "college" in text.lower():
        print(f"{text} -> {link}")
