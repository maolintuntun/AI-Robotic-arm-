# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:42:00 2017

@author: lenovo
"""
import tkinter as tk
from tkinter import *
canvas = Canvas(width=800, height=600, bg='blue')  
canvas.pack(expand=YES, fill=BOTH)                
k =1  #控制着中心圆的半径
j = 1  #各个圈之间的间隔
for i in range(0,26):
    canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=3)
    k += j
    j += 0.3
    
mainloop()
