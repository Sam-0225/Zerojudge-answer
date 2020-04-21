#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:45:46 2019

@author: sam0225
"""

while True:
    try:
        M, D = map(int, input().split())
        S = (M * 2 + D) % 3
        if S == 0:
            print("普通")
        elif S == 1:
            print("吉")
        else:
            print("大吉")
    except:
        break

