# 이진 트리
# 자식 노드의 개수가 2개가 아닌 2개이하인 트리
# 전위 순회: 루트 왼쪽 오른쪽
# 중위 순회: 왼쪽 루트 오른쪽
# 후위 순회: 왼쪽 오른쪽 루트
# while, for문으로 풀어서 못쓰겠는데..? -> 재귀함수!
n = int(input())
treeList = {}
# 입력: 루트 왼쪽 오른쪽


for i in range(1, n + 1):
    root, le, ri = input().split()
    treeList[root] = [le, ri]


def preOrder(now):
    if now == '.':
        return
    print(now, end="")
    preOrder(treeList[now][0])
    preOrder(treeList[now][1])


def inOrder(now):
    if now == '.':
        return
    inOrder(treeList[now][0])
    print(now, end="")
    inOrder(treeList[now][1])


def postOrder(now):
    if now == '.':
        return
    postOrder(treeList[now][0])
    postOrder(treeList[now][1])
    print(now, end="")


preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
