#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:36:09 2019

@author: sam0225
"""

mat = [[0] * 100 for i in range(100)]
while True:
    try:
        m, n = map(int, input().split())
        for i in range(m):
            row = list(map(int, input().split()))
            for j in range(n):
                mat[i][j] = row[j]
        for i in range(n):
            for j in range(m):
                print(mat[j][i], " ", sep="", end="")
            print()

    except:
        break
