import os
os.chdir("C://Users/김용진/Documents/Git")

with open("rosalind_lexv.txt") as f:
  lines=f.readlines()

sample=lines[0].strip().split(" ")

length=lines[1].strip()
length=int(length)

all_string=[]
for i in range(1,length+1):
  all_string=all_string+list(itertools.product(sample,repeat=i))

result=[]
for i in all_string:
  sub_string="".join(list(i))
  result.append(sub_string)

order="".join(sample)
sorted_result=sorted(result,key=lambda word:[order.index(c) for c in word])

with open("outFile.txt","w") as f:
  for i in sorted_result:
    f.write(i)
    f.write("\n")