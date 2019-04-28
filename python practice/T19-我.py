# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:47:40 2017

@author: lenovo
"""

for m in range(1,1001):
    j=0
    k=[]
    
    for i in range(1,m):
        if m%i==0:
            j=j+i
            k.append(i)
            #print(j)
        
    if m==j:
        print(m)
        print(k[:])