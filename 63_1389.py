# 케빈 베이컨의 6단계 법칙
# 케빈 베이컨의 수가 가장 적은 사람을 구하기
import sys

n, m = map(int, input().split())

D = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
A = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    D[a][b] = 1
    D[b][a] = 1

for i in range(n + 1):
    D[i][i] = 0

for k in range(1,n + 1):
    for s in range(1,n + 1):
        for e in range(1,n + 1):
            if D[s][e] > D[s][k] + D[k][e]:
                D[s][e] = D[s][k] + D[k][e]

for i in range(1,n + 1):
    for j in range(1,n+1):
        A[i]+=D[i][j]

m_min=sys.maxsize

for i in range(1,n+1):
    if m_min > A[i]:
        m_min = A[i]

for i in range(1,n+1):
    if m_min == A[i]:
        print(i)
        break
