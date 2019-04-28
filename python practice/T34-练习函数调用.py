# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 12:20:20 2017

@author: lenovo
"""

def hello_world():
    print ('hello world')

def three_hellos():
    for i in range(3):
        hello_world()
if __name__ == '__main__':
   
    three_hellos()
    hello_world()
