#다익스트라 제약조건: 항상 양수
#다익스트라: 최단거리를 구하는 알고리즘
# 출발노드와 다른 모든 노드들 간의 최단거리
#우선순위 큐를 사용해서 시간초과 면하기 -> 최소거리 먼저 탐색 + 최소거리 아니면 queue 넣지 않음

import sys
from queue import PriorityQueue
input=sys.stdin.readline
n,m= map(int,input().split())
start= int(input())
A=[[]for _ in range(n+1)]
result=[sys.maxsize]*(n+1)
visited=[False]*(n+1)
queue=PriorityQueue()


for i in range(m):
    u,v,w= map(int,input().split())
    A[u].append((v,w))

result[start]=0
queue.put((0,start))

while(queue.qsize()>0):
    now = queue.get()
    if(visited[now[1]]):
        continue
    visited[now[1]]=True
    for next in A[now[1]]:
        if(result[next[0]] > result[now[1]] + next[1]):
            result[next[0]]= result[now[1]] + next[1]
            queue.put((result[next[0]],next[0])) #최단거리일때에만, 넣어도 안넣는 노드없음 /처음에 11로 초기화를 했기때문

for i in range(1,n+1):
    if(visited[i]):
        print(result[i])
    else:
        print("INF")




