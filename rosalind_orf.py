import re
import os

os.chdir("C://Users/김용진/Documents/Git")
with open("dna_codon.txt","r") as f:
  lines=f.readlines()

#codon 딕셔너리 만들기
codon={}
for line in lines:
  line=line.strip().replace(" ","")
  if len(line)==16:
    codon[line[0:3]]=line[3]
    codon[line[4:7]]=line[7]
    codon[line[8:11]]=line[11]
    codon[line[12:15]]=line[15]
  else:
    codon[line[0:3]]=line[3:7]
    codon[line[7:10]]=line[10]
    codon[line[11:14]]=line[14]
    codon[line[15:18]]=line[18]

with open("rosalind_orf.txt","r") as f :
  lines=f.readlines()

dna_seq=""
for line in lines:
  if line[0]!=">":
    dna_seq+=line.strip()

dna_rev=""
for i in list(dna_seq):
  if i == "A":
    dna_rev+="T"
  elif i=="T":
    dna_rev+="A"
  elif i=="G":
    dna_rev+="C"
  else :
    dna_rev+="G"

dna_rev=dna_rev[::-1]

result_fwd=[]
for i in re.finditer("ATG",dna_seq):
  start=i.start()
  sub_str=dna_seq[start:]
  protein=""
  n=0
  while True :
    if sub_str[n:n+3] in ["TAA","TAG","TGA"]:
      result_fwd.append(protein)
      break
    elif n+3 > len(sub_str):
      break
    protein+=codon[sub_str[n:n+3]]
    n+=3

result_rev=[]
for i in re.finditer("ATG",dna_rev):
  start=i.start()
  sub_str=dna_rev[start:]
  protein=""
  n=0
  while True :
    if sub_str[n:n+3] in ["TAA","TAG","TGA"]:
      result_rev.append(protein)
      break
    elif n+3 > len(sub_str):
      break
    protein+=codon[sub_str[n:n+3]]
    n+=3

result=result_fwd+result_rev
for i in set(result):
  print(i)