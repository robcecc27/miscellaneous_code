# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:39:58 2018

@author: Rob
"""
import os
from collections import Counter

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'rare.txt'
hand = open(fname)
text = fname.isalpha

c = Counter(text)
print(c.most_common())

#%%
import re

text_doc = open("rare.txt")     
encoding = re._pattern_type('charset', 'utf8')
text = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->', re.S).findall()[-1]
counts = {}
for c in text: counts[c] = counts.get(c, 0) + 1

counts

print(''.join(re.findall('[a-z]', text)))
