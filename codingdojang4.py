"""
A씨는 게시판 프로그램을 작성하고 있다.

A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.

입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
출력 : 총페이지수

A씨가 필요한 프로그램을 작성하시오.

"""

def test(m,n):
    if n == 0:
        print("n은 0보다 커야합니다. 프로그램을 종료합니다.")
    elif m==0 :
        result=0
        return result
    elif m<=n:
        result=1
        return result
    elif m>n and m%n !=0 :
        result=m//n+1
        return result
    elif m>n and m%n ==0 :
        result=m//n
        return result

m=int(input("총 건수를 입력하십시오."))
n=int(input("한 페이지에 보여줄 게시물 수를 입력하십시오."))

value=test(m,n)
print(value)

