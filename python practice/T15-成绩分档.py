# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 12:40:46 2017

@author: lenovo
"""

score = int(input('input score:\n'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print ('%d belongs to %s' % (score,grade))
