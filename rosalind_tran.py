import os
os.chdir("C://Users/김용진/Documents/Git")
with open("rosalind_tran.txt","r") as f :
  lines=f.readlines()

sequence={}
for line in lines :
  if line[0]==">":
    value=""
    key=line.strip()
    continue
  else : 
    value+=line.strip()
  sequence[key]=value

keys=list(sequence.keys())
seq_1=sequence[keys[0]]
seq_2=sequence[keys[1]]

transition=0
transversion=0
for i in range(len(seq_1)):
  if seq_1[i]==seq_2[i]:
    continue
  else :
    if seq_1[i]=="A" and seq_2[i]=="G":
      transition+=1
    elif seq_1[i]=="G" and seq_2[i]=="A":
      transition+=1
    elif seq_1[i]=="C" and seq_2[i]=="T":
      transition+=1
    elif seq_1[i]=="T" and seq_2[i]=="C":
      transition+=1
    else :
      transversion+=1
ratio=transition/transversion
print(ratio)