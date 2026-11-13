import json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STAGE = ROOT / "data" / "staging"

url_map = {
    'biology': 'https://cosam.auburn.edu/biology/index.php',
    'biomed': 'https://cosam.auburn.edu/biomedical/index.php',
    'chemeng': 'https://eng.auburn.edu/chen/academics/graduate/',
    'chemistry': 'https://cosam.auburn.edu/chemistry/',
    'civil': 'https://eng.auburn.edu/cee/academics/graduate/',
    'cs': 'https://eng.auburn.edu/csse/academics/graduate/',
    'earth': 'https://cosam.auburn.edu/geosciences/',
    'ece': 'https://eng.auburn.edu/ece/academics/graduate/',
    'materials': 'https://eng.auburn.edu/matl/academics/graduate/',
    'math': 'https://cosam.auburn.edu/math/',
    'mech': 'https://eng.auburn.edu/mech/academics/graduate/'
}

shutil.copy(DATA / "universities" / "auburn.json", STAGE / "universities" / "auburn.json")

for field, url in url_map.items():
    src = DATA / "programs" / f"auburn--{field}.json"
    dst = STAGE / "programs" / f"auburn--{field}.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    data["program_page"] = url
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {dst.name} with program_page={url}")
