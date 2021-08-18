array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array,commands) :
  result=[]
  for command in commands:
    start=command[0]-1
    end=command[1]
    position=command[2]-1
    sampled_list=array[start:end]
    sampled_list.sort()
    result.append(sampled_list[position])
  return result

result=solution(array,commands)
print(result)