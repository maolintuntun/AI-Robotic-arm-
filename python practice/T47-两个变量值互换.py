# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:35:01 2017

@author: lenovo
"""

def exchange(a,b):
    a,b = b,a
    return (a,b)

if __name__ == '__main__':
    x = 10
    y = 20
    print('x = %d,y = %d' % (x,y))
    x,y = exchange(x,y)
    print('x = %d,y = %d' % (x,y))
    
    
   
