import sys
sys.setrecursionlimit(10**7) #재귀함수 사용할때, 필수
input=sys.stdin.readline

#효율적으로 해킹하기

# N개의 컴퓨터, 가장많은 노드와 연결되어있는 노드 찾기
# 3 1 입력 -> 3이 1를 신뢰한다. 1을 해킹하면 3도 해킹한다
# 최대 Depth를 가진 노드 출력
# DFS 활용시 시간초과 발생

n,e= map(int,input().split())
A=[[]for _ in range(n+1)]
visited=[False]*(n+1)
result=[0]*(n+1)


for i in range(e):
    k, s = map(int,input().split())
    A[s].append(k) #단방향

mmax=0
def DFS(v):
    global mmax
    visited[v]=True
    mmax+=1
    for i in A[v]:
        if(not visited[i]):
            DFS(i)
    visited[v]=False
    return

for i in range(1,n+1):
    DFS(i)
    result[i]=mmax
    mmax=0


for i in range(1,n+1):
    if(max(result)==result[i]):
        print(i,end=" ")
