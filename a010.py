#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:20:07 2019

@author: sam0225
"""


def m(n):
    sl = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                sl.append(i)
                n = int(n / i)
                break
    s = str(sl[0])
    if sl.count(sl[0]) > 1:
        s += "^" + str(sl.count(sl[0]))
    for i in range(1, len(sl)):
        if sl[i] != sl[i - 1]:
            t = sl.count(sl[i])
            if t > 1:
                s += " * " + str(sl[i]) + "^" + str(t)
            else:
                s += " * " + str(sl[i])

    print(s)


while True:
    try:
        m(int(input()))
    except:
        break
