import os
os.chdir("C://Users/김용진/Documents/Git")
n=int(input())
sample=list(range(1,1+n))
cases=1
for i in range(1,1+n):
  cases=cases*i
cases=str(cases)

import itertools
case_set=list(itertools.permutations(sample,n))

with open("outFile.txt","w") as f:
  f.write(cases)
  f.write("\n")
  for i in case_set:
    case=""
    for j in list(i):
      case+=str(j)+" "
    f.write(case)
    f.write("\n")