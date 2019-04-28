# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:47:47 2017

@author: lenovo
"""
import numpy as np

a=np.random.randint(1,100,9).reshape(3,3)
print(a)
(m,n)=np.shape(a)
sum=0
for i in range(m):
    for j in range(n):
        if i==j:
            sum+=a[i,j]
print(sum)