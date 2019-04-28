# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:42:13 2017

@author: lenovo
"""

n=int(input("输入整数1~n:"))
List=[]
for i in range(1,n+1):
    List.append(i)
print("打印1~n:",List)
print()
m=int(input("输入要移动的位数:"))
List2=List[n-m:n+1]+List[0:n-m]
print("打印移动后的结果:",List2)