# 구간 곱 구하기
# 수의 변경이 번번히 일어나고, 중간에 구간의 곱을 구함 -> 세그먼트 트리
# 곱셈의 성질 = (A*B)%C = A%C * B%C
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
# a=1 b -> c
# a=2 b~c 곱한 수 출력
lengh = n
lenghCount = 0
mod = 1000000007

while lengh > 1:
    lenghCount += 1
    lengh /= 2

treeSize = pow(2, lenghCount + 1)
start_index = treeSize // 2 - 1
tree = [1] * (treeSize + 1)

# 트리 값 입력
for i in range(start_index + 1, start_index + 1 + n):
    tree[i] = int(input())

# 트리 완성 시키기
for i in range(start_index, 0, -1):
    tree[i] = tree[2 * i] % mod * tree[2 * i + 1] % mod


def solve(b, c):
    start = start_index + b
    end = start_index + c
    result = 1
    while end >= start:
        if start % 2 == 1:
            result *= tree[start] % mod
        if end % 2 == 0:
            result *= tree[end] % mod
        start = (start + 1) // 2
        end = (end - 1) // 2
    return result % mod


def update(x, value):
    index = start_index + x
    tree[index] = value
    while index > 1:
        index //= 2
        tree[index] = tree[index * 2] % mod * tree[index * 2 + 1] % mod


for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    elif a == 2:
        print(solve(b, c))
