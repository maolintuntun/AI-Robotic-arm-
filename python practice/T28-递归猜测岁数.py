# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:03:24 2017

@author: lenovo
"""
def age(n):
    if n == 1: c = 10
    else: c = age(n - 1) + 2
    return c
print (age(5))