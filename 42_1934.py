#유클리드 호제법
#a와b의 최소 공배수 = a*b/ a,b의 최대 공약수 ->재귀함수 형태로 쉽게 구현

def gcd(s,e):
    if(e==0):
        return s
    else:
        return gcd(e, s%e)

t= int(input())

for i in range(t):
    s,e =map(int,input().split())
    result= s*e / gcd(s,e)
    print(int(result))

