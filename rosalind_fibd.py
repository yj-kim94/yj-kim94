import os
os.chdir("C://Users/김용진/Documents/Git")

#문제 불러오기
with open("rosalind_fibd.txt","r") as f:
  line=f.readline()

#번식 개월 수와 생존 가능 개월 수 변수에 할당
month=int(line.split(" ")[0])
live=int(line.split(" ")[1])

#첫 달 자손 세대 토끼쌍 수 1 저장
start=[1]

#첫 달 부모 세대 토끼쌍 수 0 저장
for i in range(live-1):
  start.append(0)

#매달 발생하는 토끼쌍 수를 저장할 리스트 생성
all_number_of_rabbit=[start]

#for문으로 매달 발생하는 토끼쌍 수 계산
for i in range(month-1):
  tmp=[]
  new_born=0
  for k in range(1,live):
    new_born=new_born+all_number_of_rabbit[-1][k]
  tmp.append(new_born)
  for k in range(live-1):
    tmp.append(all_number_of_rabbit[-1][k])
  all_number_of_rabbit.append(tmp)

#마지막 달 토끼쌍 수 합 구하기
result=0
for i in all_number_of_rabbit[-1]:
  result+=i
print(result)