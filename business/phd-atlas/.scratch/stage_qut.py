import json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STAGE = ROOT / "data" / "staging"

url_map = {
    'biology': 'https://www.qut.edu.au/about/faculty-of-science/school-of-biology-and-environmental-science',
    'environment': 'https://www.qut.edu.au/about/faculty-of-science/school-of-biology-and-environmental-science',
    'chemistry': 'https://www.qut.edu.au/about/faculty-of-science/school-of-chemistry-and-physics',
    'physics': 'https://www.qut.edu.au/about/faculty-of-science/school-of-chemistry-and-physics',
    'cs': 'https://www.qut.edu.au/about/faculty-of-science/school-of-computer-science',
    'earth': 'https://www.qut.edu.au/about/faculty-of-science/school-of-earth-and-atmospheric-sciences',
    'math': 'https://www.qut.edu.au/about/faculty-of-science/school-of-mathematical-sciences',
    'statistics': 'https://www.qut.edu.au/about/faculty-of-science/school-of-mathematical-sciences',
    'civil': 'https://www.qut.edu.au/about/faculty-of-engineering/school-of-civil-and-environmental-engineering',
    'ece': 'https://www.qut.edu.au/about/faculty-of-engineering/school-of-electrical-engineering-and-robotics',
    'mech': 'https://www.qut.edu.au/about/faculty-of-engineering/school-of-mechanical-medical-and-process-engineering',
    'bme': 'https://www.qut.edu.au/about/faculty-of-engineering/school-of-mechanical-medical-and-process-engineering',
    'chemeng': 'https://www.qut.edu.au/about/faculty-of-engineering/school-of-mechanical-medical-and-process-engineering',
    'materials': 'https://www.qut.edu.au/about/faculty-of-engineering/school-of-mechanical-medical-and-process-engineering'
}

shutil.copy(DATA / "universities" / "qut.json", STAGE / "universities" / "qut.json")

for field, url in url_map.items():
    src = DATA / "programs" / f"qut--{field}.json"
    dst = STAGE / "programs" / f"qut--{field}.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    data["program_page"] = url
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {dst.name} with program_page={url}")
