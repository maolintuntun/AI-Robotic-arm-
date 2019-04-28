# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:18:12 2017

@author: lenovo
"""

class Num:
    
    
    
    
    def __init__(self,camero=0): #这个叫初始化 
        self.camero=camero       #这些在
        self.frame = None
        self.roiPts = []
        self.inputMode = False
        self.dist1=0
        self.dist=0
        self.roiBox = None
    nNum = 1
    def inc(self):             #这个调用之后才会执行 优先级比第一个_init_属性靠后
        self.nNum += 1
        print ('nNum = %d' % self.nNum)

if __name__ == '__main__':
    
    inst = Num(8) #老杨说 这个叫实例化
    print(inst.camero)
    
    for i in range(3):
        nNum = 2
        nNum += 1
        print ('The num = %d' % nNum)
        inst.inc()
        print(inst.nNum)  #因为Num=inst 这就是self的意义，代表类自己


