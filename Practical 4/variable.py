#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:17:51 2019

@author: cuijiajun
"""
# store 123 to variable a
# store 123123 to variable b
a = 123
b =123123
# Can b be divided by 7?
if b % 7==0 :
    print ('true')
# check whether c==a 
c = b/7
d =c/11
e = d/13
if e==a:
    print ('same!')
# Boolean part
# X is false, Y is true    
X = 3>4
Y = 2>1
# define Z and W
Z = (X and not Y) or (not X and Y)
W = X!=Y
# check whether Z and W are true
if Z is True:
    print ('Y is ture so Z is true')
else:
    print ('False')
if W is True:
     print ('Y is ture so W is true')
else:
    print ('False')
    