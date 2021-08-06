import os
import pandas as pd

os.chdir("C://Users/김용진/Documents/Git")

#문제 불러오기
with open("rosalind_cons.txt") as f :
  lines=f.readlines()

#서열 이름을 key, 서열을 value로 하는 딕셔너리 생성
def process_seq(lines):
  result={}
  for line in lines :
    line=line.strip()
    if line[0]==">":
      dict_key=line
      result[dict_key]=""
    else :
      dict_value=line
      result[dict_key]+=dict_value
  return result
seq_dict=process_seq(lines)

#Nucelotide 단위로 리스트에 묶기
seq_list=list(seq_dict.values())
result=[]
for i in seq_list:
  result.append(list(i))

#Pandas Dataframe 생성
df=pd.DataFrame(result)

#각 position 별로 nucelotide 개수를 담을 기본 문자열 포맷 생성
A="A: "
C="C: "
G="G: "
T="T: "

#각 position 별로 가장 빈도가 높은 nucelotide를 찾아 consensus sequence 구하기
consensus_seq=""
for i in range(df.shape[1]):
  seq_cols=list(df[i])
  num_of_A=seq_cols.count("A")
  num_of_C=seq_cols.count("C")
  num_of_G=seq_cols.count("G")
  num_of_T=seq_cols.count("T")
  A+=str(num_of_A)+" "
  C+=str(num_of_C)+" "
  G+=str(num_of_G)+" "
  T+=str(num_of_T)+" "

  seq_max=""
  compare_list=[num_of_A,num_of_C,num_of_G,num_of_T]
  max_position=compare_list.index(max(compare_list))
  
  if max_position == 0:
    seq_max+="A"
  elif max_position == 1:
    seq_max+="C"
  elif max_position == 2:
    seq_max+="G"
  elif max_position == 3:
    seq_max+="T"
  consensus_seq+=seq_max

#결과를 텍스트 파일로 저장
with open("rosalind_cons.output.txt","w") as f:
  f.write(consensus_seq)
  f.write("\n")
  f.write(A)
  f.write("\n")
  f.write(C)
  f.write("\n")
  f.write(G)
  f.write("\n")
  f.write(T)