import json, pathlib

p = pathlib.Path('data/programs/njit--datasci.json')
d = json.loads(p.read_text(encoding='utf-8'))

d['fields']['deadline'] = {
    'code': '2026-12-15',
    'value': 'Application deadline for fall admission is December 15.',
    'quote': 'Application deadlines are October 15 for spring and December 15 for fall.',
    'url': 'https://ds.njit.edu/phd-data-science',
    'inferred': 'year'
}
d['fields']['supervisor'] = {
    'code': 'Not required',
    'value': 'Research advisor is identified after admission, no later than the start of the second semester.',
    'quote': 'Students are recommended to identify a research advisor as soon as possible, and no later than the start of the second semester.',
    'url': 'https://ds.njit.edu/phd-data-science'
}
d['checked'] = '2026-10-29'
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('njit--datasci updated.')
