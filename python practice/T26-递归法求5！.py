# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:14:22 2017

@author: lenovo
"""

def fun(n):

    if n==1 or n==0:

        return 1
        
    else:
        a=fun(n-1)
        print(a,'*',n)
       
        return fun(n-1)*n
        

print (fun(5))