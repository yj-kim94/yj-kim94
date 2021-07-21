import os
os.chdir("C://Users/김용진/Documents/Git")

with open("monoisotopic_mass.txt","r") as f :
  lines=f.readlines()

mass=[]
for line in lines :
  mass.append(line.strip().replace(" ",""))

mass_dict={}
for i in mass :
  mass_dict[i[0]]=i[1:]

with open("rosalind_prtm.txt","r") as f :
  amino_acid=f.readline().strip()

protein_mass=0

for i in list(amino_acid):
  protein_mass+=float(mass_dict[i])
  
result=round(protein_mass,3)
print(result)
