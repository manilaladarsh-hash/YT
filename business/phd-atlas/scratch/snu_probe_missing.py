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

# 1. Dump PDF if cached
pdf_url = "https://en.snu.ac.kr/webdata/uploads/eng/file/2026/06/2027Spring_graduate_eng.pdf"
if pdf_url in recs:
    Path('scratch/snu_pdf.txt').write_text(recs[pdf_url].get('text', ''), encoding='utf-8')
    print(f"PDF dumped: {len(recs[pdf_url].get('text', ''))} chars")
else:
    print("PDF not in cache!")

# 2. List all cached snu.ac.kr URLs with status and length
snu_urls = sorted(u for u in recs if 'snu.ac.kr' in u)
print(f"Total cached snu.ac.kr URLs: {len(snu_urls)}")
for u in snu_urls:
    r = recs[u]
    print(f"  [{r.get('status')}] {len(r.get('text','')):6d}  {u}")
