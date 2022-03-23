from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


dr = [0, -1, 1, 1] # 서, 북서, 남서, 남
dc = [-1, -1, -1, 0]


def bfs(row, col, direction):
    global num
    Q = deque()
    Q.append((row, col))
    while Q:
        nr, nc = Q.popleft()
        if arr[nr][nc] == (num - 1):
            arr[nr][nc] = num
            row = nr
            col = nc
        elif arr[nr][nc] != (num -1):
            for _ in range(1, 4):
                new_d = (direction + 1) % 4
                nr = row + dr[new_d]
                nc = col + dc[new_d]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] == (num - 1):
                        arr[nr][nc] = num
                        row = nr
                        col = nc
                        break


num = 2
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            bfs(r, c)