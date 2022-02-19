import sys ; sys.stdin = open('10989.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    add = 0
    for _ in range(M):
        row, col, power = map(int, input().split())
        for i in range(row-power, row + power + 1): # y축 더하기
            if 0 <= i < N:
                add += arr[i][col]
                arr[i][col] = 0

        for j in range(col - power, col + power + 1): # x축 더하기
            if 0 <= j < N:
                add += arr[row][j]
                arr[row][j] = 0

    print(f'#{tc} {add}')