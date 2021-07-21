import os
os.chdir("C://Users/김용진/Documents/Git")

with open("rosalind_lexf.txt") as f:
  lines=f.readlines()

sample=lines[0].strip().split(" ")

length=lines[1].strip()
length=int(length)

import itertools

with open("outFile.txt","w") as f:
  for i in list(itertools.product(sample,repeat=length)):
    result="".join(list(i))
    f.write(result)
    f.write("\n")