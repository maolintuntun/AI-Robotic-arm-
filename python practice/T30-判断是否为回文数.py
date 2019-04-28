# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:42:45 2017

@author: lenovo
"""

a = input("请输入一个数字:\n")
t=a[::-1]
print(type(a))
if a==t:
    print ("%s 是一个回文数!" % a)
else:
    print ("%s 不是一个回文数!" % a)

