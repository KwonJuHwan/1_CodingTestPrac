#임계경로 구하기
#1분도 쉬지 않고, 달린다 -> 최소거리를 제외한 모든 엣지들
#엣지에 weight가 존재-> 저장할때, (도착노드, weight)를 저장하기
#리버스 계산시 visit을 사용해야하는 이유는?
# 엣지는 한 노드안에 여러개의 노드가 꼽혀있을 수 있다. 그렇기 때문에, queue에서 노드를 pop한 상황일때, 모든 엣지에 대해 최대거리인 엣지들을
# 탐색해야 하므로, visit 여부에 관계없이 항상 실행되어야 한다. 하지만 node를 꺼내었을때, visit연산을 집어넣지 않는다면
# 엣지탐색을 진행하였을때, queue에 이전에 넣었던 노드가 다시 들어가, 탐색했던 노드에 꼽혀있는 엣지들을 다시 탐색하여 resultCount를 중복하여
# 셀 수 있는 오류가 발생한다. 따라서 node는 queue에 한번씩만 들어가야 하므로, visit연산을 넣어야한다.
# 리버스가 아닌 첫번째 위상정렬은 진입차수가 0일때만, queue에 노드를 넣으므로, 중복탐색이 불가능하다.
# 리버스를 이용하는 이유?
# 리버스를 사용하는 이유는 리버스를 사용을 해야, 탐색중인 거리의 최댓값과 비교를 할 수 있기때문
# 만약 리버스를 사용하지않고, 그래프 탐색을 진행한다면, 이전 엣지 weight+ 이전 노드의 누적 weight와 현재의 노드 weight를 비교해야하기 때문에
# queue를 이용하는 차원에서 할 수 없는 알고리즘이다. 이미 노드의 weight들과 엣지의 weight를 아는 상황이므로,
# 다음 엣지 weight+ 다음 노드 weight= 현재 노드 weight 계산을 진행하는 것이 옮음
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
m=int(input())
A=[[]for _ in range(n+1)]
reverseA=[[]for _ in range(n+1)]
indegree=[0]*(n+1) #진입차수 리스트

for i in range(m):
    s, e, v=map(int,input().split())
    A[s].append((e,v))
    reverseA[e].append((s,v))
    indegree[e]+=1

startDosi, endDosi = map(int,input().split())

queue=deque()
queue.append(startDosi)
result=[0]*(n+1)

while queue: #진입차수를 이용한 위상정렬
    now= queue.popleft()
    for next in A[now]:
        indegree[next[0]]-=1
        result[next[0]] = max(result[next[0]], result[now]+next[1]) #54번과 같은 노드 weight 갱신
        if indegree[next[0]]==0: #더 이상 자신을 가리키는 노드가 없으므로,나부터 시작하기 위해, append
            queue.append(next[0])

resultCount=0
visited=[False]*(n+1)
queue.clear()
queue.append(endDosi)
visited[endDosi]=True

while queue: #위상정렬 reverse 수행
    now= queue.popleft()
    for next in reverseA[now]:
        #1분도 쉬지 않는 도로 체크
        if result[next[0]] + next[1] == result[now]: #여유가 없음/ 크리티컬 라인 / 거리를 이동할때의 최대거리임
            resultCount+=1
            if not visited[next[0]]:
                visited[next[0]] = True
                queue.append(next[0])

print(result[endDosi])
print(resultCount)