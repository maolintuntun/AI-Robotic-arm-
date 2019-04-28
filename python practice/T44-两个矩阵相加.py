# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 11:26:45 2017

@author: lenovo
"""

X = [[12,7,3], [4 ,5,6], [7 ,8,9]]
Y = [[5,8,1], [6,7,3], [4,5,9]] 
result = [[0,0,0], [0,0,0], [0,0,0]] 
for i in range(len(X)):  # 迭代输出行 
    for j in range(len(X[0])): # 迭代输出列
        result[i][j] = X[i][j] + Y[i][j] 
for r in result: 
    print(r)