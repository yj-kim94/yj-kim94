'''
Translating RNA into Protein
'''

#convert codon table into dictionary
with open("rosalind3.txt","r") as f:
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

#translation
with open("rosalind_prot.txt","r") as f:
  line=f.readline()
RNA=line

protein=""
start=RNA.find("AUG")
RNA=RNA[start:]
while True :
    if amino_acid[RNA[0:3]]=="Stop":
        break
    protein=protein+amino_acid[RNA[0:3]]
    RNA=RNA[3:]
print(protein)