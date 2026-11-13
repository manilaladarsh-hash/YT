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


# 1 & 2. odu--math.json | gre_general (off_topic & absence)
def m_odu_math(d):
    d["fields"]["gre_general"] = {
        "code": "Not stated",
        "value": "Not stated on the pages checked",
        "quote": "",
        "url": "https://www.odu.edu/admission/graduate/requirements",
    }


update_prog("odu--math", m_odu_math)


# 3. ohiostate--chemistry.json | english_waiver (off_topic)
def m_osu_chem(d):
    d["fields"]["english_waiver"]["quote"] = (
        "Only applicants who are citizens of, or who have received a bachelor’s degree or higher from, "
        "one of the following countries are exempt from the English proficiency requirement: Australia, "
        "Belize, the British Caribbean and British West Indies, Canada (except Quebec), England, Ghana, "
        "Guyana, Ireland, Liberia, New Zealand, Nigeria, Scotland, the United States and Wales."
    )


update_prog("ohiostate--chemistry", m_osu_chem)


# 4. ohiostate--ece.json | entry_route (off_topic)
def m_osu_ece(d):
    d["fields"]["entry_route"]["quote"] = (
        "14. I have a bachelor's degree, but not a master's degree. Can I apply directly to the PhD program? | "
        "Yes, you may apply to the direct BS to PhD program."
    )


update_prog("ohiostate--ece", m_osu_ece)


# 5. ohiostate--environment.json | entry_route (off_topic)
def m_osu_env(d):
    d["fields"]["entry_route"] = {
        "code": "Either",
        "value": "PhD applicants are considered for a Regular-admit track (with a master's) or a Direct-admit track (with a bachelor's).",
        "quote": (
            "The equivalent of a four-year bachelor's or advanced degree from an accredited college or university. | "
            "PhD applicants will be considered for either the Regular-admit Track or the Direct-admit Track. | "
            "Regular-admit Track: Upload a document providing a summary of the research done for your master’s degree."
        ),
        "url": "https://senr.osu.edu/academics/graduate/graduate-admissions",
    }


update_prog("ohiostate--environment", m_osu_env)


# 6. ohiostate--math.json | funding (off_topic)
def m_osu_math(d):
    d["fields"]["funding"] = {
        "code": "Guaranteed",
        "value": "All admitted PhD students are offered a renewable Graduate Teaching Associateship (stipend, tuition waiver, health insurance subsidy).",
        "quote": (
            "Support | All admitted PhD students are offered a Graduate Teaching Associateships (GTA) during the academic year. "
            "GTAs are renewable assuming satisfactory academic progress. | "
            "All Graduate Associateships and Fellowships come with a competitive stipend, full tuition waiver, and full health insurance subsidy."
        ),
        "url": "https://math.osu.edu/grad/future",
    }


update_prog("ohiostate--math", m_osu_math)


# 7. ohsu--datasci.json | entry_route (off_topic)
def m_ohsu_ds(d):
    d["fields"]["entry_route"] = {
        "code": "Direct from bachelor's",
        "value": "Bachelor’s degree from an accredited institution and minimum 3.0 GPA required.",
        "quote": "General requirements | Bachelor’s degree from an accredited institution",
        "url": "https://www.ohsu.edu/school-of-medicine/medical-informatics-and-clinical-epidemiology/admissions-information",
    }


update_prog("ohsu--datasci", m_ohsu_ds)


# 8. ohsu--neuro.json | entry_route (off_topic)
def m_ohsu_neuro(d):
    d["fields"]["entry_route"] = {
        "code": "Not stated",
        "value": "Not stated on the pages checked",
        "quote": "",
        "url": "https://www.ohsu.edu/school-of-medicine/neuroscience-graduate-program/application-information",
    }


update_prog("ohsu--neuro", m_ohsu_neuro)


# 10. olemiss--physics.json | gre_subject (off_topic)
def m_olemiss_phys(d):
    d["fields"]["gre_subject"]["quote"] = (
        "GRE scores (General Test required, Physics Subject Test optional)"
    )


update_prog("olemiss--physics", m_olemiss_phys)

print("Staged 8 program files for Batch 45.")
