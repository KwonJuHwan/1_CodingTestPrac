# 경로 찾기

n = int(input())

A = [0 for _ in range(n)]

for i in range(n):
    A[i] = list(map(int, input().split()))

for k in range(n):
    for s in range(n):
        for e in range(n):
            if A[s][k] + A[k][e] == 2:
                A[s][e] = 1

for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
