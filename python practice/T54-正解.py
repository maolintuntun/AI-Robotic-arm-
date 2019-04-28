# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 12:45:28 2017

@author: lenovo
"""

if __name__ == '__main__':
    a = int(input('input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print ('%o\t%o' %(a,d))
