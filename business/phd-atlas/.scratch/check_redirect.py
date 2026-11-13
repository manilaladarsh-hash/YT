import urllib.request
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

req = urllib.request.Request("http://tiny.utk.edu/grad-catalog", headers={"User-Agent": "Mozilla/5.0"})
try:
    resp = urllib.request.urlopen(req)
    print("Redirected to:", resp.geturl())
except Exception as e:
    print("Error:", e)
