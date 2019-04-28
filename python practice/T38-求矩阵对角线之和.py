# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:18:26 2017

@author: lenovo
"""

if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])     #向a数组中加行列表
        for j in range(3):
            a[i].append(float(input("input num:\n"))) #向每个a的行列表中加入元素
    for i in range(3):
        print(a[i][i])    #自己加的，输出对角线元素 因为对角线上的下标都是一样的数
        sum += a[i][i]
    print (sum)