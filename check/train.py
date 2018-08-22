#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:08:14 2018

@author: frank-lsy
"""

# importing the train module
from mhcnuggets.src.train import train

# training MHC class_I allele HLA-A*02:01 using data present in the data file from scratch 
train(class_='I', data='mhcnuggets/mhcnuggets/data/production/mhcI/curated_training_data.csv',
      mhc='HLA-A02:01', save_path='test_A02:01.h5', n_epoch=100)
print ('\n')
"""
# training MHC class I allele HLA-B*08:01 using transfer weights from class I allele
# HLA-A*02:01
train(class_='I', data='mhcnuggets/mhcnuggets/data/production/mhcI/curated_training_data.csv',
      mhc='HLA-B08:01', save_path='test_B08:01.h5', n_epoch=100, transfer_path='test_A02:01.h5')
print ('\n')

# training MHC class I allele HLA-B*08:02 using transfer weights from class I allele
# HLA-B*08:01, note that this is only train for n_epochs=25
train(class_='I', data='mhcnuggets/mhcnuggets/data/production/mhcI/curated_training_data.csv',
      mhc='HLA-B08:02', save_path='test_B08:02.h5', n_epoch=25, transfer_path='test_B08:01.h5')
"""