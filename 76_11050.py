# 조합
# 모든 부분 문제가 해결 했다고 가정
# 점화식과 같은 문제 접근
# 현재 문제를 부분 문제로 나누어서 생각
# D[i][j]= D[i-1][j] + D[i-1][j-1]
# 이항 계수 구하기 1

# 초기화를 어떻게 할 것인가, for 문의 처음과 시작을 무슨 값으로 할 것인가

import sys
input=sys.stdin.readline

n, k= map(int,input().split())

D=[[0 for _ in range(11)] for _ in range(11)]


for i in range(0,11):
    D[i][1] = i
    D[i][i] = 1
    D[i][0] = 1

# i= 1, j= 0 은 신경 써줄 필요 없음
for i in range(2,11):
    for j in range(1,11):
        D[i][j] = D[i-1][j-1] + D[i-1][j]


print(D[n][k])


