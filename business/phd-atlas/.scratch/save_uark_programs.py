import os
import sys

# Ensure rec.py finds data/staging
os.environ["ATLAS_OUT"] = "data/staging"
sys.path.insert(0, "scripts")
from rec import save_program

ETS_GENERAL_URL = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_GENERAL_QUOTE = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

ETS_CHEM_URL = "https://www.ets.org/gre/test-takers/subject-tests/scores.html"
ETS_CHEM_QUOTE = "The GRE Chemistry Test was discontinued in May 2023."

ADM_URL = "https://catalog.uark.edu/graduatecatalog/admissions/"
DEADLINE_QUOTE = "The recommended deadline for fall semester graduate assistantship consideration is Feb. 1, although departments/programs may have earlier deadlines."
FUND_URL = "https://graduate-students.uark.edu/admissions/"
FUND_QUOTE = "Graduate Assistant Positions: All graduate assistants receive a monthly stipend, and | most cover the cost of tuition."

def dline():
    return ("2027-02-01", "Recommended deadline for Fall graduate assistantship consideration is February 1.", DEADLINE_QUOTE, ADM_URL, {"inferred": "year"})

def fund():
    return ("Competitive", "Graduate assistantships include a monthly stipend and tuition coverage, awarded on a competitive basis.", FUND_QUOTE, FUND_URL)

def no_sub(field_name):
    if field_name == "Chemistry":
        return ("No subject test", "No GRE Subject Test exists for this field: ETS discontinued the GRE Chemistry Test in May 2023.", ETS_CHEM_QUOTE, ETS_CHEM_URL)
    return ("No subject test", "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.", ETS_GENERAL_QUOTE, ETS_GENERAL_URL)

# 1. Physics
P_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/physicsphys/"
save_program("uark", "physics", "Department of Physics", P_URL, {
    "deadline": dline(),
    "gre_general": ("Not required", "Submission of GRE scores is not required for admission.", "While submission of Graduate Record Examination scores is not required for admission, students who have taken the GRE advanced physics test are urged to submit their test scores to the physics department to facilitate advising and placement.", P_URL),
    "gre_subject": ("Optional", "Submission of the GRE advanced physics test is not required for admission but urged to facilitate advising and placement.", "While submission of Graduate Record Examination scores is not required for admission, students who have taken the GRE advanced physics test are urged to submit their test scores to the physics department to facilitate advising and placement.", P_URL),
    "supervisor": ("Not required", "Incoming graduate students are advised by a departmental graduate adviser for the first two years.", "Incoming graduate students will be advised by a departmental graduate adviser for the first two years.", P_URL),
    "funding": fund(),
    "entry_route": ("Direct from bachelor's", "The doctoral degree requires 72 graduate credit hours beyond the bachelor's degree.", "The doctoral degree will be awarded to students who complete a minimum of 72-graduate semester credit hours beyond the bachelor's degree.", P_URL)
})

# 2. Math
M_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/mathematicalsciencesdepartmentofmasc/"
save_program("uark", "math", "Department of Mathematical Sciences", M_URL, {
    "deadline": dline(),
    "gre_subject": ("Not stated", "The department does not state a GRE subject test policy on the catalog page.", "", M_URL),
    "supervisor": ("Not stated", "Not stated on the catalog page.", "", M_URL),
    "funding": fund(),
    "entry_route": ("Direct from bachelor's", "Candidates earn not less than 60 semester hours of course credit beyond the bachelor's degree.", "Candidates for the degree of Doctor of Philosophy with a major in mathematics will be required to earn not less than 60 semester hours of course credit beyond the bachelor's degree in mathematics and closely related fields.", M_URL)
})

# 3. CS
CS_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/computerscienceandcomputerengineeringcsce/"
save_program("uark", "cs", "Department of Computer Science and Computer Engineering", CS_URL, {
    "deadline": dline(),
    "gre_general": ("Required", "Applicants must have satisfactory GRE scores.", "Have satisfactory GRE (Graduate Record Examination) scores;", CS_URL),
    "gre_subject": no_sub("Computer Science"),
    "supervisor": ("Not stated", "Not stated on the catalog page.", "", CS_URL),
    "funding": fund(),
    "entry_route": ("Direct from bachelor's", "Applicants should have a Bachelor of Science degree in computer engineering or computer science.", "Applicants to the Doctor of Philosophy degree with a concentration in computer engineering program should have a Bachelor of Science degree in computer engineering.", CS_URL)
})

# 4. Chemistry
C_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/chemistryandbiochemistrychbcdepartmentof/"
save_program("uark", "chemistry", "Department of Chemistry and Biochemistry", C_URL, {
    "deadline": dline(),
    "gre_general": ("Required", "Official scores from the GRE General Test are required.", "official scores from the Graduate Record Examination (General Test). Advanced subject GRE tests scores (Chemistry, Biochemistry, etc.) are encouraged but not required.", C_URL),
    "gre_subject": no_sub("Chemistry"),
    "supervisor": ("Not stated", "Not stated on the catalog page.", "", C_URL),
    "funding": fund(),
    "entry_route": ("Not stated", "Not stated on the catalog page.", "", C_URL)
})

# 5. Biology
B_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/biologicalsciencesbisc/"
save_program("uark", "biology", "Department of Biological Sciences", B_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Biology"),
    "supervisor": ("Not stated", "Not stated on the catalog page.", "", B_URL),
    "funding": fund(),
    "entry_route": ("Either", "Students may enter the Ph.D. program with or without a master's degree (72 hours without, 42 hours beyond master's).", "students complete a minimum of 72 graduate semester hours if entering the Ph.D. program without a master's degree, or 42 graduate semester hours beyond the master's degree.", B_URL)
})

# 6. Biomed
BM_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/cellandmolecularbiologycemb/"
save_program("uark", "biomed", "Cell and Molecular Biology Program", BM_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Cell and Molecular Biology"),
    "supervisor": ("Not required", "Students complete rotations before obtaining a faculty research sponsor.", "ology faculty designated for the rotation have agreed to host the student during this period. | After the rotation period, the student must obtain a faculty research sponsor.", BM_URL),
    "funding": fund(),
    "entry_route": ("Either", "Students may enter directly from a bachelor's or bypass the M.S. for a Ph.D.", "Students wishing to bypass the M.S. for a Ph.D. must complete the same 24 hours of course work in Cell and Molecular Biology-approved course work as for the M.S. degree, plus a minimum of 18 hours of dissertation research.", BM_URL)
}, name="Cell and Molecular Biology")

# 7. Materials
MAT_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/materialsengineeringmate/"
save_program("uark", "materials", "Materials Science and Engineering Program", MAT_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Materials Science and Engineering"),
    "supervisor": ("Not stated", "Not stated on the catalog page.", "", MAT_URL),
    "funding": fund(),
    "entry_route": ("Master's usually required", "Candidates for the Ph.D. program are expected to have completed a Master of Science degree in either engineering or science.", "Candidates for the Ph.D. program are expected to have completed a Master of Science degree in either engineering or science.", MAT_URL)
}, name="Materials Science and Engineering")

# 8. Earth
E_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/geosciencesdepartmentofgeos/"
save_program("uark", "earth", "Department of Geosciences", E_URL, {
    "deadline": dline(),
    "gre_general": ("Required", "GRE scores (Verbal, Quantitative, and Writing) will be reviewed on a competitive basis by the admissions committee.", "Undergraduate and graduate GPA as well as GRE (Verbal, Quantitative, and Writing) will be reviewed on a competitive basis by the Geosciences Ph.D. admissions committee", E_URL),
    "gre_subject": no_sub("Geosciences"),
    "supervisor": ("Not stated", "Not stated on the catalog page.", "", E_URL),
    "funding": fund(),
    "entry_route": ("Either", "Qualified students with a bachelor's degree or a master's degree may be accepted into the Ph.D. program.", "Qualified students with a bachelor's degree or a master's degree may be accepted into the Ph.D. program.", E_URL)
})

# 9. Environment
ENV_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/environmentaldynamicsendy/"
save_program("uark", "environment", "Environmental Dynamics Program", ENV_URL, {
    "deadline": dline(),
    "gre_general": ("Recommended", "GRE scores are not required but are strongly encouraged.", "GRE scores are not required but are strongly encouraged.", ENV_URL),
    "gre_subject": no_sub("Environmental Dynamics"),
    "supervisor": ("Not required", "During the first semester of study, all students will be assigned an advisory committee.", "During the first semester of study, all students will be assigned an advisory committee to determine the student’s particular program plan.", ENV_URL),
    "funding": fund(),
    "entry_route": ("Either", "Applicants should hold a bachelor's or master's degree in a discipline with an environmental focus.", "Requirements for Admission: Applicants should hold a bachelor's or master's degree in a discipline with an environmental focus.", ENV_URL)
}, name="Environmental Dynamics")

# 10. ECE
ECE_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/electricalengineeringeleg/"
save_program("uark", "ece", "Department of Electrical Engineering", ECE_URL, {
    "deadline": dline(),
    "gre_general": ("Required", "GRE is required; waiver is available only for students with an ABET-accredited B.S. degree and high GPA.", "Students who are applying for the Ph.D. E.E. degree may have the GRE requirement waived providing the student obtained a B.S. degree from an ABET-Accredited program", ECE_URL),
    "gre_subject": no_sub("Electrical Engineering"),
    "supervisor": ("Not stated", "Not stated on the catalog page.", "", ECE_URL),
    "funding": fund(),
    "entry_route": ("Either", "Students may enter with a bachelor's degree (36 hours coursework) or with an M.S. degree (minimum additional 12 hours graded coursework).", "A student entering the Ph.D. program with an M.S. degree will be required to complete a minimum of an additional 12 hours of graded coursework", ECE_URL)
})

# 11. Mech
MECH_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/mechanicalengineeringmeeg/"
save_program("uark", "mech", "Department of Mechanical Engineering", MECH_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Mechanical Engineering"),
    "supervisor": ("Not stated", "Not stated on the catalog page.", "", MECH_URL),
    "funding": fund(),
    "entry_route": ("Direct from bachelor's", "After the B.S.M.E. degree or its equivalent, study includes 42 hours of graded coursework and 30 hours of dissertation.", "After the B.S.M.E. degree or its equivalent, the student's Schedule of Study must include 42 hours of graded coursework and 30 hours of MEEG 7000V", MECH_URL)
})

# 12. ChemEng
CHE_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/chemicalengineeringralphemartindepartmentofcheg/"
save_program("uark", "chemeng", "Ralph E. Martin Department of Chemical Engineering", CHE_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Chemical Engineering"),
    "supervisor": ("Not stated", "Not stated on the catalog page.", "", CHE_URL),
    "funding": fund(),
    "entry_route": ("Direct from bachelor's", "The Ph.D. degree requires at least 33 hours of course work and 39 hours of dissertation.", "Requirements for the Ph.D. Degree: At least 33 hours of course work and 39 hours of dissertation as follows:", CHE_URL)
})

# 13. Civil
CIV_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/civilengineeringcveg/"
save_program("uark", "civil", "Department of Civil Engineering", CIV_URL, {
    "deadline": dline(),
    "gre_subject": no_sub("Civil Engineering"),
    "supervisor": ("Not stated", "Not stated on the catalog page.", "", CIV_URL),
    "funding": fund(),
    "entry_route": ("Direct from bachelor's", "Minimum 72 semester hours of graduate-level credit beyond the baccalaureate degree.", "Requirements for the Doctor of Philosophy (Ph.D.) degree with emphasis in Civil Engineering: Minimum 72 semester hours of graduate-level credit beyond the baccalaureate degree.", CIV_URL)
})

# 14. BME
BME_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/biomedicalengineeringbmen/"
save_program("uark", "bme", "Department of Biomedical Engineering", BME_URL, {
    "deadline": dline(),
    "gre_general": ("Required", "A GRE score of 302 or above (verbal and quantitative) is required.", "A GRE score of 302 or above (verbal and quantitative).", BME_URL),
    "toefl_min": ("80", "A TOEFL score of at least 80 (internet based) is required.", "A TOEFL score of at least 213 (computer-based) or 80 (internet based). This requirement is waived for applicants whose native language is English", BME_URL),
    "gre_subject": no_sub("Biomedical Engineering"),
    "supervisor": ("Required", "A member of the faculty must agree to serve as the Major Adviser to the prospective student.", "A member of the faculty who is eligible (graduate status of group III or higher) must agree to serve as the Major Adviser to the prospective student", BME_URL),
    "funding": fund(),
    "entry_route": ("Either", "Students with a B.S. or M.S. degree in engineering or engineering equivalent are eligible to apply.", "Engineering Academic Background: Students with a B.S. or M.S. degree in engineering or engineering equivalent are eligible to apply for the Ph.D. program.", BME_URL)
})

# 15. Astronomy
SPAC_URL = "https://catalog.uark.edu/graduatecatalog/programsofstudy/spaceandplanetarysciencesspac/"
save_program("uark", "astronomy", "Center for Space and Planetary Sciences", SPAC_URL, {
    "deadline": dline(),
    "gre_general": ("Recommended", "Applicants are encouraged to submit scores from the Graduate Record Examination, including the writing score.", "Applicants are encouraged to submit scores from the Graduate Record Examination, including the writing score.", SPAC_URL),
    "gre_subject": no_sub("Space and Planetary Sciences"),
    "supervisor": ("Not stated", "Not stated on the catalog page.", "", SPAC_URL),
    "funding": fund(),
    "entry_route": ("Either", "Students are required to take a minimum of 72 hours beyond the baccalaureate degree or 42 hours beyond the master's degree.", "Students are required to take a minimum of 72 hours beyond the baccalaureate degree or 42 hours beyond the master's degree to include a minimum 33 hours of required course work and 18 hours of SPAC 7000V.", SPAC_URL)
}, name="Space and Planetary Sciences")

print("Re-saved all 15 UARK programs.")
