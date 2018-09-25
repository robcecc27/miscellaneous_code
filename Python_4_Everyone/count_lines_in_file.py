

import re
with open("100_Books.txt") as f:
    for line in f:
        if re.match(r"^\d+.*$",line):
            remove(r"^\d+.*$")
            
            print(line)


            
"""         
fname = input('Enter the file name:  ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith(1, 9) :
        count = count + 1
print('There were', count, 'lines', fname)

"""