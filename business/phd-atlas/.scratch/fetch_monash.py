import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

urls = [
    'https://www.monash.edu/science/schools/physics-and-astronomy',
    'https://www.monash.edu/engineering/departments/chemical-and-biological/research',
    'https://www.monash.edu/science/schools/chemistry',
    'https://www.monash.edu/engineering/departments/civil/research',
    'https://www.monash.edu/it/research/graduate-research',
    'https://www.monash.edu/it/departments/data-science-ai',
    'https://www.monash.edu/science/schools/earth-atmosphere-environment/postgraduate-studies',
    'https://www.monash.edu/engineering/departments/ecse/research',
    'https://www.monash.edu/science/schools/earth-atmosphere-environment',
    'https://www.monash.edu/engineering/departments/materials/research',
    'https://www.monash.edu/science/schools/school-of-mathematics/postgraduate-research',
    'https://www.monash.edu/engineering/departments/mechanical-and-aerospace/research',
    'https://www.monash.edu/science/schools/physics-and-astronomy/postgraduate-studies'
]

for u in urls:
    print(f"Fetching {u} ...")
    cmd = [sys.executable, str(ROOT / "scripts" / "research.py"), u, "--kw", "PhD,Doctor,research"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    for line in res.stdout.split("\n"):
        if "status=" in line or "===" in line:
            print("  ", line)
