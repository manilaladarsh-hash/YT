import json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STAGE = ROOT / "data" / "staging"

url_map = {
    'astronomy': 'https://www.monash.edu/science/schools/physics-and-astronomy',
    'biology': 'https://www.monash.edu/science/schools/biological-sciences',
    'chemeng': 'https://www.monash.edu/engineering/departments/chemical-and-biological/research',
    'chemistry': 'https://www.monash.edu/science/schools/chemistry',
    'civil': 'https://www.monash.edu/engineering/departments/civil/research',
    'cs': 'https://www.monash.edu/it/research/graduate-research',
    'datasci': 'https://www.monash.edu/it/departments/data-science-ai',
    'earth': 'https://www.monash.edu/science/schools/earth-atmosphere-environment/postgraduate-studies',
    'ece': 'https://www.monash.edu/engineering/departments/ecse/research',
    'environment': 'https://www.monash.edu/science/schools/earth-atmosphere-environment',
    'materials': 'https://www.monash.edu/engineering/departments/materials/research',
    'math': 'https://www.monash.edu/science/schools/school-of-mathematics/postgraduate-research',
    'mech': 'https://www.monash.edu/engineering/departments/mechanical-and-aerospace/research',
    'physics': 'https://www.monash.edu/science/schools/physics-and-astronomy/postgraduate-studies'
}

shutil.copy(DATA / "universities" / "monash.json", STAGE / "universities" / "monash.json")

for field, url in url_map.items():
    src = DATA / "programs" / f"monash--{field}.json"
    dst = STAGE / "programs" / f"monash--{field}.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    data["program_page"] = url
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {dst.name} with program_page={url}")
