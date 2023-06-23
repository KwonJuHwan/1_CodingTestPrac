list_num = [[(8, 0), (0, 1), (0, 2), (1, 0), (2, 2), (2, 1), (2, 0), (3, 2), (4, 2), (4, 1), (4, 0), (3, 0), (1, 2)],
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 2), (4, 0), (4, 1), (4, 2)],
            [(9, 0), (0, 1), (0, 2), (1, 0), (2, 2), (2, 1), (2, 0), (3, 2), (4, 2), (4, 1), (4, 0), (1, 2)],
            [(6, 0), (0, 1), (0, 2), (1, 0), (2, 2), (2, 1), (2, 0), (3, 2), (4, 2), (4, 1), (4, 0), (3, 0)],
            [(5, 0), (0, 1), (0, 2), (1, 0), (2, 2), (2, 1), (2, 0), (3, 2), (4, 2), (4, 1), (4, 0)],
            [(3, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (3, 2), (4, 2), (4, 1), (4, 0)],
            [(2, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 0), (2, 1), (3, 0), (4, 0), (4, 1), (4, 2)],
            [(4, 0), (1, 0), (2, 0), (2, 1), (2, 2), (0, 2), (1, 2), (3, 2), (4, 2)],
            [(7, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
            [(1, 0), (1, 0), (2, 0), (3, 0), (4, 0)]]
n = int(input())

input_word = input()
input_list = list(input_word)
len_input = len(input_list) // 5
word_list = [["" for _ in range(len_input)] for _ in range(5)]

k = 0
for i in range(5):
    for j in range(len_input):
        word_list[i][j] = input_list[k]
        k += 1

answer = ""
for i in range(len_input):
    if word_list[0][i] == '#':
        a, b = 0, i
        for j in range(10):
            cnt = 0
            for p in range(1, len(list_num[j])):
                x, y = list_num[j][p]
                if a + x < 5 and b + y < len_input:
                    if word_list[a + x][b + y] == '#':
                        cnt += 1
            if cnt == (len(list_num[j]) - 1):
                answer += str(list_num[j][0][0])
                for q in range(1, len(list_num[j])):
                    x, y = list_num[j][q]
                    word_list[a + x][b + y] = '.'
                break

print(answer)
