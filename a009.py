#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:10:25 2019

@author: sam0225
"""


key = ord('*') - ord('1')
while True:
    try:
        ciphertext = input()
        plaintext = ""
        for x in ciphertext:
            plaintext += chr(ord(x)+key)
        print(plaintext)
    except:
        break

