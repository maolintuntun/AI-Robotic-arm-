# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:18:23 2017

@author: lenovo
"""


def inp(numbers):
    for i in range(6):
        numbers.append(int(input('input a number:\n')))
        
def arr_max(a):
    for i in range(len(a)):
        if a[i]==max(a):
            a[0],a[i]=a[i],a[0]
def arr_min(a):
    for i in range(len(a)):
        if a[i]==min(a):
            a[len(a)-1],a[i]=a[i],a[len(a)-1]
    
            
if '__name__'=='__main__':
   a=[]
   inp(a)
   arr_max(a)
   arr_min(a)
   print(a)
   
   
       
