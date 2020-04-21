#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sam0225
"""
while True:
    try:
        R, C, M = map(int, input().split())
        pre = []
        for i in range(R):
            pre.append(list(map(int, input().split())))
        op = list(map(int, input().split()))

        for opm in range(M - 1, -1, -1):
            if op[opm] == 0:  # 逆旋轉
                nxt = [[0] * R for i in range(C)]
                for i in range(R):
                    for j in range(C):
                        nxt[C - 1 - j][i] = pre[i][j]
                R, C = C, R
                pre = nxt
            else:
                nxt = [[0] * C for i in range(R)]
                for i in range(R):
                    for j in range(C):
                        nxt[R - 1 - i][j] = pre[i][j]
                pre = nxt

        print(str(R) + " " + str(C))
        for i in range(len(pre)):
            for j in range(len(pre[0])):
                print(pre[i][j], end=" ")
            print()

    except:
        break
