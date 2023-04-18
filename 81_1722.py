# 순열의 순서 구하기
# k= 1 -> k번쨰 순열
# k= 2 -> 임의의 순열이 몇번째 순열인지
# 1234 1243 1324
# 123 132 213 231 312 321
# 나머지와 몫을 이용해서 풀기 -> 이게 맞나?
n = int(input())
fac = [1] * (n + 1)
visited = [False] * (n + 1)
s = [0] * 21

for i in range(2, n + 1):
    fac[i] = i * fac[i - 1]

que = list(map(int, input().split()))
if que[0] == 1:
    k = que[1]
    for i in range(1, n + 1):
        cnt = 1
        for j in range(1, n + 1):
            if visited[j]:
                continue
            if k <= cnt * fac[n - i]:
                k -= (cnt - 1) * fac[n - i]
                s[i] = j
                visited[j] = True
                break
            cnt += 1
    for i in range(1, n + 1):
        print(s[i], end=' ')
else:
    k = 1
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, que[i]):
            if not visited[j]:
                cnt += 1
        k += cnt * fac[n - i]
        visited[que[i]] = True
    print(k)
