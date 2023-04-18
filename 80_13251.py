# 조약돌 꺼내기
# n 개의 조약돌 , 조약돌 색깔 1~M
# k 개를 뽑았을떄, 모두 같은 색일 확률
import sys
input=sys.stdin.readline

m = int(input())

A = list(map(int, input().split()))

# 전체 개수
total = 0
for i in range(m):
    total += A[i]

C = [[0 for _ in range(total+1)] for _ in range(total+1)]

for i in range(total+1):
    C[i][0] = 1
    C[i][i] = 1
    C[i][1] = i

for i in range(2, total+1):
    for j in range(1, i):
        C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

k = int(input())

up = 0
for i in range(m):
    up += C[A[i]][k]

print(up / C[total][k])
