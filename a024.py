#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:58:44 2019

@author: sam0225
"""

import math

while True:
    try:
        a, b = map(int, input().split())
        print(math.gcd(a, b))
    except:
        break

"""
while True:
    try:
        a, b= map(int, input().split())
        while True:
            if b > a:
                b,a = a,b
            if a % b ==0:
                print(b)
                break
            else:
                a -= int(a/b)*b
    except:
        break
"""
