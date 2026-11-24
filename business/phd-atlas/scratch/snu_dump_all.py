import json
from pathlib import Path

recs = {}
for p in Path('.cache/pages').glob('*.json'):
    try:
        r = json.loads(p.read_text(encoding='utf-8'))
        recs[r['url']] = r
    except Exception:
        pass

urls = sorted(u for u in recs if 'snu.ac.kr' in u and not u.endswith('.pdf'))
out = []
clean = []
for u in urls:
    r = recs[u]
    hdr = f"=== {u} (status={r.get('status')}, len={len(r.get('text',''))}, final={r.get('final_url')}) ==="
    out.append(hdr)
    clean.append(hdr)
    txt = r.get('text', '')
    lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
    out.extend(lines)
    out.append("")
    seen = set()
    for ln in lines:
        if len(ln) > 30 and ln not in seen:
            seen.add(ln)
            clean.append(ln)
    clean.append("")

Path('scratch/snu_all_pages.txt').write_text('\n'.join(out), encoding='utf-8')
Path('scratch/snu_clean_pages.txt').write_text('\n'.join(clean), encoding='utf-8')
print(f"Dumped {len(urls)} URLs ({len(clean)} clean lines)")
