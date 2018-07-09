#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:55:19 2018

@author: frank-lsy
"""

# importing the predict module
from mhcnuggets.src.predict import predict

# predicting new line separated peptides present in the peptides_path file 
# for MHC class_I allele HLA-A*02:01
predict(class_='I',
        peptides_path='mhcnuggets/mhcnuggets/data/test/test_peptides.peps', 
        mhc='HLA-A02:01', output = 'I.csv')
print("\n")
# similarly doing the same prediction for MHC class_II allele HLA-DRB1*01:01
predict(class_='II',
        peptides_path='mhcnuggets/mhcnuggets/data/test/test_peptides.peps', 
        mhc='HLA-DRB101:01', output = 'II.csv')
print("\n")
# as an example of prediction of rare alleles asking MHCnuggets to make predictions for HLA-A*02:60
# will make it search for the closest allele (HLA-A*02:01 in this case), and use the corresponding 
# network for prediction
predict(class_='I',
        peptides_path='mhcnuggets/mhcnuggets/data/test/test_peptides.peps', 
        mhc='HLA-A02:60', output = 'III.csv')