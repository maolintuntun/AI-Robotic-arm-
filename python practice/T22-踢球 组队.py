# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:37:17 2017

@author: lenovo
"""

for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k)and(i!=j):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print ('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))
