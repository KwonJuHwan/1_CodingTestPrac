# 다리 놓기
# 서쪽: N - 동쪽: M
# 개수 n만큼 다리를 짓고, 겹쳐질 수 없음 -> 조합 (정렬 X)
# M개의 다리가 N개의 다리를 선택
# mCn
import sys
input=sys.stdin.readline

t = int(input())

C = [[0 for _ in range(30)] for _ in range(30)]

for i in range(30):
    C[i][i] = 1
    C[i][0] = 1
    C[i][1] = i

for i in range(2, 30):
    for j in range(1, i):
        C[i][j] = C[i - 1][j] + C[i - 1][j - 1]

for _ in range(t):
    n, m = map(int, input().split())
    print(C[m][n])
