# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 03:47:37 2019

@author: Sam
"""

while True:
    try:
        n = int(input())
        c = [0, 0, 0]
        for i in range(n):
            c[int(input()) % 3] += 1
        print(' '.join(str(i) for i in c))
    except:
        break
