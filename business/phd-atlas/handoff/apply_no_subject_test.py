"""One-off Phase 1 helper (D1): mark gre_subject = 'No subject test' (cited verbatim to ETS)
for programs in fields where ETS offers no GRE Subject Test (all fields except physics, math, neuro),
only where gre_subject.code is currently 'Not stated'.

Usage: python3 handoff/apply_no_subject_test.py [--dir data] [--dir data/staging]
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HAS_SUBJECT_TEST = {"physics", "math", "neuro"}

ETS_ACTIVE_URL = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_ACTIVE_QUOTE = (
    "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement "
    "in a particular field of study"
)
ETS_DISC_URL = "https://www.ets.org/gre/test-takers/subject-tests/scores.html"
ETS_CHEM_QUOTE = "The GRE Chemistry Test was discontinued in May 2023."
ETS_BIO_QUOTE = "The GRE Biology Test and the GRE Literature in English Test were discontinued in May 2021."


def entry_for(field_id: str) -> dict:
    if field_id == "chemistry":
        return {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field: ETS discontinued the GRE Chemistry Test in May 2023.",
            "quote": ETS_CHEM_QUOTE,
            "url": ETS_DISC_URL,
        }
    if field_id == "biology":
        return {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field: ETS discontinued the GRE Biology Test in May 2021.",
            "quote": ETS_BIO_QUOTE,
            "url": ETS_DISC_URL,
        }
    return {
        "code": "No subject test",
        "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
        "quote": ETS_ACTIVE_QUOTE,
        "url": ETS_ACTIVE_URL,
    }


def apply_dir(rel_dir: str) -> int:
    prog_dir = ROOT / rel_dir / "programs"
    changed = 0
    for path in sorted(prog_dir.glob("*.json")):
        rec = json.loads(path.read_text(encoding="utf-8"))
        if rec["field"] in HAS_SUBJECT_TEST:
            continue
        gs = rec["fields"].get("gre_subject", {})
        if gs.get("code") != "Not stated":
            continue
        rec["fields"]["gre_subject"] = entry_for(rec["field"])
        path.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        changed += 1
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dirs", nargs="+", default=["data", "data/staging"])
    args = ap.parse_args()
    for d in args.dirs:
        n = apply_dir(d)
        print(f"{d}: updated {n} program records to 'No subject test'")


if __name__ == "__main__":
    main()
