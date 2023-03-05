# 숫자 합 구하기 이해 필요 2차원 숫자 합

import sys
input= sys.stdin.readline
n, m = map(int,input().split())
num_list= [[0]*(n+1)]
sum_list= [[0]*(n+1)for _ in range(n+1)]

for i in range(n):
    num_list_row=[0]+[int(x) for x in input().split()]
    num_list.append(num_list_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_list[i][j]= sum_list[i][j-1] + sum_list[i-1][j] - sum_list[i-1][j-1] + num_list[i][j]

for _ in range(m):
    x1, x2 , y1 ,y2 = map(int, input().split())
    result= sum_list[x2][y2] - sum_list[x2][y1-1] - sum_list[x1-1][y2] + sum_list[x1-1][y1-1]

# 다른방법
# arr = [for _ in range(num)]
#
# for i in range(num):
# 	arr[i] = list(map(int, input().split()))

# arr = [list(map(int, input().split())) for _ in range(num)]
