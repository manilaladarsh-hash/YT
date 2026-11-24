import json
from pathlib import Path

CACHE = Path(".cache/pages")
out = []
for p in sorted(CACHE.glob("*.json")):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if "hkust" not in u:
        continue
    out.append("=" * 80)
    out.append(f"URL: {u} | FINAL: {d.get('final_url', '')} | STATUS: {d.get('status')} | METHOD: {d.get('method')} | LEN: {len(d.get('text', ''))}")
    out.append(d.get("text", ""))
    links = d.get("links", [])
    if links:
        out.append("--- FILTERED LINKS ---")
        seen = set()
        for item in links:
            txt, href = item if isinstance(item, (list, tuple)) else ("", item)
            k = (txt.strip(), href.strip())
            if k in seen:
                continue
            seen.add(k)
            s = f"{txt} {href}".lower()
            if any(w in s for w in ("admis", "phd", "rpg", "pg", "requir", "dead", "fund", "fellow", "scholar", "waiv", "toefl", "ielts", "gre", "superv", "advis", "program", "apply", "cour", "ocean", "env", "math", "phys", "chem", "bio", "life", "nano", "civl", "evng", "cse", "ece", "mae", "ieda", "cbme", "bien")):
                out.append(f"  {txt[:70]} -> {href}")
Path("scratch/_hkust_dump.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote", len(out), "entries to scratch/_hkust_dump.txt")
