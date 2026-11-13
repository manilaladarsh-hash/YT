import pathlib
p = pathlib.Path('.scratch/build_ufl.py')
s = p.read_text(encoding='utf-8')
old_block = '''        "supervisor_code": "Not required",
        "supervisor_val": "Rotations take place in the first year; picking a faculty advisor before applying is not required.",
        "supervisor_q": "",
        "supervisor_url": biomed_url,'''

new_block = '''        "supervisor_code": "Not required",
        "supervisor_val": "Students explore areas of study before choosing their mentor and concentration.",
        "supervisor_q": "The BMS program is an umbrella Ph.D. program that offers students the opportunity to explore one or more areas of study before choosing their mentor and concentration of study.",
        "supervisor_url": biomed_url,'''

s = s.replace(old_block, new_block)

old_block2 = '''        "supervisor_code": "Not required",
        "supervisor_val": "Rotations take place in the first year; choosing a faculty mentor prior to admission is not required.",
        "supervisor_q": "",
        "supervisor_url": biomed_url,'''

s = s.replace(old_block2, new_block)

p.write_text(s, encoding='utf-8')
print("Successfully updated supervisor in build_ufl.py")
