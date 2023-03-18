# P[N] = 1부터 N까지 범위에서 N과 서로소인 자연수의 개수
import math
n=int(input())
result=n

for p in range(2, int(math.sqrt(n))+1):
    if( n % p == 0):
        result -= result/p
        while(n%p ==0):
            n /=p

if n>1:
    result -= result / n

print(int(result))