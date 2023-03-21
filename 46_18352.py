#특정 거리의 도시 찾기
#최단거리(BFS)를 활용해야하므로 DFS을 사용할 수 없음
#depth값을 visit에 넣으면서, 공간 최소화
import sys
from collections import deque
input=sys.stdin.readline

#노드 개수, 엣지 개수, depth, 시작 노드
#4          4         2     1
n,m,k,x=map(int,input().split())
A=[[] for _ in range(n+1)]
visited=[-1]*(n+1)
novisit=True


for i in range(m):
    s,e=map(int,input().split())
    A[s].append(e) #단방향

def BFS(v):
    queue= deque()
    queue.append(v)
    visited[v]+=1
    while(queue):
        now = queue.popleft()
        for i in A[now]:
            if(visited[i] == -1):
                visited[i]=visited[now]+1
                queue.append(i)

BFS(x)
for i in range(n+1):
    if(visited[i]==k): #어차피 작은수부터 탐색하므로, 오름차순 정렬
       print(i)
       novisit=False
if(novisit):
    print(-1)
