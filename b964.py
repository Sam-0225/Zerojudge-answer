#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:15:06 2019

@author: sam0225
"""

while True:
    try:
        times = int(input())
        score = sorted(list(map(int, input().split())))
        print(' '.join(str(e) for e in score))

        maxS = -99
        minS = 99
        for i in range(times):
            if score[i] < 60 and score[i] > maxS:
                maxS = score[i]
            if score[i] >= 60 and score[i] < minS:
                minS = score[i]

        print("best case" if maxS == -99 else maxS)
        print("worst case" if maxS == 99 else minS)

    except:
        break
