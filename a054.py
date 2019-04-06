#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 02:30:48 2019

@author: sam0225
"""


while True:
    try:
        dict1={'A':10,'J':18,'S':26,'B':11,'K':19,'T':27,'C':12,'L':20,'U':28,
               'D':13,'M':21,'V':29,'E':14,'N':22,'W':32,'F':15,'O':35,'X':30,
               'Y':31,'G':16,'H':17,'Q':24,'Z':33,'I':34,'R':25,'P':23 }
        id_text = input()
        c = 10-int(id_text[8])
        id_text = id_text[0:8]
        total = 0
        n = 8
        s= ""
        for i in id_text:
            total += int(i)*n
            n-=1
        
        for i in range(10,36):
            if (i//10+i%10*9+total)%10==c:
                s += list (dict1.keys()) [list (dict1.values()).index(i)]
        print(s)
    except:
        break