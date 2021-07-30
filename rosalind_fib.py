import os
os.chdir("C://Users/김용진/Documents/Git")

#문제 불러오기
with open("rosalind_fib.txt","r") as f:
  line=f.read()
line=line.strip().split(" ")

#개월 수와 낳는 자손 수 설정하기
month=int(line[0])
born=int(line[1])

#첫 달 토끼 커플 분류하기
new = [1]
old = [0]

#n개월 뒤 토끼 커플 수 구하는 함수 작성
def get_rabbit_pairs(month,born):
  for i in range(month-1):
    #다음 달 자손 세대 커플 수와 부모 세대 커플 수 구하기
    new_rabbit=born*old[i]
    old_rabbit=new[i]+old[i]
    
    new.append(new_rabbit)
    old.append(old_rabbit)

  all_rabbit_pairs=new[-1]+old[-1]
  return all_rabbit_pairs

#함수 적용하여 토끼 커플 수 구하기
result=get_rabbit_pairs(month,born)

#결과 출력
print(result)