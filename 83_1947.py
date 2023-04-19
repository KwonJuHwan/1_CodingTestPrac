# 선물 전달하기

n = int(input())

D = [0] * (n + 1)

D[1] = 0
D[2] = 1

for i in range(3, n + 1):
    D[i] = (i - 1)*(D[i - 2] + D[i - 1]) % 1000000000

print(D[n])
