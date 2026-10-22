"""Tiny helper for writing program records in a compact form.

Each field is a tuple: (code, value, quote, url[, extra-dict]).
Records land in data/programs/<id>.json in the same shape validate_data.py checks.
Set ATLAS_OUT=data/staging to write drafts there instead, so a build running at
the same time never picks up an unreviewed record.
"""

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRAMS = ROOT / os.environ.get("ATLAS_OUT", "data/programs")


def save(pid, institution, department, country, region, page, fields, notes="", checked="2026-10-21"):
    out = {}
    for name, spec in fields.items():
        code, value, quote, url = spec[:4]
        entry = {"code": code, "value": value, "quote": quote, "url": url}
        if len(spec) > 4:
            entry.update(spec[4])
        out[name] = entry
    record = {
        "id": pid,
        "institution": institution,
        "department": department,
        "country": country,
        "region": region,
        "program_page": page,
        "checked": checked,
        "fields": out,
        "notes": notes,
    }
    PROGRAMS.mkdir(parents=True, exist_ok=True)
    path = PROGRAMS / f"{pid}.json"
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    return path
