
'''
def DNA_strand(dna):
   res = []
   for i in dna:
      if i == "A":
         res.append('T')
      if i == 'T':
         res.append('A')
      if i == 'C':
         res.append('G')
      if i == 'G':
         res.append('C')
   return ''.join(res)
'''


pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))


print(DNA_strand("ATTGC"))
