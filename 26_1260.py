# BFS, DFS의 기본틀

from collections import deque

N,M,V = map(int,input().split())
A=[[] for _ in range(N+1)]
visit=[False]*(N+1)
#1부터 N까지이므로, N+1개 생성

for _ in range(M):
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(1,N+1):
    A[i].sort()

def DFS(a):
    print(a,end=" ")
    visit[a]=True
    for i in A[a]:
        if(not visit[i]):
            DFS(i)


DFS(V)
visit2=[False]*(N+1)
print()

# queue를 이용해서 처음 세팅 후, queue가 empty될때까지, 계속 실행
def BFS(a):
    queue=deque()
    queue.append(a)
    visit2[a]=True
    while queue:
        now = queue.popleft()
        print(now,end=" ")
        for i in A[now]:
            if(not visit2[i]):
                visit2[i]=True
                queue.append(i)


BFS(V)



