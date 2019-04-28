# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:03:18 2017

@author: lenovo
"""

TRUE = 1
FALSE = 0
def SQ(x):
    return x * x
print ('如果输入的数字小于 50，程序将停止运行。')
again = 1
while again:
    num = int(input('Please input number'))
    print ('运算结果为 %d' % (SQ(num)))
    if num >= 50:
        again = TRUE
    else:
        again = FALSE
