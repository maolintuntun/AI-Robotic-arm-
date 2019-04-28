# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:28:56 2017

@author: lenovo
"""

import numpy as np
num=np.arange(101)
for i in num[2:101]:
    c=0
    mod1=[]
    mod1.append(np.mod(i,num[1:101]))
    c=np.count_nonzero(mod1)
    if(np.size(mod1)-c <= 2):
        print(i),