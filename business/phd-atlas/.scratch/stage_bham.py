import json, os, shutil
from pathlib import Path

ROOT = Path('C:/Users/manil/YT/business/phd-atlas')
STAGE = ROOT / 'data' / 'staging'
DATA = ROOT / 'data'
REMOVED = STAGE / '_removed'

REMOVED.mkdir(parents=True, exist_ok=True)
(STAGE / 'programs').mkdir(parents=True, exist_ok=True)
(STAGE / 'universities').mkdir(parents=True, exist_ok=True)

# 1. Move birmingham--bme.json from live programs to staging/_removed
if (DATA / 'programs' / 'birmingham--bme.json').exists():
    shutil.move(str(DATA / 'programs' / 'birmingham--bme.json'), str(REMOVED / 'birmingham--bme.json'))
    print("Moved birmingham--bme.json to data/staging/_removed/")

# 2. Copy birmingham.json to staging
shutil.copy(str(DATA / 'universities' / 'birmingham.json'), str(STAGE / 'universities' / 'birmingham.json'))

# 3. Generate and write the 16 program files to staging/programs/
import sys
sys.path.insert(0, str(ROOT / '.scratch'))
import test_bham_build

for fname, r in test_bham_build.out_progs.items():
    dest = STAGE / 'programs' / fname
    dest.write_text(json.dumps(r, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print("Wrote 16 program files to data/staging/programs/")
