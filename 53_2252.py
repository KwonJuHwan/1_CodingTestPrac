#줄 세우기
import sys
from collections import deque
input=sys.stdin.readline


n,m=map(int,input().split())
A=[[]for _ in range(n+1)]
Topol=[0]*(n+1)
answer=[]


for i in range(m):
    s,e= map(int,input().split())
    A[s].append(e)
    Topol[e]+=1
#처음부터 0인거와, 위상정렬로 인해, 0이된 것을 분리해서 visit을 없앰
#정렬의 순서는 관계가 없으므로, queue를 굳이 동적으로 append 할 필요 없음

mq=deque()
for i  in range(1,n+1):
    if(Topol[i]==0):
        mq.append(i)


for i  in range(1,n+1):
    while(mq):
        now = mq.popleft()
        answer.append(now)
        for j in A[now]:
            Topol[j]-=1
            if(Topol[j]==0):
                mq.append(j)

for i in range(len(answer)):
    print(answer[i],end=' ')


