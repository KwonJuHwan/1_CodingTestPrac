# 퇴사 준비 하기
# 최대한 많은 이익 얻기
# 일반식 + 예외로 문제 풀기 
import sys

input = sys.stdin.readline

n = int(input())

T = [0] * (n + 1)
P = [0] * (n + 1)
visit = [False] * (n + 1)
# D[i] = i번째 날부터 퇴사 하는 날까지 벌 수 있는 최대 수익
D = [0] * (n + 2)

for i in range(1, n + 1):
    a, b = map(int, input().split())
    T[i] = a
    P[i] = b

for i in range(n, 0, -1):
    # range out ( 예외 )
    if i + T[i] > n + 1:
        D[i] = D[i + 1]
    else:
        # 일반식
        D[i] = max(P[i] + D[i + T[i]], D[i + 1])

print(D[1])
