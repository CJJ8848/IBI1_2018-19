#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:01:14 2019

@author: cuijiajun
"""
# input some words
string = input ('give me a string of words: ')
# reverse the elements
string =  string [::-1]
# split the string with space
string = string.split ()
# order the string 
string.sort()
# reverse the order
string.reverse()
# output
print (string)
