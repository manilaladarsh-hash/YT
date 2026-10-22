"""Tiny helpers for writing Atlas records in a compact form (schema 2.0).

Each field is a tuple: (code, value, quote, url[, extra-dict]).

save_university() writes data/universities/<uid>.json: rules the graduate school
sets once for every department (fee, fee waiver, GRE General, TOEFL, IELTS,
English-test waiver).
save_program() writes data/programs/<uid>--<field>.json: one PhD program
(deadline, subject GRE, supervisor, funding, entry route), plus any university
field the department states differently.

Set ATLAS_OUT=data/staging to write drafts there instead, so a build running at
the same time never picks up an unreviewed record.
"""

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / os.environ.get("ATLAS_OUT", "data")
UNIVERSITIES = OUT / "universities"
PROGRAMS = OUT / "programs"


def _fields(fields):
    out = {}
    for name, spec in fields.items():
        code, value, quote, url = spec[:4]
        entry = {"code": code, "value": value, "quote": quote, "url": url}
        if len(spec) > 4:
            entry.update(spec[4])
        out[name] = entry
    return out


def _write(folder, rid, record):
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{rid}.json"
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    return path


def save_university(uid, institution, country, region, grad_page, fields, notes="", checked="2026-10-22"):
    record = {
        "id": uid,
        "institution": institution,
        "country": country,
        "region": region,
        "grad_page": grad_page,
        "checked": checked,
        "fields": _fields(fields),
        "notes": notes,
    }
    return _write(UNIVERSITIES, uid, record)


def save_program(uid, field, department, page, fields, notes="", also_fields=(), checked="2026-10-22", name=""):
    """field is an id from data/fields.json; also_fields lists more ids an umbrella program covers.
    name is an optional program name when it differs from the department (e.g. 'IMPRS Quantum Dynamics')."""
    record = {
        "id": f"{uid}--{field}",
        "university": uid,
        "field": field,
        "also_fields": list(also_fields),
        "department": department,
        "program_page": page,
        "checked": checked,
        "fields": _fields(fields),
        "notes": notes,
    }
    if name:
        record["name"] = name
    return _write(PROGRAMS, record["id"], record)
