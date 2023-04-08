# 집합 Set을 이용해서 단순히 집합 안에 있으면 +1 해주기

# 문자열 찾기

n, m = map(int, input().split())
tree = set([input() for _ in range(n)])
count = 0

for _ in range(m):
    subtext = input()
    if subtext in tree:
        count += 1

print(count)
