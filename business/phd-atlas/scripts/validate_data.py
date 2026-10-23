"""Check every university and program record (schema 2.0) against the schema and, when the page cache
is present, confirm each quote really appears on its cited source page.

Usage:
  python3 scripts/validate_data.py            # schema checks; quote checks if cache exists
  python3 scripts/validate_data.py --require-cache   # fail if a quote cannot be checked
  python3 scripts/validate_data.py --dir data/staging   # check drafts (data/staging/universities, /programs)
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
DATA = ROOT / "data"
FIELDS = json.loads((DATA / "fields.json").read_text())
UNI_LIST = json.loads((DATA / "universities.json").read_text())
CACHE = ROOT / ".cache" / "pages"

FEE_RE = re.compile(r"^(\d+(\.\d+)? (USD|CAD|GBP|EUR|CHF|SEK|DKK|NOK|AUD|NZD)|0 \(waived\)|0 \(no fee\)|Not stated)$")
TOEFL_RE = re.compile(r"^(\d{2,3}|\d(\.\d)? \(new scale\)|Sections|Not required|Not stated)$")
IELTS_RE = re.compile(r"^(\d(\.[05])?|Not required|Not stated)$")
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


def check_field(where, name, spec, fld, texts, require_cache, errors, warnings):
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
    if name == "ielts_min" and not IELTS_RE.match(code):
        errors.append(f"{where}.ielts_min: code '{code}' has wrong format")
    if "time_sensitive" in fld and not (isinstance(fld["time_sensitive"], str) and DATE_RE.match(fld["time_sensitive"])):
        errors.append(f"{where}.{name}: time_sensitive must be an ISO act-by date")
    if "inferred" in fld and fld["inferred"] != "year":
        errors.append(f"{where}.{name}: inferred must be 'year'")
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


def load_json(f, errors):
    try:
        return json.loads(f.read_text())
    except json.JSONDecodeError as e:
        errors.append(f"{f.name}: invalid JSON ({e})")
        return None


def validate(require_cache=False, base=DATA):
    """Check data/universities and data/programs under base (data/ or data/staging/)."""
    errors, warnings = [], []
    texts = cached_texts()
    base = Path(base)
    field_ids = {f["id"] for f in FIELDS["fields"]}
    listed = {u["id"] for u in UNI_LIST["universities"]}
    uni_files = sorted((base / "universities").glob("*.json"))
    prog_files = sorted((base / "programs").glob("*.json"))
    if not uni_files and not prog_files:
        errors.append(f"no records found under {base}")
    known_unis = {f.stem for f in (DATA / "universities").glob("*.json")} | {f.stem for f in uni_files}
    ufields, pfields = SCHEMA["university_fields"], SCHEMA["program_fields"]
    for f in uni_files:
        rec = load_json(f, errors)
        if rec is None:
            continue
        where = "universities/" + f.name
        for key in SCHEMA["university_top_level"]:
            if key not in rec:
                errors.append(f"{where}: missing '{key}'")
        if rec.get("id") != f.stem:
            errors.append(f"{where}: id '{rec.get('id')}' does not match file name")
        if rec.get("id") not in listed:
            warnings.append(f"{where}: not in data/universities.json")
        if rec.get("country") not in SCHEMA["countries"]:
            errors.append(f"{where}: unknown country {rec.get('country')}")
        try:
            date.fromisoformat(rec.get("checked", ""))
        except ValueError:
            errors.append(f"{where}: bad 'checked' date")
        fields = rec.get("fields", {})
        if set(ufields) - set(fields):
            errors.append(f"{where}: missing fields {sorted(set(ufields) - set(fields))}")
        if set(fields) - set(ufields):
            errors.append(f"{where}: unexpected fields {sorted(set(fields) - set(ufields))}")
        for name, spec in ufields.items():
            if fields.get(name):
                check_field(where, name, spec, fields[name], texts, require_cache, errors, warnings)
    for f in prog_files:
        rec = load_json(f, errors)
        if rec is None:
            continue
        where = "programs/" + f.name
        for key in SCHEMA["program_top_level"]:
            if key not in rec:
                errors.append(f"{where}: missing '{key}'")
        if rec.get("id") != f.stem or rec.get("id") != f"{rec.get('university')}--{rec.get('field')}":
            errors.append(f"{where}: id must be '<university>--<field>' and match the file name")
        if rec.get("university") not in known_unis:
            errors.append(f"{where}: university '{rec.get('university')}' has no university record")
        if rec.get("field") not in field_ids:
            errors.append(f"{where}: unknown field '{rec.get('field')}'")
        for extra in rec.get("also_fields", []):
            if extra not in field_ids or extra == rec.get("field"):
                errors.append(f"{where}: bad also_fields entry '{extra}'")
        try:
            date.fromisoformat(rec.get("checked", ""))
        except ValueError:
            errors.append(f"{where}: bad 'checked' date")
        fields = rec.get("fields", {})
        if set(pfields) - set(fields):
            errors.append(f"{where}: missing fields {sorted(set(pfields) - set(fields))}")
        allowed = set(pfields) | set(ufields)
        if set(fields) - allowed:
            errors.append(f"{where}: unexpected fields {sorted(set(fields) - allowed)}")
        for name, fld in fields.items():
            spec = pfields.get(name) or ufields.get(name)
            if spec:
                check_field(where, name, spec, fld, texts, require_cache, errors, warnings)
    return errors, warnings, len(uni_files), len(prog_files)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--require-cache", action="store_true")
    ap.add_argument("--dir", default=str(DATA), help="base folder holding universities/ and programs/ (e.g. data/staging)")
    args = ap.parse_args()
    folder = Path(args.dir)
    if not folder.is_absolute():
        folder = ROOT / folder
    errors, warnings, nu, npr = validate(args.require_cache, folder)
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{nu} universities, {npr} programs, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
