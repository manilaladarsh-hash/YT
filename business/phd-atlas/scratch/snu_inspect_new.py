import json
import re
from pathlib import Path

recs = {}
for p in Path('.cache/pages').glob('*.json'):
    try:
        r = json.loads(p.read_text(encoding='utf-8'))
        recs[r['url']] = r
    except Exception:
        pass

targets = [
    "https://stat.snu.ac.kr/en/",
    "https://astron.snu.ac.kr/en",
    "https://cuee.snu.ac.kr/",
    "https://cbe.snu.ac.kr/cbe/main/main.do",
    "https://health.snu.ac.kr/",
    "https://cals.snu.ac.kr/",
    "https://science.snu.ac.kr/en/edu/programs",
]

out = []
for u in targets:
    r = recs.get(u) or recs.get(u.rstrip('/'))
    if not r:
        out.append(f"MISSING {u}")
        continue
    out.append(f"=== {u} (final={r.get('final_url')}) ===")
    txt = r.get('text', '')
    out.extend(ln.strip() for ln in txt.splitlines() if ln.strip())
    out.append("LINKS:")
    for lnk in r.get('links', [])[:40]:
        out.append(f"  {lnk}")
    out.append("")

Path('scratch/snu_new_pages.txt').write_text('\n'.join(out), encoding='utf-8')
print("Wrote scratch/snu_new_pages.txt", len(out), "lines")
