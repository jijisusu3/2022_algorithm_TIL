#SWEA(1209): SUM

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_x = 0
    for x in range(100):
        s1 = s2 = s3 = s4 = 0
        for i in range(100):
            s1 += arr[x][i]
        if s1 > max_x:
            max_x = s1
        for j in range(100):
            s2 += arr[j][x]
        if s2 > max_x:
            max_x = s2
        s3 += arr[x][x]
        s4 += arr[x][99-x]
    if s3 > max_x:
        max_x = s3
    if s4 > max_x:
        max_x = s2
    print(f'#{tc} {max_x}')



# SWEA(1954): 달팽이 숫자


dr = [0, 1, 0, -1]  # 우 하 좌 상
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    house = [[0] * num for _ in range(num)]
    r = c = 0
    d = 0  # direction
    for snail in range(1, num ** 2 + 1):
        house[r][c] = snail
        r += dr[d]
        c += dc[d]
        if r >= num or c >= num or house[r][c] != 0:
            r -= dr[d]
            c -= dc[d]
            d = (d + 1) % 4
            r += dr[d]
            c += dc[d]
    print(f"#{tc}")
    for i in house:
        print(*i)
