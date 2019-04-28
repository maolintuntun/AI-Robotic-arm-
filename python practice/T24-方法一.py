# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:01:59 2017

@author: lenovo
"""

a = 2.0
b = 1.0
s = 0.0
for n in range(1,21):
    s += a / b
    b,a = a , a + b
print (s)

