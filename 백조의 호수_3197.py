from collections import deque

n, m = map(int, input().split())

ice_list = [['.' for _ in range(m)] for _ in range(n)]

L_i, L_j = 0, 0
for i in range(n):
    input_list = input()
    for j in range(m):
        ice_list[i][j] = input_list[j]
        if input_list[j] == 'L':
            L_i, L_j = i, j
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

ice_list[L_i][L_j] = '.'
def bfs(start_i, start_j):
    q = deque()
    q.append((start_i, start_j))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start_i][start_j] = True
    meet = False
    while q:
        now_i, now_j = q.popleft()
        for k in range(4):
            if 0 <= now_i + di[k] < n and 0 <= now_j + dj[k] < m:
                if ice_list[now_i + di[k]][now_j + dj[k]] != 'X' and not visited[now_i + di[k]][now_j + dj[k]]:
                    q.append((now_i + di[k], now_j + dj[k]))
                    visited[now_i + di[k]][now_j + dj[k]] = True
                if ice_list[now_i + di[k]][now_j + dj[k]] == 'L':
                    meet = True
                    break
    return meet


answer = 0
while True:
    # 갈 수 있음?
    if bfs(L_i, L_j):
        print(answer)
        break
    # 얼음 깨기
    ice_break = []
    for i in range(n):
        for j in range(m):
            if ice_list[i][j] == 'X':
                for k in range(4):
                    if 0 <= i + di[k] < n and 0 <= j + dj[k] < m:
                        if ice_list[i + di[k]][j + dj[k]] == '.':
                            ice_break.append((i, j))
    while ice_break:
        break_i, break_j = ice_break.pop()
        ice_list[break_i][break_j] = '.'
    answer += 1
