# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 04:37:15 2019

@author: Sam
"""

while 1:
    try:
        input()
        print(' '.join(str(i) for i in sorted(map(int, input().split()))))
    except:
        break

