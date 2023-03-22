import sys
input=sys.stdin.readline
from collections import deque

n,e= map(int,input().split())
A=[[]for _ in range(n+1)]
visited=[False]*(n+1)
result=[0]*(n+1)

def BFS(v):
    mq=deque()
    visited[v]=True
    mq.append(v)
    while(mq):
        now=mq.popleft()
        for i in A[now]:
            if(not visited[i]):
                visited[i]=True
                result[i]+=1 #한표 투척
                mq.append(i)


for _ in range(e):
    x,y=map(int,input().split())
    A[x].append(y)


for i in range(1,n+1):
    BFS(i)
    visited = [False] * (n + 1)

maxVal=0

for i in range(1,n+1):
    maxVal=max(maxVal,result[i])


for i in range(1,n+1):
    if( maxVal== result[i]):
        print(i,end=" ")

