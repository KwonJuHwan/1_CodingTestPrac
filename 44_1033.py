#칵테일 만들기
#비율 -> 최대공배수, 최대공약수를 통해, 처음에 곱해주고, 마지막에 나눠주기

N=int(input())
A=[[]for _ in range(N)]
visited=[False]*(N)
D= [0]*N #최소 공배수 넣기
mmax=1

def gcd(s,e):
    if(e==0):
        return s
    else:
        return gcd(e,s%e)

def DFS(v):
    visited[v]=True
    for i in A[v]:
        if(not visited[i[0]]):
            D[i[0]]= D[v]*i[2]//i[1]
            DFS(i[0])

for i in range(N-1):
    a, b, p, q=map(int,input().split())
    A[a].append((b,p,q))
    A[b].append((a,q,p))
    mmax*=(p*q//gcd(p,q))

D[0]=mmax
DFS(0)
mgcd=D[0]

for i in range(1,N):
    mgcd=gcd(mgcd,D[i])

for i in range(N):
    print(int(D[i]//mgcd),end=" ")