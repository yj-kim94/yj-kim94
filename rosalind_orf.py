import re
import os

os.chdir("C://Users/김용진/Documents/Git")

#DNA codon table 불러오기
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

#문제 불러오기
with open("rosalind_orf.txt","r") as f :
  lines=f.readlines()

#DNA sequence를 한 문자열로 만들기
dna_seq=""
for line in lines:
  if line[0]!=">":
    dna_seq+=line.strip()

#상보적 서열 만들기
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

#모든 ATG 시작 위치를 찾고 코돈 테이블을 참고하여 단백질 서열 이어붙이기
result_fwd=[]
for i in re.finditer("ATG",dna_seq):
  start=i.start()
  sub_str=dna_seq[start:]
  protein=""
  n=0
  while True :
    if sub_str[n:n+3] in ["TAA","TAG","TGA"]: #stop codon일 경우 while 문 멈추기
      result_fwd.append(protein)
      break
    elif n+3 > len(sub_str): #stop codon이 계속 안 나오면 멈추기
      break
    protein+=codon[sub_str[n:n+3]]
    n+=3

#상보적 서열에 대해서도 수행
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

#결과 합치기
result=result_fwd+result_rev

#중복 값을 없애기 위해 집합 자료형으로 바꾼 뒤 결과 출력
for i in set(result):
  print(i)