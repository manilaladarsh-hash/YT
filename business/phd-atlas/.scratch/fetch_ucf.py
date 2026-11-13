import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

urls = [
    'https://sciences.ucf.edu/physics/graduate/',
    'https://sciences.ucf.edu/biology/graduate/',
    'https://med.ucf.edu/biomed/graduate-programs/phd-biomedical-sciences/',
    'https://www.ucf.edu/degree/biomedical-engineering-phd/',
    'https://www.ucf.edu/degree/chemistry-phd/',
    'https://www.ucf.edu/degree/civil-engineering-phd/',
    'https://www.ucf.edu/degree/big-data-analytics-phd/',
    'https://www.ucf.edu/degree/electrical-engineering-phd/',
    'https://www.ucf.edu/degree/environmental-engineering-phd/',
    'https://www.ucf.edu/degree/materials-science-and-engineering-phd/',
    'https://www.ucf.edu/degree/mathematics-phd/',
    'https://www.ucf.edu/degree/mechanical-engineering-phd/',
    'https://www.ucf.edu/degree/biomedical-sciences-phd/',
    'https://sciences.ucf.edu/statistics/graduate/'
]

for u in urls:
    print(f"Fetching {u} ...")
    cmd = [sys.executable, str(ROOT / "scripts" / "research.py"), u, "--kw", "PhD,Doctor,admissions"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    for line in res.stdout.split("\n"):
        if "status=" in line or "===" in line:
            print("  ", line)
