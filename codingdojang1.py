'''
10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
'''
#3의 배수 구하기
three=[]
result=0
while result < 1000:
  three.append(result)
  result=result+3

print(three)

#5의 배수 구하기
five=[]
result=0
while result < 1000:
  five.append(result)
  result=result+5

print(five)

#두 리스트 합치기
total=three+five

#모든 요소값 더하기
result=0
for i in total :
  result=result+i

print(result)

#266333 -->정답확인못함