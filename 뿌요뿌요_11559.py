from collections import deque

color_list = ['R', 'G', 'B', 'P', 'Y']
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

puyo_list = [['.' for _ in range(6)] for _ in range(12)]

for i in range(12):
    input_list = input()
    for j in range(6):
        puyo_list[i][j] = input_list[j]


def bfs(start_i, start_j, color):
    q = deque()
    q.append((start_i, start_j))
    visited = [[False for _ in range(6)] for _ in range(12)]
    visited[start_i][start_j]=True
    same_list = [(start_i, start_j)]
    while q:
        pop_x, pop_y = q.popleft()
        for bf in range(4):
            if 0 <= pop_x + dx[bf] < 12 and 0 <= pop_y + dy[bf] < 6:
                if puyo_list[pop_x + dx[bf]][pop_y + dy[bf]] == color and \
                        not visited[pop_x + dx[bf]][pop_y + dy[bf]]:
                    visited[pop_x + dx[bf]][pop_y + dy[bf]]=True
                    q.append((pop_x + dx[bf], pop_y + dy[bf]))
                    same_list.append((pop_x + dx[bf], pop_y + dy[bf]))
    return same_list


pung = True
answer = 0
while pung:
    pung = False
    # 연쇄 구간
    for i in range(12):
        for j in range(6):
            if puyo_list[i][j] in color_list:
                same = bfs(i, j, puyo_list[i][j])
                if len(same) >= 4:
                    pung = True
                    while same:
                        same_i, same_j = same.pop()
                        puyo_list[same_i][same_j] = '.'
    if pung:
        answer += 1

    # 아래로 내리기
    for i in range(1, 12):
        for j in range(6):
            # 해당 줄 아래로 내리기
            if puyo_list[i][j] == "." and puyo_list[i - 1][j] in color_list:
                dot_cnt = 1
                color_cnt = 1
                d = i + 1
                while True:
                    if d >= 12:
                        break
                    if puyo_list[d][j] == ".":
                        dot_cnt += 1
                        d += 1
                    else:
                        break
                d = i - 2
                while True:
                    if d < 0:
                        break
                    if puyo_list[d][j] in color_list:
                        color_cnt += 1
                        d -= 1
                    else:
                        break
                for xp in range(color_cnt):
                    temp = puyo_list[i - 1-xp][j]
                    puyo_list[i - 1 - xp][j] = '.'
                    puyo_list[i - 1 + dot_cnt - xp][j] = temp
print(answer)
