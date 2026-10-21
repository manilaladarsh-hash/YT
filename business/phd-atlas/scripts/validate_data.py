"""Check every program record against the schema and, when the page cache
is present, confirm each quote really appears on its cited source page.

Usage:
  python3 scripts/validate_data.py            # schema checks; quote checks if cache exists
  python3 scripts/validate_data.py --require-cache   # fail if a quote cannot be checked
Exit code is non-zero when any error is found.
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "data" / "schema.json").read_text())
PROGRAMS = ROOT / "data" / "programs"
CACHE = ROOT / ".cache" / "pages"

FEE_RE = re.compile(r"^(\d+(\.\d+)? (USD|CAD|GBP|EUR|CHF|SEK|DKK|NOK)|0 \(waived\)|0 \(no fee\)|Not stated)$")
TOEFL_RE = re.compile(r"^(\d{2,3}|\d(\.\d)? \(new scale\)|Sections|Not stated)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip().lower()


def cached_texts():
    """Map every cached URL and final URL to its normalised page text."""
    texts = {}
    if not CACHE.exists():
        return texts
    for p in CACHE.glob("*.json"):
        rec = json.loads(p.read_text())
        t = norm(rec.get("text", "").replace("\n", " "))
        texts[rec["url"]] = t
        texts[rec.get("final_url", rec["url"])] = t
    return texts


def quote_parts(quote):
    # Multi-part quotes are joined with ' | '; '...' marks an elision.
    parts = []
    for piece in quote.split(" | "):
        for sub in piece.split("..."):
            sub = sub.strip(" .,;:")
            if len(sub) >= 12:
                parts.append(sub)
    return parts


def validate(require_cache=False):
    errors, warnings = [], []
    texts = cached_texts()
    ids = set()
    files = sorted(PROGRAMS.glob("*.json"))
    if not files:
        errors.append("no program records found")
    for f in files:
        rec = json.loads(f.read_text())
        where = f.name
        for key in SCHEMA["required_top_level"]:
            if key not in rec:
                errors.append(f"{where}: missing '{key}'")
        if rec.get("id") != f.stem:
            errors.append(f"{where}: id '{rec.get('id')}' does not match file name")
        if rec.get("id") in ids:
            errors.append(f"{where}: duplicate id")
        ids.add(rec.get("id"))
        if rec.get("country") not in SCHEMA["countries"]:
            errors.append(f"{where}: unknown country {rec.get('country')}")
        try:
            date.fromisoformat(rec.get("checked", ""))
        except ValueError:
            errors.append(f"{where}: bad 'checked' date")
        fields = rec.get("fields", {})
        missing = set(SCHEMA["fields"]) - set(fields)
        extra = set(fields) - set(SCHEMA["fields"])
        if missing:
            errors.append(f"{where}: missing fields {sorted(missing)}")
        if extra:
            errors.append(f"{where}: unexpected fields {sorted(extra)}")
        for name, spec in SCHEMA["fields"].items():
            fld = fields.get(name)
            if not fld:
                continue
            code = fld.get("code", "")
            for k in ("code", "value", "quote", "url"):
                if k not in fld:
                    errors.append(f"{where}.{name}: missing '{k}'")
            if "enum" in spec and code not in spec["enum"]:
                errors.append(f"{where}.{name}: code '{code}' not in {spec['enum']}")
            if name == "deadline" and code not in ("Not stated", "Rolling", "Per position"):
                if not DATE_RE.match(code):
                    errors.append(f"{where}.deadline: code '{code}' is not ISO")
                else:
                    d = date.fromisoformat(code)
                    if not (date(2026, 10, 1) <= d <= date(2027, 6, 30)):
                        errors.append(f"{where}.deadline: {code} outside the Fall 2027 cycle")
            if name == "app_fee" and not FEE_RE.match(code):
                errors.append(f"{where}.app_fee: code '{code}' has wrong format")
            if name == "toefl_min" and not TOEFL_RE.match(code):
                errors.append(f"{where}.toefl_min: code '{code}' has wrong format")
            url = fld.get("url", "")
            if not url.startswith("https://"):
                errors.append(f"{where}.{name}: url must be https")
            quote = fld.get("quote", "")
            known = code not in SCHEMA["unknown_codes"]
            if known and not quote:
                errors.append(f"{where}.{name}: code '{code}' has no supporting quote")
            # A field may cite extra pages under "also": [{"quote", "url"}].
            sources = [(quote, url)] + [(a.get("quote", ""), a.get("url", "")) for a in fld.get("also", [])]
            for q, u in sources:
                if not q:
                    continue
                if not u.startswith("https://"):
                    errors.append(f"{where}.{name}: secondary url must be https")
                page = texts.get(u)
                if page is None:
                    msg = f"{where}.{name}: source page not in cache, quote unchecked ({u})"
                    (errors if require_cache else warnings).append(msg)
                    continue
                for part in quote_parts(q):
                    if norm(part) not in page:
                        errors.append(f"{where}.{name}: quote not found on source page: '{part[:80]}'")
    return errors, warnings, len(files)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--require-cache", action="store_true")
    args = ap.parse_args()
    errors, warnings, n = validate(args.require_cache)
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{n} records, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
