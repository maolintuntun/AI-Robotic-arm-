# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:11:17 2017

@author: lenovo
"""

tour = [] 
height = [] 
hei = 100.0 # 起始高度 
tim = 10 # 次数 
for i in range(1, tim + 1): 
    tour.append(hei) 
    hei /= 2 
    height.append(hei) 
print('总高度：tour = {0}'.format(sum(tour))) 
print('第10次反弹高度：height = {0}'.format(height[-1]))
