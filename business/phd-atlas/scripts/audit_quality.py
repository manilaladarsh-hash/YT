"""Find records that pass validation but may still be wrong. The validator proves a quote
is on the page; this checks whether the quote supports the code and the program is real.

Usage: python3 scripts/audit_quality.py [--dir data] [--csv out.csv]
Checks:
  generic_page   5+ programs at one university share one program_page (program existence unproven)
  off_topic      the quote has no word related to its field (e.g. a funding code quoting a GRE sentence)
  absence        a 'Not required' / 'No fee' code whose quote never mentions the thing (inferred from silence)
  odd_cache      the cited page was cached by something other than scripts/research.py
Exit code is 0; the counts and the CSV are for review.
"""

import argparse
import collections
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KW = {
    "funding": r"fund|stipend|scholar|studentship|support|salar|employ|assistantship|fellowship|paid|tuition|contract|position|financ|award|bursar",
    "deadline": r"deadline|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|\d{1,2}/\d|rolling|any time|year-round|throughout|open|round|apply by|position|vacanc|call",
    "supervisor": r"supervis|advis|faculty|professor|rotation|committee|contact|mentor|lab|research group|principal investigator",
    "entry_route": r"degree|bachelor|master|honours|baccalaur|undergraduate|b\.s|m\.s|diploma",
    "toefl_min": r"toefl|english|language|ibt|\b\d{2,3}\b", "ielts_min": r"ielts|english|language|band|\b\d\.\d\b",
    "app_fee": r"fee|\$|£|€|usd|cad|chf|eur|charge|cost|free", "fee_waiver": r"waiv|fee",
    "gre_general": r"gre|graduate record", "gre_subject": r"gre|subject|graduate record",
    "english_waiver": r"english|language|toefl|ielts|exempt|waiv",
}
ABSENCE = {"gre_general": ("Not required", r"gre|graduate record"), "gre_subject": ("Not required", r"gre|subject"),
           "fee_waiver": ("No fee", r"fee"), "app_fee": ("0 (no fee)", r"fee")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="data")
    ap.add_argument("--csv")
    a = ap.parse_args()
    base = ROOT / a.dir
    odd = set()
    for p in (ROOT / ".cache" / "pages").glob("*.json"):
        r = json.loads(p.read_text(encoding="utf-8"))
        if "via" in r or "method" not in r:
            odd.update({r["url"], r.get("final_url", r["url"])})
    recs = [(p.name, json.loads(p.read_text(encoding="utf-8"))) for d in ("universities", "programs") for p in (base / d).glob("*.json")]
    pages = collections.Counter((r["university"], r["program_page"]) for _, r in recs if "program_page" in r)
    out = []
    for name, r in recs:
        if "program_page" in r and pages[(r["university"], r["program_page"])] >= 5:
            out.append(("generic_page", name, "program_page", "", r["program_page"], r.get("department", "")))
        for k, v in r["fields"].items():
            q = v.get("quote", "")
            if not q or v["code"] in ("Not stated", "No subject test"):
                continue
            if k in KW and not re.search(KW[k], q, re.I):
                out.append(("off_topic", name, k, v["code"], v["url"], q[:160]))
            if k in ABSENCE and v["code"] == ABSENCE[k][0] and not re.search(ABSENCE[k][1], q, re.I):
                out.append(("absence", name, k, v["code"], v["url"], q[:160]))
            if v["url"] in odd:
                out.append(("odd_cache", name, k, v["code"], v["url"], ""))
    c = collections.Counter(o[0] for o in out)
    print(f"{len(recs)} records checked")
    for k in ("generic_page", "off_topic", "absence", "odd_cache"):
        print(f"{k:<14}{c[k]:>6}")
    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["check", "file", "field", "code", "url", "detail"])
            w.writerows(out)


if __name__ == "__main__":
    main()
