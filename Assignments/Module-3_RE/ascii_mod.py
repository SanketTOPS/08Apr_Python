import re

mystr="That is Python!1256946465"

#x=re.findall('\w',mystr)
#x=re.findall('\W',mystr)
#x=re.findall('\d',mystr)
#x=re.findall('\D',mystr)
#x=re.findall('\s',mystr)
#x=re.findall('\S',mystr)
#x=re.findall(r'\bThis',mystr)
#x=re.findall('\B68',mystr)
#x=re.findall('\AThis',mystr)
x=re.findall('67\Z',mystr)
print(x)