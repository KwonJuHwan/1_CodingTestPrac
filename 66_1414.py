# 불우이웃돕기
# 모든 엣지의 길이 - 최소 신장 트리의 길이
import sys

input = sys.stdin.readline

n = int(input())
sum = 0
edge = []

for i in range(n):
    inpt = list(input())
    for j in range(n):
        temp = 0
        if 'a' <= inpt[j] <= 'z':
            temp = ord(inpt[j]) - ord('a') + 1
        elif 'A' <= inpt[j] <= 'Z':
            temp = ord(inpt[j]) - ord('A') + 27
        sum += temp
        if i != j and temp != 0:  # 사이클 X + 길이 없음 X
            edge.append((temp, i, j))

parent = [0] * (n)

for i in range(n):
    parent[i] = i


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


edge.sort()
s_min = 0
haveEdge = 0
for w, s, e in edge:
    if find(s) != find(e):
        s_min += w
        union(s, e)
        haveEdge += 1

if haveEdge == n - 1:
    print(sum - s_min)
else:
    print(-1)

