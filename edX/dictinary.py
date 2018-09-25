# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 21:49:06 2018

@author: Rob
"""

def loadItems(): #Loads and returns the input file before returning the file
    open_inv = open('A1input.txt','r')
    inv_list = [line.strip().split(',')for line in open_inv.readlines()]
    open_inv.close()
    return inv_list

def displayItems(inv_list): #Takes the returned input file from loadItems and prints
    for item in inv_list:
        print (item)

def buildDict(inv_list):
    d = {}
    for item in inv_list:
        if item[1] not in d:
            d[item[1]] = [item[:1] + item[2:]]
        else:
            d[item[1]].append(item[:1] + item[2:])
    
    for key, value in d.items():
        for item in value:
            print(key, item)
            
    return (d)
     
def writeFile(d):
    f = open("OutputA1.txt",'w')
    for key, value in d.items():
        x = str(key)
        y = str(value)
        f.write(str(x+y+''))
        f.write(str('\n'))

itemList = loadItems()
displayItems(itemList)
print('\n\n Start of Dictionary');
dic = buildDict(itemList)
writeFile(dic)
