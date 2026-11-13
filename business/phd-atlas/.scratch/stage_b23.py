import json, shutil

canterbury_quote = (
    "'UC Doctoral Scholarships' is a term referring to a collection of scholarships "
    "that are funded centrally by the University. Two application rounds each year, "
    "the first closing in May and the second in October."
)

for fn in [
    'canterbury-nz--civil.json',
    'canterbury-nz--datasci.json',
    'canterbury-nz--earth.json',
    'canterbury-nz--ece.json',
    'canterbury-nz--environment.json',
    'canterbury-nz--mech.json',
    'canterbury-nz--physics.json',
]:
    shutil.copy(f'data/programs/{fn}', f'data/staging/programs/{fn}')
    with open(f'data/staging/programs/{fn}', encoding='utf-8') as f:
        d = json.load(f)
    d['fields']['funding']['quote'] = canterbury_quote
    with open(f'data/staging/programs/{fn}', 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')

shutil.copy('data/programs/claremontgrad--biology.json', 'data/staging/programs/claremontgrad--biology.json')
with open('data/staging/programs/claremontgrad--biology.json', encoding='utf-8') as f:
    d = json.load(f)
d['fields']['gre_general']['quote'] = (
    'Standardized test scores are not required in order to apply for this program. '
    'Applicants who have taken the Graduate Record Examinations (GRE) General Test '
    'are invited to submit scores, but are not required to do so.'
)
with open('data/staging/programs/claremontgrad--biology.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)
    f.write('\n')

shutil.copy('data/programs/clarkson--chemeng.json', 'data/staging/programs/clarkson--chemeng.json')
with open('data/staging/programs/clarkson--chemeng.json', encoding='utf-8') as f:
    d = json.load(f)
d['fields']['entry_route']['quote'] = (
    'Prerequisites: BS or BE in Chemical Engineering. '
    'Those with degrees in other science or engineering disciplines may also be admitted '
    'but are required to make up undergraduate course deficiencies.'
)
with open('data/staging/programs/clarkson--chemeng.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)
    f.write('\n')

print("Staged 9 Batch 23 programs cleanly.")
