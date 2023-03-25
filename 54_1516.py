#그래프간의 순서가 존재 -> 위상 정렬
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
inp=[[]for _ in range(n)] #입력
Topol=[0]*(n) #진입차수 배열
answer=[0]*(n) #답
weight=[0]*(n)
A=[[]for _ in range(n)] #그래프

for i in range(n):
    inp[i]=list(map(int,input().split())) #입력받기
    weight[i]=inp[i][0] #그래프 weight 업데이트
    j=1
    while(True):#그래프 A에 입력값 넣기
        Exp=False
        if(inp[i][j]==-1):
            break
        A[(inp[i][j])-1].append(i)
        Topol[i]+=1
        j+=1


mq=deque()
for i in range(n):
    if(Topol[i]==0):
        mq.append(i)

while(mq):
    now= mq.popleft()
    for i in A[now]:
        Topol[i]-=1
        #둘 중에 하나를 선택함으로써, 노드 weight의 중복 덧셈 방지 (길이 여러가지 이므로)
        # answer[4]= 1->4 // answer[3]+weight[3] = 1->3->4 둘중에 높은 값으로 선택
        answer[i] = max(answer[i],answer[now]+weight[now])
        if(Topol[i]==0):
            mq.append(i)


for i in range(n):
    print(answer[i]+weight[i])

