#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:38:23 2019

@author: cuijiajun
"""
import re
#from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse ("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName ("term")
geneslist = [["id", "name", "defination","count"],]
genelist = []
parentlist = []
def count_childnode (GOID):
    childnode = 0
    for term in terms:
        is_a = term.getElementsByTagName ("is_a")
        parentlist.append(is_a)
    if re.search (GOID,str(parentlist)):
        childnode += 1
    return childnode
  
for term in terms:
    id = term.getElementsByTagName ("id")[0].childNodes[0].nodeValue
    name = term.getElementsByTagName ("name")[0].childNodes[0].nodeValue
    #is_a = term.getElementsByTagName ("is_a")[0].childNodes[0].nodeValue
    defstr = term.getElementsByTagName ("defstr")[0].childNodes[0].nodeValue
       
    if re.search('autophagosome',defstr):
        countchild = count_childnode(id)
        genelist = [id,name,defstr,countchild] 
        geneslist.append (genelist)

import openpyxl


def write_excel_xlsx(path, sheet_name, value):
    index = len(value)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.cell(row=i+1, column=j+1, value=str(value[i][j]))
    workbook.save(path)
    print("success!")
book_name_xlsx = 'autophagosome (myself).xlsx'
 
sheet_name_xlsx = 'autophagosome genes'
 
value =  geneslist#elementCount]]
 
write_excel_xlsx(book_name_xlsx, sheet_name_xlsx, value)
