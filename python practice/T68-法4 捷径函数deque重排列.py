# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 21:04:42 2017

@author: lenovo
"""

from collections import deque
f=[]
m = -3
a = [1,2,3,4,5,6,7]   # 7 个数
f = deque(a)
f.rotate(m)
print(f)
