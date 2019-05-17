#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:31:33 2019

@author: cuijiajun
"""
# import necessary libraries
import os
import numpy as np
import matplotlib.pyplot as plt
# change the work pathway so that all the files exist in this folder
os.chdir('/Users/cuijiajun/Desktop/IBI1_2018-19/practical 13')
# a function used to change xml to cps (from teacher)
def xml_to_cps():
    import os
    import xml.dom.minidom    
    # first, convert xml to cps 
    os.system("/Applications/COPASI/CopasiSE -i predator-prey.xml -s predator-prey.cps")
    # now comes the painful part. Just copy and paste this ok    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()
# use the function
xml_to_cps()
# open modelResults.csv
os.system ('/Applications/COPASI/CopasiSE predator-prey.cps')    
f = open("modelResults.csv")
# some lists
names = []  
result = []
results = []
# read the first line as name
for i in range(1):
    names = f.readline().strip()
# read the file to get results of each time point
for line in f:
    line=line.rstrip('\n')
    line=line.split(',')
    result = line
    results.append (result)
results = np.array(results)
results = results.astype(np.float)
# first ploting
plt.figure (figsize =(6,4),dpi=150)
plt.subplot(111)
# y axis
plt.plot(results[0:,1], label='Predator (b=0.02, d=0.4)')
plt.plot(results[0:,2], label='Prey (b=0.1,d=0.02)')
# title and label
plt.title('Time course')
plt.xlabel('Time')
plt.ylabel('populaton size')
plt.legend()
# save figure
plt.savefig(' Time course' ,type='png')
plt.show()

# second ploting (limit cycle)
plt.figure (figsize =(6,4),dpi=150)
plt.subplot(111)
# x,y axis
plt.plot(results[0:,1], results[0:,2])
# title and label
plt.title('limit cycle')
plt.xlabel('Predator population')
plt.ylabel('Prey population')
plt.legend()
# save figure
plt.savefig('limit cycle' ,type='png')
plt.show()

# pseudocode for Changing values and running the simulation again
#import re
#import xml.dom.minidom
# read predator-prey.xml 
# read parameter 
# get the value of k predator breeds, k predator dies, k prey breeds, k prey dies.
# change them by 
'''def change_node_properties(nodelist, kv_map, is_delete=False):
  for node in nodelist:
    for key in kv_map:
      if is_delete:
        if key in node.attrib:
          del node.attrib[key]
      else:
        node.set(key, kv_map.get(key))
'''
# then after change the values, follow the normal steps to draw new plots 
