numbers1=[2,1,3,4,1]
numbers2=[5,0,2,7]
def solution(numbers):
  answer=[]
  #리스트에 있는 숫자 하나씩 기준으로 잡고 탐색
  for index in range(len(numbers)):
    #먼저 숫자 리스트를 복사한다.
    numbers_copy=numbers.copy()
    #기준 숫자를 ref_number로 저장
    ref_number=numbers_copy[index]
    #복사한 숫자 리스트에서 기준 숫자를 제거
    numbers_copy.remove(ref_number)
    #남은 숫자들을 기준 숫자와 더한 뒤 answer 리스트에 저장
    for number in numbers_copy :
      answer.append(ref_number+number)
  #중복 값을 제거하기 위해 set으로 변환한 뒤 list로 다시 변환
  answer=list(set(answer))
  #sort()로 오름차 순 정렬
  answer.sort()
  return answer

print(solution(numbers1))
print(solution(numbers2))