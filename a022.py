#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:53:44 2019

@author: sam0225
"""


while True:
    try:
        s = input()
        print("yes" if s == s[::-1] else "no")
    except:
        break