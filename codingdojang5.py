limit=int(input("정수를 입력하세요."))

result=[0,1]
n=0

while True : 
    a= result[n]+result[n+1]
    if a > limit :
        for i in result :
            print(i)
        break
    result.append(a)
    n=n+1