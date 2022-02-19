import sys ; sys.stdin = open('11010.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    for r in range(N):
        for c in range(N):
            i1 = i2 = i3 = i4 = 1
            j1 = j2 = j3 = j4 = 1
            add = arr[r][c]
            while c - i1 >= 0 and r - j1 >= 0: # 1
                add += arr[r-j1][c-i1]
                i1 += 1
                j1 += 1
            while c - i2 >= 0 and r + j2 < N:
                add += arr[r + j2][c-i2]
                i2 += 1
                j2 += 1
            while c + i3 < N and r - j3 >= 0:
                add += arr[r-j3][c+i3]
                i3 += 1
                j3 += 1
            while c + i4 < N and r + j4 < N:
                add += arr[r+j4][c+i4]
                i4 += 1
                j4 += 1
            if add > max_num:
                max_num = add
    print(f'#{tc} {max_num}')

