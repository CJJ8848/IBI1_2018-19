#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:00:26 2019

@author: cuijiajun
"""
#  give n 
n = int(input ())
i = 16
# n is even 
if n % 2 ==0:
    result = '0'
# n is odd    
elif n % 2 > 0 :
    n = n -1 
    result = '1'
# add 2**i to result
while n > 0:
    while n < 2**i:
          i = i-1
            
    while  i >= 0 and n >= 2**i:
           result = result+ '+'+'2**'+str (i)
           n = n - 2**i
           i = i - 1
#print result
print (result)