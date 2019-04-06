#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:09:23 2019

@author: sam0225
"""

while True:
    try:
        print(bin(int(input())).replace("0b",""))
    except:
        break