# 일반적인 최소 공통 조상 구하기
# 75번은 BFS 로 해보기
# depth가 같을때, 비교해야됨
# 초기화하는거 외워두자

import sys

input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(100000)
from collections import deque

n = int(input())

# 부모 노드 / 깊이

tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
depth = [0] * (n + 1)
parent = [0] * (n + 1)
# 루트 노드 초기화 설정
depth[1] = 0
parent[1] = 0

for _ in range(0, n - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)


# def BFS(node):
#     queue= deque()
#     queue.append(node)
#     visited[node]=True
#     level=1
#     now_size=1
#     count=0
#     while queue:
#         now_node = queue.popleft()
#         for next in tree[now_node]:
#             if not visited[next]:
#                 visited[next]=True
#                 queue.append(next)
#                 parent[next]=now_node
#                 depth[next]=level
#         count +=1
#         if count == now_size:
#             count = 0
#             now_size = len(queue)
#             level +=1
#
# BFS(1)

# def DFS(i, dep):
#     visited[i] = True
#     depth[i] = dep
#     for now in tree[i]:
#         if not visited[now]:
#             parent[now] = i
#             DFS(now, dep + 1)


DFS(1, 0)


# depth 가 같을때, 비교 해야됨

def LCA(a, b):
    if depth[a] < depth[b]:
        temp = a
        a = b
        b = temp
    # a 가 맞추기
    while depth[a] != depth[b]:
        a = parent[a]

    # depth 같아짐
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


question = int(input())

for _ in range(question):
    a, b = map(int, input().split())
    print(str(LCA(a, b)))
    print("\n")

# 부모 노드, 깊이 업데이트
