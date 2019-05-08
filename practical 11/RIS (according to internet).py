#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:01:35 2019

@author: cuijiajun
"""

#import libraries
import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np
# input parameters
beta=0.3
gamma=0.05
TS=1.0
ND=1000
S0=9999/10000
I0=1/10000
INPUT = (S0, I0, 0.0)
# a function to calculate 
def diff_eqs(INP,t):
	Y=np.zeros((3))
	V = INP
	Y[0] = - beta * V[0] * V[1]
	Y[1] = beta * V[0] * V[1] - gamma * V[1]
	Y[2] = gamma * V[1]
	return Y   # For odeint
# time course 
t_start = 0.0; t_end = ND; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)
# use the function
RES = spi.odeint(diff_eqs,INPUT,t_range)
#Ploting
plt.figure (figsize =(6,4),dpi=150)
plt.subplot(111)
x = np.linspace(0,1000)
plt.plot(RES[:,0], label='Susceptible')
plt.plot(RES[:,1], label='Infected')
plt.plot(RES[:,2], label='Recovered')
plt.title('SIR Model')
plt.xlabel('Time')
plt.ylabel('number of people')
plt.xlabel('Time')
plt.legend()
# save the figure
plt.savefig('SIR Model 2' ,type='png')
plt.show()
