"""Print the research task for one or more universities, ready to follow or paste into an agent.

Usage: python3 handoff/research_prompt.py UID [UID ...]
"""

import json
import sys
from pathlib import Path

R = Path(__file__).resolve().parent.parent
U = {u["id"]: u for u in json.loads((R / "data/universities.json").read_text())["universities"]}

for uid in sys.argv[1:]:
    u = U[uid]
    kind = "school" if u["kind"] != "university" else "university"
    has_uni = (R / f"data/universities/{uid}.json").exists()
    progs = sorted(p.name for p in (R / "data/programs").glob(f"{uid}--*.json"))
    staged = sorted(p.name for d in ("universities", "programs") for p in (R / "data/staging" / d).glob("*.json")
                    if p.name.split("--")[0].removesuffix(".json") == uid)
    s = [f"Research one {kind} for the STEM PhD Atlas 2027: uid `{uid}` ({u['name']}, {u['region']}, {u['country']}).", "",
         f"Work in {R}. First read data/staging/RESEARCH_BRIEF.md and follow it exactly: codes, saving example, quote rules, validation step, final-reply format."]
    if has_uni or progs:
        s.append(f"Live records: {'data/universities/' + uid + '.json' if has_uni else 'no university record'}; programs: {', '.join(progs) or 'none'}. "
                 "Copy them into data/staging and fill only their Not stated values (brief step 3). Keep every verified value as it is.")
    else:
        s.append(f"No records yet: create the university record with save_university(\"{uid}\", \"{u['name']}\", \"{u['country']}\", \"{u['region']}\", ...).")
    if staged:
        s.append("Already staged (keep and continue from them): " + ", ".join(staged) + ".")
    s += ["Save with ATLAS_OUT=data/staging. Write nothing outside data/staging except the fetch cache .cache/pages, which scripts/research.py writes.", "",
          "Every value needs a verbatim quote from an official page fetched with scripts/research.py. If no official page says it, use Not stated; never fill a value "
          "from memory. A department value must not contradict the university record unless the department page states its own rule. Use the university's official "
          "list of doctoral programs (one fetch) to decide which fields exist, and research every field that does. Finish with "
          "`python3 scripts/validate_data.py --dir data/staging --require-cache`, fix every error in this university's files, then reply in the brief's final-reply format."]
    print(f"===== {uid}\n" + "\n".join(s))
