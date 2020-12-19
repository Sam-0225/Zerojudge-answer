#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:21:45 2019

@author: sam0225
"""

# while True:
#     try:
#         dict1 = {'A': 10, 'J': 18, 'S': 26, 'B': 11, 'K': 19, 'T': 27, 'C': 12, 'L': 20, 'U': 28,
#                  'D': 13, 'M': 21, 'V': 29, 'E': 14, 'N': 22, 'W': 32, 'F': 15, 'O': 35, 'X': 30,
#                  'Y': 31, 'G': 16, 'H': 17, 'Q': 24, 'Z': 33, 'I': 34, 'R': 25, 'P': 23}
#         id_text = input()
#         en = str(dict1[id_text[0].upper()])
#         total = int(en[0]) + int(en[1]) * 9 + int(id_text[len(id_text) - 1])
#         id_text = id_text[1:9]
#         n = 8
#         for i in id_text:
#             total += int(i) * n
#             n -= 1
#
#         print("real" if total % 10 == 0 else "fake")
#
#     except:
#         break


x = input()
a = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
y = a[ord(x[0]) - 65]
z = (y % 10 * 9) + ((y - (y % 10)) // 10) + int(x[-1]) + int(x[-2])
for i in range(8, 1, -1):
    z += int(x[9 - i]) * i
print('real' if z % 10 == 0 else 'fake')