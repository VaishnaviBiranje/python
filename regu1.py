#re.findall()
import re
string ="""hello my number is 123456789 and my frinds number is 787654321"""
regex = '\d+'
match=re.findall(regex,string)
print(match)

#without /
s='hello.goodmorning'
match =re.search(r'.',s)
print(match)

#with /
match = re.search(r'\.',s)
print(match)

#[]
st1 = "every person has different ability "
pattern = "[a-i]"
result = re.findall(pattern,st1)
print(result)


#^ caret
regex =r'^the'
strings =['the quick brown fox','the laze dog','a quick brown box']
for string in strings:
    if re.match(regex,string):
        print (f'metched: {string}')
    else:
        print(f'not matched:{string}') 


# $ doller
string ="hello world !"
patter = r"world!$"
match=re.search(pattern,string)
if match:
    print("match found!")
else:
    print("match not found.")            

