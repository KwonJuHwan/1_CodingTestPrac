# 구간 합 구하기 3
# 단순히 arrayList로 구현 -> for문 중첩으로 사용하기 때문에, 시간 복잡도가 커진다. => 시간초과 뜸
# 값이 계속 바뀜 -> tree 이용
# 그렇기 때문에, 세그먼트 트리를 사용해서 구현해야함.

import sys
input=sys.stdin.readline

n, m, o = map(int, input().split())

k = 0
length = n
while length > 1:
    length = length / 2
    k += 1

treeSize = pow(2, k + 1)
start_index = treeSize // 2 - 1

tree = [0] * (treeSize+1)

for i in range(start_index + 1, start_index + n + 1):
    tree[i] = int(input())


# 구간 합 트리 만들기
def makeTree():
    for i in range(start_index, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]


def solveSum(s, e):
    sum = 0
    start = s + start_index
    end = e + start_index
    while end >= start:
        # start 인덱스는 오른쪽 리프 노드를 더해야됨
        # 나머지 1이 존재 -> 오른쪽 리프노드가 없다 -> 더하기
        if start % 2 == 1:
            sum += tree[start]
        # end는 왼쪽 리프 노드를 더해야됨
        # 2로 나누어 떨어진다 -> 왼쪽 리프 노드가 없음 -> 상위 노드 안가도 됨 -> 더하기
        if end % 2 == 0:
            sum += tree[end]
        # 상위 노드로 가기 ( tree height -1 하는 행위가 같음)
        # +1, -1 를 붙여줘야
        # 더하지 않았던 노드 -> 부모 노드로 가서 더해주기
        # 더한 노드 -> 부모 노드로 가지 않고, 다음 노드 탐색
        start = (start + 1) // 2
        end = (end - 1) // 2
    return sum


# 업데이트 함수 따로 만들어야 됨 -> 시간 복잡도를 줄여야 함
def update(sp, p):
    count = start_index + sp
    tree[count] = p
    while count >= 1:
        count = count // 2
        tree[count] = tree[count * 2] + tree[count * 2 + 1]

makeTree()

# a= 1 -> b번째 수를 c로 바꾸기
# a= 2 -> b~c 합 출력
for _ in range(m + o):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b,c)
    elif a == 2:
        solve_sum = solveSum(b, c)
        print(solve_sum)
