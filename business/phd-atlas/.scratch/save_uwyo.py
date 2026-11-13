import os
import sys

os.environ["ATLAS_OUT"] = "data/staging"
sys.path.insert(0, "scripts")
from rec import save_university, save_program

ETS_GENERAL_URL = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_GENERAL_QUOTE = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

ETS_CHEM_URL = "https://www.ets.org/gre/test-takers/subject-tests/scores.html"
ETS_CHEM_QUOTE = "The GRE Chemistry Test was discontinued in May 2023."

ADM_URL = "https://uwyo.catalog.acalog.com/content.php?catoid=19&navoid=2018"
BMS_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20502"
ENTITY_URL = "https://uwyo.catalog.acalog.com/preview_entity.php?catoid=19&ent_oid=3180"
POLICIES_URL = "https://uwyo.catalog.acalog.com/content.php?catoid=19&navoid=2054"

# 1. Save University
save_university("uwyo", "University of Wyoming", "USA", "Wyoming", ADM_URL, {
    "app_fee": ("Not stated", "Applicants must submit the required nonrefundable application fee; fee amount is not stated in the catalog admissions section.", "Applicants must complete the UW graduate application and submit the required nonrefundable application fee.", ADM_URL),
    "fee_waiver": ("Not stated", "No application fee waiver policy was found on the official catalog admissions pages.", "", ADM_URL),
    "gre_general": ("Not stated", "The Graduate School does not set a general GRE requirement; standardized tests are required only if specified by the individual academic department.", "Applicants whose department requires the Graduate Record Examination (GRE) must request official scores be sent directly to the Admissions Office via the Educational Testing Service (ETS), using the University of Wyoming’s institution code: 4855.", ADM_URL),
    "toefl_min": ("76", "The University of Wyoming requires a minimum TOEFL score of 76 iBT for international graduate admission.", "The minimum acceptable scores are 540 (76 iBT) and 6.5 for TOEFL and IELTS respectively.", BMS_URL),
    "ielts_min": ("6.5", "The University of Wyoming requires a minimum IELTS Academic score of 6.5 for international graduate admission.", "The minimum acceptable scores are 540 (76 iBT) and 6.5 for TOEFL and IELTS respectively.", BMS_URL),
    "english_waiver": ("Conditional", "Proof of English proficiency is required if native language is not English; a variety of proficiency exams are accepted.", "Provide proof of English proficiency if student’s native language is not English. The University of Wyoming accepts a variety of English proficiency exams.", ADM_URL)
}, checked="2026-10-29")

print("Saved uwyo university record.")

# Helper defaults
DEADLINE_QUOTE = "The priority deadline for students entering in the fall is March 1."
SUPERVISOR_QUOTE = "It is the responsibility of the graduate student, in consultation with their major advisor (usually the Committee Chair) to form a viable committee within the first two semesters of their graduate program."
FUNDING_QUOTE = "Graduate Assistantships: Many graduate programs offer assistantships, which provide tuition benefits and stipends to eligible students."
ENTRY_QUOTE = "Students wishing to pursue direct entry into a doctoral program following their bachelor’s degree | The requirements for entry into a doctoral program are determined by the departmental faculty. In some cases, students may enter"

def dline():
    return ("2027-03-01", "The priority deadline for students entering in the fall is March 1.", DEADLINE_QUOTE, ENTITY_URL, {"inferred": "year"})

def fund():
    return ("Typical", "Many graduate programs offer assistantships, which provide tuition benefits and stipends to eligible students.", FUNDING_QUOTE, ADM_URL)

def sup():
    return ("Not required", "Students form their advisory committee in consultation with their advisor during the first two semesters.", SUPERVISOR_QUOTE, POLICIES_URL)

def entry_either():
    return ("Either", "Requirements for entry into a doctoral program are determined by departmental faculty; in some cases students enter directly following a bachelor's degree.", ENTRY_QUOTE, POLICIES_URL)

def no_sub(field_name):
    if field_name == "Chemistry":
        return ("No subject test", "No GRE Subject Test exists for this field: ETS discontinued the GRE Chemistry Test in May 2023.", ETS_CHEM_QUOTE, ETS_CHEM_URL)
    return ("No subject test", "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.", ETS_GENERAL_QUOTE, ETS_GENERAL_URL)

# 1. Physics
PHYS_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20350"
save_program("uwyo", "physics", "Department of Physics and Astronomy", PHYS_URL, {
    "deadline": dline(),
    "gre_subject": ("Not stated", "Not stated on the catalog program page.", "", PHYS_URL),
    "supervisor": sup(),
    "funding": fund(),
    "entry_route": entry_either()
})

# 2. Chemistry
CHEM_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20264"
save_program("uwyo", "chemistry", "Department of Chemistry", CHEM_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Chemistry"),
    "supervisor": sup(),
    "funding": fund(),
    "entry_route": entry_either()
})

# 3. Math
MATH_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20328"
save_program("uwyo", "math", "Department of Mathematics and Statistics", MATH_URL, {
    "deadline": dline(),
    "gre_subject": ("Not stated", "Not stated on the catalog program page.", "", MATH_URL),
    "supervisor": sup(),
    "funding": fund(),
    "entry_route": entry_either()
})

# 4. CS
CS_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20454"
save_program("uwyo", "cs", "Department of Electrical Engineering and Computer Science", CS_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Computer Science"),
    "supervisor": sup(),
    "funding": fund(),
    "entry_route": entry_either()
})

# 5. ECE
ECE_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20463"
save_program("uwyo", "ece", "Department of Electrical Engineering and Computer Science", ECE_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Electrical Engineering"),
    "supervisor": sup(),
    "funding": fund(),
    "entry_route": entry_either()
})

# 6. Mech
MECH_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20468"
save_program("uwyo", "mech", "Department of Mechanical Engineering", MECH_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Mechanical Engineering"),
    "supervisor": sup(),
    "funding": fund(),
    "entry_route": entry_either()
})

# 7. ChemEng
CHE_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20437"
save_program("uwyo", "chemeng", "Department of Chemical and Biomedical Engineering", CHE_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Chemical Engineering"),
    "supervisor": sup(),
    "funding": fund(),
    "entry_route": ("Direct from bachelor's", "A master's degree is not required to enter a Ph.D. program.", "A master’s degree is not required to enter a Ph.D. program.", CHE_URL)
})

# 8. Civil
CIV_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20443"
save_program("uwyo", "civil", "Department of Civil and Architectural Engineering", CIV_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Civil Engineering"),
    "supervisor": sup(),
    "funding": fund(),
    "entry_route": entry_either()
})

# 9. Earth
EARTH_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20298"
save_program("uwyo", "earth", "Department of Geology and Geophysics", EARTH_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Geosciences"),
    "supervisor": sup(),
    "funding": fund(),
    "entry_route": entry_either()
})

# 10. Biomed
save_program("uwyo", "biomed", "School of Graduate Education", BMS_URL, {
    "deadline": ("2027-02-15", "To ensure full application review for fall semester admission, applications should be received by February 15.", "To ensure full application review for fall semester admission, applications should be received by February 15.", BMS_URL, {"inferred": "year"}),
    "gre_subject": no_sub("Biomedical Sciences"),
    "supervisor": ("Required", "A letter of sponsorship from a faculty member is required as part of the application.", "Submit your application materials (pdf files of cover letter/statement of purpose, letter of sponsorship from the faculty, three letters of recommendation", BMS_URL),
    "funding": fund(),
    "entry_route": ("Direct from bachelor's", "Successful completion of a bachelor's degree from an accredited institution is required for admission.", "Successful completion of a bachelor’s degree from an accredited institution with one or more semesters of", BMS_URL)
}, name="Biomedical Sciences")

# 11. Neuro
NEURO_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20505"
save_program("uwyo", "neuro", "Graduate Neuroscience Program", NEURO_URL, {
    "deadline": dline(),
    "gre_general": ("Optional", "GRE scores are accepted but not required.", "GRE: Accepted but not required;", NEURO_URL),
    "gre_subject": ("Optional", "GRE scores are accepted but not required.", "GRE: Accepted but not required;", NEURO_URL),
    "supervisor": ("Required", "A student is expected to have a graduate adviser at all times, who must be a participating member of the Neuroscience faculty.", "A student is expected to have a graduate adviser at all times. The faculty adviser must be a participating member of the Neuroscience faculty", NEURO_URL),
    "funding": fund(),
    "entry_route": ("Direct from bachelor's", "A bachelor's degree in a biological science from an accredited institution is required.", "Bachelor’s degree in a biological science from an accredited institution;", NEURO_URL)
}, name="Neuroscience")

# 12. Environment
save_program("uwyo", "environment", "Program in Ecology and Evolution", PIE_URL := "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20503", {
    "deadline": dline(),
    "gre_subject": no_sub("Ecology and Evolution"),
    "supervisor": ("Required", "Agreement by a member of the PiE2 faculty to sponsor or co-sponsor the student is required for admission.", "Agreement by a member of the PiE2 faculty to sponsor the student, or to co-sponsor the student together with a PiE2 affiliate", PIE_URL),
    "funding": fund(),
    "entry_route": entry_either()
}, name="Ecology and Evolution")

# 13. Biology
BIO_URL = "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20388"
save_program("uwyo", "biology", "Department of Zoology and Physiology", BIO_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Biology"),
    "supervisor": sup(),
    "funding": fund(),
    "entry_route": entry_either()
})

print("Saved all 13 UWYO programs to data/staging/programs/.")
