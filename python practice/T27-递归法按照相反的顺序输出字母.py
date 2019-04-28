# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 13:29:26 2017

@author: lenovo
"""

def put(s,l):
    if l==0:
       return
    print (s[l-1])
    put(s,l-1)
 
s = input('Input a string:')
l = len(s)
print(l)
put(s,l)