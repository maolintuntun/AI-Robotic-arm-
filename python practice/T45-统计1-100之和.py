# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:46:40 2017

@author: lenovo
"""
from functools import reduce

t= reduce(lambda x,y:x+y,range(1,101))
print(t)
