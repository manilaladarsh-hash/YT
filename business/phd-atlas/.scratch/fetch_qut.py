import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

urls = [
    'https://www.qut.edu.au/about/faculty-of-science/school-of-biology-and-environmental-science',
    'https://www.qut.edu.au/about/faculty-of-science/school-of-chemistry-and-physics',
    'https://www.qut.edu.au/about/faculty-of-science/school-of-computer-science',
    'https://www.qut.edu.au/about/faculty-of-science/school-of-earth-and-atmospheric-sciences',
    'https://www.qut.edu.au/about/faculty-of-science/school-of-mathematical-sciences',
    'https://www.qut.edu.au/about/faculty-of-engineering/school-of-civil-and-environmental-engineering',
    'https://www.qut.edu.au/about/faculty-of-engineering/school-of-electrical-engineering-and-robotics',
    'https://www.qut.edu.au/about/faculty-of-engineering/school-of-mechanical-medical-and-process-engineering'
]

for u in urls:
    print(f"Fetching {u} ...")
    cmd = [sys.executable, str(ROOT / "scripts" / "research.py"), u, "--kw", "PhD,Doctor,research"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    for line in res.stdout.split("\n"):
        if "status=" in line or "===" in line:
            print("  ", line)
