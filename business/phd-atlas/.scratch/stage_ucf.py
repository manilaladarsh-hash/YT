import json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STAGE = ROOT / "data" / "staging"

url_map = {
    'astronomy': 'https://sciences.ucf.edu/physics/graduate/',
    'biology': 'https://sciences.ucf.edu/biology/graduate/',
    'biomed': 'https://med.ucf.edu/biomed/graduate-programs/phd-biomedical-sciences/',
    'bme': 'https://www.ucf.edu/degree/biomedical-engineering-phd/',
    'chemistry': 'https://www.ucf.edu/degree/chemistry-phd/',
    'civil': 'https://www.ucf.edu/degree/civil-engineering-phd/',
    'datasci': 'https://www.ucf.edu/degree/big-data-analytics-phd/',
    'ece': 'https://www.ucf.edu/degree/electrical-engineering-phd/',
    'environment': 'https://www.ucf.edu/degree/environmental-engineering-phd/',
    'materials': 'https://www.ucf.edu/degree/materials-science-and-engineering-phd/',
    'math': 'https://www.ucf.edu/degree/mathematics-phd/',
    'mech': 'https://www.ucf.edu/degree/mechanical-engineering-phd/',
    'neuro': 'https://www.ucf.edu/degree/biomedical-sciences-phd/',
    'statistics': 'https://sciences.ucf.edu/statistics/graduate/'
}

shutil.copy(DATA / "universities" / "ucf.json", STAGE / "universities" / "ucf.json")

for field, url in url_map.items():
    src = DATA / "programs" / f"ucf--{field}.json"
    dst = STAGE / "programs" / f"ucf--{field}.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    data["program_page"] = url
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {dst.name} with program_page={url}")
