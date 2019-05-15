#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:12:22 2019

@author: cuijiajun
"""
# Sequence for human SOD2 protein (NP_000627.2)
seq1 = 'MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
# Sequence of a mouse SOD2 protein (NP_038699.2)
seq2 = 'MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
# A random sequence
seq3 = 'WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'
# read blosum62.txt   
with open('BLOSUM62.txt') as matrix_file:
    matrix = matrix_file.read()
    lines = matrix.strip().split('\n')
    header = lines.pop(0)
    columns = header.split()
    matrix = {}
# construct a dictionary
    for row in lines:
        entries = row.split()
        row_name = entries.pop(0)
        matrix[row_name] = {}
        for column_name in columns:
            matrix[row_name][column_name] = entries.pop(0)
# a function to mark according to the dict
def sc_di(sq1,sq2):
# score part   
    sq1 = list(sq1)
    score = 0
    edit_distance = 0
    for i in range(len(sq1)):
        x = matrix[sq1[i]][sq2[i]]
        score +=int(x)
# distance part
        if sq1[i]!=sq2[i]:  
            edit_distance += 1  
# %identity 
    print('%identity :',(1-int(edit_distance)/len(sq1))*100,'%')
    print ('score :',score)
    print ('distance :',edit_distance)

# print scores of three combinations    
print('compare human seq1 with mouse seq2')
sc_di(seq1,seq2)    
print('compare mouse seq2 with random seq3')
sc_di(seq2,seq3)
print('compare random seq3 with human seq1')
sc_di(seq3,seq1)
