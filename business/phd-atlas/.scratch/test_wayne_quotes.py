import glob, json

quotes_to_check = [
    ("https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/physics-astronomy/physics-phd/", "The Graduate Record Examination, both the General section and the Physics subject test, is strongly recommended as a counseling aid in preparing the student"),
    ("https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/physics-astronomy/physics-phd/", "Candidates for the doctoral degree must complete 60 credits beyond the baccalaureate, including 18 credits of dissertation research."),
    ("https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/mathematics/mathematics-phd/", "Doctoral applicants must have completed a master"),
    ("https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/chemistry/chemistry-phd/", "A minimum undergraduate grade point average of 3.0 in chemistry and cognate science is required except by special permission of the Departmental Committee on Graduate Study."),
    ("https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/biological-sciences/biological-sciences-phd/", "Applicants must submit scores for the general portion of the Graduate Record Exam (GRE)."),
    ("https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/biological-sciences/biological-sciences-phd/", "the applicant should have completed a bachelor"),
    ("https://bulletins.wayne.edu/graduate/college-engineering/computer-science/computer-science-phd/", "Applicants must submit to the Department official transcripts from each college or university that they have attended, three letters of recommendation, Graduate Record Examination scores"),
    ("https://bulletins.wayne.edu/graduate/college-engineering/computer-science/computer-science-phd/", "The successful applicant should possess a bachelor's or master's degree with a major in computer science or related field."),
    ("https://bulletins.wayne.edu/graduate/college-engineering/computer-science/computer-science-phd/", "Advisor selection must be done within the first semester of admission."),
    ("https://bulletins.wayne.edu/graduate/college-engineering/electrical-computer-engineering/electrical-engineering-phd/", "Applicants must have an overall grade point average of 3.6 in a Master of Science degree program,. It is possible for outstanding students to enter the Ph.D program with only a Bachelor of Science degree."),
    ("https://bulletins.wayne.edu/graduate/college-engineering/mechanical-engineering/mechanical-engineering-phd/", "Submission of Graduate Record Examination (GRE) scores are optional."),
    ("https://bulletins.wayne.edu/graduate/college-engineering/mechanical-engineering/mechanical-engineering-phd/", "The admission to the Ph.D. program is contingent upon the approval of an Mechanical Engineering graduate faculty to serve as the permanent Ph.D. advisor for the applicant."),
    ("https://bulletins.wayne.edu/graduate/college-engineering/mechanical-engineering/mechanical-engineering-phd/", "All students must have a M.S. in Mechanical Engineering or a very similar field. Applicants without a M.S. in Mechanical Engineering are considered on a case-by-case basis."),
    ("https://bulletins.wayne.edu/graduate/college-engineering/chemical-engineering-materials-science/materials-science-engineering-phd/", "the written approval of the student"),
    ("https://bulletins.wayne.edu/graduate/college-engineering/civil-environmental-engineering/civil-engineering-phd/", "To gain admission to the Ph.D. program in civil engineering, students should have a Bachelor of Science (or Bachelor of Engineering) degree from an ABET accredited institution (or from a comparable foreign institution) with an overall GPA of 3.3 or greater. Students who do not satisfy these minimum requirements must earn a Master of Science"),
    ("https://bulletins.wayne.edu/graduate/college-engineering/biomedical-engineering/biomedical-engineering-phd/", "For admission and full funding consideration, please have your application completed by March 1st. Most decisions will be released by April 1st."),
    ("https://bulletins.wayne.edu/graduate/college-engineering/biomedical-engineering/biomedical-engineering-phd/", "All applicants must submit Graduate Record Examination (GRE) scores."),
    ("https://bulletins.wayne.edu/graduate/college-engineering/biomedical-engineering/biomedical-engineering-phd/", "An approved faculty member who agrees to be the student's Ph.D. advisor. The student must contact the faculty member with whom they want to work and obtain this approval before their application is considered for admission."),
    ("https://bulletins.wayne.edu/graduate/college-engineering/biomedical-engineering/biomedical-engineering-phd/", "A GPA of at least 3.5/4.0 in the applicant's Bachelor's degree or a GPA of at least 3.3/4.0 in the applicant's Master's degree is required."),
    ("https://bulletins.wayne.edu/graduate/school-medicine/programs/oncology/cancer-biology-phd/", "Admission is based on previous academic accomplishments, as documented by a transcript of a degree-in-progress or a posted official transcript of a completed degree. A minimum 3.0 grade point average is required although students typically have averages well in excess of this minimum."),
    ("https://bulletins.wayne.edu/graduate/school-medicine/programs/translational-neuroscience-phd/", "the Graduate Record Examination (GRE)"),
    ("https://bulletins.wayne.edu/graduate/school-medicine/programs/translational-neuroscience-phd/", "An interview with potential graduate faculty mentor(s) is also desirable."),
    ("https://bulletins.wayne.edu/graduate/school-medicine/programs/translational-neuroscience-phd/", "Applicants must have an undergraduate degree including several courses in basic sciences such as biology and chemistry."),
    ("https://gradschool.wayne.edu/admissions/deadlines", "Canadian and international students\nApply by May 1")
]

cache = {}
for p in glob.glob('.cache/pages/*.json'):
    try:
        d = json.load(open(p, 'r', encoding='utf-8'))
        u = d.get('url', '')
        cache[u] = d.get('text', '')
    except: pass

for u, q in quotes_to_check:
    text = cache.get(u, '')
    found = q in text
    print("FOUND" if found else "NOT FOUND", ":", q[:50], "in", u.split('/')[-2])
