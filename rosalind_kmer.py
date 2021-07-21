import os
os.chdir("C://Users/김용진/Documents/Git")

import itertools
import re

with open("rosalind_kmer.txt","r") as f :
  lines=f.readlines()

sequence=""
for line in lines[1:]:
  sequence+=line.strip()

target=[]

for i in list(itertools.product(["A","C","G","T"],repeat=4)):
  case="".join(i)
  target.append(case)

result=""

for i in target :
  indice=0
  position=0
  n=0
  while True:
    position=sequence[0+indice:].find(i)
    if position <0:
      break
    indice=indice+position+1
    n=n+1
  result=result+str(n)+ " "
print(result)
