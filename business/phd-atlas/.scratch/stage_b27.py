import json, shutil

def stage(fn, fn_edit):
    shutil.copy(f'data/programs/{fn}', f'data/staging/programs/{fn}')
    with open(f'data/staging/programs/{fn}', encoding='utf-8') as f:
        d = json.load(f)
    fn_edit(d)
    with open(f'data/staging/programs/{fn}', 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')

def edit_fau_mech(d):
    d['fields']['supervisor']['code'] = 'Not stated'
    d['fields']['supervisor']['value'] = 'Not stated on the page checked'
    d['fields']['supervisor']['quote'] = ''

def edit_fiu_ece(d):
    d['fields']['supervisor']['quote'] = (
        'Within 12 months upon acceptance into the Ph.D. program, the student has to identify an area of research '
        'of his or her interest by contacting and being accepted by a professor willing to guide dissertation research.'
    )

def edit_fiu_neuro(d):
    d['fields']['gre_general']['quote'] = 'GRE: General test is not required for Fall 2027 applicants.'

fit_prefix = 'Please reference the \u201cProgram Specific Application requirements\u201d table below to verify GRE requirement for each graduate program. | '

def edit_fit(d):
    d['fields']['gre_general']['quote'] = fit_prefix + d['fields']['gre_general']['quote']

stage('fau--mech.json', edit_fau_mech)
stage('fiu--ece.json', edit_fiu_ece)
stage('fiu--neuro.json', edit_fiu_neuro)
stage('floridatech--astronomy.json', edit_fit)
stage('floridatech--biology.json', edit_fit)
stage('floridatech--biomed.json', edit_fit)
print("Staged 6 Batch 27 programs cleanly.")
