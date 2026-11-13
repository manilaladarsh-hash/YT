import glob
import json
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

cache = {}
for f in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(f, encoding="utf-8"))
        cache[d.get("url")] = d.get("text", "")
    except Exception:
        pass

def normalize(text):
    return re.sub(r"\s+", " ", text).strip().lower()

normalized_cache = {url: normalize(text) for url, text in cache.items()}

def verify_quote(url, quote, name=""):
    norm_quote = normalize(quote)
    if url in normalized_cache:
        if norm_quote in normalized_cache[url]:
            print(f"[OK] {name}: found in {url}")
            return True
        else:
            print(f"[FAIL] {name}: quote NOT found in {url}")
            print(f"       Quote: {quote[:80]}...")
            return False
    else:
        print(f"[FAIL] {name}: URL not in cache: {url}")
        return False

# University
verify_quote(
    "https://catalog.utk.edu/content.php?catoid=57&navoid=12403",
    "A non-refundable Graduate Admissions Application Fee must be submitted with each first-time admissions application before an individual will be permitted to become a University of Tennessee graduate student or attend classes and before an individual student account will be established.",
    "utk fee_waiver"
)
