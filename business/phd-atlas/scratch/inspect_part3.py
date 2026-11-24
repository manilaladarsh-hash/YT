import json
from pathlib import Path

cache = Path('.cache/pages')
by_url = {}
for p in cache.glob('*.json'):
    try:
        r = json.loads(p.read_text(encoding='utf-8'))
        by_url[r.get('url', '')] = r
        if r.get('final_url'):
            by_url[r['final_url']] = r
    except Exception:
        pass

def dump(u, start=0, length=12000):
    r = by_url.get(u)
    return f'=== {u} (found={bool(r)}, total={len(r.get("text","")) if r else 0}) ===\n' + (r.get('text', '')[start:start+length] if r else '')

parts = [
    dump('https://www.t.u-tokyo.ac.jp/hubfs/admission/2026/1001/Schdedule_B_2.pdf', 0, 5000),
    dump('https://www.t.u-tokyo.ac.jp/hubfs/admission/2026/0403/Guidelines_gse_en_d_2027.pdf', 0, 14000),
    dump('https://www.t.u-tokyo.ac.jp/hubfs/admission/2026/0728/TOEFL_2027(E)_2.pdf', 0, 5000),
    dump('https://www.t.u-tokyo.ac.jp/hubfs/admission/2026/0403/me_guide_e_2.pdf', 0, 6000),
    dump('https://www.t.u-tokyo.ac.jp/hubfs/admission/2026/0403/ee_guide_e.pdf', 0, 6000),
    dump('https://www.chemsys.t.u-tokyo.ac.jp/curriculum/graduate/admission/?lang=en', 0, 5000),
    dump('https://www.material.t.u-tokyo.ac.jp/e/prospective_students/', 0, 7000),
    dump('https://bioeng.t.u-tokyo.ac.jp/admissions/', 0, 5000),
    dump('https://www.ime.t.u-tokyo.ac.jp/Prospectus-2027.html', 0, 14000),
    dump('https://www.i.u-tokyo.ac.jp/edu/course/cs/cs_admission_guide2027_en.pdf', 0, 8000),
    dump('https://www.i.u-tokyo.ac.jp/edu/course/mi/upload/mi-2027-e.pdf', 0, 10000),
    dump('https://www.i.u-tokyo.ac.jp/edu/financial-support/index_e.shtml', 0, 7000),
    dump('https://www.s.u-tokyo.ac.jp/en/offices/ilo/scholarship.html', 0, 10000),
    dump('https://www.s.u-tokyo.ac.jp/GSGC/pdf/Guidelines.pdf', 0, 10000),
    dump('https://www.m.u-tokyo.ac.jp/daigakuin/apply/file/koukikoku2027E.pdf', 0, 10000),
    dump('https://www.m.u-tokyo.ac.jp/daigakuin/apply/file/doctor2027E.pdf', 0, 10000),
    dump('https://www.u-tokyo.ac.jp/en/prospective-students/graduate_course_list.html', 0, 7000),
]

Path('scratch/utokyo_check_part3.txt').write_text('\n'.join(parts), encoding='utf-8')
print('Wrote scratch/utokyo_check_part3.txt')
