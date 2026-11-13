import json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STAGE = ROOT / "data" / "staging"

url_map = {
    'astronomy': 'https://astronomy.ucsc.edu/',
    'biology': 'https://eeb.ucsc.edu/',
    'biomed': 'https://pbse.ucsc.edu/',
    'bme': 'https://engineering.ucsc.edu/departments/biomolecular-engineering/',
    'chemistry': 'https://chemistry.ucsc.edu/',
    'cs': 'https://engineering.ucsc.edu/departments/computer-science-and-engineering/',
    'earth': 'https://eps.ucsc.edu/',
    'ece': 'https://engineering.ucsc.edu/departments/electrical-and-computer-engineering/',
    'environment': 'https://envs.ucsc.edu/',
    'materials': 'https://materials.ucsc.edu/',
    'math': 'https://math.ucsc.edu/',
    'physics': 'https://physics.ucsc.edu/',
    'statistics': 'https://engineering.ucsc.edu/departments/statistics/'
}

shutil.copy(DATA / "universities" / "ucsc.json", STAGE / "universities" / "ucsc.json")

for field, url in url_map.items():
    src = DATA / "programs" / f"ucsc--{field}.json"
    dst = STAGE / "programs" / f"ucsc--{field}.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    data["program_page"] = url
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {dst.name} with program_page={url}")
