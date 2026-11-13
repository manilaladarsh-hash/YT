import urllib.request
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

req = urllib.request.Request("https://catalog.utk.edu/content.php?catoid=57&navoid=12418", headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode("utf-8", errors="replace")

majors = [
    "Computer Science Major, PhD",
    "Electrical Engineering Major, PhD",
    "Biomedical Engineering Major, PhD",
    "Chemical Engineering Major, PhD",
    "Civil Engineering Major, PhD",
    "Materials Science and Engineering Major, PhD",
    "Mechanical Engineering Major, PhD",
    "Physics Major, PhD",
    "Chemistry Major, PhD",
    "Mathematics Major, PhD",
    "Geology Major, PhD",
    "Biochemistry and Cellular and Molecular Biology Major, PhD",
    "Data Science and Engineering Major, PhD"
]

for m in re.finditer(r'href=["\']([^"\']*)["\'][^>]*>([^<]+)<', html):
    link = m.group(1)
    text = m.group(2).strip()
    for maj in majors:
        if maj.lower() in text.lower():
            full_link = link if link.startswith("http") else f"https://catalog.utk.edu/{link}"
            print(f"{maj} -> {full_link}")
