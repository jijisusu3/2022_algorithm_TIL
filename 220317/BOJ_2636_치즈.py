from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col):
    global cnt
    Q = deque()
    Q.append((row, col))
    while Q:
        a, b = Q.popleft()
        cnt += 1
        if arr[a][b] == 0:
            for i in range(4):
                nr = a + dr[i]
                nc = b + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] == 1:

cnt = 0
num = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            num += 1

