import hashlib, json, sys
from pathlib import Path
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
CACHE = Path(".cache/pages")

urls = [
    "https://www.uncw.edu/academics/colleges/cse/departments/biology/graduate.html",
    "https://www.uncw.edu/academics/colleges/cse/departments/chemistry/graduate-programs.html",
    "https://www.uncw.edu/academics/majors-programs/cms/applied-coastal-ocean-sciences-phd/details/index.html",
    "https://www.uncw.edu/academics/majors-programs/cse/psychology-phd/details/psychological-science/index.html",
    "https://www.uncw.edu/seahawk-life/support-success/international/students-scholars/stem-designated-programs.html",
    "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16886",
    "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16798",
    "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16891",
    "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16834",
]
out = []
for u in urls:
    p = CACHE / (hashlib.sha1(u.encode()).hexdigest()[:16] + ".json")
    if p.exists():
        d = json.loads(p.read_text(encoding="utf-8"))
        out.append(f"=== {u} (final={d.get('final_url')}, status={d.get('status')}) ===\n{d.get('text','')}\n")
Path("scratch/uncw_dump2.txt").write_text("\n".join(out), encoding="utf-8")
print("wrote scratch/uncw_dump2.txt")

# Check Slate SE_PHD_DIMB_BIO table HTML so we see exact column for 02/01/2027
r = requests.get("https://gradapply.uncw.edu/portal/apply?cmd=prog_details&program=SE_PHD_DIMB_BIO", timeout=20)
soup = BeautifulSoup(r.text, "lxml")
for tr in soup.find_all("tr"):
    print("ROW:", [" ".join(td.get_text().split()) for td in tr.find_all(["th", "td"])])
