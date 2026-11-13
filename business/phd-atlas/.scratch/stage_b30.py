import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
PROGS = ROOT / "data" / "programs"
STAGING = ROOT / "data" / "staging" / "programs"
STAGING.mkdir(parents=True, exist_ok=True)


def load_prog(name):
    return json.loads((PROGS / name).read_text(encoding="utf-8"))


def save_staged(name, data):
    (STAGING / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# 1. fsu--math.json (supervisor)
fsu_math = load_prog("fsu--math.json")
fsu_math["fields"]["supervisor"] = {
    "code": "Not required",
    "value": (
        "Applicants apply to a research area whose admissions committee decides admission; "
        "a dissertation committee and primary advisor are appointed later before the candidacy exam."
    ),
    "quote": (
        "Each major has its own admissions committee, required and elective courses, and qualifier requirements. | "
        "Before taking the candidacy exam, the student will have a dissertation committee appointed."
    ),
    "url": "https://mathematics.fsu.edu/graduate/graduate-handbook",
    "also": [
        {
            "quote": "Admission and funding decisions are made by areas.",
            "url": "https://www.math.fsu.edu/apply/",
        }
    ],
}
save_staged("fsu--math.json", fsu_math)

# 2. georgiatech--ece.json (funding)
gt_ece = load_prog("georgiatech--ece.json")
gt_ece["fields"]["funding"]["quote"] = (
    "I need help funding my education, how can I obtain a graduate teaching assistantship (GTA) "
    "or graduate research assistantship (GRA)? | "
    "Most applicants admitted to the Atlanta campus Ph.D. program will receive a GTA or GRA offer. "
    "This will be noted in your acceptance letter."
)
save_staged("georgiatech--ece.json", gt_ece)

# 3. georgiatech--physics.json (entry_route)
gt_phys = load_prog("georgiatech--physics.json")
gt_phys["fields"]["entry_route"]["quote"] = (
    "If your career plan is to do Research, you should apply directly to the Ph.D. program – not the MS Program. "
    "Almost all students directly enter a Ph.D. program after earning their BS degree."
)
save_staged("georgiatech--physics.json", gt_phys)

# 4. gmu--chemistry.json (supervisor)
gmu_chem = load_prog("gmu--chemistry.json")
gmu_chem["fields"]["supervisor"] = {
    "code": "Not required",
    "value": (
        "Admission is by departmental evaluation; upon acceptance students are assigned an academic advisor "
        "and are expected to select a dissertation/research supervisor by the end of the first year."
    ),
    "quote": (
        "Upon acceptance into the Chemistry and Biochemistry, PhD, a student will be assigned an academic advisor. | "
        "By the end of the first year, a student in the program is expected to have selected a dissertation/research "
        "supervisor and to have formed the dissertation committee."
    ),
    "url": "https://catalog.gmu.edu/colleges-schools/science/chemistry-biochemistry/chemistry-biochemistry-phd/",
    "also": [
        {
            "quote": (
                "Admission is based on a departmental evaluation of the applicant's background as evidenced by "
                "transcripts, résumés, and letters of recommendation."
            ),
            "url": "https://science.gmu.edu/academics/departments-units/chemistry-biochemistry/graduate-programs/admission-application",
        }
    ],
}
save_staged("gmu--chemistry.json", gmu_chem)

# 5. gmu--physics.json (funding)
gmu_phys = load_prog("gmu--physics.json")
gmu_phys["fields"]["funding"]["quote"] = (
    "Most first-year students who need financial support request a Graduate Teaching Assistant (GTA) position. "
    "These are offered on a competitive basis subject to departmental needs."
)
save_staged("gmu--physics.json", gmu_phys)

# 6. goettingen--biology.json (supervisor)
goet_bio = load_prog("goettingen--biology.json")
goet_bio["fields"]["supervisor"]["quote"] = (
    "Make sure to include a statement by the faculty member who is interested in your application and may be able "
    "to offer you a PhD position, including details on funding and a preliminary project title. "
    "Important: without this statement, we will not be able to process your application."
)
save_staged("goettingen--biology.json", goet_bio)

# 7 & 8. goettingen--chemistry.json (supervisor & english_waiver)
goet_chem = load_prog("goettingen--chemistry.json")
goet_chem["fields"]["supervisor"] = {
    "code": "Required",
    "value": "Before admission you need confirmation of supervision from a supervisor in the doctoral programme in chemistry for the doctoral project.",
    "quote": "Confirmation of supervision by a supervisor in the doctoral programme in chemistry for the doctoral project",
    "url": "https://www.uni-goettingen.de/en/659322.html",
}
goet_chem["fields"]["english_waiver"] = {
    "code": "Yes",
    "value": "English is not tested if your bachelor's was taught in English; an English-medium bachelor's from India therefore meets the English rule.",
    "quote": "If your native language or the language of your Bachelor's degree programme is not English , you must prove sufficient knowledge of the English language at the level C1 GER",
    "url": "https://www.uni-goettingen.de/en/659322.html",
    "also": [
        {
            "quote": "If your native language or the language of your Bachelor's programme is not German , you must prove sufficient knowledge of the German language at the level DSH-2 or comparable",
            "url": "https://www.uni-goettingen.de/en/659322.html",
        }
    ],
}
save_staged("goettingen--chemistry.json", goet_chem)

# 9. hamburg--biomed.json (deadline)
ham_bio = load_prog("hamburg--biomed.json")
ham_bio["fields"]["deadline"] = {
    "code": "Rolling",
    "value": "You can apply for admission on an ongoing basis, but check the committee's submission deadlines on the website.",
    "quote": (
        "You can apply for admission on an ongoing basis. "
        "Please note the deadlines for submitting applications to the doctoral committee on the website."
    ),
    "url": "https://www.uke.de/english/research/promotion-phd-habilitation/phd-program-non-medicine/index.html",
}
save_staged("hamburg--biomed.json", ham_bio)

print("Staged 8 program files for Batch 30.")
