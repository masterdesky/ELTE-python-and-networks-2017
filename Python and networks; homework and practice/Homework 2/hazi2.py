import sys

#definiate variable for specific file
FILE_NAME = 'hs_alt_CHM1_1.1_chr1.fa'

#open file (should be in the directory with .py inside)
GEN = open(FILE_NAME,'r').read()

#count
countAT = GEN.count('AT')
countTA = GEN.count('TA')
countAG = GEN.count('AG')
countGA = GEN.count('GA')
countAC = GEN.count('AC')
countCA = GEN.count('CA')
countTG = GEN.count('TG')
countGT = GEN.count('GT')
countTC = GEN.count('TC')
countCT = GEN.count('CT')
countGC = GEN.count('GC')
countCG = GEN.count('CG')
countA_T = GEN.count('A\nT')
countT_A = GEN.count('T\nA')
countA_G = GEN.count('A\nG')
countG_A = GEN.count('G\nA')
countA_C = GEN.count('A\nC')
countC_A = GEN.count('C\nA')
countT_G = GEN.count('T\nG')
countG_T = GEN.count('G\nT')
countT_C = GEN.count('T\nC')
countC_T = GEN.count('C\nT')
countG_C = GEN.count('G\nC')
countC_G = GEN.count('C\nG')

#print occurences
print('AT&TA: %d' % (int(countAT)+int(countTA)+int(countA_T)+int(countT_A)))
print('AG&GA: %d' % (int(countAG)+int(countGA)+int(countA_G)+int(countG_A)))
print('AC&CA: %d' % (int(countAC)+int(countCA)+int(countA_C)+int(countC_A)))
print('TG&GT: %d' % (int(countTG)+int(countGT)+int(countT_G)+int(countG_T)))
print('TC&CT: %d' % (int(countTC)+int(countCT)+int(countT_C)+int(countC_T)))
print('GC&CG: %d' % (int(countGC)+int(countCG)+int(countG_C)+int(countC_G)))