import hashlib, json, pathlib, bs4, requests

def dump_cached(url, start=0, length=40000):
    h = hashlib.sha1(url.encode()).hexdigest()[:16]
    p = pathlib.Path(".cache/pages") / f"{h}.json"
    if not p.exists():
        return f"=== MISSING {url} ({h}) ==="
    d = json.loads(p.read_text(encoding="utf-8"))
    txt = d.get("text", "")
    return f"\n=== {url} (status={d.get('status')}, total={len(txt)}, slice={start}:{start+length}) ===\n" + txt[start:start+length]

# 1) Find where College of Engineering starts in graduateschool.uccs.edu/academics
h_acad = hashlib.sha1(b"https://graduateschool.uccs.edu/academics").hexdigest()[:16]
acad_txt = json.loads((pathlib.Path(".cache/pages") / f"{h_acad}.json").read_text(encoding="utf-8")).get("text", "")
idx_eng = acad_txt.find("Computer Science, PhD\nDegree:")
if idx_eng == -1:
    idx_eng = acad_txt.find("College of Engineering\n")
    idx_eng = acad_txt.find("Computer Science, MS", idx_eng) if idx_eng != -1 else 18000
idx_nurs = acad_txt.find("College of Nursing and Health Sciences\nAthletic Training")
if idx_nurs == -1:
    idx_nurs = min(len(acad_txt), idx_eng + 45000)

out = [
    f"=== ACADEMICS ENG+LAS ({idx_eng}..{idx_nurs}) ===",
    acad_txt[max(0, idx_eng-200):idx_nurs],
    dump_cached("https://eas.uccs.edu/academics/programs/computer-science-phd", 6000, 10000),
    dump_cached("https://programfinder.uccs.edu/programs/applied-science-phd", 0, 20000),
    dump_cached("https://psychology.uccs.edu/academics/graduate", 0, 20000),
    dump_cached("https://physics.uccs.edu/sites/default/files/inline-files/UCCS_PhD_Physics_Handbook-August2023.pdf", 0, 30000),
    dump_cached("https://graduateschool.uccs.edu/current-student-resources/policies-procedures", 0, 20000),
]

# Also check links on ME PhD page, EAS graduate, MAE site, Psychology PhD pages
check_urls = [
    "https://eas.uccs.edu/graduate-programs/mechanical-engineering-phd",
    "https://eas.uccs.edu/graduate",
    "https://eas.uccs.edu/mae",
    "https://eas.uccs.edu/ece",
    "https://eas.uccs.edu/cs",
    "https://psychology.uccs.edu/academics/geropsychology-phd",
    "https://psychology.uccs.edu/academics/clinical-trauma-phd",
]
out.append("\n=== LINK DISCOVERY ===")
for u in check_urls:
    try:
        r = requests.get(u, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        out.append(f"\nLINKCHECK {u} -> {r.status_code} {r.url}")
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        seen = set()
        for a in soup.find_all("a", href=True):
            href = requests.compat.urljoin(r.url, a["href"])
            t = " ".join(a.get_text().split())
            if href not in seen and any(k in (t+href).lower() for k in ["phd","doctor","apply","admis","fund","assist","fellow","hand","deadlin","gre","toefl","gero","trauma"]):
                seen.add(href)
                out.append(f"  {t[:55]} -> {href}")
    except Exception as e:
        out.append(f"ERR {u}: {e}")

pathlib.Path("scratch/uccs_dump2.txt").write_text("\n".join(out), encoding="utf-8")
print("WROTE dump2, lines=", sum(s.count("\n")+1 for s in out))
