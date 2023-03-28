# K번째 최단경로 찾기
# 노드 , 엣지, 몇번째, 1번이 시작도시
# sort를 안에 넣으면 안된다고 생각해서 배제하고 했음 (시간 복잡도 때문에)

import sys
from queue import PriorityQueue

n, m, k = map(int, input().split())
A = [[] for _ in range(n + 1)]
result = [[sys.maxsize] * k for _ in range(n + 1)]
mq = PriorityQueue()

for i in range(m):
    a, b, c = map(int, input().split())
    A[a].append((b, c))

mq.put((0, 1))
result[1][0] = 0
# weight /node
# 앞에서부터 채우는 것이 아니라 인덱스 k 값보다 큰 값들은 다 버리기 (뒤부터 채우기)
while mq.qsize() > 0:
    now = mq.get()
    for next in A[now[1]]:
        if result[next[0]][k - 1] > next[1] + now[0]:
            result[next[0]][k - 1] = next[1] + now[0]
            result[next[0]].sort()
            mq.put((next[1] + now[0], next[0]))
            # next[1]+now[0] 이걸로 계산한 루트이므로, 이를 입력 해야함

for i in range(1, n + 1):
    if result[i][k - 1] == sys.maxsize:
        print(-1)
    else:
        print(result[i][k - 1])
