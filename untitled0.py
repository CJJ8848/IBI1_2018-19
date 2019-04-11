#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:45:37 2019

@author: cuijiajun
"""
seq = input()
gcCount = []
def seq_GCRatio(sequence):
    #输入含有序列信息的字符串，输出该序列中的GC比
    GC_count = float(sequence.count('C') + sequence.count('G'))
    seq_length = len(sequence)
    GC_ratio = GC_count / seq_length * 1
    return GC_ratio
print (seq_GCRatio(seq))