# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:28:55 2017

@author: lenovo
"""
s=0
for i in range(1,21):
    t=1
   
    for j in range(1,i+1):
        t=t*j
    s=s+t  
print('1! + 2! + 3! + ... + 20! = %d'%s)