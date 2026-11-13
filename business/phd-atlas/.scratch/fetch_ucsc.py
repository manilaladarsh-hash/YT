import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

urls = [
    'https://astronomy.ucsc.edu/',
    'https://eeb.ucsc.edu/',
    'https://pbse.ucsc.edu/',
    'https://engineering.ucsc.edu/departments/biomolecular-engineering/',
    'https://chemistry.ucsc.edu/',
    'https://engineering.ucsc.edu/departments/computer-science-and-engineering/',
    'https://eps.ucsc.edu/',
    'https://engineering.ucsc.edu/departments/electrical-and-computer-engineering/',
    'https://envs.ucsc.edu/',
    'https://materials.ucsc.edu/',
    'https://math.ucsc.edu/',
    'https://physics.ucsc.edu/',
    'https://engineering.ucsc.edu/departments/statistics/'
]

for u in urls:
    print(f"Fetching {u} ...")
    cmd = [sys.executable, str(ROOT / "scripts" / "research.py"), u, "--kw", "PhD,Doctor,admissions"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    for line in res.stdout.split("\n"):
        if "status=" in line or "===" in line:
            print("  ", line)
