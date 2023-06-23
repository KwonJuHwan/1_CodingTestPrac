from collections import deque



n = int(input())
k = int(input())

dummy_list = [[0 for _ in range(n)] for _ in range(n)]

lotate_dict = {}
# 왼쪽 ->
# 오른쪽 <-
mov = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for _ in range(k):
    inpt_1, inpt_2 = map(int, input().split())
    dummy_list[inpt_1 - 1][inpt_2 - 1] = 1

L = int(input())
for _ in range(L):
    inpt_1, inpt_2 = map(str, input().split())
    lotate_dict[int(inpt_1)] = inpt_2

snake = deque()
snake.append((0, 0))
time = 0
index = 0
while True:
    # 사과 있을떄 없을때, 맞춰서 뱀의 이동
    head_x, head_y = snake.popleft()
    x, y = mov[index]
    # 머리가 벽이나 몸에 박았나?
    if 0 > head_x + x or head_x + x >= n or 0 > head_y + y or head_y + y >= n or (head_x + x, head_y + y) in snake:
        print(time+1)
        break
    snake.appendleft((head_x, head_y))
    snake.appendleft((head_x + x, head_y + y))
    if dummy_list[head_x + x][head_y + y] == 1:
        dummy_list[head_x + x][head_y + y] = 0
    elif dummy_list[head_x + x][head_y + y] == 0:
        snake.pop()
    time += 1
    if time in lotate_dict:
        if lotate_dict[time] == 'L':
            if index == 3:
                index = 0
            else:
                index += 1
        elif lotate_dict[time] == 'D':
            if index == 0:
                index = 3
            else:
                index -= 1
