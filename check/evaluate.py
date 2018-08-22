#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:23:32 2018

@author: frank-lsy
"""

# importing the evaluation module
from mhcnuggets.src.evaluate import test

# Evaluating training performance of model test.h5 on peptides 
# correspondingn to class I allele HLA-B*08:01 in database given by the 
# data path. 
test(class_='I',
     data='mhcnuggets/mhcnuggets/data/production/mhcI/curated_training_data.csv',
     model_path='test_A02-a01.h5', mhc='HLA-B08:01')