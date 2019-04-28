# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:21:29 2017

@author: lenovo
"""


a=[]
for i in range(5):
    a.append(int(input('输入一个数:\n')))
m = int(input('back m:\n'))
t=int(input('the total number is:\n'))
#a=[2,3,9,6,1]
#a.append(int(input('请输入一个数字：\n')))
p=a[-m: ]
#print(p)
u=0
c=[]
d=[]
for j in range(t-m):
    c.append(a[j])
    
    #print(c[u])

for i in range(m):
    d.append(p[i])
    print(d)
    
 
    
