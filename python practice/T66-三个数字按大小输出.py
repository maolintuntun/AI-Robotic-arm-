# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:34:39 2017

@author: lenovo
"""

n1=int(input('n1=:\n'))
n2=int(input('n2=:\n'))
n3=int(input('n3=:\n'))

def swap(p1,p2):
    if p2>p1:
        p1,p2=p2,p1
    return p1,p2

n1,n2=swap(n1,n2)
n1,n3=swap(n1,n3)
n2,n3=swap(n2,n3)

print(n1,n2,n3)