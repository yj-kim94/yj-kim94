#Finding a Spliced Motif
#solution for rosalind_sseq 
#solved by yjkim

import os
os.chdir("C://Users/김용진/Documents/Git")

import itertools

#문제를 불러온다.
with open("rosalind_sseq.txt","r") as f :
  lines=f.readlines()

#빈 딕셔너리를 생성한다.
sequence={}

#for문으로 각 line을 읽어 첫 시작에 따라 key 값으로 설정할지, value 값으로 설정할지 정하여 딕셔너리를 완성한다.
for line in lines :
  if line[0]==">":
    value=""
    key=line.strip()
    continue
  else : 
    value+=line.strip()
  sequence[key]=value

s=sequence[list(sequence.keys())[0]]
t=sequence[list(sequence.keys())[1]]

def get_all_index(t):
  result=[]
  for i in list(t):
    for j in re.finditer(i,s):
      result.append(j.start())
  return result


def get_spliced_index(all_index):
  result=[]
  for index in all_index:
    if len(result)==0:
      result.append(index)
    elif result[-1] < index-1 and s[result[-1]]!=s[index]:
      result.append(index)

  add_one=[]
  for i in result :
    add_one.append(str(i+1))
  return add_one

all_index=get_all_index(t)
result=get_spliced_index(all_index)

print(" ".join(result))