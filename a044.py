#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:44:13 2019

@author: sam0225
"""


while True:
    try:
        n = int(input())
        print(int(1 + n + n * (n + 1) * (n - 1) / 6))
    except:
        break

