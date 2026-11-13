import json
from pathlib import Path

# Update lehigh.json
uni_path = Path("data/universities/lehigh.json")
uni = json.load(open(uni_path, encoding="utf-8"))

uni["fields"]["gre_general"] = {
    "code": "Not required",
    "value": "Most graduate programs at Lehigh do not require a GRE or GMAT for admission consideration. Individual programs set their own testing requirements.",
    "quote": "Is GRE/GMAT required? | Most programs at Lehigh do not require a GRE or GMAT for admission consideration. It is best to review the policies of the specific college and/or program to determine the application requirements for the program of interest.",
    "url": "https://www2.lehigh.edu/admissions/applying-to-graduate-studies-at-lehigh"
}

uni["fields"]["ielts_min"] = {
    "code": "6.5",
    "value": "Minimum composite IELTS score is 6.5 across the College of Arts & Sciences, College of Health, College of Education, and P.C. Rossin College of Engineering.",
    "quote": "College of Arts & Sciences ... Overall: 6.5 | P.C. Rossin College of Engineering and Applied Science ... Overall: 6.5",
    "url": "https://www2.lehigh.edu/admissions/english-proficiency-requirement-for-graduate-studies"
}

with open(uni_path, "w", encoding="utf-8") as f:
    json.dump(uni, f, indent=2, ensure_ascii=False)
    f.write("\n")

# Update lehigh--math.json
math_path = Path("data/programs/lehigh--math.json")
math_prog = json.load(open(math_path, encoding="utf-8"))
math_prog["fields"]["supervisor"] = {
    "code": "Not required",
    "value": "No research advisor required prior to admission; admission is based on application review with official transcripts and two letters of recommendation.",
    "quote": "Official transcripts and two letters of recommendation are required. | Q: Is an interview required? | A: An interview is not required, but please contact us if you would like to visit.",
    "url": "https://math.cas.lehigh.edu/graduate/faqs"
}

with open(math_path, "w", encoding="utf-8") as f:
    json.dump(math_prog, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("Updated lehigh.json and lehigh--math.json successfully!")
