# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:20:23 2017

@author: lenovo
"""

a=[]
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)     #非常重要！因为必须先给整个二维数组赋值 这里全部赋值成一个0的十乘十矩阵
for i in range(10):
    a[i][0]=1
    for j in range(10):
        a[i][i]=1
for i in range(2,10):
    for j in range(1,10):
        a[i][j]=a[i-1][j]+a[i-1][j-1]
        
from sys import stdout       #这一段是提前打印出数组,新学的
for i in range(10):
    for j in range(i+1):
        stdout.write(str(a[i][j]))
        stdout.write(' ')
    print('')
print

    