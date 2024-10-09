import re 
p =re.compile('[a-e]')
print(p.findall("aye,said mr.vaishnavi bianje"))

#\w
p=re.compile('\w')
print(p.findall("she said me * in some_lang"))

p = re.compile('\w+')
print(p.findall("i want meet him at 12 A.M.,he \ said ** in some_language."))

p =re.compile('\w')
print(p.findall("he said *** in some_language."))

p = re.compile('ab*')
print(p.findall("ababbaabbb"))

