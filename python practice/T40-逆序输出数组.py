# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:17:35 2017

@author: lenovo
"""
a=[9,6,5,4,1]
t=int(len(a))
for i in range(0,int(t/2)):
    a[i],a[t-1-i]=a[t-1-i],a[i]
print(a)
                 