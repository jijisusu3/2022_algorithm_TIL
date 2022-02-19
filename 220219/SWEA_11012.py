import sys;

sys.stdin = open('11012.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    add = 0
    for _ in range(M):
        row, col, width = map(int, input().split())
        for i in range(width):
            for j in range(width):
                if row + i < N and col + j < N:
                    add += arr[row+i][col+j]
                    arr[row+i][col+j] = 0
    print(f'#{tc} {add}')
