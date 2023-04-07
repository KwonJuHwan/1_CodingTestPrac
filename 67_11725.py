# 트리의 부모 찾기
# 루트 노드 = 1

n = int(input())
A = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
number = [0] * (n + 1)  # 각 노드의 부모 노드의 값을 넣기

for _ in range(n - 1):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)


# 루트 노드부터 DFS를 실행하면, 계속 부모의 노드를 업데이트 하면서 진행할 수 있음

def DFS(v):
    visit[v] = True
    for now in A[v]:
        if not visit[now]:  # 이 조건문을 하지 않는다면, 위로 역행할 수 있음
            number[now] = v  # 해당 노드의 부모노드 인덱스를 넣기
            DFS(now)


DFS(1)

for i in range(2, n + 1):
    print(number[i])
