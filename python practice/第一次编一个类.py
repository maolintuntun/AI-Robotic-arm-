# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 22:19:55 2017

@author: lenovo
"""

class change:
    def __init__(self,num,a,delay):
        self.num=5
        self.a=[1,2,3,4,5]
        self.delay=3
        
        
        
    def exchange(self):
        p=[]
        p=self.a[self.delay: ]
        c=[]
        d=[]
        for j in range(self.num-self.delay):
            c.append(self.a[j])
        for i in range(self.delay):
            d.append(p[i])               
        return(d+c)

if '__name__'=='__main__':
    Num=int(input('the total number is:\n'))
    laoyang=change(62)
    print(laoyang.exchange())
    
    
        
    