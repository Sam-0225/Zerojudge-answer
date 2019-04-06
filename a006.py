#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:54:35 2019

@author: sam0225
"""


while True:
    try:
        a, b, c= map(int, input().split())
        D = b**2 - 4*a*c
        if D > 0:
            x1 = int((-b + D**0.5) / (2*a))
            x2 = int((-b - D**0.5) / (2*a))
            print("Two different roots x1="+str(x1)+" , x2="+str(x2))
        elif D == 0:
            x = int(-b / (2*a))
            print("Two same roots x="+str(x))
        else:
            print("No real root")
    except:
        break
    