# P[K][N] = N 번 노드의 2^K 번째 부모의 노드 번호
# P[K][N] = P[K-1][P[K-1][N]]
# K : 트리의 깊이 > 2^k 를 만족 하는 최댓값


import sys

input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(1000000)
from collections import deque

n = int(input())
tree = [[0] for _ in range(n + 1)]
visited = [False] * (n + 1)
depth = [0] * (n + 1)

for _ in range(n - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)


# max_depth 구하기
temp = 1
maxQ = 0
while temp <= n:
    temp <<= 1
    maxQ += 1

parent = [[0 for _ in range(n + 1)] for _ in range(maxQ + 1)]


#parent 세팅
def dfs2(i, dep):
    visited[i] = True
    depth[i] = dep
    for next in tree[i]:
        if not visited[next]:
            parent[0][next] = i
            dfs2(next, dep + 1)
dfs2(1, 0)

for k in range(1, maxQ + 1):
    for n in range(1, n + 1):
        parent[k][n] = parent[k - 1][parent[k - 1][n]]


# 무슨 느낌인지는 알겠음
def lca(a, b):
    if depth[a] > depth[b]:
        temp = a
        a = b
        b = temp

    # 기존의 1씩 탐색 -> 2의 제곱씩 탐색
    for k in range(maxQ, -1, -1):
        if pow(2, k) <= depth[b] - depth[a]:  # 두 노드의 depth 차이 찾기
            if depth[a] <= depth[parent[k][b]]:  # depth 차이만큼 노드 b 올리기
                b = parent[k][b]  # 위로 땡기기

    # 최대 -> 최소로 탐색해야지, a에 최소 공통 조상이 담김

    for k in range(maxQ, -1, -1):
        if a == b:
            break
        # 같으면, 아직 최소 공통 조상까지 도달하지 못한 것
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    result = a
    # 홀수 예외 처리?
    if a != b:
        result = parent[0][result]
    return result


m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(str(lca(a, b)))
    print("\n")

    # 15
    # 1 2
    # 1 3
    # 2 4
    # 3 7
    # 6 2
    # 3 8
    # 4 9
    # 2 5
    # 5 11
    # 7 13
    # 10 4
    # 11 15
    # 12 5
    # 14 7
    # 6
    # 6 11
    # 10 9
    # 2 6
    # 7 6
    # 8 13
    # 8 15
