# 전체 경로의 최단 경로는 부분 경로의 최단 경로의 조합으로 이뤄진다.
# 모든 노드 간의 최단 거리를 알려주는 것이 특징
# 삼중 for 문 k - s - e
# 경유지인 k를 기준으로 계산하기 위해서
# D[s][e] = Math.min(D[s][e],D[s][k]+D[k][e])
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

D = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if D[a][b] > c: #여러 길이 있을 수도 있으므로
        D[a][b] = c

for i in range(1, n + 1):  # 시작과 끝이 같으면, 0으로 초기화
    D[i][i] = 0

for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if D[s][e] > D[s][k] + D[k][e]:
                D[s][e] = D[s][k] + D[k][e]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if D[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(D[i][j], end=' ')
    print()
