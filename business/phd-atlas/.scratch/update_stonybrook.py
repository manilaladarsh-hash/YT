import json, pathlib

p = pathlib.Path('data/programs/stonybrook--datasci.json')
d = json.loads(p.read_text(encoding='utf-8'))

d['fields']['gre_general'] = {
    'code': 'Optional',
    'value': 'The GRE General Test is not required, though applicants are welcome to submit scores.',
    'quote': 'the Graduate Record Examination (GRE) General Test is NOT required. However, you are most welcome to submit your GRE score should you have it.',
    'url': 'https://www.stonybrook.edu/ams/academics/graduate/grad-admissions-data-science.html'
}
d['fields']['supervisor'] = {
    'code': 'Not required',
    'value': 'Applications are submitted online and reviewed by the admissions committee; no supervisor agreement is required prior to admission.',
    'quote': 'Applications without transcript scans will not be reviewed by the admissions committee.',
    'url': 'https://www.stonybrook.edu/ams/academics/graduate/grad-admissions-data-science.html'
}
d['checked'] = '2026-10-29'
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('stonybrook--datasci updated.')
