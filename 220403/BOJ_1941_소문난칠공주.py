arr = [list(input()) for _ in range(5)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(temp_lst, num, cnt, y_cnt):
    global count
    if y_cnt > 3:
        return
    if cnt == 7:
        print(temp_lst)
        # 이미 세 두었던 무리인지 확인 후 return
        return
    row = num // 10
    col = num % 10
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < 5 and 0 <= nr < 5:
            temp_lst.append(nr * 10 + nc)  # 넣고~
            if arr[nr][nc] == 'S':  # 이다솜파일 때
                dfs(temp_lst, nr * 10 + nc, cnt + 1, y_cnt)
            else:  # 임도연파일 때
                dfs(temp_lst, nr * 10 + nc, cnt + 1, y_cnt + 1)
            temp_lst.pop()  # 빼고~



count = 0
for r in range(5):
    for c in range(5):
        if arr[r][c] == 'S':
            temp = [r * 10 + c]
            dfs(temp, r * 10 + c, 1, 0)
