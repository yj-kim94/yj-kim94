#파일을 불러온다.
import os
os.chdir("C://Users/김용진/Documents/Git")
with open("rosalind_revp.txt","r") as f :
  lines=f.readlines()

#빈 문자열을 생성한다.
sequence=""

# > 로 시작하지 않는 문자열을 sequence 변수에 반복해서 더한다.
for i in lines:
  if i[0]==">":
    continue
  else:
    sequence+=i.strip()

#palindrome sequence는 4~12로 길이가 제한되어 있어 range(4,13)을 이용
#for문으로 반복해서 palindrome sequence를 찾는 작업을 수행한다.
for i in range(4,13):
  n=0 #length 값이 설정되면 한칸씩 이동하면서 작업을 수행해야 하는데, 이를 위한 초기 n=0값 설정
  while True :
    if n+i > len(sequence):
      break #while문을 빠져나오기 위한 조건을 설정한다.
    result=sequence[n:n+i] #n+sequence 길이만큼을 indexing 해서 result 변수에 할당
    result_pal="" #빈 문자열을 palindrome sequence 변수에 할당
    for j in list(result): #for문으로 indexing한 result 변수의 상보적 서열을 만든다.
      if j=="A":
        result_pal+="T"
      elif j=="T":
        result_pal+="A"
      elif j=="G":
        result_pal+="C"
      else :
        result_pal+="G"
    result_pal=result_pal[::-1] #str[::-1]은 문자열을 거꾸로 만들 때 사용
    if result==result_pal: #indexing한 문자열과 palindrome sequence처럼 만든 서열이 동일할 경우 출력
      print(n+1,i)
    n=n+1 #n에 1을 더한 뒤 동일한 작업 수행