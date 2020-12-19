#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 03:04:41 2019

@author: sam0225
"""


def romanToInt(s):
    ROMANSdict = {'M': 1000,
                  'D': 500,
                  'C': 100,
                  'L': 50,
                  'X': 10,
                  'V': 5,
                  'I': 1}
    sum = 0
    for i in range(len(s) - 1):
        if ROMANSdict[s[i]] < ROMANSdict[s[i + 1]]:
            sum -= ROMANSdict[s[i]]
        else:
            sum += ROMANSdict[s[i]]
    return sum + ROMANSdict[s[-1]]


def roman(number):
    ROMANS = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))

    s = ''
    for roman, value in ROMANS:
        while number >= value:
            number -= value
            s += roman
    return s


while True:
    try:
        a, b = input().split()
        answer = roman(abs(romanToInt(a) - romanToInt(b)))
        if answer == '':
            print('ZERO')
        else:
            print(answer)
    except:
        break
