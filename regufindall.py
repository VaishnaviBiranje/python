    #re.findall()
import re
string ="""hello my number is 123456789 and my frinds number is 787654321"""
regex = '\d+'
match=re.findall(regex,string)
print(match)
