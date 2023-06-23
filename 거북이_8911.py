f = [(0, 1), (-1, 0), (0, -1), (1, 0)]
b = [(0, -1), (1, 0), (0, 1), (-1, 0)]

n = int(input())

for i in range(n):
    command = input()
    index = 0
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    now_x = 0
    now_y = 0
    for com in command:
        if com == 'L':
            if index == 3:
                index = 0
            else:
                index += 1
        elif com == 'R':
            if index == 0:
                index = 3
            else:
                index -= 1
        elif com == 'F':
            now_x = now_x + f[index][0]
            now_y = now_y + f[index][1]
        elif com == 'B':
            now_x = now_x + b[index][0]
            now_y = now_y + b[index][1]
        min_x = min(min_x, now_x)
        min_y = min(min_y, now_y)
        max_x = max(max_x, now_x)
        max_y = max(max_y, now_y)
    print((max_x - min_x) * (max_y - min_y))
