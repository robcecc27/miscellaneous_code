import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[aeiou]+',x)
print(y)


a = 'From: Using the: character'
b = re.findall('^F.+?:',a)
print(b)
