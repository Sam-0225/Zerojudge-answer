#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:47:25 2019

@author: sam0225
"""

while True:
    try:
        y = int(input())
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            print("閏年")
        else:
            print("平年")
    except:
        break

"""
import calendar
while True:
    try:
        y = int(input())
        check_year=calendar.isleap(y)
        if check_year == True:
            print("閏年")
        else:
            print("平年")
    except:
        break
"""
