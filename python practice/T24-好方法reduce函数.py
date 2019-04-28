# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 09:37:44 2017

@author: lenovo
"""


from functools import reduce
a = 2.0
b = 1.0
l = []

for n in range(1,21):
    l.append(a / b)
    print(a,"/",b)
    b,a = a,a + b
    
   
    
print (reduce(lambda x,y: x + y,l))
