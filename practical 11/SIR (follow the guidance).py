#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:29:51 2019

@author: cuijiajun
"""
#mport necessary librabies
import numpy as np
import matplotlib.pyplot as plt
#input parameters 
S0 = 9999
I0 = 1
R0 = 0
N = 10000
beta = 0.3
gamma = 0.05
# make arrays
Sarr = [S0]
Iarr = [I0]
Rarr = [R0]
# count loop time
t = 0 
# a loop to count S,I,R
while t<=1000:
    # rate
    rateI = beta*I0/N
    rateR = gamma 
    t +=1
    # random choose 0 or 1 
    A = np.random.choice(range(2),S0,p=[(1-rateI),rateI])
    B = np.random.choice(range(2),I0,p=[(1-rateR),rateR])
    # add new people to each group
    S0 = S0-sum(A)
    I0 = I0+sum(A)-sum(B)
    R0 = R0+sum(B)
    Sarr=np.append(Sarr,(S0))
    Iarr=np.append(Iarr,(I0))
    Rarr=np.append(Rarr,(R0)) 
# ploting
plt.figure (figsize =(6,4),dpi=150)
plt.subplot(111)
# x axis
x = np.linspace(0,1000)
# y axis
plt.plot(Sarr[:], label='Susceptible')
plt.plot(Iarr[:], label='Infected')
plt.plot(Rarr[:], label='Recovered')
# title and label
plt.title('SIR Model')
plt.xlabel('Time')
plt.ylabel('number of people')
plt.xlabel('Time')
plt.legend()
# save figure
plt.savefig('SIR Model 1' ,type='png')
plt.show()