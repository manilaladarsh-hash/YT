import json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STAGE = ROOT / "data" / "staging"

url_map = {
    'astronomy': 'https://fys.kuleuven.be/ster',
    'biology': 'https://bio.kuleuven.be/',
    'bme': 'https://www.mech.kuleuven.be/en/bme',
    'chemeng': 'https://cit.kuleuven.be/english',
    'chemistry': 'https://chem.kuleuven.be/en',
    'civil': 'https://bwk.kuleuven.be/',
    'cs': 'https://wms.cs.kuleuven.be/cs/english/research/phd',
    'earth': 'https://ees.kuleuven.be/en',
    'ece': 'https://www.esat.kuleuven.be/english',
    'materials': 'https://www.mtm.kuleuven.be/',
    'math': 'https://wis.kuleuven.be/english',
    'mech': 'https://www.mech.kuleuven.be/en',
    'neuro': 'https://gbiomed.kuleuven.be/english/research/50000666',
    'physics': 'https://fys.kuleuven.be/english',
    'statistics': 'https://lstat.kuleuven.be/'
}

shutil.copy(DATA / "universities" / "kuleuven.json", STAGE / "universities" / "kuleuven.json")

for field, url in url_map.items():
    src = DATA / "programs" / f"kuleuven--{field}.json"
    dst = STAGE / "programs" / f"kuleuven--{field}.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    data["program_page"] = url
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {dst.name} with program_page={url}")
