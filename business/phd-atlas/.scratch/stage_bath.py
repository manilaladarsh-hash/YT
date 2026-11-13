import json, os, shutil
from pathlib import Path

ROOT = Path('C:/Users/manil/YT/business/phd-atlas')
STAGE = ROOT / 'data' / 'staging'
DATA = ROOT / 'data'
REMOVED = STAGE / '_removed'

REMOVED.mkdir(parents=True, exist_ok=True)
(STAGE / 'programs').mkdir(parents=True, exist_ok=True)
(STAGE / 'universities').mkdir(parents=True, exist_ok=True)

# 1. Move 4 unverified programs from live to staging/_removed
for field in ['bme', 'materials', 'earth', 'environment']:
    f = DATA / 'programs' / f'bath--{field}.json'
    if f.exists():
        shutil.move(str(f), str(REMOVED / f'bath--{field}.json'))
        print(f"Moved bath--{field}.json to data/staging/_removed/")

# 2. Copy bath.json to staging
shutil.copy(str(DATA / 'universities' / 'bath.json'), str(STAGE / 'universities' / 'bath.json'))

# 3. Write 13 programs to staging/programs/
import sys
sys.path.insert(0, str(ROOT / '.scratch'))
import test_bath_build

for fname, r in test_bath_build.out_progs.items():
    dest = STAGE / 'programs' / fname
    dest.write_text(json.dumps(r, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print("Wrote 13 Bath program files to data/staging/programs/")
