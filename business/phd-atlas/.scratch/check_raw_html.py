import urllib.request
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

req = urllib.request.Request("https://catalog.utk.edu/content.php?catoid=57&navoid=12418", headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode("utf-8", errors="replace")

idx = html.find("Computer Science Major, PhD")
if idx != -1:
    print(html[idx-200:idx+200])
else:
    print("Not found in raw HTML! Might be rendered via JS.")
