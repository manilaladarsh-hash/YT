with open('scripts/research.py', 'r', encoding='utf-8') as f:
    c = f.read()
old = 'html_src = raw_html if (method == "http" and status == 200) else rendered_html if (method.startswith("chromium") and status == 200) else ""'
new = 'html_src = raw_html if (method == "http" and (status == 200 or str(status).startswith("2"))) else rendered_html if (method.startswith("chromium") and rendered_html) else ""'
assert old in c, 'old not found'
c = c.replace(old, new)
with open('scripts/research.py', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated research.py')
