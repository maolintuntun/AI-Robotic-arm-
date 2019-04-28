# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:24:02 2017

@author: lenovo
"""

n=100
s=0

for i in range(1, 11): 
    n=n/2
    s=s+2*n
    print(s)
   
print('总高度：%f'%s) 
print('第10次反弹高度：height = %f'%n)