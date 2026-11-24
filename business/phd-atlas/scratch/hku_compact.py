import pathlib, json, hashlib

urls = [
    'https://engg.hku.hk/Admissions/PhD-MPhil',
    'https://www.civil.hku.hk/h4_pros_pg_MPhil_PhD.html',
    'https://sbme.hku.hk/',
    'https://www.cds.hku.hk/',
    'https://www.eee.hku.hk/study/rpg/',
    'https://www.mech.hku.hk/rpg',
    'https://www.med.hku.hk/en/teaching-and-learning/postgraduate/rpg',
    'https://www.sbms.hku.hk/',
    'https://www.biosch.hku.hk/teaching/research-postgraduate-programmes/',
    'https://chemistry.hku.hk/study/postgraduate_students/11/',
    'https://www.earthsciences.hku.hk/prospective-students/postgraduate-students/research-postgraduates/general-information',
    'https://hkumath.hku.hk/web/prospective/p-pg-admission.php',
    'https://www.physics.hku.hk/prospective-students/rpg-admission',
    'https://www.scifac.hku.hk/rpg/why-hku-science',
    'https://www.geog.hku.hk/mphil-phd',
]
out = []
for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    p = pathlib.Path('.cache/pages') / f'{h}.json'
    if not p.exists():
        out.append(f'=== MISSING {u} ===')
        continue
    d = json.loads(p.read_text(encoding='utf-8'))
    out.append(f'=== {u} -> {d.get("final_url")} ===')
    t = d.get('text', '')
    out.append(t[:4000])
    links = [f'{l[0]} -> {l[1]}' for l in d.get('links', []) if any(k in (l[0]+l[1]).lower() for k in ['phd','mphil','rpg','research','admiss','postgrad','stipend','fellow','dase','sbme','mech','material','neuro','env','bio','stat','cds','prog','entry','supervis','requir'])]
    out.append('KEY LINKS:\n  ' + '\n  '.join(dict.fromkeys(links[:40])))
pathlib.Path('scratch/hku_compact.txt').write_text('\n'.join(out), encoding='utf-8')
print('Wrote scratch/hku_compact.txt')
