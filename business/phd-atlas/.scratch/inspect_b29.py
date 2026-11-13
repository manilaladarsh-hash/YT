import hashlib, json, re
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")

def load_cache(url):
    h = hashlib.sha256(url.encode()).hexdigest()[:16]
    p = ROOT / ".cache" / "pages" / f"{h}.json"
    if not p.exists():
        for cp in (ROOT / ".cache" / "pages").glob("*.json"):
            d = json.loads(cp.read_text(encoding="utf-8"))
            if d.get("url") == url or d.get("final_url") == url:
                return cp, d
        return None, None
    return p, json.loads(p.read_text(encoding="utf-8"))

fit_url = "https://www.fit.edu/admissions/applying/graduate/"
_, fit_c = load_cache(fit_url)
ft = fit_c["text"]
for k in ["Environmental Science", "Applied Mathematics", "Mechanical Engineering", "Physics"]:
    for m in re.finditer(k, ft):
        print("FIT:", k, repr(ft[m.start():m.start()+140]))

for fn, field in [
    ("floridatech--physics.json", "gre_general"),
    ("floridatech--environment.json", "gre_general"),
    ("floridatech--math.json", "gre_general"),
    ("floridatech--mech.json", "gre_general"),
    ("fordham--biology.json", "gre_subject"),
    ("fsu--biology.json", "supervisor"),
]:
    j = json.loads((ROOT / "data" / "programs" / fn).read_text(encoding="utf-8"))
    print(f"\n=== {fn} [{field}] ===")
    print(json.dumps(j["fields"][field], indent=2, ensure_ascii=False))
    u = j["fields"][field].get("url")
    if u and u != fit_url:
        cp, cd = load_cache(u)
        print("CACHE:", cp, cd["status"] if cd else None, cd.get("final_url") if cd else None)
        if cd and cd.get("text"):
            t = cd["text"]
            q = j["fields"][field]["quote"]
            idx = t.lower().find(q.lower()[:40]) if q else -1
            if idx != -1:
                print("AROUND QUOTE:", repr(t[max(0, idx-300):idx+500]))
            else:
                print("QUOTE NOT EXACT MATCH; TEXT SAMPLE:", repr(t[:1200]))
            if "fsu" in fn:
                for kw in ["faculty", "advisor", "supervisor", "major professor", "sponsor", "committee", "rotat", "area"]:
                    hits = [m.start() for m in re.finditer(kw, t, re.I)]
                    print(f"FSU kw '{kw}': {len(hits)} hits", [repr(t[max(0,h-80):h+160]) for h in hits[:3]])
                print("FSU LINKS:", [l for l in cd.get("links", []) if isinstance(l, dict) or isinstance(l, str)][:30])
