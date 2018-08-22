#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:45:04 2018

@author: frank-lsy
"""

import numpy as np
import re
import sys
import os

def parse_dna_change(dna_change):
    parsed_dna_change = []
    
    parsed_dna_change.append(dna_change)
    #取出第几号染色体
    if (dna_change[4]>='0' and dna_change[4]<='9'):
        parsed_dna_change.append(dna_change[3:5])
    else:
        parsed_dna_change.append(dna_change[3:4])
        
    #取出位点
    locus = re.findall(r"\.(\d+)",dna_change,re.M|re.I)
    parsed_dna_change.append(locus)
    
    #取出变异类型
    Delete_Search = re.compile(r"del")
    Substitude_Search = re.compile(r">")
    Insert_Search = re.compile(r"ins")
    
    if (Delete_Search.search(dna_change)):
        parsed_dna_change.append("Deletion")
        bases = re.findall(r"del([A-Z]*)",dna_change,re.M|re.I)
        parsed_dna_change.append(bases)
    elif (Substitude_Search.search(dna_change)):
        parsed_dna_change.append("Substitution")
        bases1 = re.findall(r"([A-Z]*)>",dna_change,re.M|re.I)
        parsed_dna_change.append(bases1)
        bases2 = re.findall(r">([A-Z]*)",dna_change,re.M|re.I)
        parsed_dna_change.append(bases2)
    elif (Insert_Search.search(dna_change)):
        parsed_dna_change.append("Insertion")
        bases = re.findall(r"ins([A-Z]*)",dna_change,re.M|re.I)
        parsed_dna_change.append(bases)
    else:
        parsed_dna_change.append("Unknown Change")
    
    return parsed_dna_change

dna_change1 = 'chr7:g.6751496delA'
dna_change2 = 'chr12:g.56085070G>A'
dna_change3 = 'chr17:g.30379664_30379665insC'
print(parse_dna_change(dna_change3))