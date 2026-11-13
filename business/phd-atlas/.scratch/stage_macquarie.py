import json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STAGE = ROOT / "data" / "staging"

computing = 'https://www.mq.edu.au/faculty-of-science-and-engineering/departments-and-schools/school-of-computing'
engineering = 'https://www.mq.edu.au/faculty-of-science-and-engineering/departments-and-schools/school-of-engineering'
math_phys = 'https://www.mq.edu.au/faculty-of-science-and-engineering/departments-and-schools/school-of-mathematical-and-physical-sciences'
natural_sci = 'https://www.mq.edu.au/faculty-of-science-and-engineering/departments-and-schools/school-of-natural-sciences'

url_map = {
    'cs': computing,
    'bme': engineering,
    'civil': engineering,
    'ece': engineering,
    'mech': engineering,
    'astronomy': math_phys,
    'math': math_phys,
    'physics': math_phys,
    'biology': natural_sci,
    'chemistry': natural_sci,
    'earth': natural_sci,
    'environment': natural_sci
}

shutil.copy(DATA / "universities" / "macquarie.json", STAGE / "universities" / "macquarie.json")

for field, url in url_map.items():
    src = DATA / "programs" / f"macquarie--{field}.json"
    dst = STAGE / "programs" / f"macquarie--{field}.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    data["program_page"] = url
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {dst.name} with program_page={url}")
