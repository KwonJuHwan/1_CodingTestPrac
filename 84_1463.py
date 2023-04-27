# 정수를 1로 만들기
# 횟수의 최솟값
# 3 or 2으로 나누는 것이 이득
import sys
input = sys.stdin.readline

x = int(input())
D = [0] * (x + 1)

D[1] = 0


for i in range(2, x + 1):
    # 먼저 무조건 계산한 다음, min 을 통해 비교
    D[i] = D[i - 1] + 1
    # 어차피 min 함수로 비교 하기 때문에, 순서 상관 X
    if i % 3 == 0:
        D[i] = min(D[i], D[i // 3] + 1)
    if i % 2 == 0:
        D[i] = min(D[i], D[i // 2] + 1)

print(D[x])
