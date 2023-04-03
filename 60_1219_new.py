#음수 사이클 -> 양수 사이클(계속해서 이익이 되는 사이클)
#최단거리 구하기 -> 돈의 액수를 최대로
#파훼법 -> 에지의 업데이트를 충분히 큰수로 업데이트
# hy? 에지를 충분히 탐색하면서 양수 사이클에서 도달할 수 있는
#모든 노드를 양수 사이클에 연결된 노드로 업데이트하기 위함
#무슨말이냐? 시작 도시가 만약 양수사이클과 연결된 도시라면-> 도착도시도 양수사이클과 연관됨
#충분히 탐색해야 양수사이클과 관련되있음을 앎
#나는 w가 한번 이동할때 버는 값 cityMoney가 max값인줄 알았음
#그게 아니라 w는 -되는 값, cityMoney는 +값이었음.
import sys
input=sys.stdin.readline

n, startDosi, endDosi, m = map(int,input().split())
distance=[-sys.maxsize]*(n)
edge=[]

for _ in range(m):
    s, e, w= map(int,input().split())
    edge.append((s,e,w))

cityMoney= list(map(int,input().split()))

distance[startDosi]=cityMoney[startDosi]

for i in range(n+101):
    for s,e,w in edge:
        if(distance[s] == -sys.maxsize): #출발노드가 아직 방문하지 못했음 -> 스킵
            continue
        elif distance[s] == sys.maxsize: # 시작도시가 양수 사이클-> 도착도시도 양수사이클/ 시작노드에 사이클이 있는경우
            distance[e]=sys.maxsize
        elif distance[e] < distance[s]-w+cityMoney[e]:
            distance[e] = distance[s] - w + cityMoney[e] #양수사이클이라면, 계속해서 값이 올라감
            if i >= n-1: #모든 방문이 끝났어도, 계속해서 distance가 업데이트되고있음->양수사이클에 빠짐
                        # 이 경우의 수는 시작도시는 max에 도달하지않았음에도, 도착도시가 계속 업데이트 중인 상황 /도착노드에 사이클이 있는경우
                distance[e] = sys.maxsize

if(distance[endDosi] == -sys.maxsize):
    print("gg")
elif distance[endDosi] == sys.maxsize:
    print("Gee")
else:
    print(distance[endDosi])
