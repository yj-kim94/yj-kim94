board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

def solution(board,moves):
  basket=[]
  answer=0
  #인형은 집게가 움직인 횟수만큼 상자에 담긴다.
  for move in moves :
    #집게가 움직인 위치에서 인형이 몇 번째 칸에 위치하고 있는지 탐색
    for i in range(len(board)):
      #맨 위부터 탐색하다 0이 아닌 숫자가 나오면 상자에 담고, 인형이 있던 칸을 0으로 만든다.
      if board[i][move-1] != 0 :
        basket.append(board[i][move-1])
        board[i][move-1]=0
        #상자에 인형이 2개 이상 채워지고 마지막에 들어온 인형이 그 전 인형과 같을 경우, 인형 두개가 사라지고 숫자는 2가 더해진다.
        if len(basket) >= 2 and basket[-1] == basket[-2] :
          basket=basket[:-2]
          answer+=2
        break
  return answer
solution(board,moves)