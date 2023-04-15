# 이항 계수 구하기 2
# 어떤 값으로 나누어라 -> 모듈러 계산 (MOD)

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
mod = 10007

D = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

for i in range(2, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i - 1][j] % mod + D[i - 1][j - 1] % mod

print(D[n][k] % mod)
