# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:30:05 2017

@author: lenovo
"""

import string
s = input('input a string:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print ('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))
