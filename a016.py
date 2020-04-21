#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:59:22 2019

@author: sam0225
"""

while True:
    try:
        flag = True
        matrix_9x9 = [input().split() for _ in range(9)]
        for row in matrix_9x9:
            if len(set(row)) < 9:
                flag = False
                break
        for row in zip(*matrix_9x9):
            if len(set(row)) < 9:
                flag = False
                break
        flag = True
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                matrix_3x3 = matrix_9x9[i][j:j + 3] + matrix_9x9[i + 1][j:j + 3] + matrix_9x9[i + 2][j:j + 3]
                # print(matrix_3x3)
                if len(set(matrix_3x3)) < 9:
                    flag = False
                    break
        if flag:
            print("yes")
        else:
            print("no")
        input()
    except:
        break
