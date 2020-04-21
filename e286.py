#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:53:44 2019

@author: sam0225
"""

score = [0] * 4
for i in range(4):
    score[i] = sum(map(int, input().split()))
print(str(score[0]) + ":" + str(score[1]))
print(str(score[2]) + ":" + str(score[3]))

if score[0] > score[1] and score[2] > score[3]:
    print("Win")
elif not score[0] > score[1] and not score[2] > score[3]:
    print("Lose")
else:
    print("Tie")

#
# sumA = sumB = 0
# first = True
# second = True
# for i in range(4):
#     a, b, c, d = map(int, input().split())
#     if i % 2:
#         sumB = a + b + c + d
#         print(str(sumA)+":"+str(sumB))
#         if i == 1:
#             first = True if sumA > sumB else False
#         else:
#             second = True if sumA > sumB else False
#     else:
#         sumA = a + b + c + d
# if first and second:
#     print("Win")
# elif not first and not second:
#     print("Lose")
# else:
#     print("Tie")
