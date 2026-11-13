import json, shutil

new_quote = (
    "'UC Doctoral Scholarships' is a term referring to a collection of scholarships "
    "that are funded centrally by the University. Two application rounds each year, "
    "the first closing in May and the second in October."
)

for fn in [
    'canterbury-nz--astronomy.json',
    'canterbury-nz--bme.json',
    'canterbury-nz--chemeng.json',
    'canterbury-nz--chemistry.json',
]:
    src = f'data/programs/{fn}'
    dst = f'data/staging/programs/{fn}'
    shutil.copy(src, dst)
    with open(dst, encoding='utf-8') as f:
        d = json.load(f)
    d['fields']['funding']['quote'] = new_quote
    with open(dst, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')

print("Staged 4 canterbury-nz programs cleanly.")
