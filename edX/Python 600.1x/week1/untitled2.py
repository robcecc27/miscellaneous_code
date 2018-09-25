# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 18:00:18 2018

@author: Rob
"""
#char = chr(number)
#number = ord(char)

#%%
s = 'azcbobobegghakl'
bob = 0
count = 0
while bob < len(s):
    bob = s.find('bob', bob)
    count += 1
    if bob == -1:
        count -= 1
        break
    bob += 2 # +2 because len('bob') == 2
print("Number of times bob occurs is: ",count)

#%%
s = 'azcbobobegghakl'
#alpha = 'abcdefghijklmnopqrstuvwxyz'
temp = ''
temp1 = ''
for i in s:
    if i in "abcdefghijklmnopqrstuvwxyz":
        number = ord(i)
        if number + 1 == number :
            temp += i
            print(temp, "first")
        if number == number +1 :
            temp1 += i
        print(temp1, "Second")
        
 #%%  
    
    if temp1 <= i :
        temp1 = i
    #if temp1 >= i:
    #    temp1 += i
        print(temp1, "2")
    print(i, "3")
        
#%%       