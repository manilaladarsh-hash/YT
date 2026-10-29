import json, pathlib

u_path = pathlib.Path('data/universities/clevelandstate.json')
u_data = json.loads(u_path.read_text(encoding='utf-8'))
u_data['fields']['gre_general'] = {
    'code': 'Not required',
    'value': 'Entrance exam scores are not required centrally; requirements are set program by program.',
    'quote': 'Not all programs require entrance exam scores.',
    'url': 'https://graduate-studies.csuohio.edu/grad-engage/international-admissions'
}
u_data['checked'] = '2026-10-29'
u_path.write_text(json.dumps(u_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

p_path = pathlib.Path('data/programs/clevelandstate--datasci.json')
p_data = json.loads(p_path.read_text(encoding='utf-8'))
p_data['fields']['funding'] = {
    'code': 'Competitive',
    'value': 'Research assistantships are provided through sponsored research activities depending on college funding availability.',
    'quote': 'Research assistantships are provided through sponsored research activities; the number available at a given time is dependent on the research activity within the College.',
    'url': 'https://engineering.csuohio.edu/cs/phd-in-engineering-applied-data-science'
}
p_data['checked'] = '2026-10-29'
p_path.write_text(json.dumps(p_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('clevelandstate updated.')
