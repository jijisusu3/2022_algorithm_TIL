import sys
sys.stdin = open('1861.txt')


def bfs(row, col):
    Q = []
    S = []
    Q.append((row, col))
    v[row][col] = 1
    S.append(arr[row][col])
    while Q:
        now_r, now_c = Q.pop(0)
        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nr, nc = now_r + dr, now_c + dc
            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == 0 and \
                    abs(arr[now_r][now_c]-arr[nr][nc]) == 1:
                Q.append((nr, nc))
                v[nr][nc] = 1
                S.append(arr[nr][nc])
        return min(S), len(S)


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    num = N*N
    cnt = 0
    for r in range(N):
        for c in range(N):
            if v[r][c] == 0 :
                n, c = bfs(r, c)
                if cnt < c or cnt == c and num > tc:
                    cnt = c
                    num = n
    print(cnt, num)

# 교수님 방법
    # pos = [0] * (N * N + 1)
    # arr = []
    # for i in range(N):
    #     arr.append(list(map(int, input().split())))
    #     for j in range(N):
    #         pos[arr[i][j]] = (i, j)
    # D = [0] * (N * N + 1)
    # for i in range(N*N, 0, -1):
    #     r, c = pos[i]
    #     if D[i]:continue
    #     D[i] = 1
    #     for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #         nr, nc = r + dr, c + dc
    #         if 0 < nr <= N and 0 < nc <= N: continue
    #         if arr[nr][nc] + 1 == arr[r][c]:
    #             D[i-1] = D[i] + 1
    # ans = 1
    # for i in range(2, N*N+1):
    #
