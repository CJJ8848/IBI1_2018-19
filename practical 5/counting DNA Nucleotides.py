#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:40:16 2019

@author: cuijiajun
"""

DNA = input ('give me a sequence of DNA: ')
mydict = {}
for word in DNA :
    if word in mydict :
        mydict[word] += 1
    else :
        mydict[word] = 1
print (mydict)

import matplotlib.pyplot as plt

labels = 'A','T','C','G'
sizes = [mydict['A'],mydict['T'], mydict['C'], mydict['G'] ]
explode = (0,0,0,0)
plt.pie(sizes, explode=explode, labels =labels, autopct = '%1.1f%%', shadow = True, startangle= 90)
plt.axis('equal')

plt.show()
