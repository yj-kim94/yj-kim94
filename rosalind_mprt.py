import requests
import re

#문제 불러오기
with open("rosalind_mprt.txt","r") as f:
  lines=f.readlines()

#id 리스트를 저장할 빈 리스트 생성
uniprot_id=[]
for line in lines :
  uniprot_id.append(line.strip())

#PROTEIN fasta 서열을 가져올 URL templete 만들어놓기
PROTEIN_TMP="http://www.uniprot.org/uniprot/{}.fasta"

#각 id 별로 N-glycosylation site 찾아서 출력하기
for i in uniprot_id:
  PROTEIN_URL=PROTEIN_TMP.format(i)
  response=requests.get(PROTEIN_URL)
  PROTEIN_SEQ="".join(response.text.split("\n")[1:])
  result=[str(i.start()+1) for i in re.finditer("N[^P][ST][^P]",PROTEIN_SEQ)]
  if len(result)==0:
    continue
  print(i)
  print(" ".join(set(result)))