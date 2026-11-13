import json, shutil

def stage(fn, fn_edit):
    shutil.copy(f'data/programs/{fn}', f'data/staging/programs/{fn}')
    with open(f'data/staging/programs/{fn}', encoding='utf-8') as f:
        d = json.load(f)
    fn_edit(d)
    with open(f'data/staging/programs/{fn}', 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')

def edit_cornell_bio(d):
    d['fields']['entry_route']['quote'] = (
        'A successful applicant to the Graduate School must: | '
        'have received a baccalaureate degree or its equivalent from a college or university of recognized standing'
    )
    d['fields']['entry_route']['url'] = 'https://catalog.cornell.edu/graduate-school/'
    d['fields']['entry_route']['also'] = [{
        'quote': 'matriculating students will have commonly majored in one of the many areas of biology, chemistry, or physics',
        'url': 'https://catalog.cornell.edu/programs/molecular-cell-biology-phd/'
    }]

def edit_cornell_chemeng(d):
    d['fields']['entry_route']['quote'] = (
        'Most applicants have satisfactorily completed the equivalent of the fundamental work required by an accredited curriculum in chemical engineering. '
        'Outstanding students with undergraduate majors in chemistry, materials science, microbiology, or physics are also encouraged to apply.'
    )

def edit_cornell_math(d):
    d['fields']['supervisor']['quote'] = (
        'Admission Decisions | '
        'Applications are evaluated by the Mathematics Field graduate admissions committee, which consists of about a dozen faculty.'
    )
    d['fields']['supervisor']['url'] = 'https://www.math.cornell.edu/graduate-admissions-application'

def edit_cornell_physics(d):
    d['fields']['supervisor']['quote'] = (
        'Students must form their permanent special committee before the beginning of the fifth semester.'
    )
    d['fields']['supervisor']['url'] = 'https://catalog.cornell.edu/programs/physics-phd/'

def edit_denver_sup(d):
    d['fields']['supervisor']['code'] = 'Not stated'
    d['fields']['supervisor']['value'] = 'Not stated on the page checked'
    d['fields']['supervisor']['quote'] = ''

def edit_dtu_chemeng(d):
    d['fields']['deadline']['quote'] = (
        'If you are interested in becoming a PhD student at our Department, '
        'please check out our "Vacant positions" or contact a member of faculty that works within your area of interest to discuss future possibilities.'
    )

def edit_edinburgh_mech(d):
    d['fields']['supervisor']['quote'] = (
        'Before applying, we strongly recommend that you identify and discuss your research ideas with an academic staff member that you are interested in working with. '
        'This initial contact can help with writing a research proposal and the application process. | '
        'You should include the name of your proposed supervisor in your online application.'
    )

stage('cornell--biology.json', edit_cornell_bio)
stage('cornell--chemeng.json', edit_cornell_chemeng)
stage('cornell--math.json', edit_cornell_math)
stage('cornell--physics.json', edit_cornell_physics)
stage('denver--math.json', edit_denver_sup)
stage('denver--physics.json', edit_denver_sup)
stage('dtu--chemeng.json', edit_dtu_chemeng)
stage('edinburgh--mech.json', edit_edinburgh_mech)
print("Staged 8 Batch 25 programs cleanly.")
