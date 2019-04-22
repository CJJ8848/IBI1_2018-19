#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:40:16 2019

@author: cuijiajun
"""
# input some sequence
DNA = input ('give me a sequence of DNA: ')
# construct mydict
mydict = {}
# show the times words appear
# if word in ['A','T','C','G'] : can allow you to input letters except ATCG
for word in DNA :
    if word in ['A','T','C','G'] :
        if word in mydict :
            mydict[word] += 1
        else :
            mydict[word] = 1
# output
print (mydict)
# get a plot
import matplotlib.pyplot as plt
# give the labels
labels = mydict.keys()
# give the sizes of labels
sizes = mydict.values()
# it can allow you to input a DNA with just one or two letters (e.g. ATTT)
explode = [0]*len(labels)
# autopct : means the number will in the shape of 1.0, 
# shadow: choose whether pie has shadow 
# startangle : it is beautiful if the startgngle is 90
# plt.axis ('equal'): make the pie be a circle.  
plt.pie(sizes, explode=explode, labels =labels, autopct = '%1.1f%%', shadow = True, startangle= 90)
plt.axis('equal')
# output
plt.show()