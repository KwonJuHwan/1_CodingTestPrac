# 물의 양 구하기
# A: 0 B:0 C:C 로 시작
# A:0 일때, C가 가능한 값을 모두 보여줘
#a,b,c 를 0,1,2로 생각하고 진행하는 판단
#무게 총량이 정해져있으니 a,b 무게로만 진행하는 아이디어
# 물을 주는 행위를 6개로 정리하고 for문으로 만들기
# 물을 주는 행위는 다 따르거나 or 다 따르고 남는 물 -> if문으로 해결
from collections import deque
#a,b/a,c/b,a/b,c/c,a/c,b
Sender=  [0,0,1,1,2,2]
Receiver=[1,2,0,2,0,1]
now=list(map(int,input().split()))
#같은양의 물을 가지고 있으면 탐색할 필요 없으니, 탐색하지 않도록 visit 만들기 또한, 두개의 값만 알아도 나머지 한개는 고정이므로 , 두개의 값만을
#이용해서 무게 나타내기 여기서는 a와 b의 무게로 판단
visited=[[False for _ in range(201)] for _ in range(201)]
answer=[False]*(201) #인덱스 값= 답

# a,b 기준으로 진행
def BFS():
    queue= deque()
    queue.append((0,0))
    visited[0][0]=True
    answer[now[2]]=True
    while queue:
        nowNode=queue.popleft()
        A=nowNode[0]
        B=nowNode[1]
        C=now[2]-A-B
        for k in range(6): #선계산 (서순차이 없음)
            next=[A,B,C]
            next[Receiver[k]]+=next[Sender[k]]
            next[Sender[k]]=0
            if(next[Receiver[k]] > now[Receiver[k]]): #용량제한
                next[Sender[k]]=next[Receiver[k]] - now[Receiver[k]]
                next[Receiver[k]]=now[Receiver[k]]
            if(not visited[next[0]][next[1]]):
                visited[next[0]][next[1]]=True
                queue.append((next[0],next[1],))
                if(next[0]==0):
                    answer[next[2]]=True

BFS()

for i in range(201):
    if answer[i]:
        print(i,end=" ")


