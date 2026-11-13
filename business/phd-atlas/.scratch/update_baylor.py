import json, pathlib

p = pathlib.Path('data/programs/baylor--statistics.json')
d = json.loads(p.read_text(encoding='utf-8'))

d['fields']['supervisor'] = {
    'code': 'Not required',
    'value': 'Application requires form, transcripts, letters, and GRE scores submitted to the Graduate School; no prior supervisor is required.',
    'quote': 'Applicants must submit the following: | A Baylor University application form | Official transcripts that bear the seal from all colleges or universities attended | Three letters of reference | GRE scores (verbal & quantitative)',
    'url': 'https://statistics.artsandsciences.baylor.edu/graduate/how-apply'
}
d['checked'] = '2026-10-29'
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('baylor--statistics updated.')
