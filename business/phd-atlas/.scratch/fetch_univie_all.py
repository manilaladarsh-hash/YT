import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

urls = [
    'https://careers.univie.ac.at/en/praedoc/stem-call/computer-sciences',
    'https://careers.univie.ac.at/en/praedoc/stem-call/chemistry',
    'https://careers.univie.ac.at/en/praedoc/stem-call/ecology-and-evolution',
    'https://careers.univie.ac.at/en/praedoc/stem-call/microbiology-and-environmental-sciences',
    'https://fgga.univie.ac.at/en/',
    'https://astro.univie.ac.at/en/'
]

for u in urls:
    print(f"Fetching {u} ...")
    cmd = [sys.executable, str(ROOT / "scripts" / "research.py"), u, "--kw", "PhD,Doctor,Praedoc"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    for line in res.stdout.split("\n"):
        if "status=" in line or "===" in line:
            print("  ", line)
