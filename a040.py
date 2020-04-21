#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:15:06 2019

@author: sam0225
"""


def f(num):
    str_num = str(num)
    len_num = len(str_num)
    total = 0

    for i in range(len_num):
        total += int(str_num[i]) ** len_num
    return total


while True:
    try:
        a = 0
        n, m = map(int, input().split())
        for i in range(n, m + 1):
            if i == f(i):
                print(i, "", end="")
                a += 1
        if not a:
            print("none")
        print()
    except:
        break
