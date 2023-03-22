#이분 그래프 판별하기
#인접 노드들을 다른색으로 색칠 -> 인접노드들과 모두 다른색 -> 이분 그래프

import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
correct=True


def DFS(v):
    global correct
    visited[v]=True
    for i in A[v]:
        if(not visited[i]):
            check[i]=(check[v]+1)%2
            DFS(i)
        elif(check[i]==check[v]):
            correct=False



N=int(input())
for _ in range(N):
    n,e= map(int,input().split())
    check=[0]*(n+1) #0,1 반복
    A=[[]for _ in range(n+1)]
    visited=[False]*(n+1)
    correct = True
    for i in range(e):
        x,y=map(int,input().split())
        A[x].append(y)
        A[y].append(x)
    for i in range(1,n+1):
        if(correct):
            DFS(i)
        else:
            break
    if (correct):
        print("YES")
    else:
        print("NO")


