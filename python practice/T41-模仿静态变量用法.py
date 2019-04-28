# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:50:47 2017

@author: lenovo
"""


# 类的属性
# 作为类的一个属性吧
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print (self.StaticVar)

print(Static.StaticVar)
a = Static()
print(a.StaticVar)
for i in range(3):
    a.varfunc()
