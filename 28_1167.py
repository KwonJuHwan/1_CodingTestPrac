#트리의 지름 구하기
from collections import deque

N=int(input())
A=[[]for _ in range(N+1)]
visit=[False]*(N+1)

#입력 값들을 A 인접 리스트에 넣기
for i in range(1,N+1):
    k=list(map(int,input().split()))
    j=1
    while(True):
        if(k[j]== -1):
            break
        A[i].append((k[j],k[j+1]))
        j=j+2

# i[0]= node num
# i[1]= weight
max=0
maxNode=0
#내 방식은 weight를 계속 업데이트 하며, queue에 입력함
#풀이는 distance 리스트를 하나 만들고, 거리 값을 따로 저장
def BFS(v):
    global max, maxNode
    visit[v]=True
    queue=deque()
    queue.append((v,0))
    while(queue):
        k=queue.popleft()
        node=k[0]
        weight=k[1]
        if(weight> max):
            max=weight
            maxNode=node
        for i in A[node]:
            if(not visit[i[0]]):
                visit[i[0]]=True
                queue.append((i[0],weight+i[1]))


BFS(1)
BFS(maxNode)
print(max)




