#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:21:12 2019

@author: cuijiajun
"""
#mport necessary librabies
import numpy as np
import matplotlib.pyplot as plt
# a function to deal with different S0 and vaccination rate
def para(s0,rate):
    #input parameters 
    S0 = s0
    I0 = 1
    R0 = 0
    N = 10000
    beta = 0.3
    gamma = 0.05
    # make arrays
    Sarr = [S0]
    Iarrs = [I0]
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
        Iarrs=np.append(Iarrs,(I0))
        Rarr=np.append(Rarr,(R0))    
    plt.plot(Iarrs[:], label=rate)
#ploting
plt.figure (figsize =(6,4),dpi=150)
plt.subplot(111)
x = np.linspace(0,1000)
plt.title('SIR Model')
plt.xlabel('Time')
plt.ylabel('number of people')
plt.xlabel('Time')
# use finctions
para(9999,'0%')
para(8999,'10%')
para(7999,'20%')
para(6999,'30%')
para(5999,'40%')
para(4999,'50%')
para(3999,'60%')
para(2999,'70%')
para(1999,'80%')
para(999,'90%')
para(0,'100%')
plt.legend()
# save the figure
plt.savefig('SIR_vaccination Model' ,type='png')
# show the figure
plt.show()