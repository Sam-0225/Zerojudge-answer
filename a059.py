# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 04:01:58 2019

@author: Sam
"""


while True:
    try:
        N = int(input())
        for i in range(N):
            a = int(input())
            b = int(input())
            sum = 0
            for j in range(a, b+1):
                if j**0.5 == int(j**0.5):
                    sum += j
            print("Case " + str(i + 1) + ": "+str(sum))
    except:
        break