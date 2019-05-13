#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:04:58 2019

@author: cuijiajun
"""
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# input the two parameters
beta = 0.3
gamma = 0.05
# make an array for susceptible population
population = np.zeros((100, 100))
# choose one infected people randomly 
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
t = 0
while t< 100:
    # maps for different t
    if t == 0:
        plt.figure(figsize = (6, 4), dpi = 150)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    elif t == 9:
        plt.figure(figsize = (6, 4), dpi = 150)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    elif t == 49:
        plt.figure(figsize = (6, 4), dpi = 150)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    elif t == 99:
        plt.figure(figsize = (6, 4), dpi = 150)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    t += 1
    # find infected points
    infectedIndex = np.where(population==1)    
    for i in range(len(infectedIndex[0])):
        # get x, y for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect all 8 neighbours 
        for xNeighbour in range(x-1,x+2):
                for yNeighbour in range(y-1,y+2):
                    if (xNeighbour,yNeighbour) != (x,y):
                        # make sure not fall off an edge
                        if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                            # only infect uninfected ones 
                            if population[xNeighbour,yNeighbour]==0:
                                population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
                            # only recover unrecovered ones