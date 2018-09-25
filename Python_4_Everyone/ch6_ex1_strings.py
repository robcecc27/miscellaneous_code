

str = 'X-DSPAM-Confidence: 0.8475 '

ipos = str.find(':')
#print(ipos)
num = str[ipos + 2: ]
#print(num)
fnum = float(num)
print(fnum)
print(type(fnum))
