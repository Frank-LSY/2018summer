#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:01:14 2018

@author: frank-lsy
"""
from mhcnuggets.src.aa_embeddings import MHCI_MASK_LEN
import mhcnuggets.src.dataset as dataset
import mhcnuggets.src.predict as predict
import os
import numpy as np
import csv

"""
标准化mhc
"""
mhc = 'HLA-A02:01'
new_mhc = dataset.standardize_mhc(mhc)#标准化mhc模式
#print (new_mhc)


"""
对原csv数据中的ic50用三种方式输出
"""
data = '2018summer/mhcnuggets-2.0/mhcnuggets/data/production/mhcI/curated_training_data.csv'
with open(data,'r') as csvfile:
    reader = csv.DictReader(csvfile)
    ic50_data = [row['IC50(nM)'] for row in reader]
    
regression_ic50 = []
binarized_ic50 = []

for ic50 in ic50_data:
    float_ic50_data = float(ic50)
    regression_ic50.append(dataset.map_ic50_for_regression(float_ic50_data))
    binarized_ic50.append(dataset.binarize_ic50(float_ic50_data))  
    
count = 0
for item in binarized_ic50:
    if item ==0:
        count += 1    
#print (regression_ic50)
#print (count)

"""
mask_peptides干啥的
"""
mask_len = MHCI_MASK_LEN
with open(data,'r') as csvfile:
    reader = csv.DictReader(csvfile)
    peptides = [row['peptide'] for row in reader]
masked_peptides = dataset.mask_peptides(peptides, max_len = mask_len)
#print (masked_peptides)

"""
cut_pad_peptides干啥的
"""
padded_peptides = dataset.cut_pad_peptides(peptides)
#print(padded_peptides)

"""
tensorize_keras干啥的
"""
tensorized = dataset.tensorize_keras(padded_peptides,embed_type = "onehot")
print(tensorized)
