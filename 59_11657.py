#타임머신으로 빨리 가기
#weight가 음수가 가능 -> 다이제스트라 사용하지 못함
#시간복잡도가 크다
#모든 엣지를 노드의 수만큼 탐색
#출발노드 초기화/ 초기화를 0으로 해줘야 출발노드로부터의 최단거리가 성립 ( 0을 기준으로 계산하므로)
import sys
input=sys.stdin.readline


n, m=map(int,input().split())
A=[]
d=[sys.maxsize]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    A.append((a,b,c))

d[1]=0

for _ in range(n-1): #출발노드 제외
    for s, e, w in A:
        if d[s] != sys.maxsize and d[e]> d[s]+w:
            d[e]=d[s]+w

cyc=False
#한번만 돌려봐도, 바뀌는지 안바뀌는지 앎
for s, e, w in A:
    if d[s] != sys.maxsize and d[e] > d[s] + w:
        d[e] = d[s] + w
        cyc=True

if(cyc):
    print(-1)
else:
    for i in range(2,n+1):
        if(d[i] != sys.maxsize):
            print(d[i])
        else:
            print(-1)




