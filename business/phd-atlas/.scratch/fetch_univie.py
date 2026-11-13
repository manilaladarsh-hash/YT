import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

urls = [
    'https://informatik.univie.ac.at/',
    'https://mathematik.univie.ac.at/',
    'https://chemie.univie.ac.at/',
    'https://physik.univie.ac.at/',
    'https://lifesciences.univie.ac.at/',
    'https://fgga.univie.ac.at/',
    'https://astro.univie.ac.at/',
    'https://vds-cobene.univie.ac.at/'
]

for u in urls:
    print(f"Fetching {u} ...")
    cmd = [sys.executable, str(ROOT / "scripts" / "research.py"), u, "--kw", "PhD,Doctor,Doktorat"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    for line in res.stdout.split("\n"):
        if "status=" in line or "===" in line:
            print("  ", line)
