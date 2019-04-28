# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:49:26 2017

@author: lenovo
"""
from math import sqrt

for i in range(2,101):
    flag=0
    for t in range(2,int(sqrt(i)) + 1):
        if i%t==0:
            flag=1
            break
    if flag==0:
        print(i)
            
        
