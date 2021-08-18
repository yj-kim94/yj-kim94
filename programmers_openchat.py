logs=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def check_changes_in_name(logs):
  id_name={}
  for log in logs :
    move_message=log.split(" ")[0]
    if move_message=="Enter" or move_message=="Change"  :
      user_id=log.split(" ")[1]
      user_name=log.split(" ")[2]
      id_name[user_id]=user_name
  return id_name

def solution(logs):
  id_name=check_changes_in_name(logs)
  result=[]
  for log in logs:
    move_message=log.split(" ")[0]
    user_id=log.split(" ")[1]
    user_name=id_name[user_id]
    if move_message=="Enter":
      result.append("{0}님이 들어왔습니다.".format(user_name))
    elif move_message=="Leave":
      result.append("{0}님이 나갔습니다.".format(user_name))
  return result

result=solution(logs)
print(result)