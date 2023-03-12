#미로 탐색하기
#내가 못한부분
# 1. x,dy를 선언하여, 좌표 이동
# 2. 미로 자체에 값을 변환하여, 리스트 A에 +1씩 증가시켜 depth를 남김
# list(input())으로 받으면, str로 받기때문에, int로 변환 해줘야함
from collections import deque

N,M= map(int,input().split())

A=[[0 for _ in range(M)] for _ in range(N)]
visit=[[False for _ in range(M)] for _ in range(N)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for i in range(N):
    ipt=list(input())
    for j in range(M):
        A[i][j]=int(ipt[j])

#2차원 리스트에 미로 담기

def DFS(x,y):
    queue=deque()
    queue.append((x,y))
    visit[x][y]=True
    while(queue):
        now= queue.popleft()
        for k in range(4):
            i=now[0]+dx[k]
            j=now[1]+dy[k]
            if(i>=0 and j>=0 and i<N and j<M):
               if(not visit[i][j] and A[i][j]!=0):
                    visit[i][j]=True
                    A[i][j]=A[now[0]][now[1]]+1
                    queue.append((i,j))

DFS(0,0)

print(A[N-1][M-1])