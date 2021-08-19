import re

def solution(new_id):
  #1단계 모든 대문자를 소문자로 치환
  new_id=new_id.lower()
  
  #2단계 영문자, 숫자, .,-,_를 제외한 문자를 제거
  tmp=""
  for i in list(new_id) :
    if i.isalpha() or i.isdigit() or i in ["-",".","_"]:
      tmp+=i
  new_id=tmp
  #new_id=re.sub("[^a-z1-9-.\_]","",new_id)

  #3단계 마침표가 두번 이상 반복되면 마침표 한개로 변경
  new_id=re.sub(r"[.]+",".",new_id)
  
  #4단계
  #문자열 시작이나 끝이 마침표인 경우 제거
  new_id=new_id.strip(".")
  
  #5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입
  if new_id =="":
    new_id+="a"

  #6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개 문자를 제외한 나머지 문자 제거
  if len(new_id) >= 16 :
    new_id=new_id[:15]
    #만약 제거 후 마침표가 new_id의 끝에 위치한다면 끝에 위치한 마침표 문자를 제거
    if new_id[-1]==".": 
      new_id=new_id[0:-1]

  #7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 길이가 3이 될 때 까지 반복해서 추가
  while len(new_id) < 3 :
    new_id+=new_id[-1]
  return new_id