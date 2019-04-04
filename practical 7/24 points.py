#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:59:25 2019

@author: cuijiajun
"""
# inout
n =input('Please input numbers to computer 24 and use comma to divide them:')
# split with comma to make n a list
n = n.split(',')
#print (n)
# judge whether the numbers are smaller than 24
m=[]
for i in n:
     m.append(int(i))
     if int(i) >=24:
         print('The input number must be integers from 1 to 23')
         break
if int(i)<=24:
    r=0
# a function about the operator    
    def compute(x,y,op):
        if op=='+':return x+y
        elif op=='*':return x*y
        elif op=='-':return x-y
        else:return x/y if y else None
# a function about permutation 
    def exp(p,iter=0):
    
        from itertools import permutations
        if len(p)==1:return [(p[0],str(p[0]))]
        operation = ['+','-','*','/']
        ret = []
        p = permutations(p) if iter==0 else [p]
        for array_n in p:
            global r
            r=r+1
            #print(array_n)
            for num in range(1,len(array_n)):
                r=r+1
                ret1 = exp(array_n[:num],iter+1)
                ret2 = exp(array_n[num:],iter+1)
                for op in operation: 
                    r=r+1
                    for va1,expression in ret1:
                        r=r+1
                        if va1==None:continue
                        for va2,expression2 in ret2:
                            r=r+1
                            if va2==None:continue
                            combined_exp = '{}{}' if expression.isalnum() else '({}){}'
                            combined_exp += '{}' if expression2.isalnum() else '({})'
                            new_val = compute(va1,va2,op)
                            ret.append((new_val,combined_exp.format(expression,op,expression2)))
                            if iter==0 and new_val==24:
        
                                return 'yes',''.join(e+'' for x,e in ret if x==24)
        return ret
    import re
    if re.search(r'yes',str(exp(m))):
        print(exp(m))
        print('recursion times:',r)
    else:
        print('no output')

    
       
       
        