# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:23:25 2017

@author: lenovo
"""


#a = int(input('input a number:\n'))
#b = a >> 4
#c = ~(~0 << 4)
#d = b & c
#print ('%o\t%o' %(a,d))

a = int(input('input a number:\n'))


tt=str(bin(a)[::-1][4:7])
print(tt)