def dfs(n, ci, cj, num):
    if n == 7:
        sset.add(num)
        return
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(n + 1, ni, nj, num*10 + arr[ni][nj])

TC = int(input())
for tc in range(1, TC+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    sset = set()
    for i in range(4):
        for j in range(4):
            dfs(0, i, j, 0)
    print(f'#{tc} {len(set)}')