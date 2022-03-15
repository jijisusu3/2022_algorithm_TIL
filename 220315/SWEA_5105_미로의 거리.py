import sys
sys.stdin = open('5105.txt')
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(sr, sc):
    global er
    global ec
    q = deque()
    q.append((sr, sc))
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0 and maze[nr][nc] == 0:
                    q.append((nr, nc))
                    distance[nr][nc] = distance[x][y] + 1
                elif visited[nr][nc] == 0 and maze[nr][nc] == 3:
                    distance[nr][nc] = distance[x][y]
    return distance[er][ec]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c
            elif maze[r][c] == 3:
                er, ec = r, c
    result = bfs(sr, sc)
    print(f'#{tc} {result}')
