TC = int(input())


def dfs(n, sr, sc, v, cnt):
    global r, c, ans
    if n > 3:
        return
    if n == 3 and sr == r and sc == c and ans < cnt:
        ans = cnt
        return
    for i in range(n, n + 2):
        nr, nc = sr + dr[i], sc + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] not in v:
            dfs(i, nr, nc, v+arr[nr][nc], cnt + 1)


dr, dc = (1, 1, -1, -1), (-1, 1, 1, -1)

for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for r in range(N):
        for c in range(N):
            dfs()
