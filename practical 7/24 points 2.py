#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:45:10 2019

@author: cuijiajun
"""
import itertools
import re
n =input('Please input numbers to computer 24 and use comma to divide them:')
n = n.split(',')
m=[]
for i in n:
     m.append(int(i))
     if int(i) >=24:
         print('The input number must be integers from 1 to 23')
op=['+','-','*','/'] 
ol = list(itertools.product(op,repeat=1))
r=0   
if int(i)<=24:
    print(m)
    for e in m:
        from itertolls import permutations
        m=permutations(m)
        sub1=m[0:len[m]/2]
        sub2=m[len[m]/2:len[m]]
        sub1=re.sub('',ol,sub1)
        sub2=re.sub('',ol,sub2)
        
        
