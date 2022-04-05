import sys
sys.stdin = open('11901.txt')
from heapq import heappush, heappop

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra(row, col):
    Q = [(row, col, 0)]
    D[row][col] = 0

    while Q:
        now_r, now_c, now_val = heappop(Q)
        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                height = 0
                if arr[nr][nc] > arr[now_r][now_c]:
                    height = arr[nr][nc] - arr[now_r][now_c]

                w = height + 1
                if D[nr][nc] > now_val + w:
                    D[nr][nc] = now_val + w
                    heappush(Q, (nr, nc, D[nr][nc]))
    return D[N-1][N-1]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[0xfffff] * N for _ in range(N)]
    result = dijkstra(0, 0)
    print(f'#{tc} {result}')