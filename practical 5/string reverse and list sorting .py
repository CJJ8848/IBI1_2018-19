#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:01:14 2019

@author: cuijiajun
"""

string = input ('give me a string of words: ')
string =  string [::-1]
string = string.split ()
string.sort()
string.reverse()
print (string)
