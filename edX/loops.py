# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
#%%
end = 6
total = 0
for next in range(1, end+1):
    total += next
print(total)
#%%
# Here is another:
total = end
for next in range(end):
    total += next
print(total)
#%%
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
#%%    
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)
#%%
# Prints out 3,4,5
for x in range(3, 6):
    print(x)
#%%
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
#%%
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
    
#%%
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
    
#%%
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
    
#%%
# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
    
#%%
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes 

#%%
num = 10
for num in range(5):
    print(num)
print(num)

#%%
divisor = 2
for num in range(0, 10, 2):
    print(num)
    print(divisor)
    print(num/divisor)

#%%
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')


#%%
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for nums in numbers:
    numbers.sort(nums)
    print(nums)
    
    
#%%
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')
#%%
for letter in 'hola':
    print(letter)  

#%%
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    #break
print(count)

#%%
divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 
    
#%%
myStr = '6.00x'

for char in myStr:
    print(char)

print('done')

#%%
greeting = 'Hello!'
count = 0

for letter in greeting: # H e l l o !
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

#%%
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or str == 'Mass':
        print(str)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))
