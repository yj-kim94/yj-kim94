with open("rosalind_splc.txt","r") as f :
  lines=f.readlines()

seq_dict={}

for i in range(len(lines)):
    if lines[i][0]==">":
        seq_dict[lines[i].strip()]=""
        n=1      
        while lines[i+n][0]!=">":
            seq_dict[lines[i].strip()]+=lines[i+n].strip()
            n+=1
            if len(lines)==(i+n):
                break
    else : continue

seq_ref=list(seq_dict.keys())[0]
intron=list(seq_dict.keys())[1:]

result=seq_dict[seq_ref]
for i in intron:
  result=result.replace(seq_dict[i],"")
RNA=result.replace("T","U")

with open("codon.txt","r") as f:
    lines=f.readlines()

codon=[]
for i in lines:
    codon.append(i.strip().replace(" ",""))

amino_acid={}
for i in codon:
    if i.find("Stop")<0:
        amino_acid[i[0:3]]=i[3]
        amino_acid[i[4:7]]=i[7]
        amino_acid[i[8:11]]=i[11]
        amino_acid[i[12:15]]=i[15]
    else:
        amino_acid[i[0:3]]=i[3:7]
        amino_acid[i[7:10]]=i[10]
        amino_acid[i[11:14]]=i[14]
        amino_acid[i[15:18]]=i[18]

protein=""
start=RNA.find("AUG")
RNA=RNA[start:]

while True :
    if amino_acid[RNA[0:3]]=="Stop":
      break
    protein=protein+amino_acid[RNA[0:3]]
    RNA=RNA[3:]

print(protein)