# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 04:11:33 2019

@author: Sam
"""

while True:
    try:
        pwd = input()
        s = ""
        for i in range(6):
            s += str(abs(ord(pwd[i])-ord(pwd[i+1])))
        print(s)
    except:
        break
