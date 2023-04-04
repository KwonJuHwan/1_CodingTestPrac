# 최소 신장 트리
# 조건: 사이클 X , n개의 노드 -> 최소 신장 트리를 구성 하는 에지의 개수는 항상 n-1
# 엣지 중심 -> 엣지 리스트로 저장 + 유니온 파인드
# 가중치 정렬 후, 낮은 것 부터 연결 시도 ->
# 파인드로 확인 후(대표 노드가 같으면 사이클 발생) , 사이클이 아닐 때에만 union 연산
# 최소 확정(정렬로 인해) , 노드의 사이클이 없는 것도 확정(find 값이 다름) -> 무조건 최소 신장 트리의 노드

import sys

input = sys.stdin.readline

v, e = map(int, input().split())
edge = []
f_list = [0] * (v + 1)

for i in range(v + 1):
    f_list[i] = i

for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort()


def find(k):
    if k == f_list[k]:
        return k
    else:
        # 유니온 파인드의 핵심은 find에서 재귀함수로 업데이트 시켜주기
        f_list[k] = find(f_list[k])
        return f_list[k]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        f_list[b] = a


count = 0
weight = 0
while count < v - 1:
    for w, s, e in edge:
        if find(s) != find(e):
            union(s, e)
            weight += w
            count += 1

print(weight)
