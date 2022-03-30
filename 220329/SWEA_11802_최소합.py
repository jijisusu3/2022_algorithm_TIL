import sys
sys.stdin = open('11802.txt')

dr = [0, 1]
dc = [1, 0] # 오른쪽, 아래


def dfs(row, col, val):
    global result
    if val > result:
        return
    if row + 1 == N and col + 1 == N:
        if result > val:
            result = val
        return
    for i in range(2):
        nr, nc = row + dr[i], col + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            dfs(nr, nc, val + arr[nr][nc])


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10 * (N ** 2)
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {result}')