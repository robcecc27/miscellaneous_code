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

#print(di)

tmp = list()
for k,v in di.items():
    #print(k,v)
    newt = (v,k)
    tmp.append(newt)
    
#print('flipped',tmp)

tmp = sorted(tmp, reverse=True)
#print('Sorted',tmp)

for v,k in tmp[:20] :
    print(k,v)