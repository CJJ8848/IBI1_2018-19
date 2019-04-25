#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:18:53 2019

@author: cuijiajun
"""
# give a positive integer x    
x = 234
# check whether x is a even
while x>1:
    print (x)
    if x%2 ==0:
        x=x/2    
# if x is odd
    elif  x%2!=0:
        x=x*3+1

