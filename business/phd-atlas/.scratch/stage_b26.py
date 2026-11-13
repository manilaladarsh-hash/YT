import json, shutil

def stage(fn, fn_edit):
    shutil.copy(f'data/programs/{fn}', f'data/staging/programs/{fn}')
    with open(f'data/staging/programs/{fn}', encoding='utf-8') as f:
        d = json.load(f)
    fn_edit(d)
    with open(f'data/staging/programs/{fn}', 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')

def edit_epfl_civil(d):
    d['fields']['gre_general']['quote'] = (
        'Are the TOEFL and GRE certificates mandatory? | '
        'They are not obligatory, but you must be aware that all courses are held in English '
        'and that a good level of English is required for your thesis work.'
    )

def edit_epfl_mech(d):
    d['fields']['gre_general']['quote'] = (
        'Are TOEFL and GRE certificates obligatory? | '
        'They are not obligatory, but you must be aware that all courses are held in English '
        'and that an excellent level of English is required for your thesis work.'
    )

def edit_ethz_neuro(d):
    d['fields']['deadline']['quote'] = (
        'Until further notice we do not recruit PhD students via the Life Science Zurich Graduate School '
        'online application portal (Track 1). | '
        'Track II (Direct Application via ZNZ Group Leader) | '
        'You can contact ZNZ group leaders directly to enquire about PhD openings and apply to the group of your choice (Track II).'
    )

def edit_fau_chem(d):
    d['fields']['entry_route']['quote'] = (
        'No. Although an undergraduate degree in chemistry is recommended we accept students who have obtained degrees in other disciplines. | '
        'Therefore, if you applied to the Ph.D. program and instead were offered a place in the M.S. degree program, '
        'it means that your credentials were assessed as not strong enough for direct entry into the Ph.D.'
    )

def edit_fau_eecs(d):
    d['fields']['funding']['quote'] = (
        'Graduate teaching assistantships are provided for eligible EECS graduate students with a 3.4 GPA, '
        'with a priority given to new doctoral students, new BS to PhD Direct-Path program students, '
        'and incoming joint BS/MS degree program students. | '
        'The TA Committee makes the final selection after all required documentation has been reviewed'
    )

stage('epfl--civil.json', edit_epfl_civil)
stage('epfl--mech.json', edit_epfl_mech)
stage('ethz--neuro.json', edit_ethz_neuro)
stage('fau--chemistry.json', edit_fau_chem)
stage('fau--cs.json', edit_fau_eecs)
stage('fau--ece.json', edit_fau_eecs)
print("Staged 6 Batch 26 programs cleanly.")
