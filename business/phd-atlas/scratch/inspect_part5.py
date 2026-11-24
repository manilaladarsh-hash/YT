import glob, json, os

cache_files = glob.glob('.cache/pages/*.json')
by_sub = {}
targets = [
    'Prospectus-2027.html',
    '05CBMS_BD_e.pdf',
    '06NENV_BD_e.pdf',
    '03CSE_BD_e.pdf',
    'Guidelines-for-toefl-scores_2027_e.pdf',
    'bi_guide_d.pdf',
    'cs_guide_e_3.pdf',
    'ma_guide.pdf',
    '2027guidelines_for_applicants_to_dc.pdf',
    'gsfs/financial_support',
    'examinee_e.html',
    'soe/international-programs',
    'soe/admission/scholarship',
    'soe/admission/financial-aid',
    's.u-tokyo.ac.jp/en/admission/scholarship.html',
    's.u-tokyo.ac.jp/en/admission/doctor/index.html',
    's.u-tokyo.ac.jp/GSGC/overview/index.html',
    's.u-tokyo.ac.jp/GSGC/faq/',
    'phys.s.u-tokyo.ac.jp',
    'www.sih.m.u-tokyo.ac.jp',
]

out = []
for f in sorted(cache_files):
    with open(f, 'r', encoding='utf-8') as fh:
        d = json.load(fh)
    url = d.get('url', '')
    for t in targets:
        if t in url:
            txt = d.get('text', '')
            out.append(f"\n=== {url} (status={d.get('status')}, len={len(txt)}) ===")
            if 'Prospectus-2027.html' in url:
                out.append(txt[12000:18000])
            elif '2027guidelines_for_applicants_to_dc.pdf' in url:
                out.append(txt[:18000])
            elif 'ma_guide.pdf' in url:
                out.append(txt[:15000])
            elif 'cs_guide_e_3.pdf' in url:
                out.append(txt[:18000])
            elif 'bi_guide_d.pdf' in url:
                out.append(txt[:18000])
            else:
                out.append(txt[:15000])
            break

with open('scratch/utokyo_check_part5.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out))
print("Wrote scratch/utokyo_check_part5.txt")
