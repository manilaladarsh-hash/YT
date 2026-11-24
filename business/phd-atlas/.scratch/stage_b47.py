import json
import os

os.makedirs("data/staging/programs", exist_ok=True)


def update_prog(uid, mutator):
    with open(f"data/programs/{uid}.json", "r", encoding="utf-8") as f:
        d = json.load(f)
    mutator(d)
    out_path = f"data/staging/programs/{uid}.json"
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp_path, out_path)


# 2. portlandstate--chemistry.json | entry_route
def m_psu_chem(d):
    d["fields"]["entry_route"]["quote"] = (
        "NOTE: Admission to the M.S. program is not considered a typical pathway into the Ph.D. program. "
        "If a student is interested in earning a Ph.D. in Chemistry, they should apply directly to the Ph.D. program."
    )


update_prog("portlandstate--chemistry", m_psu_chem)


# 3. princeton--biology.json | supervisor
def m_pri_bio(d):
    d["fields"]["supervisor"] = {
        "code": "Not required",
        "value": "Applicants apply directly to Graduate Admission and complete three first-year laboratory rotations with different faculty advisers.",
        "quote": (
            "During the first year of graduate study, students actively carry out research with different faculty "
            "investigators and learn about their experimental strategies and approaches. Students are required to "
            "complete three laboratory rotations (approximately 8 weeks each) with different faculty advisers, "
            "and have the option of performing an additional rotation the summer before entering graduate school."
        ),
        "url": "https://molbio.princeton.edu/graduate/requirements",
    }


update_prog("princeton--biology", m_pri_bio)


# 4. princeton--materials.json | gre_general
def m_pri_mat(d):
    d["fields"]["gre_general"]["quote"] = "GRE | General Test - Optional/Not Required"


update_prog("princeton--materials", m_pri_mat)


# 5. princeton--math.json | gre_general
def m_pri_math(d):
    d["fields"]["gre_general"]["quote"] = (
        "GREs - Math Subject Test - Optional but highly recommended "
        "(Months offered: September, October, April) and General Test - Optional (not required)."
    )


update_prog("princeton--math", m_pri_math)


# 6. princeton--mech.json | gre_general
def m_pri_mech(d):
    d["fields"]["gre_general"]["quote"] = "GRE | General Test - Not Accepted"


update_prog("princeton--mech", m_pri_mech)


# 7. qmul--biomed.json | deadline
def m_qmul_biomed(d):
    d["fields"]["deadline"]["quote"] = (
        "Deadlines for funded studentships | "
        "Medicine and Dentistry studentships: various (please check the advert for project)"
    )


update_prog("qmul--biomed", m_qmul_biomed)


# 8 & 9. qmul--bme.json | deadline & funding
def m_qmul_bme(d):
    d["fields"]["deadline"]["quote"] = (
        "Deadlines for funded studentships | "
        "Other Science and Engineering Studentships: various (please check the advert for the project)"
    )
    d["fields"]["funding"] = {
        "code": "Competitive",
        "value": "Studentships are usually fully funded (tuition and stipend) but are limited, and applicants are advised to apply early.",
        "quote": (
            "PhD Research Studentships | We offer studentships in a range of categories. "
            "These are usually fully-funded, with a stipend and tuition fee covered. | "
            "Please apply early in order to check your eligibility and to improve your chances of selection."
        ),
        "url": "https://www.sems.qmul.ac.uk/research/studentships/",
    }


update_prog("qmul--bme", m_qmul_bme)


# 10. qmul--chemeng.json | deadline
def m_qmul_chemeng(d):
    d["fields"]["deadline"]["quote"] = (
        "Deadlines for funded studentships | "
        "Other Science and Engineering Studentships: various (please check the advert for the project)"
    )


update_prog("qmul--chemeng", m_qmul_chemeng)

print("Staged 8 program files for Batch 47.")
