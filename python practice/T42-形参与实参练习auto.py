# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:05:02 2017

@author: lenovo
"""

num = 2
def autofunc():
    num = 1
    print( 'internal block num = %d' % num)
    num += 1
for i in range(3):
    print ('The num = %d' % num)
    num += 1
    autofunc()
