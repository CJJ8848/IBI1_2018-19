#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:04:15 2019

@author: cuijiajun
"""
# Sequence for human SOD2 protein (NP_000627.2)
seq1 = 'MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
# Sequence of a mouse SOD2 protein (NP_038699.2)
seq2 = 'MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
# A random sequence
seq3 = 'WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'
# import blosum62 as dictionary
blosum62 = {
             'A':{'A':  4, 'C':  0, 'B': -2, 'E': -1,
                  'D': -2, 'G':  0, 'F': -2, 'I': -1, 'H': -2,
                  'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1,
                  'P': -1, 'S':  1, 'R': -1, 'T':  0, 'W': -3,
                  'V':  0, 'Y': -2, 'X':  0, 'Z': -1},

             'C':{'A':  0, 'C':  9, 'B': -3, 'E': -4,
                  'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3,
                  'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3,
                  'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2,
                  'V': -1, 'Y': -2, 'X': -2, 'Z': -3},

             'B':{'A': -2, 'C': -3, 'B':  4, 'E':  1,
                  'D':  4, 'G': -1, 'F': -3, 'I': -3, 'H':  0,
                  'K':  0, 'M': -3, 'L': -4, 'N':  3, 'Q':  0,
                  'P': -2, 'S':  0, 'R': -1, 'T': -1, 'W': -4,
                  'V': -3, 'Y': -3, 'X': -1, 'Z':  1},

             'E':{'A': -1, 'C': -4, 'B':  1, 'E':  5,
                  'D':  2, 'G': -2, 'F': -3, 'I': -3, 'H':  0,
                  'K':  1, 'M': -2, 'L': -3, 'N':  0, 'Q':  2,
                  'P': -1, 'S':  0, 'R':  0, 'T': -1, 'W': -3,
                  'V': -2, 'Y': -2, 'X': -1, 'Z':  4},

             'D':{'A': -2, 'C': -3, 'B':  4, 'E':  2,
                  'D':  6, 'G': -1, 'F': -3, 'I': -3, 'H': -1,
                  'K': -1, 'M': -3, 'L': -4, 'N':  1, 'Q':  0,
                  'P': -1, 'S':  0, 'R': -2, 'T': -1, 'W': -4,
                  'V': -3, 'Y': -3, 'X': -1, 'Z':  1},

             'G':{'A':  0, 'C': -3, 'B': -1, 'E': -2,
                  'D': -1, 'G':  6, 'F': -3, 'I': -4, 'H': -2,
                  'K': -2, 'M': -3, 'L': -4, 'N':  0, 'Q': -2,
                  'P': -2, 'S':  0, 'R': -2, 'T': -2, 'W': -2,
                  'V': -3, 'Y': -3, 'X': -1, 'Z': -2},

             'F':{'A': -2, 'C': -2, 'B': -3, 'E': -3,
                  'D': -3, 'G': -3, 'F':  6, 'I':  0, 'H': -1,
                  'K': -3, 'M':  0, 'L':  0, 'N': -3, 'Q': -3,
                  'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W':  1,
                  'V': -1, 'Y':  3, 'X': -1, 'Z': -3},

             'I':{'A': -1, 'C': -1, 'B': -3, 'E': -3,
                  'D': -3, 'G': -4, 'F':  0, 'I':  4, 'H': -3,
                  'K': -3, 'M':  1, 'L':  2, 'N': -3, 'Q': -3,
                  'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3,
                  'V':  3, 'Y': -1, 'X': -1, 'Z': -3},

             'H':{'A': -2, 'C': -3, 'B':  0, 'E':  0,
                  'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H':  8,
                  'K': -1, 'M': -2, 'L': -3, 'N':  1, 'Q':  0,
                  'P': -2, 'S': -1, 'R':  0, 'T': -2, 'W': -2,
                  'V': -3, 'Y':  2, 'X': -1, 'Z':  0},

             'K':{'A': -1, 'C': -3, 'B':  0, 'E':  1,
                  'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1,
                  'K':  5, 'M': -1, 'L': -2, 'N':  0, 'Q':  1,
                  'P': -1, 'S':  0, 'R':  2, 'T': -1, 'W': -3,
                  'V': -2, 'Y': -2, 'X': -1, 'Z':  1},

             'M':{'A': -1, 'C': -1, 'B': -3, 'E': -2,
                  'D': -3, 'G': -3, 'F':  0, 'I':  1, 'H': -2,
                  'K': -1, 'M':  5, 'L':  2, 'N': -2, 'Q':  0,
                  'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1,
                  'V':  1, 'Y': -1, 'X': -1, 'Z': -1},

             'L':{'A': -1, 'C': -1, 'B': -4, 'E': -3,
                  'D': -4, 'G': -4, 'F':  0, 'I':  2, 'H': -3,
                  'K': -2, 'M':  2, 'L':  4, 'N': -3, 'Q': -2,
                  'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2,
                  'V':  1, 'Y': -1, 'X': -1, 'Z': -3},

             'N':{'A': -2, 'C': -3, 'B':  3, 'E':  0,
                  'D':  1, 'G':  0, 'F': -3, 'I': -3, 'H':  1,
                  'K':  0, 'M': -2, 'L': -3, 'N':  6, 'Q':  0,
                  'P': -2, 'S':  1, 'R':  0, 'T':  0, 'W': -4,
                  'V': -3, 'Y': -2, 'X': -1, 'Z':  0},

             'Q':{'A': -1, 'C': -3, 'B':  0, 'E':  2,
                  'D':  0, 'G': -2, 'F': -3, 'I': -3, 'H':  0,
                  'K':  1, 'M':  0, 'L': -2, 'N':  0, 'Q':  5,
                  'P': -1, 'S':  0, 'R':  1, 'T': -1, 'W': -2,
                  'V': -2, 'Y': -1, 'X': -1, 'Z':  3},

             'P':{'A': -1, 'C': -3, 'B': -2, 'E': -1,
                  'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2,
                  'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1,
                  'P':  7, 'S': -1, 'R': -2, 'T': -1, 'W': -4,
                  'V': -2, 'Y': -3, 'X': -2, 'Z': -1},

             'S':{'A':  1, 'C': -1, 'B':  0, 'E':  0,
                  'D':  0, 'G':  0, 'F': -2, 'I': -2, 'H': -1,
                  'K':  0, 'M': -1, 'L': -2, 'N':  1, 'Q':  0,
                  'P': -1, 'S':  4, 'R': -1, 'T':  1, 'W': -3,
                  'V': -2, 'Y': -2, 'X':  0, 'Z':  0},

             'R':{'A': -1, 'C': -3, 'B': -1, 'E':  0,
                  'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H':  0,
                  'K':  2, 'M': -1, 'L': -2, 'N':  0, 'Q':  1,
                  'P': -2, 'S': -1, 'R':  5, 'T': -1, 'W': -3,
                  'V': -3, 'Y': -2, 'X': -1, 'Z':  0},

             'T':{'A':  0, 'C': -1, 'B': -1, 'E': -1,
                  'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2,
                  'K': -1, 'M': -1, 'L': -1, 'N':  0, 'Q': -1,
                  'P': -1, 'S':  1, 'R': -1, 'T':  5, 'W': -2,
                  'V':  0, 'Y': -2, 'X':  0, 'Z': -1},

             'W':{'A': -3, 'C': -2, 'B': -4, 'E': -3,
                  'D': -4, 'G': -2, 'F':  1, 'I': -3, 'H': -2,
                  'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2,
                  'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11,
                  'V': -3, 'Y':  2, 'X': -2, 'Z': -3},

             'V':{'A':  0, 'C': -1, 'B': -3, 'E': -2,
                  'D': -3, 'G': -3, 'F': -1, 'I':  3, 'H': -3,
                  'K': -2, 'M':  1, 'L':  1, 'N': -3, 'Q': -2,
                  'P': -2, 'S': -2, 'R': -3, 'T':  0, 'W': -3,
                  'V':  4, 'Y': -1, 'X': -1, 'Z': -2},

             'Y':{'A': -2, 'C': -2, 'B': -3, 'E': -2,
                  'D': -3, 'G': -3, 'F':  3, 'I': -1, 'H':  2,
                  'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1,
                  'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W':  2,
                  'V': -1, 'Y':  7, 'X': -1, 'Z': -2},

             'X':{'A':  0, 'C': -2, 'B': -1, 'E': -1,
                  'D': -1, 'G': -1, 'F': -1, 'I': -1, 'H': -1,
                  'K': -1, 'M': -1, 'L': -1, 'N': -1, 'Q': -1,
                  'P': -2, 'S':  0, 'R': -1, 'T':  0, 'W': -2,
                  'V': -1, 'Y': -1, 'X': -1, 'Z': -1},

             'Z':{'A': -1, 'C': -3, 'B':  1, 'E':  4,
                  'D':  1, 'G': -2, 'F': -3, 'I': -3, 'H':  0,
                  'K':  1, 'M': -1, 'L': -3, 'N':  0, 'Q':  3,
                  'P': -1, 'S':  0, 'R':  0, 'T': -1, 'W': -3,
                  'V': -2, 'Y': -2, 'X': -1, 'Z': 4}}

# a function to mark according to the dict
def sc_di(sq1,sq2):
# score part   
    sq1 = list(sq1)
    score = 0
    edit_distance = 0
    for i in range(len(sq1)):
        x = blosum62[sq1[i]][sq2[i]]
        score +=int(x)
# distance part
        if sq1[i]!=sq2[i]:  
            edit_distance += 1      
    print ('score :',score)
    print ('distance :',edit_distance)
# print scores of three combinations    
print('compare seq1 with seq2')
sc_di(seq1,seq2)
print('compare seq1 with seq3')
sc_di(seq1,seq3)
print('compare seq2 with seq3')
sc_di(seq2,seq3)