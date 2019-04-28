# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 09:38:47 2017

@author: lenovo
"""

import tkinter as tk
if __name__ == '__main__':
    from tkinter import *
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30
    canvas = Canvas(width = 400,height = 600,bg = 'white')
    for i in range(20):
        canvas.create_oval(250 - top,250 - bottom,250 + top,250 + bottom,width=i*0.1,fill = "red")
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()
