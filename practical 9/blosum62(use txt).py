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
<<<<<<< HEAD
=======


        

>>>>>>> master
def sc_di(sq1,sq2):
    sq1 = list(sq1)
    score = 0
    edit_distance = 0
    for i in range(len(sq1)):
<<<<<<< HEAD
        x = matrix[sq1[i]][sq2[i]]
=======
        x = blosum62[sq1[i]][sq2[i]]
>>>>>>> master
        score +=int(x)
        if sq1[i]!=sq2[i]:  
            edit_distance += 1      
    print ('score :',score)
    print ('distance :',edit_distance)
print('seq1 compared with seq2')
sc_di(seq1,seq2)
print('seq1 compared with seq3')
sc_di(seq1,seq3)
print('seq2 compared with seq3')
sc_di(seq2,seq3)
