"""Promote reviewed drafts from data/staging/ into data/.

Usage: python3 scripts/promote.py UID [UID ...]   (moves the university record and all its programs)
Each draft set is validated with quote checks first; nothing moves if any error is found.
"""

import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_data  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
STAGE, DATA = ROOT / "data" / "staging", ROOT / "data"


def main(uids):
    errors, warnings, nu, npr = validate_data.validate(True, STAGE)
    mine = [e for e in errors if any(f"/{u}.json" in e or f"/{u}--" in e for u in uids)]
    if mine:
        print("\n".join(mine))
        raise SystemExit("not promoted: fix the errors above")
    moved = 0
    for uid in uids:
        files = list((STAGE / "universities").glob(f"{uid}.json")) + list((STAGE / "programs").glob(f"{uid}--*.json"))
        if not files:
            print(f"nothing staged for {uid}")
        for f in files:
            dest = DATA / f.parent.name / f.name
            dest.parent.mkdir(exist_ok=True)
            shutil.move(str(f), dest)
            moved += 1
    print(f"promoted {moved} files")


if __name__ == "__main__":
    main(sys.argv[1:])
