#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:20:07 2019

@author: sam0225
"""

# def m(n):
#     sl = []
#     while n > 1:
#         for i in range(2, n + 1):
#             if n % i == 0:
#                 sl.append(i)
#                 n = int(n / i)
#                 break
#
#     s = str(sl[0])
#     if sl.count(sl[0]) > 1:
#         s += '^' + str(sl.count(sl[0]))
#
#     for i in range(1, len(sl)):
#         if sl[i] != sl[i - 1]:
#             t = sl.count(sl[i])
#             if t > 1:
#                 s += " * " + str(sl[i]) + "^" + str(t)
#             else:
#                 s += " * " + str(sl[i])
#
#     print(s)
#
#
# while True:
#     try:
#         m(int(input()))
#     except:
#         break


while True:

    try:
        _input = int(input())
        factorsCount = 0
        factor = 2
        s = ''
        while _input > 1:
            while _input % factor == 0:
                _input = _input // factor
                factorsCount += 1
            if factorsCount > 1:
                s += str(factor) + '^' + str(factorsCount)
            if factorsCount == 1:
                s += str(factor)
            if _input % (factor + 1) == 0 and s != '':
                s += ' * '
            factorsCount = 0
            factor += 1
        print(s)
    except:
        break
