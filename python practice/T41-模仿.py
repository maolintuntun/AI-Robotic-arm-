# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:54:08 2017

@author: lenovo
"""


def varfunc():
    var = 0
    print ('var = %d' % var)
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()