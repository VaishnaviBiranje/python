from re import split
print (split('\W+','words,words,word'))
print(split('\W+',"word's words words"))
print(split('\W+','on 12th jan 2016 , at 11:02 AM'))
print(split('\d+','on 12th jan 2016 , at 11:02 AM'))


