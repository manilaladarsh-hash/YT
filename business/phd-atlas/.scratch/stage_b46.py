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


# 1. oregonstate--materials.json | funding
def m_orst_mat(d):
    d["fields"]["funding"]["quote"] = (
        "All students, regardless of domestic/international status, are eligible to be awarded "
        "a graduate research assistantship (GRA) and/or graduate teaching assistantships (GTA) "
        "position, however it is very competitive."
    )


update_prog("oregonstate--materials", m_orst_mat)


# 2. oregonstate--math.json | entry_route
def m_orst_math(d):
    d["fields"]["entry_route"]["quote"] = (
        "If you have a Master's degree in mathematics, you should apply to the PhD program "
        "(OSU's Office of Graduate Education discourages a second Master's degree in the same field). "
        "If you do not have a Master's degree in mathematics, you should consider your long-term "
        "career goals as well as your preparation. If you are unsure about these, then your fit "
        "is better for the Master's. If you are sure, and your application demonstrates this, apply to the PhD program."
    )


update_prog("oregonstate--math", m_orst_math)


# 4. paris-saclay--chemistry.json | supervisor
def m_ps_chem(d):
    d["fields"]["supervisor"]["quote"] = (
        "Submission of subject proposals by the supervisors (HDR) | "
        "Student applications on topics published by ED | "
        "Except in special cases, the supervision of a thesis will be entrusted to researchers "
        "or teaching researchers with a supervising authorization (HDR)"
    )
    d["fields"]["supervisor"].pop("also", None)


update_prog("paris-saclay--chemistry", m_ps_chem)


# 5. paris-saclay--cs.json | supervisor
def m_ps_cs(d):
    d["fields"]["supervisor"]["quote"] = (
        "Finding a doctoral project requires finding a thesis director who is the bearer of a project. | "
        "The candidate applies for a project using ADUM. It is essential that the application be preceded "
        "by a direct contact with the thesis project leader and then, in the case of the concretization "
        "of the application, by a meeting with him/her."
    )


update_prog("paris-saclay--cs", m_ps_cs)


# 6 & 7. paris-saclay--ece.json | supervisor & entry_route
def m_ps_ece(d):
    d["fields"]["supervisor"]["quote"] = (
        "An application is considered complete if : | "
        "i) Submission of the application via ADUM by the candidate is complete | "
        "ii) And if at least one favorable opinion of the thesis supervisor has been formulated from the ADUM space | "
        "iii) And if at least one contact (by phone or in person) has taken place between the candidate and the supervisor."
    )
    d["fields"]["supervisor"].pop("also", None)
    d["fields"]["entry_route"]["quote"] = (
        "Q6) I have no european Master degree. Can I yet apply to PhD in Paris-Saclay? | "
        "R6) YES, for sure. The doctoral school will just check additional points from the information given by the PhD supervisor."
    )


update_prog("paris-saclay--ece", m_ps_ece)


# 8. paris-saclay--math.json | supervisor (expand quote for clarity + review in CSV)
def m_ps_math(d):
    d["fields"]["supervisor"]["quote"] = (
        "There are 4 aspects to a thesis project: a doctoral student, a thesis director, a research topic, "
        "and funding secured for 3 years. The first step for a student is to find a thesis director, "
        "and a research topic in a field that interests him or her."
    )


update_prog("paris-saclay--math", m_ps_math)

print("Staged 6 program files for Batch 46.")
