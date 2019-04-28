# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:03:23 2017

@author: lenovo
"""
from math import sqrt
from sys import stdout

class tingge:
    def __init__ (self,p=101,q=201,a=0):
       
        self.begin=p
        self.end=q
        self.amount=a
        
    def die(self):
        self.amount=0
#a为素数个数
#每次找到一个素数，b就加一 用来求素数的总个数
        for m in range(self.begin,self.end):
            b=1
            for i in range(2, int(sqrt(m)) + 1):
                if m % i == 0:
                    b = 0
                    break
            if b==1:
                print('%-4d' % m)
            self.amount=self.amount+b
            if self.amount%10==0:
                print('')
    
        print('The total is %d' %  self.amount)
        
if __name__ =='__main__':
    
        c=tingge()
        c.die
    
    
    
    
    
    
a=0
#a为素数个数
#每次找到一个素数，b就加一 用来求素数的总个数
for m in range(101,201):
    b=1
    for i in range(2, int(sqrt(m)) + 1):
        if m % i == 0:
            b = 0
            break
    if b==1:
        print ('%-4d' % m)
    a=a+b
    if a%10==0:
        print('')
    
print('The total is %d' % a)