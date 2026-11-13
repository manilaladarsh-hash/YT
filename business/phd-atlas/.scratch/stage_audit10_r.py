import json
import pathlib

SRC = pathlib.Path("data/programs")
DST = pathlib.Path("data/staging/programs")
DST.mkdir(parents=True, exist_ok=True)


def load(name):
    return json.loads((SRC / f"{name}.json").read_text(encoding="utf-8"))


def save(name, d):
    (DST / f"{name}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# 1. berkeley--chemeng: gre_general
d = load("berkeley--chemeng")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["quote"] = (
    "The faculty of the Department of Chemical and Biomolecular Engineering (CBE) at UC Berkeley have determined the Graduate Records Exam (GRE) "
    "is a proven identifier of race and socio-economic status. Its association with successful completion of the doctorate is minimal, and its fulfillment "
    "is an economic burden on applicants. CBE will no longer consider it for admission."
)
save("berkeley--chemeng", d)

# 2. berkeley--neuro: english_waiver
d = load("berkeley--neuro")
d["checked"] = "2026-11-12"
d["fields"]["english_waiver"]["quote"] = (
    "Evidence of English Language Proficiency: All applicants who have completed a basic degree in a country/region in which the official language "
    "is not English are required to submit official evidence of English language proficiency: the Test of English as a Foreign Language (TOEFL), "
    "or the International English Language Testing System (IELTS). This requirement applies to institutions from Bangladesh, Nepal, India, Pakistan"
)
save("berkeley--neuro", d)

# 3. bgsu--datasci: funding
d = load("bgsu--datasci")
d["checked"] = "2026-11-12"
d["fields"]["funding"]["quote"] = (
    "Opportunities for graduate assistantships for the doctorate in data science – with scholarships and stipend – are granted on a competitive basis."
)
save("bgsu--datasci", d)

# 4. boise--biomed: fee_waiver
d = load("boise--biomed")
d["checked"] = "2026-11-12"
d["fields"]["fee_waiver"]["quote"] = (
    "A limited number of application fee waivers are available for qualified Ph.D. applicants. | "
    "Eligibility for a fee waiver: | "
    "Domestic applicant (citizen or lawful permanent resident of the United States)"
)
save("boise--biomed", d)

# 5. bonn-cologne--physics: supervisor
d = load("bonn-cologne--physics")
d["checked"] = "2026-11-12"
d["fields"]["supervisor"]["quote"] = (
    d["fields"]["supervisor"]["quote"]
    + " | PhD: No deadline (start possible at any time; individual arrangement with the supervisor)"
)
save("bonn-cologne--physics", d)

# 6. bostonu--astronomy: supervisor
d = load("bostonu--astronomy")
d["checked"] = "2026-11-12"
d["fields"]["supervisor"]["quote"] = (
    "During the first academic year, students generally concentrate on coursework; a research area is usually chosen during the first or second year. | "
    "An Astronomy graduate student traditionally has two faculty advisors: the Director of Graduate Studies and a research advisor."
)
save("bostonu--astronomy", d)

# 7. brandeis--biology: supervisor + broken apply-phd.html redirect updates
d = load("brandeis--biology")
d["checked"] = "2026-11-12"
d["program_page"] = "https://www.brandeis.edu/molecular-cell-biology/graduate/phd-program/index.html"
d["fields"]["gre_general"] = {
    "code": "Optional",
    "value": "Submission of GRE scores is optional per Brandeis Graduate Admissions PhD requirements (old MCB apply-phd URL now redirects).",
    "quote": "GRE (Optional) | Submission of GRE scores is entirely optional.",
    "url": "https://www.brandeis.edu/graduate-admissions/apply/phd.html",
}
d["fields"]["gre_subject"] = {
    "code": "No subject test",
    "value": "No GRE Subject Test exists for biology; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
    "quote": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
    "url": "https://www.ets.org/gre/score-users/about/subject-tests.html",
}
d["fields"]["supervisor"] = {
    "code": "Not required",
    "value": "Faculty members cannot accept students directly into labs before admission; all MCB PhD students complete four rotations in year 1 before choosing a dissertation lab.",
    "quote": "Faculty members cannot accept graduate students directly into their labs prior to acceptance into the program. All MCB PhD students must complete four research rotations in their first year before choosing a dissertation lab.",
    "url": "https://www.brandeis.edu/molecular-cell-biology/graduate/phd-program/faqs.html",
}
save("brandeis--biology", d)

# 8-10. bristol--civil, bristol--ece, bristol--mech: supervisor
for name in ("bristol--civil", "bristol--ece", "bristol--mech"):
    d = load(name)
    d["checked"] = "2026-11-12"
    d["fields"]["supervisor"]["quote"] = (
        "This form should be completed in collaboration with a University of Bristol supervisor. "
        "We will not be able to proceed with your application until we have received a completed copy of this document."
    )
    save(name, d)

print("Staged 10 files for Batch 18")
