import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

urls = [
    'https://www.mq.edu.au/faculty-of-science-and-engineering/schools-and-departments/school-of-computing',
    'https://www.mq.edu.au/faculty-of-science-and-engineering/schools-and-departments/school-of-engineering',
    'https://www.mq.edu.au/faculty-of-science-and-engineering/schools-and-departments/school-of-mathematical-and-physical-sciences',
    'https://www.mq.edu.au/faculty-of-science-and-engineering/schools-and-departments/school-of-natural-sciences',
    'https://www.mq.edu.au/faculty-of-science-and-engineering/schools-and-departments/australian-astronomical-optics'
]

for u in urls:
    print(f"Fetching {u} ...")
    cmd = [sys.executable, str(ROOT / "scripts" / "research.py"), u, "--kw", "PhD,Doctor,research"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    for line in res.stdout.split("\n"):
        if "status=" in line or "===" in line:
            print("  ", line)
