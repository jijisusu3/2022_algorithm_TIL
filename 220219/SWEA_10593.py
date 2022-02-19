import sys;

sys.stdin = open('10593.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    max_num = 0
    row = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        add_row = sum(arr[r])
        for c in range(N):
            add_col = 0
            for i in range(N):
                add_col += arr[i][c]
            if add_row + add_col - arr[r][c] > max_num:
                max_num = add_row + add_col - arr[r][c]
    print(f'#{tc} {max_num}')

