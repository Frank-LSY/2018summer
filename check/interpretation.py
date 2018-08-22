#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:02:33 2018
###RNA翻译成peptide###
@author: frank-lsy
"""

protein = {'Alanine':'A', 'Phenylalanine':'F', 
           'Cysteine':'C', 'Selenocysteine':'U', 
           'Aspartate':'D', 'Asparagine':'N', 
           'Glutamate':'E', 'Glutamine':'Q', 
           'Glycine':'G', 'Histidine':'H', 
           'Leucine':'L', 'Isoleucine':'I', 
           'Lysine': 'K', 'Pyrrolusine':'O', 
           'Methionine':'M', 'Proline':'P', 
           'Arginine':'R', 'Serine':'S', 
           'Threonine':'T', 'Valine':'V', 
           'Tryptophan':'W', 'Tyrosine':'Y'}

codon = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 
         'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
         'UAU':'Y', 'UAC':'Y', 'UAA':'Z', 'UAG':'Z',
         'UGU':'C', 'UGC':'C', 'UGA':'Z', 'UGG':'W',
         'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
         'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
         'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
         'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
         'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
         'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
         'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
         'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
         'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
         'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
         'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
         'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

def interpretate(rna):
    rna_upper = rna.upper()
    peptide = ''
    i = 0
    while (i<len(rna_upper)):
        code = codon[rna_upper[i:i+3]]
        peptide = peptide + code
        if (code == 'Z'):
            return peptide
        i += 3
    return peptide


rna = 'uuaucguaaaaugau'

peptide = interpretate(rna)

print (peptide)