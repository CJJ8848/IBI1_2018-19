#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:12:22 2019

@author: cuijiajun
"""

seq1 = 'MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
# Sequence of a mouse SOD2 protein (NP_038699.2)
seq2 = 'MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
# A random sequence
seq3 = 'WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'

    
with open('BLOSUM62.txt') as matrix_file:
    matrix = matrix_file.read()
    lines = matrix.strip().split('\n')
    header = lines.pop(0)
    columns = header.split()
    matrix = {}
    for row in lines:
        entries = row.split()
        row_name = entries.pop(0)
        matrix[row_name] = {}
        for column_name in columns:
            matrix[row_name][column_name] = entries.pop(0)


        

seq1 = list(seq1)
seq2 = list(seq2)
seq3 = list(seq3)


score_x = 0
score_y = 0
score_z = 0
edit_distance_x = 0
edit_distance_y = 0
edit_distance_z = 0
for i in range(len(seq1)):
    x = matrix[seq1[i]][seq2[i]]
    y = matrix[seq1[i]][seq3[i]]
    z = matrix[seq3[i]][seq2[i]]
    score_x +=int(x)
    score_y +=int(y)
    score_z +=int(z)
    if seq1[i]!=seq2[i]:
       edit_distance_x += 1
    if seq1[i]!=seq3[i]:
       edit_distance_y += 1
    if seq3[i]!=seq2[i]:
       edit_distance_z += 1
      
print ('score of 1,2:',score_x)
print ('edit_distance_x:',edit_distance_x)
print ('score of 1,3:',score_y)
print ('edit_distance_y:',edit_distance_y)
print ('score of 2,3:',score_z)
print ('edit_distance_z:',edit_distance_z)