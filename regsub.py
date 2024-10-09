import re 
print(re.sub('ub','~*','subject has uber boked alreday',flags =re.IGNORECASE))
print(re.sub('ub','~*','subject has uber booked alreday'))
print(re.sub('ub','~*','subject has uber booked alreaday',count=1,flags=re.IGNORECASE))
print(re.sub(r'\sAND\s','&','baked beand and spam',flags=re.IGNORECASE))
