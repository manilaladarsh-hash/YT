import pathlib, json, hashlib

urls = [
  'https://engg.hku.hk/Teaching-Learning/PhD-MPhil/Fields-of-Study',
  'https://engg.hku.hk/About-Us/Departments',
  'https://sbme.hku.hk/programme',
  'https://www.cds.hku.hk/prospective-students/postgraduate/',
  'https://www.cds.hku.hk/prospective-students/scholarships/',
  'https://saasweb.hku.hk/',
  'https://www.dase.hku.hk/',
  'https://ece.hku.hk/study/admissions/',
  'https://mech.hku.hk/research-postgraduate/',
  'https://www.med.hku.hk/en/teaching-and-learning/postgraduate/rpg/key-info',
  'https://www.med.hku.hk/en/teaching-and-learning/postgraduate/rpg/support',
  'https://www.sbms.hku.hk/study',
  'https://www.sbms.hku.hk/research',
  'https://chemistry.hku.hk/study/postgraduate_students/1/',
  'https://chemistry.hku.hk/study/postgraduate_students/2/',
  'https://chemistry.hku.hk/study/postgraduate_students/13/',
  'https://www.earthsciences.hku.hk/education/postgraduate_students/research_postgraduates/general_information/',
  'https://www.earthsciences.hku.hk/education/postgraduate_students/research_postgraduates/how_to_apply/',
  'https://www.earthsciences.hku.hk/education/postgraduate_students/research_postgraduates/fellowships/',
  'https://www.physics.hku.hk/graduate_studies/for_prospective_students/research_postgraduate_program/',
  'https://www.scifac.hku.hk/rpg-programme/',
  'https://hkumath.hku.hk/web/prospective/p-pg-program.php',
]
out = []
for u in urls:
  h = hashlib.sha1(u.encode()).hexdigest()[:16]
  p = pathlib.Path('.cache/pages') / f'{h}.json'
  if not p.exists():
    out.append(f'=== MISSING {u} ===')
    continue
  d = json.loads(p.read_text(encoding='utf-8'))
  lines = d.get('text','').splitlines()
  fu = d.get('final_url')
  out.append(f'=== {u} -> {fu} ===')
  if 'engg.hku.hk' in u and 'Content' in lines:
    lines = lines[lines.index('Content'):]
  out.append('\n'.join(lines[:140]))
  links = [f'{l[0]} -> {l[1]}' for l in d.get('links',[]) if any(k in (l[0]+l[1]).lower() for k in ['phd','mphil','rpg','research','admiss','postgrad','dase','mat','stat','cds','neuro','bio','mech','ece','eee','civil','env','chem','phys','astro','math','fellow','scholar'])]
  out.append('KEY LINKS:\n  ' + '\n  '.join(list(dict.fromkeys(links))[:35]))
pathlib.Path('scratch/hku_dept_summary.txt').write_text('\n'.join(out), encoding='utf-8')
print('Done', len(out))
