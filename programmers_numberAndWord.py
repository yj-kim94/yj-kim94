s="one4seveneight"
number_dict={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

def solution(s):
  #딕셔너리 모든 key 값을 탐색
  for i in list(number_dict.keys()):
    #문자열 내 key 값 존재 유무 판별
    if s.find(i) != (-1):
      old=i
      new=number_dict[i]
      #문자열을 숫자(문자열)로 치환
      s=s.replace(old,new)
  return int(s)

solution(s)