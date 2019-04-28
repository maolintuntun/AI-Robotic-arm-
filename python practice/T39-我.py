# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:48:34 2017

@author: lenovo
"""

a = [1,4,6,9,13,16,19,28,40,100,0]
l=len(a)
print(l)
number=int(input('输入一个数：\n'))
   
for i in range(0,l):
    if a[i+1]>number>a[i]:
        a.insert(i,number)
    else :a.append(number)

print(a)
    