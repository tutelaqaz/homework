import re
f = open('eDIL - Irish Language Dictionary.html', 'r', encoding = 'utf-8')
text =f.read()
dictin = {}
m = re.search('headword_id="(\\d*)">', text)
if m != None:
    ident = m.group(1)
m = re.search('Forms:\\s*(.*[^>])<', text)
if m != None:
    forms = m.group(1)
m = re.search('\\s(\\w*)\\s*,\\s\((.*)\)</h3>', text)
if m != None:
    head = m.group(1)+' ' + m.group(2)
forms = forms.split()
for form in forms:
    dictin[form] = ident + ' ' + head
print(dictin)
f.close()

    
