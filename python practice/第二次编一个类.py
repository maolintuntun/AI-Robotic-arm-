# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:17:18 2017

@author: lenovo
"""


#class change:
#    def __init__(self,num,a=[1,2,3,4,5],delay=4):
#        self.pp=num
#        self.qq=a
#        self.oo=[]
#        self.mm=delay
#        print(self.exchange())
#        
#    def exchange(self):
#        p=self.qq[-self.mm: ]
#        c=[]
#        d=[]
#        for j in range(self.pp-self.mm):
#            c.append(self.qq[j])
#        for i in range(self.mm):
#            d.append(p[i])
#        return(d+c)
##    
##if __name__=='__main__':
##
##    
##    laoyang=change(num=8,a=[1,2,3,4,5,6,7,8],delay=3)
##    print('after moved:',laoyang.exchange())
#    

class Calculator:
    name='Good calculator'
    price=18
    
    def __init__(self,name,price,height=18,width=2,weight=2):   # 注意，这里的下划线是双下划线
        self.name=name
        self.price=price
        self.h=height
        self.wi=width
        self.we=weight
        print(self.add(1,2))
        #self.divide(6,5)
    def add(self,x,y):
        print(self.name)
        return(x+y)
        #print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        result=x*y
        print(result)
    def divide(self,x,y):
        print(x/y)





















