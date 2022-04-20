arr = [list(input()) for _ in range(5)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(temp_lst, cnt, y_cnt):
    global count, result
    if y_cnt > 3:
        return
    if cnt == 7:
        # temp_lst.sort()
        print(temp_lst)
        # x = ''
        # for i in temp_lst:
        #     x += str(i)
        # result.add(x)
        return

    for j in range(len(temp_lst)):
        for i in range(4):
            nr = temp_lst[j][0] + dr[i]
            nc = temp_lst[j][1] + dc[i]
            if 0 <= nr < 5 and 0 <= nc < 5 and (nr, nc) not in temp_lst:
                temp_lst.append((nr, nc))  # 넣고~
                if arr[nr][nc] == 'S':  # 이다솜파일 때
                    dfs(temp_lst, cnt + 1, y_cnt)
                else:  # 임도연파일 때
                    dfs(temp_lst, cnt + 1, y_cnt + 1)
                temp_lst.pop()  # 빼고~


count = 0
result = set()
for r in range(5):
    for c in range(5):
        if arr[r][c] == 'S':
            temp = [(r, c)]
            dfs(temp, 1, 0)

print(result)