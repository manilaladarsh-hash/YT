import json

rec = json.loads(open(".cache/pages/404bcc40fb08826e.json", encoding="utf-8").read())
print("URL:", rec["url"])
lines = rec.get("text", "").splitlines()
in_adm = False
for line in lines:
    if "Admission Requirements" in line or "PhD in Physics" in line or "Tests Required" in line:
        in_adm = True
    if in_adm:
        print(line.encode("ascii", errors="replace").decode("ascii"))
    if "Degree Requirements" in line and in_adm:
        # print another 30 lines then stop
        pass
    if "Course List" in line and in_adm:
        break
