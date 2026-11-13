import json

rec = json.loads(open(".cache/pages/c8ce4496ffa326bc.json", encoding="utf-8").read())
lines = rec.get("text", "").splitlines()
in_adm = False
for line in lines:
    if "Admission" in line or "PhD in Physics" in line:
        in_adm = True
    if in_adm:
        print(line.encode("ascii", errors="replace").decode("ascii"))
    if "Degree Requirements" in line and in_adm:
        # print some degree reqs then stop
        pass
    if "Courses" in line and in_adm:
        break
