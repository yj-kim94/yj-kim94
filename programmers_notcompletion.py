def solution(participants,completion):
  participants.sort()
  completion.sort()
  answer=""
  for i in range(len(completion)):
    if participants[i] != completion[i]:
      answer+=participants[i]
      break
    elif i==(len(completion)-1) :
      answer=participants[i+1]
  return answer