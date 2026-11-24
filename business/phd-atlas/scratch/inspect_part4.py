import glob, json, os

cache_files = glob.glob('.cache/pages/*.json')
ut_entries = []
for f in cache_files:
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            d = json.load(fh)
        url = d.get('url', '')
        if 'u-tokyo' in url or 'umin.jp' in url:
            ut_entries.append((url, f, d))
    except Exception:
        pass

print(f"Total cached u-tokyo/umin entries: {len(ut_entries)}")
for url, f, d in sorted(ut_entries):
    print(f"  {d.get('status')} | {len(d.get('text','')):>6} | {os.path.basename(f)} | {url}")

out = []
def dump_match(substr, start=0, length=40000):
    for url, f, d in sorted(ut_entries):
        if substr in url:
            txt = d.get('text', '')
            out.append(f"\n=== {url} (file={os.path.basename(f)}, status={d.get('status')}, len={len(txt)}) ===")
            out.append(txt[start:start+length])

dump_match('GSGC/pdf/Guidelines.pdf', 0, 30000)
dump_match('General%20Application%20Guidelines', 0, 35000)
dump_match('Prospectus-2027.html', 15000, 20000)
dump_match('ee_guide_e.pdf', 8000, 26000)
dump_match('me_guide_e_2.pdf', 8000, 10000)
dump_match('koukikoku2027E.pdf', 10000, 20000)
dump_match('englishnotes', 0, 20000)
dump_match('doctor2027E.pdf', 12000, 22000)
dump_match('ci/admission_e.shtml', 0, 15000)
dump_match('ipc/admissions_e.shtml', 0, 15000)
dump_match('ms.u-tokyo', 0, 25000)
dump_match('s.u-tokyo.ac.jp/en/departments/index.html', 0, 18000)
dump_match('s.u-tokyo.ac.jp/en/graduate-applicants/index.html', 0, 20000)
dump_match('s.u-tokyo.ac.jp/en/overview/graduate02.html', 0, 20000)
dump_match('m.u-tokyo.ac.jp/english/daigakuin/apply/', 0, 20000)
dump_match('civil.t.u-tokyo.ac.jp', 0, 20000)
dump_match('chemsys', 0, 10000)
dump_match('bioeng', 0, 15000)
dump_match('04IB_BD_e.pdf', 0, 25000)
dump_match('05CBMS_BD_e.pdf', 0, 25000)
dump_match('06NENV_BD_e.pdf', 0, 25000)
dump_match('Guidelines-for-toefl-scores_2027_e.pdf', 0, 15000)

with open('scratch/utokyo_check_part4.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out))
print(f"Wrote scratch/utokyo_check_part4.txt ({len(out)} blocks)")
