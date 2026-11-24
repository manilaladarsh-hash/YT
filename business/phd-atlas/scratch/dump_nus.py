import json
from pathlib import Path

out = []
for p in sorted(Path(".cache/pages").glob("*.json")):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    txt = d.get("text", "")
    if "nus.edu.sg" in u and len(txt) > 500:
        out.append("====================================")
        out.append(f"{u} ({len(txt)} chars, method={d.get('method')})")
        seen = set()
        for ln in txt.splitlines():
            s = ln.strip()
            if not s or s in seen:
                continue
            low = s.lower()
            if len(s) > 45 or any(w in low for w in [
                "fee", "toefl", "ielts", "gre", "deadlin", "nov", "dec", "jan", "may", "jun",
                "supervis", "advis", "stipend", "scholar", "waiv", "english", "bachelor", "master",
                "honour", "require", "phd", "doctor", "s$", "sgd", "0677", "908", "astro", "biomed",
                "neuro", "environ", "mater", "mech", "chem", "civil", "elect", "stat", "data",
            ]):
                seen.add(s)
                out.append(s)
Path("scratch/nus_dump.txt").write_text("\n".join(out), encoding="utf-8")
print("wrote", len(out), "lines")
