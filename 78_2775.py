# 부녀 회장이 될테야

# D[a][b] = D[a-1][1] + ... +D[a-1][b-1] +  D[a-1][b]
# 여기서 D[a-1][1] + ... +D[a-1][b-1] 이 부분을 D[a][b-1]로 치환 가능 (부분 문제들의 합)
# 이렇게 부분 문제의 합으로 문제를 분석 해보는 능력을 길러야 한다.

import sys

input = sys.stdin.readline

D = [[0 for _ in range(15)] for _ in range(15)]

for i in range(15):
    D[0][i] = i
    D[i][1] = 1

# 3중으로 해도 풀리긴함
# for i in range(1, 15):
#     for j in range(2, 15):
#         for k in range(1, j+1):
#             D[i][j] += D[i - 1][k]

for i in range(1, 15):
    for j in range(2, 15):
        D[i][j] = D[i][j - 1] + D[i - 1][j]

n = int(input())

for _ in range(n):
    a = int(input())
    b = int(input())
    print(D[a][b])
