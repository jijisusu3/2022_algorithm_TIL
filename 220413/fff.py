from collections import deque
import sys

d = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
H, W = map(int, input().split())  # 가로세로
arr = [list(sys.stdin.readline().rstrip()) for i in range(H)]
Q = deque()  # 아직 숫자(모래성)인 애들 넣어주는 곳
temp = deque()  # 다음회차에 '.'으로 바뀔 애들 넣어주는 곳

flag = True
for r in range(H):
    for c in range(W):
        if arr[r][c] == '.':
            temp.append((r, c))
            flag = False
            break
    if flag == False:
        break

result = 0

while temp:
    result += 1
    while temp:
        r, c = temp.popleft()
        arr[r][c] = '.'

    for r in range(H):
        for c in range(W):
            if arr[r][c] != '.':
                Q.append((r, c))

    while Q:
        row, col = Q.popleft()
        cnt = 0
        for i in range(8):
            nr, nc = row + d[i][0], col + d[i][1]
            if 0 <= nr < H and 0 <= nc < W:
                if arr[nr][nc] == '.':
                    cnt += 1
            if cnt >= int(arr[row][col]):
                temp.append((row, col))

print(result)