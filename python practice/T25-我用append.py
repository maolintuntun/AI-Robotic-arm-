# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:55:56 2017

@author: lenovo
"""
from functools import reduce
s=0
l=[]
for i in range(1,21):
    t=1
   
    for j in range(1,i+1):
        t=t*j
    l.append(t) 
    #print(t,'*',j)
   
print(reduce(lambda x,y:x+y,l))