#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:49:54 2019

@author: sam0225
"""


times = int(input())
for _ in range(times):
    a, b, c, d = map(int, input().split())
    if a-b == b-c:
        e = (b - a) + d
    else:
        e = (b // a) * d
    print(a, b, c, d, e)