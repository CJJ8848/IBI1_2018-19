#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:38:23 2019

@author: cuijiajun
"""
def Child (id , resultSet):
    for term in terms:
        # parents is a list containing all parents of one term
        parents = term.getElementsByTagName('is_a')
        # geneid is a string, the id of one term 
        geneid = term.getElementsByTagName('id')[0].childNodes[0].data
        # for each parent of one term if there is a id in parents, add the geneid of one term(a child)
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultSet.add(geneid)
                Child(geneid, resultSet)
# a function to write excel
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
import re
import xml.dom.minidom
# read go_obo.xml 
DOMTree = xml.dom.minidom.parse ("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName ("term")
# a list called geneslist and another one called genelist
geneslist = [["id", "name", "defination","count"],]
genelist = []
# get the value of id, name and defstr
for term in terms:
    id = term.getElementsByTagName ("id")[0].childNodes[0].nodeValue
    name = term.getElementsByTagName ("name")[0].childNodes[0].nodeValue
    defstr = term.getElementsByTagName ("defstr")[0].childNodes[0].nodeValue
# search for autophagosome in defstr      
    if re.search('autophagosome',defstr):
        resultSet = set()
        Child(id,resultSet)
        countchild = len(resultSet)
        genelist = [id,name,defstr,countchild] 
        geneslist.append (genelist)

import openpyxl
# name of excel sheet
book_name_xlsx = 'autophagosome (myself).xlsx'
sheet_name_xlsx = 'autophagosome genes' 
# value is the list called geneslist
value =  geneslist
# write in
write_excel_xlsx(book_name_xlsx, sheet_name_xlsx, value)