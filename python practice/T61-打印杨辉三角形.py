# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:11:17 2017

@author: lenovo
"""

if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append([])
        for j in range(10):
            a[i].append(0)
    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2,10):
        for j in range(1,i):
            a[i][j] = a[i - 1][j-1] + a[i - 1][j]
    from sys import stdout
    for i in range(10):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print('')               #这句是我写的厉害吧
        print
