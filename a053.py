#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:01:52 2019

@author: sam0225
"""

while True:
    try:
        n = int(input())
        if n <= 10:
            grade = n * 6
        elif n <= 20:
            grade = 60 + (n - 10) * 2
        elif n <= 40:
            grade = 80 + (n - 20) * 1
        else:
            grade = 100
        print(grade)
    except:
        break
