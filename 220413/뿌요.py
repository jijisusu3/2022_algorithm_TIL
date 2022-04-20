from collections import deque
arr = [list(input()) for _ in range(12)]
answer = 0
N, M = 12, 6


def bfs():
    global answer
    visit = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '.' and visit[i][j] == 0:
                Q = deque()
                Q.append
