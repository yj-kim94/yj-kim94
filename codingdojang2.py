'''
1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?

8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
(※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)
'''
#풀이방법
'''
1. 1씩 숫자를 더해서 8이 포함되어 있을 경우 count 해서 개수를 저장

'''

#1부터 1씩 더해가며 8 개수 count
a=0
result=[]
for i in range(1,10001):
  if "8" in str(i):
    number=str(i).count("8")
    result.append(int(number))
  else :
    continue
print(result)

#모든 result 더하기
sum=0
for i in result:
  sum+=i
print(sum)

#정답 : 4000 맞았다.

