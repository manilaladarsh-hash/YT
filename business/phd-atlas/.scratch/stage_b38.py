import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
STAGING_PROGS = ROOT / "data" / "staging" / "programs"
STAGING_PROGS.mkdir(parents=True, exist_ok=True)

def load_prog(name):
    return json.loads((ROOT / "data" / "programs" / name).read_text(encoding="utf-8"))

def save_prog(name, data):
    (STAGING_PROGS / name).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

# 1. memphis--cs.json (gre_general: prepend GRE minimum scores sentence)
d = load_prog("memphis--cs.json")
d["fields"]["gre_general"]["quote"] = (
    "GRE Scores: The following minimum scores are required. Applicants who hold a "
    "Computer Science degree from the University of Memphis may request to have the "
    "GRE requirement waived by sending an email request to csgrad@memphis.edu. | "
    "143 on Verbal Reasoning | 153 on Quantitative Reasoning | 3.0 on Analytical Writing"
)
save_prog("memphis--cs.json", d)

# 2. memphis--neuro.json (supervisor: include mentor & faculty context sentence)
d = load_prog("memphis--neuro.json")
d["fields"]["supervisor"]["quote"] = (
    "To pick a mentor first look for someone with a similar interest by looking through "
    "the faculty profiles; then read their papers. Once you have found someone who looks "
    "compatible, call that person and discuss your interest in the Ph.D. program and "
    "working as a trainee in their lab."
)
save_prog("memphis--neuro.json", d)

# 3 & 4. miami--earth.json and miami--environment.json (entry_route: include Q10 question)
miami_quote = (
    "10. Can a student enter the Ph.D. degree program directly with just an undergraduate "
    "degree? | Yes. In all of the Ph.D. programs, direct entry for study leading to the "
    "Ph.D. is encouraged."
)
for fn in ("miami--earth.json", "miami--environment.json"):
    d = load_prog(fn)
    d["fields"]["entry_route"]["quote"] = miami_quote
    save_prog(fn, d)

# 5, 6, 7. miamiohio--biology.json, miamiohio--earth.json, miamiohio--environment.json
# gre_general was inferred from omission in application materials lists -> Not stated
for fn in ("miamiohio--biology.json", "miamiohio--earth.json", "miamiohio--environment.json"):
    d = load_prog(fn)
    d["fields"]["gre_general"]["code"] = "Not stated"
    d["fields"]["gre_general"]["value"] = "Not stated on the page checked"
    d["fields"]["gre_general"]["quote"] = ""
    save_prog(fn, d)

print("Staged 7 files for Batch 38")
