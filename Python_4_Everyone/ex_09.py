fname = input('Enter File: ')
if len(fname) < 1 : fname = 'romeo.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create 
        di[w] = di.get(w,0) + 1

largest = -1
theword = None
for key, value in d.items():
        x = str(key)
        y = str(value)
        f.write(str(x+y+'\n'))

print(theword, largest)

