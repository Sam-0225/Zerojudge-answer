# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 04:22:29 2019

@author: Sam
"""

while True:
    try:
        n, m = map(int, input().split())
        print(m + 1 if n > m else m if n == m else "")
    except:
        break

