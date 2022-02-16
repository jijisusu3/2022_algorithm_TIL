# 달팽이 again...

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = map(int, input().split())
house = [[0]*m for _ in range(n)]
snail = n*m
r = 0
c = 0
d = 0

for snail in range(m*n, 0, -1):
    house[r][c] = snail
    r += dr[d]
    c += dc[d]
    if r >= n or c >= m or house[r][c] != 0:
        r -= dr[d]
        c -= dc[d]
        d = (d+1) % 4
        r += dr[d]
        c += dc[d]

for i in house:
    print(*i)