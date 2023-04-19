# 사전찾기

n, m, k = map(int, input().split())

# k에 대한 이해
# 몇번째 문자열을 표현해야 하는지 : k

D = [[0 for _ in range(202)] for _ in range(202)]

for i in range(0, 201):
    for j in range(0, i + 1):
        if j == 0 or j == i:
            D[i][j] = 1
        else:
            D[i][j] = D[i - 1][j] + D[i - 1][j - 1]
            if D[i][j] > 1000000000:
                D[i][j] = 1000000001


if D[n + m][m] < k:
    print(-1)

else:
    while not (n == 0 and m == 0):
        if D[n - 1 + m][m] >= k:
            print('a', end='')
            n -= 1
        else:
            print('z', end='')
            k -= D[n - 1 + m][m]
            m -= 1
