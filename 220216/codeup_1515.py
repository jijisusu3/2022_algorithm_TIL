# code up (1515): 생명 게임 1

now_arr = [[0] * 27 for i in range(27)]
next_arr = [[0] * 27 for i in range(27)]

for i in range(1, 26):
    input_list = list(map(int, input().split()))
    for j in range(0, 25):
        now_arr[i][j + 1] = input_list[j]


def find(x, y):
    cnt = 0
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        if now_arr[x + dr[i]][y + dc[i]] == 1:
            cnt += 1
    return cnt


for r in range(1, 26):
    for c in range(1, 26):
        if now_arr[r][c] == 0 and find(r, c) == 3:
            next_arr[r][c] = 1
        if now_arr[r][c] == 1 and (find(r, c) >= 4 or find(r, c) <= 1):
            next_arr[r][c] = 0
        if now_arr[r][c] == 1 and (find(r, c) == 2 or find(r, c) == 3):
            next_arr[r][c] = 1

for i in range(1, 26):
    for j in range(1, 26):
        print(next_arr[i][j], end=' ')
    print()


