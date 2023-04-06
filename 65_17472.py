# 다리 만들기
# 섬을 노드로 생각
from collections import deque

n, m = map(int, input().split())
A = [[0 for _ in range(m)] for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, +1]

for i in range(n):
    A[i] = list(map(int, input().split()))

mq = deque()
nq = deque()
count = 2


# BFS를 이용해서 섬 -> 노드 처리
def BFS(x, y):
    global count
    if not visit[x][y]:
        visit[x][y] = True
        while (mq):
            pop = mq.pop()
            nq.appendleft((count - 1, pop[0], pop[1]))
            a = pop[0]
            b = pop[1]
            for i in range(4):
                if 0 <= a + dx[i] < n and 0 <= b + dy[i] < m:
                    if not visit[a + dx[i]][b + dy[i]] and A[a + dx[i]][b + dy[i]] == 1:
                        visit[a + dx[i]][b + dy[i]] = True
                        A[a + dx[i]][b + dy[i]] = count
                        mq.appendleft((a + dx[i], b + dy[i]))
                        BFS(a + dx[i], b + dy[i])


# BFS를 통해, 섬 ->노드
for i in range(n):
    for j in range(m):
        if A[i][j] != 0 and not visit[i][j]:
            A[i][j] = count
            mq.appendleft((i, j))
            BFS(i, j)
            count += 1

nlist = [[] for _ in range(count)]
# 지도 좌표 따기 for 엣지 탐색
while nq:
    pop = nq.pop()
    nlist[pop[0]].append((pop[1], pop[2]))

# 가능한 다리 싹다 넣기 (엣지 리스트 만드는 행위랑 같음)
edge = []
for i in range(1, count):
    for now in nlist[i]:
        x = now[0]
        y = now[1]
        for j in range(4):
            alength = 0
            xtemp = dx[j]
            ytemp = dy[j]
            while 0 <= x + xtemp and x + xtemp < n and 0 <= y + ytemp and y + ytemp < m:
                if A[x + xtemp][y + ytemp] == A[x][y]:  # 같은 땅 더 진행할 수 없음
                    break
                elif A[x + xtemp][y + ytemp] != 0:  # 다른 땅 도착
                    if alength > 1:  # 문제 조건 다리의 길이는 2 이상
                        edge.append((alength, A[x][y], A[x + xtemp][y + ytemp]))  # w, s, e
                    break
                else:  # 계속 탐색
                    alength += 1  # 길이 +1
                if xtemp > 0:  # 탐색한 방향으로 계속 탐색
                    xtemp += 1
                elif xtemp < 0:
                    xtemp -= 1
                elif ytemp > 0:
                    ytemp += 1
                elif ytemp < 0:
                    ytemp -= 1

parent = [0] * (count + 1)
for i in range(2, count + 1):
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


result = 0
useEdge = 0
edge.sort()

for w, s, e in edge:
    if find(s) != find(e):
        result += w
        union(s, e)
        useEdge += 1

if useEdge == count - 3:
    print(result)
else:
    print(-1)
