#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:09:18 2018

@author: frank-lsy
"""

def get_kmer_peptides(whole_peptides,k,file):
    peptides = []
    f = open(file,'w+')
    for i in range(len(whole_peptides)-k):
        peptides.append(whole_peptides[i:i+9])
        print(whole_peptides[i:i+9],file = f) #输出到文件
    f.close()
    return peptides



whole_peptides = 'MQCLAAALKDETNMSGGGEQADILPANYVVKDRWKVLKKIGGGGFGEIYEAMDLLTRENVALKVESAQQPKQVLKMEVAVLKKLQGKDHVCRFIGCGRNEKFNYVVMQLQGRNLADLRRSQPRGTFTLSTTLRLGKQILESIEAIHSVGFLHRDIKPSNFAMGRLPSTYRKCYMLDFGLARQYTNTTGDVRPPRNVAGFRGTVRYASVNAHKNREMGRHDDLWSLFYMLVEFAVGQLPWRKIKDKEQVGMIKEKYEHRMLLKHMPSEFHLFLDHIASLDYFTKPDYQLIMSVFENSMKERGIAENEAFDWEKAGTDALLSTSTSTPPQQNTRQTAAMFGVVNVTPVPGDLLRENTEDVLQGEHLSDQENAPPILPGRPSEGLGPSPHLVPHPGGPEAEVWEETDVNRNKLRINIGKSPCVEEEQSRGMGVPSSPVRAPPDSPTTPVRSLRYRRVNSPESERLSTADGRVELPERRSRMDLPGSPSRQACSSQPAQMLSVDTGHADRQASGRMDVSASVEQEALSNAFRSVPLAEEEDFDSKEWVIIDKETELKDFPPGAEPSTSGTTDEEPEELRPLPEEGEERRRLGAEPTVRPRGRSMQALAEEDLQHLPPQPLPPQLSQGDGRSETSQPPTPGSPSHSPLHSGPRPRRRESDPTGPQRQVFSVAPPFEVNGLPRAVPLSLPYQDFKRDLSDYRERARLLNRVRRVGFSHMLLTTPQVPLAPVQPQANGKEEEEEEEEDEEEEEEDEEEEEEEEEEEEEEEEEEEEEEEAAAAVALGEVLGPRSGSSSEGSERSTDRSQEGAPSTLLADDQKESRGRASMADGDLEPEEGSKTLVLVSPGDMKKSPVTAELAPDPDLGTLAALTPQHERPQPTGSQLDVSEPGTLSSVLKSEPKPPGPGAGLGAGTVTTGVGGVAVTSSPFTKVERTFVHIAEKTHLNVMSSGGQALRSEEFSAGGELGLELASDGGAVEEGARAPLENGLALSGLNGAEIEGSALSGAPRETPSEMATNSLPNGPALADGPAPVSPLEPSPEKVATISPRRHAMPGSRPRSRIPVLLSEEDTGSEPSGSLSAKERWSKRARPQQDLARLVMEKRQGRLLLRLASGASSSSSEEQRRASETLSGTGSEEDTPASEPAAALPRKSGRAAATRSRIPRPIGLRMPMPVAAQQPASRSHGAAPALDTAITSRLQLQTPPGSATAADLRPKQPPGRGLGPGRAQAGARPPAPRSPRLPASTSAARNASASPRSQSLSRRESPSPSHQARPGVPPPRGVPPARAQPDGTPSPGGSKKGPRGKLQAQRATTKGRAGGAEGRAGAR'
k = 9
file = 'test.peps'
result = get_kmer_peptides(whole_peptides,k,file)
print(result)