import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

urls = [
    'https://cosam.auburn.edu/biology/index.php',
    'https://cosam.auburn.edu/biomedical/index.php',
    'https://eng.auburn.edu/chen/academics/graduate/',
    'https://cosam.auburn.edu/chemistry/',
    'https://eng.auburn.edu/cee/academics/graduate/',
    'https://eng.auburn.edu/csse/academics/graduate/',
    'https://cosam.auburn.edu/geosciences/',
    'https://eng.auburn.edu/ece/academics/graduate/',
    'https://eng.auburn.edu/matl/academics/graduate/',
    'https://cosam.auburn.edu/math/',
    'https://eng.auburn.edu/mech/academics/graduate/'
]

for u in urls:
    print(f"Fetching {u} ...")
    cmd = [sys.executable, str(ROOT / "scripts" / "research.py"), u, "--kw", "PhD,Doctor,graduate"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    for line in res.stdout.split("\n"):
        if "status=" in line or "===" in line:
            print("  ", line)
